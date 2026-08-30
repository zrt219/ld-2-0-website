/**
 * Resume scheduling remaining Destiny Spurlock campaign posts (Posts 7 - 10)
 * Run once Buffer API 24h limit window clears.
 */

import { bufferGraphQL } from './buffer-post.mjs';
import { destinySpurlockPosts } from './schedule-destiny-campaign.mjs';

const CHANNEL_ID = '6a39d30c5ab6d2f1065f5301';

async function schedulePost(post) {
  const input = {
    channelId: CHANNEL_ID,
    text: post.text,
    mode: 'customScheduled',
    dueAt: post.dueAt,
    schedulingType: 'automatic',
    needsApproval: false,
    saveToDraft: false,
    assets: [
      {
        image: {
          url: post.imageUrl,
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
            dueAt
          }
        }
        ... on LimitReachedError { message }
        ... on InvalidInputError { message }
      }
    }
  `;

  return await bufferGraphQL(mutation, { input });
}

async function main() {
  const remaining = destinySpurlockPosts.slice(6); // Posts 7, 8, 9, 10
  console.log(`Attempting to schedule ${remaining.length} remaining Destiny Spurlock posts...`);

  for (const post of remaining) {
    console.log(`[Scheduling #${post.id}] ${post.title} (${post.timeLabel})...`);
    try {
      const res = await schedulePost(post);
      if (res.createPost?.__typename === 'PostActionSuccess' && res.createPost.post) {
        console.log(`   ✅ SUCCESS! Buffer Post ID: ${res.createPost.post.id}`);
      } else {
        console.log(`   ⚠️ Response:`, JSON.stringify(res, null, 2));
      }
    } catch (err) {
      console.error(`   ❌ Error:`, err.message);
    }
    await new Promise(r => setTimeout(r, 600));
  }
}

main().catch(console.error);
