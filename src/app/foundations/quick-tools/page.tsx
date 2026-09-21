"use client";

import { useState } from "react";
import Link from "next/link";
import { LearnerShell } from "@/components/foundations/learner/LearnerShell";
import {
  Compass,
  Download,
  Focus,
  Printer,
  RotateCcw,
  ShieldAlert,
  Sparkles,
  Target,
  Wind,
} from "lucide-react";

export default function QuickToolsPage() {
  const [activeTab, setActiveTab] = useState<"reset" | "routine" | "pressure" | "cue">("reset");

  const handlePrint = () => {
    if (typeof window !== "undefined") {
      window.print();
    }
  };

  return (
    <LearnerShell>
      <div className="p-4 sm:p-6 lg:p-8 max-w-5xl mx-auto space-y-6 print:p-0 print:max-w-none">
        {/* Top Header */}
        <div className="flex flex-col sm:flex-row sm:items-end justify-between gap-4 border-b border-[#ebdcc9] pb-4 print:border-black">
          <div>
            <p className="font-sans text-[11px] font-bold uppercase tracking-[0.24em] text-[#8e7e6e] print:text-black">
              On-Course Performance Field Reference
            </p>
            <h1 className="font-serif text-3xl sm:text-4xl font-semibold tracking-tight text-[#1e1b18] print:text-black">
              Quick Golf Field Tools
            </h1>
            <p className="text-xs sm:text-sm text-[#706456] mt-1 print:text-black">
              Fast-access mental performance protocols designed for immediate on-course application under competition pressure.
            </p>
          </div>

          <div className="flex items-center gap-3 shrink-0 print:hidden">
            <button
              type="button"
              onClick={handlePrint}
              className="inline-flex items-center gap-1.5 rounded-md border border-[#dfcca6] bg-white px-3.5 py-2 text-xs font-bold uppercase tracking-wider text-[#1e1b18] hover:bg-[#f4ede1] transition-colors cursor-pointer shadow-xs"
            >
              <Printer size={15} />
              <span>Print / Save Field Card</span>
            </button>
          </div>
        </div>

        {/* Quick Tabs */}
        <div className="flex items-center gap-2 overflow-x-auto pb-1 print:hidden">
          {[
            { id: "reset", label: "5-Sec Reset Card", icon: RotateCcw },
            { id: "routine", label: "6-Step Pre-Shot Routine", icon: Target },
            { id: "pressure", label: "Pressure Protocol", icon: Wind },
            { id: "cue", label: "Anchor Cue & Focus", icon: Focus },
          ].map((tab) => {
            const Icon = tab.icon;
            const isActive = activeTab === tab.id;
            return (
              <button
                key={tab.id}
                type="button"
                onClick={() => setActiveTab(tab.id as typeof activeTab)}
                className={`inline-flex items-center gap-2 px-4 py-2.5 rounded-lg text-xs font-bold uppercase tracking-wider transition-all shrink-0 cursor-pointer ${
                  isActive
                    ? "bg-[#1e3a29] text-white shadow-xs"
                    : "bg-white border border-[#ebdcc9] text-[#6d6255] hover:text-[#1e1b18] hover:bg-[#fbf9f5]"
                }`}
              >
                <Icon size={14} className={isActive ? "text-[#dfc385]" : "text-[#8e7e6e]"} />
                <span>{tab.label}</span>
              </button>
            );
          })}
        </div>

        {/* Tool Content Surface */}
        <div className="rounded-2xl border border-[#dfcca6] bg-[#fdfbf7] p-6 sm:p-8 shadow-sm space-y-6 print:border-none print:p-0 print:bg-white">
          {/* Tool 1: 5-Second Reset Card */}
          {activeTab === "reset" && (
            <div className="space-y-6">
              <div className="border-b border-[#ebdcc9] pb-4">
                <div className="flex items-center gap-2">
                  <span className="rounded-sm bg-[#1e3a29] text-white px-2 py-0.5 text-[10px] font-bold uppercase tracking-widest">
                    Tool PE-GOLF-03
                  </span>
                  <span className="text-xs font-bold uppercase tracking-wider text-[#8a6828]">
                    Mistake Recovery Protocol
                  </span>
                </div>
                <h2 className="font-serif text-2xl sm:text-3xl font-semibold text-[#1e1b18] mt-2">
                  The 5-Second Mistake Reset
                </h2>
                <p className="font-serif italic text-lg text-[#8a6828] mt-1">
                  “Your previous shot cannot hit your next shot.”
                </p>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-5 gap-3.5">
                {[
                  {
                    num: "1",
                    step: "ACKNOWLEDGE",
                    desc: "Notice the outcome without emotion, blame, or self-condemnation.",
                  },
                  {
                    num: "2",
                    step: "EVALUATE",
                    desc: "Extract the single factual lesson: contact, wind, lie, or tempo.",
                  },
                  {
                    num: "3",
                    step: "RELEASE",
                    desc: "Execute a double nasal inhalation and long oral sigh to clear tension.",
                  },
                  {
                    num: "4",
                    step: "RESET",
                    desc: "Ground the clubhead, unfasten glove, and step off the shot line.",
                  },
                  {
                    num: "5",
                    step: "RECOMMIT",
                    desc: "Lock visual attention on your target for the upcoming shot.",
                  },
                ].map((item) => (
                  <div
                    key={item.num}
                    className="p-4 rounded-xl border border-[#ebdcc9] bg-white space-y-2 print:border-black"
                  >
                    <div className="flex items-center gap-2">
                      <span className="flex h-6 w-6 items-center justify-center rounded-full bg-[#dfc385]/30 text-[#8a6828] font-serif font-bold text-xs">
                        {item.num}
                      </span>
                      <span className="font-serif font-bold text-xs text-[#1e1b18] uppercase tracking-wider">
                        {item.step}
                      </span>
                    </div>
                    <p className="text-xs text-[#5e5245] leading-relaxed">
                      {item.desc}
                    </p>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Tool 2: 6-Step Pre-Shot Routine */}
          {activeTab === "routine" && (
            <div className="space-y-6">
              <div className="border-b border-[#ebdcc9] pb-4">
                <div className="flex items-center gap-2">
                  <span className="rounded-sm bg-[#1e3a29] text-white px-2 py-0.5 text-[10px] font-bold uppercase tracking-widest">
                    Tool PE-GOLF-02
                  </span>
                  <span className="text-xs font-bold uppercase tracking-wider text-[#8a6828]">
                    Execution System
                  </span>
                </div>
                <h2 className="font-serif text-2xl sm:text-3xl font-semibold text-[#1e1b18] mt-2">
                  The 6-Step Pre-Shot Cadence
                </h2>
                <p className="font-serif italic text-lg text-[#8a6828] mt-1">
                  “Consistency isn’t talent; it’s systems.”
                </p>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
                {[
                  {
                    num: "1",
                    title: "Lie & Conditions Assessment",
                    desc: "Analyze slope, wind direction, firmness, and carry yardage.",
                  },
                  {
                    num: "2",
                    title: "Clear Club Selection",
                    desc: "Commit decisively to one club. Never swing with doubt in your hands.",
                  },
                  {
                    num: "3",
                    title: "Intermediate Target Pick",
                    desc: "Stand behind the ball. Pick a blade of grass 18 inches in front on the line.",
                  },
                  {
                    num: "4",
                    title: "Physical Entry & Stance",
                    desc: "Step in from behind. Align clubface square to the intermediate mark first.",
                  },
                  {
                    num: "5",
                    title: "Waggle & Focal Lock",
                    desc: "Settle grip pressure at 4/10. Look once at target, once at intermediate mark.",
                  },
                  {
                    num: "6",
                    title: "Trigger & Free Swing",
                    desc: "Initiate takeaway without hesitation within 3 seconds of settling stance.",
                  },
                ].map((step) => (
                  <div
                    key={step.num}
                    className="p-4 rounded-xl border border-[#ebdcc9] bg-white space-y-2 print:border-black"
                  >
                    <div className="flex items-center gap-2">
                      <span className="flex h-6 w-6 items-center justify-center rounded-full bg-[#1e3a29] text-white font-serif font-bold text-xs">
                        {step.num}
                      </span>
                      <span className="font-serif font-bold text-xs text-[#1e1b18]">
                        {step.title}
                      </span>
                    </div>
                    <p className="text-xs text-[#5e5245] leading-relaxed">
                      {step.desc}
                    </p>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Tool 3: Pressure Protocol */}
          {activeTab === "pressure" && (
            <div className="space-y-6">
              <div className="border-b border-[#ebdcc9] pb-4">
                <div className="flex items-center gap-2">
                  <span className="rounded-sm bg-[#1e3a29] text-white px-2 py-0.5 text-[10px] font-bold uppercase tracking-widest">
                    Tool PE-GOLF-05
                  </span>
                  <span className="text-xs font-bold uppercase tracking-wider text-[#8a6828]">
                    Physiological Regulation
                  </span>
                </div>
                <h2 className="font-serif text-2xl sm:text-3xl font-semibold text-[#1e1b18] mt-2">
                  The Tournament Pressure Protocol
                </h2>
                <p className="font-serif italic text-lg text-[#8a6828] mt-1">
                  “Pressure is a privilege that yields to steady respiration.”
                </p>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
                <div className="p-5 rounded-xl border border-[#ebdcc9] bg-white space-y-2 print:border-black">
                  <h3 className="font-serif font-bold text-sm text-[#1e1b18]">
                    1. Double Physiological Sigh
                  </h3>
                  <p className="text-xs text-[#5e5245] leading-relaxed">
                    Two rapid inhales through the nose followed by one long, unforced exhalation through the mouth. Drops heart rate in under 10 seconds.
                  </p>
                </div>

                <div className="p-5 rounded-xl border border-[#ebdcc9] bg-white space-y-2 print:border-black">
                  <h3 className="font-serif font-bold text-sm text-[#1e1b18]">
                    2. Grip Pressure Calibration
                  </h3>
                  <p className="text-xs text-[#5e5245] leading-relaxed">
                    Tension gathers in the forearms. Consciously release grip tension to a steady 4 on a 1-to-10 scale before entering the stance.
                  </p>
                </div>

                <div className="p-5 rounded-xl border border-[#ebdcc9] bg-white space-y-2 print:border-black">
                  <h3 className="font-serif font-bold text-sm text-[#1e1b18]">
                    3. Process over Outcome
                  </h3>
                  <p className="text-xs text-[#5e5245] leading-relaxed">
                    Surrender score control. Direct all mental energy into executing the 6-step cadence with total commitment.
                  </p>
                </div>
              </div>
            </div>
          )}

          {/* Tool 4: Anchor Cue & Focus */}
          {activeTab === "cue" && (
            <div className="space-y-6">
              <div className="border-b border-[#ebdcc9] pb-4">
                <div className="flex items-center gap-2">
                  <span className="rounded-sm bg-[#1e3a29] text-white px-2 py-0.5 text-[10px] font-bold uppercase tracking-widest">
                    Tool PE-GOLF-01
                  </span>
                  <span className="text-xs font-bold uppercase tracking-wider text-[#8a6828]">
                    Attention Anchoring
                  </span>
                </div>
                <h2 className="font-serif text-2xl sm:text-3xl font-semibold text-[#1e1b18] mt-2">
                  Anchor Cues & Focus Calibration
                </h2>
                <p className="font-serif italic text-lg text-[#8a6828] mt-1">
                  “Playing Your Best When It Matters.”
                </p>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div className="p-5 rounded-xl border border-[#ebdcc9] bg-white space-y-2 print:border-black">
                  <span className="text-[10px] font-bold uppercase tracking-wider text-[#8a6828] block">
                    Sensory Focus Anchor
                  </span>
                  <h3 className="font-serif font-bold text-base text-[#1e1b18]">
                    The Intermediate Aim Spot
                  </h3>
                  <p className="text-xs text-[#5e5245] leading-relaxed">
                    Narrow your visual field from the entire 450-yard fairway to a single distinct blemish or leaf 18 inches in front of your ball. Align the clubface with absolute geometric precision.
                  </p>
                </div>

                <div className="p-5 rounded-xl border border-[#ebdcc9] bg-white space-y-2 print:border-black">
                  <span className="text-[10px] font-bold uppercase tracking-wider text-[#8a6828] block">
                    Verbal Performance Cue
                  </span>
                  <h3 className="font-serif font-bold text-base text-[#1e1b18]">
                    Tempo & Smooth Acceleration
                  </h3>
                  <p className="text-xs text-[#5e5245] leading-relaxed">
                    Replace intrusive thoughts with one rhythmic verbal cue, such as “Smooth to Target” or “Breathe and Commit”. Say it softly at takeaway initiation.
                  </p>
                </div>
              </div>
            </div>
          )}

          {/* Quick Offline Save Notice */}
          <div className="rounded-xl border border-[#ebdcc9] bg-[#f4ede1] p-4 text-xs text-[#5e5245] flex items-center justify-between gap-4 print:hidden">
            <div>
              <span className="font-bold text-[#1e1b18] block">
                Offline Field Use
              </span>
              <span>
                These quick reference tools are cached locally on this device. You can access them on the tee box even without cellular service.
              </span>
            </div>
            <Link
              href="/foundations/dashboard"
              className="text-xs font-bold text-[#1e3a29] hover:underline shrink-0"
            >
              Return to Dashboard &rarr;
            </Link>
          </div>
        </div>
      </div>
    </LearnerShell>
  );
}
