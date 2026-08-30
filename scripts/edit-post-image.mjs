import { bufferGraphQL } from './buffer-post.mjs';

async function main() {
  const postId = '6a939951d6c6c023c6592228';
  const imageUrl = 'https://lornettedaye.com/campaigns/turkey/turkey-08.png';

  const editMutation = `
    mutation EditPost($input: EditPostInput!) {
      editPost(input: $input) {
        __typename
        ... on PostActionSuccess {
          post {
            id
            text
            status
            dueAt
          }
        }
        ... on NotFoundError { message }
        ... on UnauthorizedError { message }
        ... on UnexpectedError { message }
        ... on LimitReachedError { message }
        ... on InvalidInputError { message }
      }
    }
  `;

  const input = {
    id: postId,
    assets: [
      {
        image: {
          url: imageUrl
        }
      }
    ]
  };

  const res = await bufferGraphQL(editMutation, { input });
  console.log('Edit result:', JSON.stringify(res, null, 2));
}

main().catch(console.error);
