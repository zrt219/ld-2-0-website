"use client";

import Image from "next/image";
import { ChevronRight } from "lucide-react";
import { useState } from "react";

import type { AboutGallerySlide } from "@/content/aboutGallery";

type AboutGalleryProps = {
  slides: AboutGallerySlide[];
};

export function AboutGallery({ slides }: AboutGalleryProps) {
  const [activeIndex, setActiveIndex] = useState(0);
  const activeSlide = slides[activeIndex];
  const slidePosition = `Slide ${activeIndex + 1} of ${slides.length}`;

  function showNextSlide() {
    setActiveIndex((index) => (index + 1) % slides.length);
  }

  if (!activeSlide) {
    return null;
  }

  return (
    <section aria-label="Lornette story gallery" className="mx-auto mt-12 w-full max-w-3xl">
      <div className="overflow-hidden border border-[rgba(198,165,92,0.38)] bg-[rgba(250,247,240,0.78)] shadow-[0_18px_70px_rgba(23,20,18,0.06)]">
        <div className="bg-[var(--sand)] p-2 sm:p-3">
          <div className="relative aspect-[690/446]">
            <Image
              src={activeSlide.image.src}
              alt={activeSlide.image.alt}
              fill
              unoptimized
              sizes="(max-width: 768px) 92vw, 768px"
              className="h-full w-full object-contain"
            />
            <button
              type="button"
              aria-label="Show next gallery slide"
              onClick={showNextSlide}
              className="absolute right-3 top-1/2 inline-flex h-10 w-10 -translate-y-1/2 items-center justify-center rounded-full border border-[rgba(155,118,46,0.42)] bg-[rgba(250,247,240,0.96)] text-[var(--ink)] shadow-[0_10px_28px_rgba(23,20,18,0.14)] transition hover:border-[var(--champagne)] hover:bg-white sm:right-4 sm:h-11 sm:w-11"
            >
              <ChevronRight size={22} aria-hidden="true" />
            </button>
          </div>
        </div>
        <div
          aria-live="polite"
          className="border-t border-[rgba(198,165,92,0.28)] bg-[rgba(232,221,203,0.46)] px-5 py-5 sm:px-6 sm:py-6"
        >
          <p className="sr-only">{slidePosition}</p>
          <p className="text-[15px] font-medium leading-7 text-[var(--charcoal)] sm:text-base">
            {activeSlide.title}
          </p>
          <p className="mt-2 text-[15px] leading-7 text-[#675d50] sm:text-base">
            {activeSlide.body}
          </p>
        </div>
      </div>
    </section>
  );
}
