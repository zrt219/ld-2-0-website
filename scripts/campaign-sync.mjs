/**
 * Campaign Manifest & Queue Synchronizer for Lornette Daye LinkedIn
 * 
 * Manages 63 posts across 21 days (3 Weeks) at 6pm, 7pm, and 8pm MDT.
 * Keeps the Buffer queue filled to maximum capacity (10 active scheduled posts).
 * Also stages all remaining posts as Drafts in Buffer.
 */

import fs from 'fs';
import path from 'path';

const BUFFER_ACCESS_TOKEN = process.env.BUFFER_ACCESS_TOKEN || 'mLbjEsRdn5FKtGOskFoGzK-gW2CGTl8dfAK8klDVEPC';
const BUFFER_API_URL = 'https://api.buffer.com';
const CHANNEL_ID = '6a39d30c5ab6d2f1065f5301';
const BASE_IMAGE_URL = 'https://lornettedaye.com/campaigns/vargas';
const MANIFEST_FILE = path.join(process.cwd(), 'scripts', 'campaign-manifest.json');

export async function bufferGraphQL(query, variables = {}) {
  const response = await fetch(BUFFER_API_URL, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${BUFFER_ACCESS_TOKEN}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ query, variables }),
  });

  const json = await response.json();
  if (json.errors && json.errors.length > 0) {
    throw new Error(`Buffer GraphQL Error: ${JSON.stringify(json.errors, null, 2)}`);
  }
  return json.data;
}

// Generate MDT ISO string for a given date offset and hour (18, 19, 20)
export function getDueAt(dayOffset, hour) {
  const year = 2026;
  const month = 7; // August (0-indexed)
  const baseDay = 28;

  const targetDate = new Date(Date.UTC(year, month, baseDay + dayOffset, hour + 6, 0, 0, 0));
  return targetDate.toISOString();
}

// Create post mutation
export async function createPostInQueue(post, mode = 'customScheduled', saveToDraft = false) {
  const imgNum = String(post.imageIndex).padStart(2, '0');
  const imageUrl = `${BASE_IMAGE_URL}/vargas-${imgNum}.png`;

  const input = {
    channelId: CHANNEL_ID,
    text: post.text,
    mode,
    dueAt: post.dueAt,
    schedulingType: 'automatic',
    needsApproval: false,
    saveToDraft,
    assets: [
      {
        image: {
          url: imageUrl,
        },
      },
    ],
  };

  const mutation = `
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
          }
        }
        ... on NotFoundError { message }
        ... on UnauthorizedError { message }
        ... on UnexpectedError { message }
        ... on LimitReachedError { message }
        ... on InvalidInputError { message }
      }
    }
  `;

  const res = await bufferGraphQL(mutation, { input });
  return res.createPost;
}

// Check current scheduled count
export async function getQueueStatus() {
  const data = await bufferGraphQL(`
    query GetLimits($input: DailyPostingLimitsInput!) {
      dailyPostingLimits(input: $input) {
        channelId
        scheduled
        limit
        isAtLimit
      }
    }
  `, { input: { channelIds: [CHANNEL_ID] } });

  return data.dailyPostingLimits?.[0] || { scheduled: 0, limit: 10 };
}

export async function syncCampaign() {
  if (!fs.existsSync(MANIFEST_FILE)) {
    console.error('Manifest file not found at', MANIFEST_FILE);
    return;
  }

  const manifest = JSON.parse(fs.readFileSync(MANIFEST_FILE, 'utf-8'));
  console.log(`\n======================================================`);
  console.log(`Checking Buffer Queue for Lornette Daye Campaign`);
  console.log(`Total Posts in Manifest: ${manifest.length}`);

  const status = await getQueueStatus();
  console.log(`Current Buffer Scheduled in Queue: ${status.scheduled}`);
  console.log(`======================================================\n`);

  let availableSlots = Math.max(0, 10 - status.scheduled);
  console.log(`Available Queue Slots to schedule: ${availableSlots}`);

  for (let i = 0; i < manifest.length; i++) {
    const item = manifest[i];

    // If item is pending and we have available slots, schedule it
    if (item.status === 'pending' && availableSlots > 0) {
      console.log(`[Slot Available] Scheduling Post #${item.id} (Day ${item.day}, ${item.timeMDT})...`);
      try {
        const result = await createPostInQueue(item, 'customScheduled', false);
        if (result.__typename === 'PostActionSuccess' && result.post) {
          item.status = 'scheduled';
          item.bufferPostId = result.post.id;
          item.scheduledAt = new Date().toISOString();
          console.log(`   ✅ Successfully Scheduled! Buffer Post ID: ${result.post.id}`);
          availableSlots--;
        } else if (result.__typename === 'LimitReachedError') {
          console.log(`   ⚠️ Buffer queue limit reached.`);
          break;
        } else {
          console.error(`   ⚠️ Unexpected result:`, result);
        }
      } catch (err) {
        console.error(`   ❌ Error scheduling #${item.id}:`, err.message);
      }
      await new Promise(r => setTimeout(r, 400));
    }
  }

  // Save updated manifest
  fs.writeFileSync(MANIFEST_FILE, JSON.stringify(manifest, null, 2));

  const scheduledCount = manifest.filter(m => m.status === 'scheduled').length;
  const pendingCount = manifest.filter(m => m.status === 'pending').length;
  console.log(`\nSync Summary:`);
  console.log(`- Scheduled in Buffer Queue: ${scheduledCount}`);
  console.log(`- Pending in Pipeline: ${pendingCount}`);
  console.log(`- Manifest saved to scripts/campaign-manifest.json\n`);
}

// If run directly
if (process.argv[1]?.endsWith('campaign-sync.mjs') || process.argv[1]?.endsWith('campaign-sync')) {
  syncCampaign().catch(console.error);
}
