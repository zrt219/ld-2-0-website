"use client";

import { useState } from "react";
import Image from "next/image";
import Link from "next/link";
import { motion, AnimatePresence } from "framer-motion";
import { ChevronLeft, ChevronRight, Sparkles, Target, ArrowRight } from "lucide-react";

export interface CorporateShowcaseSlide {
  id: string;
  badge: string;
  title: string;
  subtitle: string;
  description: string;
  image: string;
  imageAlt: string;
  objectPosition?: string;
  pillarNumber: string;
  keyMetric: string;
  keyMetricLabel: string;
}

export const corporateShowcaseSlides: CorporateShowcaseSlide[] = [
  {
    id: "boardroom-calm",
    badge: "EXECUTIVE PRESENCE & CLARITY",
    title: "The Strategic Boardroom",
    subtitle: "Commanding High-Stakes Decision Rooms with Emotional Poise",
    description:
      "Championship execution begins with leaders who remain grounded when timelines compress. Lornette Daye works directly with senior executives to cultivate steady somatic calm, non-reactive listening, and unshakeable authority.",
    image: "/foundations/corporate/lornette-executive-boardroom-dialogue.jpg",
    imageAlt: "Lornette Daye engaging corporate executive leaders in boardroom dialogue",
    objectPosition: "center 20%",
    pillarNumber: "01",
    keyMetric: "5-Second Reset",
    keyMetricLabel: "Cognitive protocol to eliminate rumination under pressure",
  },
  {
    id: "leadership-workshop",
    badge: "INTERACTIVE MASTERCLASS",
    title: "The Refined Leadership Workshop",
    subtitle: "Turning Athletic Pedagogy into Sustainable Corporate Habits",
    description:
      "Practical intensives where management teams deconstruct pressure patterns, establish daily execution routines, and build unified accountability systems that prevent burnout and elevate departmental trust.",
    image: "/foundations/corporate/lornette-executive-presentation-screen.jpg",
    imageAlt: "Lornette Daye presenting data and strategic leadership concepts in corporate session",
    objectPosition: "center 20%",
    pillarNumber: "02",
    keyMetric: "100% Alignment",
    keyMetricLabel: "Cross-departmental cohesion between sales, operations, and finance",
  },
  {
    id: "one-on-one-consultation",
    badge: "EXECUTIVE MENTORSHIP",
    title: "Strategic 1-on-1 Consultation",
    subtitle: "Personalized Composure Frameworks for Senior Decision-Makers",
    description:
      "Confidential advisory sessions focused on personal composure, cognitive load management, and decision-making clarity for C-suite leaders and dealership general managers carrying intense operational responsibility.",
    image: "/foundations/corporate/lornette-executive-one-on-one-consultation.jpg",
    imageAlt: "Lornette Daye in private strategic executive consultation in penthouse suite",
    objectPosition: "center 20%",
    pillarNumber: "03",
    keyMetric: "Individual Poise",
    keyMetricLabel: "Targeted emotional poise and executive decision frameworks",
  },
  {
    id: "keynote-assembly",
    badge: "KEYNOTE & ASSEMBLY STAGE",
    title: "Championship Keynote & Address",
    subtitle: "Inspirational Poise and Clear Perspective on the Grand Stage",
    description:
      "High performance demands intentional clarity and visionary inspiration. Lornette delivers resonant keynotes that elevate organizational morale, reframe setback into capacity, and align collective purpose.",
    image: "/foundations/corporate/lornette-executive-keynote-stage.jpg",
    imageAlt: "Lornette Daye delivering corporate keynote address to executive audience",
    objectPosition: "center 20%",
    pillarNumber: "04",
    keyMetric: "Energy Retention",
    keyMetricLabel: "Multi-decade Olympic energy frameworks replacing burnout cycles",
  },
];

export function CorporateExecutiveGallery() {
  const [activeIndex, setActiveIndex] = useState(0);
  const activeSlide = corporateShowcaseSlides[activeIndex];

  const handlePrev = () => {
    setActiveIndex((prev) => (prev === 0 ? corporateShowcaseSlides.length - 1 : prev - 1));
  };

  const handleNext = () => {
    setActiveIndex((prev) => (prev === corporateShowcaseSlides.length - 1 ? 0 : prev + 1));
  };

  return (
    <section className="border-t border-[var(--line)] bg-[linear-gradient(180deg,#fffdfa_0%,#f5eee1_100%)] px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
      <div className="mx-auto max-w-7xl">
        <div className="text-center max-w-3xl mx-auto">
          <div className="inline-flex items-center gap-2 border border-[rgba(198,165,92,0.48)] bg-white/80 px-3.5 py-1.5 shadow-xs mb-3">
            <Sparkles size={13} className="text-[var(--gold-dark)]" />
            <span className="text-[10.5px] font-bold uppercase tracking-[0.24em] text-[var(--gold-dark)]">
              EXECUTIVE SPACES &amp; PRACTICES
            </span>
          </div>
          <h2 className="mt-2 font-serif text-3xl sm:text-5xl text-[var(--ink)] leading-tight">
            The Architecture of Executive Composure
          </h2>
          <p className="mt-4 text-base sm:text-lg leading-relaxed text-[#554b40]">
            Explore the high-trust environments, disciplined daily spaces, and somatic practices where Lornette Daye develops organizational resilience.
          </p>
        </div>

        <div className="mt-14 grid grid-cols-1 lg:grid-cols-12 gap-8 items-stretch">
          {/* Main Visual Display (7 cols) */}
          <div className="lg:col-span-7 flex flex-col justify-between">
            <div className="relative aspect-[16/10] w-full overflow-hidden rounded-[2px] border border-[rgba(198,165,92,0.45)] bg-[#120f0d] shadow-[0_24px_70px_rgba(23,20,18,0.18)]">
              <AnimatePresence mode="wait">
                <motion.div
                  key={activeSlide.id}
                  initial={{ opacity: 0, scale: 1.04 }}
                  animate={{ opacity: 1, scale: 1 }}
                  exit={{ opacity: 0, scale: 0.98 }}
                  transition={{ duration: 0.6, ease: [0.22, 1, 0.36, 1] }}
                  className="absolute inset-0"
                >
                  <Image
                    src={activeSlide.image}
                    alt={activeSlide.imageAlt}
                    fill
                    sizes="(max-width: 1024px) 100vw, 58vw"
                    className="object-cover"
                    style={{ objectPosition: activeSlide.objectPosition || "center 20%" }}
                    priority
                  />
                </motion.div>
              </AnimatePresence>

              {/* Atmosphere Overlay */}
              <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-black/85 via-black/25 to-transparent" />
              <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/10" />

              {/* Docked Luxury Editorial Plaque */}
              <div className="absolute inset-x-0 bottom-0 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(18,15,13,0.85)] p-4 sm:p-5 backdrop-blur-md shadow-2xl">
                <div className="flex items-center justify-between gap-4">
                  <div>
                    <p className="text-[10px] sm:text-[11px] font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
                      {activeSlide.badge}
                    </p>
                    <p className="mt-0.5 font-serif text-base sm:text-xl text-white leading-snug">
                      {activeSlide.title}
                    </p>
                  </div>
                  <div className="shrink-0 flex items-center gap-1.5">
                    <button
                      type="button"
                      onClick={handlePrev}
                      aria-label="Previous corporate space"
                      className="flex h-9 w-9 items-center justify-center rounded-[2px] border border-white/20 bg-white/10 text-white transition hover:bg-white/25 hover:border-[var(--champagne)] cursor-pointer"
                    >
                      <ChevronLeft size={16} />
                    </button>
                    <button
                      type="button"
                      onClick={handleNext}
                      aria-label="Next corporate space"
                      className="flex h-9 w-9 items-center justify-center rounded-[2px] border border-white/20 bg-white/10 text-white transition hover:bg-white/25 hover:border-[var(--champagne)] cursor-pointer"
                    >
                      <ChevronRight size={16} />
                    </button>
                  </div>
                </div>
              </div>
            </div>

            {/* Thumbnail Strip */}
            <div className="mt-4 grid grid-cols-4 gap-2 sm:gap-3">
              {corporateShowcaseSlides.map((slide, idx) => {
                const isActive = idx === activeIndex;
                return (
                  <button
                    key={slide.id}
                    type="button"
                    onClick={() => setActiveIndex(idx)}
                    aria-label={`Select ${slide.title}`}
                    className={`group relative aspect-[16/10] w-full overflow-hidden rounded-[2px] border transition-all duration-300 cursor-pointer ${
                      isActive
                        ? "border-[var(--gold-dark)] ring-2 ring-[var(--gold-dark)] shadow-md"
                        : "border-[rgba(198,165,92,0.3)] opacity-70 hover:opacity-100 hover:border-[var(--champagne)]"
                    }`}
                  >
                    <Image
                      src={slide.image}
                      alt={slide.title}
                      fill
                      sizes="25vw"
                      className="object-cover"
                    />
                    <div
                      className={`absolute inset-0 transition-opacity ${
                        isActive ? "bg-black/10" : "bg-black/35 group-hover:bg-black/15"
                      }`}
                    />
                    <div className="absolute bottom-1 left-1.5 text-[9px] font-bold text-white uppercase tracking-wider drop-shadow-sm hidden sm:block">
                      0{idx + 1}
                    </div>
                  </button>
                );
              })}
            </div>
          </div>

          {/* Editorial Content Card (5 cols) */}
          <div className="lg:col-span-5 flex flex-col justify-between rounded-[2px] border border-[rgba(198,165,92,0.38)] bg-white p-6 sm:p-8 shadow-[0_18px_50px_rgba(30,24,15,0.08)]">
            <AnimatePresence mode="wait">
              <motion.div
                key={activeSlide.id}
                initial={{ opacity: 0, y: 12 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -10 }}
                transition={{ duration: 0.35 }}
                className="flex flex-col justify-between h-full"
              >
                <div>
                  <div className="flex items-center justify-between border-b border-[var(--line)] pb-4">
                    <div className="flex items-center gap-2">
                      <span className="inline-flex h-6 w-6 items-center justify-center rounded-full bg-[var(--gold-dark)] text-[10px] font-bold text-white">
                        {activeSlide.pillarNumber}
                      </span>
                      <span className="text-xs font-bold uppercase tracking-[0.2em] text-[#6e6355]">
                        Executive Practice {activeSlide.pillarNumber} of 04
                      </span>
                    </div>
                    <Target size={15} className="text-[var(--gold-dark)]" />
                  </div>

                  <h3 className="mt-5 font-serif text-2xl sm:text-3xl text-[var(--ink)] leading-snug">
                    {activeSlide.title}
                  </h3>
                  <p className="mt-1 font-serif text-sm italic text-[var(--gold-dark)]">
                    {activeSlide.subtitle}
                  </p>

                  <p className="mt-4 text-xs sm:text-sm leading-relaxed text-[#554b40]">
                    {activeSlide.description}
                  </p>

                  <div className="mt-6 rounded-sm border border-[rgba(198,165,92,0.28)] bg-[var(--sand)]/25 p-4">
                    <p className="text-[10px] font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)]">
                      COMMERCIAL PERFORMANCE BENCHMARK
                    </p>
                    <p className="mt-1 font-serif text-base font-bold text-[var(--ink)]">
                      {activeSlide.keyMetric}
                    </p>
                    <p className="mt-0.5 text-xs text-[#6e6255] leading-relaxed">
                      {activeSlide.keyMetricLabel}
                    </p>
                  </div>
                </div>

                <div className="mt-8 pt-6 border-t border-[var(--line)] flex flex-wrap gap-3">
                  <Link
                    href="/book"
                    className="inline-flex items-center gap-1.5 rounded-[2px] bg-[var(--gold-dark)] px-4 py-2.5 text-xs font-bold uppercase tracking-[0.16em] text-white transition hover:bg-[#8f6d2b]"
                  >
                    <span>Schedule Executive Briefing</span>
                    <ArrowRight size={13} />
                  </Link>
                  <Link
                    href="/leadership"
                    className="inline-flex items-center gap-1.5 rounded-[2px] border border-[rgba(198,165,92,0.5)] px-4 py-2.5 text-xs font-bold uppercase tracking-[0.16em] text-[var(--gold-dark)] transition hover:bg-[var(--sand)]/30"
                  >
                    <span>Leadership Pillars</span>
                  </Link>
                </div>
              </motion.div>
            </AnimatePresence>
          </div>
        </div>
      </div>
    </section>
  );
}
