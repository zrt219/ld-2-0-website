import fs from "node:fs";

const catalogue = JSON.parse(
  fs.readFileSync("public/products/umattr-product-catalogue.json", "utf8")
);

const themes = [
  {
    id: "hair-cleansing-moisture",
    name: "Hair Cleansing & Moisture",
    description:
      "Deep hydration shampoos, revitalizing masks, botanical leave-in conditioners, and weightless styling mists crafted for crown vitality.",
  },
  {
    id: "scalp-growth-oils",
    name: "Scalp & Hair Growth Oils",
    description:
      "Nutrient-dense scalp treatments, growth-look serums, nourishing black hair oils, and protective satin nightwear essentials.",
  },
  {
    id: "luxury-wigs-extensions",
    name: "Luxury Wigs & Clip-In Extensions",
    description:
      "Couture lace front wigs, custom closures, headband units, sleek bobs, and premium clip-in extensions tailored for versatile elegance.",
  },
  {
    id: "serums-facial-treatments",
    name: "Serums & Facial Treatments",
    description:
      "Gentle botanical cleansers, toning mists, vitamin glow infusions, and purifying clay masks that elevate your daily ritual.",
  },
  {
    id: "body-barrier-creams",
    name: "Body & Barrier Creams",
    description:
      "Rich lipid-barrier moisturizers, velvety body butters, hand creams, and curated winter ritual sets for lasting all-over hydration.",
  },
  {
    id: "primers-complexion-glow",
    name: "Primers & Complexion Glow",
    description:
      "Radiance-boosting primers, luminous skin tints, seamless concealers, contour sticks, and silky powders designed to enhance natural beauty.",
  },
];

function getThemeForSequence(seq) {
  if ([1, 2, 3, 4, 5, 9, 10, 12, 13, 14, 17, 20].includes(seq)) {
    return themes[0]; // Hair Cleansing & Moisture
  }
  if ([6, 7, 8, 11, 15, 16, 18, 19].includes(seq)) {
    return themes[1]; // Scalp & Hair Growth Oils
  }
  if (seq >= 21 && seq <= 40) {
    return themes[2]; // Luxury Wigs & Extensions
  }
  if ([41, 42, 43, 44, 45, 46, 50, 55, 56, 57].includes(seq)) {
    return themes[3]; // Serums & Facial Treatments
  }
  if ([47, 48, 49, 51, 52, 53, 54, 58, 59, 60].includes(seq)) {
    return themes[4]; // Body & Barrier Creams
  }
  if (seq >= 61 && seq <= 72) {
    return themes[5]; // Primers & Complexion Glow
  }
  return themes[0];
}

const products = [];
for (let i = 1; i <= 72; i++) {
  const catItem = catalogue.find((c) => c.sequence === i);
  if (!catItem) continue;

  const padded = String(i).padStart(2, "0");
  const theme = getThemeForSequence(i);

  products.push({
    id: "product-" + padded,
    sequence: i,
    name: catItem.name,
    categoryName: theme.name,
    categorySlug: theme.id,
    subcategory: catItem.subcategory,
    originalCategory: catItem.category,
    imageSrc: "/products/clean/product-" + padded + ".png",
    alt: `${catItem.name} — Curated by Lornette Daye`,
    status: "Coming Soon",
    displayOrder: i,
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
export const allProductCategories: ProductCategory[] = ${JSON.stringify(
  themes,
  null,
  2
)};

export const collectionProducts: ProductItem[] = ${JSON.stringify(
  products,
  null,
  2
)};

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

fs.writeFileSync("src/content/products.ts", fileContent, "utf8");
console.log("src/content/products.ts regenerated with 6 distinct thematic galleries!");
