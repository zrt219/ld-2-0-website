import type { Metadata } from "next";

import { collectionMeta, getActiveCategories } from "@/content/products";
import { PageShell } from "@/components/PageShell";
import { CollectionHero } from "@/components/collection/CollectionHero";
import { CollectionClientView } from "@/components/collection/CollectionClientView";

export const metadata: Metadata = {
  title: collectionMeta.seoTitle,
  description: collectionMeta.seoDescription,
  alternates: {
    canonical: collectionMeta.canonicalUrl,
  },
  openGraph: {
    title: collectionMeta.seoTitle,
    description: collectionMeta.seoDescription,
    url: collectionMeta.canonicalUrl,
    siteName: "Lornette Daye",
    images: [
      {
        url: collectionMeta.ogImage,
        width: 1200,
        height: 630,
        alt: collectionMeta.title,
      },
    ],
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: collectionMeta.seoTitle,
    description: collectionMeta.seoDescription,
    images: [collectionMeta.ogImage],
  },
};

export default function CollectionPage() {
  const activeCategories = getActiveCategories();

  return (
    <PageShell>
      <main className="bg-[var(--ivory)] text-[var(--ink)]">
        {/* Editorial Hero Section */}
        <CollectionHero />

        {/* Interactive Category Galleries, Lightbox & Interest Form */}
        <CollectionClientView categories={activeCategories} />
      </main>
    </PageShell>
  );
}
