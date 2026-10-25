import fs from 'fs';
import https from 'https';

const BUFFER_ACCESS_TOKEN = process.env.BUFFER_ACCESS_TOKEN || 'uR7DeyYk4O9VcFHqPQOnWseUl7BONqA8RZ4CK_03Ci0';
const LINKEDIN_CHANNEL_ID = '6a39d30c5ab6d2f1065f5301';

const REQUIRED_ASSETS = [
  'https://lornettedaye.com/campaigns/oilers/nuge-is-back-poster.png',
  'https://lornettedaye.com/campaigns/oilers/nuge-one-shot-poster.png',
  'https://lornettedaye.com/campaigns/oilers/nuge-shootout-hero-poster.png'
];

function probeUrl(url) {
  return new Promise((resolve) => {
    https.get(url, (res) => {
      resolve({ url, status: res.statusCode });
    }).on('error', (e) => {
      resolve({ url, status: 500, error: e.message });
    });
  });
}

function bufferGraphQL(query, variables) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify({ query, variables });
    const req = https.request('https://api.buffer.com', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${BUFFER_ACCESS_TOKEN}`,
        'Content-Length': Buffer.byteLength(data),
        'User-Agent': 'Mozilla/5.0'
      }
    }, (res) => {
      let body = '';
      res.on('data', chunk => body += chunk);
      res.on('end', () => {
        try {
          const parsed = JSON.parse(body);
          resolve(parsed);
        } catch (e) {
          reject(new Error(`Failed to parse response: ${body}`));
        }
      });
    });
    req.on('error', reject);
    req.write(data);
    req.end();
  });
}

async function main() {
  console.log('=== Pre-Flight HTTP 200 Probes ===');
  let allLive = true;
  for (const url of REQUIRED_ASSETS) {
    const res = await probeUrl(url);
    console.log(`[PROBE] ${res.status === 200 ? 'SUCCESS' : 'WAITING'} HTTP ${res.status}: ${url}`);
    if (res.status !== 200) allLive = false;
  }

  if (!allLive) {
    console.log('Not all production assets returned HTTP 200 yet. Wait for Vercel deployment to finish.');
    process.exit(2);
  }

  console.log('\n=== Loading 14-Post Campaign Data ===');
  const posts = JSON.parse(fs.readFileSync('scripts/oilers-14day-data.json', 'utf8'));
  console.log(`Loaded ${posts.length} posts.`);

  // Load or initialize report
  let report = [];
  if (fs.existsSync('scripts/oilers-14day-report.json')) {
    report = JSON.parse(fs.readFileSync('scripts/oilers-14day-report.json', 'utf8'));
  }

  const CREATE_POST_MUTATION = `
    mutation CreatePost($input: CreatePostInput!) {
      createPost(input: $input) {
        __typename
        ... on PostActionSuccess {
          post {
            id
            text
            status
            shareMode
            dueAt
            sentAt
            channelService
          }
        }
        ... on NotFoundError {
          message
        }
        ... on UnauthorizedError {
          message
        }
        ... on UnexpectedError {
          message
        }
        ... on LimitReachedError {
          message
        }
        ... on InvalidInputError {
          message
        }
      }
    }
  `;

  for (const post of posts) {
    // Check if already posted/scheduled successfully
    const existing = report.find(r => r.day === post.day && r.status === 'SUCCESS');
    if (existing) {
      console.log(`[SKIP] Day ${post.day} already processed (Buffer ID: ${existing.bufferPostId})`);
      continue;
    }

    console.log(`\n--- Processing Day ${post.day}: ${post.title} ---`);
    console.log(`Mode: ${post.isLiveNow ? 'LIVE IMMEDIATELY (shareNow)' : 'SCHEDULED at ' + post.scheduledAt}`);

    const input = {
      channelId: LINKEDIN_CHANNEL_ID,
      text: post.caption,
      mode: post.isLiveNow ? 'shareNow' : 'customScheduled',
      schedulingType: 'automatic',
      needsApproval: false,
      saveToDraft: false,
      assets: [
        {
          image: {
            url: post.assetUrl
          }
        }
      ],
      ...(post.scheduledAt ? { dueAt: post.scheduledAt } : {})
    };

    try {
      const response = await bufferGraphQL(CREATE_POST_MUTATION, { input });
      const result = response.data?.createPost;

      if (result?.post?.id) {
        console.log(`[SUCCESS] Day ${post.day} dispatched! Buffer ID: ${result.post.id}, Status: ${result.post.status}, DueAt: ${result.post.dueAt || 'LIVE'}`);
        report.push({
          day: post.day,
          title: post.title,
          date: post.date,
          status: 'SUCCESS',
          bufferPostId: result.post.id,
          postStatus: result.post.status,
          shareMode: result.post.shareMode,
          dueAt: result.post.dueAt || 'LIVE_NOW',
          assetUrl: post.assetUrl
        });
      } else {
        console.error(`[ERROR] Day ${post.day} failed:`, result?.message || JSON.stringify(response));
        report.push({
          day: post.day,
          title: post.title,
          date: post.date,
          status: 'ERROR',
          error: result?.message || JSON.stringify(response)
        });
      }
    } catch (err) {
      console.error(`[EXCEPTION] Day ${post.day}:`, err.message);
      report.push({
        day: post.day,
        title: post.title,
        date: post.date,
        status: 'EXCEPTION',
        error: err.message
      });
    }

    fs.writeFileSync('scripts/oilers-14day-report.json', JSON.stringify(report, null, 2));
    // polite pacing between Buffer calls
    await new Promise(r => setTimeout(r, 1500));
  }

  console.log('\n=== Campaign Processing Complete ===');
  console.log(`Processed ${report.length} entries.`);
}

main().catch(console.error);
