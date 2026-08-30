import { bufferGraphQL, getChannels } from './buffer-post.mjs';

async function main() {
  const { account, channels } = await getChannels();
  const orgId = account.organizations[0].id;
  const channelId = channels[0].id;

  const query = `
    query GetPosts($input: PostsInput!) {
      posts(input: $input) {
        totalCount
        edges {
          node {
            id
            text
            dueAt
            status
          }
        }
      }
    }
  `;

  const res = await bufferGraphQL(query, {
    input: {
      organizationId: orgId,
      filter: {
        channelIds: [channelId],
        status: ['scheduled']
      }
    }
  });

  console.log(`\n======================================================`);
  console.log(`Total Scheduled Posts in Buffer: ${res.posts?.totalCount || res.posts?.edges?.length}`);
  console.log(`======================================================\n`);
  
  res.posts?.edges?.forEach((e, idx) => {
    console.log(`[#${idx+1}] ID: ${e.node.id} | Due At: ${e.node.dueAt} | Status: ${e.node.status}`);
    console.log(`    Snippet: ${e.node.text?.slice(0, 100)?.replace(/\n/g, ' ')}...`);
    console.log('---');
  });
}

main().catch(console.error);
