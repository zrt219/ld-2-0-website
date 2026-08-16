"use client";

import { useEffect, useRef, useCallback } from "react";
import Image from "next/image";
import { motion, AnimatePresence } from "framer-motion";
import { X, ChevronLeft, ChevronRight, Sparkles, Bell, CheckCircle2, Quote } from "lucide-react";

import { ProductItem } from "@/content/products";

interface ProductLightboxProps {
  product: ProductItem | null;
  products: ProductItem[];
  isOpen: boolean;
  onClose: () => void;
  onSelectProduct: (product: ProductItem) => void;
  onJoinInterest: (categoryName: string) => void;
}

export function ProductLightbox({
  product,
  products,
  isOpen,
  onClose,
  onSelectProduct,
  onJoinInterest,
}: ProductLightboxProps) {
  const dialogRef = useRef<HTMLDivElement>(null);
  const triggerElementRef = useRef<HTMLElement | null>(null);
  const touchStartX = useRef<number | null>(null);

  // Store active element before opening to return focus on close
  useEffect(() => {
    if (isOpen) {
      triggerElementRef.current = document.activeElement as HTMLElement;
      document.body.style.overflow = "hidden";
    } else {
      document.body.style.overflow = "";
      if (triggerElementRef.current) {
        triggerElementRef.current.focus();
      }
    }
    return () => {
      document.body.style.overflow = "";
    };
  }, [isOpen]);

  const currentIndex = product
    ? products.findIndex((p) => p.id === product.id)
    : -1;

  const handlePrev = useCallback(() => {
    if (currentIndex > 0) {
      onSelectProduct(products[currentIndex - 1]);
    } else if (currentIndex === 0) {
      onSelectProduct(products[products.length - 1]);
    }
  }, [currentIndex, products, onSelectProduct]);

  const handleNext = useCallback(() => {
    if (currentIndex >= 0 && currentIndex < products.length - 1) {
      onSelectProduct(products[currentIndex + 1]);
    } else if (currentIndex === products.length - 1) {
      onSelectProduct(products[0]);
    }
  }, [currentIndex, products, onSelectProduct]);

  // Keyboard navigation
  useEffect(() => {
    if (!isOpen) return;

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        e.preventDefault();
        onClose();
      } else if (e.key === "ArrowLeft") {
        e.preventDefault();
        handlePrev();
      } else if (e.key === "ArrowRight") {
        e.preventDefault();
        handleNext();
      } else if (e.key === "Tab") {
        if (!dialogRef.current) return;
        const focusableElements = dialogRef.current.querySelectorAll<HTMLElement>(
          'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
        );
        if (focusableElements.length === 0) return;

        const firstElement = focusableElements[0];
        const lastElement = focusableElements[focusableElements.length - 1];

        if (e.shiftKey && document.activeElement === firstElement) {
          e.preventDefault();
          lastElement.focus();
        } else if (!e.shiftKey && document.activeElement === lastElement) {
          e.preventDefault();
          firstElement.focus();
        }
      }
    };

    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [isOpen, handlePrev, handleNext, onClose]);

  // Touch Swipe Handlers for Mobile
  const handleTouchStart = (e: React.TouchEvent) => {
    touchStartX.current = e.touches[0].clientX;
  };

  const handleTouchEnd = (e: React.TouchEvent) => {
    if (touchStartX.current === null) return;
    const touchEndX = e.changedTouches[0].clientX;
    const diff = touchStartX.current - touchEndX;

    if (Math.abs(diff) > 50) {
      if (diff > 0) {
        handleNext();
      } else {
        handlePrev();
      }
    }
    touchStartX.current = null;
  };

  return (
    <AnimatePresence>
      {isOpen && product && (
        <div
          role="dialog"
          aria-modal="true"
          aria-labelledby="lightbox-product-title"
          className="fixed inset-0 z-50 flex items-center justify-center p-3 sm:p-5 lg:p-8"
          ref={dialogRef}
        >
          {/* Backdrop Blur */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.3 }}
            className="fixed inset-0 bg-black/80 backdrop-blur-md"
            onClick={onClose}
            aria-hidden="true"
          />

          {/* Modal Container */}
          <motion.div
            initial={{ opacity: 0, scale: 0.94, y: 20 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.94, y: 20 }}
            transition={{ type: "spring", stiffness: 340, damping: 28 }}
            className="relative z-10 mx-auto flex max-h-[92vh] w-full max-w-5xl flex-col overflow-hidden rounded-2xl border border-[rgba(198,165,92,0.4)] bg-[var(--ivory)] shadow-2xl"
            onTouchStart={handleTouchStart}
            onTouchEnd={handleTouchEnd}
          >
            {/* Top Action Bar */}
            <div className="flex items-center justify-between border-b border-[var(--line)] bg-white/95 px-5 py-3.5 backdrop-blur-sm">
              <div className="flex items-center gap-3">
                <span className="rounded-full bg-[var(--champagne)]/25 px-3 py-1 text-xs font-bold uppercase tracking-wider text-[var(--gold-dark)]">
                  {product.categoryName}
                </span>
                <span className="text-xs font-medium text-[#7d7164]">
                  Item {currentIndex + 1} of {products.length}
                </span>
              </div>

              <div className="flex items-center gap-2">
                {/* Navigation counter arrows */}
                <div className="flex items-center gap-1 mr-2">
                  <motion.button
                    type="button"
                    onClick={handlePrev}
                    whileHover={{ scale: 1.1 }}
                    whileTap={{ scale: 0.9 }}
                    aria-label="Previous product"
                    className="inline-flex h-8 w-8 items-center justify-center rounded-full border border-[rgba(198,165,92,0.3)] bg-white text-[var(--ink)] transition hover:bg-[var(--ink)] hover:text-white"
                  >
                    <ChevronLeft className="h-4 w-4" />
                  </motion.button>
                  <motion.button
                    type="button"
                    onClick={handleNext}
                    whileHover={{ scale: 1.1 }}
                    whileTap={{ scale: 0.9 }}
                    aria-label="Next product"
                    className="inline-flex h-8 w-8 items-center justify-center rounded-full border border-[rgba(198,165,92,0.3)] bg-white text-[var(--ink)] transition hover:bg-[var(--ink)] hover:text-white"
                  >
                    <ChevronRight className="h-4 w-4" />
                  </motion.button>
                </div>

                <motion.button
                  type="button"
                  onClick={onClose}
                  whileHover={{ scale: 1.1, rotate: 90 }}
                  whileTap={{ scale: 0.9 }}
                  aria-label="Close product preview"
                  className="inline-flex h-9 w-9 items-center justify-center rounded-full border border-[rgba(198,165,92,0.2)] bg-[#faf7f0] text-[var(--charcoal)] transition hover:bg-black/10 hover:text-[var(--ink)] focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)]"
                >
                  <X className="h-5 w-5" aria-hidden="true" />
                </motion.button>
              </div>
            </div>

            {/* Content Body: 50/50 Split View */}
            <div className="grid flex-1 overflow-hidden md:grid-cols-2 md:max-h-[calc(92vh-60px)]">
              {/* Left Column: Image Showcase Area */}
              <div className="relative flex min-h-[300px] sm:min-h-[380px] md:min-h-full items-center justify-center bg-gradient-to-b from-[#fdfbf7] via-[#f7f2e9] to-[#eee5d5] p-6 sm:p-8 lg:p-10 border-b md:border-b-0 md:border-r border-[var(--line)]">
                <AnimatePresence mode="wait">
                  <motion.div
                    key={product.id}
                    initial={{ opacity: 0, scale: 0.94 }}
                    animate={{ opacity: 1, scale: 1 }}
                    exit={{ opacity: 0, scale: 0.94 }}
                    transition={{ duration: 0.25 }}
                    className="relative aspect-square h-full w-full max-w-[420px]"
                  >
                    <Image
                      src={product.image}
                      alt={product.name}
                      fill
                      priority
                      unoptimized
                      sizes="(max-width: 768px) 90vw, 500px"
                      className="object-contain drop-shadow-xl transition-all duration-300"
                    />
                  </motion.div>
                </AnimatePresence>

                {/* Left/Right Floating Quick Arrows over Image on Mobile/Desktop */}
                <motion.button
                  type="button"
                  onClick={handlePrev}
                  whileHover={{ scale: 1.1, x: -2 }}
                  whileTap={{ scale: 0.9 }}
                  aria-label="Previous product in collection"
                  className="absolute left-3 top-1/2 -translate-y-1/2 inline-flex h-10 w-10 items-center justify-center rounded-full border border-[rgba(198,165,92,0.4)] bg-white/90 text-[var(--ink)] shadow-md transition hover:bg-[var(--ink)] hover:text-white"
                >
                  <ChevronLeft className="h-5 w-5" aria-hidden="true" />
                </motion.button>

                <motion.button
                  type="button"
                  onClick={handleNext}
                  whileHover={{ scale: 1.1, x: 2 }}
                  whileTap={{ scale: 0.9 }}
                  aria-label="Next product in collection"
                  className="absolute right-3 top-1/2 -translate-y-1/2 inline-flex h-10 w-10 items-center justify-center rounded-full border border-[rgba(198,165,92,0.4)] bg-white/90 text-[var(--ink)] shadow-md transition hover:bg-[var(--ink)] hover:text-white"
                >
                  <ChevronRight className="h-5 w-5" aria-hidden="true" />
                </motion.button>
              </div>

              {/* Right Column: Full Product Details, Story & Specs (Clean Scrollable Panel) */}
              <div className="flex flex-col justify-between overflow-y-auto overflow-x-hidden bg-white p-6 sm:p-8 lg:p-10 [scrollbar-width:thin]">
                <div>
                  {/* Eyebrow badge */}
                  <div className="flex items-center gap-2">
                    <Sparkles className="h-4 w-4 text-[var(--gold-dark)]" aria-hidden="true" />
                    <span className="text-[0.7rem] font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)]">
                      Coming Soon • Private Preview
                    </span>
                  </div>

                  <AnimatePresence mode="wait">
                    <motion.div
                      key={product.id}
                      initial={{ opacity: 0, y: 10 }}
                      animate={{ opacity: 1, y: 0 }}
                      exit={{ opacity: 0, y: -10 }}
                      transition={{ duration: 0.2 }}
                      className="mt-3"
                    >
                      {/* Product Title */}
                      <h3
                        id="lightbox-product-title"
                        className="font-serif text-2xl font-normal leading-snug tracking-tight text-[var(--ink)] sm:text-3xl lg:text-[2rem]"
                      >
                        {product.name}
                      </h3>

                      {/* Attribute Pills */}
                      <div className="mt-3.5 flex flex-wrap gap-2 text-xs">
                        <span className="rounded-full border border-[rgba(198,165,92,0.4)] bg-[var(--ivory)] px-3 py-1 font-semibold text-[var(--charcoal)]">
                          {product.subcategory}
                        </span>
                        {product.fabric && (
                          <span className="rounded-full border border-[rgba(198,165,92,0.3)] bg-white px-3 py-1 font-medium text-[#6b5f52]">
                            {product.fabric}
                          </span>
                        )}
                        {product.fit && (
                          <span className="rounded-full border border-[rgba(198,165,92,0.3)] bg-white px-3 py-1 font-medium text-[#6b5f52]">
                            {product.fit}
                          </span>
                        )}
                      </div>

                      {/* Overview & Short Description */}
                      <div className="mt-5 space-y-4 text-sm leading-relaxed text-[#4a4237]">
                        <p className="text-base font-normal text-[var(--ink)] leading-relaxed">
                          {product.shortDescription}
                        </p>

                        {/* Curation Narrative Box */}
                        {product.curationReason && (
                          <div className="relative rounded-xl border border-[rgba(198,165,92,0.35)] bg-[#faf7f0] p-4 text-xs sm:text-sm text-[#5a4e40]">
                            <div className="flex items-center gap-1.5 font-serif font-semibold text-[var(--ink)] mb-1.5 text-sm">
                              <Quote className="h-3.5 w-3.5 text-[var(--gold-dark)]" />
                              <span>Why Lornette Curated This:</span>
                            </div>
                            <p className="leading-relaxed">
                              {product.curationReason}
                            </p>
                          </div>
                        )}

                        {/* Craftsmanship & Specifications */}
                        {product.details && product.details.length > 0 && (
                          <div className="space-y-2 pt-2">
                            <span className="text-xs font-bold uppercase tracking-wider text-[var(--ink)] block">
                              Craftsmanship & Features:
                            </span>
                            <ul className="space-y-2 text-xs sm:text-sm text-[#5a4e40]">
                              {product.details.map((detail, idx) => (
                                <li key={idx} className="flex items-start gap-2">
                                  <CheckCircle2 className="h-4 w-4 shrink-0 text-[var(--gold-dark)] mt-0.5" />
                                  <span className="leading-snug">{detail}</span>
                                </li>
                              ))}
                            </ul>
                          </div>
                        )}

                        {/* Editorial Quote */}
                        {product.editorialQuote && (
                          <div className="border-l-2 border-[var(--gold-dark)] pl-3.5 py-1 text-xs sm:text-sm italic text-[var(--gold-dark)]">
                            &ldquo;{product.editorialQuote}&rdquo;
                          </div>
                        )}
                      </div>
                    </motion.div>
                  </AnimatePresence>
                </div>

                {/* Priority Reservation CTA Footer */}
                <div className="mt-8 border-t border-[var(--line)] pt-5">
                  <motion.button
                    type="button"
                    onClick={() => {
                      onClose();
                      onJoinInterest(product.categoryName);
                    }}
                    whileHover={{ scale: 1.02 }}
                    whileTap={{ scale: 0.98 }}
                    className="inline-flex min-h-12 w-full items-center justify-center gap-2 rounded-xl bg-[var(--ink)] px-6 text-sm font-bold uppercase tracking-wider text-[var(--ivory)] shadow-md transition-all hover:bg-[var(--gold-dark)] focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)]"
                  >
                    <Bell className="h-4 w-4" aria-hidden="true" />
                    <span>Join Priority List for This Item</span>
                  </motion.button>
                  <p className="mt-2 text-center text-[0.7rem] text-[#8b7d6c]">
                    Private launch announcements and early reservations will be shared exclusively with registered members.
                  </p>
                </div>
              </div>
            </div>
          </motion.div>
        </div>
      )}
    </AnimatePresence>
  );
}
