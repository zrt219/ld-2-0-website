"use client";

import { useEffect, useRef, useState } from "react";
import { motion } from "framer-motion";
import { ChevronLeft, ChevronRight, Sparkles } from "lucide-react";
import { ProductCategory, ProductItem } from "@/content/products";

interface CategoryNavProps {
  categories: (ProductCategory & { products: ProductItem[] })[];
  activeId?: string;
  onSelectCategory?: (id: string) => void;
}

export function CategoryNav({ categories, activeId, onSelectCategory }: CategoryNavProps) {
  const [currentSection, setCurrentSection] = useState<string>(
    activeId || categories[0]?.id || ""
  );
  const scrollContainerRef = useRef<HTMLDivElement>(null);
  const [canScrollLeft, setCanScrollLeft] = useState(false);
  const [canScrollRight, setCanScrollRight] = useState(true);

  const checkScroll = () => {
    const el = scrollContainerRef.current;
    if (!el) return;
    setCanScrollLeft(el.scrollLeft > 10);
    setCanScrollRight(el.scrollLeft < el.scrollWidth - el.clientWidth - 10);
  };

  useEffect(() => {
    const handleScroll = () => {
      const scrollPosition = window.scrollY + 180;
      for (const cat of categories) {
        const el = document.getElementById(cat.id);
        if (el) {
          const top = el.offsetTop;
          const height = el.offsetHeight;
          if (scrollPosition >= top && scrollPosition < top + height) {
            setCurrentSection(cat.id);
            break;
          }
        }
      }
    };

    window.addEventListener("scroll", handleScroll, { passive: true });
    return () => window.removeEventListener("scroll", handleScroll);
  }, [categories]);

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

  const scrollToCategory = (id: string) => {
    const el = document.getElementById(id);
    if (el) {
      const headerOffset = 135;
      const elementPosition = el.getBoundingClientRect().top;
      const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

      window.scrollTo({
        top: offsetPosition,
        behavior: "smooth",
      });
      setCurrentSection(id);
      if (onSelectCategory) {
        onSelectCategory(id);
      }
    }
  };

  const handleArrowScroll = (direction: "left" | "right") => {
    const el = scrollContainerRef.current;
    if (!el) return;
    const distance = 220;
    el.scrollBy({
      left: direction === "left" ? -distance : distance,
      behavior: "smooth",
    });
  };

  return (
    <div
      id="categories"
      className="sticky top-[73px] z-40 border-b border-[rgba(198,165,92,0.35)] bg-[rgba(250,247,240,0.96)] px-3 py-3 shadow-[0_4px_20px_rgba(0,0,0,0.03)] backdrop-blur-md transition-all sm:px-6 lg:px-8"
    >
      <div className="mx-auto flex max-w-7xl items-center justify-between gap-3">
        {/* Category Label */}
        <div className="hidden shrink-0 items-center gap-1.5 font-serif text-xs font-semibold uppercase tracking-widest text-[#7d7164] lg:flex">
          <Sparkles className="h-3.5 w-3.5 text-[var(--gold-dark)]" />
          <span>Categories</span>
        </div>

        {/* Scrollable Pills Strip with Framer Motion Layout Transitions */}
        <div className="relative flex min-w-0 flex-1 items-center">
          {/* Left Arrow if scrollable */}
          {canScrollLeft && (
            <button
              type="button"
              onClick={() => handleArrowScroll("left")}
              aria-label="Scroll categories left"
              className="absolute left-0 z-20 hidden -translate-x-2 rounded-full border border-[rgba(198,165,92,0.4)] bg-white/95 p-1.5 text-[var(--ink)] shadow-md transition hover:bg-[var(--ink)] hover:text-white md:flex"
            >
              <ChevronLeft className="h-4 w-4" />
            </button>
          )}

          <div
            ref={scrollContainerRef}
            className="flex w-full items-center gap-2 overflow-x-auto py-1 scroll-smooth [scrollbar-width:none] [-ms-overflow-style:none] [&::-webkit-scrollbar]:hidden"
          >
            {categories.map((cat) => {
              const isActive = currentSection === cat.id;
              return (
                <motion.button
                  key={cat.id}
                  type="button"
                  onClick={() => scrollToCategory(cat.id)}
                  aria-current={isActive ? "true" : undefined}
                  whileHover={{ scale: 1.02 }}
                  whileTap={{ scale: 0.98 }}
                  className="relative shrink-0 rounded-full px-4 py-2 text-xs font-bold uppercase tracking-wider transition-colors focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)]"
                >
                  {/* Framer Motion Active Background Pill Indicator */}
                  {isActive && (
                    <motion.div
                      layoutId="activeCategoryPill"
                      className="absolute inset-0 rounded-full border border-[var(--gold-dark)] bg-[var(--ink)] shadow-sm"
                      transition={{ type: "spring", stiffness: 380, damping: 30 }}
                    />
                  )}

                  {!isActive && (
                    <div className="absolute inset-0 rounded-full border border-[rgba(198,165,92,0.35)] bg-white/80 transition-colors hover:border-[var(--gold-dark)] hover:bg-white" />
                  )}

                  <div className="relative z-10 flex items-center gap-2">
                    <span className={isActive ? "text-[var(--ivory)]" : "text-[var(--charcoal)]"}>
                      {cat.name}
                    </span>
                    <motion.span
                      layout
                      className={`rounded-full px-1.5 py-0.5 text-[0.65rem] font-bold transition-colors ${
                        isActive
                          ? "bg-[var(--gold-dark)] text-white"
                          : "bg-[var(--line)] text-[#6a5e50]"
                      }`}
                    >
                      {cat.products.length}
                    </motion.span>
                  </div>
                </motion.button>
              );
            })}
          </div>

          {/* Right Arrow if scrollable */}
          {canScrollRight && (
            <button
              type="button"
              onClick={() => handleArrowScroll("right")}
              aria-label="Scroll categories right"
              className="absolute right-0 z-20 hidden translate-x-2 rounded-full border border-[rgba(198,165,92,0.4)] bg-white/95 p-1.5 text-[var(--ink)] shadow-md transition hover:bg-[var(--ink)] hover:text-white md:flex"
            >
              <ChevronRight className="h-4 w-4" />
            </button>
          )}
        </div>

        {/* Priority CTA link */}
        <motion.a
          href="#interest-list"
          whileHover={{ x: 2 }}
          className="hidden shrink-0 text-xs font-bold uppercase tracking-wider text-[var(--gold-dark)] transition hover:text-[var(--ink)] sm:inline-block"
        >
          Priority List →
        </motion.a>
      </div>
    </div>
  );
}
