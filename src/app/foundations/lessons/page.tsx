"use client";

import { useState, useEffect } from "react";
import Link from "next/link";
import { LearnerShell } from "@/components/foundations/learner/LearnerShell";
import {
  Check,
  CheckCircle2,
  ChevronRight,
  Flag,
  Sparkles,
  Target,
  TrendingUp,
} from "lucide-react";

import { useFoundationsStore } from "@/lib/foundations/store";
import {
  saveOfflineDraft,
  getOfflineDraft,
  clearOfflineDraft,
  queueReflectionSync,
  flushOutboxSync,
} from "@/lib/foundations/offline-store";

type FoundationLesson = {
  id: number;
  title: string;
  foundation: string;
  duration: string;
  description: string;
  tool: string;
  reflectionPrompt: string;
};

const CANONICAL_LESSONS: FoundationLesson[] = [
  {
    id: 1,
    title: "Welcome & Identity Beyond Sport",
    foundation: "Foundation 1: Identity Beyond Sport",
    duration: "3 min",
    description: "Meet Lornette and discover what's possible when you ground your athletic identity beyond the scoreboard. Learn why who you are drives how you play.",
    tool: "Athlete Identity Audit",
    reflectionPrompt: "When you step off the 18th green after a difficult round, what reminds you of your worth beyond your score?",
  },
  {
    id: 2,
    title: "Champion Mindset & Mental Focus",
    foundation: "Foundation 2: Champion Mindset",
    duration: "14 min",
    description: "Build the unshakable mental focus required for championship golf. Train your attention to lock onto what you can control and discard peripheral distractions.",
    tool: "Focus Calibration Drill",
    reflectionPrompt: "What is your primary distraction during competitive play, and what sensory anchor brings you back to the present?",
  },
  {
    id: 3,
    title: "Discipline Systems & Pre-Shot Cadence",
    foundation: "Foundation 3: Discipline Systems",
    duration: "18 min",
    description: "Consistency isn't talent; it's systems. Build a repeatable 6-step pre-shot routine that insulates your swing mechanics from tournament nerves.",
    tool: "6-Step Pre-Shot Protocol",
    reflectionPrompt: "Where in your pre-shot routine do you tend to rush when feeling pressured?",
  },
  {
    id: 4,
    title: "Resilience After Setback & Mistake Reset",
    foundation: "Foundation 4: Resilience After Setback",
    duration: "16 min",
    description: "Master the Next-Shot Principle. Discover Lornette's 5-second physical reset protocol to clear double-bogeys before stepping onto the next tee box.",
    tool: "5-Second Physical Reset",
    reflectionPrompt: "What physical gesture or breath cadence allows you to definitively let go of a poor shot?",
  },
  {
    id: 5,
    title: "Pressure, Emotional Regulation & Recovery",
    foundation: "Foundation 5: Pressure, Emotional Regulation & Recovery",
    duration: "20 min",
    description: "Learn how to stay centered, make calm decisions under pressure, and regulate physiological heart rate spikes in high-stakes matches.",
    tool: "Physiological Sigh & Heart Rate Regulation",
    reflectionPrompt: "What changes in your body and thoughts when the score matters most?",
  },
  {
    id: 6,
    title: "Communication & Presence",
    foundation: "Foundation 6: Communication & Presence",
    duration: "15 min",
    description: "Elevate your self-talk, coach interactions, and body language. Your presence on the fairways communicates certainty to yourself and your competitors.",
    tool: "Internal Dialogue Script",
    reflectionPrompt: "What negative phrase do you catch yourself repeating on difficult holes, and what will you replace it with?",
  },
  {
    id: 7,
    title: "Family & Community Support",
    foundation: "Foundation 7: Family & Community Support",
    duration: "12 min",
    description: "Align your inner circle, manage expectations, and create an emotional sanctuary that supports sustained athletic longevity.",
    tool: "Support Alignment Canvas",
    reflectionPrompt: "How can you best communicate your competitive boundaries to family and support networks during tournament weeks?",
  },
  {
    id: 8,
    title: "Career & Money Readiness",
    foundation: "Foundation 8: Career & Money Readiness",
    duration: "17 min",
    description: "Equip yourself with long-term financial wisdom, sponsorship readiness, and career balance to thrive through all competitive transitions.",
    tool: "Financial & Transition Roadmap",
    reflectionPrompt: "What financial or career habits would give you greater peace of mind while focusing on competition?",
  },
  {
    id: 9,
    title: "Personal Brand & Story",
    foundation: "Foundation 9: Personal Brand & Story",
    duration: "14 min",
    description: "Articulate your personal narrative, values, and leadership voice. Build a reputation that commands respect across clubs and communities.",
    tool: "Story & Values Matrix",
    reflectionPrompt: "If a young golfer watched you compete for 18 holes, what values would they observe in your behavior?",
  },
  {
    id: 10,
    title: "Legacy & Community Impact",
    foundation: "Foundation 10: Legacy & Community Impact",
    duration: "15 min",
    description: "Define your lasting contribution. Giving back through mentorship and community elevates your purpose and sustains true fulfillment in the game.",
    tool: "Legacy Blueprint",
    reflectionPrompt: "How will you use the lessons and confidence gained in golf to lift others in your community?",
  },
];

export default function FoundationsLessonsPage() {
  const { activeAthlete, saveReflection } = useFoundationsStore();
  const [activeLessonId, setActiveLessonId] = useState<number>(3);
  const [isPlaying, setIsPlaying] = useState(false);
  const [progress, setProgress] = useState(38); // 38%
  const [showSubtitles, setShowSubtitles] = useState(true);
  const [isMuted, setIsMuted] = useState(false);
  const [isFullscreen, setIsFullscreen] = useState(false);

  // Initialize reflection from activeAthlete store or localStorage draft
  const existingReflection = activeAthlete.reflections[activeLessonId];
  const [reflectionNotice, setReflectionNotice] = useState(
    existingReflection?.noticed || ""
  );
  const [reflectionWorked, setReflectionWorked] = useState(
    existingReflection?.worked || ""
  );
  const [reflectionRepeat, setReflectionRepeat] = useState(
    existingReflection?.repeated || ""
  );
  const [savedStatus, setSavedStatus] = useState<string | null>(null);
  const [draftStatus, setDraftStatus] = useState<string | null>(null);

  // Restore unsaved draft from IndexedDB (or localStorage fallback) if no saved reflection or draft is newer
  useEffect(() => {
    let isMounted = true;
    const athleteCohort = (activeAthlete as { cohortId?: string })?.cohortId || null;
    getOfflineDraft(activeAthlete.id, activeLessonId, athleteCohort).then((draft) => {
      if (!isMounted || !draft) return;
      const draftTime = draft.updatedAt ? new Date(draft.updatedAt).getTime() : 0;
      const serverTime = existingReflection?.updatedAt ? new Date(existingReflection.updatedAt).getTime() : 0;
      const hasDraft = Boolean(draft.noticed?.trim() || draft.worked?.trim() || draft.repeated?.trim());
      const hasServer = Boolean(
        existingReflection?.noticed?.trim() ||
        existingReflection?.worked?.trim() ||
        existingReflection?.repeated?.trim()
      );

      if (hasDraft && (!hasServer || draftTime > serverTime)) {
        if (draft.noticed) setReflectionNotice(draft.noticed);
        if (draft.worked) setReflectionWorked(draft.worked);
        if (draft.repeated) setReflectionRepeat(draft.repeated);
        setDraftStatus("Draft restored from this device");
        setTimeout(() => {
          if (isMounted) setDraftStatus(null);
        }, 3500);
      }
    });
    return () => {
      isMounted = false;
    };
  }, [activeAthlete.id, activeLessonId, existingReflection]);

  // Debounced auto-save draft to IndexedDB on input change (750ms)
  useEffect(() => {
    if (typeof window === "undefined") return;
    const athleteCohort = (activeAthlete as { cohortId?: string })?.cohortId || null;
    const hasContent = reflectionNotice.trim() || reflectionWorked.trim() || reflectionRepeat.trim();
    if (!hasContent) {
      clearOfflineDraft(activeAthlete.id, activeLessonId, athleteCohort);
      return;
    }

    const timeout = setTimeout(async () => {
      setDraftStatus("Saving...");
      await saveOfflineDraft(
        activeAthlete.id,
        activeLessonId,
        CANONICAL_LESSONS.find((l) => l.id === activeLessonId)?.foundation || "",
        reflectionNotice,
        reflectionWorked,
        reflectionRepeat,
        athleteCohort
      );
      const isOnline = typeof navigator !== "undefined" ? navigator.onLine : true;
      setDraftStatus(isOnline ? "Draft saved on this device" : "Offline - draft protected");
    }, 750);

    return () => clearTimeout(timeout);
  }, [reflectionNotice, reflectionWorked, reflectionRepeat, activeAthlete, activeLessonId]);

  // Sync reflection state when active athlete persona switches
  const [prevAthleteId, setPrevAthleteId] = useState(activeAthlete.id);
  if (activeAthlete.id !== prevAthleteId) {
    setPrevAthleteId(activeAthlete.id);
    const ref = activeAthlete.reflections[activeLessonId];
    setReflectionNotice(ref?.noticed || "");
    setReflectionWorked(ref?.worked || "");
    setReflectionRepeat(ref?.repeated || "");
    setDraftStatus(null);
    setSavedStatus(null);
  }

  // When lesson changes, populate reflection fields or cached draft from IndexedDB
  const handleSelectLesson = async (lessonId: number) => {
    setActiveLessonId(lessonId);
    setProgress(0);
    setIsPlaying(false);
    setDraftStatus(null);
    setSavedStatus(null);
    const athleteCohort = (activeAthlete as { cohortId?: string })?.cohortId || null;
    const ref = activeAthlete.reflections[lessonId];
    const draft = await getOfflineDraft(activeAthlete.id, lessonId, athleteCohort);
    const draftTime = draft?.updatedAt ? new Date(draft.updatedAt).getTime() : 0;
    const serverTime = ref?.updatedAt ? new Date(ref.updatedAt).getTime() : 0;

    if (draft && (draft.noticed || draft.worked || draft.repeated) && (!ref || draftTime > serverTime)) {
      setReflectionNotice(draft.noticed || "");
      setReflectionWorked(draft.worked || "");
      setReflectionRepeat(draft.repeated || "");
      setDraftStatus("Draft restored from this device");
      setTimeout(() => setDraftStatus(null), 3000);
    } else if (ref && (ref.noticed || ref.worked || ref.repeated)) {
      setReflectionNotice(ref.noticed);
      setReflectionWorked(ref.worked);
      setReflectionRepeat(ref.repeated);
    } else {
      setReflectionNotice("");
      setReflectionWorked("");
      setReflectionRepeat("");
    }
  };

  const activeLesson =
    CANONICAL_LESSONS.find((l) => l.id === activeLessonId) ||
    CANONICAL_LESSONS[2];

  const handleTogglePlay = () => {
    setIsPlaying(!isPlaying);
  };

  const handleSaveReflection = async (e?: React.FormEvent) => {
    if (e && typeof e.preventDefault === "function") {
      e.preventDefault();
    }
    setDraftStatus(null);
    setSavedStatus("Saving...");

    const athleteCohort = (activeAthlete as { cohortId?: string })?.cohortId || null;

    // Update local reactive store
    saveReflection(
      activeLesson.id,
      activeLesson.foundation,
      reflectionNotice,
      reflectionWorked,
      reflectionRepeat
    );

    const isOnline = typeof navigator !== "undefined" ? navigator.onLine : true;

    if (!isOnline) {
      await queueReflectionSync(
        activeAthlete.id,
        activeLesson.id,
        activeLesson.foundation,
        reflectionNotice,
        reflectionWorked,
        reflectionRepeat
      );
      // Queued in durable offline store outbox, safe to clear working draft
      await clearOfflineDraft(activeAthlete.id, activeLesson.id, athleteCohort);
      setSavedStatus("Saved to device (Offline mode). Queued to sync when back online.");
    } else {
      try {
        await queueReflectionSync(
          activeAthlete.id,
          activeLesson.id,
          activeLesson.foundation,
          reflectionNotice,
          reflectionWorked,
          reflectionRepeat
        );
        const syncResult = await flushOutboxSync();
        if (syncResult.remaining === 0) {
          // Success: delete local draft only after verified server save
          await clearOfflineDraft(activeAthlete.id, activeLesson.id, athleteCohort);
          setSavedStatus("Reflection saved to your Performance Edge Plan.");
        } else {
          setSavedStatus("Reflection saved to device. Queued for cloud sync.");
        }
      } catch {
        // Network or server failure: draft remains preserved in client storage
        setSavedStatus("Saved locally. Queued for background sync.");
      }
    }

    setTimeout(() => {
      setSavedStatus(null);
    }, 4500);
  };

  return (
    <LearnerShell>
      <div className="p-4 sm:p-6 lg:p-8 max-w-7xl mx-auto space-y-6">
        {/* ========================================================= */}
        {/* TOP HEADER EYEBROW & TITLE (Matches Mockup 4)             */}
        {/* ========================================================= */}
        <div className="flex flex-col md:flex-row md:items-end justify-between gap-4 border-b border-[#ebdcc9] pb-4">
          <div>
            <p className="font-sans text-[11px] font-bold uppercase tracking-[0.28em] text-[#8e7e6e]">
              YOUR JOURNEY STARTS HERE
            </p>
            <div className="flex items-baseline gap-3 mt-1">
              <h1 className="font-serif text-3xl sm:text-4xl font-semibold tracking-tight text-[#1e1b18]">
                WELCOME, GOLFER
              </h1>
              <span className="font-serif text-lg sm:text-xl italic text-[#b89456]">
                Begin with Lornette.
              </span>
            </div>
          </div>

          <div className="text-right">
            <p className="font-serif text-sm italic text-[#7a6f62]">
              A More Focused You. A Stronger Game.
            </p>
            <div className="mt-1 flex items-center justify-end gap-2 text-xs font-semibold text-[#1e3a29]">
              <span className="h-2 w-2 rounded-full bg-[#1e3a29]" />
              <span>Foundation {activeLesson.id} of 10</span>
            </div>
          </div>
        </div>

        {/* ========================================================= */}
        {/* MAIN COURSE PLAYER + RIGHT CURRICULUM RAIL                */}
        {/* ========================================================= */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          {/* Left / Center: Interactive Video Player & Lesson Details */}
          <div className="lg:col-span-8 space-y-4">
            {/* Interactive Player Frame */}
            <div className="relative overflow-hidden rounded-xl border border-[#dfcca6] bg-[#1a1715] shadow-[0_6px_28px_rgba(30,24,15,0.08)]">
              <div className="relative aspect-video w-full">
                {/* Real Accessible Video Player */}
                <video
                  className="h-full w-full object-cover"
                  controls
                  poster="/foundations/golf/lornette-golf-simulator-studio-tablet.png"
                  onPlay={() => setIsPlaying(true)}
                  onPause={() => setIsPlaying(false)}
                  onTimeUpdate={(e) => {
                    const el = e.currentTarget;
                    if (el.duration) {
                      setProgress(Math.round((el.currentTime / el.duration) * 100));
                    }
                  }}
                  aria-label="Foundation Lesson Video Player"
                >
                  <source src="/videos/lesson-placeholder.mp4" type="video/mp4" />
                  <track
                    kind="captions"
                    src="/captions/lesson-en.vtt"
                    srcLang="en"
                    label="English"
                    default
                  />
                  Your browser does not support the video tag.
                </video>
              </div>
            </div>

            {/* Sub-Player Metadata Card (Matches Mockup 4 bottom left card) */}
            <div className="rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-5 sm:p-6 shadow-[0_2px_12px_rgba(30,24,15,0.03)] flex flex-col md:flex-row md:items-center justify-between gap-5">
              <div className="space-y-1.5">
                <p className="text-[10.5px] font-bold uppercase tracking-[0.24em] text-[#8e7e6e]">
                  LESSON {activeLesson.id}
                </p>
                <h2 className="font-serif text-xl sm:text-2xl font-semibold tracking-tight text-[#1e1b18]">
                  {activeLesson.title}
                </h2>
                <p className="text-xs sm:text-sm text-[#665a4c] max-w-xl leading-relaxed">
                  {activeLesson.description}
                </p>
                <div className="pt-2 flex flex-wrap items-center gap-3 text-xs text-[#7a6f62]">
                  <span className="font-semibold text-[#1e1b18]">{activeLesson.duration}</span>
                  <span>•</span>
                  <span>Video Lesson</span>
                  <span>•</span>
                  <span className="inline-flex items-center gap-1 text-[#1e3a29] font-medium">
                    <Target size={13} aria-hidden="true" />
                    {activeLesson.tool}
                  </span>
                </div>
              </div>

              <div className="shrink-0">
                <button
                  type="button"
                  onClick={handleTogglePlay}
                  className="inline-flex min-h-11 items-center gap-2 rounded-lg bg-gradient-to-r from-[#dfc385] via-[#ceab68] to-[#b38f4a] px-6 py-3 text-xs font-bold uppercase tracking-[0.16em] text-[#1e1b18] shadow-sm hover:brightness-105 active:brightness-95 transition-all focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#ba934d]"
                >
                  <span>{isPlaying ? "Pause Lesson" : "Watch Lesson >"}</span>
                </button>
              </div>
            </div>

            {/* Interactive Reflection Card (Matches Mockup 2 reflection module) */}
            <div className="rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-5 sm:p-6 shadow-[0_2px_12px_rgba(30,24,15,0.03)] space-y-4">
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-2">
                  <Sparkles size={16} className="text-[#7f5b1d]" aria-hidden="true" />
                  <p className="text-[10.5px] font-bold uppercase tracking-[0.22em] text-[#5e5245]">
                    Weekly Athlete Reflection
                  </p>
                </div>
                <span className="text-[11px] font-semibold text-[#1e3a29]">
                  Foundation {activeLesson.id} Exercise
                </span>
              </div>

              <h3 className="font-serif text-base sm:text-lg italic text-[#1e1b18]">
                “{activeLesson.reflectionPrompt}”
              </h3>

              <div className="space-y-4">
                <div className="space-y-3">
                  <div>
                    <label htmlFor="reflection-notice" className="block text-[11px] font-bold uppercase tracking-wider text-[#4e4337] mb-1">
                      1. What Did You Notice?
                    </label>
                    <textarea
                      id="reflection-notice"
                      rows={2}
                      value={reflectionNotice}
                      onChange={(e) => setReflectionNotice(e.target.value)}
                      placeholder="Observations on your tempo, breathing, or inner dialogue..."
                      className="w-full rounded-md border border-[#dac8b2] bg-white p-2.5 text-xs sm:text-sm text-[#1e1b18] placeholder-[#756756] shadow-xs focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)] focus:border-[var(--gold-dark)]"
                    />
                  </div>

                  <div>
                    <label htmlFor="reflection-worked" className="block text-[11px] font-bold uppercase tracking-wider text-[#4e4337] mb-1">
                      2. What Worked?
                    </label>
                    <textarea
                      id="reflection-worked"
                      rows={2}
                      value={reflectionWorked}
                      onChange={(e) => setReflectionWorked(e.target.value)}
                      placeholder="Techniques, cues, or reset habits that produced composure..."
                      className="w-full rounded-md border border-[#dac8b2] bg-white p-2.5 text-xs sm:text-sm text-[#1e1b18] placeholder-[#756756] shadow-xs focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)] focus:border-[var(--gold-dark)]"
                    />
                  </div>

                  <div>
                    <label htmlFor="reflection-repeat" className="block text-[11px] font-bold uppercase tracking-wider text-[#4e4337] mb-1">
                      3. What Will You Repeat?
                    </label>
                    <textarea
                      id="reflection-repeat"
                      rows={2}
                      value={reflectionRepeat}
                      onChange={(e) => setReflectionRepeat(e.target.value)}
                      placeholder="The signature habit or routine cue you will take into your next round..."
                      className="w-full rounded-md border border-[#dac8b2] bg-white p-2.5 text-xs sm:text-sm text-[#1e1b18] placeholder-[#756756] shadow-xs focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)] focus:border-[var(--gold-dark)]"
                    />
                  </div>
                </div>

                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pt-1">
                  <div role="status" aria-live="polite" aria-atomic="true">
                    {savedStatus ? (
                      <span className="inline-flex items-center gap-1.5 text-xs font-semibold text-[#1e3a29]">
                        <CheckCircle2 size={15} aria-hidden="true" />
                        <span>{savedStatus}</span>
                      </span>
                    ) : draftStatus ? (
                      <span className="inline-flex items-center gap-1.5 text-xs font-medium text-[#8a6828]">
                        <Sparkles size={13} aria-hidden="true" className="text-[#b89456]" />
                        <span>{draftStatus}</span>
                      </span>
                    ) : (
                      <span className="text-xs text-[#5e5245]">
                        Responses are private to you and reviewed by Coach Lornette Daye.
                      </span>
                    )}
                  </div>

                  <button
                    type="button"
                    onClick={() => handleSaveReflection()}
                    className="inline-flex min-h-11 items-center justify-center gap-2 rounded-md bg-gradient-to-r from-[#dfc385] via-[#ceab68] to-[#b38f4a] px-5 py-2.5 text-xs font-bold uppercase tracking-[0.14em] text-[#1e1b18] shadow-xs hover:brightness-105 transition-all focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)]"
                  >
                    <span>Save Reflection</span>
                    <ChevronRight size={15} aria-hidden="true" />
                  </button>
                </div>
              </div>
            </div>
          </div>

          {/* Right Rail: 10-Foundation Playlist & Progress (Matches Mockup 4 right rail) */}
          <aside aria-label="Curriculum Foundations Playlist" className="lg:col-span-4 rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-5 sm:p-6 shadow-[0_2px_12px_rgba(30,24,15,0.03)] space-y-6">
            {/* Top Progress Meter */}
            <div>
              <p className="text-[10.5px] font-bold uppercase tracking-[0.24em] text-[#5e5245]">
                YOUR PROGRESS
              </p>
              <div className="mt-4 flex items-center gap-4">
                {/* Circular Gauge */}
                <div
                  role="progressbar"
                  aria-valuenow={Math.round((activeAthlete.completedFoundations.length / 10) * 100)}
                  aria-valuemin={0}
                  aria-valuemax={100}
                  aria-label="Foundations curriculum completion progress"
                  className="relative flex items-center justify-center"
                >
                  {(() => {
                    const completedPct = Math.round(
                      (activeAthlete.completedFoundations.length / 10) * 100
                    );
                    const strokeDashoffset =
                      251.2 - (251.2 * completedPct) / 100;
                    return (
                      <>
                        <svg
                          aria-hidden="true"
                          className="w-16 h-16 -rotate-90 transform"
                          viewBox="0 0 100 100"
                        >
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
                        <span className="absolute font-serif text-sm font-bold text-[#1e1b18]">
                          {completedPct}%
                        </span>
                      </>
                    );
                  })()}
                </div>

                <div>
                  <h3 className="font-serif text-lg font-semibold text-[#1e1b18] leading-tight">
                    Step {activeLesson.id} of 10
                  </h3>
                  <p className="text-[10px] font-bold uppercase tracking-[0.18em] text-[#8a6828]">
                    LET’S GET STARTED
                  </p>
                </div>
              </div>
              <div className="mt-3 h-[1px] w-12 bg-[#dfcca6]" />
            </div>

            {/* 10-Week Ordered Playlist */}
            <div className="space-y-1.5">
              {CANONICAL_LESSONS.map((lesson) => {
                const isActive = lesson.id === activeLessonId;
                const isCompleted =
                  activeAthlete.completedFoundations.includes(lesson.id);
                return (
                  <button
                    key={lesson.id}
                    type="button"
                    onClick={() => handleSelectLesson(lesson.id)}
                    className={`w-full text-left flex items-center gap-3.5 rounded-lg p-2.5 transition-all duration-150 ${
                      isActive
                        ? "bg-[#e8dbbf]/60 border border-[#dfcca6] shadow-xs"
                        : "hover:bg-[#f4ede1]"
                    }`}
                  >
                    {/* Number Badge */}
                    <div
                      className={`flex h-8 w-8 shrink-0 items-center justify-center rounded-full text-xs font-serif font-bold ${
                        isActive
                          ? "bg-[#b89456] text-white shadow-xs"
                          : isCompleted
                          ? "bg-[#1e3a29] text-white"
                          : "bg-[#ede4d5] text-[#5e5346]"
                      }`}
                    >
                      {isCompleted && !isActive ? (
                        <Check size={14} />
                      ) : (
                        lesson.id
                      )}
                    </div>

                    <div className="min-w-0 flex-1">
                      <p
                        className={`text-xs font-serif font-semibold truncate ${
                          isActive ? "text-[#1e1b18]" : "text-[#4d4337]"
                        }`}
                      >
                        {lesson.title}
                      </p>
                      <p className="text-[10px] text-[#8e7e6e]">
                        {lesson.duration} • Video Lesson
                      </p>
                    </div>

                    {isActive && (
                      <span className="text-[9.5px] font-bold uppercase tracking-wider text-[#b89456] shrink-0">
                        Playing
                      </span>
                    )}
                  </button>
                );
              })}
            </div>

            {/* Script Signature Plaque */}
            <div className="pt-4 border-t border-[#ebdcc9]/60 text-center">
              <p className="font-serif text-2xl italic tracking-wide text-[#b89456] select-none">
                Progress Looks Good on You.
              </p>
              <div className="mx-auto mt-2 h-[1px] w-8 bg-[#dfcca6]" />
            </div>
          </aside>
        </div>

        {/* ========================================================= */}
        {/* BOTTOM 3 CAPABILITY CARDS (Matches Mockup 4 & Mockup 2)   */}
        {/* ========================================================= */}
        <section aria-label="Program Capabilities" className="grid grid-cols-1 md:grid-cols-3 gap-4 pt-2">
          {/* Card 1: Better Skills */}
          <div className="rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-5 shadow-[0_2px_12px_rgba(30,24,15,0.03)] flex items-center gap-4">
            <div className="flex h-12 w-12 shrink-0 items-center justify-center rounded-full bg-[#f4ebe0] text-[#1e3a29]">
              <Target size={22} strokeWidth={1.75} aria-hidden="true" />
            </div>
            <div>
              <h3 className="font-serif text-sm font-bold uppercase tracking-wider text-[#1e1b18]">
                Better Skills
              </h3>
              <p className="text-xs text-[#706456]">
                Play with confidence.
              </p>
            </div>
          </div>

          {/* Card 2: Stronger Mindset */}
          <div className="rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-5 shadow-[0_2px_12px_rgba(30,24,15,0.03)] flex items-center gap-4">
            <div className="flex h-12 w-12 shrink-0 items-center justify-center rounded-full bg-[#f4ebe0] text-[#1e3a29]">
              <Sparkles size={22} strokeWidth={1.75} aria-hidden="true" />
            </div>
            <div>
              <h3 className="font-serif text-sm font-bold uppercase tracking-wider text-[#1e1b18]">
                Stronger Mindset
              </h3>
              <p className="text-xs text-[#706456]">
                Stay calm. Stay present.
              </p>
            </div>
          </div>

          {/* Card 3: Real Results */}
          <div className="rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-5 shadow-[0_2px_12px_rgba(30,24,15,0.03)] flex items-center gap-4">
            <div className="flex h-12 w-12 shrink-0 items-center justify-center rounded-full bg-[#f4ebe0] text-[#1e3a29]">
              <TrendingUp size={22} strokeWidth={1.75} aria-hidden="true" />
            </div>
            <div>
              <h3 className="font-serif text-sm font-bold uppercase tracking-wider text-[#1e1b18]">
                Real Results
              </h3>
              <p className="text-xs text-[#706456]">
                A stronger you on and off the course.
              </p>
            </div>
          </div>
        </section>

        {/* ========================================================= */}
        {/* BOTTOM DOCKED STRIP (Matches Mockup 2 bottom bar)         */}
        {/* ========================================================= */}
        <section
          aria-label="Training Calm Principle Banner"
          className="rounded-xl border border-[#dfcca6] bg-[#fdfbf7] p-4 sm:p-5 flex flex-col sm:flex-row items-center justify-between gap-4 shadow-xs"
        >
          <div className="flex items-center gap-3.5">
            <div className="flex h-11 w-11 shrink-0 items-center justify-center rounded-full bg-[#f4ebe0] text-[#a6864a]">
              <Flag size={20} strokeWidth={1.75} aria-hidden="true" />
            </div>
            <div>
              <p className="font-serif text-xs sm:text-sm font-semibold tracking-wide text-[#1e1b18]">
                “The same calm you practice in training is the calm that shows up in the moments that matter.”
              </p>
              <p className="text-[11px] font-bold uppercase tracking-[0.2em] text-[#a6864a] mt-0.5">
                Coach Lornette Daye
              </p>
            </div>
          </div>

          <Link
            href="/foundations/plan"
            className="inline-flex items-center gap-2 rounded-full bg-gradient-to-r from-[#dfc385] via-[#ceab68] to-[#b38f4a] px-6 py-2.5 text-xs font-bold uppercase tracking-[0.16em] text-white shadow-xs hover:brightness-105 active:brightness-95 transition-all shrink-0 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[#ba934d]"
          >
            <span>Review My Plan</span>
            <ChevronRight size={15} aria-hidden="true" />
          </Link>
        </section>
      </div>
    </LearnerShell>
  );
}
