import Image from "next/image";
import Link from "next/link";
import { Mail } from "lucide-react";

import { siteCopy } from "@/content/site";
import { CTAButton } from "./CTAButton";

export function Footer() {
  return (
    <footer className="bg-[var(--ink)] text-[var(--ivory)]">
      <div className="mx-auto grid max-w-7xl gap-10 px-4 py-14 sm:px-6 lg:grid-cols-[1.1fr_0.9fr] lg:px-8">
        <div>
          <div className="flex items-center gap-3.5">
            <div className="relative h-12 w-12 shrink-0 overflow-hidden rounded-lg border border-[rgba(198,165,92,0.45)] bg-[#1e1915] shadow-md">
              <Image
                src="/monogramlogo.png"
                alt="Lornette Daye Official Logo"
                fill
                sizes="48px"
                className="object-contain p-1"
                unoptimized
              />
            </div>
            <div>
              <p className="font-serif text-3xl sm:text-4xl text-white">{siteCopy.brandName}</p>
              <p className="text-[11px] font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
                Speaker · Coach · Leader
              </p>
            </div>
          </div>
          <p className="mt-5 max-w-2xl text-sm leading-7 text-[#d8cdbb]">
            Professional keynote speaking, leadership development, inclusion,
            mentorship, youth development, and athlete performance coaching.
          </p>
          <div className="mt-7 flex flex-wrap gap-3">
            <CTAButton href="/book">Inquire About Availability</CTAButton>
            <CTAButton
              href="/speaker-kit"
              variant="secondary"
              className="border-[#d8b96e] text-[var(--ivory)] hover:bg-white/10"
            >
              View Speaker Kit
            </CTAButton>
          </div>
        </div>
        <div className="grid gap-8 sm:grid-cols-2">
          <div>
            <h2 className="text-sm font-bold uppercase text-[var(--champagne)]">
              Quick Links
            </h2>
            <div className="mt-4 grid gap-2">
              <Link href="/" className="text-sm text-[#d8cdbb] transition hover:text-white">
                Home
              </Link>
              <Link href="/speaking" className="text-sm text-[#d8cdbb] transition hover:text-white">
                Speaker
              </Link>
              <Link href="/foundations" className="text-sm text-[#d8cdbb] transition hover:text-white">
                Foundations
              </Link>
              <Link href="/foundations/login" className="text-sm text-[#dfcca6] font-semibold transition hover:text-white">
                Athlete &amp; Coach Portal
              </Link>
              <Link href="/leadership" className="text-sm text-[#d8cdbb] transition hover:text-white">
                Leadership
              </Link>
              <Link href="/mentorship" className="text-sm text-[#d8cdbb] transition hover:text-white">
                Mentorship
              </Link>
              <Link href="/books" className="text-sm text-[#d8cdbb] transition hover:text-white">
                Books
              </Link>
              <Link href="/collection" className="text-sm text-[#d8cdbb] transition hover:text-white">
                Collection
              </Link>
              <Link href="/about" className="text-sm text-[#d8cdbb] transition hover:text-white">
                About
              </Link>
              <Link href="/media" className="text-sm text-[#d8cdbb] transition hover:text-white">
                Media
              </Link>
              <Link href="/blog" className="text-sm text-[#d8cdbb] transition hover:text-white">
                Blog
              </Link>
              <Link href="/book" className="text-sm text-[#d8cdbb] transition hover:text-white">
                Book Lornette
              </Link>
            </div>
          </div>
          <div>
            <h2 className="text-sm font-bold uppercase text-[var(--champagne)]">
              Let&apos;s Connect
            </h2>
            <div className="mt-4 grid gap-3 text-sm text-[#d8cdbb]">
              <a href={`mailto:${siteCopy.contactEmail}`} className="inline-flex items-center gap-2 hover:text-white">
                <Mail size={16} aria-hidden="true" />
                {siteCopy.contactEmail}
              </a>
            </div>
            <div className="mt-5 grid gap-2">
              {siteCopy.socialLinks
                .filter((link) => link.label.toLowerCase() !== "email")
                .map((link) => (
                  <a
                    key={link.label}
                    href={link.href}
                    className="text-sm text-[#d8cdbb] transition hover:text-white"
                  >
                    {link.label}
                  </a>
                ))}
            </div>
          </div>
        </div>
      </div>
      <div className="border-t border-white/10 px-4 py-5 text-center text-xs text-[#b9ad9a]">
        &copy; 2026 Lornette Daye. All rights reserved.
      </div>
    </footer>
  );
}
