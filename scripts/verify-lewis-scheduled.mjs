import { bufferGraphQL } from './buffer-post.mjs';

const lewisPostIds = [
  '6a939f3cf7f5d8f78d0f817d',
  '6a939f3d6521164abcfb13f1',
  '6a939f3e61f7ab587cd4524c',
  '6a939f4019e5b3c30eb181e9',
  '6a939f41bb2aa0b2b4a1597e',
  '6a939f4261f7ab587cd452a3',
  '6a939f4473b542df4de839dc',
  '6a939f466521164abcfb1448',
  '6a939f4a19e5b3c30eb18595',
  '6a939f4c61f7ab587cd452ef',
];

async function main() {
  console.log('======================================================');
  console.log('🏎️ Auditing 10 Lewis Hamilton Posts in Buffer Queue');
  console.log('======================================================\n');

  for (let i = 0; i < lewisPostIds.length; i++) {
    const id = lewisPostIds[i];
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
        console.log(`[Lewis Hamilton #${i+1}] ID: ${post.id}`);
        console.log(`   📅 Slot: ${post.dueAt}`);
        console.log(`   📊 Status: ${post.status}`);
        console.log(`   🖼️ Image Asset: ${hasImage ? '✅ YES (' + post.assets[0].thumbnail.slice(0, 65) + '...)' : '❌ NO IMAGE'}`);
        console.log(`   📝 Text preview: ${post.text?.slice(0, 75)?.replace(/\n/g, ' ')}...`);
        console.log('------------------------------------------------------');
      }
    } catch (err) {
      console.error(`[Lewis Hamilton #${i+1}] Error:`, err.message);
    }
  }
}

main().catch(console.error);
