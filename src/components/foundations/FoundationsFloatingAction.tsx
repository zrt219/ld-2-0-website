"use client";

import Link from "next/link";
import { ArrowUpRight } from "lucide-react";
import { motion, AnimatePresence, useReducedMotion } from "framer-motion";
import { useState, useEffect } from "react";

export type FoundationsTrackKey =
  | "foundations"
  | "golf"
  | "hockey"
  | "corporate"
  | "europe";

interface FoundationsFloatingActionProps {
  track?: FoundationsTrackKey;
  customLabel?: string;
  customHref?: string;
  customBadge?: string;
}

const TRACK_CONFIGS: Record<
  FoundationsTrackKey,
  { label: string; href: string; badge: string }
> = {
  foundations: {
    label: "Explore Pathways",
    href: "#pathways",
    badge: "Four Pathways",
  },
  golf: {
    label: "Inquire Golf Cohort",
    href: "/book?topic=golf",
    badge: "10-Week Program",
  },
  hockey: {
    label: "Inquire Team Program",
    href: "/book?topic=hockey",
    badge: "Game-Speed Focus",
  },
  corporate: {
    label: "Book Corporate Workshop",
    href: "/book?topic=corporate",
    badge: "Leadership Track",
  },
  europe: {
    label: "Connect European Summit",
    href: "/book?topic=europe",
    badge: "Transatlantic Track",
  },
};

export function FoundationsFloatingAction({
  track = "foundations",
  customLabel,
  customHref,
  customBadge,
}: FoundationsFloatingActionProps) {
  const [isVisible, setIsVisible] = useState(false);
  const reduce = useReducedMotion();

  const config = TRACK_CONFIGS[track] ?? TRACK_CONFIGS.foundations;
  const label = customLabel ?? config.label;
  const href = customHref ?? config.href;
  const badge = customBadge ?? config.badge;

  useEffect(() => {
    const handleScroll = () => {
      // Reveal after user scrolls past 380px of hero content
      const scrolledPastHero = window.scrollY > 380;
      setIsVisible(scrolledPastHero);
    };

    window.addEventListener("scroll", handleScroll, { passive: true });
    handleScroll();

    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  if (reduce) {
    if (!isVisible) return null;
    return (
      <div className="fixed bottom-5 left-5 z-40 sm:bottom-7 sm:left-7">
        <Link
          href={href}
          className="flex items-center gap-2.5 rounded-full border border-[rgba(198,165,92,0.6)] bg-[#171412] px-4 py-2.5 text-xs font-bold uppercase tracking-wider text-white shadow-xl"
        >
          <span>{label}</span>
          <ArrowUpRight size={14} aria-hidden="true" />
        </Link>
      </div>
    );
  }

  return (
    <AnimatePresence>
      {isVisible && (
        <motion.div
          initial={{ opacity: 0, y: 24, scale: 0.94 }}
          animate={{ opacity: 1, y: 0, scale: 1 }}
          exit={{ opacity: 0, y: 20, scale: 0.94 }}
          whileHover={{ scale: 1.03, y: -2 }}
          whileTap={{ scale: 0.97 }}
          transition={{ duration: 0.3, ease: [0.22, 1, 0.36, 1] }}
          className="fixed bottom-5 left-5 sm:bottom-7 sm:left-7 z-40 group"
          aria-label={`Floating quick action: ${label}`}
        >
          <Link
            href={href}
            className="relative flex items-center gap-3 overflow-hidden rounded-full border border-[rgba(198,165,92,0.55)] bg-[linear-gradient(135deg,rgba(23,20,18,0.96)_0%,rgba(32,27,24,0.94)_100%)] px-4 py-2.5 sm:px-5 sm:py-3 text-[var(--ivory)] shadow-[0_18px_40px_rgba(23,20,18,0.35)] backdrop-blur-xl transition-all duration-300 hover:border-[var(--champagne)] hover:shadow-[0_20px_50px_rgba(198,165,92,0.25)]"
          >
            {/* Live active availability pulse dot */}
            <span className="relative flex h-2 w-2 shrink-0">
              <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-[var(--champagne)] opacity-75" />
              <span className="relative inline-flex h-2 w-2 rounded-full bg-[var(--champagne)]" />
            </span>

            <div className="flex flex-col text-left">
              {badge && (
                <span className="text-[9px] font-bold uppercase tracking-[0.2em] text-[var(--champagne)] leading-none">
                  {badge}
                </span>
              )}
              <span className="font-serif text-sm font-semibold tracking-wide text-white group-hover:text-[var(--champagne)] transition-colors leading-tight mt-0.5">
                {label}
              </span>
            </div>

            <div className="ml-1 flex h-6 w-6 sm:h-7 sm:w-7 shrink-0 items-center justify-center rounded-full bg-[linear-gradient(135deg,var(--champagne)_0%,#d8b96e_100%)] text-[var(--ink)] shadow-md transition-transform duration-300 group-hover:translate-x-0.5 group-hover:-translate-y-0.5">
              <ArrowUpRight
                size={14}
                aria-hidden="true"
                className="stroke-[2.5]"
              />
            </div>
          </Link>
        </motion.div>
      )}
    </AnimatePresence>
  );
}
