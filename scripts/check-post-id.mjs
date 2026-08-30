const TOKEN = process.env.BUFFER_ACCESS_TOKEN || 'mLbjEsRdn5FKtGOskFoGzK-gW2CGTl8dfAK8klDVEPC';

async function checkPostById(id) {
  const query = `
    query GetPost($id: String!) {
      post(input: { id: $id }) {
        id
        status
        shareMode
        dueAt
        sentAt
        text
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
      variables: { id },
    }),
  });

  const data = await res.json();
  console.log(JSON.stringify(data, null, 2));
}

checkPostById('6a9397fe19e5b3c30eb0ffde').catch(console.error);
