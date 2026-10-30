/**
 * scripts/scrub-buffer-day-tags.mjs
 * 
 * Genuine production scrubber for Buffer scheduled posts on channel 6a39d30c5ab6d2f1065f5301.
 * Fetches all scheduled posts, cleans bracketed day tags from headlines via editPost mutation,
 * enforces Invariant Rules 7 & 9, and runs post-scrub live verification over scheduled and draft posts.
 */

import fs from 'node:fs';
import path from 'node:path';

const TOKEN = process.env.BUFFER_ACCESS_TOKEN || 'uR7DeyYk4O9VcFHqPQOnWseUl7BONqA8RZ4CK_03Ci0';
const ORG_ID = '6a39d1c13585011445b875dc';
const CHAN_ID = '6a39d30c5ab6d2f1065f5301';
const BUFFER_API_URL = 'https://api.buffer.com';

export const METADATA_TAG_REGEX = /[\(\[]\s*(?:DAY\b|SLOT\b|POST\b|WAVE\b)[^\]\)]*[\)\]]/i;

export function cleanPostText(text) {
  if (!text || typeof text !== 'string') return text;

  let cleaned = text;

  // 1. Tag followed by a colon: e.g. "PREFIX [Day 1]: SUFFIX" -> "PREFIX: SUFFIX"
  cleaned = cleaned.replace(/:\s*[\(\[]\s*DAY\s*\d+[^\]\)]*[\)\]]\s*:\s*/gi, ': ');
  cleaned = cleaned.replace(/\s*[\(\[]\s*DAY\s*\d+[^\]\)]*[\)\]]\s*:\s*/gi, ': ');

  // 2. Tag at start of string or line: e.g. "[Day 1] TITLE" -> "TITLE"
  cleaned = cleaned.replace(/^[\(\[]\s*DAY\s*\d+[^\]\)]*[\)\]]\s*[:-]?\s*/gim, '');

  // 3. Trailing or embedded bracketed day tag: e.g. "TITLE (DAY 28 - EVENING)" -> "TITLE"
  cleaned = cleaned.replace(/\s*[\(\[]\s*DAY\s*\d+[^\]\)]*[\)\]]/gi, '');

  // 4. Line-by-line whitespace normalization: trim trailing space, collapse internal multi-spaces
  cleaned = cleaned.split('\n').map(line => {
    return line.replace(/[ \t]{2,}/g, ' ').trimEnd();
  }).join('\n');

  // 5. Paragraph structure preservation: normalize excessive consecutive newlines to double newline
  cleaned = cleaned.replace(/\n{3,}/g, '\n\n').trim();

  return cleaned;
}

async function bufferGraphQL(query, variables = {}, retries = 3) {
  for (let attempt = 1; attempt <= retries; attempt++) {
    const res = await fetch(BUFFER_API_URL, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${TOKEN}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ query, variables })
    });

    if (res.status === 429) {
      const retryAfter = parseInt(res.headers.get('retry-after') || '30', 10);
      console.warn(`[HTTP 429] Rate limit hit. Pausing for ${retryAfter}s (attempt ${attempt}/${retries})...`);
      await new Promise(r => setTimeout(r, (retryAfter + 1) * 1000));
      continue;
    }

    const json = await res.json();
    if (json.errors && json.errors.length > 0) {
      throw new Error(`Buffer GraphQL Error: ${JSON.stringify(json.errors, null, 2)}`);
    }
    return json.data;
  }
  throw new Error(`Exceeded max retries for GraphQL request`);
}

const GET_POSTS_QUERY = `
  query GetPosts($input: PostsInput!, $first: Int, $after: String) {
    posts(input: $input, first: $first, after: $after) {
      pageInfo {
        hasNextPage
        endCursor
      }
      edges {
        node {
          id
          status
          text
          dueAt
          shareMode
          channelId
          createdAt
          assets {
            id
            type
            source
            thumbnail
          }
        }
      }
    }
  }
`;

const EDIT_POST_MUTATION = `
  mutation EditPost($input: EditPostInput!) {
    editPost(input: $input) {
      __typename
      ... on PostActionSuccess {
        post {
          id
          status
          dueAt
          text
        }
      }
      ... on InvalidInputError { message }
      ... on NotFoundError { message }
      ... on LimitReachedError { message }
      ... on UnexpectedError { message }
      ... on UnauthorizedError { message }
    }
  }
`;

async function fetchAllPostsByStatus(status) {
  let hasNext = true;
  let cursor = null;
  const allPosts = [];
  let page = 0;

  while (hasNext) {
    page++;
    const data = await bufferGraphQL(GET_POSTS_QUERY, {
      input: {
        organizationId: ORG_ID,
        filter: {
          channelIds: [CHAN_ID],
          status: [status]
        }
      },
      first: 50,
      after: cursor
    });

    const postsData = data?.posts;
    const edges = postsData?.edges || [];
    for (const e of edges) {
      allPosts.push(e.node);
    }

    hasNext = postsData?.pageInfo?.hasNextPage;
    cursor = postsData?.pageInfo?.endCursor;
    process.stdout.write(`Fetching ${status} posts: page ${page} (${allPosts.length} collected)...\r`);
  }
  console.log(`\nCollected ${allPosts.length} total ${status} posts.`);
  return allPosts;
}

async function scrubPosts() {
  console.log('================================================================');
  console.log('🚀 STARTING BUFFER SCHEDULED POSTS SCRUBBING OPERATION');
  console.log('================================================================');
  console.log(`Target Channel: ${CHAN_ID}`);
  console.log(`Organization ID: ${ORG_ID}\n`);

  console.log('Step 1: Fetching all current scheduled posts from Buffer...');
  const scheduled = await fetchAllPostsByStatus('scheduled');

  const taggedPosts = scheduled.filter(p => METADATA_TAG_REGEX.test(p.text || ''));
  console.log(`\nTotal scheduled posts scanned: ${scheduled.length}`);
  console.log(`Scheduled posts containing bracketed day tags: ${taggedPosts.length}`);

  if (taggedPosts.length === 0) {
    console.log('✅ No scheduled posts contain bracketed day tags. Everything is clean!');
  }

  const logEntries = [];
  let updatedCount = 0;
  let failedCount = 0;

  console.log(`\nStep 2: Executing editPost mutations for ${taggedPosts.length} tagged posts (pacing 400ms)...`);

  for (let i = 0; i < taggedPosts.length; i++) {
    const post = taggedPosts[i];
    const originalText = post.text;
    const originalFirstLine = originalText.split('\n')[0];
    const cleanText = cleanPostText(originalText);
    const cleanFirstLine = cleanText.split('\n')[0];

    // Assert cleanText adheres to Invariants
    if (METADATA_TAG_REGEX.test(cleanText)) {
      throw new Error(`CRITICAL: cleanPostText failed to remove tag for post ${post.id}: "${cleanFirstLine}"`);
    }
    if (cleanText.includes('*')) {
      throw new Error(`CRITICAL: cleanText contains asterisk for post ${post.id}`);
    }

    process.stdout.write(`[${i + 1}/${taggedPosts.length}] Updating ${post.id} (Due: ${post.dueAt})...\r`);

    try {
      const data = await bufferGraphQL(EDIT_POST_MUTATION, {
        input: {
          id: post.id,
          text: cleanText
        }
      });

      const result = data?.editPost;
      if (result?.__typename === 'PostActionSuccess' && result.post) {
        updatedCount++;
        logEntries.push({
          index: i + 1,
          id: post.id,
          dueAt: post.dueAt,
          status: 'SUCCESS',
          originalFirstLine,
          cleanedFirstLine: cleanFirstLine,
          updatedAt: new Date().toISOString()
        });
      } else {
        failedCount++;
        console.error(`\n❌ Failed to update post ${post.id}:`, result);
        logEntries.push({
          index: i + 1,
          id: post.id,
          dueAt: post.dueAt,
          status: 'FAILED',
          error: result,
          originalFirstLine
        });
      }
    } catch (err) {
      failedCount++;
      console.error(`\n❌ Exception updating post ${post.id}:`, err.message);
      logEntries.push({
        index: i + 1,
        id: post.id,
        dueAt: post.dueAt,
        status: 'EXCEPTION',
        error: err.message,
        originalFirstLine
      });
    }

    // Pacing delay (400ms)
    await new Promise(r => setTimeout(r, 400));
  }

  console.log(`\n\nScrubbing Finished: ${updatedCount} successfully updated, ${failedCount} failures.`);

  // Save log
  const logFilePath = path.join(process.cwd(), '.agents', 'teamwork', 'worker_scrub_1', 'scrub_execution_log.json');
  fs.writeFileSync(logFilePath, JSON.stringify({
    timestamp: new Date().toISOString(),
    channelId: CHAN_ID,
    totalTargeted: taggedPosts.length,
    updatedCount,
    failedCount,
    logEntries
  }, null, 2), 'utf8');
  console.log(`Execution log saved to: ${logFilePath}`);

  // Step 3: Run Live Post-Scrub Verification
  console.log('\n================================================================');
  console.log('🔍 RUNNING LIVE BUFFER POST-SCRUB VERIFICATION QUERY');
  console.log('================================================================\n');

  console.log('Querying all scheduled posts on channel...');
  const postVerificationScheduled = await fetchAllPostsByStatus('scheduled');
  const postVerificationScheduledTagged = postVerificationScheduled.filter(p => METADATA_TAG_REGEX.test(p.text || ''));

  console.log('\nQuerying all draft posts on channel...');
  const postVerificationDrafts = await fetchAllPostsByStatus('draft');
  const postVerificationDraftsTagged = postVerificationDrafts.filter(p => METADATA_TAG_REGEX.test(p.text || ''));

  console.log('\n--- VERIFICATION RESULTS ---');
  console.log(`Total Scheduled Posts in Buffer: ${postVerificationScheduled.length}`);
  console.log(`Scheduled Posts with Bracketed Day Tags: ${postVerificationScheduledTagged.length} (Target: 0)`);
  console.log(`Total Draft Posts in Buffer: ${postVerificationDrafts.length}`);
  console.log(`Draft Posts with Bracketed Day Tags: ${postVerificationDraftsTagged.length} (Target: 0)`);

  const verificationSuccess = (postVerificationScheduledTagged.length === 0 && postVerificationDraftsTagged.length === 0);

  const verificationReport = {
    timestamp: new Date().toISOString(),
    channelId: CHAN_ID,
    organizationId: ORG_ID,
    totalScheduledPosts: postVerificationScheduled.length,
    scheduledPostsWithTags: postVerificationScheduledTagged.length,
    totalDraftPosts: postVerificationDrafts.length,
    draftPostsWithTags: postVerificationDraftsTagged.length,
    verificationStatus: verificationSuccess ? 'PASSED_100_PERCENT_CLEAN' : 'FAILED',
    taggedScheduledPostsRemaining: postVerificationScheduledTagged.map(p => ({
      id: p.id,
      dueAt: p.dueAt,
      firstLine: (p.text || '').split('\n')[0]
    }))
  };

  const verReportPath = path.join(process.cwd(), '.agents', 'teamwork', 'worker_scrub_1', 'verification_report.json');
  fs.writeFileSync(verReportPath, JSON.stringify(verificationReport, null, 2), 'utf8');
  console.log(`Verification report written to: ${verReportPath}`);

  if (verificationSuccess) {
    console.log('\n🎉 ALL SCHEDULED POSTS AND DRAFTS ARE 100% CLEAN OF BRACKETED DAY TAGS!');
  } else {
    console.error('\n⚠️ VERIFICATION FAILURE: Some posts still contain bracketed day tags.');
    process.exit(1);
  }
}

if (process.argv[1]?.endsWith('scrub-buffer-day-tags.mjs') || process.argv[1]?.endsWith('scrub-buffer-day-tags')) {
  scrubPosts().catch(err => {
    console.error('Fatal error during scrubbing:', err);
    process.exit(1);
  });
}
