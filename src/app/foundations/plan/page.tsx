"use client";

import { useState } from "react";
import Link from "next/link";
import { LearnerShell } from "@/components/foundations/learner/LearnerShell";
import {
  Check,
  CheckCircle2,
  Compass,
  FileDown,
  Flame,
  Plus,
  Save,
  ShieldAlert,
  ShieldCheck,
  Sparkles,
  Target,
  Trash2,
} from "lucide-react";
import { useFoundationsStore, GoalItem } from "@/lib/foundations/store";

export default function FoundationsPlanPage() {
  const { activeAthlete, updateActivePlan } = useFoundationsStore();

  const [prevAthleteId, setPrevAthleteId] = useState(activeAthlete.id);
  const [pressureSignal, setPressureSignal] = useState(activeAthlete.pressureSignal);
  const [resetProtocol, setResetProtocol] = useState(activeAthlete.resetProtocol);
  const [anchorCue, setAnchorCue] = useState(activeAthlete.anchorCue);
  const [goals, setGoals] = useState<GoalItem[]>(activeAthlete.goals);
  const [newGoalText, setNewGoalText] = useState("");
  const [isSaved, setIsSaved] = useState(false);

  // Sync state when activeAthlete changes
  if (prevAthleteId !== activeAthlete.id) {
    setPrevAthleteId(activeAthlete.id);
    setPressureSignal(activeAthlete.pressureSignal);
    setResetProtocol(activeAthlete.resetProtocol);
    setAnchorCue(activeAthlete.anchorCue);
    setGoals(activeAthlete.goals);
  }

  const handleToggleGoal = (id: string) => {
    const updated = goals.map((g) =>
      g.id === id ? { ...g, completed: !g.completed } : g
    );
    setGoals(updated);
  };

  const handleAddGoal = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newGoalText.trim()) return;
    const newGoal: GoalItem = {
      id: `goal-${Date.now()}`,
      text: newGoalText.trim(),
      completed: false,
    };
    setGoals([...goals, newGoal]);
    setNewGoalText("");
  };

  const handleRemoveGoal = (id: string) => {
    setGoals(goals.filter((g) => g.id !== id));
  };

  const handleSave = (e: React.FormEvent) => {
    e.preventDefault();
    updateActivePlan({
      pressureSignal,
      resetProtocol,
      anchorCue,
      goals,
    });
    setIsSaved(true);
    setTimeout(() => setIsSaved(false), 4000);
  };

  const handleExportPdf = () => {
    window.print();
  };

  return (
    <LearnerShell>
      <div className="p-4 sm:p-6 lg:p-8 max-w-7xl mx-auto space-y-6">
        {/* Top Header */}
        <section className="relative overflow-hidden rounded-2xl border border-[#dfcca6] bg-[#fbf9f4] p-6 sm:p-8 shadow-[0_4px_24px_rgba(30,24,15,0.04)]">
          <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
            <div>
              <p className="font-sans text-[11px] font-bold uppercase tracking-[0.28em] text-[#8e7e6e]">
                INDIVIDUAL ATHLETE BLUEPRINT
              </p>
              <h1 className="mt-1 font-serif text-3xl sm:text-4xl font-semibold tracking-tight text-[#1e1b18]">
                My Performance Edge Plan
              </h1>
              <p className="mt-2 font-sans text-xs sm:text-sm text-[#665a4c] max-w-xl leading-relaxed">
                Your personalized competitive blueprint, reset cues, pre-shot routine cadence, and 30-day performance commitments.
              </p>
            </div>

            <div className="flex flex-col sm:flex-row items-start sm:items-center gap-3">
              <div
                className={`inline-flex items-center gap-2 rounded-full border px-3.5 py-1.5 text-xs font-semibold shadow-xs ${
                  activeAthlete.status === "approved"
                    ? "bg-[#e8f5ec] text-[#1e3a29] border-[#b8dfc4]"
                    : activeAthlete.status === "needs_revision"
                    ? "bg-[#fef3c7] text-[#92400e] border-[#fde68a]"
                    : activeAthlete.status === "pending_review"
                    ? "bg-[#eff6ff] text-[#1e40af] border-[#bfdbfe]"
                    : "bg-[#f5ede2] text-[#1e3a29] border-[rgba(198,165,92,0.4)]"
                }`}
              >
                {activeAthlete.status === "approved" ? (
                  <CheckCircle2 size={15} className="text-[#1e3a29]" />
                ) : activeAthlete.status === "needs_revision" ? (
                  <ShieldAlert size={15} className="text-[#92400e]" />
                ) : (
                  <ShieldCheck size={15} className="text-[#1e3a29]" />
                )}
                <span>
                  {activeAthlete.status === "approved"
                    ? "Coach Lornette Daye Approved ✓"
                    : activeAthlete.status === "needs_revision"
                    ? "Revision Requested by Coach Lornette"
                    : activeAthlete.status === "pending_review"
                    ? "Awaiting Coach Lornette Review"
                    : "Coach Lornette Daye Reviewed"}
                </span>
              </div>

              <button
                type="button"
                onClick={handleExportPdf}
                className="inline-flex items-center gap-1.5 rounded-sm bg-[#1e3a29] px-3.5 py-1.5 text-xs font-bold text-white hover:bg-[#274d36] transition-colors cursor-pointer"
              >
                <FileDown size={14} />
                <span>Export PDF</span>
              </button>
            </div>
          </div>
        </section>

        {/* Grill-Me Pressure Test Teaser Banner */}
        <section className="rounded-xl border border-[#dfcca6] bg-gradient-to-r from-[#fbf9f4] via-[#f7f0e4] to-[#fbf9f4] p-4 sm:p-5 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 shadow-xs">
          <div className="flex items-center gap-3">
            <div className="flex h-10 w-10 shrink-0 items-center justify-center rounded-full bg-[#1e3a29] text-[#dfc385]">
              <Flame size={20} />
            </div>
            <div>
              <h3 className="font-serif text-sm sm:text-base font-semibold text-[#1e1b18]">
                Test Your Reset Protocol: Coach Lornette&apos;s Grill-Me Challenge
              </h3>
              <p className="text-xs text-[#6d6153]">
                Put your 5-second reset protocol through authentic tournament pressure scenarios (water left, OB right, downhill putts).
              </p>
            </div>
          </div>

          <Link
            href="/foundations/grill-me"
            className="inline-flex items-center gap-1.5 rounded-md bg-[#1e3a29] px-4 py-2 text-xs font-bold text-white hover:bg-[#274d36] shrink-0 transition-colors"
          >
            <span>Take Grill-Me Audit →</span>
          </Link>
        </section>

        {/* Plan Editor & Canvas */}
        <form onSubmit={handleSave} className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          {/* Main Blueprint Form (col-span-8) */}
          <div className="lg:col-span-8 space-y-6">
            {/* Section 1: Pressure Signal & Reset Protocol */}
            <div className="rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-6 shadow-[0_2px_12px_rgba(30,24,15,0.03)] space-y-4">
              <div className="flex items-center gap-2 border-b border-[#ebdcc9] pb-3">
                <Target size={18} className="text-[#a6864a]" />
                <h2 className="font-serif text-lg font-semibold text-[#1e1b18]">
                  1. Pressure Signal & 5-Second Reset Protocol
                </h2>
              </div>

              <div>
                <label className="block text-xs font-bold uppercase tracking-wider text-[#4e4337] mb-1.5">
                  My Primary Pressure Signal (Physical & Mental)
                </label>
                <input
                  type="text"
                  value={pressureSignal}
                  onChange={(e) => setPressureSignal(e.target.value)}
                  className="w-full rounded-md border border-[#dac8b2] bg-white p-3 text-xs sm:text-sm text-[#1e1b18] shadow-xs focus:border-[var(--gold-dark)] focus:outline-none"
                />
              </div>

              <div>
                <label className="block text-xs font-bold uppercase tracking-wider text-[#4e4337] mb-1.5">
                  My 5-Second Physical Reset Sequence
                </label>
                <textarea
                  rows={2}
                  value={resetProtocol}
                  onChange={(e) => setResetProtocol(e.target.value)}
                  className="w-full rounded-md border border-[#dac8b2] bg-white p-3 text-xs sm:text-sm text-[#1e1b18] shadow-xs focus:border-[var(--gold-dark)] focus:outline-none leading-relaxed"
                />
              </div>
            </div>

            {/* Section 2: 6-Step Pre-Shot Routine Cadence */}
            <div className="rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-6 shadow-[0_2px_12px_rgba(30,24,15,0.03)] space-y-4">
              <div className="flex items-center gap-2 border-b border-[#ebdcc9] pb-3">
                <Compass size={18} className="text-[#a6864a]" />
                <h2 className="font-serif text-lg font-semibold text-[#1e1b18]">
                  2. Repeatable 6-Step Pre-Shot Cadence
                </h2>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {activeAthlete.preShotRoutine.map((s) => (
                  <div
                    key={s.step}
                    className="rounded-lg border border-[#ebdcc9] bg-[#fcfaf5] p-3.5"
                  >
                    <span className="text-[10px] font-bold uppercase tracking-wider text-[#a6864a] block">
                      {s.step}
                    </span>
                    <h3 className="font-serif text-sm font-semibold text-[#1e1b18]">
                      {s.title}
                    </h3>
                    <p className="text-xs text-[#706456] mt-0.5">{s.desc}</p>
                  </div>
                ))}
              </div>
            </div>

            {/* Section 3: Focus Cue & Affirmation */}
            <div className="rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-6 shadow-[0_2px_12px_rgba(30,24,15,0.03)] space-y-4">
              <div className="flex items-center gap-2 border-b border-[#ebdcc9] pb-3">
                <Sparkles size={18} className="text-[#a6864a]" />
                <h2 className="font-serif text-lg font-semibold text-[#1e1b18]">
                  3. Competitive Anchor Cue
                </h2>
              </div>

              <div>
                <label className="block text-xs font-bold uppercase tracking-wider text-[#4e4337] mb-1.5">
                  Pre-Shot Cue Word or Phrase
                </label>
                <input
                  type="text"
                  value={anchorCue}
                  onChange={(e) => setAnchorCue(e.target.value)}
                  className="w-full rounded-md border border-[#dac8b2] bg-white p-3 text-xs sm:text-sm text-[#1e1b18] shadow-xs focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)] focus:border-[var(--gold-dark)] italic"
                />
              </div>

              <div className="pt-2 flex items-center justify-between">
                <div role="status" aria-live="polite" aria-atomic="true">
                  {isSaved && (
                    <span className="inline-flex items-center gap-1.5 text-xs font-semibold text-[#1e3a29]">
                      <CheckCircle2 size={15} aria-hidden="true" />
                      <span>Plan changes saved & queued for Coach Lornette review.</span>
                    </span>
                  )}
                </div>
                <button
                  type="submit"
                  className="ml-auto inline-flex min-h-11 items-center gap-2 rounded-md bg-gradient-to-r from-[#dfc385] via-[#ceab68] to-[#b38f4a] px-5 py-2.5 text-xs font-bold uppercase tracking-[0.14em] text-[#1e1b18] shadow-xs hover:brightness-105 transition-all cursor-pointer focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)]"
                >
                  <Save size={15} aria-hidden="true" />
                  <span>Save Plan Updates</span>
                </button>
              </div>
            </div>
          </div>

          {/* Right Column: Coach Feedback & Milestones (col-span-4) */}
          <div className="lg:col-span-4 space-y-5">
            {/* Coach Review Card */}
            <div className="rounded-xl border-2 border-[#dfcca6] bg-[#fdfbf7] p-6 shadow-xs space-y-4">
              <div className="flex items-center justify-between">
                <p className="text-[10px] font-bold uppercase tracking-[0.24em] text-[#8e7e6e]">
                  COACH LORNETTE REVIEW
                </p>
                <span
                  className={`rounded-full px-2 py-0.5 text-[9.5px] font-bold uppercase tracking-wider ${
                    activeAthlete.status === "approved"
                      ? "bg-[#d1fae5] text-[#065f46]"
                      : activeAthlete.status === "needs_revision"
                      ? "bg-[#fef3c7] text-[#92400e]"
                      : activeAthlete.status === "pending_review"
                      ? "bg-[#eff6ff] text-[#1e40af]"
                      : "bg-[#f4ede1] text-[#8a6828]"
                  }`}
                >
                  {activeAthlete.status === "approved"
                    ? "Approved ✓"
                    : activeAthlete.status === "needs_revision"
                    ? "Needs Revision"
                    : activeAthlete.status === "pending_review"
                    ? "Under Review"
                    : "Reviewed"}
                </span>
              </div>

              {activeAthlete.coachFeedbackNotes ? (
                <p className="font-serif text-sm italic text-[#2c2620] leading-relaxed">
                  “{activeAthlete.coachFeedbackNotes}”
                </p>
              ) : (
                <p className="text-xs text-[#706456] italic">
                  Your plan has been submitted to Coach Lornette Daye. Coaching review notes will appear here once reviewed.
                </p>
              )}

              <div className="pt-2 border-t border-[#ebdcc9] text-xs font-semibold text-[#8a6828]">
                {activeAthlete.reviewedAt ? (
                  <span>
                    Last reviewed: {activeAthlete.reviewedAt} by {activeAthlete.reviewerName}
                  </span>
                ) : (
                  <span>Awaiting initial coach audit</span>
                )}
              </div>
            </div>

            {/* 30-Day Commitments (Interactive & Dynamic) */}
            <div className="rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-6 shadow-xs space-y-4">
              <div className="flex items-center justify-between">
                <h3 className="font-serif text-base font-semibold text-[#1e1b18]">
                  30-Day Performance Goals
                </h3>
                <span className="text-[10px] font-bold uppercase tracking-wider text-[#8e7e6e]">
                  {goals.filter((g) => g.completed).length} / {goals.length} Complete
                </span>
              </div>

              <ul className="space-y-2.5 text-xs">
                {goals.map((goal) => (
                  <li
                    key={goal.id}
                    className="flex items-start justify-between gap-2 group rounded-md p-1.5 hover:bg-[#f4ede1]/50 transition-colors"
                  >
                    <button
                      type="button"
                      role="checkbox"
                      aria-checked={goal.completed}
                      aria-label={goal.text}
                      onClick={() => handleToggleGoal(goal.id)}
                      className="flex items-start gap-2 text-left flex-1 cursor-pointer focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)] rounded-xs"
                    >
                      <div
                        className={`h-4 w-4 rounded shrink-0 mt-0.5 flex items-center justify-center border transition-colors ${
                          goal.completed
                            ? "bg-[#1e3a29] border-[#1e3a29] text-white"
                            : "border-[#c4b59f] bg-white hover:border-[#1e3a29]"
                        }`}
                      >
                        {goal.completed && <Check size={12} aria-hidden="true" />}
                      </div>
                      <span
                        className={
                          goal.completed
                            ? "line-through text-[#8e7e6e]"
                            : "text-[#2c2620] font-medium"
                        }
                      >
                        {goal.text}
                      </span>
                    </button>

                    <button
                      type="button"
                      onClick={() => handleRemoveGoal(goal.id)}
                      aria-label={`Remove goal: ${goal.text}`}
                      className="opacity-0 group-hover:opacity-100 focus-visible:opacity-100 text-[#756756] hover:text-red-700 transition-opacity p-2 min-h-9 min-w-9 flex items-center justify-center rounded-xs focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)]"
                    >
                      <Trash2 size={14} aria-hidden="true" />
                    </button>
                  </li>
                ))}
              </ul>

              {/* Add Goal Input */}
              <div className="pt-2 border-t border-[#ebdcc9]">
                <div className="flex items-center gap-1.5">
                  <input
                    type="text"
                    value={newGoalText}
                    onChange={(e) => setNewGoalText(e.target.value)}
                    placeholder="Add a new 30-day commitment..."
                    className="flex-1 rounded-md border border-[#dac8b2] bg-white px-2.5 py-1.5 text-xs text-[#1e1b18] shadow-2xs focus:border-[var(--gold-dark)] focus:outline-none"
                    onKeyDown={(e) => {
                      if (e.key === "Enter") {
                        e.preventDefault();
                        handleAddGoal(e);
                      }
                    }}
                  />
                  <button
                    type="button"
                    onClick={handleAddGoal}
                    className="rounded-md bg-[#1e3a29] px-2.5 py-1.5 text-xs font-bold text-white hover:bg-[#274d36] transition-colors"
                  >
                    <Plus size={14} />
                  </button>
                </div>
              </div>
            </div>
          </div>
        </form>
      </div>
    </LearnerShell>
  );
}
