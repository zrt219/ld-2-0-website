import { bufferGraphQL } from './buffer-post.mjs';

async function main() {
  const schema = await bufferGraphQL(`
    query {
      __type(name: "Mutation") {
        fields {
          name
          description
          args {
            name
            type { name kind ofType { name kind } }
          }
        }
      }
    }
  `);
  console.log('Mutations:', schema.__type.fields.filter(f => 
    f.name.toLowerCase().includes('upload') || 
    f.name.toLowerCase().includes('media') || 
    f.name.toLowerCase().includes('asset') ||
    f.name.toLowerCase().includes('image') ||
    f.name.toLowerCase().includes('idea')
  ));
}

main().catch(console.error);
