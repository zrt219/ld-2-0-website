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

interface SanctuarySlide {
  id: string;
  src: string;
  alt: string;
  title: string;
  caption: string;
  tag: string;
}

const sanctuarySlides: SanctuarySlide[] = [
  {
    id: "sanctuary-1",
    src: "/images/place-of-peace-sanctuary.jpg",
    alt: "A Place of Peace - Travertine architectural alcove with delicate botanical vase and sculptural form",
    title: "Sanctuary & Stillness",
    caption: "Finding calm in the quiet, intentional spaces of life.",
    tag: "Architectural Peace",
  },
  {
    id: "sanctuary-2",
    src: "/images/place-of-peace-coastal-terrace.jpg",
    alt: "A Place of Peace - Mediterranean travertine loggia terrace overlooking calm azure ocean",
    title: "Tides of Peace",
    caption: "Allowing your mind to rest and reset like calm waters.",
    tag: "Coastal Sanctuary",
  },
  {
    id: "sanctuary-3",
    src: "/images/place-of-peace-water-closeup.jpg",
    alt: "A Place of Peace - Cinematic close-up of tranquil water ripples with gentle sunset reflections",
    title: "Still Waters",
    caption: "Peace that runs deep, quiet as still waters at eventide.",
    tag: "Water & Serenity",
  },
  {
    id: "sanctuary-4",
    src: "/images/place-of-peace-coastal-dunes.jpg",
    alt: "A Place of Peace - Golden sunrise over peaceful ocean shores",
    title: "Morning Horizon",
    caption: "Letting hope rise with the morning light and gentle tides.",
    tag: "Seaside Horizon",
  },
  {
    id: "sanctuary-5",
    src: "/images/place-of-peace-mountain-loggia.jpg",
    alt: "A Place of Peace - Majestic alpine mountain peaks at sunset above a sea of clouds",
    title: "Mountain Strength",
    caption: "Rooted above the clouds in quiet endurance and perspective.",
    tag: "Alpine Solitude",
  },
  {
    id: "sanctuary-6",
    src: "/images/place-of-peace-mountain-valley.jpg",
    alt: "A Place of Peace - Sunlit expansive mountain valley with pine ridges and snow-capped peaks",
    title: "Open Horizons",
    caption: "Space to breathe, reflect, and renew your spirit in wide vistas.",
    tag: "Mountain Sanctuary",
  },
];

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
  const [activeSanctuaryIndex, setActiveSanctuaryIndex] = useState(0);
  const [isSanctuaryModalOpen, setIsSanctuaryModalOpen] = useState(false);
  const [isPaused, setIsPaused] = useState(false);
  const [isCardHovered, setIsCardHovered] = useState(false);
  const scrollContainerRef = useRef<HTMLDivElement>(null);

  // Auto-advance sanctuary card on homepage when not hovered or open
  useEffect(() => {
    if (isCardHovered || isSanctuaryModalOpen) return;
    const interval = setInterval(() => {
      setActiveSanctuaryIndex((prev) => (prev + 1) % sanctuarySlides.length);
    }, 6500);
    return () => clearInterval(interval);
  }, [isCardHovered, isSanctuaryModalOpen]);

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
      if (e.key === "Escape") {
        setSelectedCardIndex(null);
        setIsSanctuaryModalOpen(false);
        return;
      }

      if (isSanctuaryModalOpen) {
        if (e.key === "ArrowRight") {
          setActiveSanctuaryIndex((prev) => (prev + 1) % sanctuarySlides.length);
        }
        if (e.key === "ArrowLeft") {
          setActiveSanctuaryIndex((prev) =>
            (prev - 1 + sanctuarySlides.length) % sanctuarySlides.length
          );
        }
        return;
      }

      if (selectedCardIndex !== null) {
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
      }
    },
    [selectedCardIndex, isSanctuaryModalOpen]
  );

  useEffect(() => {
    window.addEventListener("keydown", handleKeyDown);
    return () => window.removeEventListener("keydown", handleKeyDown);
  }, [handleKeyDown]);

  // Lock body scroll when any modal is open without causing layout shift
  useEffect(() => {
    const isModalOpen = selectedCardIndex !== null || isSanctuaryModalOpen;
    if (isModalOpen) {
      const scrollbarWidth = window.innerWidth - document.documentElement.clientWidth;
      const previousOverflow = document.body.style.overflow;
      const previousPaddingRight = document.body.style.paddingRight;
      document.body.style.overflow = "hidden";
      if (scrollbarWidth > 0) {
        document.body.style.paddingRight = `${scrollbarWidth}px`;
      }
      return () => {
        document.body.style.overflow = previousOverflow;
        document.body.style.paddingRight = previousPaddingRight;
      };
    }
  }, [selectedCardIndex, isSanctuaryModalOpen]);

  // Tripled list for infinite seamless marquee
  const marqueeCards = [...peaceCards, ...peaceCards, ...peaceCards];

  const currentSanctuary = sanctuarySlides[activeSanctuaryIndex];

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

      {/* Split Editorial Header */}
      <div className="mx-auto max-w-7xl">
        <div className="grid items-center gap-10 lg:grid-cols-12 lg:gap-12">
          {/* Left Column: Typography and Intention */}
          <div className="lg:col-span-6 xl:col-span-7">
            <div className="inline-flex items-center gap-2 rounded-full border border-[rgba(198,165,92,0.35)] bg-white/70 px-3.5 py-1 text-xs font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)] backdrop-blur-sm">
              <span className="h-1.5 w-1.5 rounded-full bg-[var(--gold)]" />
              Protect Your Peace
            </div>

            <h2 className="mt-4 font-serif text-4xl leading-[1.15] text-[var(--ink)] sm:text-5xl lg:text-6xl">
              A Place of Peace
            </h2>

            <p className="mt-5 text-lg leading-relaxed text-[#675d50] sm:text-xl">
              A quiet sanctuary to ground you in truth, quiet the noise, and remind you that you are valued, seen, and never forgotten; that your life matters.
            </p>

            <div className="mt-6 border-l-2 border-[var(--gold)] bg-white/40 p-3.5 pl-4 rounded-r-lg italic text-[#7a6f60]">
              &ldquo;Rest is not a detour from your purpose—it is the foundation that sustains it.&rdquo;
            </div>

            <p className="mt-5 text-xs font-bold uppercase tracking-[0.16em] text-[var(--gold-dark)]">
              Explore the curated reflections below or click to immerse in full screen
            </p>
          </div>

          {/* Right Column: Multi-Slide Sanctuary Showcase with Carousel & Lightbox */}
          <div className="lg:col-span-6 xl:col-span-5">
            <motion.div
              onMouseEnter={() => setIsCardHovered(true)}
              onMouseLeave={() => setIsCardHovered(false)}
              whileHover={{ scale: 1.015, y: -2 }}
              whileTap={{ scale: 0.98 }}
              onClick={() => setIsSanctuaryModalOpen(true)}
              className="group relative aspect-[16/10] sm:aspect-[4/3] w-full cursor-pointer overflow-hidden rounded-2xl border border-[rgba(198,165,92,0.4)] bg-white shadow-[0_20px_50px_rgba(23,20,18,0.09)] transition-all duration-300 hover:border-[var(--gold)] hover:shadow-[0_24px_60px_rgba(198,165,92,0.22)]"
            >
              <AnimatePresence mode="wait">
                <motion.div
                  key={currentSanctuary.id}
                  initial={{ opacity: 0, scale: 1.04 }}
                  animate={{ opacity: 1, scale: 1 }}
                  exit={{ opacity: 0, scale: 0.98 }}
                  transition={{ duration: 0.7, ease: "easeInOut" }}
                  className="absolute inset-0"
                >
                  <Image
                    src={currentSanctuary.src}
                    alt={currentSanctuary.alt}
                    fill
                    priority
                    unoptimized
                    sizes="(max-width: 768px) 100vw, 600px"
                    className="object-cover"
                  />
                </motion.div>
              </AnimatePresence>

              {/* Subtle Warm Inset Vignette */}
              <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-black/60 via-black/10 to-transparent opacity-70 transition-opacity duration-300 group-hover:opacity-50" />

              {/* Top Navigation Dots */}
              <div
                className="absolute top-4 left-4 right-4 z-20 flex items-center justify-between"
                onClick={(e) => e.stopPropagation()}
              >
                <span className="rounded-full border border-white/20 bg-black/40 px-3 py-1 text-[11px] font-semibold uppercase tracking-wider text-white backdrop-blur-md">
                  {currentSanctuary.tag}
                </span>

                {/* Mini Indicator Dots */}
                <div className="flex items-center gap-1.5 rounded-full bg-black/40 px-2.5 py-1.5 backdrop-blur-md">
                  {sanctuarySlides.map((slide, idx) => (
                    <button
                      key={slide.id}
                      type="button"
                      onClick={() => setActiveSanctuaryIndex(idx)}
                      aria-label={`Go to sanctuary view ${idx + 1}: ${slide.title}`}
                      className={`h-1.5 rounded-full transition-all duration-300 cursor-pointer ${
                        idx === activeSanctuaryIndex
                          ? "w-5 bg-[var(--gold)]"
                          : "w-1.5 bg-white/50 hover:bg-white"
                      }`}
                    />
                  ))}
                </div>
              </div>

              {/* Bottom Floating Pill & Title */}
              <div className="absolute bottom-4 left-4 right-4 z-20 flex items-end justify-between">
                <div>
                  <p className="font-serif text-base font-semibold text-white drop-shadow-md sm:text-lg">
                    {currentSanctuary.title}
                  </p>
                  <p className="line-clamp-1 text-xs text-white/80 drop-shadow-sm">
                    {currentSanctuary.caption}
                  </p>
                </div>

                <span className="flex items-center gap-1.5 rounded-full bg-white/95 px-3 py-1.5 text-xs font-semibold text-[var(--ink)] shadow-md transition-transform duration-200 group-hover:scale-105">
                  <Maximize2 className="h-3.5 w-3.5 text-[var(--gold-dark)]" />
                  View Sanctuary
                </span>
              </div>
            </motion.div>
          </div>
        </div>
      </div>

      {/* Marquee Gallery Container */}
      <div className="relative mt-14 w-full">
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
                    whileTap={{ scale: 0.96 }}
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

      {/* Multi-Slide Sanctuary Fullscreen Lightbox Modal */}
      <AnimatePresence>
        {isSanctuaryModalOpen && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.25 }}
            className="fixed inset-0 z-50 flex items-center justify-center bg-black/90 p-4 backdrop-blur-md sm:p-6 md:p-10"
            onClick={() => setIsSanctuaryModalOpen(false)}
          >
            <div
              className="relative flex w-full max-w-[980px] flex-col items-center"
              onClick={(e) => e.stopPropagation()}
            >
              {/* Floating Close Button */}
              <button
                type="button"
                onClick={() => setIsSanctuaryModalOpen(false)}
                className="absolute -top-12 right-0 z-30 flex h-10 w-10 items-center justify-center rounded-full bg-white/20 text-white backdrop-blur-md transition-all hover:scale-110 hover:bg-white hover:text-[var(--ink)] focus:outline-none cursor-pointer"
                aria-label="Close sanctuary preview"
              >
                <X className="h-5 w-5" />
              </button>

              {/* Prev Button */}
              <button
                type="button"
                onClick={() =>
                  setActiveSanctuaryIndex(
                    (prev) =>
                      (prev - 1 + sanctuarySlides.length) % sanctuarySlides.length
                  )
                }
                className="absolute left-3 top-1/2 z-30 flex h-12 w-12 -translate-y-1/2 items-center justify-center rounded-full border border-white/20 bg-black/60 text-white shadow-xl backdrop-blur-md transition-all hover:scale-110 hover:bg-white hover:text-[var(--ink)] focus:outline-none md:-left-16 md:bg-white/20 md:hover:bg-white cursor-pointer"
                aria-label="Previous sanctuary view"
              >
                <ChevronLeft className="h-6 w-6" />
              </button>

              {/* Next Button */}
              <button
                type="button"
                onClick={() =>
                  setActiveSanctuaryIndex(
                    (prev) => (prev + 1) % sanctuarySlides.length
                  )
                }
                className="absolute right-3 top-1/2 z-30 flex h-12 w-12 -translate-y-1/2 items-center justify-center rounded-full border border-white/20 bg-black/60 text-white shadow-xl backdrop-blur-md transition-all hover:scale-110 hover:bg-white hover:text-[var(--ink)] focus:outline-none md:-right-16 md:bg-white/20 md:hover:bg-white cursor-pointer"
                aria-label="Next sanctuary view"
              >
                <ChevronRight className="h-6 w-6" />
              </button>

              {/* Main Sanctuary Card with Slide Transition */}
              <div className="relative aspect-[16/10] sm:aspect-[16/9] w-full overflow-hidden rounded-2xl border border-[rgba(198,165,92,0.45)] bg-[var(--ink)] shadow-2xl">
                <AnimatePresence mode="wait">
                  <motion.div
                    key={currentSanctuary.id}
                    initial={{ opacity: 0, scale: 0.96 }}
                    animate={{ opacity: 1, scale: 1 }}
                    exit={{ opacity: 0, scale: 1.02 }}
                    transition={{ duration: 0.35, ease: "easeInOut" }}
                    className="absolute inset-0"
                  >
                    <Image
                      src={currentSanctuary.src}
                      alt={currentSanctuary.alt}
                      fill
                      priority
                      unoptimized
                      className="object-cover"
                      sizes="(max-width: 768px) 94vw, 980px"
                    />
                  </motion.div>
                </AnimatePresence>
              </div>

              {/* Caption & Navigation Controls */}
              <div className="mt-4 flex w-full flex-col gap-2 px-2 sm:flex-row sm:items-center sm:justify-between text-neutral-300">
                <div>
                  <p className="font-serif text-lg font-semibold tracking-wide text-white">
                    {currentSanctuary.title}
                  </p>
                  <p className="text-sm text-neutral-300">
                    {currentSanctuary.caption}
                  </p>
                </div>

                <div className="flex items-center gap-3 self-end sm:self-center">
                  {/* Indicator Dots */}
                  <div className="flex items-center gap-1.5">
                    {sanctuarySlides.map((slide, idx) => (
                      <button
                        key={slide.id}
                        type="button"
                        onClick={() => setActiveSanctuaryIndex(idx)}
                        aria-label={`Go to slide ${idx + 1}`}
                        className={`h-2 rounded-full transition-all duration-300 cursor-pointer ${
                          idx === activeSanctuaryIndex
                            ? "w-6 bg-[var(--gold)]"
                            : "w-2 bg-white/40 hover:bg-white"
                        }`}
                      />
                    ))}
                  </div>

                  <span className="font-mono text-xs font-medium text-[var(--sand)]">
                    {activeSanctuaryIndex + 1} / {sanctuarySlides.length}
                  </span>
                  <span className="hidden text-xs text-neutral-400 md:inline">
                    (Use ← → keys)
                  </span>
                </div>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      {/* Message Cards Lightbox Modal */}
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

              {/* Prev Button */}
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

              {/* Next Button */}
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
