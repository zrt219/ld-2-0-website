import { bufferGraphQL } from './buffer-post.mjs';

const postIds = [
  '6a93994fd6c6c023c65921fb', // Post 1
  '6a93995119e5b3c30eb1208f', // Post 2
  '6a939951d6c6c023c6592228', // Post 3
  '6a93995373b542df4de7cc46', // Post 4
  '6a93995419e5b3c30eb120d5', // Post 5
  '6a93995573b542df4de7cc69', // Post 6
  '6a939956d6c6c023c6592255', // Post 7
  '6a939957bb2aa0b2b4a106e0', // Post 8
  '6a939958d6c6c023c659229a', // Post 9
  '6a93995abb2aa0b2b4a1070f', // Post 10
];

async function main() {
  console.log('======================================================');
  console.log('🔍 Auditing All 10 Scheduled Posts in Buffer for Images');
  console.log('======================================================\n');

  for (let i = 0; i < postIds.length; i++) {
    const id = postIds[i];
    const query = `
      query GetPost($input: PostInput!) {
        post(input: $input) {
          id
          dueAt
          status
          text
          assets {
            __typename
            ... on ImageAsset {
              id
              thumbnail
              type
            }
          }
        }
      }
    `;

    try {
      const res = await bufferGraphQL(query, { input: { id } });
      const post = res.post;
      if (post) {
        const hasImage = post.assets && post.assets.length > 0 && post.assets[0].thumbnail;
        console.log(`[Post #${i+1}] ID: ${post.id}`);
        console.log(`   📅 Due At: ${post.dueAt}`);
        console.log(`   📊 Status: ${post.status}`);
        console.log(`   🖼️ Image Asset: ${hasImage ? '✅ YES (' + post.assets[0].thumbnail.slice(0, 75) + '...)' : '❌ NO IMAGE'}`);
        console.log(`   📝 Text: ${post.text?.slice(0, 80)?.replace(/\n/g, ' ')}...`);
        console.log('------------------------------------------------------');
      } else {
        console.log(`[Post #${i+1}] ID: ${id} - Not found`);
      }
    } catch (err) {
      console.error(`[Post #${i+1}] Error:`, err.message);
    }
  }
}

main().catch(console.error);
