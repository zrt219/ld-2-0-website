import Link from "next/link";
import {
  ArrowRight,
  BookOpen,
  Compass,
  Home,
  Mail,
  Mic2,
  Sparkles,
  Target,
} from "lucide-react";

import { CTAButton } from "@/components/CTAButton";
import { PageShell } from "@/components/PageShell";

const pathways = [
  {
    title: "Keynote Speaking",
    tagline: "Inspiring & Transformational",
    description:
      "Keynote sessions on resilience, navigating pressure, and lessons learned from four decades in elite athletics.",
    href: "/speaking",
    icon: Mic2,
  },
  {
    title: "Official Book Catalog",
    tagline: "Practical Wisdom & Guides",
    description:
      "Digital editions including Survival Skills for Men, Finish Strong, Surviving Life, and UMATTR Devotional.",
    href: "/books",
    icon: BookOpen,
  },
  {
    title: "Lornette's Foundation: Golf",
    tagline: "Athlete Development Program",
    description:
      "10-Week Guided Athlete Development Program powered by the Performance Edge Framework for competitive players.",
    href: "/foundations",
    icon: Target,
  },
  {
    title: "Executive & Youth Inquiries",
    tagline: "Connect & Book",
    description:
      "Explore executive coaching, youth development initiatives, awards, or direct event booking inquiries.",
    href: "/contact",
    icon: Mail,
  },
];

export default function NotFound() {
  return (
    <PageShell>
      <main className="relative min-h-[calc(100vh-94px)] overflow-hidden bg-[var(--ivory)] px-4 py-16 sm:px-6 sm:py-24 lg:px-8">
        {/* Background luxury subtle radial glow */}
        <div
          aria-hidden="true"
          className="pointer-events-none absolute inset-0 bg-[radial-gradient(circle_at_top,_rgba(198,165,92,0.18)_0%,_rgba(250,247,240,0)_60%)]"
        />

        <div className="relative mx-auto max-w-5xl">
          {/* Top Hero Section */}
          <div className="text-center">
            <div className="inline-flex items-center gap-2 rounded-full border border-[rgba(198,165,92,0.45)] bg-[rgba(198,165,92,0.12)] px-4 py-1.5 text-xs font-bold uppercase tracking-[0.24em] text-[var(--gold-dark)] backdrop-blur-sm">
              <Compass className="h-3.5 w-3.5 text-[var(--champagne)]" aria-hidden="true" />
              <span>Error 404 · Page Not Found</span>
            </div>

            <h1 className="mt-6 font-serif text-4xl font-normal tracking-tight text-[var(--ink)] sm:text-5xl lg:text-6xl">
              A Moment to Reset <br className="hidden sm:inline" />
              and Recalibrate
            </h1>

            <p className="mx-auto mt-5 max-w-2xl text-base text-[var(--charcoal)] sm:text-lg">
              The page or resource you are looking for may have moved, been updated, or is no longer at this address. Let us guide you back to the right path.
            </p>
          </div>

          {/* Coach Lornette Quote Plaque */}
          <div className="mx-auto mt-10 max-w-3xl overflow-hidden rounded-2xl border border-[rgba(198,165,92,0.35)] bg-[rgba(23,20,18,0.94)] p-6 shadow-2xl backdrop-blur-md sm:p-8">
            <div className="flex flex-col items-center text-center">
              <div className="flex items-center gap-2 text-[11px] font-bold uppercase tracking-[0.24em] text-[var(--champagne)]">
                <Sparkles className="h-3.5 w-3.5" aria-hidden="true" />
                <span>Coach Lornette Daye · Signature Principle</span>
              </div>
              <blockquote className="mt-3 font-serif text-xl italic text-[var(--ivory)] sm:text-2xl">
                &ldquo;Your previous shot cannot hit your next shot.&rdquo;
              </blockquote>
              <p className="mt-2 text-xs uppercase tracking-[0.18em] text-[var(--taupe)]">
                Better People · Better Players · Unshakable Focus
              </p>
            </div>
          </div>

          {/* Primary Action Buttons */}
          <div className="mt-10 flex flex-col items-center justify-center gap-4 sm:flex-row">
            <CTAButton href="/" size="large">
              RETURN TO HOMEPAGE
            </CTAButton>
            <CTAButton href="/contact" variant="secondary" size="large">
              CONTACT LORNETTE
            </CTAButton>
          </div>

          {/* Pathway Grid */}
          <div className="mt-16 sm:mt-20">
            <div className="mb-6 flex items-center justify-between border-b border-[rgba(198,165,92,0.25)] pb-4">
              <div>
                <h2 className="text-xs font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)]">
                  Explore The Lornette Daye Ecosystem
                </h2>
                <p className="mt-1 font-serif text-lg text-[var(--ink)]">
                  Select a destination to continue
                </p>
              </div>
              <Link
                href="/"
                className="hidden items-center gap-1.5 text-xs font-bold uppercase tracking-[0.16em] text-[var(--gold-dark)] hover:underline sm:inline-flex"
              >
                <Home className="h-3.5 w-3.5" aria-hidden="true" />
                <span>All Pages</span>
              </Link>
            </div>

            <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4">
              {pathways.map((pathway) => {
                const IconComponent = pathway.icon;
                return (
                  <Link
                    key={pathway.title}
                    href={pathway.href}
                    className="group relative flex flex-col justify-between rounded-xl border border-[rgba(198,165,92,0.3)] bg-white/70 p-6 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:border-[var(--champagne)] hover:bg-white hover:shadow-xl"
                  >
                    <div>
                      <div className="flex h-11 w-11 items-center justify-center rounded-lg border border-[rgba(198,165,92,0.3)] bg-[rgba(198,165,92,0.12)] text-[var(--gold-dark)] transition-colors group-hover:bg-[var(--champagne)] group-hover:text-[var(--ink)]">
                        <IconComponent className="h-5 w-5" aria-hidden="true" />
                      </div>
                      <p className="mt-4 text-[10px] font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)]">
                        {pathway.tagline}
                      </p>
                      <h3 className="mt-1 font-serif text-base font-medium text-[var(--ink)] group-hover:text-[var(--gold-dark)]">
                        {pathway.title}
                      </h3>
                      <p className="mt-2 text-xs leading-relaxed text-[var(--charcoal)]">
                        {pathway.description}
                      </p>
                    </div>

                    <div className="mt-6 flex items-center gap-1.5 text-xs font-bold uppercase tracking-[0.14em] text-[var(--gold-dark)] group-hover:text-[var(--ink)]">
                      <span>Explore</span>
                      <ArrowRight className="h-3.5 w-3.5 transition-transform duration-300 group-hover:translate-x-1" aria-hidden="true" />
                    </div>
                  </Link>
                );
              })}
            </div>
          </div>
        </div>
      </main>
    </PageShell>
  );
}
