"use client";

import Link from "next/link";
import {
  ArrowLeft,
  CheckCircle2,
  Lock,
  Printer,
  ShieldCheck,
} from "lucide-react";

type FoundationGuideline = {
  week: number;
  foundation: string;
  tool: string;
  cue: string;
  reinforce: string;
  avoid: string;
  lessonApplication: string;
};

const COACH_FOUNDATIONS: FoundationGuideline[] = [
  {
    week: 1,
    foundation: "Foundation 1: Identity Beyond Sport",
    tool: "Athlete Identity Audit",
    cue: "“Who you are drives how you play.”",
    reinforce: "Praise preparation, self-talk discipline, and posture rather than just shot outcome.",
    avoid: "Do not tie the player’s personal self-worth to their handicap or tournament score.",
    lessonApplication: "Begin range sessions by asking how they felt walking to the range, not what score they shot yesterday.",
  },
  {
    week: 2,
    foundation: "Foundation 2: Champion Mindset",
    tool: "Focus Calibration Drill",
    cue: "“Narrow your world to what you control.”",
    reinforce: "Target selection, visual intermediate blade 18 inches in front, committed execution.",
    avoid: "Do not overload range practice with multiple conflicting swing thoughts.",
    lessonApplication: "Have golfer alternate between a broad target view and a micro-intermediate aim mark before each ball.",
  },
  {
    week: 3,
    foundation: "Foundation 3: Discipline Systems",
    tool: "6-Step Pre-Shot Cadence",
    cue: "“Consistency isn’t talent; it’s systems.”",
    reinforce: "Strict adherence to the 6-step cadence. Timing consistency from ball approach to takeaway trigger.",
    avoid: "Do not let players rush their routine when hitting poor shots during range blocks.",
    lessonApplication: "Time 5 consecutive shots. The pre-shot sequence should stay within 1.5 seconds of baseline.",
  },
  {
    week: 4,
    foundation: "Foundation 4: Resilience After Setback",
    tool: "5-Second Physical Reset",
    cue: "“Your previous shot cannot hit your next shot.”",
    reinforce: "The 5-step reset sequence: Acknowledge, Evaluate, Release, Reset, Recommit.",
    avoid: "Do not allow lingering negative complaints about past holes while walking to the ball.",
    lessonApplication: "Simulate a severe mis-hit on the range. Require a full 5-second reset before touching another club.",
  },
  {
    week: 5,
    foundation: "Foundation 5: Pressure, Emotional Regulation & Recovery",
    tool: "Physiological Sigh & Heart Rate Regulation",
    cue: "“Steady respiration produces calm hands.”",
    reinforce: "Two quick nasal inhales and long oral sigh. Grip tension resting at 4/10.",
    avoid: "Do not shout technical instructions when the golfer is visibly agitated or rushed.",
    lessonApplication: "Measure grip pressure when hitting from difficult fairway lies; cue a physiological sigh before setup.",
  },
  {
    week: 6,
    foundation: "Foundation 6: Communication & Presence",
    tool: "Internal Dialogue Script",
    cue: "“Walk tall. Your presence speaks first.”",
    reinforce: "Neutral, constructive language. Chin up, shoulders square, brisk fairway pacing.",
    avoid: "Do not accept self-defeating language (“I always slice on 16”) without demanding a verbal reset.",
    lessonApplication: "Have athlete announce their shot intention aloud with calm, definitive certainty before stepping in.",
  },
  {
    week: 7,
    foundation: "Foundation 7: Family & Community Support",
    tool: "Support Alignment Canvas",
    cue: "“Protect your competitive sanctuary.”",
    reinforce: "Clear boundaries with caddies, family, and peers during match preparation.",
    avoid: "Do not initiate unsolicited technical swing overhauls within 48 hours of a tournament round.",
    lessonApplication: "Establish a clear pre-round warmup timetable with the player and their family.",
  },
  {
    week: 8,
    foundation: "Foundation 8: Career & Money Readiness",
    tool: "Financial & Transition Roadmap",
    cue: "“Long-term perspective breeds daily calm.”",
    reinforce: "Treat equipment care, practice planning, and time management as professional habits.",
    avoid: "Do not treat practice sessions as casual hitting sessions without explicit objectives.",
    lessonApplication: "Ensure athlete has a written scorecard for every range bucket with specific technical goals.",
  },
  {
    week: 9,
    foundation: "Foundation 9: Personal Brand & Story",
    tool: "Story & Values Matrix",
    cue: "“Excellence in conduct builds lasting respect.”",
    reinforce: "Respect for the course, competitors, club staff, and golf traditions.",
    avoid: "Do not overlook club-throwing, sulking, or disrespectful interactions with facility staff.",
    lessonApplication: "Reinforce standard post-round handshakes, rake etiquette, and repair of ball marks as core identity.",
  },
  {
    week: 10,
    foundation: "Foundation 10: Legacy & Community Impact",
    tool: "Legacy Blueprint",
    cue: "“Better People · Better Players.”",
    reinforce: "Mentorship of younger junior golfers, leadership within the club junior league.",
    avoid: "Do not isolate the athlete from their peer club community as if winning were a solitary endeavor.",
    lessonApplication: "Pair athlete with a younger junior golfer for a 3-hole demonstration of the 6-step routine.",
  },
];

export default function CoachCompanionPage() {
  const handlePrint = () => {
    if (typeof window !== "undefined") {
      window.print();
    }
  };

  return (
    <div className="min-h-screen bg-[#faf7f2] text-[#2c2620] font-sans antialiased selection:bg-[#dfc187]/40">
      {/* Top Header */}
      <header className="sticky top-0 z-30 flex h-16 w-full items-center justify-between border-b border-[#ebdcc9] bg-[#fbf9f5] px-4 lg:px-8 shadow-xs print:hidden">
        <div className="flex items-center gap-3">
          <Link
            href="/foundations/club"
            className="inline-flex items-center gap-1 text-xs font-bold uppercase tracking-wider text-[#706456] hover:text-[#1e1b18] transition-colors"
          >
            <ArrowLeft size={14} />
            <span>Return to Club Portal</span>
          </Link>
          <span className="text-[#ebdcc9]">|</span>
          <span className="text-xs font-semibold text-[#1e1b18]">
            INTERNAL-06: PGA Club Delivery Companion
          </span>
        </div>

        <div className="flex items-center gap-3">
          <button
            type="button"
            onClick={handlePrint}
            className="inline-flex items-center gap-1.5 rounded-md border border-[#dfcca6] bg-white px-3 py-1.5 text-xs font-bold uppercase tracking-wider text-[#1e1b18] hover:bg-[#f4ede1] transition-colors cursor-pointer"
          >
            <Printer size={14} />
            <span>Print Coach Field Guide</span>
          </button>
        </div>
      </header>

      <main className="p-4 sm:p-6 lg:p-8 max-w-6xl mx-auto space-y-8 print:p-0 print:max-w-none">
        {/* Banner */}
        <section className="relative overflow-hidden rounded-2xl border border-[#dfcca6] bg-[#fbf9f4] p-6 sm:p-8 shadow-sm space-y-4 print:border-black print:bg-white print:p-0">
          <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div>
              <div className="inline-flex items-center gap-2 rounded-full bg-[#f4ede1] px-3.5 py-1 text-xs font-semibold text-[#1e3a29] border border-[#dfcca6] print:border-black">
                <ShieldCheck size={14} />
                <span>Coach Lornette Daye · Technical Staff Companion</span>
              </div>
              <h1 className="font-serif text-3xl sm:text-4xl font-semibold tracking-tight text-[#1e1b18] mt-2">
                PGA & Club Coach Delivery Companion
              </h1>
              <p className="text-xs sm:text-sm text-[#706456] max-w-2xl mt-1 leading-relaxed">
                A 10-week reference guide for PGA Head Professionals and Academy instructors to align swing mechanics with Coach Lornette’s mental performance architecture.
              </p>
            </div>

            {/* Pre-Program Briefing Status Card */}
            <div className="rounded-xl border border-[#ebdcc9] bg-white p-4 shadow-xs min-w-[240px] space-y-2 print:border-black">
              <div className="flex items-center justify-between text-[11px] font-bold uppercase tracking-wider text-[#8e7e6e]">
                <span>Pre-Program Briefing</span>
                <span className="text-[#1e3a29] flex items-center gap-1">
                  <CheckCircle2 size={13} />
                  <span>Completed</span>
                </span>
              </div>
              <p className="font-serif font-bold text-sm text-[#1e1b18]">
                Coach Alignment (25 Min)
              </p>
              <div className="text-[11px] text-[#706456] space-y-0.5">
                <p>Scheduled: <strong>Prior to Week 1 Kickoff</strong></p>
                <p>Led by: <strong>Coach Lornette Daye</strong></p>
              </div>
            </div>
          </div>

          {/* Privacy Boundary Card */}
          <div className="rounded-xl border border-[#b89456]/40 bg-[#f7f2e7] p-4 text-xs text-[#2c2419] flex items-start gap-3">
            <Lock size={18} className="text-[#8a6828] shrink-0 mt-0.5" />
            <div className="space-y-1">
              <span className="font-serif font-bold text-sm text-[#1e1b18] block">
                Athlete Reflection Privacy Boundary
              </span>
              <p className="text-xs text-[#5c5042] leading-relaxed">
                <strong>DO REINFORCE:</strong> Shared performance vocabulary, pre-shot routine timing, 5-second reset protocol, and competition preparation.
                <br />
                <strong>DO NOT REQUEST:</strong> Private athlete reflection answers, personal vulnerabilities, or Lornette review notes. Reflections are confidential between the athlete and Coach Lornette to preserve psychological safety.
              </p>
            </div>
          </div>
        </section>

        {/* 10-Foundation Summary Grid */}
        <section className="space-y-4">
          <div className="flex items-center justify-between border-b border-[#ebdcc9] pb-3">
            <h2 className="font-serif text-xl font-semibold text-[#1e1b18]">
              10-Foundation Weekly Alignment Grid
            </h2>
            <span className="text-xs font-bold uppercase tracking-wider text-[#8a6828]">
              Canonical Curriculum
            </span>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {COACH_FOUNDATIONS.map((cf) => (
              <div
                key={cf.week}
                className="p-5 rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] space-y-3.5 shadow-xs print:border-black print:bg-white"
              >
                <div className="flex items-start justify-between gap-2 border-b border-[#ebdcc9]/70 pb-2.5">
                  <div>
                    <span className="text-[10px] font-bold uppercase tracking-widest text-[#8a6828]">
                      Week {cf.week} · {cf.tool}
                    </span>
                    <h3 className="font-serif font-bold text-base text-[#1e1b18]">
                      {cf.foundation}
                    </h3>
                  </div>
                  <span className="h-6 w-6 rounded-full bg-[#1e3a29] text-white flex items-center justify-center text-xs font-serif font-bold shrink-0">
                    {cf.week}
                  </span>
                </div>

                <p className="font-serif italic text-xs text-[#8a6828]">
                  {cf.cue}
                </p>

                <div className="space-y-2 text-xs">
                  <div className="p-2.5 rounded-lg bg-emerald-50/70 border border-emerald-200">
                    <span className="font-bold text-emerald-950 block text-[10.5px] uppercase tracking-wider mb-0.5">
                      ✓ What to Reinforce
                    </span>
                    <span className="text-emerald-900 leading-snug">
                      {cf.reinforce}
                    </span>
                  </div>

                  <div className="p-2.5 rounded-lg bg-amber-50/70 border border-amber-200">
                    <span className="font-bold text-amber-950 block text-[10.5px] uppercase tracking-wider mb-0.5">
                      ✕ What to Avoid
                    </span>
                    <span className="text-amber-900 leading-snug">
                      {cf.avoid}
                    </span>
                  </div>

                  <div className="p-2.5 rounded-lg bg-white border border-[#ebdcc9]">
                    <span className="font-bold text-[#1e1b18] block text-[10.5px] uppercase tracking-wider mb-0.5">
                      Range / Lesson Application
                    </span>
                    <span className="text-[#5e5245] leading-snug">
                      {cf.lessonApplication}
                    </span>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </section>

        {/* Footer */}
        <footer className="pt-4 border-t border-[#ebdcc9] text-center text-xs text-[#8e7e6e]">
          <p>Lornette’s Foundation Golf · INTERNAL-06 PGA Club Delivery Companion</p>
          <p className="mt-0.5">Confidential Staff Instruction Material · For Authorized Club Coaches Only</p>
        </footer>
      </main>
    </div>
  );
}
