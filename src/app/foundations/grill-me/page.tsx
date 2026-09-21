"use client";

import { useState } from "react";
import Link from "next/link";
import { LearnerShell } from "@/components/foundations/learner/LearnerShell";
import {
  CheckCircle2,
  ChevronRight,
  Clock,
  Compass,
  Flame,
  Send,
  ShieldCheck,
  Sparkles,
  Target,
  Zap,
} from "lucide-react";
import { useFoundationsStore } from "@/lib/foundations/store";

const TOURNAMENT_SCENARIOS = [
  {
    id: "sc-18th-water",
    title: "18th Tee with Water Left & Out of Bounds Right",
    stakes: "Club Championship Final Round · 1-Shot Lead",
    context:
      "You are 1 shot off or holding a 1-shot lead on the 18th tee box. Water hugs the left side; thick trees and out-of-bounds line the right. The group ahead took 15 minutes to clear the green, so you've been standing in the wind. Your hands feel cold and your pulse is noticeably elevated.",
    challengePrompt:
      "Grill me: What is your exact physical reset cadence, where do your eyes lock, and what is your non-negotiable anchor cue before stepping into this shot?",
  },
  {
    id: "sc-bogey-cascade",
    title: "Back-to-Back Bogeys Entering Tough 3-Hole Stretch",
    stakes: "Medal Play · Holes 16–18",
    context:
      "You just three-putted 14 and lipped out for par on 15. Your lead has vanished. A voice in your head says: 'You're giving this away again.' You have 3 minutes walking to the 16th tee box.",
    challengePrompt:
      "Grill me: How do you definitively close the door on the previous hole so your previous shot cannot hit your next shot?",
  },
  {
    id: "sc-downhill-slider",
    title: "3-Foot Downhill Slider to Force Playoff",
    stakes: "18th Green · Match On The Line",
    context:
      "You have a 3-foot downhill, right-to-left putt to force sudden-death playoff. The entire clubhouse gallery is surrounding the fringe. You feel an impulse to hit it quickly just to get it over with.",
    challengePrompt:
      "Grill me: How do you govern your breath, pace your routine, and strike the putt with pure visual commitment?",
  },
];

export default function FoundationsGrillMePage() {
  const { activeAthlete, submitGrillMeChallenge, updateActivePlan } = useFoundationsStore();
  const [selectedScenarioId, setSelectedScenarioId] = useState(
    TOURNAMENT_SCENARIOS[0].id
  );

  const selectedScenario =
    TOURNAMENT_SCENARIOS.find((s) => s.id === selectedScenarioId) ||
    TOURNAMENT_SCENARIOS[0];

  const [golferResponse, setGolferResponse] = useState("");
  const [resetProtocolApplied, setResetProtocolApplied] = useState(
    activeAthlete.resetProtocol || ""
  );
  const [anchorCueUsed, setAnchorCueUsed] = useState(
    activeAthlete.anchorCue || ""
  );
  const [isSubmitted, setIsSubmitted] = useState(false);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!golferResponse.trim()) return;

    submitGrillMeChallenge({
      scenarioId: selectedScenario.id,
      scenarioTitle: selectedScenario.title,
      pressureContext: selectedScenario.context,
      golferResponse: golferResponse.trim(),
      resetProtocolApplied: resetProtocolApplied.trim() || activeAthlete.resetProtocol,
      anchorCueUsed: anchorCueUsed.trim() || activeAthlete.anchorCue,
    });

    // Synchronize protocol/cue to athlete's active plan
    updateActivePlan({
      resetProtocol: resetProtocolApplied.trim() || activeAthlete.resetProtocol,
      anchorCue: anchorCueUsed.trim() || activeAthlete.anchorCue,
    });

    setIsSubmitted(true);
    setTimeout(() => {
      setIsSubmitted(false);
      setGolferResponse("");
    }, 4500);
  };

  return (
    <LearnerShell>
      <div className="p-4 sm:p-6 lg:p-8 max-w-7xl mx-auto space-y-6">
        {/* Top Header */}
        <section className="relative overflow-hidden rounded-2xl border border-[#dfcca6] bg-[#fbf9f4] p-6 sm:p-8 shadow-[0_4px_24px_rgba(30,24,15,0.04)]">
          <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
            <div>
              <div className="inline-flex items-center gap-2 rounded-full border border-[rgba(198,165,92,0.4)] bg-[#f5ede2] px-3 py-1 text-[11px] font-bold uppercase tracking-[0.22em] text-[#1e3a29] shadow-xs mb-2">
                <Flame size={14} className="text-[#b45309]" />
                <span>Pressure Simulation Lab</span>
              </div>
              <h1 className="font-serif text-3xl sm:text-4xl font-semibold tracking-tight text-[#1e1b18]">
                Coach Lornette&apos;s Grill-Me Challenge
              </h1>
              <p className="mt-2 font-sans text-xs sm:text-sm text-[#665a4c] max-w-xl leading-relaxed">
                Test your 5-second reset protocol and pre-shot commitment under authentic tournament pressure. Responses are submitted directly to Coach Lornette Daye for personalized scrutiny and coaching feedback.
              </p>
            </div>

            <div className="flex items-center gap-3">
              <Link
                href="/foundations/plan"
                className="inline-flex items-center gap-1.5 rounded-sm border border-[#dac8b2] bg-white px-3.5 py-1.5 text-xs font-semibold text-[#4e4337] hover:bg-[#f4ede1] transition-colors"
              >
                <Compass size={14} />
                <span>My Plan & Blueprint</span>
              </Link>
            </div>
          </div>
        </section>

        {/* Main 2-Column Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 items-start">
          {/* Left Column: Scenario Selector & Form (col-span-8) */}
          <div className="lg:col-span-8 space-y-6">
            {/* Scenario Picker */}
            <div className="rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-5 shadow-xs space-y-3">
              <p className="text-[10px] font-bold uppercase tracking-[0.22em] text-[#8e7e6e]">
                Select Pressure Scenario
              </p>
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-2.5">
                {TOURNAMENT_SCENARIOS.map((sc) => {
                  const isSelected = selectedScenarioId === sc.id;
                  return (
                    <button
                      key={sc.id}
                      type="button"
                      onClick={() => {
                        setSelectedScenarioId(sc.id);
                        setIsSubmitted(false);
                      }}
                      className={`text-left p-3 rounded-lg border text-xs transition-all ${
                        isSelected
                          ? "bg-[#e8dbbf]/70 border-[#dfcca6] shadow-xs ring-1 ring-[#c7a45e]/50 font-semibold"
                          : "bg-white/70 hover:bg-[#f4ede1] border-[#ebdcc9]"
                      }`}
                    >
                      <span className="text-[9.5px] font-bold uppercase text-[#a6864a] block mb-1">
                        {sc.stakes}
                      </span>
                      <p className="font-serif font-semibold text-[#1e1b18] leading-snug">
                        {sc.title}
                      </p>
                    </button>
                  );
                })}
              </div>
            </div>

            {/* Active Scenario Card & Form */}
            <form
              onSubmit={handleSubmit}
              action="javascript:void(0)"
              className="rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-6 shadow-xs space-y-5"
            >
              <div className="border-b border-[#ebdcc9] pb-4 space-y-2">
                <div className="flex items-center gap-2">
                  <Zap size={18} className="text-[#a6864a]" />
                  <h2 className="font-serif text-xl font-semibold text-[#1e1b18]">
                    {selectedScenario.title}
                  </h2>
                </div>
                <div className="rounded-lg bg-[#f7f2ea] p-3.5 border border-[#ebdcc9] text-xs text-[#4e4337] leading-relaxed">
                  <p className="font-bold uppercase tracking-wider text-[9.5px] text-[#7a6f62] mb-1">
                    Live Tournament Scenario
                  </p>
                  <p>{selectedScenario.context}</p>
                </div>
                <p className="font-serif text-sm italic text-[#1e1b18] pt-1">
                  “{selectedScenario.challengePrompt}”
                </p>
              </div>

              {/* Input: Golfer In-The-Moment Tactical Response */}
              <div className="space-y-1.5">
                <label htmlFor="golfer-response" className="block text-xs font-bold uppercase tracking-wider text-[#1e1b18]">
                  Your In-The-Moment Tactical Execution
                </label>
                <textarea
                  id="golfer-response"
                  rows={3}
                  required
                  value={golferResponse}
                  onChange={(e) => setGolferResponse(e.target.value)}
                  placeholder="Detail your exact steps: breath count, target fix point, walking tempo, and internal self-talk..."
                  className="w-full rounded-md border border-[#dac8b2] bg-white p-3 text-xs sm:text-sm text-[#1e1b18] placeholder-[#756756] shadow-xs focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)] focus:border-[var(--gold-dark)] leading-relaxed"
                />
              </div>

              {/* 2 Inputs: Protocol Applied & Anchor Cue */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div>
                  <label htmlFor="protocol-applied" className="block text-xs font-bold uppercase tracking-wider text-[#4e4337] mb-1">
                    Physical Reset Protocol Applied
                  </label>
                  <input
                    id="protocol-applied"
                    type="text"
                    value={resetProtocolApplied}
                    onChange={(e) => setResetProtocolApplied(e.target.value)}
                    className="w-full rounded-md border border-[#dac8b2] bg-white p-2.5 text-xs text-[#1e1b18] shadow-xs focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)] focus:border-[var(--gold-dark)]"
                  />
                </div>

                <div>
                  <label htmlFor="anchor-cue" className="block text-xs font-bold uppercase tracking-wider text-[#4e4337] mb-1">
                    Anchor Focus Cue Used
                  </label>
                  <input
                    id="anchor-cue"
                    type="text"
                    value={anchorCueUsed}
                    onChange={(e) => setAnchorCueUsed(e.target.value)}
                    className="w-full rounded-md border border-[#dac8b2] bg-white p-2.5 text-xs text-[#1e1b18] shadow-xs focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)] focus:border-[var(--gold-dark)] italic"
                  />
                </div>
              </div>

              {/* Form Action */}
              <div className="pt-2 flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-t border-[#ebdcc9]">
                <div role="status" aria-live="polite" aria-atomic="true">
                  {isSubmitted ? (
                    <span className="inline-flex items-center gap-1.5 text-xs font-semibold text-[#1e3a29]">
                      <CheckCircle2 size={16} aria-hidden="true" />
                      <span>Submitted to Coach Lornette Daye&apos;s Review Queue!</span>
                    </span>
                  ) : (
                    <span className="text-xs text-[#5e5245]">
                      Coach Lornette reviews and critiques all scenario submissions in the admin console.
                    </span>
                  )}
                </div>

                <button
                  type="submit"
                  className="inline-flex min-h-11 items-center justify-center gap-2 rounded-md bg-gradient-to-r from-[#dfc385] via-[#ceab68] to-[#b38f4a] px-6 py-2.5 text-xs font-bold uppercase tracking-wider text-[#1e1b18] shadow-xs hover:brightness-105 transition-all cursor-pointer focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)]"
                >
                  <Flame size={15} className="text-[#8a3828]" aria-hidden="true" />
                  <span>Submit to Coach Lornette</span>
                </button>
              </div>
            </form>
          </div>

          {/* Right Column: Submitted Audits & Coach Critiques (col-span-4) */}
          <div className="lg:col-span-4 space-y-5">
            <div className="rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-5 sm:p-6 shadow-xs space-y-4">
              <div className="flex items-center justify-between border-b border-[#ebdcc9] pb-3">
                <h3 className="font-serif text-base font-semibold text-[#1e1b18]">
                  My Pressure Audit Log
                </h3>
                <span className="text-[10px] font-bold text-[#8a6828] uppercase tracking-wider">
                  {activeAthlete.grillMeSubmissions.length} Recorded
                </span>
              </div>

              {activeAthlete.grillMeSubmissions.length === 0 ? (
                <p className="text-xs text-[#706456] italic py-3 text-center">
                  You have not submitted any tournament pressure audits yet. Select a scenario on the left to begin.
                </p>
              ) : (
                <div className="space-y-4">
                  {activeAthlete.grillMeSubmissions.map((entry) => (
                    <div
                      key={entry.id}
                      className="rounded-lg border border-[#ebdcc9] bg-[#fcfaf5] p-3.5 space-y-2.5 text-xs"
                    >
                      <div className="flex items-center justify-between">
                        <span className="font-serif font-semibold text-[#1e1b18] truncate max-w-[180px]">
                          {entry.scenarioTitle}
                        </span>
                        <span
                          className={`rounded-full px-2 py-0.5 text-[9px] font-bold uppercase tracking-wider ${
                            entry.status === "reviewed_by_lornette"
                              ? "bg-[#d1fae5] text-[#065f46]"
                              : "bg-[#fef3c7] text-[#92400e]"
                          }`}
                        >
                          {entry.status === "reviewed_by_lornette"
                            ? "Critiqued ✓"
                            : "Pending Review"}
                        </span>
                      </div>

                      <p className="text-[#4e4337] line-clamp-2">
                        {entry.golferResponse}
                      </p>

                      <div className="text-[10px] text-[#8e7e6e]">
                        Cue: <span className="italic text-[#1e1b18]">{entry.anchorCueUsed}</span>
                      </div>

                      {entry.coachCritique && (
                        <div className="rounded-md bg-[#f4ede1] p-2.5 border-l-2 border-[#b89456] space-y-1">
                          <p className="text-[9.5px] font-bold uppercase tracking-wider text-[#8a6828]">
                            Coach Lornette Critique
                          </p>
                          <p className="font-serif italic text-xs text-[#1e1b18]">
                            “{entry.coachCritique}”
                          </p>
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              )}
            </div>

            {/* Principles Plaque */}
            <div className="rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-5 text-center space-y-2 shadow-xs">
              <p className="text-[9.5px] font-bold uppercase tracking-[0.24em] text-[#8e7e6e]">
                The Next-Shot Principle
              </p>
              <p className="font-serif text-sm italic text-[#1e1b18]">
                “The championship isn&apos;t won when things feel easy. It&apos;s won in the 5 seconds after they go wrong.”
              </p>
              <p className="text-[10px] font-bold uppercase tracking-wider text-[#8a6828]">
                Coach Lornette Daye
              </p>
            </div>
          </div>
        </div>
      </div>
    </LearnerShell>
  );
}
