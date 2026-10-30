/**
 * scripts/verify-buffer-integrity.mjs
 * 
 * Independent Empirical Verification Harness by Challenger 2
 * 
 * Directly queries Buffer GraphQL API (channel 6a39d30c5ab6d2f1065f5301)
 * across ALL scheduled posts and drafts.
 * Scans ALL 101 JSON files in scripts/.
 * Cross-references the 148 scrubbed post IDs.
 * Audits formatting: trailing whitespace, orphan colons, paragraph integrity.
 */

import fs from 'node:fs';
import path from 'node:path';

const BUFFER_ACCESS_TOKEN = process.env.BUFFER_ACCESS_TOKEN || 'uR7DeyYk4O9VcFHqPQOnWseUl7BONqA8RZ4CK_03Ci0';
const ORG_ID = '6a39d1c13585011445b875dc';
const CHAN_ID = '6a39d30c5ab6d2f1065f5301';
const BUFFER_API_URL = 'https://api.buffer.com';

const METADATA_TAG_REGEX = /[\(\[]\s*(?:DAY\b|SLOT\b|POST\b|WAVE\b)[^\]\)]*[\)\]]/i;
const BROADER_METADATA_REGEX = /[\(\[]\s*(?:DAY|SLOT|POST|WAVE)\b[^\]\)]*[\)\]]/i;

async function bufferGraphQL(query, variables = {}, retries = 5) {
  for (let attempt = 1; attempt <= retries; attempt++) {
    try {
      const res = await fetch(BUFFER_API_URL, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${BUFFER_ACCESS_TOKEN}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query, variables })
      });

      if (res.status === 429) {
        const retryAfter = parseInt(res.headers.get('retry-after') || '20', 10);
        console.warn(`[HTTP 429] Rate limit hit. Waiting ${retryAfter}s (attempt ${attempt}/${retries})...`);
        await new Promise(r => setTimeout(r, (retryAfter + 1) * 1000));
        continue;
      }

      if (!res.ok) {
        throw new Error(`HTTP ${res.status}: ${res.statusText}`);
      }

      const json = await res.json();
      if (json.errors && json.errors.length > 0) {
        throw new Error(`Buffer GraphQL Error: ${JSON.stringify(json.errors, null, 2)}`);
      }
      return json.data;
    } catch (err) {
      if (attempt === retries) throw err;
      console.warn(`[GraphQL Attempt ${attempt} failed: ${err.message}. Retrying in 2s...]`);
      await new Promise(r => setTimeout(r, 2000));
    }
  }
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
        }
      }
    }
  }
`;

async function fetchAllPosts(status) {
  let hasNext = true;
  let cursor = null;
  const posts = [];
  let page = 0;

  console.log(`[Buffer Query] Starting paginated query for status="${status}"...`);
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

    const pageData = data?.posts;
    const edges = pageData?.edges || [];
    for (const edge of edges) {
      posts.push(edge.node);
    }

    hasNext = pageData?.pageInfo?.hasNextPage;
    cursor = pageData?.pageInfo?.endCursor;
    console.log(`  Page ${page}: fetched ${edges.length} posts (cumulative: ${posts.length}, hasNext: ${hasNext})`);
  }
  console.log(`[Buffer Query] Total ${status} posts retrieved: ${posts.length}\n`);
  return posts;
}

async function runIntegrityAudit() {
  const auditResults = {
    timestamp: new Date().toISOString(),
    channelId: CHAN_ID,
    organizationId: ORG_ID,
    step1_bufferScheduled: {},
    step2_bufferDrafts: {},
    step3_scrubbed148PostsAudit: {},
    step4_localJsonFilesScan: {},
    step5_preflightRegexStressTest: {},
    overallVerdict: 'PENDING'
  };

  console.log('========================================================================');
  console.log('🔍 CHALLENGER 2: ADVERSARIAL EMPIRICAL INTEGRITY AUDIT');
  console.log('========================================================================\n');

  // STEP 1: Query All Buffer Scheduled Posts
  console.log('--- STEP 1: AUDITING LIVE BUFFER SCHEDULED POSTS ---');
  const scheduledPosts = await fetchAllPosts('scheduled');
  
  const scheduledViolations = [];
  const asteriskViolations = [];
  const formattingIssues = [];

  for (let i = 0; i < scheduledPosts.length; i++) {
    const post = scheduledPosts[i];
    const text = post.text || '';
    const firstLine = text.split('\n')[0] || '';

    // Regex Check 1: Rule 9 standard regex
    const match = text.match(METADATA_TAG_REGEX);
    if (match) {
      scheduledViolations.push({
        id: post.id,
        dueAt: post.dueAt,
        type: 'RULE_9_MATCH',
        match: match[0],
        firstLine
      });
    }

    // Regex Check 2: Broader metadata regex
    const broaderMatch = text.match(BROADER_METADATA_REGEX);
    if (broaderMatch && !match) {
      scheduledViolations.push({
        id: post.id,
        dueAt: post.dueAt,
        type: 'BROADER_METADATA_MATCH',
        match: broaderMatch[0],
        firstLine
      });
    }

    // Rule 7 Check: Asterisk
    if (text.includes('*')) {
      asteriskViolations.push({
        id: post.id,
        dueAt: post.dueAt,
        firstLine
      });
    }

    // Formatting Checks on First Line (Headline)
    if (/[ \t]+$/.test(firstLine)) {
      formattingIssues.push({
        id: post.id,
        type: 'TRAILING_WHITESPACE',
        firstLine
      });
    }
    if (/(?::|-|–)\s*$/.test(firstLine)) {
      formattingIssues.push({
        id: post.id,
        type: 'ORPHAN_TRAILING_PUNCTUATION',
        firstLine
      });
    }
    if ((firstLine.match(/\(/g) || []).length !== (firstLine.match(/\)/g) || []).length) {
      formattingIssues.push({
        id: post.id,
        type: 'UNBALANCED_PARENTHESES',
        firstLine
      });
    }
    if ((firstLine.match(/\[/g) || []).length !== (firstLine.match(/\]/g) || []).length) {
      formattingIssues.push({
        id: post.id,
        type: 'UNBALANCED_BRACKETS',
        firstLine
      });
    }
  }

  auditResults.step1_bufferScheduled = {
    totalScheduledPostsScanned: scheduledPosts.length,
    bracketedTagViolationsCount: scheduledViolations.length,
    bracketedTagViolations: scheduledViolations,
    asteriskViolationsCount: asteriskViolations.length,
    asteriskViolations: asteriskViolations,
    formattingIssuesCount: formattingIssues.length,
    formattingIssues: formattingIssues.slice(0, 10), // sample if any
  };

  console.log(`Total scheduled posts scanned: ${scheduledPosts.length}`);
  console.log(`Bracketed day/metadata tag violations: ${scheduledViolations.length} (Target: 0)`);
  console.log(`Asterisk violations: ${asteriskViolations.length} (Target: 0)`);
  console.log(`Headline formatting issues: ${formattingIssues.length} (Target: 0)`);

  // STEP 2: Query All Buffer Draft Posts
  console.log('\n--- STEP 2: AUDITING LIVE BUFFER DRAFT POSTS ---');
  const draftPosts = await fetchAllPosts('draft');
  const draftViolations = [];

  for (const draft of draftPosts) {
    const text = draft.text || '';
    const match = text.match(METADATA_TAG_REGEX) || text.match(BROADER_METADATA_REGEX);
    if (match) {
      draftViolations.push({
        id: draft.id,
        match: match[0],
        firstLine: text.split('\n')[0]
      });
    }
  }

  auditResults.step2_bufferDrafts = {
    totalDraftPostsScanned: draftPosts.length,
    bracketedTagViolationsCount: draftViolations.length,
    bracketedTagViolations: draftViolations
  };

  console.log(`Total draft posts scanned: ${draftPosts.length}`);
  console.log(`Draft bracketed day tag violations: ${draftViolations.length} (Target: 0)`);

  // STEP 3: Cross-Reference 148 Scrubbed Posts
  console.log('\n--- STEP 3: CROSS-REFERENCING THE 148 SCRUBBED POSTS ---');
  const scrubLogPath = path.join(process.cwd(), '.agents', 'teamwork', 'worker_scrub_1', 'scrub_execution_log.json');
  let scrubLog = null;
  const scrubAuditDetails = {
    logFileExists: false,
    expectedPostCount: 148,
    matchedLiveCount: 0,
    missingLiveCount: 0,
    mismatchedTextCount: 0,
    cleanFormattingVerifiedCount: 0,
    samples: []
  };

  if (fs.existsSync(scrubLogPath)) {
    scrubAuditDetails.logFileExists = true;
    scrubLog = JSON.parse(fs.readFileSync(scrubLogPath, 'utf8'));
    const logEntries = scrubLog.logEntries || [];
    scrubAuditDetails.expectedPostCount = logEntries.length;

    const scheduledMap = new Map(scheduledPosts.map(p => [p.id, p]));

    for (const entry of logEntries) {
      const livePost = scheduledMap.get(entry.id);
      if (!livePost) {
        scrubAuditDetails.missingLiveCount++;
        continue;
      }
      scrubAuditDetails.matchedLiveCount++;

      const liveFirstLine = (livePost.text || '').split('\n')[0];
      if (liveFirstLine !== entry.cleanedFirstLine) {
        scrubAuditDetails.mismatchedTextCount++;
      }

      // Check formatting of this specific post
      const isClean = !/[ \t]+$/.test(liveFirstLine) &&
                      !/(?::|-|–)\s*$/.test(liveFirstLine) &&
                      !METADATA_TAG_REGEX.test(livePost.text);

      if (isClean) {
        scrubAuditDetails.cleanFormattingVerifiedCount++;
      }

      if (scrubAuditDetails.samples.length < 5) {
        scrubAuditDetails.samples.push({
          id: entry.id,
          dueAt: entry.dueAt,
          originalFirstLine: entry.originalFirstLine,
          cleanedFirstLine: entry.cleanedFirstLine,
          liveFirstLine,
          verifiedMatch: liveFirstLine === entry.cleanedFirstLine
        });
      }
    }
  }

  auditResults.step3_scrubbed148PostsAudit = scrubAuditDetails;
  console.log(`Scrub log found: ${scrubAuditDetails.logFileExists}`);
  console.log(`Expected posts in log: ${scrubAuditDetails.expectedPostCount}`);
  console.log(`Matched in live Buffer schedule: ${scrubAuditDetails.matchedLiveCount}/${scrubAuditDetails.expectedPostCount}`);
  console.log(`Mismatched first line text: ${scrubAuditDetails.mismatchedTextCount} (Target: 0)`);
  console.log(`Clean formatting verified: ${scrubAuditDetails.cleanFormattingVerifiedCount}/${scrubAuditDetails.matchedLiveCount}`);

  // STEP 4: Scan All JSON Files in scripts/
  console.log('\n--- STEP 4: SCANNING ALL JSON FILES IN scripts/ ---');
  const scriptsDir = path.join(process.cwd(), 'scripts');
  const allJsonFiles = fs.readdirSync(scriptsDir).filter(f => f.endsWith('.json'));

  const jsonScanResults = {
    totalJsonFilesScanned: allJsonFiles.length,
    filesWithViolations: [],
    keyFilesAudited: {}
  };

  const keyFiles = [
    'master-campaign-queue.json',
    'campaign-manifest.json',
    'scheduled-master-report.json',
    'dawn-staley-scheduled-report.json',
    'como-scheduled-report.json',
    'superpowers-scheduled-report.json'
  ];

  for (const filename of allJsonFiles) {
    const filePath = path.join(scriptsDir, filename);
    const content = fs.readFileSync(filePath, 'utf8');

    const matches = content.match(new RegExp(METADATA_TAG_REGEX.source, 'gi'));
    if (matches && matches.length > 0) {
      jsonScanResults.filesWithViolations.push({
        file: filename,
        matchCount: matches.length,
        samples: matches.slice(0, 5)
      });
    }

    if (keyFiles.includes(filename)) {
      jsonScanResults.keyFilesAudited[filename] = {
        sizeBytes: content.length,
        violations: matches ? matches.length : 0
      };
    }
  }

  auditResults.step4_localJsonFilesScan = jsonScanResults;
  console.log(`Total JSON files scanned in scripts/: ${jsonScanResults.totalJsonFilesScanned}`);
  console.log(`Files with bracketed tag violations: ${jsonScanResults.filesWithViolations.length} (Target: 0)`);
  for (const kf of Object.keys(jsonScanResults.keyFilesAudited)) {
    console.log(`  - ${kf}: ${jsonScanResults.keyFilesAudited[kf].violations} violations (bytes: ${jsonScanResults.keyFilesAudited[kf].sizeBytes})`);
  }

  // STEP 5: Stress-Test Regex and Pre-Flight Assertions
  console.log('\n--- STEP 5: STRESS-TESTING METADATA_TAG_REGEX ---');
  const adversarialCases = [
    // True positives (MUST MATCH)
    { input: 'HEADLINE (DAY 8 - MORNING)', expected: true, label: 'Standard (DAY 8 - MORNING)' },
    { input: 'HEADLINE (DAY 28)', expected: true, label: 'Standard (DAY 28)' },
    { input: 'HEADLINE [Day 1]', expected: true, label: 'Square bracket [Day 1]' },
    { input: 'HEADLINE [DAY 14 - MIDDAY]', expected: true, label: 'Square bracket [DAY 14 - MIDDAY]' },
    { input: 'HEADLINE (day 5 - evening)', expected: true, label: 'Lowercase (day 5 - evening)' },
    { input: 'HEADLINE [SLOT 1]', expected: true, label: 'Slot tag [SLOT 1]' },
    { input: 'HEADLINE (SLOT: MORNING)', expected: true, label: 'Slot tag (SLOT: MORNING)' },
    { input: 'HEADLINE [POST 12]', expected: true, label: 'Post tag [POST 12]' },
    { input: 'HEADLINE [WAVE 3]', expected: true, label: 'Wave tag [WAVE 3]' },
    { input: 'HEADLINE (  DAY 9  )', expected: true, label: 'Padded whitespace (  DAY 9  )' },
    { input: 'HEADLINE [DAY 10: MORNING]', expected: true, label: 'Colon within bracket [DAY 10: MORNING]' },
    
    // True negatives (MUST NOT MATCH)
    { input: 'SERIE A LEADERSHIP: THE COMO (1907) BLUEPRINT', expected: false, label: 'Year in parenthesis (1907)' },
    { input: 'Finish Strong: Chasing the Olympic Dream ($14.99 CAD)', expected: false, label: 'Currency ($14.99 CAD)' },
    { input: 'Friday 6:30 AM MDT (Sep 25, 2026)', expected: false, label: 'Date/time (Sep 25, 2026)' },
    { input: 'A NEW DAY FOR ATHLETES EVERYWHERE', expected: false, label: 'Word "DAY" without brackets' },
    { input: 'DISCIPLINE TODAY BREEDS VICTORY TOMORROW', expected: false, label: 'Word "TODAY"' },
    { input: 'Better People, Better Players.', expected: false, label: 'Standard text' },
  ];

  let stressTestFailures = 0;
  const stressResults = [];
  for (const tc of adversarialCases) {
    const matched = METADATA_TAG_REGEX.test(tc.input);
    const passed = (matched === tc.expected);
    if (!passed) stressTestFailures++;
    stressResults.push({
      label: tc.label,
      input: tc.input,
      expected: tc.expected,
      actual: matched,
      passed
    });
  }

  auditResults.step5_preflightRegexStressTest = {
    totalCases: adversarialCases.length,
    passedCases: adversarialCases.length - stressTestFailures,
    failedCases: stressTestFailures,
    results: stressResults
  };
  console.log(`Adversarial test cases: ${adversarialCases.length}`);
  console.log(`Passed: ${adversarialCases.length - stressTestFailures}, Failed: ${stressTestFailures}`);

  // OVERALL VERDICT DETERMINATION
  const isBufferScheduledClean = (scheduledViolations.length === 0);
  const isBufferDraftsClean = (draftViolations.length === 0);
  const isLocalJsonClean = (jsonScanResults.filesWithViolations.length === 0);
  const isScrubbed148Clean = (scrubAuditDetails.mismatchedTextCount === 0 && scrubAuditDetails.matchedLiveCount === 148);
  const isStressTestPassing = (stressTestFailures === 0);

  const verdictApproved = isBufferScheduledClean &&
                          isBufferDraftsClean &&
                          isLocalJsonClean &&
                          isScrubbed148Clean &&
                          isStressTestPassing;

  auditResults.overallVerdict = verdictApproved ? 'APPROVE' : 'REJECT';

  console.log('\n========================================================================');
  console.log(`🏁 FINAL VERDICT: ${auditResults.overallVerdict}`);
  console.log('========================================================================');
  console.log(`- Buffer Scheduled Posts Clean (0 violations): ${isBufferScheduledClean ? 'PASS' : 'FAIL'}`);
  console.log(`- Buffer Draft Posts Clean (0 violations): ${isBufferDraftsClean ? 'PASS' : 'FAIL'}`);
  console.log(`- Local JSON Queues Clean (0 violations in 101 files): ${isLocalJsonClean ? 'PASS' : 'FAIL'}`);
  console.log(`- 148 Scrubbed Posts Verified in Live State: ${isScrubbed148Clean ? 'PASS' : 'FAIL'}`);
  console.log(`- Regex Guard Stress-Test: ${isStressTestPassing ? 'PASS' : 'FAIL'}`);

  // Write audit results JSON
  const auditJsonPath = path.join(process.cwd(), 'scripts', 'challenger_buffer_integrity_audit.json');
  fs.writeFileSync(auditJsonPath, JSON.stringify(auditResults, null, 2), 'utf8');
  console.log(`\nAudit results written to: ${auditJsonPath}`);

  return auditResults;
}

runIntegrityAudit().catch(err => {
  console.error('Fatal audit failure:', err);
  process.exit(1);
});
