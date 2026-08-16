"use client";

import Image from "next/image";
import Link from "next/link";
import { Menu, X } from "lucide-react";
import { usePathname } from "next/navigation";
import { useState } from "react";

import { images, mainNav, siteCopy } from "@/content/site";
import { CTAButton } from "./CTAButton";

export function Header() {
  const [open, setOpen] = useState(false);
  const pathname = usePathname();

  return (
    <header className="sticky top-0 z-50 border-b border-[rgba(198,165,92,0.32)] bg-[rgba(250,247,240,0.94)] backdrop-blur-xl">
      <nav
        className="mx-auto flex max-w-7xl items-center justify-between px-4 py-4 sm:px-6 lg:px-8"
        aria-label="Primary navigation"
      >
        <Link href="/" className="flex items-center gap-3">
          <Image
            src="/ld-signature-black.png"
            alt={images.signatureBlack.alt}
            width={92}
            height={44}
            unoptimized
            className="h-11 w-[5.5rem] object-cover object-center sm:w-[5.75rem]"
          />
          <span className="border-l border-[rgba(198,165,92,0.42)] pl-3">
            <span className="block font-serif text-[1.28rem] leading-none text-[var(--ink)]">
              {siteCopy.brandName}
            </span>
            <span className="hidden text-[0.58rem] font-bold uppercase tracking-[0.16em] text-[#7d7164] sm:block">
              Speaker. Coach. Leader.
            </span>
          </span>
        </Link>

        <div className="hidden items-center gap-1 xl:flex">
          {mainNav.slice(0, -1).map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className={`border-b-2 px-3 py-2 text-sm font-semibold transition hover:border-[var(--champagne)] hover:text-[var(--gold-dark)] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-4 focus-visible:outline-[var(--champagne)] ${
                pathname === item.href
                  ? "border-[var(--champagne)] text-[var(--gold-dark)]"
                  : "border-transparent text-[var(--charcoal)]"
              }`}
            >
              {item.label}
            </Link>
          ))}
        </div>

        <div className="hidden xl:block">
          <CTAButton href="/book" variant="dark">
            Book Lornette
          </CTAButton>
        </div>

        <button
          type="button"
          data-mobile-menu-trigger
          className="inline-flex min-h-11 min-w-11 items-center justify-center border border-[var(--line)] text-[var(--ink)] xl:hidden"
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
          className="border-t border-[var(--line)] bg-[var(--ivory)] px-4 pb-5 xl:hidden"
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
