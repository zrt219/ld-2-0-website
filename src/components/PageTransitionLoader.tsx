"use client";

import { useEffect, useState, useTransition } from "react";
import Image from "next/image";
import { usePathname } from "next/navigation";

/**
 * PageTransitionLoader provides a luxury Lornette Daye LD gold monogram loading
 * overlay during Next.js client-side page route transitions.
 *
 * It listens to internal link navigations, provides immediate visual feedback
 * with an organic golden breathing glow, and smoothly fades out once the new route renders.
 */
export function PageTransitionLoader() {
  const pathname = usePathname();
  const [isLoading, setIsLoading] = useState(false);
  const [, startTransition] = useTransition();

  // Reset loading whenever pathname changes
  useEffect(() => {
    setIsLoading(false);
  }, [pathname]);

  // Intercept click on internal links to activate transition loader
  useEffect(() => {
    const handleAnchorClick = (e: MouseEvent) => {
      // Find the closest anchor tag
      const target = (e.target as HTMLElement)?.closest("a");
      if (!target) return;

      const href = target.getAttribute("href");
      if (!href) return;

      // Ignore external links, mailto, tel, anchor jumps, or new tab clicks
      if (
        href.startsWith("http://") ||
        href.startsWith("https://") ||
        href.startsWith("mailto:") ||
        href.startsWith("tel:") ||
        href.startsWith("#") ||
        target.target === "_blank" ||
        e.ctrlKey ||
        e.metaKey ||
        e.shiftKey ||
        e.altKey
      ) {
        return;
      }

      // Check if it's the exact same pathname (e.g. clicking current page or in-page hash)
      const url = new URL(href, window.location.origin);
      if (url.pathname === window.location.pathname && url.search === window.location.search) {
        return;
      }

      // Only trigger if navigating to a new path
      startTransition(() => {
        setIsLoading(true);
      });
    };

    document.addEventListener("click", handleAnchorClick, { capture: true });

    return () => {
      document.removeEventListener("click", handleAnchorClick, { capture: true });
    };
  }, []);

  // Safety fallback timeout: never keep loader stuck if navigation is cancelled or instant
  useEffect(() => {
    if (!isLoading) return;
    const timer = setTimeout(() => {
      setIsLoading(false);
    }, 4000);
    return () => clearTimeout(timer);
  }, [isLoading]);

  if (!isLoading) return null;

  return (
    <div
      role="status"
      aria-live="polite"
      aria-label="Loading page"
      className="fixed inset-0 z-[9999] flex flex-col items-center justify-center bg-[rgba(250,247,240,0.92)] backdrop-blur-md transition-opacity duration-300 animate-fadeIn"
    >
      {/* Luxury Golden Ambient Backlight Glow */}
      <div className="absolute h-64 w-64 rounded-full bg-[radial-gradient(circle,rgba(218,185,115,0.35)_0%,rgba(198,165,92,0.12)_50%,transparent_70%)] animate-pulse" />

      {/* Center Emblem Container */}
      <div className="relative flex flex-col items-center">
        {/* Outer Circular Ring with subtle gold shimmer */}
        <div className="relative flex h-28 w-28 sm:h-32 sm:w-32 items-center justify-center rounded-full p-1 shadow-[0_12px_40px_rgba(127,91,29,0.18)] bg-[linear-gradient(145deg,rgba(255,255,255,0.95),rgba(245,237,222,0.9))] border border-[rgba(198,165,92,0.55)]">
          {/* Subtle spinning gold accent orbit */}
          <div className="absolute inset-0 rounded-full border-2 border-transparent border-t-[var(--champagne)] border-r-[rgba(198,165,92,0.6)] animate-spin" style={{ animationDuration: "1.8s" }} />

          {/* Authentic LD Emblem */}
          <div className="relative h-20 w-20 sm:h-24 sm:w-24 overflow-hidden rounded-full shadow-inner">
            <Image
              src="/ld-loading-badge.png"
              alt="Lornette Daye"
              fill
              priority
              unoptimized
              className="object-cover scale-105"
            />
          </div>
        </div>

        {/* Elegant typography subtitle */}
        <div className="mt-5 flex flex-col items-center">
          <p className="font-serif text-sm sm:text-base font-semibold tracking-[0.24em] text-[var(--gold-dark)] uppercase">
            LORNETTE DAYE
          </p>
          <div className="mt-1 flex items-center gap-1.5">
            <span className="h-1 w-1 rounded-full bg-[var(--champagne)] animate-ping" />
            <span className="text-[10px] font-bold tracking-[0.26em] uppercase text-[#8c7d6b]">
              Loading
            </span>
          </div>
        </div>
      </div>
    </div>
  );
}
