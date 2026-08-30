import fs from 'fs';
import path from 'path';
import { bufferGraphQL, getChannels } from './buffer-post.mjs';

async function main() {
  const { account } = await getChannels();
  const orgId = account.organizations[0].id;
  const res = await bufferGraphQL(`
    query GetIdeas($input: IdeasInput!) {
      ideas(input: $input) {
        edges {
          node {
            id
            groupId
            position
            content {
              text
              media { url thumbnailUrl }
              title
            }
          }
        }
      }
    }
  `, { input: { organizationId: orgId } });

  const ideas = res.ideas.edges.map(e => e.node);
  ideas.sort((a, b) => (a.position || 0) - (b.position || 0));
  
  fs.writeFileSync(path.join(process.cwd(), 'scripts', 'buffer-ideas-dump.json'), JSON.stringify(ideas, null, 2));
  console.log(`Successfully dumped ${ideas.length} ideas to scripts/buffer-ideas-dump.json`);
}

main().catch(console.error);
