/**
 * Buffer API Client for Lornette Daye LinkedIn Publishing
 * 
 * Buffer GraphQL API Endpoint: https://api.buffer.com
 */

const BUFFER_ACCESS_TOKEN = process.env.BUFFER_ACCESS_TOKEN || 'mLbjEsRdn5FKtGOskFoGzK-gW2CGTl8dfAK8klDVEPC';
const BUFFER_API_URL = 'https://api.buffer.com';

export async function bufferGraphQL(query, variables = {}) {
  const response = await fetch(BUFFER_API_URL, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${BUFFER_ACCESS_TOKEN}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ query, variables }),
  });

  const json = await response.json();
  if (json.errors && json.errors.length > 0) {
    throw new Error(`Buffer GraphQL Error: ${JSON.stringify(json.errors, null, 2)}`);
  }
  return json.data;
}

/**
 * Get account organizations and channels
 */
export async function getChannels() {
  const accountData = await bufferGraphQL(`
    query {
      account {
        id
        email
        organizations {
          id
          name
        }
      }
    }
  `);

  const orgId = accountData?.account?.organizations?.[0]?.id;
  if (!orgId) {
    throw new Error('No organization found for this Buffer account.');
  }

  const channelsData = await bufferGraphQL(`
    query GetChannels($input: ChannelsInput!) {
      channels(input: $input) {
        id
        name
        service
        serviceId
        displayName
        avatar
      }
    }
  `, { input: { organizationId: orgId } });

  return {
    account: accountData.account,
    channels: channelsData.channels || [],
  };
}

/**
 * Create / Schedule / Publish a Post to LinkedIn via Buffer GraphQL API
 * 
 * @param {Object} options
 * @param {string} options.text - The post content
 * @param {string} [options.channelId] - Buffer channel ID (defaults to Lornette's LinkedIn)
 * @param {'shareNow'|'addToQueue'|'customScheduled'|'shareNext'} [options.shareMode='shareNow']
 * @param {string} [options.dueAt] - ISO DateTime string if using customScheduled
 * @param {boolean} [options.saveToDraft=false]
 */
export async function createLinkedInPost({
  text,
  channelId = '6a39d30c5ab6d2f1065f5301',
  shareMode = 'addToQueue',
  dueAt,
  saveToDraft = false,
}) {
  const input = {
    channelId,
    text,
    mode: shareMode,
    schedulingType: 'automatic',
    needsApproval: false,
    saveToDraft,
    assets: [],
    ...(dueAt ? { dueAt } : {}),
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
            shareMode
            dueAt
            sentAt
            channelService
          }
        }
        ... on NotFoundError {
          message
        }
        ... on UnauthorizedError {
          message
        }
        ... on UnexpectedError {
          message
        }
        ... on LimitReachedError {
          message
        }
        ... on InvalidInputError {
          message
        }
      }
    }
  `;

  const result = await bufferGraphQL(mutation, { input });
  return result.createPost;
}

// CLI Execution Helper
if (process.argv[1]?.endsWith('buffer-post.mjs') || process.argv[1]?.endsWith('buffer-post')) {
  const action = process.argv[2] || 'status';

  if (action === 'status' || action === 'channels') {
    getChannels()
      .then(info => {
        console.log('--- Buffer Account & Channels ---');
        console.log(`Account Email: ${info.account.email}`);
        console.log(`Channels:`);
        info.channels.forEach(ch => {
          console.log(`  - [${ch.service.toUpperCase()}] ${ch.displayName} (${ch.name}) | Channel ID: ${ch.id}`);
        });
      })
      .catch(console.error);
  } else if (action === 'post') {
    const postText = process.argv[3];
    const mode = process.argv[4] || 'addToQueue';

    if (!postText) {
      console.log('Usage: node scripts/buffer-post.mjs post "Your post text" [shareNow|addToQueue]');
      process.exit(1);
    }

    createLinkedInPost({ text: postText, shareMode: mode })
      .then(res => {
        console.log('Post Result:', JSON.stringify(res, null, 2));
      })
      .catch(console.error);
  }
}
