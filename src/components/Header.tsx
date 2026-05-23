"use client";

import Image from "next/image";
import Link from "next/link";
import { Menu, X } from "lucide-react";
import { usePathname } from "next/navigation";
import { useState } from "react";

import { mainNav, siteCopy } from "@/content/site";

export function Header() {
  const [open, setOpen] = useState(false);
  const pathname = usePathname();

  return (
    <header className="sticky top-0 z-50 border-y border-[#dfd1b4] bg-[#fbf8f0]">
      <nav
        className="mx-auto flex h-[82px] max-w-7xl items-center justify-between px-5 sm:px-8 lg:justify-start lg:gap-16 lg:px-12 xl:gap-20"
        aria-label="Primary navigation"
      >
        <Link
          href="/"
          className="flex min-w-0 items-center gap-2 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[var(--gold-dark)]"
        >
          <Image
            src="/monogramlogo.png"
            alt="Lornette Daye LD monogram logo"
            width={122}
            height={71}
            unoptimized
            className="h-[64px] w-[110px] object-contain"
          />
          <span className="hidden h-9 w-px bg-[#d9c69e] sm:block" aria-hidden="true" />
          <span className="min-w-0">
            <span className="block font-serif text-xl leading-none tracking-[-0.01em] text-[#171412] sm:text-[1.35rem]">
              {siteCopy.brandName}
            </span>
            <span className="hidden text-[0.58rem] font-bold uppercase tracking-[0.26em] text-[#6f655a] sm:block">
              Speaker. Coach. Leader.
            </span>
          </span>
        </Link>

        <div className="hidden items-center gap-7 lg:flex xl:gap-8">
          {mainNav.slice(0, -1).map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className={`border-b-2 px-0 pb-4 pt-5 text-sm font-semibold leading-none transition hover:border-[#b28a39] hover:text-[#9b762e] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[var(--gold-dark)] ${
                pathname === item.href
                  ? "border-[#b28a39] text-[#9b762e]"
                  : "border-transparent text-[#2f2a25]"
              }`}
            >
              {item.label}
            </Link>
          ))}
        </div>

        <button
          type="button"
          data-mobile-menu-trigger
          className="inline-flex min-h-11 min-w-11 items-center justify-center border border-[#dfd1b4] text-[var(--ink)] lg:hidden"
          aria-expanded={open}
          aria-controls="mobile-menu"
          aria-label={open ? "Close navigation menu" : "Open navigation menu"}
          onClick={() => setOpen((value) => !value)}
        >
          {open ? <X size={22} aria-hidden="true" /> : <Menu size={22} aria-hidden="true" />}
        </button>
      </nav>

      {open ? (
        <div
          id="mobile-menu"
          data-mobile-menu
          className="border-t border-[#dfd1b4] bg-[#fbf8f0] px-4 pb-5 lg:hidden"
        >
          <div className="mx-auto grid max-w-7xl gap-1 py-4">
            {mainNav.map((item) => (
              <Link
                key={item.href}
                href={item.href}
                onClick={() => setOpen(false)}
                className="min-h-11 border-b border-[var(--line)] px-2 py-3 text-base font-semibold text-[var(--ink)]"
              >
                {item.label}
              </Link>
            ))}
          </div>
        </div>
      ) : null}
    </header>
  );
}
