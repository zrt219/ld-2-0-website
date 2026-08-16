"use client";

import { useState } from "react";

import {
  ProductCategory,
  ProductItem,
  collectionProducts,
} from "@/content/products";
import { CategoryNav } from "./CategoryNav";
import { ProductGalleryRow } from "./ProductGalleryRow";
import { ProductLightbox } from "./ProductLightbox";
import { InterestForm } from "./InterestForm";

interface CollectionClientViewProps {
  categories: (ProductCategory & { products: ProductItem[] })[];
}

export function CollectionClientView({ categories }: CollectionClientViewProps) {
  const [selectedProduct, setSelectedProduct] = useState<ProductItem | null>(null);
  const [lightboxOpen, setLightboxOpen] = useState(false);
  const [formCategory, setFormCategory] = useState<string | undefined>(undefined);

  const handleOpenLightbox = (product: ProductItem) => {
    setSelectedProduct(product);
    setLightboxOpen(true);
  };

  const handleCloseLightbox = () => {
    setLightboxOpen(false);
  };

  const handleJoinInterestFromLightbox = (categoryName: string) => {
    setLightboxOpen(false);
    setFormCategory(categoryName);

    // Smooth scroll to interest form
    const el = document.getElementById("interest-list");
    if (el) {
      el.scrollIntoView({ behavior: "smooth" });
    }
  };

  return (
    <>
      {/* Sticky Category Filter Bar */}
      <CategoryNav categories={categories} />

      {/* Category Galleries */}
      <div className="space-y-0">
        {categories.map((category) => (
          <ProductGalleryRow
            key={category.id}
            category={category}
            onSelectProduct={handleOpenLightbox}
          />
        ))}
      </div>

      {/* Accessible Product Lightbox */}
      <ProductLightbox
        product={selectedProduct}
        products={collectionProducts}
        isOpen={lightboxOpen}
        onClose={handleCloseLightbox}
        onSelectProduct={setSelectedProduct}
        onJoinInterest={handleJoinInterestFromLightbox}
      />

      {/* Interest Capture Section */}
      <InterestForm initialSelectedCategory={formCategory} key={formCategory} />
    </>
  );
}
