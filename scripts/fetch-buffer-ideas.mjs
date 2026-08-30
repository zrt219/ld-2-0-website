import { bufferGraphQL, getChannels } from './buffer-post.mjs';

async function main() {
  const { account, channels } = await getChannels();
  const orgId = account.organizations[0].id;

  const groupsQuery = `
    query GetIdeaGroups($input: IdeaGroupsInput!) {
      ideaGroups(input: $input) {
        id
        name
      }
    }
  `;
  const groupsData = await bufferGraphQL(groupsQuery, { input: { organizationId: orgId } });
  const groups = groupsData.ideaGroups || [];
  const groupMap = Object.fromEntries(groups.map(g => [g.id, g.name]));

  const ideasQuery = `
    query GetIdeas($input: IdeasInput!) {
      ideas(input: $input) {
        edges {
          node {
            id
            groupId
            position
            content {
              text
              media {
                url
                thumbnailUrl
              }
              title
              date
            }
            createdAt
            updatedAt
          }
        }
      }
    }
  `;
  const ideasRes = await bufferGraphQL(ideasQuery, { input: { organizationId: orgId } });
  const ideas = ideasRes.ideas?.edges?.map(e => e.node) || [];
  console.log(`\nTotal Ideas Found in Buffer: ${ideas.length}\n`);

  const grouped = {};
  for (const idea of ideas) {
    const groupName = groupMap[idea.groupId] || 'Ungrouped';
    if (!grouped[groupName]) grouped[groupName] = [];
    grouped[groupName].push(idea);
  }

  for (const [grp, list] of Object.entries(grouped)) {
    console.log(`\n=================== GROUP: ${grp} (${list.length} ideas) ===================`);
    list.sort((a, b) => (a.position || 0) - (b.position || 0));
    list.forEach((item, idx) => {
      console.log(`[#${idx + 1}] ID: ${item.id} | Position: ${item.position}`);
      console.log(`Text: ${item.content?.text?.replace(/\n/g, ' ')?.slice(0, 120)}...`);
      console.log(`Media: ${JSON.stringify(item.content?.media)}`);
      console.log('---');
    });
  }
}

main().catch(console.error);
