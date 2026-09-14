/**
 * 100% Autonomous Master Buffer Campaign Publisher & Queue Daemon
 * Seamless Multi-Day Spacing Engine (adheres to LinkedIn 50/day channel limits)
 */

import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';

const BUFFER_TOKEN = process.env.BUFFER_ACCESS_TOKEN || 'mLbjEsRdn5FKtGOskFoGzK-gW2CGTl8dfAK8klDVEPC';
const CHANNEL_ID = '6a39d30c5ab6d2f1065f5301';
const GRAPHQL_ENDPOINT = 'https://api.buffer.com';

const isCatchup = process.argv.includes('--catchup');
if (isCatchup) {
  console.log('[Catchup Mode] Executing pending campaign queue handlers...');
  const parents2Script = path.join(process.cwd(), 'scripts', 'schedule-parents-set-2-campaign.py');
  if (fs.existsSync(parents2Script)) {
    try {
      console.log('[Catchup Mode] Running schedule-parents-set-2-campaign.py...');
      execSync(`python "${parents2Script}"`, { stdio: 'inherit' });
    } catch (e) {
      console.error('[Catchup Mode] Python script exited:', e.message);
    }
  }
}

const manifestPath = path.join(process.cwd(), 'scripts', 'campaign-manifest.json');
const queuePath = path.join(process.cwd(), 'scripts', 'master-campaign-queue.json');
const reportPath = path.join(process.cwd(), 'scripts', 'scheduled-master-report.json');

async function syncQueue() {
  let manifest = [];
  if (fs.existsSync(manifestPath)) {
    manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf-8'));
  } else if (fs.existsSync(queuePath)) {
    manifest = JSON.parse(fs.readFileSync(queuePath, 'utf-8'));
  } else {
    console.error('No queue or manifest file found.');
    return;
  }

  // Ensure post 280 status is reflected
  const p280 = manifest.find(q => q.id === 280);
  if (p280 && p280.status !== 'scheduled') {
    p280.status = 'scheduled';
    p280.bufferPostId = '6a965485d351db8f3269ff55';
  }

  fs.writeFileSync(queuePath, JSON.stringify(manifest, null, 2));

  const now = new Date();
  let pendingPosts = manifest.filter(p => p.status === 'staged' || p.status === 'pending');

  console.log(`\n======================================================`);
  console.log(`[Master Campaign Daemon] Total: ${manifest.length} | Pending: ${pendingPosts.length}`);
  console.log(`Current Time: ${now.toISOString()}`);
  console.log(`======================================================\n`);

  if (pendingPosts.length === 0) {
    console.log('🎉 ALL 320 POSTS IN MASTER MANIFEST HAVE BEEN SCHEDULED IN BUFFER!');
    fs.writeFileSync(reportPath, JSON.stringify({
      lastRun: new Date().toISOString(),
      totalPosts: manifest.length,
      scheduledCount: manifest.length,
      pendingCount: 0,
      scheduledThisRun: 0,
      rateLimitHit: false,
      allComplete: true,
    }, null, 2));
    return;
  }

  const mutation = `
    mutation CreatePost($input: CreatePostInput!) {
      createPost(input: $input) {
        __typename
        ... on PostActionSuccess {
          post {
            id
            status
            shareMode
            dueAt
          }
        }
        ... on LimitReachedError {
          message
        }
        ... on InvalidInputError {
          message
        }
        ... on UnauthorizedError {
          message
        }
        ... on UnexpectedError {
          message
        }
      }
    }
  `;

  let scheduledThisRun = 0;
  let rateLimitHit = false;

  // Daily MDT time slots converted to UTC (8:30 AM, 11:00 AM, 1:30 PM, 4:00 PM, 6:30 PM, 9:00 PM MDT)
  const timeSlotsUTC = [
    { hour: 14, min: 30 },
    { hour: 17, min: 0 },
    { hour: 19, min: 30 },
    { hour: 22, min: 0 },
    { hour: 0, min: 30 },
    { hour: 3, min: 0 }
  ];

  // Base starting date: September 28, 2026 (Day 29 of campaign)
  const baseStart = new Date(Date.UTC(2026, 8, 28, 0, 0, 0)); // Month 8 is Sept in JS Date

  for (let i = 0; i < pendingPosts.length; i++) {
    const post = pendingPosts[i];
    
    const dayOffset = Math.floor(i / 6);
    const slotIndex = i % 6;
    const targetDate = new Date(baseStart.getTime() + dayOffset * 24 * 3600 * 1000);
    targetDate.setUTCHours(timeSlotsUTC[slotIndex].hour, timeSlotsUTC[slotIndex].min, 0, 0);

    const postDueAt = targetDate.toISOString();

    console.log(`[Queueing #${post.id}] Target: ${postDueAt} -> ${post.campaign} (${post.imageFile})`);

    const variables = {
      input: {
        channelId: CHANNEL_ID,
        mode: 'customScheduled',
        schedulingType: 'automatic',
        needsApproval: false,
        saveToDraft: false,
        dueAt: postDueAt,
        text: post.text,
        assets: [
          {
            image: {
              url: post.imageUrl,
            },
          },
        ],
      },
    };

    try {
      const res = await fetch(GRAPHQL_ENDPOINT, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${BUFFER_TOKEN}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          query: mutation,
          variables,
        }),
      });

      const result = await res.json();

      if (res.status === 429 || result.errors?.[0]?.extensions?.code === 'RATE_LIMIT_EXCEEDED') {
        console.log(`   ⏳ Buffer API rate limit reached (HTTP ${res.status}). Will resume on next cycle.`);
        rateLimitHit = true;
        break;
      } else if (result.errors) {
        console.error(`   ❌ GraphQL Error:`, result.errors[0]?.message);
      } else if (result.data?.createPost?.post?.id) {
        const p = result.data.createPost.post;
        console.log(`   ✅ Scheduled in Buffer! ID: ${p.id} | Due: ${p.dueAt}`);
        post.status = 'scheduled';
        post.bufferPostId = p.id;
        scheduledThisRun++;
      } else if (result.data?.createPost?.__typename === 'LimitReachedError') {
        console.log(`   ⚠️ Buffer LimitReachedError:`, result.data.createPost.message);
        rateLimitHit = true;
        break;
      } else if (result.data?.createPost?.__typename === 'InvalidInputError') {
        console.log(`   ⚠️ InvalidInputError:`, result.data.createPost.message);
      } else {
        console.error(`   ⚠️ Unexpected Response:`, JSON.stringify(result.data?.createPost));
      }
    } catch (err) {
      console.error(`   ❌ Fetch Exception:`, err.message);
    }

    await new Promise(r => setTimeout(r, 650));
  }

  fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2));
  fs.writeFileSync(queuePath, JSON.stringify(manifest, null, 2));

  const scheduledTotal = manifest.filter(m => m.status === 'scheduled').length;
  const pendingTotal = manifest.filter(m => m.status === 'staged' || m.status === 'pending').length;

  const summaryReport = {
    lastRun: new Date().toISOString(),
    totalPosts: manifest.length,
    scheduledCount: scheduledTotal,
    pendingCount: pendingTotal,
    scheduledThisRun,
    rateLimitHit,
  };

  fs.writeFileSync(reportPath, JSON.stringify(summaryReport, null, 2));
  console.log(`\nSync Run Complete: ${scheduledThisRun} newly scheduled. Total Scheduled: ${scheduledTotal}/${manifest.length}`);
}

syncQueue().catch(console.error);
