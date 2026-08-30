import { bufferGraphQL } from './buffer-post.mjs';

async function main() {
  const intro = await bufferGraphQL(`
    query {
      __type(name: "ImageAsset") {
        fields {
          name
        }
      }
    }
  `);
  console.log('ImageAsset fields:', intro.__type.fields.map(f => f.name));
}

main().catch(console.error);
