"use client";

import Image from "next/image";
import Link from "next/link";
import { LearnerShell } from "@/components/foundations/learner/LearnerShell";
import {
  ArrowRight,
  Check,
  ChevronRight,
  Flag,
  Sparkles,
} from "lucide-react";

type JourneyStage = {
  number: number;
  title: string;
  subtitle: string;
  status: "completed" | "active" | "upcoming";
  thumbnail: string;
};

const CANONICAL_JOURNEY_STAGES: JourneyStage[] = [
  {
    number: 1,
    title: "Identity Beyond Sport",
    subtitle: "Ground your identity and self-worth beyond the scoreboard.",
    status: "completed",
    thumbnail: "/foundations/golf/curriculum/week-01-dew-flag.jpg",
  },
  {
    number: 2,
    title: "Champion Mindset",
    subtitle: "Train focus, confidence, and visualization under pressure.",
    status: "completed",
    thumbnail: "/foundations/golf/curriculum/week-02-fairway-sunrise.jpg",
  },
  {
    number: 3,
    title: "Discipline Systems",
    subtitle: "Create consistency with your 6-step pre-shot protocol.",
    status: "active",
    thumbnail: "/foundations/golf/curriculum/week-03-address-stance.jpg",
  },
  {
    number: 4,
    title: "Resilience After Setback",
    subtitle: "Master the 5-second mistake reset and next-shot principle.",
    status: "upcoming",
    thumbnail: "/foundations/golf/curriculum/week-04-keynote-fairway.jpg",
  },
  {
    number: 5,
    title: "Pressure, Emotional Regulation & Recovery",
    subtitle: "Regulate heart rate spikes and maintain composure.",
    status: "upcoming",
    thumbnail: "/foundations/golf/curriculum/week-05-sunrise-lake.jpg",
  },
  {
    number: 6,
    title: "Communication & Presence",
    subtitle: "Elevate your self-talk, body language, and coach dialogue.",
    status: "upcoming",
    thumbnail: "/foundations/golf/curriculum/week-06-tour-bag.jpg",
  },
  {
    number: 7,
    title: "Family & Community Support",
    subtitle: "Align your inner circle and competitive boundaries.",
    status: "upcoming",
    thumbnail: "/foundations/golf/curriculum/week-07-clubhouse-lounge.jpg",
  },
  {
    number: 8,
    title: "Career & Money Readiness",
    subtitle: "Equip yourself with financial stability and career transition tools.",
    status: "upcoming",
    thumbnail: "/foundations/golf/curriculum/week-08-executive-desk.jpg",
  },
  {
    number: 9,
    title: "Personal Brand & Story",
    subtitle: "Articulate your personal values and leadership presence.",
    status: "upcoming",
    thumbnail: "/foundations/golf/curriculum/week-09-terrace-vista.jpg",
  },
  {
    number: 10,
    title: "Legacy & Community Impact",
    subtitle: "Give back through mentorship and build an enduring legacy.",
    status: "upcoming",
    thumbnail: "/foundations/golf/curriculum/week-10-ocean-links.jpg",
  },
];

import { useFoundationsStore } from "@/lib/foundations/store";

export default function FoundationsProgressPage() {
  const { activeAthlete } = useFoundationsStore();
  const completedCount = activeAthlete.completedFoundations.length;

  return (
    <LearnerShell>
      <div className="p-4 sm:p-6 lg:p-8 max-w-7xl mx-auto space-y-6">
        {/* ========================================================= */}
        {/* TOP HERO BANNER (Matches Mockup 3 media_1789625869325.jpg) */}
        {/* ========================================================= */}
        <section className="relative overflow-hidden rounded-2xl border border-[#dfcca6] bg-[#fbf9f4] p-6 sm:p-8 shadow-[0_4px_24px_rgba(30,24,15,0.04)]">
          <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
            <div>
              <h1 className="font-serif text-3xl sm:text-4xl lg:text-[42px] font-semibold tracking-tight text-[#1e1b18] leading-tight">
                YOUR PERFORMANCE JOURNEY
              </h1>
              <p className="mt-2 font-serif text-base sm:text-xl text-[#665a4c]">
                Ten weeks. Practical tools. One next shot at a time.
              </p>
            </div>

            <div className="text-right flex flex-col items-end">
              <span className="font-serif text-xl sm:text-2xl italic text-[#b89456]">
                Better Golf. A Stronger You.
              </span>
              <div className="mt-2 inline-flex items-center gap-2 rounded-full bg-[#f4ede1] px-3.5 py-1 text-xs font-semibold text-[#1e3a29] border border-[#dfcca6]/50">
                <Sparkles size={13} />
                <span>{completedCount} of 10 Foundations Completed</span>
              </div>
            </div>
          </div>
        </section>

        {/* ========================================================= */}
        {/* 2-COLUMN LAYOUT: COACH CARD + 10-FOUNDATION OVERVIEW      */}
        {/* ========================================================= */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          {/* Left Column: Coach Lornette Profile Card (col-span-4) */}
          <div className="lg:col-span-4 rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-6 shadow-[0_2px_12px_rgba(30,24,15,0.03)] space-y-5">
            <div className="relative aspect-[4/5] w-full overflow-hidden rounded-lg border border-[#dfcca6]/60 shadow-xs">
              <Image
                src="/generated/lornette-executive-portrait.jpg"
                alt="Coach Lornette Daye in white blazer"
                fill
                sizes="(max-width: 1024px) 100vw, 380px"
                quality={95}
                className="object-cover"
                priority
              />
            </div>

            <div className="space-y-1">
              <p className="text-[10px] font-bold uppercase tracking-[0.24em] text-[#8e7e6e]">
                YOUR COACH
              </p>
              <h2 className="font-serif text-2xl font-semibold tracking-tight text-[#1e1b18]">
                LORNETTE DAYE
              </h2>
              <p className="pt-1 text-xs sm:text-sm text-[#665a4c] leading-relaxed">
                Helping you build the mindset, habits, and resilience to perform your best, on and off the course.
              </p>
            </div>

            {/* Quote Card */}
            <div className="rounded-lg border border-[#ebdcc9] bg-[#fcfaf5] p-4">
              <p className="font-serif text-sm italic text-[#2c2620] leading-relaxed">
                “Progress isn’t about perfection. It’s about your next shot.”
              </p>
              <p className="mt-2 text-[10px] font-bold uppercase tracking-wider text-[#8a6828]">
                LORNETTE DAYE
              </p>
            </div>
          </div>

          {/* Right Column: 10-Foundation Overview Sequence (col-span-8) */}
          <div id="assessments" className="lg:col-span-8 rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-5 sm:p-7 shadow-[0_2px_12px_rgba(30,24,15,0.03)] space-y-4 scroll-mt-24">
            <div className="flex flex-col sm:flex-row sm:items-center justify-between border-b border-[#ebdcc9] pb-3 gap-2">
              <p className="text-[11px] font-bold uppercase tracking-[0.24em] text-[#8e7e6e]">
                PROGRAM OVERVIEW
              </p>
              <span className="text-[11px] font-bold uppercase tracking-[0.16em] text-[#8a6828]">
                10 FOUNDATIONS &nbsp;|&nbsp; 10 WEEKS &nbsp;|&nbsp; A STRONGER YOU
              </span>
            </div>

            {/* Stepper List */}
            <div className="space-y-2.5 pt-1">
              {CANONICAL_JOURNEY_STAGES.map((stage) => {
                const isCompleted =
                  activeAthlete.completedFoundations.includes(stage.number);
                const isActive =
                  stage.number === activeAthlete.currentWeek && !isCompleted;

                return (
                  <Link
                    key={stage.number}
                    href={`/foundations/lessons?lesson=${stage.number}`}
                    className={`flex items-center justify-between gap-4 rounded-xl p-3 sm:p-3.5 transition-all duration-150 ${
                      isActive
                        ? "bg-[#e8dbbf]/60 border border-[#dfcca6] shadow-xs"
                        : "hover:bg-[#f4ede1] border border-transparent"
                    }`}
                  >
                    {/* Left: Number Circle */}
                    <div className="flex items-center gap-3.5 min-w-0">
                      <div
                        className={`flex h-9 w-9 shrink-0 items-center justify-center rounded-full text-xs font-serif font-bold ${
                          isActive
                            ? "bg-[#b89456] text-[#1e1b18] shadow-xs ring-2 ring-[#dfcca6]"
                            : isCompleted
                            ? "bg-[#1e3a29] text-white"
                            : "bg-[#ede4d5] text-[#5e5346]"
                        }`}
                      >
                        {isCompleted ? <Check size={16} aria-hidden="true" /> : stage.number}
                      </div>

                      {/* Middle: Titles */}
                      <div className="min-w-0">
                        <div className="flex items-center gap-2">
                          <h3
                            className={`font-serif text-sm sm:text-base font-semibold truncate ${
                              isActive ? "text-[#1e1b18]" : "text-[#3d3429]"
                            }`}
                          >
                            {stage.title}
                          </h3>
                          {isActive && (
                            <span className="hidden sm:inline-block rounded-xs bg-[#1e3a29] px-1.5 py-0.5 text-[9px] font-bold uppercase tracking-wider text-white">
                              Active Week
                            </span>
                          )}
                        </div>
                        <p className="text-xs text-[#706456] truncate max-w-sm sm:max-w-md">
                          {stage.subtitle}
                        </p>
                      </div>
                    </div>

                    {/* Right: Scenic Preview Thumbnail & Chevron */}
                    <div className="flex items-center gap-3 shrink-0">
                      <div className="relative h-8 w-20 sm:w-28 rounded-md overflow-hidden border border-[#ebdcc9] hidden sm:block">
                        <Image
                          src={stage.thumbnail}
                          alt=""
                          role="presentation"
                          fill
                          sizes="(max-width: 640px) 80px, 120px"
                          quality={95}
                          className="object-cover"
                        />
                      </div>
                      <ChevronRight size={18} className="text-[#a69888]" aria-hidden="true" />
                    </div>
                  </Link>
                );
              })}
            </div>
          </div>
        </div>

        {/* ========================================================= */}
        {/* BOTTOM DOCKED STRIP (Matches Mockup 3 bottom bar)         */}
        {/* ========================================================= */}
        <section className="rounded-xl border border-[#dfcca6] bg-[#fdfbf7] p-4 sm:p-5 flex flex-col sm:flex-row items-center justify-between gap-4 shadow-xs">
          <div className="flex items-center gap-3.5">
            <div className="flex h-11 w-11 shrink-0 items-center justify-center rounded-full bg-[#f4ebe0] text-[#a6864a]">
              <Flag size={20} strokeWidth={1.75} aria-hidden="true" />
            </div>
            <div>
              <p className="font-serif text-xs sm:text-sm font-bold uppercase tracking-[0.2em] text-[#1e1b18]">
                SAME PRINCIPLES. A STRONGER YOU.
              </p>
              <p className="text-xs text-[#706456]">
                Continue your daily practice and weekly coaching reflections.
              </p>
            </div>
          </div>

          <Link
            href="/foundations/lessons"
            className="inline-flex items-center gap-2 rounded-full bg-gradient-to-r from-[#dfc385] via-[#ceab68] to-[#b38f4a] px-6 py-2.5 text-xs font-bold uppercase tracking-[0.16em] text-white shadow-xs hover:brightness-105 active:brightness-95 transition-all focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#ba934d]"
          >
            <span>Let’s Do This</span>
            <ArrowRight size={15} aria-hidden="true" />
          </Link>
        </section>
      </div>
    </LearnerShell>
  );
}
