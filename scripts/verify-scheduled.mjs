const TOKEN = process.env.BUFFER_ACCESS_TOKEN || 'mLbjEsRdn5FKtGOskFoGzK-gW2CGTl8dfAK8klDVEPC';

async function verifyScheduled() {
  const query = `
    query GetChannelPosts($input: PostsInput!) {
      posts(input: $input) {
        edges {
          node {
            id
            status
            dueAt
            text
          }
        }
      }
    }
  `;

  const res = await fetch('https://api.buffer.com', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${TOKEN}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      query,
      variables: {
        input: {
          channelId: '6a39d30c5ab6d2f1065f5301',
        },
      },
    }),
  });

  const data = await res.json();
  const edges = data.data?.posts?.edges || [];
  console.log(`\n✅ Verified in Buffer: ${edges.length} scheduled posts found.`);
  edges.forEach((e, idx) => {
    console.log(`[${idx + 1}] ID: ${e.node.id} | Due: ${e.node.dueAt} | ${e.node.text.slice(0, 60)}...`);
  });
}

verifyScheduled().catch(console.error);
