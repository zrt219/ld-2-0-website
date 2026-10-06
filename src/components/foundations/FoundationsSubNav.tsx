"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useState, useEffect, useSyncExternalStore } from "react";
import { motion } from "framer-motion";

type SubNavItem = {
  label: string;
  href: string;
};

const subNavItems: SubNavItem[] = [
  { label: "Start Here", href: "/foundations#start-here" },
  { label: "Golf", href: "/foundations/golf" },
  { label: "Hockey", href: "/foundations/hockey" },
  { label: "Corporate", href: "/foundations/corporate" },
  { label: "Europe", href: "/foundations/europe" },
  { label: "Resources", href: "/foundations#resources" },
];

export function FoundationsSubNav() {
  const hydrated = useSyncExternalStore(
    () => () => {},
    () => true,
    () => false,
  );
  const pathname = usePathname();
  const [isScrolled, setIsScrolled] = useState(false);
  const [activeHash, setActiveHash] = useState<string>("");

  useEffect(() => {
    const handleScroll = () => {
      // Trigger subtle scroll elevation when page is scrolled down
      setIsScrolled(window.scrollY > 40);
    };
    window.addEventListener("scroll", handleScroll, { passive: true });
    handleScroll();
    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  // Track hash on page load and hash changes
  useEffect(() => {
    const updateHash = () => {
      if (typeof window !== "undefined") {
        setActiveHash(window.location.hash);
      }
    };
    updateHash();
    window.addEventListener("hashchange", updateHash);
    return () => window.removeEventListener("hashchange", updateHash);
  }, [pathname]);

  // Scroll spy for sections when on /foundations
  useEffect(() => {
    if (pathname !== "/foundations") return;

    const handleSpy = () => {
      const resourcesEl = document.getElementById("resources");
      if (!resourcesEl) return;
      const rect = resourcesEl.getBoundingClientRect();
      // If resources section enters the upper area of the viewport
      if (rect.top <= 240 && rect.bottom >= 120) {
        setActiveHash("#resources");
      } else if (rect.top > 240) {
        // Above resources section
        if (window.location.hash === "#resources") {
          setActiveHash("#start-here");
        } else {
          setActiveHash(window.location.hash || "#start-here");
        }
      }
    };

    window.addEventListener("scroll", handleSpy, { passive: true });
    return () => window.removeEventListener("scroll", handleSpy);
  }, [pathname]);

  // Resolve the single active tab label strictly and deterministically
  const getActiveLabel = (): string => {
    if (pathname.startsWith("/foundations/golf") || pathname === "/foundations/clubs") {
      return "Golf";
    }
    if (pathname.startsWith("/foundations/hockey")) {
      return "Hockey";
    }
    if (pathname.startsWith("/foundations/corporate")) {
      return "Corporate";
    }
    if (pathname.startsWith("/foundations/europe")) {
      return "Europe";
    }
    if (pathname === "/foundations") {
      return activeHash === "#resources" ? "Resources" : "Start Here";
    }
    return "";
  };

  const activeLabel = getActiveLabel();

  return (
    <nav
      data-hydrated={hydrated ? "true" : "false"}
      aria-label="Foundations section navigation"
      className={`sticky top-[94px] z-30 w-full border-b border-[#dfd1b4] bg-[#fbf8f0]/95 backdrop-blur-md transition-shadow duration-300 ${
        isScrolled ? "shadow-[0_4px_20px_rgba(30,24,15,0.06)]" : ""
      }`}
    >
      <div className="mx-auto flex h-[58px] sm:h-[60px] max-w-7xl items-center px-4 sm:px-6 lg:px-8 xl:max-w-[1440px] 2xl:max-w-[1536px]">
        {/* Left: Foundations Brand Eyebrow + Links Rail */}
        <div className="flex h-full min-w-0 flex-1 items-center gap-3 sm:gap-6 overflow-x-auto no-scrollbar py-1">
          {/* Section Indicator Badge */}
          <div className="flex shrink-0 items-center gap-3 pr-2 sm:pr-4 border-r border-[#d9c69e]/70">
            <span className="text-[10px] sm:text-[11px] font-bold uppercase tracking-[0.24em] text-[var(--gold-dark)] select-none">
              Foundations
            </span>
          </div>

          {/* Links list */}
          <div className="flex h-full items-center gap-1 sm:gap-2">
            {subNavItems.map((item) => {
              const active = item.label === activeLabel;
              return (
                <Link
                  key={item.href}
                  href={item.href}
                  aria-current={active ? "page" : undefined}
                  onClick={() => {
                    if (item.href.includes("#resources")) {
                      setActiveHash("#resources");
                    } else if (item.href.includes("#start-here")) {
                      setActiveHash("#start-here");
                    }
                  }}
                  className={`group relative flex h-full shrink-0 items-center px-2.5 sm:px-3 text-[11px] sm:text-[12px] font-bold uppercase tracking-[0.16em] transition-colors focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)] whitespace-nowrap ${
                    active
                      ? "text-[var(--gold-dark)] font-extrabold"
                      : "text-[#5c5246] hover:text-[var(--ink)]"
                  }`}
                >
                  <span className="py-1">{item.label}</span>
                  {active && (
                    <motion.span
                      layoutId="subnav-active-pill"
                      className="absolute inset-x-1.5 bottom-0 h-[2.5px] rounded-t-full bg-[var(--gold-dark)]"
                      transition={{ type: "spring", stiffness: 380, damping: 30 }}
                      aria-hidden="true"
                    />
                  )}
                </Link>
              );
            })}
          </div>
        </div>
      </div>
    </nav>
  );
}
