"use client";

import { useState } from "react";
import { ChevronDown, Compass, Users, Brain, Target, type LucideIcon } from "lucide-react";
import { motion, AnimatePresence, useReducedMotion } from "framer-motion";

interface HighlightItem {
  label: string;
  desc: string;
}

interface OrientationStep {
  step: string;
  eyebrow: string;
  title: string;
  summary: string;
  icon: LucideIcon;
  highlights: HighlightItem[];
}

const orientationSteps: OrientationStep[] = [
  {
    step: "01",
    eyebrow: "FOUNDATION BLUEPRINT",
    title: "What Foundations Is",
    summary:
      "A 10-week guided athlete and leadership development system built around mental performance, somatic composure, and execution under competition fire.",
    icon: Compass,
    highlights: [
      {
        label: "10 Athletic Foundations",
        desc: "Structured from 40+ years of Olympic coaching and Canadian national sprint championship practice.",
      },
      {
        label: "Whole-Athlete Pedagogy",
        desc: "Integrates mental discipline, somatic emotional composure, identity beyond sport, and habit systems.",
      },
      {
        label: "Human-Led Experience",
        desc: "Guided directly with weekly reflections, progress checkpoints, and personal oversight from Lornette Daye.",
      },
    ],
  },
  {
    step: "02",
    eyebrow: "WHO WE SERVE",
    title: "Who It’s Designed For",
    summary:
      "Tailored developmental pathways for individual competitors, varsity programs, executive leadership teams, and international federations.",
    icon: Users,
    highlights: [
      {
        label: "Competitive Athletes & Golfers",
        desc: "Junior, collegiate, and tournament competitors seeking repeatable focus, somatic poise, and 5-second error resets under pressure.",
      },
      {
        label: "Varsity & Academy Rosters",
        desc: "Hockey programs, coaching staffs, and athletic departments establishing unified standards of championship culture and accountability.",
      },
      {
        label: "Corporate & Executive Teams",
        desc: "Senior leadership and organizations cultivating championship composure, clarity, and decision poise in high-stakes environments.",
      },
      {
        label: "European Sport Partners",
        desc: "Regional federations, premier clubs, and sport ecosystems co-designing transatlantic athletic development initiatives.",
      },
    ],
  },
  {
    step: "03",
    eyebrow: "THE METHODOLOGY",
    title: "How The Experience Works",
    summary:
      "Deliberate weekly cadence translating elite Olympic principles into repeatable competitive habits and actionable drills.",
    icon: Brain,
    highlights: [
      {
        label: "5-Step Weekly Cadence",
        desc: "Audio briefing, psychological concept, practical action tool, real-world drill, and confidential reflection.",
      },
      {
        label: "Battle-Tested Tools",
        desc: "Immediate routines including the 5-Second Reset, Attention Dial, and pre-performance focus sequences.",
      },
      {
        label: "Private Athlete Workspace",
        desc: "A secure personal ledger for notes, evidence logs, and direct developmental feedback with Lornette Daye.",
      },
    ],
  },
  {
    step: "04",
    eyebrow: "GET STARTED",
    title: "Choose Your Pathway",
    summary:
      "Four dedicated tracks tailored to individual sports, team dynamics, corporate leadership, or international athletic partnerships.",
    icon: Target,
    highlights: [
      {
        label: "Golf Pathway",
        desc: "10-Week Guided Athlete Development Program powered by the Performance Edge Framework.",
      },
      {
        label: "Hockey Pathway",
        desc: "Shift-to-shift composure, leadership, and emotional regulation for competitive rosters.",
      },
      {
        label: "Corporate Pathway",
        desc: "Strategic briefings, executive keynotes, and high-trust resilience intensives.",
      },
      {
        label: "Europe Pathway",
        desc: "Transatlantic sport education, athletic symposiums, and institutional ecosystem collaborations.",
      },
    ],
  },
];

export function FoundationsOrientationSteps() {
  const [openStep, setOpenStep] = useState<string | null>(null);
  const reduce = useReducedMotion();

  const toggleStep = (stepNumber: string) => {
    setOpenStep((prev) => (prev === stepNumber ? null : stepNumber));
  };

  return (
    <div className="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
      {orientationSteps.map((step, idx) => {
        const IconComponent = step.icon;
        const isOpen = openStep === step.step;

        return (
          <motion.div
            key={step.step}
            initial={reduce ? { opacity: 1 } : { opacity: 0, y: 22 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-30px" }}
            transition={{ duration: 0.5, delay: idx * 0.1, ease: [0.22, 1, 0.36, 1] }}
            whileHover={reduce ? undefined : { y: -5, transition: { duration: 0.25 } }}
            className="group relative flex flex-col justify-between rounded-[2px] border border-[rgba(198,165,92,0.36)] bg-white p-5 sm:p-6 shadow-sm transition-all duration-300 hover:border-[#c9a75e] hover:shadow-[0_14px_36px_rgba(198,165,92,0.14)]"
          >
            <div>
              {/* Top Header Row: Step Badge + Icon */}
              <div className="flex items-center justify-between pb-3.5 border-b border-[rgba(198,165,92,0.2)]">
                <span className="inline-flex items-center justify-center rounded-[1px] bg-[var(--ivory)] border border-[rgba(198,165,92,0.6)] px-2.5 py-0.5 text-[10.5px] font-mono font-bold tracking-[0.16em] text-[var(--ink)] shadow-[0_1px_2px_rgba(0,0,0,0.04)]">
                  STEP {step.step}
                </span>
                <div className="flex h-8 w-8 items-center justify-center rounded-full bg-[#fbf8f2] border border-[rgba(198,165,92,0.3)] text-[var(--gold-dark)] transition-transform duration-300 group-hover:scale-110 group-hover:bg-[#faf4e6]">
                  <IconComponent size={16} aria-hidden="true" />
                </div>
              </div>

              {/* Eyebrow & Title */}
              <div className="mt-3.5">
                <p className="text-[10px] font-extrabold uppercase tracking-[0.22em] text-[var(--gold-dark)]">
                  {step.eyebrow}
                </p>
                <h3 className="mt-1 font-serif text-lg sm:text-xl font-bold tracking-tight text-[var(--ink)] leading-snug">
                  {step.title}
                </h3>
              </div>

              {/* Summary */}
              <p className="mt-2.5 text-xs sm:text-[13px] leading-relaxed text-[#5c5043]">
                {step.summary}
              </p>
            </div>

            {/* Interactive Animated Drawer */}
            <div className="mt-4 border-t border-[rgba(198,165,92,0.22)] pt-3">
              <button
                type="button"
                onClick={() => toggleStep(step.step)}
                aria-expanded={isOpen}
                className="flex w-full cursor-pointer items-center justify-between rounded-[1px] py-1 text-[11px] font-bold uppercase tracking-[0.18em] text-[var(--gold-dark)] hover:text-[#171412] focus-visible:outline focus-visible:outline-2 focus-visible:outline-[var(--gold-dark)] select-none transition-colors"
              >
                <span>{isOpen ? "Hide Details" : "View Details"}</span>
                <motion.div
                  animate={{ rotate: isOpen ? 180 : 0 }}
                  transition={{ duration: 0.25, ease: "easeInOut" }}
                  className="flex h-5 w-5 items-center justify-center rounded-full bg-[#fbf8f2] border border-[rgba(198,165,92,0.35)] text-[var(--gold-dark)]"
                >
                  <ChevronDown size={12} aria-hidden="true" />
                </motion.div>
              </button>

              <AnimatePresence initial={false}>
                {isOpen && (
                  <motion.div
                    initial={{ opacity: 0, height: 0 }}
                    animate={{ opacity: 1, height: "auto" }}
                    exit={{ opacity: 0, height: 0 }}
                    transition={{ duration: 0.3, ease: [0.22, 1, 0.36, 1] }}
                    className="overflow-hidden"
                  >
                    <div className="mt-3 space-y-2.5 pt-2 border-t border-[rgba(198,165,92,0.15)]">
                      {step.highlights.map((item) => (
                        <div
                          key={item.label}
                          className="rounded-[1px] bg-[#fbf9f4] border-l-2 border-[var(--gold-dark)] px-2.5 py-2 shadow-[0_1px_3px_rgba(0,0,0,0.02)] transition-colors duration-150 hover:bg-[#faf4e8]"
                        >
                          <p className="text-[11px] font-bold text-[var(--ink)] leading-snug">
                            {item.label}
                          </p>
                          <p className="mt-0.5 text-[10.5px] text-[#6d6152] leading-relaxed">
                            {item.desc}
                          </p>
                        </div>
                      ))}
                    </div>
                  </motion.div>
                )}
              </AnimatePresence>
            </div>
          </motion.div>
        );
      })}
    </div>
  );
}
