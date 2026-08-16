"use client";

import { useEffect, useRef, useCallback } from "react";
import Image from "next/image";
import { motion, AnimatePresence } from "framer-motion";
import { X, ChevronLeft, ChevronRight, Sparkles, Bell } from "lucide-react";

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
          className="fixed inset-0 z-50 flex items-center justify-center p-4 sm:p-6 lg:p-8"
          ref={dialogRef}
        >
          {/* Backdrop Blur */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.3 }}
            className="fixed inset-0 bg-black/75 backdrop-blur-md"
            onClick={onClose}
            aria-hidden="true"
          />

          {/* Modal Container */}
          <motion.div
            initial={{ opacity: 0, scale: 0.95, y: 16 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.95, y: 16 }}
            transition={{ type: "spring", stiffness: 320, damping: 28 }}
            className="relative z-10 mx-auto flex max-h-[90vh] w-full max-w-4xl flex-col overflow-hidden rounded-2xl border border-[rgba(198,165,92,0.35)] bg-[var(--ivory)] shadow-2xl"
            onTouchStart={handleTouchStart}
            onTouchEnd={handleTouchEnd}
          >
            {/* Top Action Header */}
            <div className="flex items-center justify-between border-b border-[var(--line)] bg-white/90 px-5 py-3.5 backdrop-blur-sm">
              <div className="flex items-center gap-2">
                <span className="rounded-full bg-[var(--champagne)]/20 px-2.5 py-0.5 text-xs font-bold uppercase tracking-wider text-[var(--gold-dark)]">
                  {product.categoryName}
                </span>
                <span className="text-xs font-medium text-[#7d7164]">
                  ({currentIndex + 1} of {products.length})
                </span>
              </div>

              <motion.button
                type="button"
                onClick={onClose}
                whileHover={{ scale: 1.1, rotate: 90 }}
                whileTap={{ scale: 0.9 }}
                aria-label="Close product preview"
                className="inline-flex min-h-11 min-w-11 items-center justify-center rounded-full text-[var(--charcoal)] transition hover:bg-black/5 hover:text-[var(--ink)] focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)]"
              >
                <X className="h-6 w-6" aria-hidden="true" />
              </motion.button>
            </div>

            {/* Content Body */}
            <div className="grid flex-1 overflow-y-auto md:grid-cols-[1.1fr_0.9fr]">
              {/* Image Showcase Area */}
              <div className="relative flex aspect-square items-center justify-center bg-gradient-to-b from-[#fdfbf7] to-[#f4ede2] p-6 md:p-10">
                <AnimatePresence mode="wait">
                  <motion.div
                    key={product.id}
                    initial={{ opacity: 0, scale: 0.92 }}
                    animate={{ opacity: 1, scale: 1 }}
                    exit={{ opacity: 0, scale: 0.92 }}
                    transition={{ duration: 0.25 }}
                    className="relative h-full w-full"
                  >
                    <Image
                      src={product.image}
                      alt={product.name}
                      fill
                      priority
                      unoptimized
                      sizes="(max-width: 768px) 90vw, 450px"
                      className="object-contain drop-shadow-md transition-all duration-300"
                    />
                  </motion.div>
                </AnimatePresence>

                {/* Prev / Next floating overlay controls for Desktop/Tablet */}
                <motion.button
                  type="button"
                  onClick={handlePrev}
                  whileHover={{ scale: 1.1, x: -2 }}
                  whileTap={{ scale: 0.9 }}
                  aria-label="Previous product in collection"
                  className="absolute left-3 top-1/2 -translate-y-1/2 inline-flex min-h-11 min-w-11 items-center justify-center rounded-full border border-[rgba(198,165,92,0.4)] bg-white/90 text-[var(--ink)] shadow-md transition hover:bg-[var(--ink)] hover:text-[var(--ivory)] focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)]"
                >
                  <ChevronLeft className="h-6 w-6" aria-hidden="true" />
                </motion.button>

                <motion.button
                  type="button"
                  onClick={handleNext}
                  whileHover={{ scale: 1.1, x: 2 }}
                  whileTap={{ scale: 0.9 }}
                  aria-label="Next product in collection"
                  className="absolute right-3 top-1/2 -translate-y-1/2 inline-flex min-h-11 min-w-11 items-center justify-center rounded-full border border-[rgba(198,165,92,0.4)] bg-white/90 text-[var(--ink)] shadow-md transition hover:bg-[var(--ink)] hover:text-[var(--ivory)] focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)]"
                >
                  <ChevronRight className="h-6 w-6" aria-hidden="true" />
                </motion.button>
              </div>

              {/* Product Details & Launch Info */}
              <div className="flex flex-col justify-between bg-white p-6 sm:p-8">
                <div>
                  <div className="flex items-center gap-2">
                    <Sparkles className="h-4 w-4 text-[var(--gold-dark)]" aria-hidden="true" />
                    <span className="text-xs font-bold uppercase tracking-widest text-[var(--gold-dark)]">
                      Coming Soon • Exclusive Preview
                    </span>
                  </div>

                  <AnimatePresence mode="wait">
                    <motion.div
                      key={product.id}
                      initial={{ opacity: 0, y: 8 }}
                      animate={{ opacity: 1, y: 0 }}
                      exit={{ opacity: 0, y: -8 }}
                      transition={{ duration: 0.2 }}
                    >
                      <h3
                        id="lightbox-product-title"
                        className="mt-3 font-serif text-2xl font-medium tracking-tight text-[var(--ink)] sm:text-3xl"
                      >
                        {product.name}
                      </h3>

                      <div className="mt-3 flex flex-wrap gap-2 text-xs">
                        <span className="rounded-md border border-[var(--line)] bg-[var(--ivory)] px-2.5 py-1 font-semibold text-[var(--charcoal)]">
                          {product.subcategory}
                        </span>
                        {product.fabric && (
                          <span className="rounded-md border border-[var(--line)] bg-[var(--ivory)] px-2.5 py-1 font-semibold text-[var(--charcoal)]">
                            {product.fabric}
                          </span>
                        )}
                        {product.fit && (
                          <span className="rounded-md border border-[var(--line)] bg-[var(--ivory)] px-2.5 py-1 font-semibold text-[var(--charcoal)]">
                            Fit: {product.fit}
                          </span>
                        )}
                      </div>

                      <div className="mt-5 space-y-4 text-sm leading-relaxed text-[#5c5246]">
                        <p className="font-medium text-[var(--ink)]">
                          {product.shortDescription}
                        </p>

                        {product.curationReason && (
                          <div className="rounded-lg border border-[rgba(198,165,92,0.25)] bg-[#faf7f0] p-3 text-xs text-[#736657]">
                            <strong className="text-[var(--ink)] block mb-1 font-serif text-sm">Why Lornette Curated This:</strong>
                            {product.curationReason}
                          </div>
                        )}

                        {product.details && product.details.length > 0 && (
                          <div className="space-y-1.5 pt-1">
                            <span className="text-xs font-bold uppercase tracking-wider text-[var(--charcoal)]">Craftsmanship & Features:</span>
                            <ul className="list-disc pl-4 text-xs space-y-1 text-[#6b5f52]">
                              {product.details.map((detail, idx) => (
                                <li key={idx}>{detail}</li>
                              ))}
                            </ul>
                          </div>
                        )}

                        {product.editorialQuote && (
                          <p className="italic text-xs text-[var(--gold-dark)] border-l-2 border-[var(--gold-dark)] pl-3 py-1">
                            &ldquo;{product.editorialQuote}&rdquo;
                          </p>
                        )}
                      </div>
                    </motion.div>
                  </AnimatePresence>
                </div>

                <div className="mt-8 border-t border-[var(--line)] pt-6">
                  <motion.button
                    type="button"
                    onClick={() => {
                      onClose();
                      onJoinInterest(product.categoryName);
                    }}
                    whileHover={{ scale: 1.02 }}
                    whileTap={{ scale: 0.98 }}
                    className="inline-flex min-h-12 w-full items-center justify-center gap-2 rounded-lg bg-[var(--ink)] px-6 text-sm font-bold uppercase tracking-wider text-[var(--ivory)] shadow-md transition-all hover:bg-[var(--gold-dark)] focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)]"
                  >
                    <Bell className="h-4 w-4" aria-hidden="true" />
                    Join Priority List for {product.name}
                  </motion.button>
                </div>
              </div>
            </div>
          </motion.div>
        </div>
      )}
    </AnimatePresence>
  );
}
