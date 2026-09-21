"use client";

import Link from "next/link";
import { ChevronDown } from "lucide-react";
import { usePathname } from "next/navigation";
import { useState, useRef, useEffect, useSyncExternalStore } from "react";
import { motion, AnimatePresence } from "framer-motion";

type SubNavChild = {
  label: string;
  href: string;
};

type SubNavItem = {
  label: string;
  href: string;
  exact: boolean;
  children?: SubNavChild[];
};

const subNavItems: SubNavItem[] = [
  { label: "Overview", href: "/foundations", exact: true },
  {
    label: "Golf",
    href: "/foundations/golf",
    exact: true,
    children: [
      { label: "Overview", href: "/foundations/golf" },
      { label: "Keynote Experience", href: "/foundations/golf/keynote" },
      { label: "Member Clinic & Workshop", href: "/foundations/golf/workshop" },
      { label: "10-Week Guided Program", href: "/foundations/golf/program" },
      { label: "Club Partnership", href: "/foundations/golf/club-partnership" },
      { label: "Program Registration", href: "/foundations/golf/register" },
    ],
  },
  { label: "Clubs & Teams", href: "/foundations/clubs", exact: false },
  { label: "Performance Edge", href: "/foundations/performance-edge", exact: false },
];

export function FoundationsSubNav() {
  const hydrated = useSyncExternalStore(
    () => () => {},
    () => true,
    () => false,
  );
  const pathname = usePathname();
  const [mobileOpen, setMobileOpen] = useState(false);
  const [activeDropdown, setActiveDropdown] = useState<string | null>(null);
  const [mobileExpandedGolf, setMobileExpandedGolf] = useState(true);
  const navRef = useRef<HTMLElement>(null);
  const toggleButtonRef = useRef<HTMLButtonElement>(null);
  const golfButtonRef = useRef<HTMLButtonElement>(null);

  // Close mobile drawer & desktop dropdown on route change
  const [prevPathname, setPrevPathname] = useState(pathname);
  if (prevPathname !== pathname) {
    setPrevPathname(pathname);
    setMobileOpen(false);
    setActiveDropdown(null);
  }

  // Handle escape key and click outside to close dropdowns / mobile drawer
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        if (activeDropdown) {
          setActiveDropdown(null);
          golfButtonRef.current?.focus();
        } else if (mobileOpen) {
          setMobileOpen(false);
          toggleButtonRef.current?.focus();
        }
      }
    };

    const handleClickOutside = (e: MouseEvent) => {
      if (navRef.current && !navRef.current.contains(e.target as Node)) {
        setMobileOpen(false);
        setActiveDropdown(null);
      }
    };

    document.addEventListener("keydown", handleKeyDown);
    document.addEventListener("mousedown", handleClickOutside);
    return () => {
      document.removeEventListener("keydown", handleKeyDown);
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, [mobileOpen, activeDropdown]);

  const isLinkActive = (href: string, exact: boolean) => {
    if (exact) {
      return pathname === href;
    }
    return pathname === href || pathname.startsWith(`${href}/`);
  };

  const isGolfActive = pathname.startsWith("/foundations/golf");

  const activeItem =
    subNavItems.find((item) =>
      item.label === "Golf" ? isGolfActive : isLinkActive(item.href, item.exact),
    ) ?? subNavItems[0];

  return (
    <nav
      ref={navRef}
      data-hydrated={hydrated ? "true" : "false"}
      aria-label="Foundations section navigation"
      className="sticky top-[83px] z-30 border-b border-[#dfd1b4] bg-[#fbf8f0]/95 px-4 backdrop-blur-md sm:px-6 lg:px-8"
    >
      <div className="mx-auto max-w-7xl">
        {/* Mobile Collapsible Subnav */}
        <div className="lg:hidden py-1">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-2">
              <span className="text-[0.65rem] font-bold uppercase tracking-[0.22em] text-[#6f655a]">
                Foundations /
              </span>
              <span className="text-xs font-bold uppercase tracking-[0.16em] text-[var(--gold-dark)]">
                {activeItem.label}
              </span>
            </div>
            <button
              ref={toggleButtonRef}
              type="button"
              onClick={() => setMobileOpen((prev) => !prev)}
              aria-expanded={mobileOpen}
              aria-controls="foundations-mobile-subnav"
              aria-label={mobileOpen ? "Close Foundations section menu" : "Open Foundations section menu"}
              className="flex min-h-11 min-w-11 items-center justify-center text-[#6f655a] hover:text-[var(--gold-dark)] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)]"
            >
              <ChevronDown
                size={16}
                aria-hidden="true"
                className={`transition-transform duration-200 ${
                  mobileOpen ? "rotate-180 text-[var(--gold-dark)]" : ""
                }`}
              />
            </button>
          </div>

          <AnimatePresence initial={false}>
            {mobileOpen ? (
              <motion.div
                id="foundations-mobile-subnav"
                initial={{ height: 0, opacity: 0 }}
                animate={{ height: "auto", opacity: 1 }}
                exit={{ height: 0, opacity: 0 }}
                transition={{ duration: 0.2, ease: "easeInOut" }}
                className="overflow-hidden border-t border-[#dfd1b4] pt-2 mt-1"
              >
                <div className="grid gap-1 pb-2">
                  {subNavItems.map((item) => {
                    if (item.children) {
                      const isParentActive = isGolfActive;
                      return (
                        <div key={item.label} className="border-b border-[var(--line)]/50 pb-1">
                          <div className="flex items-center justify-between">
                            <Link
                              href={item.href}
                              aria-current={pathname === item.href ? "page" : undefined}
                              className={`flex min-h-11 flex-1 items-center px-2 py-2 text-xs font-bold uppercase tracking-[0.16em] transition focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)] ${
                                isParentActive
                                  ? "font-semibold text-[var(--gold-dark)]"
                                  : "text-[#62584c] hover:text-[var(--gold-dark)]"
                              }`}
                            >
                              {item.label}
                            </Link>
                            <button
                              type="button"
                              onClick={() => setMobileExpandedGolf((prev) => !prev)}
                              aria-expanded={mobileExpandedGolf}
                              aria-label={mobileExpandedGolf ? "Collapse Golf subpages" : "Expand Golf subpages"}
                              className="flex min-h-11 min-w-11 items-center justify-center text-[#6f655a] hover:text-[var(--gold-dark)]"
                            >
                              <ChevronDown
                                size={14}
                                aria-hidden="true"
                                className={`transition-transform duration-200 ${
                                  mobileExpandedGolf ? "rotate-180 text-[var(--gold-dark)]" : ""
                                }`}
                              />
                            </button>
                          </div>
                          {mobileExpandedGolf && (
                            <div className="ml-4 pl-2 border-l border-[#d9c69e]/50 grid gap-0.5 py-1">
                              {item.children.map((child) => {
                                const childActive = pathname === child.href;
                                return (
                                  <Link
                                    key={child.href}
                                    href={child.href}
                                    aria-current={childActive ? "page" : undefined}
                                    className={`flex min-h-11 items-center px-2 py-2 text-xs font-medium tracking-[0.08em] transition ${
                                      childActive
                                        ? "font-bold text-[var(--gold-dark)]"
                                        : "text-[#7a6f62] hover:text-[var(--ink)]"
                                    }`}
                                  >
                                    {child.label}
                                  </Link>
                                );
                              })}
                            </div>
                          )}
                        </div>
                      );
                    }

                    const active = isLinkActive(item.href, item.exact);
                    return (
                      <Link
                        key={item.href}
                        href={item.href}
                        aria-current={active ? "page" : undefined}
                        className={`flex min-h-11 items-center border-b border-[var(--line)]/50 px-2 py-2 text-xs font-bold uppercase tracking-[0.16em] transition focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)] ${
                          active
                            ? "font-semibold text-[var(--gold-dark)]"
                            : "text-[#62584c] hover:text-[var(--gold-dark)]"
                        }`}
                      >
                        {item.label}
                      </Link>
                    );
                  })}
                </div>
              </motion.div>
            ) : null}
          </AnimatePresence>
        </div>

        {/* Desktop Horizontal Subnav */}
        <div className="hidden lg:flex items-center gap-6 py-0">
          <span className="text-[0.68rem] font-bold uppercase tracking-[0.24em] text-[var(--gold-dark)] pr-3 border-r border-[#d9c69e]/60">
            Foundations
          </span>
          <div className="flex items-center gap-4 py-1">
            {subNavItems.map((item) => {
              if (item.children) {
                const isParentActive = isGolfActive;
                const isDropdownOpen = activeDropdown === item.label;
                return (
                  <div
                    key={item.label}
                    className="relative flex items-center"
                    onBlur={(e) => {
                      if (!e.currentTarget.contains(e.relatedTarget as Node)) {
                        setActiveDropdown((curr) => (curr === item.label ? null : curr));
                      }
                    }}
                  >
                    <Link
                      href={item.href}
                      aria-current={pathname === item.href ? "page" : undefined}
                      className={`min-h-11 shrink-0 flex items-center border-b-2 pl-4 pr-1 py-3 text-xs font-bold uppercase tracking-[0.18em] transition focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)] ${
                        isParentActive
                          ? "border-[var(--gold-dark)] text-[var(--gold-dark)]"
                          : "border-transparent text-[#62584c] hover:border-[var(--champagne)] hover:text-[var(--ink)]"
                      }`}
                    >
                      {item.label}
                    </Link>
                    <button
                      ref={golfButtonRef}
                      type="button"
                      aria-expanded={isDropdownOpen}
                      aria-controls="foundations-golf-submenu"
                      aria-label={isDropdownOpen ? "Close Golf subpages menu" : "Open Golf subpages menu"}
                      onClick={() => setActiveDropdown((prev) => (prev === item.label ? null : item.label))}
                      className="mr-2 flex min-h-11 min-w-8 items-center justify-center text-[#6f655a] transition-colors hover:text-[var(--gold-dark)] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-1 focus-visible:outline-[var(--gold-dark)]"
                    >
                      <ChevronDown
                        size={12}
                        aria-hidden="true"
                        className={`transition-transform duration-200 ${
                          isDropdownOpen ? "rotate-180 text-[var(--gold-dark)]" : "text-[#6f655a]"
                        }`}
                      />
                    </button>

                    <AnimatePresence>
                      {isDropdownOpen && (
                        <motion.div
                          id="foundations-golf-submenu"
                          initial={{ opacity: 0, y: -4 }}
                          animate={{ opacity: 1, y: 0 }}
                          exit={{ opacity: 0, y: -4 }}
                          transition={{ duration: 0.14, ease: "easeOut" }}
                          className="absolute left-0 top-full z-50 pt-1"
                        >
                          <ul className="w-[260px] list-none rounded-[1px] border border-[#dfd1b4] bg-[#fbf8f0] py-1.5 m-0 shadow-[0_8px_24px_rgba(30,24,15,0.08)]">
                            {item.children.map((child) => {
                              const childActive = pathname === child.href;
                              return (
                                <li key={child.href}>
                                  <Link
                                    href={child.href}
                                    aria-current={childActive ? "page" : undefined}
                                    onClick={() => setActiveDropdown(null)}
                                    className={`flex min-h-11 items-center px-4 py-2 text-[12.5px] font-semibold tracking-wide transition-colors duration-150 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-[-2px] focus-visible:outline-[var(--gold-dark)] ${
                                      childActive
                                        ? "border-l-2 border-[var(--gold-dark)] bg-[#faf4e6]/60 pl-3.5 text-[var(--gold-dark)]"
                                        : "border-l-2 border-transparent text-[#2f2a25] hover:bg-[#faf4e6]/40 hover:text-[var(--gold-dark)]"
                                    }`}
                                  >
                                    {child.label}
                                  </Link>
                                </li>
                              );
                            })}
                          </ul>
                        </motion.div>
                      )}
                    </AnimatePresence>
                  </div>
                );
              }

              const active = isLinkActive(item.href, item.exact);
              return (
                <Link
                  key={item.href}
                  href={item.href}
                  aria-current={active ? "page" : undefined}
                  className={`min-h-11 shrink-0 flex items-center border-b-2 px-4 py-3 text-xs font-bold uppercase tracking-[0.18em] transition focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)] ${
                    active
                      ? "border-[var(--gold-dark)] text-[var(--gold-dark)]"
                      : "border-transparent text-[#62584c] hover:border-[var(--champagne)] hover:text-[var(--ink)]"
                  }`}
                >
                  {item.label}
                </Link>
              );
            })}
          </div>
        </div>
      </div>
    </nav>
  );
}
