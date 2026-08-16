"use client";

import { useEffect, useRef, useState, useCallback } from "react";
import Image from "next/image";
import { motion, AnimatePresence } from "framer-motion";
import { ChevronLeft, ChevronRight, X, Maximize2 } from "lucide-react";

interface PeaceCard {
  id: string;
  src: string;
  alt: string;
  title: string;
}

const peaceCards: PeaceCard[] = [
  {
    id: "peace-1",
    src: "/PROTECT%20YOUR%20PEACE/chrome_Z0mWHeSwf3.png",
    alt: "Protect Your Peace - Rest is part of the process.",
    title: "Rest is part of the process.",
  },
  {
    id: "peace-2",
    src: "/PROTECT%20YOUR%20PEACE/chrome_fQgelmRc8R.png",
    alt: "Protect Your Peace - Remember you.",
    title: "Remember you.",
  },
  {
    id: "peace-3",
    src: "/PROTECT%20YOUR%20PEACE/chrome_gL6N0N70Ru.png",
    alt: "Protect Your Peace - You deserve hope.",
    title: "You deserve hope.",
  },
  {
    id: "peace-4",
    src: "/PROTECT%20YOUR%20PEACE/chrome_kRyyPxpTL3.png",
    alt: "Protect Your Peace - True love comes from within.",
    title: "True love comes from within.",
  },
  {
    id: "peace-5",
    src: "/PROTECT%20YOUR%20PEACE/chrome_I2GMVS2AQu.png",
    alt: "Protect Your Peace - Storms aren't forever.",
    title: "Storms aren't forever.",
  },
  {
    id: "peace-6",
    src: "/PROTECT%20YOUR%20PEACE/chrome_LOxtmQW4g7.png",
    alt: "Protect Your Peace - You are needed.",
    title: "You are needed.",
  },
  {
    id: "peace-7",
    src: "/PROTECT%20YOUR%20PEACE/chrome_WJDa8tBw5u.png",
    alt: "Protect Your Peace - Your story isn't over.",
    title: "Your story isn't over.",
  },
  {
    id: "peace-8",
    src: "/PROTECT%20YOUR%20PEACE/chrome_n1uqMmbCBs.png",
    alt: "Protect Your Peace - Your dreams matter.",
    title: "Your dreams matter.",
  },
];

export function PlaceOfPeaceGallery() {
  const [selectedCardIndex, setSelectedCardIndex] = useState<number | null>(null);
  const [isPaused, setIsPaused] = useState(false);
  const scrollContainerRef = useRef<HTMLDivElement>(null);

  const handleScroll = (direction: "left" | "right") => {
    if (scrollContainerRef.current) {
      const scrollAmount = direction === "left" ? -340 : 340;
      scrollContainerRef.current.scrollBy({
        left: scrollAmount,
        behavior: "smooth",
      });
    }
  };

  const handleKeyDown = useCallback(
    (e: KeyboardEvent) => {
      if (selectedCardIndex === null) return;
      if (e.key === "Escape") setSelectedCardIndex(null);
      if (e.key === "ArrowRight") {
        setSelectedCardIndex((prev) =>
          prev !== null ? (prev + 1) % peaceCards.length : 0
        );
      }
      if (e.key === "ArrowLeft") {
        setSelectedCardIndex((prev) =>
          prev !== null
            ? (prev - 1 + peaceCards.length) % peaceCards.length
            : peaceCards.length - 1
        );
      }
    },
    [selectedCardIndex]
  );

  useEffect(() => {
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [handleKeyDown]);

  // Lock body scroll when modal is open
  useEffect(() => {
    if (selectedCardIndex !== null) {
      document.body.style.overflow = "hidden";
    } else {
      document.body.style.overflow = "unset";
    }
    return () => {
      document.body.style.overflow = "unset";
    };
  }, [selectedCardIndex]);

  // Tripled list for infinite seamless marquee
  const marqueeCards = [...peaceCards, ...peaceCards, ...peaceCards];

  return (
    <section
      className="relative overflow-hidden bg-[var(--sand)]/40 px-4 py-20 sm:px-6 lg:px-8"
      aria-label="A Place of Peace Gallery"
    >
      {/* Background ambient accents */}
      <div
        className="pointer-events-none absolute -top-24 left-1/2 -z-10 h-96 w-[800px] -translate-x-1/2 rounded-full bg-[radial-gradient(ellipse_at_center,rgba(198,165,92,0.18)_0%,rgba(247,243,235,0)_70%)] blur-3xl"
        aria-hidden="true"
      />

      <div className="mx-auto max-w-7xl text-center">
        <p className="text-xs font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)]">
          Protect Your Peace
        </p>
        <h2 className="mt-3 font-serif text-4xl text-[var(--ink)] sm:text-5xl lg:text-6xl">
          A Place of Peace
        </h2>
        <p className="mx-auto mt-4 max-w-2xl text-base leading-relaxed text-[#675d50] sm:text-lg">
          A message wall to ground you in truth, reminding you that you are valued, seen, and never forgotten; that your life matters.
        </p>
      </div>

      {/* Marquee Gallery Container */}
      <div className="relative mt-12 w-full">
        {/* Navigation arrows */}
        <div className="mx-auto mb-4 flex max-w-7xl items-center justify-end gap-2 px-4 sm:px-0">
          <button
            type="button"
            onClick={() => handleScroll("left")}
            aria-label="Previous cards"
            className="flex h-10 w-10 items-center justify-center rounded-full border border-[var(--line)] bg-white/90 text-[var(--ink)] shadow-sm backdrop-blur-sm transition-all hover:bg-[var(--gold)] hover:text-white focus:outline-none focus:ring-2 focus:ring-[var(--gold)] active:scale-95 cursor-pointer"
          >
            <ChevronLeft className="h-5 w-5" />
          </button>
          <button
            type="button"
            onClick={() => handleScroll("right")}
            aria-label="Next cards"
            className="flex h-10 w-10 items-center justify-center rounded-full border border-[var(--line)] bg-white/90 text-[var(--ink)] shadow-sm backdrop-blur-sm transition-all hover:bg-[var(--gold)] hover:text-white focus:outline-none focus:ring-2 focus:ring-[var(--gold)] active:scale-95 cursor-pointer"
          >
            <ChevronRight className="h-5 w-5" />
          </button>
        </div>

        {/* Outer scroll track with edge gradients */}
        <div
          className="relative w-full overflow-hidden"
          onMouseEnter={() => setIsPaused(true)}
          onMouseLeave={() => setIsPaused(false)}
          onTouchStart={() => setIsPaused(true)}
          onTouchEnd={() => setIsPaused(false)}
        >
          {/* Subtle fade edges for smooth entry/exit */}
          <div className="pointer-events-none absolute left-0 top-0 z-10 h-full w-12 bg-gradient-to-r from-[var(--sand)]/80 to-transparent sm:w-24" />
          <div className="pointer-events-none absolute right-0 top-0 z-10 h-full w-12 bg-gradient-to-l from-[var(--sand)]/80 to-transparent sm:w-24" />

          {/* Scrollable Container with Continuous Animation */}
          <div
            ref={scrollContainerRef}
            className="flex w-full overflow-x-auto no-scrollbar py-4 scroll-smooth"
            style={{
              scrollbarWidth: "none",
              msOverflowStyle: "none",
            }}
          >
            <motion.div
              className="flex flex-nowrap gap-5 pr-5"
              animate={{
                x: isPaused ? undefined : ["0%", "-33.333333%"],
              }}
              transition={{
                x: {
                  repeat: Infinity,
                  repeatType: "loop",
                  duration: 35,
                  ease: "linear",
                },
              }}
            >
              {marqueeCards.map((card, idx) => {
                const originalIndex = idx % peaceCards.length;
                return (
                  <motion.div
                    key={`${card.id}-${idx}`}
                    whileHover={{
                      y: -6,
                      scale: 1.02,
                      transition: { duration: 0.25, ease: "easeOut" },
                    }}
                    onClick={() => setSelectedCardIndex(originalIndex)}
                    className="group relative flex-shrink-0 cursor-pointer overflow-hidden rounded-xl border border-[rgba(198,165,92,0.3)] bg-white shadow-md transition-shadow hover:border-[var(--gold)] hover:shadow-xl w-[260px] sm:w-[290px] md:w-[320px] aspect-square"
                  >
                    <Image
                      src={card.src}
                      alt={card.alt}
                      fill
                      unoptimized
                      sizes="(max-width: 640px) 260px, (max-width: 768px) 290px, 320px"
                      className="object-cover transition-transform duration-500 group-hover:scale-105"
                      loading="lazy"
                    />
                    {/* Hover Overlay with expand icon */}
                    <div className="absolute inset-0 flex items-center justify-center bg-black/30 opacity-0 backdrop-blur-[2px] transition-opacity duration-300 group-hover:opacity-100">
                      <span className="flex items-center gap-1.5 rounded-full bg-white/90 px-3.5 py-1.5 text-xs font-semibold text-[var(--ink)] shadow-md">
                        <Maximize2 className="h-3.5 w-3.5" />
                        View
                      </span>
                    </div>
                  </motion.div>
                );
              })}
            </motion.div>
          </div>
        </div>
      </div>

      {/* Interactive Lightbox Modal */}
      <AnimatePresence>
        {selectedCardIndex !== null && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.25 }}
            className="fixed inset-0 z-50 flex items-center justify-center bg-black/85 p-4 backdrop-blur-md sm:p-6 md:p-10"
            onClick={() => setSelectedCardIndex(null)}
          >
            {/* Modal Content Wrapper */}
            <div
              className="relative flex w-full max-w-[780px] flex-col items-center"
              onClick={(e) => e.stopPropagation()}
            >
              {/* Floating Close Button */}
              <button
                type="button"
                onClick={() => setSelectedCardIndex(null)}
                className="absolute -top-12 right-0 z-30 flex h-10 w-10 items-center justify-center rounded-full bg-white/20 text-white backdrop-blur-md transition-all hover:scale-110 hover:bg-white hover:text-[var(--ink)] focus:outline-none cursor-pointer"
                aria-label="Close image preview"
              >
                <X className="h-5 w-5" />
              </button>

              {/* Prev Button (Floating beside on desktop, overlay on mobile) */}
              <button
                type="button"
                onClick={() =>
                  setSelectedCardIndex((prev) =>
                    prev !== null
                      ? (prev - 1 + peaceCards.length) % peaceCards.length
                      : 0
                  )
                }
                className="absolute left-3 top-1/2 z-30 flex h-12 w-12 -translate-y-1/2 items-center justify-center rounded-full border border-white/20 bg-black/60 text-white shadow-xl backdrop-blur-md transition-all hover:scale-110 hover:bg-white hover:text-[var(--ink)] focus:outline-none md:-left-16 md:bg-white/20 md:hover:bg-white cursor-pointer"
                aria-label="Previous card"
              >
                <ChevronLeft className="h-6 w-6" />
              </button>

              {/* Next Button (Floating beside on desktop, overlay on mobile) */}
              <button
                type="button"
                onClick={() =>
                  setSelectedCardIndex((prev) =>
                    prev !== null ? (prev + 1) % peaceCards.length : 0
                  )
                }
                className="absolute right-3 top-1/2 z-30 flex h-12 w-12 -translate-y-1/2 items-center justify-center rounded-full border border-white/20 bg-black/60 text-white shadow-xl backdrop-blur-md transition-all hover:scale-110 hover:bg-white hover:text-[var(--ink)] focus:outline-none md:-right-16 md:bg-white/20 md:hover:bg-white cursor-pointer"
                aria-label="Next card"
              >
                <ChevronRight className="h-6 w-6" />
              </button>

              {/* Main Card */}
              <motion.div
                key={selectedCardIndex}
                initial={{ scale: 0.92, opacity: 0, y: 15 }}
                animate={{ scale: 1, opacity: 1, y: 0 }}
                exit={{ scale: 0.92, opacity: 0, y: 15 }}
                transition={{ type: "spring", stiffness: 320, damping: 28 }}
                className="relative aspect-square w-full overflow-hidden rounded-2xl border border-[rgba(198,165,92,0.45)] bg-white shadow-2xl"
              >
                <Image
                  src={peaceCards[selectedCardIndex].src}
                  alt={peaceCards[selectedCardIndex].alt}
                  fill
                  priority
                  unoptimized
                  className="object-contain"
                  sizes="(max-width: 768px) 92vw, 780px"
                />
              </motion.div>

              {/* Caption & Counter */}
              <div className="mt-4 flex w-full items-center justify-between px-2 text-sm text-neutral-300">
                <span className="font-serif tracking-wide text-white/90">
                  {peaceCards[selectedCardIndex].title}
                </span>
                <div className="flex items-center gap-3">
                  <span className="font-mono text-xs text-[var(--sand)]">
                    {selectedCardIndex + 1} / {peaceCards.length}
                  </span>
                  <span className="hidden text-xs text-neutral-400 sm:inline">
                    (Use ← → keys or ESC to close)
                  </span>
                </div>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </section>
  );
}
