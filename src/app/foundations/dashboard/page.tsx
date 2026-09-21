"use client";

import Image from "next/image";
import Link from "next/link";
import { LearnerShell } from "@/components/foundations/learner/LearnerShell";
import { useFoundationsStore } from "@/lib/foundations/store";
import {
  ArrowRight,
  BarChart3,
  CheckCircle2,
  ChevronRight,
  Compass,
  FileText,
  Flame,
  MapPin,
  PlayCircle,
  ShieldCheck,
} from "lucide-react";

export default function FoundationsDashboardPage() {
  const { activeAthlete } = useFoundationsStore();
  const completedPct = Math.round(
    (activeAthlete.completedFoundations.length / 10) * 100
  );
  const strokeDashoffset = 251.2 - (251.2 * completedPct) / 100;
  const completedGoalsCount = activeAthlete.goals.filter((g) => g.completed).length;
  return (
    <LearnerShell>
      <div className="p-4 sm:p-6 lg:p-8 max-w-7xl mx-auto space-y-6">
        {/* ========================================================= */}
        {/* HERO BANNER (Matches Mockup 1 media_1789625869327.png)     */}
        {/* ========================================================= */}
        <section className="relative overflow-hidden rounded-2xl border border-[#dfcca6] bg-[#fbf9f4] shadow-[0_4px_24px_rgba(30,24,15,0.04)]">
          <div className="grid grid-cols-1 lg:grid-cols-12 items-center min-h-[300px] p-6 sm:p-8 lg:p-10 gap-6">
            {/* Left Copy Column */}
            <div className="lg:col-span-6 z-10 space-y-4">
              <div className="flex items-center gap-3">
                <div className="relative h-9 w-12 shrink-0">
                  <Image
                    src="/monogramlogo.png"
                    alt="Lornette Daye Official Logo"
                    fill
                    sizes="48px"
                    className="object-contain"
                    priority
                    unoptimized
                  />
                </div>
                <p className="font-sans text-[11px] font-bold uppercase tracking-[0.28em] text-[#5e5245]">
                  LORNETTE’S FOUNDATION GOLF
                </p>
              </div>
              <h1 className="font-serif text-3xl sm:text-4xl lg:text-[44px] font-semibold tracking-tight text-[#1e1b18] leading-[1.08]">
                WELCOME TO MY PERFORMANCE EDGE
              </h1>
              <p className="font-sans text-xs font-semibold uppercase tracking-widest text-[#7f5b1d]">
                Powered by the Performance Edge Framework
              </p>
              <p className="font-serif text-lg sm:text-xl text-[#3d3429] leading-snug">
                Your guided Golf performance journey starts here.
              </p>
              <p className="font-sans text-xs sm:text-sm text-[#5e5245] max-w-lg leading-relaxed">
                Build the mindset, habits and strategies to play with greater clarity, confidence and consistency, on and off the course.
              </p>

              <div className="pt-2">
                <Link
                  href="/foundations/lessons"
                  className="inline-flex min-h-11 items-center gap-2.5 rounded-full bg-gradient-to-r from-[#dfc385] via-[#ceab68] to-[#b38f4a] px-6 py-3 text-xs font-bold uppercase tracking-[0.16em] text-[#1e1b18] shadow-sm hover:brightness-105 active:brightness-95 transition-all focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#ba934d]"
                >
                  <span>Start Your Journey</span>
                  <ArrowRight size={15} aria-hidden="true" />
                </Link>
              </div>
            </div>

            {/* Right Framed Terrace Feature Card with Docked Luxury Editorial Plaque */}
            <div className="lg:col-span-6 relative w-full h-[320px] sm:h-[360px] lg:h-[380px] rounded-xl overflow-hidden border border-[#dfcca6] shadow-sm group">
              <Image
                src="/foundations/golf/dashboard/lornette-table-notebook-pen.png"
                alt="Coach Lornette Daye with reflection journal and coffee on clubhouse terrace overlooking the fairway"
                fill
                sizes="(max-width: 1024px) 100vw, 600px"
                quality={95}
                className="object-cover object-[25%_center] sm:object-center group-hover:scale-[1.02] transition-transform duration-700"
                priority
              />
              {/* Docked Luxury Editorial Plaque */}
              <div className="absolute inset-x-0 bottom-0 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(18,15,13,0.85)] p-4 sm:p-5 backdrop-blur-md shadow-2xl">
                <p className="text-[10px] sm:text-[11px] font-bold uppercase tracking-[0.22em] text-[#dfcca6]">
                  FOUNDATION PRINCIPLE · COACH LORNETTE DAYE
                </p>
                <p className="mt-1 font-serif text-base sm:text-lg italic text-white leading-snug">
                  “A stronger you creates a stronger game.”
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* ========================================================= */}
        {/* 4 QUICK ACTION CARDS                                      */}
        {/* ========================================================= */}
        <section aria-label="Portal Shortcuts" className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          {/* Card 1: My Journey */}
          <Link
            href="/foundations/progress"
            className="group flex items-center justify-between rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-4 sm:p-5 shadow-[0_2px_12px_rgba(30,24,15,0.03)] hover:border-[#dfcca6] hover:shadow-md transition-all focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)]"
          >
            <div className="flex items-center gap-3.5">
              <div className="flex h-12 w-12 shrink-0 items-center justify-center rounded-full bg-[#f4ebe0] text-[#7f5b1d] group-hover:bg-[#dfcca6] group-hover:text-[#1e1b18] transition-colors">
                <MapPin size={22} strokeWidth={1.75} aria-hidden="true" />
              </div>
              <div>
                <span className="block font-serif text-base font-semibold text-[#1e1b18] group-hover:text-[#7f5b1d] transition-colors">
                  My Journey
                </span>
                <p className="text-xs text-[#5e5245] leading-tight">
                  Track your progress and milestones.
                </p>
              </div>
            </div>
            <ChevronRight size={18} className="text-[#756756] group-hover:text-[#1e1b18] transition-colors shrink-0" aria-hidden="true" />
          </Link>

          {/* Card 2: Lessons */}
          <Link
            href="/foundations/lessons"
            className="group flex items-center justify-between rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-4 sm:p-5 shadow-[0_2px_12px_rgba(30,24,15,0.03)] hover:border-[#dfcca6] hover:shadow-md transition-all focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)]"
          >
            <div className="flex items-center gap-3.5">
              <div className="flex h-12 w-12 shrink-0 items-center justify-center rounded-full bg-[#f4ebe0] text-[#7f5b1d] group-hover:bg-[#dfcca6] group-hover:text-[#1e1b18] transition-colors">
                <PlayCircle size={22} strokeWidth={1.75} aria-hidden="true" />
              </div>
              <div>
                <span className="block font-serif text-base font-semibold text-[#1e1b18] group-hover:text-[#7f5b1d] transition-colors">
                  Lessons
                </span>
                <p className="text-xs text-[#5e5245] leading-tight">
                  Learn, apply and level up.
                </p>
              </div>
            </div>
            <ChevronRight size={18} className="text-[#756756] group-hover:text-[#1e1b18] transition-colors shrink-0" aria-hidden="true" />
          </Link>

          {/* Card 3: Assessments */}
          <Link
            href="/foundations/progress#assessments"
            className="group flex items-center justify-between rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-4 sm:p-5 shadow-[0_2px_12px_rgba(30,24,15,0.03)] hover:border-[#dfcca6] hover:shadow-md transition-all focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)]"
          >
            <div className="flex items-center gap-3.5">
              <div className="flex h-12 w-12 shrink-0 items-center justify-center rounded-full bg-[#f4ebe0] text-[#7f5b1d] group-hover:bg-[#dfcca6] group-hover:text-[#1e1b18] transition-colors">
                <BarChart3 size={22} strokeWidth={1.75} aria-hidden="true" />
              </div>
              <div>
                <span className="block font-serif text-base font-semibold text-[#1e1b18] group-hover:text-[#7f5b1d] transition-colors">
                  Assessments
                </span>
                <p className="text-xs text-[#5e5245] leading-tight">
                  Understand your game and growth.
                </p>
              </div>
            </div>
            <ChevronRight size={18} className="text-[#756756] group-hover:text-[#1e1b18] transition-colors shrink-0" aria-hidden="true" />
          </Link>

          {/* Card 4: Resources */}
          <Link
            href="/foundations/resources"
            className="group flex items-center justify-between rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-4 sm:p-5 shadow-[0_2px_12px_rgba(30,24,15,0.03)] hover:border-[#dfcca6] hover:shadow-md transition-all focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)]"
          >
            <div className="flex items-center gap-3.5">
              <div className="flex h-12 w-12 shrink-0 items-center justify-center rounded-full bg-[#f4ebe0] text-[#7f5b1d] group-hover:bg-[#dfcca6] group-hover:text-[#1e1b18] transition-colors">
                <FileText size={22} strokeWidth={1.75} aria-hidden="true" />
              </div>
              <div>
                <span className="block font-serif text-base font-semibold text-[#1e1b18] group-hover:text-[#7f5b1d] transition-colors">
                  Resources
                </span>
                <p className="text-xs text-[#5e5245] leading-tight">
                  Tools, guides and bonus materials.
                </p>
              </div>
            </div>
            <ChevronRight size={18} className="text-[#756756] group-hover:text-[#1e1b18] transition-colors shrink-0" aria-hidden="true" />
          </Link>
        </section>

        {/* ========================================================= */}
        {/* COACH LORNETTE REVIEW & 30-DAY GOALS SHOWCASE             */}
        {/* ========================================================= */}
        <section
          aria-label="Coach Review & Goals"
          className="rounded-2xl border border-[#dfcca6] bg-gradient-to-br from-[#fdfbf7] via-[#f9f4ea] to-[#fbf8f0] p-6 shadow-sm"
        >
          <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-6">
            <div className="space-y-2 flex-1">
              <div className="flex flex-wrap items-center gap-2.5">
                <span className="rounded-xs bg-[#1e3a29] px-2.5 py-0.5 text-[9.5px] font-bold uppercase tracking-wider text-white">
                  Athlete Blueprint
                </span>
                <span
                  className={`inline-flex items-center gap-1.5 rounded-full px-2.5 py-0.5 text-[10.5px] font-semibold border ${
                    activeAthlete.status === "approved"
                      ? "bg-[#d1fae5] text-[#065f46] border-[#a7f3d0]"
                      : activeAthlete.status === "needs_revision"
                      ? "bg-[#fef3c7] text-[#92400e] border-[#fde68a]"
                      : activeAthlete.status === "pending_review"
                      ? "bg-[#eff6ff] text-[#1e40af] border-[#bfdbfe]"
                      : "bg-[#f5ede2] text-[#1e3a29] border-[#dfcca6]"
                  }`}
                >
                  <ShieldCheck size={13} />
                  <span>
                    {activeAthlete.status === "approved"
                      ? "Coach Lornette Daye Approved ✓"
                      : activeAthlete.status === "needs_revision"
                      ? "Revision Requested"
                      : activeAthlete.status === "pending_review"
                      ? "Awaiting Coach Review"
                      : "Coach Lornette Daye Reviewed"}
                  </span>
                </span>
              </div>

              <h2 className="font-serif text-xl sm:text-2xl font-semibold text-[#1e1b18]">
                My Performance Edge Plan & 30-Day Goals
              </h2>

              {activeAthlete.coachFeedbackNotes ? (
                <p className="font-serif text-sm sm:text-base italic text-[#2c2620] leading-relaxed max-w-2xl">
                  “{activeAthlete.coachFeedbackNotes}”
                </p>
              ) : (
                <p className="text-xs sm:text-sm text-[#706456] italic">
                  Your customized pre-shot routine and 5-second reset protocol are active. Notes from Coach Lornette appear here once reviewed.
                </p>
              )}

              <div className="flex flex-wrap items-center gap-4 pt-1 text-xs text-[#6d6153]">
                <span className="font-medium">
                  {completedGoalsCount} of {activeAthlete.goals.length} Goals Active & Verified
                </span>
                <span>•</span>
                <span className="italic text-[#8a6828]">
                  Reset Cue: {activeAthlete.anchorCue}
                </span>
              </div>
            </div>

            <div className="flex flex-col sm:flex-row lg:flex-col gap-2.5 shrink-0">
              <Link
                href="/foundations/plan"
                className="inline-flex min-h-11 items-center justify-center gap-2 rounded-lg bg-gradient-to-r from-[#dfc385] via-[#ceab68] to-[#b38f4a] px-5 py-2.5 text-xs font-bold uppercase tracking-[0.14em] text-[#1e1b18] shadow-xs hover:brightness-105 transition-all"
              >
                <Compass size={14} aria-hidden="true" />
                <span>View Full Performance Plan →</span>
              </Link>
              <Link
                href="/foundations/grill-me"
                className="inline-flex min-h-11 items-center justify-center gap-2 rounded-lg border border-[#dac8b2] bg-white px-5 py-2.5 text-xs font-semibold text-[#4e4337] hover:bg-[#f4ede1] transition-colors"
              >
                <Flame size={14} className="text-[#b45309]" aria-hidden="true" />
                <span>Take Grill-Me Audit →</span>
              </Link>
            </div>
          </div>
        </section>

        {/* ========================================================= */}
        {/* ROW OF 3 BOTTOM FEATURE CARDS                             */}
        {/* ========================================================= */}
        <section aria-label="Portal Highlights" className="grid grid-cols-1 lg:grid-cols-12 gap-5">
          {/* Card 1: A Message From Lornette (col-span-5) */}
          <div className="lg:col-span-5 rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-5 sm:p-6 shadow-[0_2px_12px_rgba(30,24,15,0.03)] flex flex-col justify-between">
            <div>
              <p className="text-[10.5px] font-bold uppercase tracking-[0.22em] text-[#8e7e6e]">
                A Message From Lornette
              </p>
              <div className="mt-4 flex items-center gap-4 sm:gap-5">
                <div className="relative h-20 w-20 sm:h-24 sm:w-24 shrink-0 rounded-full overflow-hidden border-2 border-[#dfcca6] shadow-sm">
                  <Image
                    src="/generated/lornette-executive-portrait.jpg"
                    alt="Coach Lornette Daye"
                    fill
                    sizes="96px"
                    quality={95}
                    className="object-cover object-top"
                  />
                </div>
                <div>
                  <p className="font-serif text-sm sm:text-base italic text-[#2c2620] leading-relaxed">
                    “I’m so glad you’re here. This journey is about more than golf. It is about becoming the strongest version of you. Let’s get started.”
                  </p>
                </div>
              </div>
            </div>

            {/* Elegant Signature */}
            <div className="mt-4 pt-3 border-t border-[#ebdcc9]/60 flex items-center justify-between">
              <span className="font-serif text-xl sm:text-2xl italic tracking-wide text-[#8a6828] select-none">
                Lornette Daye
              </span>
              <span className="text-[10px] font-bold uppercase tracking-wider text-[#8e7e6e]">
                Olympic Coach & Founder
              </span>
            </div>
          </div>

          {/* Card 2: Your Progress Circular Gauge (col-span-3) */}
          <div className="lg:col-span-3 rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-5 sm:p-6 shadow-[0_2px_12px_rgba(30,24,15,0.03)] flex flex-col justify-between">
            <p className="text-[10.5px] font-bold uppercase tracking-[0.22em] text-[#5e5245]">
              Your Progress
            </p>

            <div className="my-auto py-4 flex items-center justify-around gap-3">
              {/* Circular Gauge */}
              <div
                role="progressbar"
                aria-valuenow={completedPct}
                aria-valuemin={0}
                aria-valuemax={100}
                aria-label="Foundations curriculum completion progress"
                className="relative flex items-center justify-center"
              >
                <svg aria-hidden="true" className="w-24 h-24 -rotate-90 transform" viewBox="0 0 100 100">
                  <circle
                    cx="50"
                    cy="50"
                    r="40"
                    stroke="#ede3d5"
                    strokeWidth="8"
                    fill="transparent"
                  />
                  <circle
                    cx="50"
                    cy="50"
                    r="40"
                    stroke="#1e3a29"
                    strokeWidth="8"
                    fill="transparent"
                    strokeDasharray="251.2"
                    strokeDashoffset={strokeDashoffset}
                    strokeLinecap="round"
                  />
                </svg>
                <div className="absolute text-center">
                  <span className="font-serif text-2xl font-bold text-[#1e1b18]">
                    {completedPct}%
                  </span>
                  <span className="block text-[9px] uppercase tracking-wider text-[#7a6f62]">
                    complete
                  </span>
                </div>
              </div>

              {/* Vertical divider and copy */}
              <div className="border-l border-[#ebdcc9] pl-3 py-1">
                <p className="font-serif text-sm font-semibold text-[#1e1b18] leading-tight">
                  Progress builds performance.
                </p>
                <p className="mt-1 text-[11px] text-[#706456]">
                  Week {activeAthlete.currentWeek} of 10
                </p>
                <div className="mt-2 h-[2px] w-10 bg-[#dfcca6]" />
              </div>
            </div>

            <Link
              href="/foundations/progress"
              className="text-center text-[11px] font-bold uppercase tracking-[0.16em] text-[#1e3a29] hover:underline"
            >
              View Full 10-Foundation Pathway →
            </Link>
          </div>

          {/* Card 3: Scenic Golf Hole with Docked Editorial Plaque (col-span-4) */}
          <div className="lg:col-span-4 rounded-xl border border-[#ebdcc9] bg-[#1e1b18] overflow-hidden shadow-[0_2px_12px_rgba(30,24,15,0.03)] relative min-h-[220px] flex flex-col justify-end">
            <Image
              src="/foundations/golf/sunlight-golf-fairway-sunrise.jpg"
              alt="Pristine championship golf green in warm morning sunlight"
              fill
              sizes="(max-width: 1024px) 100vw, 450px"
              quality={95}
              className="object-cover"
            />
            {/* Docked Plaque */}
            <div className="relative z-10 bg-[rgba(18,15,13,0.85)] backdrop-blur-xs border-t border-[rgba(198,165,92,0.4)] p-4 text-center">
              <p className="font-serif text-sm sm:text-base font-semibold tracking-[0.16em] text-[#fbf9f4] uppercase leading-snug">
                A Calmer Mind
              </p>
              <p className="font-serif text-sm sm:text-base font-semibold tracking-[0.16em] text-[#dfcca6] uppercase leading-snug">
                A Stronger Game
              </p>
            </div>
          </div>
        </section>

        {/* ========================================================= */}
        {/* LUXURY SIGNATURE BOTTOM BANNER (Matches user mockup)      */}
        {/* ========================================================= */}
        <section
          aria-label="Signature Philosophy Banner"
          className="relative overflow-hidden rounded-2xl border border-[#ebdcc9] bg-[#fdfbf7] shadow-[0_2px_16px_rgba(30,24,15,0.03)] min-h-[78px] sm:min-h-[88px] flex items-center justify-between p-3.5 sm:px-8"
        >
          {/* Left panoramic fairway image with smooth gradient fade into cream */}
          <div className="absolute inset-y-0 left-0 w-2/5 sm:w-1/2 pointer-events-none overflow-hidden">
            <Image
              src="/foundations/golf/sunlight-golf-fairway-sunrise.jpg"
              alt=""
              role="presentation"
              fill
              sizes="(max-width: 768px) 40vw, 50vw"
              quality={95}
              className="object-cover object-left"
            />
            <div className="absolute inset-0 bg-gradient-to-r from-transparent via-[#fdfbf7]/70 to-[#fdfbf7]" />
          </div>

          <div className="hidden sm:block flex-1" />

          {/* Right Text & Signature */}
          <div className="relative z-10 flex items-center gap-2.5 sm:gap-6 ml-auto">
            <div className="text-right">
              <p className="font-sans text-[8.5px] sm:text-[11.5px] font-bold uppercase tracking-[0.18em] sm:tracking-[0.24em] text-[#8e7e6e]">
                Discipline Your Focus.
              </p>
              <p className="font-sans text-[8.5px] sm:text-[11.5px] font-bold uppercase tracking-[0.18em] sm:tracking-[0.24em] text-[#a6864a]">
                Elevate Your Game.
              </p>
            </div>
            <div className="hidden sm:block h-[1px] w-12 sm:w-20 bg-[#dfcca6]" />
            <span className="font-serif text-lg sm:text-3xl italic tracking-wide text-[#8a6828] select-none whitespace-nowrap">
              Lornette Daye
            </span>
          </div>
        </section>
      </div>
    </LearnerShell>
  );
}
