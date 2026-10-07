"use client";

import { useState, useEffect, useCallback } from "react";
import Link from "next/link";
import { motion, AnimatePresence } from "framer-motion";
import { ChevronLeft, ChevronRight, Pause, Play } from "lucide-react";
import { RobustImage } from "@/components/ui/RobustImage";

interface RegionalSlide {
  id: string;
  regionCode: string;
  regionShort: string;
  regionTitle: string;
  sublabel: string;
  tag: string;
  image: string;
  alt: string;
}

const REGIONAL_SLIDES: RegionalSlide[] = [
  {
    id: "mediterranean-basin",
    regionCode: "REGION 01",
    regionShort: "Mediterranean",
    regionTitle: "Mediterranean & Southern Maritime Hubs",
    sublabel: "Historic Coastal Academies | High-Performance Poise",
    tag: "SOUTHERN EUROPEAN & MARITIME HUBS",
    image: "/foundations/europe/banners/stock-mediterranean-basin.jpg",
    alt: "Historic Mediterranean coastal athletic training academy with running track overlooking the azure sea at golden hour",
  },
  {
    id: "nordic-baltic",
    regionCode: "REGION 02",
    regionShort: "Nordic & Baltic",
    regionTitle: "Nordic & Baltic Applied Science Centers",
    sublabel: "Waterfront Biomechanics Telemetry | Endurance Innovation",
    tag: "NORTHERN & BALTIC HIGH-PERFORMANCE HUBS",
    image: "/foundations/europe/banners/stock-nordic-baltic.jpg",
    alt: "Modern Scandinavian waterfront sports science pavilion with illuminated training track on the archipelago",
  },
  {
    id: "central-western",
    regionCode: "REGION 03",
    regionShort: "Central & Alpine",
    regionTitle: "Central & Western European Corridor",
    sublabel: "Alpine High-Performance Institutes | Multi-Club Networks",
    tag: "ALPINE & CONTINENTAL ATHLETIC CAMPUSES",
    image: "/foundations/europe/banners/stock-central-western.jpg",
    alt: "State-of-the-art Alpine high-performance sports training institute with blue running track in mountain foothills",
  },
  {
    id: "pan-european-alliances",
    regionCode: "REGION 04",
    regionShort: "Transatlantic",
    regionTitle: "Transatlantic Summit & Governance Hubs",
    sublabel: "Continental Coordination | Multi-Nation Athletic Standards",
    tag: "PAN-EUROPEAN ATHLETIC ALLIANCES",
    image: "/foundations/europe/banners/stock-continental-summit.jpg",
    alt: "Modern European athletic governance summit pavilion terrace with continental flags overlooking European capital city",
  },
];

const AUTOPLAY_INTERVAL_MS = 6500;

export function EuropeanBannerSlideshow() {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isPaused, setIsPaused] = useState(false);

  const nextSlide = useCallback(() => {
    setCurrentIndex((prev) => (prev + 1) % REGIONAL_SLIDES.length);
  }, []);

  const prevSlide = useCallback(() => {
    setCurrentIndex((prev) => (prev - 1 + REGIONAL_SLIDES.length) % REGIONAL_SLIDES.length);
  }, []);

  const goToSlide = (idx: number) => {
    setCurrentIndex(idx);
  };

  // Reset timer on slide change or pause toggle to eliminate double-jumps
  useEffect(() => {
    if (isPaused) return;
    const timer = setInterval(() => {
      setCurrentIndex((prev) => (prev + 1) % REGIONAL_SLIDES.length);
    }, AUTOPLAY_INTERVAL_MS);
    return () => clearInterval(timer);
  }, [isPaused, currentIndex]);

  const activeSlide = REGIONAL_SLIDES[currentIndex];

  return (
    <section
      aria-label="European regional sport ecosystems slideshow"
      className="relative overflow-hidden min-h-[520px] sm:min-h-[580px] lg:min-h-[620px] border-t border-[rgba(198,165,92,0.4)] flex flex-col justify-between"
      onMouseEnter={() => setIsPaused(true)}
      onMouseLeave={() => setIsPaused(false)}
    >
      {/* Background Regional Stock Venue Slides with Cross-Fade */}
      <div className="absolute inset-0 pointer-events-none overflow-hidden">
        {REGIONAL_SLIDES.map((slide, idx) => {
          const isActive = idx === currentIndex;
          return (
            <div
              key={slide.id}
              id={`regional-slide-panel-${slide.id}`}
              role="tabpanel"
              aria-hidden={!isActive}
              className={`absolute inset-0 transition-opacity duration-1000 ease-in-out ${
                isActive ? "opacity-100 z-10" : "opacity-0 z-0"
              }`}
            >
              <RobustImage
                src={slide.image}
                fallbackSrcs={[
                  "/foundations/banners/european-pathway-banner.jpg",
                  "/foundations/banners/scenic-alpine-training.jpg",
                  "/foundations/select-stock/europe.jpg",
                ]}
                alt={slide.alt}
                fill
                priority={idx === 0}
                sizes="100vw"
                quality={95}
                className="object-cover object-center"
              />
            </div>
          );
        })}

        {/* High-Contrast Balanced Gradient Overlays (Zero murky wash, rich photographic framing) */}
        <div className="absolute inset-0 z-20 bg-gradient-to-t from-[#0e0c0b]/95 via-[#0e0c0b]/55 to-[#0e0c0b]/75" />
        <div className="absolute inset-0 z-20 bg-[radial-gradient(ellipse_at_center,rgba(14,12,11,0.2)_0%,rgba(14,12,11,0.85)_100%)]" />
      </div>

      {/* Top Floating Active Region Badge & Touch-Accessible Controls */}
      <div className="relative z-30 pt-6 px-4 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl flex flex-wrap items-center justify-between gap-3">
          <AnimatePresence mode="wait">
            <motion.div
              key={activeSlide.id}
              initial={{ opacity: 0, x: -10 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: 10 }}
              transition={{ duration: 0.35 }}
              className="inline-flex items-center gap-2 rounded-full border border-[rgba(226,201,146,0.6)] bg-[rgba(24,20,17,0.92)] px-4 py-1.5 backdrop-blur-md shadow-xl"
            >
              <span className="relative flex h-2 w-2">
                <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-[#e2c992] opacity-80" />
                <span className="relative inline-flex rounded-full h-2 w-2 bg-[#dfc385]" />
              </span>
              <span className="text-[11px] font-bold uppercase tracking-[0.22em] text-[#f3dfb2]">
                {activeSlide.tag}
              </span>
              <span className="hidden sm:inline text-white/40">|</span>
              <span className="hidden sm:inline text-xs font-serif text-white">
                {activeSlide.regionTitle}
              </span>
            </motion.div>
          </AnimatePresence>

          {/* Universal Controls: Mobile Touch & Desktop Accessible */}
          <div className="flex items-center gap-1.5 sm:gap-2">
            <button
              type="button"
              onClick={() => setIsPaused((prev) => !prev)}
              aria-label={isPaused ? "Play slideshow autoplay" : "Pause slideshow autoplay"}
              className="flex h-8 w-8 items-center justify-center rounded-full border border-[rgba(226,201,146,0.5)] bg-[rgba(24,20,17,0.85)] text-[#f3dfb2] transition-colors hover:border-[#dfc385] hover:text-white backdrop-blur-md shadow-lg cursor-pointer"
            >
              {isPaused ? <Play size={13} /> : <Pause size={13} />}
            </button>
            <button
              type="button"
              onClick={prevSlide}
              aria-label="Previous European region"
              className="flex h-8 w-8 items-center justify-center rounded-full border border-[rgba(226,201,146,0.5)] bg-[rgba(24,20,17,0.85)] text-[#f3dfb2] transition-colors hover:border-[#dfc385] hover:text-white backdrop-blur-md shadow-lg cursor-pointer"
            >
              <ChevronLeft size={16} />
            </button>
            <button
              type="button"
              onClick={nextSlide}
              aria-label="Next European region"
              className="flex h-8 w-8 items-center justify-center rounded-full border border-[rgba(226,201,146,0.5)] bg-[rgba(24,20,17,0.85)] text-[#f3dfb2] transition-colors hover:border-[#dfc385] hover:text-white backdrop-blur-md shadow-lg cursor-pointer"
            >
              <ChevronRight size={16} />
            </button>
          </div>
        </div>
      </div>

      {/* Center Hero CTA Copy (Zero Black-on-Black: High-Visibility Gold & Crisp Ivory) */}
      <div className="relative z-30 my-auto px-4 py-10 text-center sm:px-6 lg:px-8">
        <div className="max-w-3xl mx-auto text-white">
          <p className="text-xs font-bold uppercase tracking-[0.28em] text-[#dfc385] drop-shadow-sm">
            EUROPEAN PARTNERSHIPS
          </p>
          <h2 className="mt-3 font-serif text-3xl sm:text-5xl lg:text-6xl text-white tracking-tight leading-[1.08] drop-shadow-lg">
            Let&apos;s Explore Partnership Opportunities.
          </h2>
          <p className="mt-4 text-base sm:text-lg text-[#f4efe6] leading-relaxed max-w-2xl mx-auto drop-shadow-sm">
            Connect to discuss how we can work together to support stronger athletes, coaches, and sport ecosystems across Europe.
          </p>

          <div className="mt-8 flex flex-wrap justify-center items-center gap-4">
            {/* Primary High-Contrast Gold Button */}
            <Link
              href="/book"
              className="inline-flex items-center justify-center border border-[#e2c992] bg-[linear-gradient(180deg,#dfc385_0%,#b8934d_100%)] px-7 py-3.5 text-xs font-extrabold uppercase tracking-[0.22em] text-[#171412] shadow-[0_12px_36px_rgba(0,0,0,0.45)] transition-all hover:brightness-110 hover:shadow-[0_16px_44px_rgba(223,195,133,0.35)] active:translate-y-px"
            >
              START A PARTNERSHIP CONVERSATION
            </Link>

            {/* Secondary High-Contrast Translucent-White/Gold Button (Zero Black-on-Black) */}
            <Link
              href="/foundations"
              className="inline-flex items-center justify-center border-2 border-[#dfc385] bg-white/10 hover:bg-white/20 px-7 py-3.5 text-xs font-extrabold uppercase tracking-[0.22em] text-white shadow-[0_8px_24px_rgba(0,0,0,0.3)] transition-all backdrop-blur-md hover:border-[#f3dfb2]"
            >
              VIEW FOUNDATIONS FRAMEWORK
            </Link>
          </div>
        </div>
      </div>


      {/* Docked Luxury Glass Regional Selector Bar */}
      <div className="relative z-30 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(20,16,14,0.92)] backdrop-blur-md">
        <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
          <div
            role="tablist"
            aria-label="European regions"
            className="grid grid-cols-2 lg:grid-cols-4 divide-y sm:divide-y-0 sm:divide-x divide-[rgba(198,165,92,0.24)]"
          >
            {REGIONAL_SLIDES.map((slide, idx) => {
              const isSelected = idx === currentIndex;
              return (
                <button
                  key={slide.id}
                  id={`regional-tab-${slide.id}`}
                  role="tab"
                  aria-selected={isSelected}
                  aria-controls={`regional-slide-panel-${slide.id}`}
                  aria-label={`${slide.regionCode}: ${slide.regionTitle}`}
                  type="button"
                  onClick={() => goToSlide(idx)}
                  className={`text-left p-3.5 sm:p-4 transition-all duration-300 relative group ${
                    isSelected
                      ? "bg-[rgba(198,165,92,0.16)]"
                      : "hover:bg-white/5"
                  }`}
                >
                  {/* Active Top Gold Line */}
                  {isSelected && (
                    <span className="absolute top-0 inset-x-0 h-0.5 bg-[#dfc385] shadow-[0_0_10px_#dfc385]" />
                  )}

                  <div className="flex items-center justify-between">
                    <span
                      className={`text-[10px] font-bold tracking-[0.2em] uppercase ${
                        isSelected
                          ? "text-[#dfc385]"
                          : "text-[#d8cbba] group-hover:text-white"
                      }`}
                    >
                      {slide.regionCode}
                    </span>
                    <span
                      className={`text-[9px] font-semibold tracking-wider uppercase px-2 py-0.5 rounded border ${
                        isSelected
                          ? "bg-[#dfc385]/20 text-[#f3dfb2] border-[#dfc385]/50"
                          : "bg-white/5 text-[#d8cbba] border-white/10"
                      }`}
                    >
                      {slide.regionShort}
                    </span>
                  </div>

                  <p
                    className={`mt-1.5 font-serif text-xs sm:text-sm truncate ${
                      isSelected
                        ? "text-white font-semibold"
                        : "text-[#eee6da] group-hover:text-white"
                    }`}
                  >
                    {slide.regionTitle}
                  </p>

                  <p className="mt-0.5 text-[10px] text-[#c7b9a5] truncate hidden sm:block">
                    {slide.sublabel}
                  </p>
                </button>
              );
            })}
          </div>
        </div>
      </div>
    </section>
  );
}
