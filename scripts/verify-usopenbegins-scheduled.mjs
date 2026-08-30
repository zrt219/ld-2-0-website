import { bufferGraphQL } from './buffer-post.mjs';

const postIds = [
  '6a939e52bb2aa0b2b4a1459d',
  '6a939e54f7f5d8f78d0f707f',
  '6a939e5519e5b3c30eb16393',
  '6a939e5619e5b3c30eb163d1',
  '6a939e58bb2aa0b2b4a145d6',
  '6a939e596521164abcfaf5ff',
  '6a939e5a19e5b3c30eb1642b',
  '6a939e5cf7f5d8f78d0f70d8',
  '6a939e5d6521164abcfaf622',
  '6a939e5e6521164abcfaf648',
];

async function main() {
  console.log('======================================================');
  console.log('🎾 Auditing 10 "US OPEN BEGINS" Posts in Buffer Queue');
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
        console.log(`[US Open Begins #${i+1}] ID: ${post.id}`);
        console.log(`   📅 Slot: ${post.dueAt}`);
        console.log(`   📊 Status: ${post.status}`);
        console.log(`   🖼️ Image Asset: ${hasImage ? '✅ YES (' + post.assets[0].thumbnail.slice(0, 65) + '...)' : '❌ NO IMAGE'}`);
        console.log(`   📝 Text preview: ${post.text?.slice(0, 75)?.replace(/\n/g, ' ')}...`);
        console.log('------------------------------------------------------');
      }
    } catch (err) {
      console.error(`[US Open Begins #${i+1}] Error:`, err.message);
    }
  }
}

main().catch(console.error);
