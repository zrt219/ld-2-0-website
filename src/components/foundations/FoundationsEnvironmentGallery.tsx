"use client";

import { useState } from "react";
import Image from "next/image";
import Link from "next/link";
import { motion, AnimatePresence } from "framer-motion";
import { ChevronLeft, ChevronRight, ArrowRight, Sparkles } from "lucide-react";

export interface GalleryEnvironment {
  id: string;
  title: string;
  subtitle: string;
  pillar: string;
  pillarNumber: string;
  quote: string;
  application: string;
  imageSrc: string;
  imageAlt: string;
  objectPosition?: string;
}

export const galleryEnvironments: GalleryEnvironment[] = [
  {
    id: "atrium-preparation",
    title: "The Training Facility Atrium",
    subtitle: "High-Performance Atmosphere",
    pillar: "Discipline Systems & Routine",
    pillarNumber: "03",
    quote:
      "Preparation is where composure is forged. Championship execution begins long before entering the competition arena.",
    application:
      "Daily training cadences that turn erratic effort into structured, repeatable athletic habits.",
    imageSrc: "/foundations/football-film-room-strategy-session.jpg",
    imageAlt:
      "Coach and football players analyzing game tape and strategy on large screen in film room",
    objectPosition: "center center",
  },
  {
    id: "concentric-focus",
    title: "The Architectural Track Pavilion",
    subtitle: "Geometry of Mental Focus",
    pillar: "Champion Mindset & Attention",
    pillarNumber: "02",
    quote:
      "Your internal focus must remain as clear as the lane in front of you. When you master your attention, external pressure dissolves.",
    application:
      "Deploying the Attention Dial tool to narrow mental focus onto immediate execution cues.",
    imageSrc: "/foundations/track-sprinter-starting-blocks.jpg",
    imageAlt:
      "Focused sprinter in starting blocks on running track at golden sunset",
    objectPosition: "center 40%",
  },
  {
    id: "stadium-sunset",
    title: "Championship Stadium Sunset",
    subtitle: "Poise Under Crunch-Time Pressure",
    pillar: "Pressure, Emotional Regulation & Recovery",
    pillarNumber: "05",
    quote:
      "The stadium lights will test your composure. When the noise rises, your breath and somatic routines keep you centered.",
    application:
      "Physiological reset protocols to regulate nervous tension during critical competition moments.",
    imageSrc: "/foundations/golfer-fairway-course-focus.jpg",
    imageAlt:
      "Golfer holding club assessing the fairway and green through trees with poise and focus",
    objectPosition: "center center",
  },
  {
    id: "golden-dawn",
    title: "Golden Dawn Field",
    subtitle: "Foundational Identity & Purpose",
    pillar: "Identity Beyond Sport",
    pillarNumber: "01",
    quote:
      "'Athlete' is only one part of the story. We are students, parents, professionals, and builders with complex needs and endless potential.",
    application:
      "Separating personal self-worth from athletic scoreboards to cultivate unshakeable confidence.",
    imageSrc: "/foundations/student-lecture-exam-focus.jpg",
    imageAlt:
      "Dedicated university student writing an exam in a lecture hall with calm concentration",
    objectPosition: "center center",
  },
  {
    id: "tunnel-execution",
    title: "The Tunnel of Execution",
    subtitle: "Stepping into the Competitive Arena",
    pillar: "Resilience After Setback & Reset",
    pillarNumber: "04",
    quote:
      "Between preparation and the podium lies the tunnel. Breathe, step forward with intention, and trust your training.",
    application:
      "The 5-Second Reset routine to release previous mistakes and focus 100% on the immediate next action.",
    imageSrc: "/foundations/lornette-foundations-stadium-tunnel.png",
    imageAlt:
      "Lornette Daye striding forward through illuminated modern architectural arena tunnel",
    objectPosition: "center center",
  },
];

export function FoundationsEnvironmentGallery() {
  const [activeIndex, setActiveIndex] = useState(0);
  const activeItem = galleryEnvironments[activeIndex];

  const handlePrev = () => {
    setActiveIndex((prev) => (prev === 0 ? galleryEnvironments.length - 1 : prev - 1));
  };

  const handleNext = () => {
    setActiveIndex((prev) => (prev === galleryEnvironments.length - 1 ? 0 : prev + 1));
  };

  return (
    <section
      id="environments"
      className="border-t border-[var(--line)] bg-[linear-gradient(180deg,#fcfaf5_0%,#f6f0e3_100%)] px-4 py-16 sm:px-6 lg:px-8 lg:py-24 scroll-mt-24"
    >
      <div className="mx-auto max-w-7xl">
        {/* Section Header */}
        <div className="max-w-3xl">
          <div className="inline-flex items-center gap-2 rounded-[2px] border border-[rgba(198,165,92,0.35)] bg-white/70 px-3 py-1 shadow-xs backdrop-blur-xs">
            <Sparkles size={13} className="text-[var(--gold-dark)]" aria-hidden="true" />
            <span className="text-[11px] font-extrabold uppercase tracking-[0.24em] text-[var(--gold-dark)]">
              HIGH-PERFORMANCE ENVIRONMENTS
            </span>
          </div>
          <h2 className="mt-4 font-serif text-3xl sm:text-4xl lg:text-5xl text-[var(--ink)] leading-tight">
            The Standard in Motion
          </h2>
          <p className="mt-3 text-base sm:text-lg leading-relaxed text-[#675d50]">
            Explore the high-performance spaces and foundational principles where Lornette Daye shapes athletic composure, daily discipline, and championship readiness.
          </p>
        </div>

        {/* Interactive Gallery Stage & Info Card */}
        <div className="mt-10 grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          {/* Main Visual Stage (7 cols on lg) */}
          <div className="lg:col-span-7 flex flex-col">
            <div className="relative aspect-[16/10] sm:aspect-[16/9] w-full overflow-hidden rounded-[2px] border border-[rgba(198,165,92,0.45)] bg-[#120f0d] shadow-[0_20px_50px_rgba(23,20,18,0.12)]">
              <AnimatePresence mode="wait">
                <motion.div
                  key={activeItem.id}
                  initial={{ opacity: 0, scale: 1.03 }}
                  animate={{ opacity: 1, scale: 1 }}
                  exit={{ opacity: 0, scale: 0.98 }}
                  transition={{ duration: 0.55, ease: [0.22, 1, 0.36, 1] }}
                  className="absolute inset-0"
                >
                  <Image
                    src={activeItem.imageSrc}
                    alt={activeItem.imageAlt}
                    fill
                    priority
                    unoptimized
                    sizes="(max-width: 1024px) 100vw, 60vw"
                    className="object-cover"
                    style={{ objectPosition: activeItem.objectPosition || "center" }}
                  />
                </motion.div>
              </AnimatePresence>

              {/* Cinematic Vignette */}
              <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-black/75 via-transparent to-black/20" />
              <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/10" />

              {/* Docked Luxury Editorial Plaque */}
              <div className="absolute inset-x-0 bottom-0 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(18,15,13,0.85)] p-4 sm:p-5 backdrop-blur-md shadow-2xl">
                <div className="flex items-center justify-between gap-4">
                  <div>
                    <p className="font-serif text-base sm:text-xl text-white leading-snug">
                      {activeItem.pillar}
                    </p>
                  </div>
                  <div className="shrink-0 flex items-center gap-1.5">
                    <button
                      type="button"
                      onClick={handlePrev}
                      aria-label="Previous environment"
                      className="flex h-9 w-9 items-center justify-center rounded-[2px] border border-white/20 bg-white/10 text-white transition hover:bg-white/25 hover:border-[var(--champagne)] cursor-pointer"
                    >
                      <ChevronLeft size={16} />
                    </button>
                    <button
                      type="button"
                      onClick={handleNext}
                      aria-label="Next environment"
                      className="flex h-9 w-9 items-center justify-center rounded-[2px] border border-white/20 bg-white/10 text-white transition hover:bg-white/25 hover:border-[var(--champagne)] cursor-pointer"
                    >
                      <ChevronRight size={16} />
                    </button>
                  </div>
                </div>
              </div>
            </div>

            {/* Clickable Thumbnail Strip */}
            <div className="mt-4 grid grid-cols-5 gap-2 sm:gap-3">
              {galleryEnvironments.map((env, index) => {
                const isActive = index === activeIndex;
                return (
                  <button
                    key={env.id}
                    type="button"
                    onClick={() => setActiveIndex(index)}
                    aria-label={`Select ${env.title}`}
                    className={`group relative aspect-[16/10] w-full overflow-hidden rounded-[2px] border transition-all duration-300 cursor-pointer ${
                      isActive
                        ? "border-[var(--gold-dark)] ring-2 ring-[var(--gold-dark)] shadow-md"
                        : "border-[rgba(198,165,92,0.3)] opacity-70 hover:opacity-100 hover:border-[var(--champagne)]"
                    }`}
                  >
                    <Image
                      src={env.imageSrc}
                      alt={env.title}
                      fill
                      unoptimized
                      sizes="20vw"
                      className="object-cover"
                    />
                    <div
                      className={`absolute inset-0 transition-opacity ${
                        isActive ? "bg-black/10" : "bg-black/35 group-hover:bg-black/15"
                      }`}
                    />
                    <div className="absolute bottom-1 left-1.5 text-[9px] font-bold text-white uppercase tracking-wider drop-shadow-sm hidden sm:block">
                      0{index + 1}
                    </div>
                  </button>
                );
              })}
            </div>
          </div>

          {/* Docked Editorial Info Card (5 cols on lg) */}
          <div className="lg:col-span-5 rounded-[2px] border border-[rgba(198,165,92,0.38)] bg-white p-6 sm:p-8 shadow-[0_16px_40px_rgba(30,24,15,0.08)]">
            <AnimatePresence mode="wait">
              <motion.div
                key={activeItem.id}
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -10 }}
                transition={{ duration: 0.35, ease: [0.22, 1, 0.36, 1] }}
                className="flex flex-col"
              >
                <div>
                  {/* Pillar Counter Header */}
                  <div className="flex items-center justify-between border-b border-[var(--line)] pb-4">
                    <div className="flex items-center gap-2">
                      <span className="inline-flex h-6 w-6 items-center justify-center rounded-full bg-[var(--gold-dark)] text-[10px] font-bold text-white">
                        {activeItem.pillarNumber}
                      </span>
                      <span className="text-[11px] font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)]">
                        FOUNDATION {activeItem.pillarNumber}
                      </span>
                    </div>
                    <span className="text-xs font-semibold text-[#8a7e70]">
                      {activeIndex + 1} of {galleryEnvironments.length}
                    </span>
                  </div>

                  {/* Foundation Header */}
                  <div className="mt-4 sm:mt-5">
                    <h3 className="font-serif text-2xl sm:text-3xl text-[var(--ink)] leading-snug">
                      {activeItem.pillar}
                    </h3>
                  </div>

                  {/* Lornette Daye Quote */}
                  <div className="mt-5 border-l-2 border-[var(--gold-dark)] bg-[#fcfaf5] p-4 sm:p-4.5 rounded-r-[2px]">
                    <p className="text-xs font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)] mb-1">
                      Lornette Daye
                    </p>
                    <blockquote className="font-serif italic text-base sm:text-[17px] text-[var(--ink)] leading-relaxed">
                      &ldquo;{activeItem.quote}&rdquo;
                    </blockquote>
                  </div>

                </div>

                {/* Bottom Actions */}
                <div className="mt-5 pt-4 sm:pt-5 border-t border-[var(--line)] flex flex-col sm:flex-row items-stretch sm:items-center gap-3">
                  <Link
                    href="#pathways"
                    className="inline-flex items-center justify-center gap-2 rounded-[2px] bg-[var(--gold-dark)] px-5 py-3 text-xs font-bold uppercase tracking-[0.2em] text-white shadow-sm transition hover:bg-[#8e7232]"
                  >
                    <span>EXPLORE PATHWAYS</span>
                    <ArrowRight size={13} />
                  </Link>
                  <Link
                    href="/book"
                    className="inline-flex items-center justify-center gap-2 rounded-[2px] border border-[var(--line)] bg-transparent px-4 py-3 text-xs font-bold uppercase tracking-[0.18em] text-[var(--ink)] transition hover:border-[var(--gold-dark)] hover:text-[var(--gold-dark)]"
                  >
                    <span>SCHEDULE CONSULTATION</span>
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

