import Image from "next/image";
import { Sparkles, ArrowDown } from "lucide-react";

import { collectionMeta } from "@/content/products";
import { CTAButton } from "@/components/CTAButton";

export function CollectionHero() {
  return (
    <section className="relative overflow-hidden border-b border-[var(--line)] bg-gradient-to-b from-white via-[var(--ivory)] to-[#f3ece0]/60 px-4 pt-12 pb-16 sm:px-6 sm:pt-16 sm:pb-20 lg:px-8 lg:pt-20 lg:pb-24">
      {/* Subtle decorative gold ambient glow */}
      <div
        className="pointer-events-none absolute -top-24 left-1/2 -translate-x-1/2 h-96 w-[48rem] max-w-full rounded-full bg-[radial-gradient(circle,rgba(198,165,92,0.18)_0%,transparent_70%)] blur-3xl"
        aria-hidden="true"
      />

      <div className="relative mx-auto max-w-7xl">
        <div className="grid items-center gap-12 lg:grid-cols-[1.1fr_0.9fr] lg:gap-16">
          {/* Text Content */}
          <div className="flex flex-col items-start text-left">
            <div className="inline-flex items-center gap-2 rounded-full border border-[rgba(198,165,92,0.45)] bg-[rgba(250,247,240,0.85)] px-3.5 py-1.5 backdrop-blur-sm">
              <Sparkles className="h-3.5 w-3.5 text-[var(--gold-dark)]" aria-hidden="true" />
              <span className="text-xs font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)]">
                {collectionMeta.eyebrow}
              </span>
            </div>

            <h1 className="mt-6 font-serif text-4xl font-normal tracking-tight text-[var(--ink)] sm:text-5xl lg:text-6xl">
              {collectionMeta.title}
            </h1>

            <p className="mt-2 text-lg font-medium italic tracking-wide text-[var(--gold-dark)] sm:text-xl">
              {collectionMeta.signature}
            </p>

            <p className="mt-6 max-w-xl text-base leading-relaxed text-[#5c5246] sm:text-lg">
              {collectionMeta.supportingCopy}
            </p>

            <div className="mt-8 flex flex-wrap items-center gap-4 sm:mt-10">
              <CTAButton href="#categories" variant="dark" className="group">
                <span>{collectionMeta.primaryCtaText}</span>
                <ArrowDown className="ml-2 h-4 w-4 transition-transform group-hover:translate-y-0.5" aria-hidden="true" />
              </CTAButton>

              <CTAButton href="#interest-list" variant="secondary">
                {collectionMeta.secondaryCtaText}
              </CTAButton>
            </div>

            <div className="mt-8 flex items-center gap-6 border-t border-[rgba(198,165,92,0.3)] pt-6 text-xs text-[#7d7164]">
              <span className="flex items-center gap-1.5">
                <span className="h-1.5 w-1.5 rounded-full bg-[var(--champagne)]" />
                72 Curated Product Formulations
              </span>
              <span className="flex items-center gap-1.5">
                <span className="h-1.5 w-1.5 rounded-full bg-[var(--champagne)]" />
                Pure Botanical Essentials
              </span>
            </div>
          </div>

          {/* Editorial Visual Composition */}
          <div className="relative mx-auto w-full max-w-lg lg:max-w-none">
            <div className="relative aspect-square w-full overflow-hidden rounded-2xl border border-[rgba(198,165,92,0.35)] bg-white p-3 shadow-[0_20px_50px_rgba(42,37,32,0.08)] sm:p-4">
              <div className="relative h-full w-full overflow-hidden rounded-xl bg-[#fdfbf7]">
                <Image
                  src={collectionMeta.heroImage}
                  alt="Featured UMATTR Crown Care product curated by Lornette Daye"
                  fill
                  priority
                  unoptimized
                  sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 540px"
                  className="object-contain p-6 transition-transform duration-700 hover:scale-105"
                />

                {/* Floating Editorial Badge */}
                <div className="absolute top-4 right-4 rounded-lg border border-[rgba(198,165,92,0.4)] bg-white/90 px-3 py-1.5 text-xs font-semibold tracking-wider text-[var(--ink)] shadow-sm backdrop-blur-md">
                  UMATTR™ Edition
                </div>

                <div className="absolute bottom-4 left-4 right-4 rounded-xl border border-[rgba(198,165,92,0.25)] bg-[rgba(250,247,240,0.92)] p-3 shadow-md backdrop-blur-md">
                  <p className="text-xs font-bold uppercase tracking-wider text-[var(--gold-dark)]">
                    Exclusive Preview
                  </p>
                  <p className="text-sm font-serif font-medium text-[var(--ink)]">
                    Signature Beauty, Crown Care & Holistic Wellness
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
