"use client";

import { useEffect, useRef, useState } from "react";
import Image from "next/image";
import Link from "next/link";
import { usePathname } from "next/navigation";
import {
  Compass,
  FileText,
  Flame,
  Home,
  LogOut,
  MapPin,
  Pause,
  Play,
  PlayCircle,
  RotateCcw,
  Settings,
  ShieldCheck,
} from "lucide-react";
import { logoutFoundationsAction } from "@/app/foundations/login/actions";

type ScenicSlide = {
  src: string;
  theme: string;
  title: string;
};

const SCENIC_SLIDES: ScenicSlide[] = [
  {
    src: "/foundations/golf/scenic-gold-sunrise.jpg",
    theme: "Gold Sunrise",
    title: "Golden Hour Championship Links & Dewy Green",
  },
  {
    src: "/foundations/golf/scenic-beach-links.jpg",
    theme: "Beach Links",
    title: "Coastal White Sand Beach & Turquoise Ocean Fairway",
  },
  {
    src: "/foundations/golf/scenic-mountain-fairway.jpg",
    theme: "Mountain Vista",
    title: "Sunlit Alpine Mountain Valley & Fairway Reflection Pond",
  },
];

type NavItem = {
  label: string;
  href: string;
  icon: typeof Home;
  exact?: boolean;
};

const navItems: NavItem[] = [
  { label: "Dashboard", href: "/foundations/dashboard", icon: Home, exact: true },
  { label: "My Journey", href: "/foundations/progress", icon: MapPin },
  { label: "Lessons", href: "/foundations/lessons", icon: PlayCircle },
  { label: "Quick Tools", href: "/foundations/quick-tools", icon: RotateCcw },
  { label: "Grill-Me Lab", href: "/foundations/grill-me", icon: Flame },
  { label: "My Plan", href: "/foundations/plan", icon: Compass },
  { label: "Resources", href: "/foundations/resources", icon: FileText },
];

type LearnerSidebarProps = {
  onNavClick?: () => void;
  className?: string;
};

export function LearnerSidebar({ onNavClick, className = "" }: LearnerSidebarProps) {
  const pathname = usePathname();
  const [activeSlide, setActiveSlide] = useState(0);
  const [isHovered, setIsHovered] = useState(false);
  const [isFocused, setIsFocused] = useState(false);
  const [isUserPaused, setIsUserPaused] = useState(() => {
    if (typeof window !== "undefined") {
      return window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    }
    return false;
  });
  const tabRefs = useRef<(HTMLButtonElement | null)[]>([]);

  // Respect system prefers-reduced-motion setting
  useEffect(() => {
    if (typeof window === "undefined") return;
    const mediaQuery = window.matchMedia("(prefers-reduced-motion: reduce)");
    const handler = (e: MediaQueryListEvent) => setIsUserPaused(e.matches);
    mediaQuery.addEventListener("change", handler);
    return () => mediaQuery.removeEventListener("change", handler);
  }, []);

  const isPaused = isHovered || isFocused || isUserPaused;

  // 6-second rotation countdown that resets cleanly whenever activeSlide changes
  useEffect(() => {
    if (isPaused) return;

    const timer = setTimeout(() => {
      setActiveSlide((prev) => (prev + 1) % SCENIC_SLIDES.length);
    }, 6000);

    return () => clearTimeout(timer);
  }, [isPaused, activeSlide]);

  const handleTabKeyDown = (e: React.KeyboardEvent, idx: number) => {
    if (e.key === "ArrowRight") {
      e.preventDefault();
      const nextIdx = (idx + 1) % SCENIC_SLIDES.length;
      setActiveSlide(nextIdx);
      tabRefs.current[nextIdx]?.focus();
    } else if (e.key === "ArrowLeft") {
      e.preventDefault();
      const prevIdx = (idx - 1 + SCENIC_SLIDES.length) % SCENIC_SLIDES.length;
      setActiveSlide(prevIdx);
      tabRefs.current[prevIdx]?.focus();
    }
  };

  const isActive = (item: NavItem) => {
    if (item.exact) {
      return pathname === item.href;
    }
    return pathname === item.href || pathname.startsWith(`${item.href}/`);
  };

  return (
    <aside
      aria-label="Participant portal navigation"
      className={`flex h-full w-full flex-col justify-between bg-[#fcfaf4] p-4 text-[#2c2620] overflow-y-auto no-scrollbar ${className}`}
    >
      <div>
        {/* Section Header: Athlete Workspace */}
        <div className="px-3.5 pb-2.5 pt-1 flex items-center justify-between">
          <p className="text-[12px] font-bold uppercase tracking-[0.2em] text-[#635546]">
            Athlete Workspace
          </p>
          <span className="text-[10px] font-semibold text-[#8f8070] uppercase tracking-wider">
            10-Week Cohort
          </span>
        </div>

        {/* Nav list */}
        <nav aria-label="Portal main links" className="space-y-1.5">
          {navItems.map((item) => {
            const Icon = item.icon;
            const active = isActive(item);
            return (
              <Link
                key={item.label}
                href={item.href}
                onClick={onNavClick}
                aria-current={active ? "page" : undefined}
                className={`group flex min-h-[48px] items-center gap-3.5 rounded-xl px-4 py-2.5 text-[16px] font-semibold transition-all duration-150 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)] ${
                  active
                    ? "bg-[#dfc288] text-[#1a1714] font-bold shadow-xs border border-[#cba65a]/60"
                    : "text-[#3d3328] hover:bg-[#f3e9dc] hover:text-[#1a1714]"
                }`}
              >
                <Icon
                  size={21}
                  aria-hidden="true"
                  className={active ? "text-[#1a1714] stroke-[2.3]" : "text-[#6b5d4d] stroke-[2] group-hover:text-[#1a1714]"}
                />
                <span className="tracking-[-0.015em]">{item.label}</span>
              </Link>
            );
          })}
        </nav>

        {/* Divider */}
        <div className="my-4 border-t border-[#ebdcc9]" />

        {/* Section Header: Account & Settings */}
        <div className="px-3.5 pb-2.5">
          <p className="text-[12px] font-bold uppercase tracking-[0.2em] text-[#635546]">
            Account &amp; Access
          </p>
        </div>

        {/* Secondary Links */}
        <div className="space-y-1.5">
          <Link
            href="/foundations/account"
            onClick={onNavClick}
            className={`group flex min-h-[48px] items-center gap-3.5 rounded-xl px-4 py-2.5 text-[16px] font-semibold transition-all duration-150 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)] ${
              pathname.startsWith("/foundations/account")
                ? "bg-[#dfc288] text-[#1a1714] font-bold shadow-xs border border-[#cba65a]/60"
                : "text-[#3d3328] hover:bg-[#f3e9dc] hover:text-[#1a1714]"
            }`}
          >
            <Settings size={21} aria-hidden="true" className="text-[#6b5d4d] stroke-[2] group-hover:text-[#1a1714]" />
            <span className="tracking-[-0.015em]">Account / Settings</span>
          </Link>

          <Link
            href="/foundations/admin"
            onClick={onNavClick}
            className={`group flex min-h-[48px] items-center gap-3.5 rounded-xl px-4 py-2.5 text-[16px] font-semibold transition-all duration-150 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)] ${
              pathname.startsWith("/foundations/admin")
                ? "bg-[#dfc288] text-[#1a1714] font-bold shadow-xs border border-[#cba65a]/60"
                : "text-[#3d3328] hover:bg-[#f3e9dc] hover:text-[#1a1714]"
            }`}
          >
            <ShieldCheck size={21} aria-hidden="true" className="text-[#6b5d4d] stroke-[2] group-hover:text-[#1a1714]" />
            <span className="tracking-[-0.015em]">Admin Console</span>
          </Link>

          <button
            type="button"
            onClick={async () => {
              await logoutFoundationsAction();
              if (onNavClick) onNavClick();
              window.location.href = "/foundations/login";
            }}
            className="w-full flex min-h-[48px] items-center gap-3.5 rounded-xl px-4 py-2.5 text-[16px] font-semibold text-[#5c4f40] hover:bg-[#f3e9dc] hover:text-[#1a1714] transition-colors focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)] cursor-pointer text-left"
          >
            <LogOut size={21} aria-hidden="true" className="stroke-[2]" />
            <span className="tracking-[-0.015em]">Log Out</span>
          </button>
        </div>
      </div>

      {/* Bottom Scenic Golf Image & Lornette Principle */}
      <div className="pt-4 pb-1">
        <div
          className="rounded-xl border border-[#ebdcc9] bg-[#fbf9f4] p-3 shadow-xs"
          role="region"
          aria-roledescription="carousel"
          aria-label="Scenic golf atmospheric gallery"
        >
          <div className="px-1 text-left">
            <p className="font-serif text-[11.5px] italic text-[#3d3328] leading-snug">
              “Your previous shot cannot hit your next shot.”
            </p>
            <p className="mt-1 text-[9px] font-bold uppercase tracking-[0.2em] text-[#8e7e6e]">
              Coach Lornette Daye
            </p>
          </div>

          <div
            className="group relative mt-2.5 h-26 w-full overflow-hidden rounded-md border border-[#dfcca6] bg-[#1a1714]"
            onMouseEnter={() => setIsHovered(true)}
            onMouseLeave={() => setIsHovered(false)}
            onFocusCapture={() => setIsFocused(true)}
            onBlurCapture={() => setIsFocused(false)}
          >
            {SCENIC_SLIDES.map((slide, idx) => {
              const isCurrent = idx === activeSlide;
              return (
                <div
                  key={slide.src}
                  role="tabpanel"
                  id={`scenic-panel-${idx}`}
                  aria-labelledby={`scenic-tab-${idx}`}
                  aria-hidden={!isCurrent}
                  className={`absolute inset-0 transition-opacity duration-1000 ease-in-out ${
                    isCurrent ? "opacity-100 z-1" : "opacity-0 z-0 pointer-events-none"
                  }`}
                >
                  <Image
                    src={slide.src}
                    alt=""
                    fill
                    sizes="(max-width: 1024px) 240px, 240px"
                    quality={92}
                    priority
                    className="object-cover"
                  />
                </div>
              );
            })}
            <div className="absolute inset-0 z-2 bg-gradient-to-t from-black/40 via-transparent to-black/15 pointer-events-none" />

            {/* Scenic Theme Label */}
            <div className="absolute top-2 left-2 z-10 flex items-center gap-1 rounded-xs bg-black/60 px-1.5 py-0.5 text-[8px] font-bold uppercase tracking-[0.18em] text-[#e2c792] backdrop-blur-xs border border-[rgba(226,199,146,0.3)] shadow-xs select-none pointer-events-none transition-all duration-300">
              <span>{SCENIC_SLIDES[activeSlide].theme}</span>
            </div>
          </div>

          {/* Micro-Controls: Sleek external indicator dots & Pause/Play */}
          <div className="mt-2 flex items-center justify-between px-1">
            <div
              role="tablist"
              aria-label="Scenic gallery slides"
              className="flex items-center gap-1"
            >
              {SCENIC_SLIDES.map((slide, idx) => {
                const isCurrent = idx === activeSlide;
                return (
                  <button
                    key={slide.src}
                    ref={(el) => {
                      tabRefs.current[idx] = el;
                    }}
                    type="button"
                    role="tab"
                    id={`scenic-tab-${idx}`}
                    aria-controls={`scenic-panel-${idx}`}
                    aria-selected={isCurrent}
                    tabIndex={isCurrent ? 0 : -1}
                    onClick={() => setActiveSlide(idx)}
                    onKeyDown={(e) => handleTabKeyDown(e, idx)}
                    className="group/tab min-h-[20px] min-w-[20px] inline-flex items-center justify-center p-1 focus-visible:outline focus-visible:outline-2 focus-visible:outline-[#a6864a] rounded-full cursor-pointer"
                    aria-label={`Slide ${idx + 1} of ${SCENIC_SLIDES.length}: ${slide.theme}`}
                    title={slide.title}
                  >
                    <span
                      className={`block h-1.5 rounded-full transition-all duration-300 ${
                        isCurrent
                          ? "w-3 bg-[#a6864a]"
                          : "w-1.5 bg-[#d4c3aa] group-hover/tab:bg-[#a6864a]/70"
                      }`}
                    />
                  </button>
                );
              })}
            </div>

            {/* Compact Accessible Pause/Play Toggle Button */}
            <button
              type="button"
              onClick={() => setIsUserPaused((prev) => !prev)}
              className="flex h-6 w-6 min-h-[24px] min-w-[24px] items-center justify-center text-[#8e7e6e] hover:text-[#2c2620] transition-colors focus-visible:outline focus-visible:outline-2 focus-visible:outline-[#a6864a] rounded-full cursor-pointer"
              aria-label={isUserPaused ? "Resume scenic slideshow" : "Pause scenic slideshow"}
              title={isUserPaused ? "Resume slideshow" : "Pause slideshow"}
            >
              {isUserPaused ? (
                <Play size={10} className="fill-current text-[#a6864a]" aria-hidden="true" />
              ) : (
                <Pause size={10} className="fill-current" aria-hidden="true" />
              )}
            </button>
          </div>

          <div className="mt-2 text-center">
            <p className="font-serif text-[9.5px] font-bold tracking-[0.22em] text-[#a6864a] uppercase select-none">
              Better People · Better Players
            </p>
          </div>
        </div>
      </div>
    </aside>
  );
}
