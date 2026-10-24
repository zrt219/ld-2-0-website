// scripts/schedule-master.mjs
// Master Autonomous Scheduling & Recovery Engine
// Supports: Multi-Sport 21-Day Pacing, COMO Asterisk Sanitization,
// Dawn Staley WNBA Series, and 90-Day Coco Gauff Campaign.

import fs from 'fs';
import path from 'path';
import https from 'https';

const TOKEN = process.env.BUFFER_ACCESS_TOKEN || 'uR7DeyYk4O9VcFHqPQOnWseUl7BONqA8RZ4CK_03Ci0';
const CHANNEL_ID = '6a39d30c5ab6d2f1065f5301';

const CREATE_POST_MUTATION = `
mutation CreatePost($input: CreatePostInput!) {
  createPost(input: $input) {
    __typename
    ... on PostActionSuccess {
      post {
        id
        status
        dueAt
      }
    }
    ... on LimitReachedError { message }
    ... on InvalidInputError { message }
    ... on UnexpectedError { message }
    ... on RestError { message }
  }
}
`;

function sendGraphql(payload) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify(payload);
    const req = https.request('https://api.buffer.com', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${TOKEN}`,
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(data),
        'User-Agent': 'Mozilla/5.0'
      },
      rejectUnauthorized: false
    }, (res) => {
      let body = '';
      res.on('data', chunk => body += chunk);
      res.on('end', () => {
        if (res.statusCode === 429) {
          const retryAfter = res.headers['retry-after'];
          return resolve({ error: 429, retryAfter });
        }
        try {
          resolve(JSON.parse(body));
        } catch (e) {
          resolve({ error: 'PARSE_ERROR', body });
        }
      });
    });
    req.on('error', reject);
    req.write(data);
    req.end();
  });
}

// 1. Dawn Staley Queue Processing
async function runDawnStaleyQueue() {
  console.log("\n--- Processing Dawn Staley Campaign Queue ---");
  const queuePath = path.resolve('scripts/master-dawn-staley-queue.json');
  const reportPath = path.resolve('scripts/dawn-staley-scheduled-report.json');

  if (!fs.existsSync(queuePath)) return;

  const queue = JSON.parse(fs.readFileSync(queuePath, 'utf8'));
  const report = fs.existsSync(reportPath) ? JSON.parse(fs.readFileSync(reportPath, 'utf8')) : {};

  for (const item of queue) {
    if (report[item.id]) continue;

    console.log(`Scheduling ${item.id} | Day ${item.day} (${item.slot})...`);
    const resp = await sendGraphql({
      query: CREATE_POST_MUTATION,
      variables: {
        input: {
          channelId: CHANNEL_ID,
          text: item.text,
          schedulingType: "automatic",
          mode: item.mode || "customScheduled",
          dueAt: item.dueAt,
          assets: [{ image: { url: item.asset_url } }]
        }
      }
    });

    if (resp.error === 429) {
      console.log(`⚠️ Rate limit active. Retry-After: ${resp.retryAfter}s`);
      return false;
    }

    if (resp.data?.createPost?.__typename === 'PostActionSuccess') {
      const p = resp.data.createPost.post;
      console.log(`   ✅ SUCCESS: Post ${p.id} (${p.status})`);
      report[item.id] = {
        postId: p.id,
        status: p.status,
        dueAt: item.dueAt,
        mode: item.mode,
        asset_url: item.asset_url
      };
      fs.writeFileSync(reportPath, JSON.stringify(report, null, 2), 'utf8');
      await new Promise(r => setTimeout(r, 1000));
    } else {
      console.log(`   ⚠️ Failed to schedule ${item.id}:`, JSON.stringify(resp));
      return false;
    }
  }
  return true;
}

// 2. Coco Gauff 90-Day Campaign Processing
async function runCocoRacismQueue() {
  console.log("\n--- Processing 90-Day Coco Gauff Campaign Queue ---");
  const queuePath = path.resolve('scripts/master-coco-racism-queue.json');
  const reportPath = path.resolve('scripts/coco-racism-scheduled-report.json');

  if (!fs.existsSync(queuePath)) return;

  const queue = JSON.parse(fs.readFileSync(queuePath, 'utf8'));
  const report = fs.existsSync(reportPath) ? JSON.parse(fs.readFileSync(reportPath, 'utf8')) : {};

  for (const item of queue) {
    if (report[item.id]) continue;

    console.log(`Scheduling ${item.id} | Day ${item.day} (${item.slot})...`);
    const assetPayload = item.asset_type === 'video'
      ? [{ video: { url: item.asset_url } }]
      : [{ image: { url: item.asset_url } }];

    const resp = await sendGraphql({
      query: CREATE_POST_MUTATION,
      variables: {
        input: {
          channelId: CHANNEL_ID,
          text: item.text,
          schedulingType: "automatic",
          mode: item.mode || "customScheduled",
          dueAt: item.dueAt,
          assets: assetPayload
        }
      }
    });

    if (resp.error === 429) {
      console.log(`⚠️ Rate limit active. Retry-After: ${resp.retryAfter}s`);
      return false;
    }

    if (resp.data?.createPost?.__typename === 'PostActionSuccess') {
      const p = resp.data.createPost.post;
      console.log(`   ✅ SUCCESS: Post ${p.id} (${p.status})`);
      report[item.id] = {
        postId: p.id,
        status: p.status,
        dueAt: item.dueAt,
        slot: item.slot,
        mode: item.mode,
        asset_url: item.asset_url,
        asset_type: item.asset_type
      };
      fs.writeFileSync(reportPath, JSON.stringify(report, null, 2), 'utf8');
      await new Promise(r => setTimeout(r, 1200));
    } else {
      console.log(`   ⚠️ Failed to schedule ${item.id}:`, JSON.stringify(resp));
      return false;
    }
  }
  return true;
}

async function runMaster() {
  console.log("================================================================");
  console.log("🚀 MASTER AUTONOMOUS CAMPAIGN SCHEDULER & RECOVERY ENGINE");
  console.log("================================================================");

  // 1. Finish pending Dawn Staley
  const dawnOk = await runDawnStaleyQueue();
  if (!dawnOk) {
    console.log("\nPaused on Dawn Staley due to Buffer quota limit. Waiting for timer reset.");
    return;
  }

  // 2. Schedule 90-Day Coco Gauff
  const cocoOk = await runCocoRacismQueue();
  if (!cocoOk) {
    console.log("\nPaused on Coco Gauff due to Buffer quota limit. Waiting for timer reset.");
    return;
  }

  console.log("\n>>> ALL CAMPAIGNS FULLY SCHEDULED & SYNCHRONIZED <<<");
}

runMaster().catch(console.error);
