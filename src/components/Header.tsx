"use client";

import Image from "next/image";
import Link from "next/link";
import { ArrowRight, ArrowUpRight, BookOpen, ChevronDown, Compass, Menu, Sparkles, X } from "lucide-react";
import { usePathname } from "next/navigation";
import { useState, useRef, useEffect, useSyncExternalStore } from "react";
import { motion, AnimatePresence } from "framer-motion";

import { mainNav, siteCopy, type NavItem } from "@/content/site";
import { FoundationsMegaMenu, foundationsPathways } from "@/components/FoundationsMegaMenu";

export function Header() {
  const hydrated = useSyncExternalStore(
    () => () => {},
    () => true,
    () => false,
  );
  const [open, setOpen] = useState(false);
  const [activeDropdown, setActiveDropdown] = useState<string | null>(null);
  const [mobileExpanded, setMobileExpanded] = useState<Record<string, boolean>>({
    Foundations: true,
    Books: true,
  });
  const pathname = usePathname();
  const dropdownContainerRef = useRef<HTMLUListElement>(null);
  const megaMenuRef = useRef<HTMLDivElement>(null);
  const buttonRefs = useRef<Record<string, HTMLButtonElement | null>>({});
  const mobileMenuButtonRef = useRef<HTMLButtonElement>(null);

  const isItemActive = (item: NavItem) => {
    if (item.children) {
      return (
        pathname === item.href ||
        item.children.some(
          (child) =>
            pathname === child.href ||
            (child.href !== "/" && pathname.startsWith(`${child.href}/`)),
        )
      );
    }
    return pathname === item.href || (item.href !== "/" && pathname.startsWith(`${item.href}/`));
  };

  const isChildActive = (href: string) => {
    if (href === "/foundations" || href === "/books") {
      return pathname === href;
    }
    return pathname === href || (href !== "/" && pathname.startsWith(`${href}/`));
  };

  // Automatically close dropdowns and mobile menu on route change
  const [prevPathname, setPrevPathname] = useState(pathname);
  if (prevPathname !== pathname) {
    setPrevPathname(pathname);
    setActiveDropdown(null);
    setOpen(false);
  }

  // Handle escape key and click outside to close desktop dropdowns and mobile menu
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        if (activeDropdown) {
          const triggerBtn = buttonRefs.current[activeDropdown];
          setActiveDropdown(null);
          if (triggerBtn) {
            triggerBtn.focus();
          }
        } else if (open) {
          setOpen(false);
          mobileMenuButtonRef.current?.focus();
        }
      }
    };

    const handleClickOutside = (e: MouseEvent) => {
      const target = e.target as Node;
      if (
        dropdownContainerRef.current &&
        !dropdownContainerRef.current.contains(target) &&
        !megaMenuRef.current?.contains(target)
      ) {
        setActiveDropdown(null);
      }
    };

    document.addEventListener("keydown", handleKeyDown);
    document.addEventListener("mousedown", handleClickOutside);
    return () => {
      document.removeEventListener("keydown", handleKeyDown);
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, [activeDropdown, open]);

  const toggleDropdown = (label: string) => {
    setActiveDropdown((prev) => (prev === label ? null : label));
  };

  const toggleMobileSection = (label: string) => {
    setMobileExpanded((prev) => ({
      ...prev,
      [label]: !prev[label],
    }));
  };

  const primaryItems = mainNav.slice(0, -1);

  return (
    <header
      data-hydrated={hydrated ? "true" : "false"}
      className="sticky top-0 z-50 border-y border-[#dfd1b4] bg-[#fbf8f0]"
    >
      <nav
        className="mx-auto flex h-[94px] max-w-7xl items-center justify-between px-5 sm:px-8 xl:max-w-[1440px] xl:gap-10 xl:px-8 2xl:max-w-[1536px] 2xl:px-12"
        aria-label="Primary navigation"
      >
        <Link
          href="/"
          className="flex shrink-0 items-center gap-3.5 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[var(--gold-dark)]"
        >
          <Image
            src="/monogramlogo.png"
            alt="Lornette Daye LD monogram logo"
            width={140}
            height={82}
            priority
            unoptimized
            className="h-[58px] sm:h-[66px] w-auto max-w-[104px] sm:max-w-[118px] object-contain"
          />
          <span className="hidden h-11 w-px bg-[#d9c69e] sm:block shrink-0" aria-hidden="true" />
          <span className="shrink-0">
            <span className="block font-serif text-[1.35rem] leading-none tracking-[-0.01em] text-[#171412] sm:text-[1.62rem] whitespace-nowrap">
              {siteCopy.brandName}
            </span>
            <span className="hidden text-[0.66rem] font-bold uppercase tracking-[0.24em] text-[#6f655a] sm:block mt-1 whitespace-nowrap">
              Speaker · Coach · Leader
            </span>
          </span>
        </Link>

        {/* Desktop Split Navigation */}
        <ul
          ref={dropdownContainerRef}
          className="hidden h-full items-center list-none m-0 p-0 xl:flex xl:gap-5 2xl:gap-6"
        >
          {primaryItems.map((item) => {
            const hasChildren = Boolean(item.children && item.children.length > 0);
            const isOpen = activeDropdown === item.label;
            const active = isItemActive(item);
            const submenuId = `${item.label.toLowerCase().replace(/[^a-z0-9]/g, "-")}-submenu`;

            if (hasChildren) {
              return (
                <li
                  key={item.label}
                  className="flex h-full items-center"
                  onBlur={(e) => {
                    if (
                      !e.currentTarget.contains(e.relatedTarget as Node) &&
                      !megaMenuRef.current?.contains(e.relatedTarget as Node)
                    ) {
                      setActiveDropdown((curr) => (curr === item.label ? null : curr));
                    }
                  }}
                >
                  <div className="group relative flex items-center">
                    {/* Standard Text Link */}
                    <Link
                      href={item.href}
                      aria-current={active ? "page" : undefined}
                      className={`relative flex items-center py-2 text-sm font-semibold tracking-[-0.01em] transition-colors group-hover:text-[var(--gold-dark)] hover:text-[var(--gold-dark)] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[var(--gold-dark)] ${
                        active ? "text-[var(--gold-dark)]" : "text-[#2f2a25]"
                      }`}
                    >
                      <span className="relative">
                        {item.label}
                        {active && (
                          <span
                            aria-hidden="true"
                            className="absolute -bottom-1 inset-x-0 h-[2px] bg-[var(--gold-dark)]"
                          />
                        )}
                      </span>
                    </Link>

                    {/* Adjacent Disclosure Button */}
                    <button
                      ref={(el) => {
                        buttonRefs.current[item.label] = el;
                      }}
                      type="button"
                      aria-expanded={isOpen}
                      aria-controls={submenuId}
                      aria-label={
                        isOpen
                          ? `Close ${item.label} menu`
                          : `Open ${item.label} menu`
                      }
                      onClick={() => toggleDropdown(item.label)}
                      className="ml-1 inline-flex h-5 w-4 items-center justify-center p-0 text-[#6f655a] transition-colors group-hover:text-[var(--gold-dark)] hover:text-[var(--gold-dark)] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-1 focus-visible:outline-[var(--gold-dark)] cursor-pointer"
                    >
                      <ChevronDown
                        size={12}
                        aria-hidden="true"
                        className={`transition-transform duration-200 ${
                          isOpen ? "rotate-180 text-[var(--gold-dark)]" : ""
                        }`}
                      />
                    </button>

                    {/* Refined Editorial Disclosure Flyout for Standard Dropdowns */}
                    <AnimatePresence>
                      {isOpen && item.label !== "Foundations" ? (
                        <motion.div
                          id={submenuId}
                          initial={{ opacity: 0, y: -4 }}
                          animate={{ opacity: 1, y: 0 }}
                          exit={{ opacity: 0, y: -4 }}
                          transition={{ duration: 0.14, ease: "easeOut" }}
                          className="absolute left-0 top-[calc(100%+16px)] z-50"
                        >
                          <ul className="w-[245px] list-none rounded-[1px] border border-[#dfd1b4] bg-[#fbf8f0] py-1.5 m-0 shadow-[0_8px_24px_rgba(30,24,15,0.06)]">
                            {item.children?.map((child) => {
                              const childActive = isChildActive(child.href);
                              return (
                                <li key={child.href}>
                                  <Link
                                    href={child.href}
                                    aria-current={childActive ? "page" : undefined}
                                    onClick={() => setActiveDropdown(null)}
                                    className={`flex min-h-[42px] items-center px-4 py-2.5 text-[13.5px] leading-snug transition-colors duration-150 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-[-2px] focus-visible:outline-[var(--gold-dark)] ${
                                      childActive
                                        ? "border-l-2 border-[var(--gold-dark)] bg-[#faf4e6]/50 pl-3.5 font-medium text-[var(--gold-dark)]"
                                        : "border-l-2 border-transparent font-normal text-[#2f2a25] hover:bg-[#faf4e6]/40 hover:text-[var(--gold-dark)]"
                                    }`}
                                  >
                                    {child.label}
                                  </Link>
                                </li>
                              );
                            })}
                          </ul>
                        </motion.div>
                      ) : null}
                    </AnimatePresence>
                  </div>
                </li>
              );
            }

            return (
              <li key={item.href} className="flex h-full items-center">
                <Link
                  href={item.href}
                  aria-current={active ? "page" : undefined}
                  className={`group relative flex items-center py-2 text-sm font-semibold tracking-[-0.01em] transition-colors hover:text-[var(--gold-dark)] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[var(--gold-dark)] ${
                    active ? "text-[var(--gold-dark)]" : "text-[#2f2a25]"
                  }`}
                >
                  <span className="relative">
                    {item.label}
                    {active && (
                      <span
                        aria-hidden="true"
                        className="absolute -bottom-1 inset-x-0 h-[2px] bg-[var(--gold-dark)]"
                      />
                    )}
                  </span>
                </Link>
              </li>
            );
          })}

          {/* Framer-styled BOOK LORNETTE button right beside Blog */}
          <li className="flex h-full items-center pl-1 xl:pl-1.5">
            <motion.div
              whileHover={{ scale: 1.03, y: -1 }}
              whileTap={{ scale: 0.97 }}
              transition={{ type: "spring", stiffness: 400, damping: 25 }}
            >
              <Link
                href="/book"
                className="group relative inline-flex items-center justify-center gap-1.5 rounded-[1px] bg-[#c7a75e] px-3.5 py-2 xl:px-4 xl:py-2 text-[11px] xl:text-[11.5px] font-bold uppercase tracking-[0.14em] text-[#171412] shadow-[0_2px_8px_rgba(199,167,94,0.22)] transition-all duration-200 hover:bg-[#d4b368] hover:shadow-[0_6px_20px_rgba(199,167,94,0.38)] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)] select-none whitespace-nowrap"
              >
                <span>BOOK LORNETTE</span>
                <ArrowUpRight
                  size={14}
                  className="transition-transform duration-200 group-hover:translate-x-0.5 group-hover:-translate-y-0.5"
                  aria-hidden="true"
                />
              </Link>
            </motion.div>
          </li>
        </ul>

        {/* Mobile menu trigger */}
        <button
          ref={mobileMenuButtonRef}
          type="button"
          data-mobile-menu-trigger
          className="inline-flex min-h-11 min-w-11 items-center justify-center border border-[#dfd1b4] text-[var(--ink)] xl:hidden cursor-pointer focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)]"
          aria-expanded={open}
          aria-controls="mobile-menu"
          aria-label={open ? "Close navigation menu" : "Open navigation menu"}
          onClick={() => setOpen((value) => !value)}
        >
          {open ? <X size={22} aria-hidden="true" /> : <Menu size={22} aria-hidden="true" />}
        </button>
      </nav>

      {/* Desktop Foundations Full-Width Mega Menu Flyout */}
      <AnimatePresence>
        {activeDropdown === "Foundations" ? (
          <motion.div
            ref={megaMenuRef}
            id="foundations-submenu"
            initial={{ opacity: 0, y: -6 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -6 }}
            transition={{ duration: 0.16, ease: "easeOut" }}
            className="absolute left-0 right-0 top-full z-50 px-4 sm:px-6 lg:px-8 py-2.5"
          >
            <FoundationsMegaMenu onClose={() => setActiveDropdown(null)} />
          </motion.div>
        ) : null}
      </AnimatePresence>

      {/* Mobile navigation drawer */}
      <AnimatePresence>
        {open ? (
          <motion.div
            id="mobile-menu"
            data-mobile-menu
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: "auto", opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.25, ease: "easeInOut" }}
            className="max-h-[calc(100dvh-94px)] overflow-y-auto no-scrollbar border-t border-[#dfd1b4] bg-[#fbf8f0] xl:hidden"
          >
            <div className="mx-auto grid max-w-7xl gap-1 px-4 pb-8 pt-4">
              {primaryItems.map((item) => {
                const hasChildren = Boolean(item.children && item.children.length > 0);
                const isExpanded = mobileExpanded[item.label] ?? false;
                const active = isItemActive(item);
                const mobileSubmenuId = `mobile-${item.label.toLowerCase().replace(/[^a-z0-9]/g, "-")}-submenu`;

                if (hasChildren) {
                  return (
                    <div key={item.label} className="border-b border-[var(--line)]">
                      <div className="flex items-center justify-between">
                        <Link
                          href={item.href}
                          aria-current={active ? "page" : undefined}
                          onClick={() => setOpen(false)}
                          className="flex min-h-11 flex-1 items-center px-2 py-3 text-base font-semibold text-[var(--ink)] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)]"
                        >
                          {item.label}
                        </Link>
                        <button
                          type="button"
                          onClick={() => toggleMobileSection(item.label)}
                          aria-expanded={isExpanded}
                          aria-controls={mobileSubmenuId}
                          aria-label={
                            isExpanded
                              ? `Collapse ${item.label} submenu`
                              : `Expand ${item.label} submenu`
                          }
                          className="flex min-h-11 min-w-11 items-center justify-center text-[#6f655a] hover:text-[var(--gold-dark)] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)]"
                        >
                          <ChevronDown
                            size={18}
                            aria-hidden="true"
                            className={`transition-transform duration-200 ${
                              isExpanded ? "rotate-180 text-[var(--gold-dark)]" : ""
                            }`}
                          />
                        </button>
                      </div>

                      <AnimatePresence initial={false}>
                        {isExpanded ? (
                          <motion.div
                            id={mobileSubmenuId}
                            initial={{ height: 0, opacity: 0 }}
                            animate={{ height: "auto", opacity: 1 }}
                            exit={{ height: 0, opacity: 0 }}
                            transition={{ duration: 0.2, ease: "easeInOut" }}
                            className="overflow-hidden bg-[rgba(245,239,228,0.5)] px-2.5 pb-3.5 pt-1"
                          >
                            {item.label === "Foundations" ? (
                              <div className="grid gap-2.5 pt-1.5">
                                {(() => {
                                  const isHubActive = pathname === "/foundations";
                                  return (
                                    <Link
                                      href="/foundations"
                                      aria-current={isHubActive ? "page" : undefined}
                                      onClick={() => setOpen(false)}
                                      className={`group flex items-center justify-between rounded-[2px] border px-3.5 py-2.5 text-[11px] font-extrabold uppercase tracking-[0.2em] shadow-xs transition-all ${
                                        isHubActive
                                          ? "border-[var(--gold-dark)] bg-[#faf4e6] text-[var(--gold-dark)] ring-1 ring-[var(--gold-dark)]/30 font-extrabold"
                                          : "border-[#dfd1b4] bg-[#fbf6ec] text-[var(--gold-dark)] hover:border-[var(--gold-dark)] hover:bg-[#f6ede0]"
                                      }`}
                                    >
                                      <div className="flex items-center gap-2">
                                        <Compass size={14} className="text-[var(--gold-dark)] shrink-0" />
                                        <span>Foundations Overview &amp; Hub</span>
                                      </div>
                                      <ArrowRight size={13} className="text-[var(--gold-dark)] transition-transform duration-200 group-hover:translate-x-1 shrink-0" />
                                    </Link>
                                  );
                                })()}

                                {foundationsPathways.map((pathway) => {
                                  const isPathwayActive = isChildActive(pathway.href);
                                  return (
                                    <Link
                                      key={pathway.title}
                                      href={pathway.href}
                                      aria-current={isPathwayActive ? "page" : undefined}
                                      onClick={() => setOpen(false)}
                                      className={`group relative flex items-center gap-3 sm:gap-3.5 overflow-hidden rounded-[3px] border p-2.5 sm:p-3 shadow-xs transition-all duration-200 active:scale-[0.99] ${
                                        isPathwayActive
                                          ? "border-[var(--gold-dark)] bg-[#faf4e6] shadow-md ring-1 ring-[var(--gold-dark)]/30"
                                          : "border-[#dfd1b4] bg-gradient-to-r from-white via-[#fdfbf8] to-[#faf6ee] hover:border-[var(--gold-dark)] hover:shadow-md"
                                      }`}
                                    >
                                      <div className="relative h-[62px] w-[78px] sm:h-[68px] sm:w-[88px] shrink-0 overflow-hidden rounded-[2px] border border-[rgba(198,165,92,0.35)] bg-[#171412] shadow-xs">
                                        <Image
                                          src={pathway.imageSrc}
                                          alt={pathway.imageAlt}
                                          fill
                                          sizes="88px"
                                          className="object-cover transition-transform duration-300 group-hover:scale-105"
                                          style={{ objectPosition: pathway.objectPosition || "center" }}
                                        />
                                        <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-black/40 via-transparent to-transparent" />
                                      </div>
                                      <div className="min-w-0 flex-1">
                                        <p className="text-[10px] font-extrabold uppercase tracking-[0.22em] text-[var(--gold-dark)]">
                                          {pathway.tagline}
                                        </p>
                                        <p className="font-serif text-[16px] sm:text-[17px] font-bold text-[#171412] leading-tight group-hover:text-[var(--gold-dark)] transition-colors">
                                          {pathway.title}
                                        </p>
                                        <p className="mt-0.5 sm:mt-1 text-[11px] sm:text-[11.5px] leading-snug text-[#675d50] line-clamp-1">
                                          {pathway.description}
                                        </p>
                                      </div>
                                      <div className={`flex h-7 w-7 shrink-0 items-center justify-center rounded-full border transition-all duration-200 shadow-xs ${
                                        isPathwayActive
                                          ? "border-[var(--gold-dark)] bg-[var(--gold-dark)] text-white"
                                          : "border-[rgba(198,165,92,0.4)] bg-[#faf5eb] text-[var(--gold-dark)] group-hover:border-[var(--gold-dark)] group-hover:bg-[var(--gold-dark)] group-hover:text-white"
                                      }`}>
                                        <ArrowUpRight size={14} aria-hidden="true" />
                                      </div>
                                    </Link>
                                  );
                                })}
                              </div>
                            ) : (
                              <div className="grid gap-2 py-1.5">
                                {item.children?.map((child) => {
                                  const childActive = isChildActive(child.href);
                                  const isCollection = child.href === "/collection";
                                  return (
                                    <Link
                                      key={child.href}
                                      href={child.href}
                                      aria-current={childActive ? "page" : undefined}
                                      onClick={() => setOpen(false)}
                                      className={`group flex min-h-[46px] items-center justify-between rounded-[2px] border px-3.5 py-2.5 text-xs font-bold uppercase tracking-[0.16em] transition-all focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)] ${
                                        childActive
                                          ? "border-[var(--gold-dark)] bg-[#faf4e6] text-[var(--gold-dark)] shadow-xs font-extrabold"
                                          : "border-[#dfd1b4]/70 bg-white/80 text-[#3e3730] hover:border-[var(--gold-dark)] hover:bg-white hover:text-[var(--gold-dark)]"
                                      }`}
                                    >
                                      <div className="flex items-center gap-2.5">
                                        {isCollection ? (
                                          <Sparkles size={14} className="text-[var(--gold-dark)] shrink-0" />
                                        ) : (
                                          <BookOpen size={14} className="text-[var(--gold-dark)] shrink-0" />
                                        )}
                                        <span>{child.label}</span>
                                      </div>
                                      <ArrowUpRight
                                        size={13}
                                        className="text-[#8c7f70] transition-colors group-hover:text-[var(--gold-dark)] shrink-0"
                                      />
                                    </Link>
                                  );
                                })}
                              </div>
                            )}
                          </motion.div>
                        ) : null}
                      </AnimatePresence>
                    </div>
                  );
                }

                return (
                  <Link
                    key={item.href}
                    href={item.href}
                    aria-current={active ? "page" : undefined}
                    onClick={() => setOpen(false)}
                    className={`flex min-h-11 items-center border-b border-[var(--line)] px-2 py-3 text-base font-semibold transition focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)] ${
                      active
                        ? "text-[var(--gold-dark)]"
                        : "text-[var(--ink)] hover:text-[var(--gold-dark)]"
                    }`}
                  >
                    {item.label}
                  </Link>
                );
              })}

              {/* Framer-styled BOOK LORNETTE button right beside Blog in mobile drawer */}
              <div className="pt-3 pb-1">
                <Link
                  href="/book"
                  onClick={() => setOpen(false)}
                  className="group flex w-full items-center justify-center gap-2 rounded-[1px] bg-[#c7a75e] py-3 text-xs font-bold uppercase tracking-[0.18em] text-[#171412] shadow-sm transition-colors hover:bg-[#d4b368] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)]"
                >
                  <span>BOOK LORNETTE</span>
                  <ArrowUpRight
                    size={15}
                    className="transition-transform duration-200 group-hover:translate-x-0.5 group-hover:-translate-y-0.5"
                    aria-hidden="true"
                  />
                </Link>
              </div>
            </div>
          </motion.div>
        ) : null}
      </AnimatePresence>
    </header>
  );
}
