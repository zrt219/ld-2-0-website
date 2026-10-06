"use client";

import { useState } from "react";
import Image from "next/image";
import Link from "next/link";
import { motion, AnimatePresence } from "framer-motion";
import { LearnerShell } from "@/components/foundations/learner/LearnerShell";
import {
  MotionFadeIn,
  MotionScaleIn,
  MotionStaggerContainer,
  MotionStaggerItem,
} from "@/components/motion";
import { useFoundationsStore } from "@/lib/foundations/store";
import {
  TrackId,
  getTrackConfig,
} from "@/lib/foundations/track-registry";
import {
  ArrowLeft,
  ArrowRight,
  BarChart3,
  ChevronRight,
  Compass,
  FileText,
  Flame,
  Globe,
  Lock,
  MapPin,
  PlayCircle,
  ShieldCheck,
} from "lucide-react";

export default function FoundationsDashboardPage() {
  const {
    state,
    activeAthlete,
    updateGdprConsents,
    exportGdprDataArchive,
  } = useFoundationsStore();

  const [showGdprModal, setShowGdprModal] = useState(false);
  const [gdprSaving, setGdprSaving] = useState(false);
  const [gdprSuccess, setGdprSuccess] = useState(false);

  const currentTrackId: TrackId = (state.activeTrack as TrackId) || "golf";
  const trackConfig = getTrackConfig(currentTrackId);

  const completedPct = Math.round(
    (activeAthlete.completedFoundations.length / 10) * 100
  );
  const strokeDashoffset = 251.2 - (251.2 * completedPct) / 100;
  const completedGoalsCount = activeAthlete.goals.filter((g) => g.completed).length;

  const handleSaveGdpr = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setGdprSaving(true);
    const form = e.currentTarget;
    const analytics = (form.elements.namedItem("gdpr_analytics") as HTMLInputElement)?.checked ?? false;
    const coachingRecordings = (form.elements.namedItem("gdpr_recordings") as HTMLInputElement)?.checked ?? false;
    const peerFeedback = (form.elements.namedItem("gdpr_feedback") as HTMLInputElement)?.checked ?? false;

    await updateGdprConsents({
      analytics,
      coachingRecordings,
      peerFeedback,
    });
    setGdprSaving(false);
    setGdprSuccess(true);
    setTimeout(() => {
      setGdprSuccess(false);
      setShowGdprModal(false);
    }, 1200);
  };

  return (
    <LearnerShell>
      <div className="p-4 sm:p-6 lg:p-8 max-w-7xl mx-auto space-y-8">

        {/* ========================================================= */}
        {/* TRACK HEADER STRIP (With '← Change Track' Button)         */}
        {/* ========================================================= */}
        <section aria-label="Active Track Status" className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b border-[#ebdcc9] pb-4">
          <div className="flex items-center gap-3">
            <span className="flex h-2.5 w-2.5 rounded-full bg-[#1e3a29]" />
            <div>
              <p className="text-[10px] font-bold uppercase tracking-[0.22em] text-[#7f5b1d]">
                Active Focused Workspace
              </p>
              <h2 className="font-serif text-lg sm:text-xl font-bold text-[#1e1b18] leading-tight">
                {trackConfig.label} Track
              </h2>
            </div>
          </div>

          <div className="flex items-center gap-3">
            {currentTrackId === "europe" && (
              <span className="inline-flex items-center gap-1 rounded-full bg-[#e0f2fe] px-2.5 py-0.5 text-[10.5px] font-bold uppercase tracking-wider text-[#0369a1] border border-[#bae6fd]">
                <Globe size={11} /> EU GDPR Sovereign
              </span>
            )}

            <Link
              href="/foundations/select"
              className="inline-flex items-center gap-1.5 rounded-full border border-[#cfb78f] bg-white px-3.5 py-1.5 text-xs font-semibold text-[#5e5245] hover:bg-[#f4ede1] hover:text-[#1e1b18] transition-colors shadow-2xs"
            >
              <ArrowLeft size={13} />
              <span>Change Track</span>
            </Link>
          </div>
        </section>

        {/* ========================================================= */}
        {/* HERO BANNER (Dedicated to Selected Track)                 */}
        {/* ========================================================= */}
        <MotionFadeIn className="relative overflow-hidden rounded-2xl border border-[#dfcca6] bg-[#fbf9f4] shadow-[0_4px_24px_rgba(30,24,15,0.04)]">
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
                  {trackConfig.editorialBadge}
                </p>
              </div>
              <h1 className="font-serif text-3xl sm:text-4xl lg:text-[42px] font-semibold tracking-tight text-[#1e1b18] leading-[1.08]">
                {trackConfig.heroHeadline}
              </h1>
              <p className="font-sans text-xs font-semibold uppercase tracking-widest text-[#7f5b1d]">
                {trackConfig.heroSubtitle}
              </p>
              <p className="font-serif text-lg sm:text-xl text-[#3d3429] leading-snug">
                {trackConfig.heroTagline}
              </p>
              <p className="font-sans text-xs sm:text-sm text-[#5e5245] max-w-lg leading-relaxed">
                {trackConfig.heroDescription}
              </p>

              <div className="pt-2 flex flex-wrap items-center gap-3">
                <Link
                  href="/foundations/lessons"
                  className="inline-flex min-h-11 items-center gap-2.5 rounded-full bg-gradient-to-r from-[#dfc385] via-[#ceab68] to-[#b38f4a] px-6 py-3 text-xs font-bold uppercase tracking-[0.16em] text-[#1e1b18] shadow-sm hover:brightness-105 active:brightness-95 transition-all focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#ba934d]"
                >
                  <span>Start {trackConfig.label} Journey</span>
                  <ArrowRight size={15} aria-hidden="true" />
                </Link>

                <Link
                  href={trackConfig.overviewRoute}
                  className="inline-flex min-h-11 items-center gap-2 rounded-full border border-[#cfb78f] bg-white/80 px-4 py-2.5 text-xs font-semibold text-[#4e4337] hover:bg-[#f4ede1] transition-colors"
                >
                  <span>Public Overview</span>
                  <ChevronRight size={14} />
                </Link>
              </div>
            </div>

            {/* Right Framed Terrace Feature Card with Docked Luxury Editorial Plaque */}
            <div className="lg:col-span-6 relative w-full h-[320px] sm:h-[360px] lg:h-[380px] rounded-xl overflow-hidden border border-[#dfcca6] shadow-sm group">
              <Image
                src={trackConfig.heroImage}
                alt={trackConfig.heroImageAlt}
                fill
                sizes="(max-width: 1024px) 100vw, 600px"
                quality={95}
                className="object-cover object-[25%_center] sm:object-center group-hover:scale-[1.02] transition-transform duration-700"
                priority
              />
              {/* Docked Luxury Editorial Plaque */}
              <div className="absolute inset-x-0 bottom-0 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(18,15,13,0.85)] p-4 sm:p-5 backdrop-blur-md shadow-2xl">
                <p className="text-[10px] sm:text-[11px] font-bold uppercase tracking-[0.22em] text-[#dfcca6]">
                  {trackConfig.quoteEyebrow}
                </p>
                <p className="mt-1 font-serif text-base sm:text-lg italic text-white leading-snug">
                  {trackConfig.quote}
                </p>
              </div>
            </div>
          </div>
        </MotionFadeIn>

        {/* ========================================================= */}
        {/* 4 QUICK ACTION CARDS (Customized to Active Track)         */}
        {/* ========================================================= */}
        <section aria-label="Portal Shortcuts">
          <MotionStaggerContainer className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            {/* Card 1: My Journey */}
            <MotionStaggerItem>
              <Link
                href="/foundations/progress"
                className="group flex items-center justify-between rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-4 sm:p-5 shadow-[0_2px_12px_rgba(30,24,15,0.03)] hover:border-[#dfcca6] hover:shadow-md transition-all focus-visible:outline focus-visible:outline-2 focus-visible:outline-[#8a6828]"
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
                      {trackConfig.quickActionLabels.journeyDesc}
                    </p>
                  </div>
                </div>
                <ChevronRight size={18} className="text-[#756756] group-hover:text-[#1e1b18] transition-colors shrink-0" aria-hidden="true" />
              </Link>
            </MotionStaggerItem>

            {/* Card 2: Lessons */}
            <MotionStaggerItem>
              <Link
                href="/foundations/lessons"
                className="group flex items-center justify-between rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-4 sm:p-5 shadow-[0_2px_12px_rgba(30,24,15,0.03)] hover:border-[#dfcca6] hover:shadow-md transition-all focus-visible:outline focus-visible:outline-2 focus-visible:outline-[#8a6828]"
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
                      {trackConfig.quickActionLabels.lessonsDesc}
                    </p>
                  </div>
                </div>
                <ChevronRight size={18} className="text-[#756756] group-hover:text-[#1e1b18] transition-colors shrink-0" aria-hidden="true" />
              </Link>
            </MotionStaggerItem>

            {/* Card 3: Assessments */}
            <MotionStaggerItem>
              <Link
                href="/foundations/progress#assessments"
                className="group flex items-center justify-between rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-4 sm:p-5 shadow-[0_2px_12px_rgba(30,24,15,0.03)] hover:border-[#dfcca6] hover:shadow-md transition-all focus-visible:outline focus-visible:outline-2 focus-visible:outline-[#8a6828]"
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
                      {trackConfig.quickActionLabels.assessmentsDesc}
                    </p>
                  </div>
                </div>
                <ChevronRight size={18} className="text-[#756756] group-hover:text-[#1e1b18] transition-colors shrink-0" aria-hidden="true" />
              </Link>
            </MotionStaggerItem>

            {/* Card 4: Resources */}
            <MotionStaggerItem>
              <Link
                href="/foundations/resources"
                className="group flex items-center justify-between rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-4 sm:p-5 shadow-[0_2px_12px_rgba(30,24,15,0.03)] hover:border-[#dfcca6] hover:shadow-md transition-all focus-visible:outline focus-visible:outline-2 focus-visible:outline-[#8a6828]"
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
                      {trackConfig.quickActionLabels.resourcesDesc}
                    </p>
                  </div>
                </div>
                <ChevronRight size={18} className="text-[#756756] group-hover:text-[#1e1b18] transition-colors shrink-0" aria-hidden="true" />
              </Link>
            </MotionStaggerItem>
          </MotionStaggerContainer>
        </section>

        {/* ========================================================= */}
        {/* EUROPEAN SPORTS & GDPR TAILORED SUITE (If European / EU)  */}
        {/* ========================================================= */}
        {currentTrackId === "europe" && (
          <MotionFadeIn
            aria-label="EU GDPR Sovereignty & Compliance Center"
            className="rounded-2xl border border-[#bae6fd] bg-gradient-to-br from-[#f0f9ff] via-[#e0f2fe] to-[#f8fafc] p-6 shadow-sm space-y-5"
          >
            <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-[#bae6fd]/60 pb-4">
              <div className="flex items-center gap-3">
                <div className="flex h-11 w-11 shrink-0 items-center justify-center rounded-full bg-[#0284c7] text-white shadow-xs">
                  <Globe size={22} />
                </div>
                <div>
                  <div className="flex items-center gap-2">
                    <span className="rounded-xs bg-[#0369a1] px-2 py-0.5 text-[9px] font-bold uppercase tracking-wider text-white">
                      EU GDPR Article 15 / 17 / 20
                    </span>
                    <span className="text-xs font-semibold text-[#0369a1]">
                      European Athlete Data Sovereignty
                    </span>
                  </div>
                  <h3 className="font-serif text-xl font-semibold text-[#0f172a] mt-0.5">
                    EU GDPR Compliance & Transatlantic Ecosystem
                  </h3>
                </div>
              </div>

              <div className="flex items-center gap-2.5">
                <button
                  type="button"
                  onClick={() => setShowGdprModal(true)}
                  className="inline-flex items-center gap-1.5 rounded-lg border border-[#0284c7] bg-white px-3.5 py-2 text-xs font-bold text-[#0369a1] hover:bg-[#e0f2fe] transition-colors cursor-pointer"
                >
                  <Lock size={13} />
                  <span>Manage EU Privacy Consents</span>
                </button>
                <button
                  type="button"
                  onClick={() => exportGdprDataArchive()}
                  className="inline-flex items-center gap-1.5 rounded-lg bg-[#0284c7] px-3.5 py-2 text-xs font-bold text-white shadow-xs hover:bg-[#0369a1] transition-colors cursor-pointer"
                >
                  <FileText size={13} />
                  <span>Download Article 20 JSON Archive</span>
                </button>
              </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs text-[#334155]">
              <div className="rounded-lg bg-white/80 p-3.5 border border-[#bae6fd]/50">
                <p className="font-semibold text-[#0f172a]">Nordic & Mediterranean Hubs</p>
                <p className="mt-1 text-[#475569] leading-relaxed">
                  Tailored curriculum delivery respecting European athletic schedules, academic semesters, and cross-border federation rules.
                </p>
              </div>
              <div className="rounded-lg bg-white/80 p-3.5 border border-[#bae6fd]/50">
                <p className="font-semibold text-[#0f172a]">Zero-Tracking Guarantee</p>
                <p className="mt-1 text-[#475569] leading-relaxed">
                  Athlete reflections and video notes are strictly private to you and Lornette Daye. No third-party ad brokers or cross-site tracking.
                </p>
              </div>
              <div className="rounded-lg bg-white/80 p-3.5 border border-[#bae6fd]/50">
                <p className="font-semibold text-[#0f172a]">Right to Erasure (Article 17)</p>
                <p className="mt-1 text-[#475569] leading-relaxed">
                  Instant local and cloud deletion workflows available in your account settings with a cryptographic audit trail.
                </p>
              </div>
            </div>
          </MotionFadeIn>
        )}

        {/* ========================================================= */}
        {/* REVIEW & PLAN SHOWCASE (Tied to track-specific routine)    */}
        {/* ========================================================= */}
        <MotionFadeIn
          aria-label="Coach Review & Goals"
          className="rounded-2xl border border-[#dfcca6] bg-gradient-to-br from-[#fdfbf7] via-[#f9f4ea] to-[#fbf8f0] p-6 shadow-sm"
        >
          <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-6">
            <div className="space-y-2 flex-1">
              <div className="flex flex-wrap items-center gap-2.5">
                <span className="rounded-xs bg-[#1e3a29] px-2.5 py-0.5 text-[9.5px] font-bold uppercase tracking-wider text-white">
                  {trackConfig.label} Blueprint
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
                      ? "Lornette Daye Approved ✓"
                      : activeAthlete.status === "needs_revision"
                      ? "Revision Requested"
                      : activeAthlete.status === "pending_review"
                      ? "Awaiting Coach Review"
                      : "Lornette Daye Reviewed"}
                  </span>
                </span>
              </div>

              <h2 className="font-serif text-xl sm:text-2xl font-semibold text-[#1e1b18]">
                {trackConfig.routineTitle}
              </h2>
              <p className="text-xs font-semibold text-[#7f5b1d] uppercase tracking-wider">
                {trackConfig.routineSubtitle}
              </p>

              {activeAthlete.coachFeedbackNotes ? (
                <p className="font-serif text-sm sm:text-base italic text-[#2c2620] leading-relaxed max-w-2xl">
                  “{activeAthlete.coachFeedbackNotes}”
                </p>
              ) : (
                <p className="text-xs sm:text-sm text-[#706456] italic">
                  Your customized cadence protocol is active. Feedback from Lornette Daye appears here once reviewed.
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
                <span>View {trackConfig.label} Plan →</span>
              </Link>
              <Link
                href="/foundations/grill-me"
                className="inline-flex min-h-11 items-center justify-center gap-2 rounded-lg border border-[#dac8b2] bg-white px-5 py-2.5 text-xs font-semibold text-[#4e4337] hover:bg-[#f4ede1] transition-colors"
              >
                <Flame size={14} className="text-[#b45309]" aria-hidden="true" />
                <span>Simulate {trackConfig.label} Scenarios →</span>
              </Link>
            </div>
          </div>
        </MotionFadeIn>

        {/* ========================================================= */}
        {/* ROW OF 3 BOTTOM FEATURE CARDS                             */}
        {/* ========================================================= */}
        <section aria-label="Portal Highlights">
          <MotionStaggerContainer className="grid grid-cols-1 lg:grid-cols-12 gap-5">
            {/* Card 1: A Message From Lornette (col-span-5) */}
            <MotionStaggerItem className="lg:col-span-5 rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-5 sm:p-6 shadow-[0_2px_12px_rgba(30,24,15,0.03)] flex flex-col justify-between">
              <div>
                <p className="text-[10.5px] font-bold uppercase tracking-[0.22em] text-[#8e7e6e]">
                  A Message From Lornette
                </p>
                <div className="mt-4 flex items-center gap-4 sm:gap-5">
                  <div className="relative h-20 w-20 sm:h-24 sm:w-24 shrink-0 rounded-full overflow-hidden border-2 border-[#dfcca6] shadow-sm">
                    <Image
                      src="/generated/lornette-executive-portrait.jpg"
                      alt="Lornette Daye executive portrait"
                      fill
                      sizes="96px"
                      quality={95}
                      className="object-cover object-top"
                    />
                  </div>
                  <div>
                    <p className="font-serif text-sm sm:text-base italic text-[#2c2620] leading-relaxed">
                      “I’m so glad you’re here. This journey is about more than performance. It is about becoming the strongest version of you. Let’s get started.”
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
            </MotionStaggerItem>

            {/* Card 2: Your Progress Circular Gauge (col-span-3) */}
            <MotionStaggerItem className="lg:col-span-3 rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-5 sm:p-6 shadow-[0_2px_12px_rgba(30,24,15,0.03)] flex flex-col justify-between">
              <p className="text-[10.5px] font-bold uppercase tracking-[0.22em] text-[#5e5245]">
                Your Progress
              </p>

              <div className="my-auto py-4 flex items-center justify-around gap-3">
                {/* Circular Gauge with Motion Animation */}
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
                    <motion.circle
                      cx="50"
                      cy="50"
                      r="40"
                      stroke="#1e3a29"
                      strokeWidth="8"
                      fill="transparent"
                      strokeDasharray="251.2"
                      initial={{ strokeDashoffset: 251.2 }}
                      animate={{ strokeDashoffset }}
                      transition={{ duration: 1.2, ease: [0.22, 1, 0.36, 1], delay: 0.2 }}
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
            </MotionStaggerItem>

            {/* Card 3: Track Atmospheric Visual Card (col-span-4) */}
            <MotionStaggerItem className="lg:col-span-4 rounded-xl border border-[#ebdcc9] bg-[#1e1b18] overflow-hidden shadow-[0_2px_12px_rgba(30,24,15,0.03)] relative min-h-[220px] flex flex-col justify-end">
              <Image
                src={trackConfig.bottomImage}
                alt={trackConfig.heroImageAlt}
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
            </MotionStaggerItem>
          </MotionStaggerContainer>
        </section>

        {/* ========================================================= */}
        {/* LUXURY SIGNATURE BOTTOM BANNER                            */}
        {/* ========================================================= */}
        <MotionFadeIn
          aria-label="Signature Philosophy Banner"
          className="relative overflow-hidden rounded-2xl border border-[#ebdcc9] bg-[#fdfbf7] shadow-[0_2px_16px_rgba(30,24,15,0.03)] min-h-[78px] sm:min-h-[88px] flex items-center justify-between p-3.5 sm:px-8"
        >
          <div className="absolute inset-y-0 left-0 w-2/5 sm:w-1/2 pointer-events-none overflow-hidden">
            <Image
              src={trackConfig.bottomImage}
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
                Elevate Your Performance.
              </p>
            </div>
            <div className="hidden sm:block h-[1px] w-12 sm:w-20 bg-[#dfcca6]" />
            <span className="font-serif text-lg sm:text-3xl italic tracking-wide text-[#8a6828] select-none whitespace-nowrap">
              Lornette Daye
            </span>
          </div>
        </MotionFadeIn>

      </div>

      {/* ========================================================= */}
      {/* GDPR CONSENT MODAL (Accessible from Europe banner)        */}
      {/* ========================================================= */}
      <AnimatePresence>
        {showGdprModal && (
          <motion.div
            role="dialog"
            aria-modal="true"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-xs p-4"
          >
            <motion.div
              initial={{ opacity: 0, scale: 0.95, y: 15 }}
              animate={{ opacity: 1, scale: 1, y: 0 }}
              exit={{ opacity: 0, scale: 0.95, y: 15 }}
              transition={{ duration: 0.25, ease: [0.22, 1, 0.36, 1] }}
              className="w-full max-w-lg rounded-2xl border border-[#dfcca6] bg-[#fbf9f4] p-6 shadow-2xl space-y-4"
            >
              <div className="flex items-center justify-between border-b border-[#ebdcc9] pb-3">
                <div className="flex items-center gap-2">
                  <Globe size={18} className="text-[#0284c7]" />
                  <h3 className="font-serif text-lg font-semibold text-[#1e1b18]">
                    EU GDPR Privacy & Sovereignty Preferences
                  </h3>
                </div>
                <button
                  type="button"
                  onClick={() => setShowGdprModal(false)}
                  className="text-xs text-[#786c5e] hover:text-[#1e1b18] cursor-pointer"
                >
                  ✕ Close
                </button>
              </div>

              <p className="text-xs text-[#5e5245] leading-relaxed">
                In accordance with European Union Regulation (EU) 2016/679 (GDPR), you retain full sovereign ownership over your reflection notes, coaching telemetry, and account data.
              </p>

              <form onSubmit={handleSaveGdpr} className="space-y-3 pt-1">
                <label className="flex items-start gap-3 p-3 rounded-lg border border-[#e5d6be] bg-white cursor-pointer hover:bg-[#fbf9f4]">
                  <input
                    type="checkbox"
                    name="gdpr_analytics"
                    defaultChecked={activeAthlete.gdprConsents?.analytics ?? false}
                    className="mt-0.5 h-4 w-4 rounded border-[#ceb893] text-[#1e3a29] focus:ring-[#8a6828]"
                  />
                  <div className="text-xs">
                    <span className="font-semibold text-[#1e1b18] block">Minimal Session Analytics</span>
                    <span className="text-[#6d6153]">Anonymized performance page-load metrics with zero cross-site tracker pixels.</span>
                  </div>
                </label>

                <label className="flex items-start gap-3 p-3 rounded-lg border border-[#e5d6be] bg-white cursor-pointer hover:bg-[#fbf9f4]">
                  <input
                    type="checkbox"
                    name="gdpr_recordings"
                    defaultChecked={activeAthlete.gdprConsents?.coachingRecordings ?? false}
                    className="mt-0.5 h-4 w-4 rounded border-[#ceb893] text-[#1e3a29] focus:ring-[#8a6828]"
                  />
                  <div className="text-xs">
                    <span className="font-semibold text-[#1e1b18] block">Coaching Call Audio / Reflection Archiving</span>
                    <span className="text-[#6d6153]">Permit Lornette Daye to reference your prior weekly reflection notes during review sessions.</span>
                  </div>
                </label>

                <label className="flex items-start gap-3 p-3 rounded-lg border border-[#e5d6be] bg-white cursor-pointer hover:bg-[#fbf9f4]">
                  <input
                    type="checkbox"
                    name="gdpr_feedback"
                    defaultChecked={activeAthlete.gdprConsents?.peerFeedback ?? false}
                    className="mt-0.5 h-4 w-4 rounded border-[#ceb893] text-[#1e3a29] focus:ring-[#8a6828]"
                  />
                  <div className="text-xs">
                    <span className="font-semibold text-[#1e1b18] block">Anonymized Academy Peer Case Studies</span>
                    <span className="text-[#6d6153]">Allow aggregated anonymous mental recovery stats to be discussed in academy group sessions.</span>
                  </div>
                </label>

                {gdprSuccess && (
                  <div className="rounded-lg bg-[#d1fae5] border border-[#a7f3d0] p-2.5 text-xs text-[#065f46] text-center font-semibold">
                    Privacy preferences updated and logged to Supabase audit trail.
                  </div>
                )}

                <div className="flex items-center justify-end gap-3 pt-3 border-t border-[#ebdcc9]">
                  <button
                    type="button"
                    onClick={() => setShowGdprModal(false)}
                    className="rounded-lg border border-[#cfb78f] px-4 py-2 text-xs font-semibold text-[#4e4337] hover:bg-[#f4ede1] cursor-pointer"
                  >
                    Cancel
                  </button>
                  <button
                    type="submit"
                    disabled={gdprSaving}
                    className="rounded-lg bg-gradient-to-r from-[#dfc385] via-[#ceab68] to-[#b38f4a] px-5 py-2 text-xs font-bold uppercase tracking-wider text-[#1e1b18] shadow-xs hover:brightness-105 disabled:opacity-50 cursor-pointer"
                  >
                    {gdprSaving ? "Saving..." : "Save Preferences"}
                  </button>
                </div>
              </form>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </LearnerShell>
  );
}
