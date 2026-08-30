import { bufferGraphQL } from './buffer-post.mjs';

const usOpenPostIds = [
  '6a939d0a73b542df4de808bf', // Post 1
  '6a939d0b73b542df4de808e2', // Post 2
  '6a939d0c73b542df4de80913', // Post 3
  '6a939d0ebb2aa0b2b4a134bb', // Post 4
  '6a939d0ff7f5d8f78d0f5e08', // Post 5
  '6a939d11f7f5d8f78d0f5e3c', // Post 6
  '6a939d1219e5b3c30eb14dad', // Post 7
  '6a939d136521164abcfae577', // Post 8
  '6a939d1519e5b3c30eb14de8', // Post 9
  '6a939d1661f7ab587cd4306e', // Post 10
];

async function main() {
  console.log('======================================================');
  console.log('🎾 Auditing All 10 US Open Posts in Buffer Queue');
  console.log('======================================================\n');

  for (let i = 0; i < usOpenPostIds.length; i++) {
    const id = usOpenPostIds[i];
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
        console.log(`[US Open Ad #${i+1}] ID: ${post.id}`);
        console.log(`   📅 Slot: ${post.dueAt}`);
        console.log(`   📊 Status: ${post.status}`);
        console.log(`   🖼️ Image Asset: ${hasImage ? '✅ YES (' + post.assets[0].thumbnail.slice(0, 65) + '...)' : '❌ NO IMAGE'}`);
        console.log(`   📝 Text preview: ${post.text?.slice(0, 75)?.replace(/\n/g, ' ')}...`);
        console.log('------------------------------------------------------');
      }
    } catch (err) {
      console.error(`[US Open Ad #${i+1}] Error:`, err.message);
    }
  }
}

main().catch(console.error);
