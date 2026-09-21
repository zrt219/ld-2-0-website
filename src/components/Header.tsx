"use client";

import Image from "next/image";
import Link from "next/link";
import { ChevronDown, Menu, X } from "lucide-react";
import { usePathname } from "next/navigation";
import { useState, useRef, useEffect, useSyncExternalStore } from "react";
import { motion, AnimatePresence } from "framer-motion";

import { mainNav, siteCopy, type NavItem } from "@/content/site";

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
      if (
        dropdownContainerRef.current &&
        !dropdownContainerRef.current.contains(e.target as Node)
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
        className="mx-auto flex h-[94px] max-w-7xl items-center justify-between px-5 sm:px-8 lg:justify-start lg:gap-8 lg:px-8 xl:gap-14 xl:px-12"
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
          className="hidden h-full items-center gap-5 lg:flex xl:gap-7 list-none m-0 p-0"
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
                    if (!e.currentTarget.contains(e.relatedTarget as Node)) {
                      setActiveDropdown((curr) => (curr === item.label ? null : curr));
                    }
                  }}
                >
                  <div className="relative flex items-center">
                    {/* Standard Text Link */}
                    <Link
                      href={item.href}
                      aria-current={active ? "page" : undefined}
                      className={`border-b-2 px-0 pb-4 pt-5 text-sm font-semibold leading-none transition hover:border-[var(--gold-dark)] hover:text-[var(--gold-dark)] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[var(--gold-dark)] ${
                        active
                          ? "border-[var(--gold-dark)] text-[var(--gold-dark)]"
                          : "border-transparent text-[#2f2a25]"
                      }`}
                    >
                      {item.label}
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
                      className="ml-1.5 flex h-6 w-6 items-center justify-center text-[#6f655a] transition-colors hover:text-[var(--gold-dark)] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-1 focus-visible:outline-[var(--gold-dark)]"
                    >
                      <ChevronDown
                        size={13}
                        aria-hidden="true"
                        className={`transition-transform duration-200 ${
                          isOpen ? "rotate-180 text-[var(--gold-dark)]" : "text-[#6f655a]"
                        }`}
                      />
                    </button>

                    {/* Refined Editorial Disclosure Flyout */}
                    <AnimatePresence>
                      {isOpen ? (
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
                  className={`border-b-2 px-0 pb-4 pt-5 text-sm font-semibold leading-none transition hover:border-[var(--gold-dark)] hover:text-[var(--gold-dark)] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[var(--gold-dark)] ${
                    active
                      ? "border-[var(--gold-dark)] text-[var(--gold-dark)]"
                      : "border-transparent text-[#2f2a25]"
                  }`}
                >
                  {item.label}
                </Link>
              </li>
            );
          })}
        </ul>

        {/* Mobile menu trigger */}
        <button
          ref={mobileMenuButtonRef}
          type="button"
          data-mobile-menu-trigger
          className="inline-flex min-h-11 min-w-11 items-center justify-center border border-[#dfd1b4] text-[var(--ink)] lg:hidden cursor-pointer focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)]"
          aria-expanded={open}
          aria-controls="mobile-menu"
          aria-label={open ? "Close navigation menu" : "Open navigation menu"}
          onClick={() => setOpen((value) => !value)}
        >
          {open ? <X size={22} aria-hidden="true" /> : <Menu size={22} aria-hidden="true" />}
        </button>
      </nav>

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
            className="overflow-hidden border-t border-[#dfd1b4] bg-[#fbf8f0] lg:hidden"
          >
            <div className="mx-auto grid max-w-7xl gap-1 px-4 pb-6 pt-4">
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
                            className="overflow-hidden bg-[rgba(245,239,228,0.5)] pl-4 pr-2"
                          >
                            <div className="grid gap-1 py-1">
                              {item.children?.map((child) => {
                                const childActive = isChildActive(child.href);
                                return (
                                  <Link
                                    key={child.href}
                                    href={child.href}
                                    aria-current={childActive ? "page" : undefined}
                                    onClick={() => setOpen(false)}
                                    className={`flex min-h-11 items-center border-b border-[var(--line)]/50 px-3 py-2 text-sm font-medium transition focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)] ${
                                      childActive
                                        ? "font-semibold text-[var(--gold-dark)]"
                                        : "text-[#3e3730] hover:text-[var(--gold-dark)]"
                                    }`}
                                  >
                                    {child.label}
                                  </Link>
                                );
                              })}
                            </div>
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
            </div>
          </motion.div>
        ) : null}
      </AnimatePresence>
    </header>
  );
}
