"use client";

import { useEffect, useRef, useState } from "react";
import Image from "next/image";
import { ChevronLeft, ChevronRight, Eye } from "lucide-react";

import { ProductCategory, ProductItem } from "@/content/products";

interface ProductGalleryRowProps {
  category: ProductCategory & { products: ProductItem[] };
  onSelectProduct: (product: ProductItem) => void;
}

export function ProductGalleryRow({
  category,
  onSelectProduct,
}: ProductGalleryRowProps) {
  const scrollContainerRef = useRef<HTMLDivElement>(null);
  const [canScrollLeft, setCanScrollLeft] = useState(false);
  const [canScrollRight, setCanScrollRight] = useState(true);
  const [scrollProgress, setScrollProgress] = useState(0);

  const checkScroll = () => {
    const el = scrollContainerRef.current;
    if (!el) return;

    const { scrollLeft, scrollWidth, clientWidth } = el;
    setCanScrollLeft(scrollLeft > 5);
    setCanScrollRight(scrollLeft < scrollWidth - clientWidth - 5);

    if (scrollWidth - clientWidth > 0) {
      const progress = Math.min(
        100,
        Math.max(0, (scrollLeft / (scrollWidth - clientWidth)) * 100)
      );
      setScrollProgress(progress);
    }
  };

  useEffect(() => {
    checkScroll();
    const el = scrollContainerRef.current;
    if (!el) return;

    el.addEventListener("scroll", checkScroll, { passive: true });
    window.addEventListener("resize", checkScroll);

    return () => {
      el.removeEventListener("scroll", checkScroll);
      window.removeEventListener("resize", checkScroll);
    };
  }, []);

  const handleScroll = (direction: "left" | "right") => {
    const el = scrollContainerRef.current;
    if (!el) return;

    const cardWidth = el.firstElementChild
      ? (el.firstElementChild as HTMLElement).offsetWidth + 20
      : 300;
    const scrollAmount = direction === "left" ? -cardWidth * 2 : cardWidth * 2;

    el.scrollBy({
      left: scrollAmount,
      behavior: "smooth",
    });
  };

  return (
    <section
      id={category.id}
      className="group relative border-b border-[var(--line)] py-16 sm:py-20"
      aria-label={`${category.name} gallery`}
    >
      <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        {/* Category Header */}
        <div className="flex flex-col justify-between gap-4 md:flex-row md:items-end">
          <div>
            <div className="flex items-center gap-3">
              <span className="h-2 w-2 rounded-full bg-[var(--gold-dark)]" />
              <h2 className="font-serif text-2xl font-medium tracking-tight text-[var(--ink)] sm:text-3xl">
                {category.name}
              </h2>
              <span className="rounded-full border border-[rgba(198,165,92,0.3)] bg-white px-2.5 py-0.5 text-xs font-semibold text-[#7d7164]">
                {category.products.length} Products
              </span>
            </div>
            <p className="mt-2 max-w-2xl text-sm leading-relaxed text-[#5c5246] sm:text-base">
              {category.description}
            </p>
          </div>

          {/* Desktop & Tablet Gallery Navigation Controls */}
          <div className="flex items-center gap-3">
            {/* Position indicator */}
            <div
              className="hidden h-1.5 w-24 overflow-hidden rounded-full bg-[var(--line)] sm:block"
              aria-hidden="true"
            >
              <div
                className="h-full bg-[var(--gold-dark)] transition-all duration-300"
                style={{ width: `${Math.max(15, scrollProgress)}%` }}
              />
            </div>

            <div className="flex items-center gap-2">
              <button
                type="button"
                onClick={() => handleScroll("left")}
                disabled={!canScrollLeft}
                aria-label={`Scroll ${category.name} products left`}
                className={`inline-flex min-h-11 min-w-11 items-center justify-center rounded-full border transition-all focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)] ${
                  canScrollLeft
                    ? "border-[var(--gold-dark)] bg-white text-[var(--ink)] shadow-sm hover:bg-[var(--ink)] hover:text-[var(--ivory)]"
                    : "cursor-not-allowed border-black/10 bg-black/5 text-black/25 opacity-40"
                }`}
              >
                <ChevronLeft className="h-5 w-5" aria-hidden="true" />
              </button>

              <button
                type="button"
                onClick={() => handleScroll("right")}
                disabled={!canScrollRight}
                aria-label={`Scroll ${category.name} products right`}
                className={`inline-flex min-h-11 min-w-11 items-center justify-center rounded-full border transition-all focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)] ${
                  canScrollRight
                    ? "border-[var(--gold-dark)] bg-white text-[var(--ink)] shadow-sm hover:bg-[var(--ink)] hover:text-[var(--ivory)]"
                    : "cursor-not-allowed border-black/10 bg-black/5 text-black/25 opacity-40"
                }`}
              >
                <ChevronRight className="h-5 w-5" aria-hidden="true" />
              </button>
            </div>
          </div>
        </div>

        {/* Scrollable Products Strip */}
        <div className="relative mt-8">
          <div
            ref={scrollContainerRef}
            tabIndex={0}
            aria-label={`${category.name} product list. Use left and right arrow keys or scroll buttons to navigate.`}
            className="flex gap-4 overflow-x-auto no-scrollbar scroll-smooth pb-4 pt-2 snap-x snap-mandatory focus-visible:outline-none"
            onKeyDown={(e) => {
              if (e.key === "ArrowLeft") {
                e.preventDefault();
                handleScroll("left");
              } else if (e.key === "ArrowRight") {
                e.preventDefault();
                handleScroll("right");
              }
            }}
          >
            {category.products.map((product) => (
              <div
                key={product.id}
                className="w-[78vw] max-w-[300px] shrink-0 snap-start sm:w-[280px] lg:w-[300px]"
              >
                <button
                  type="button"
                  onClick={() => onSelectProduct(product)}
                  className="group/card flex h-full w-full flex-col overflow-hidden rounded-xl border border-[rgba(198,165,92,0.25)] bg-white p-4 text-left shadow-sm transition-all duration-300 hover:-translate-y-1 hover:border-[var(--gold-dark)] hover:shadow-md focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)]"
                  aria-label={`View details for ${product.name}`}
                >
                  {/* Image container */}
                  <div className="relative aspect-square w-full overflow-hidden rounded-lg bg-[#fbf9f5]">
                    <Image
                      src={product.imageSrc}
                      alt={product.alt}
                      fill
                      unoptimized
                      loading="lazy"
                      sizes="(max-width: 640px) 78vw, (max-width: 1024px) 280px, 300px"
                      className="object-contain p-4 transition-transform duration-500 group-hover/card:scale-105"
                    />

                    {/* Coming Soon Tag */}
                    <div className="absolute top-2.5 left-2.5 rounded-full border border-[rgba(198,165,92,0.4)] bg-[rgba(250,247,240,0.92)] px-2.5 py-0.5 text-[0.65rem] font-bold uppercase tracking-wider text-[var(--gold-dark)] backdrop-blur-sm">
                      {product.status}
                    </div>

                    {/* Hover Quick View Overlay */}
                    <div className="absolute inset-0 flex items-center justify-center bg-black/20 opacity-0 backdrop-blur-[2px] transition-opacity duration-300 group-hover/card:opacity-100">
                      <span className="inline-flex items-center gap-1.5 rounded-full bg-[var(--ink)] px-3 py-1.5 text-xs font-semibold text-[var(--ivory)] shadow-lg">
                        <Eye className="h-3.5 w-3.5" aria-hidden="true" />
                        Preview
                      </span>
                    </div>
                  </div>

                  {/* Product Details */}
                  <div className="mt-4 flex flex-1 flex-col justify-between">
                    <div>
                      <p className="text-[0.7rem] font-bold uppercase tracking-wider text-[#8b7d6c]">
                        {product.subcategory}
                      </p>
                      <h3 className="mt-1 font-serif text-base font-medium text-[var(--ink)] group-hover/card:text-[var(--gold-dark)] sm:text-lg">
                        {product.name}
                      </h3>
                    </div>

                    <div className="mt-4 flex items-center justify-between border-t border-[var(--line)]/60 pt-3 text-xs font-medium text-[#7d7164]">
                      <span>Curated Formulation</span>
                      <span className="font-semibold text-[var(--gold-dark)]">
                        Launch Details →
                      </span>
                    </div>
                  </div>
                </button>
              </div>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
