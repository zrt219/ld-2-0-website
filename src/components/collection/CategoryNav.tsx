"use client";

import { useEffect, useState } from "react";
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

  const scrollToCategory = (id: string) => {
    const el = document.getElementById(id);
    if (el) {
      const headerOffset = 130;
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

  return (
    <div
      id="categories"
      className="sticky top-[73px] z-40 border-b border-[rgba(198,165,92,0.3)] bg-[rgba(250,247,240,0.96)] px-4 py-3.5 shadow-sm backdrop-blur-md transition-all sm:px-6 lg:px-8"
    >
      <div className="mx-auto flex max-w-7xl items-center justify-between gap-4">
        <div className="flex items-center gap-2 overflow-x-auto no-scrollbar py-1">
          <span className="mr-2 hidden text-xs font-bold uppercase tracking-widest text-[#7d7164] sm:inline-block">
            Categories:
          </span>
          {categories.map((cat) => {
            const isActive = currentSection === cat.id;
            return (
              <button
                key={cat.id}
                type="button"
                onClick={() => scrollToCategory(cat.id)}
                aria-current={isActive ? "true" : undefined}
                className={`group inline-flex shrink-0 items-center gap-2 rounded-full border px-4 py-2 text-xs font-semibold uppercase tracking-wider transition-all duration-200 focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)] ${
                  isActive
                    ? "border-[var(--gold-dark)] bg-[var(--ink)] text-[var(--ivory)] shadow-sm"
                    : "border-[rgba(198,165,92,0.35)] bg-white/80 text-[var(--charcoal)] hover:border-[var(--gold-dark)] hover:bg-white"
                }`}
              >
                <span>{cat.name}</span>
                <span
                  className={`rounded-full px-1.5 py-0.5 text-[0.65rem] font-bold ${
                    isActive
                      ? "bg-[var(--gold-dark)] text-white"
                      : "bg-[var(--line)] text-[#6a5e50] group-hover:bg-[#dfd1bd]"
                  }`}
                >
                  {cat.products.length}
                </span>
              </button>
            );
          })}
        </div>

        <a
          href="#interest-list"
          className="hidden shrink-0 text-xs font-bold uppercase tracking-wider text-[var(--gold-dark)] transition hover:text-[var(--ink)] hover:underline md:inline-block"
        >
          Join Interest List →
        </a>
      </div>
    </div>
  );
}
