import fs from 'fs';
import path from 'path';

const BUFFER_TOKEN = process.env.BUFFER_ACCESS_TOKEN || 'mLbjEsRdn5FKtGOskFoGzK-gW2CGTl8dfAK8klDVEPC';
const CHANNEL_ID = '6a39d30c5ab6d2f1065f5301';
const GRAPHQL_ENDPOINT = 'https://api.buffer.com';

const query = `
  query GetScheduledPosts($channelId: RecordId!) {
    channel(id: $channelId) {
      id
      name
      service
      posts(status: [scheduled, bufferred], limit: 100) {
        total
        lines {
          id
          dueAt
          status
          text
        }
      }
    }
  }
`;

async function main() {
  const res = await fetch(GRAPHQL_ENDPOINT, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${BUFFER_TOKEN}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      query,
      variables: { channelId: CHANNEL_ID },
    }),
  });

  const result = await res.json();
  if (result.errors) {
    console.error('GraphQL Error:', JSON.stringify(result.errors, null, 2));
    return;
  }

  const posts = result.data?.channel?.posts?.lines || [];
  console.log(`Found ${posts.length} currently scheduled posts in Buffer:`);
  posts.forEach((p, idx) => {
    console.log(`  [#${idx + 1}] ID: ${p.id} | Due: ${p.dueAt} | Text: ${p.text.substring(0, 40)}...`);
  });

  fs.writeFileSync('scripts/live-buffer-posts.json', JSON.stringify(posts, null, 2));
}

main().catch(console.error);
