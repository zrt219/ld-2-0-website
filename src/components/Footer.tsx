import Link from "next/link";
import { Mail } from "lucide-react";

import { mainNav, siteCopy } from "@/content/site";
import { CTAButton } from "./CTAButton";

export function Footer() {
  return (
    <footer className="bg-[var(--ink)] text-[var(--ivory)]">
      <div className="mx-auto grid max-w-7xl gap-10 px-4 py-14 sm:px-6 lg:grid-cols-[1.1fr_0.9fr] lg:px-8">
        <div>
          <p className="font-serif text-4xl">{siteCopy.brandName}</p>
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
              {mainNav.map((item) => (
                <Link
                  key={item.href}
                  href={item.href}
                  className="text-sm text-[#d8cdbb] transition hover:text-white"
                >
                  {item.label}
                </Link>
              ))}
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
              {siteCopy.socialLinks.map((link) => (
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
