import fs from 'fs';
import https from 'https';

const BUFFER_ACCESS_TOKEN = process.env.BUFFER_ACCESS_TOKEN || 'uR7DeyYk4O9VcFHqPQOnWseUl7BONqA8RZ4CK_03Ci0';
const LINKEDIN_CHANNEL_ID = '6a39d30c5ab6d2f1065f5301';

const MASTER_QUEUE_FILE = 'scripts/master-foundations-umattr-queue.json';
const REPORT_FILE = 'scripts/scheduled-foundations-umattr-report.json';

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

async function main() {
  const isCatchup = process.argv.includes('--catchup');
  const isReplenish = process.argv.includes('--replenish');

  console.log('===============================================================');
  console.log(`LD x UMATTR 90-Day Campaign Scheduler (Mode: ${isCatchup ? 'CATCHUP' : isReplenish ? 'REPLENISH' : 'STANDARD'})`);
  console.log('===============================================================\n');

  // Verify master queue exists
  if (!fs.existsSync(MASTER_QUEUE_FILE)) {
    console.error(`Master queue not found at ${MASTER_QUEUE_FILE}. Run generator first.`);
    process.exit(1);
  }

  const posts = JSON.parse(fs.readFileSync(MASTER_QUEUE_FILE, 'utf8'));
  console.log(`Loaded ${posts.length} posts from master queue.`);

  // Load persistent report
  let report = [];
  if (fs.existsSync(REPORT_FILE)) {
    try {
      report = JSON.parse(fs.readFileSync(REPORT_FILE, 'utf8'));
    } catch (e) {
      report = [];
    }
  }
  console.log(`Existing report entries: ${report.length} (Successfully scheduled: ${report.filter(r => r.status === 'SUCCESS').length})`);

  // Pre-flight check on unique asset URLs
  console.log('\n--- Pre-Flight HTTP 200 Asset Verification ---');
  const sampleAssets = [
    'https://lornettedaye.com/campaigns/foundations-sports/sports-01.png',
    'https://lornettedaye.com/campaigns/foundations-sports/sports-10.png',
    'https://lornettedaye.com/campaigns/foundations-sports/sports-20.png'
  ];

  let assetsReady = true;
  for (const url of sampleAssets) {
    const res = await probeUrl(url);
    console.log(`[PROBE] ${res.status === 200 ? 'SUCCESS' : 'WAITING'} HTTP ${res.status}: ${url}`);
    if (res.status !== 200) assetsReady = false;
  }

  if (!assetsReady) {
    console.log('\nProduction assets not yet live on CDN. Waiting for Vercel deployment.');
    process.exit(2);
  }

  console.log('\n--- Processing Campaign Queue into Buffer ---');
  let scheduledThisRun = 0;
  let queueFull = false;

  for (const post of posts) {
    if (queueFull) break;

    // Check if already scheduled
    const existing = report.find(r => r.id === post.id && r.status === 'SUCCESS');
    if (existing) {
      continue;
    }

    console.log(`\n[Queue #${post.id}/360] Day ${post.day} (${post.slot}): ${post.topic}`);
    console.log(`Due: ${post.dueAt} | Asset: ${post.assetName}`);

    const input = {
      channelId: LINKEDIN_CHANNEL_ID,
      text: post.caption,
      mode: 'customScheduled',
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
      dueAt: post.dueAt
    };

    try {
      const response = await bufferGraphQL(CREATE_POST_MUTATION, { input });
      const result = response.data?.createPost;

      if (result?.__typename === 'PostActionSuccess' && result?.post?.id) {
        console.log(`[SUCCESS] Buffer ID: ${result.post.id} | Status: ${result.post.status} | DueAt: ${result.post.dueAt}`);
        scheduledThisRun++;
        report.push({
          id: post.id,
          day: post.day,
          slot: post.slot,
          date: post.date,
          dueAt: post.dueAt,
          pillar: post.pillar,
          topic: post.topic,
          assetName: post.assetName,
          assetUrl: post.assetUrl,
          status: 'SUCCESS',
          bufferPostId: result.post.id,
          postStatus: result.post.status,
          scheduledAtTime: new Date().toISOString()
        });
      } else if (result?.__typename === 'LimitReachedError') {
        console.log(`\n[BUFFER QUEUE FULL] LimitReachedError: ${result.message}`);
        console.log('Buffer channel capacity reached. Pausing until upcoming posts publish.');
        queueFull = true;
        break;
      } else {
        const errMsg = result?.message || JSON.stringify(response);
        console.error(`[ERROR] Post #${post.id} failed:`, errMsg);
        report.push({
          id: post.id,
          day: post.day,
          slot: post.slot,
          status: 'ERROR',
          error: errMsg,
          attemptedAt: new Date().toISOString()
        });
      }
    } catch (err) {
      console.error(`[EXCEPTION] Post #${post.id}:`, err.message);
      report.push({
        id: post.id,
        day: post.day,
        slot: post.slot,
        status: 'EXCEPTION',
        error: err.message,
        attemptedAt: new Date().toISOString()
      });
    }

    // Persist report after every post
    fs.writeFileSync(REPORT_FILE, JSON.stringify(report, null, 2));

    // Polite pacing between Buffer calls
    await new Promise(r => setTimeout(r, 1200));
  }

  console.log('\n===============================================================');
  console.log(`Execution Run Complete: ${scheduledThisRun} new posts scheduled in Buffer.`);
  console.log(`Total successfully scheduled to date: ${report.filter(r => r.status === 'SUCCESS').length} / ${posts.length}`);
  if (queueFull) {
    console.log('Channel queue is currently at capacity. The automated background timer will replenish remaining posts as slots clear.');
  }
  console.log('===============================================================\n');
}

main().catch(console.error);
