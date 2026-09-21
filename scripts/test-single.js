/* eslint-disable @typescript-eslint/no-require-imports */
const fs = require('fs');

const queue = JSON.parse(fs.readFileSync('scripts/master-campaign-queue.json', 'utf-8'));
const post = queue.find(q => q.status !== 'scheduled');
console.log('Testing post ID:', post.id, post.campaign, post.imageFile);

const mutation = `
  mutation CreatePost($input: CreatePostInput!) {
    createPost(input: $input) {
      __typename
      ... on PostActionSuccess {
        post { id dueAt status }
      }
      ... on LimitReachedError { message }
      ... on InvalidInputError { message }
      ... on UnauthorizedError { message }
      ... on UnexpectedError { message }
    }
  }
`;

async function test() {
  const token = 'mLbjEsRdn5FKtGOskFoGzK-gW2CGTl8dfAK8klDVEPC';
  const channelId = '6a39d30c5ab6d2f1065f5301';
  const res = await fetch('https://api.buffer.com', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      query: mutation,
      variables: {
        input: {
          channelId,
          mode: 'customScheduled',
          schedulingType: 'automatic',
          needsApproval: false,
          saveToDraft: false,
          dueAt: new Date(Date.now() + 86400000).toISOString(),
          text: post.text,
          assets: [{ image: { url: post.imageUrl } }]
        }
      }
    })
  });
  console.log('HTTP Status:', res.status);
  const json = await res.json();
  console.log('Result:', JSON.stringify(json, null, 2));
}
test().catch(console.error);
