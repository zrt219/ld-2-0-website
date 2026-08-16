import fs from 'node:fs';

const catalogue = JSON.parse(fs.readFileSync('public/products/umattr-product-catalogue.json', 'utf8'));

const categoryMap = {
  'UMATTR Crown Care': {
    slug: 'hair-crown-care',
    displayName: 'Hair & Crown Care',
    description: 'Nourishing botanical formulas and protective crown solutions designed to honor texture, strength, and radiance.'
  },
  'UMATTR Crown Wigs': {
    slug: 'hair-crown-care',
    displayName: 'Hair & Crown Care',
    description: 'Nourishing botanical formulas and protective crown solutions designed to honor texture, strength, and radiance.'
  },
  'UMATTR Skin': {
    slug: 'makeup-skin',
    displayName: 'Makeup & Skin',
    description: 'Luminous skincare essentials and glow-focused formulations crafted for vitality and everyday elegance.'
  },
  'UMATTR Glow Makeup': {
    slug: 'makeup-skin',
    displayName: 'Makeup & Skin',
    description: 'Luminous skincare essentials and glow-focused formulations crafted for vitality and everyday elegance.'
  },
  'UMATTR Glow Lips': {
    slug: 'makeup-skin',
    displayName: 'Makeup & Skin',
    description: 'Luminous skincare essentials and glow-focused formulations crafted for vitality and everyday elegance.'
  },
  'UMATTR Tea & Wellness': {
    slug: 'tea-wellness',
    displayName: 'Tea & Wellness',
    description: 'Restorative herbal blends and holistic wellness rituals crafted to ground the mind and nourish the body.'
  },
  'UMATTR Fashion': {
    slug: 'clothing',
    displayName: 'Clothing',
    description: 'Refined silhouettes and timeless apparel tailored for confidence, comfort, and effortless presence.'
  },
  'UMATTR Men': {
    slug: 'clothing',
    displayName: 'Clothing',
    description: 'Refined silhouettes and timeless apparel tailored for confidence, comfort, and effortless presence.'
  },
  'UMATTR Intimates': {
    slug: 'clothing',
    displayName: 'Clothing',
    description: 'Refined silhouettes and timeless apparel tailored for confidence, comfort, and effortless presence.'
  },
  'UMATTR Carry': {
    slug: 'bags-accessories',
    displayName: 'Bags & Accessories',
    description: 'Sophisticated carry goods and statement accents made for modern movement and versatile utility.'
  },
  'UMATTR Accessories': {
    slug: 'bags-accessories',
    displayName: 'Bags & Accessories',
    description: 'Sophisticated carry goods and statement accents made for modern movement and versatile utility.'
  },
  'UMATTR Step': {
    slug: 'footwear',
    displayName: 'Footwear',
    description: 'Elevated footwear combining architectural comfort with graceful, commanding style.'
  },
  'UMATTR Home & Gift': {
    slug: 'home-gifts',
    displayName: 'Home & Gifts',
    description: 'Meaningful accents and luxury home comforts that cultivate an atmosphere of serenity and warmth.'
  }
};

const allCategories = [
  {
    id: 'hair-crown-care',
    name: 'Hair & Crown Care',
    description: 'Nourishing botanical formulas and protective crown solutions designed to honor texture, strength, and radiance.'
  },
  {
    id: 'makeup-skin',
    name: 'Makeup & Skin',
    description: 'Luminous skincare essentials and glow-focused formulations crafted for vitality and everyday elegance.'
  },
  {
    id: 'tea-wellness',
    name: 'Tea & Wellness',
    description: 'Restorative herbal blends and holistic wellness rituals crafted to ground the mind and nourish the body.'
  },
  {
    id: 'clothing',
    name: 'Clothing',
    description: 'Refined silhouettes and timeless apparel tailored for confidence, comfort, and effortless presence.'
  },
  {
    id: 'bags-accessories',
    name: 'Bags & Accessories',
    description: 'Sophisticated carry goods and statement accents made for modern movement and versatile utility.'
  },
  {
    id: 'footwear',
    name: 'Footwear',
    description: 'Elevated footwear combining architectural comfort with graceful, commanding style.'
  },
  {
    id: 'home-gifts',
    name: 'Home & Gifts',
    description: 'Meaningful accents and luxury home comforts that cultivate an atmosphere of serenity and warmth.'
  }
];

const products = [];
for (let i = 1; i <= 72; i++) {
  const catItem = catalogue.find(c => c.sequence === i);
  if (!catItem) {
    console.error('Sequence not found in catalogue:', i);
    continue;
  }
  const padded = String(i).padStart(2, '0');
  const catMeta = categoryMap[catItem.category] || { slug: 'hair-crown-care', displayName: 'Hair & Crown Care' };
  
  products.push({
    id: 'product-' + padded,
    sequence: i,
    name: catItem.name,
    categoryName: catMeta.displayName,
    categorySlug: catMeta.slug,
    subcategory: catItem.subcategory,
    originalCategory: catItem.category,
    imageSrc: '/products/clean/product-' + padded + '.png',
    alt: catItem.name + ' — Curated by Lornette Daye',
    status: 'Coming Soon',
    displayOrder: i
  });
}

const headerCode = `// Generated product catalogue configuration for The Collection — Curated by Lornette Daye

export interface ProductCategory {
  id: string;
  name: string;
  description: string;
}

export interface ProductItem {
  id: string;
  sequence: number;
  name: string;
  categoryName: string;
  categorySlug: string;
  subcategory: string;
  originalCategory: string;
  imageSrc: string;
  alt: string;
  status: string;
  displayOrder: number;
}

export const collectionMeta = {
  eyebrow: "COMING SOON",
  title: "The Collection",
  signature: "Curated by Lornette Daye",
  supportingCopy:
    "A thoughtful collection of beauty, wellness, fashion, and everyday essentials—chosen with confidence, purpose, and personal expression in mind.",
  primaryCtaText: "Explore the Collection",
  secondaryCtaText: "Join the Interest List",
  seoTitle: "The Collection — Curated by Lornette Daye",
  seoDescription:
    "Explore a coming collection of beauty, wellness, fashion, and everyday essentials curated by Lornette Daye. Join the interest list for launch updates.",
  canonicalUrl: "https://lornettedaye.com/collection",
  heroImage: "/products/clean/product-01.png",
  ogImage: "/products/clean/product-01.png",
};
`;

const fileContent = `${headerCode}
export const allProductCategories: ProductCategory[] = ${JSON.stringify(allCategories, null, 2)};

export const collectionProducts: ProductItem[] = ${JSON.stringify(products, null, 2)};

export function getActiveCategories(): (ProductCategory & { products: ProductItem[] })[] {
  return allProductCategories
    .map((category) => {
      const categoryProducts = collectionProducts.filter(
        (product) => product.categorySlug === category.id
      );
      return {
        ...category,
        products: categoryProducts,
      };
    })
    .filter((category) => category.products.length > 0);
}

export function getProductById(id: string): ProductItem | undefined {
  return collectionProducts.find((p) => p.id === id);
}
`;

fs.writeFileSync('src/content/products.ts', fileContent, 'utf8');
console.log('src/content/products.ts generated successfully!');
