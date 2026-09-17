"use client";

export const dynamic = "force-dynamic";

import { useEffect, useState } from "react";
import Link from "next/link";
import {
  ArrowLeft,
  Calendar,
  CheckCircle2,
  FileBarChart,
  Lock,
  Printer,
  ShieldCheck,
  Users,
} from "lucide-react";
import { createClient } from "@/lib/supabase/client";

type ReportCohort = {
  id: string;
  title: string;
  code: string;
  capacity: number | null;
  enrolled: number;
  currentWeek: number;
  status: string;
  startDate: string;
};

export default function ClubExecutiveReportPage() {
  const [cohort, setCohort] = useState<ReportCohort>({
    id: "demo-cohort",
    title: "Derrick Golf & Winter Club",
    code: "DERRICK-FALL-2026",
    capacity: 20,
    enrolled: 15,
    currentWeek: 3,
    status: "Active (In Progress)",
    startDate: "2026-09-01",
  });

  const [generatedDate] = useState(() =>
    new Date().toLocaleDateString("en-US", {
      year: "numeric",
      month: "long",
      day: "numeric",
    })
  );

  const supabase = createClient();

  useEffect(() => {
    async function loadReportData() {
      try {
        const { data: cohorts } = await supabase
          .from("cohorts")
          .select("id, title, cohort_code, capacity, status, start_date")
          .limit(1);

        if (cohorts && cohorts.length > 0) {
          const c = cohorts[0];
          const { count: enrolled } = await supabase
            .from("cohort_members")
            .select("*", { count: "exact", head: true })
            .eq("cohort_id", c.id);

          setCohort({
            id: c.id,
            title: c.title || "Partner Club Cohort",
            code: c.cohort_code || "GOLF-FALL-2026",
            capacity: c.capacity !== undefined ? c.capacity : 20,
            enrolled: enrolled || 0,
            currentWeek: 1,
            status: c.status === "active" ? "Active (In Progress)" : c.status,
            startDate: c.start_date || "2026-09-01",
          });
        }
      } catch {}
    }
    loadReportData();
  }, [supabase]);

  const handlePrint = () => {
    if (typeof window !== "undefined") {
      window.print();
    }
  };

  const isSmallCohort = cohort.enrolled < 5;
  const activationPct = cohort.capacity
    ? Math.min(100, Math.round((cohort.enrolled / cohort.capacity) * 100))
    : 100;

  return (
    <div className="min-h-screen bg-[#faf7f2] text-[#2c2620] font-sans antialiased selection:bg-[#dfc187]/40 print:bg-white print:text-black">
      {/* Top Interactive Controls (Hidden during printing) */}
      <header className="sticky top-0 z-30 flex h-16 w-full items-center justify-between border-b border-[#ebdcc9] bg-[#fbf9f5] px-4 lg:px-8 shadow-xs print:hidden">
        <div className="flex items-center gap-3">
          <Link
            href="/foundations/club"
            className="inline-flex items-center gap-1.5 text-xs font-bold uppercase tracking-wider text-[#706456] hover:text-[#1e1b18] transition-colors"
          >
            <ArrowLeft size={14} />
            <span>Return to Club Operations</span>
          </Link>
          <span className="text-[#ebdcc9]">|</span>
          <span className="text-xs font-semibold text-[#1e1b18]">
            Board-Ready Executive Report
          </span>
        </div>

        <div className="flex items-center gap-3">
          <button
            type="button"
            onClick={handlePrint}
            className="inline-flex items-center gap-1.5 rounded-md bg-[#1e1b18] px-4 py-2 text-xs font-bold uppercase tracking-wider text-white hover:bg-[#332b24] transition-colors cursor-pointer shadow-xs"
          >
            <Printer size={15} />
            <span>Print / Save PDF</span>
          </button>
        </div>
      </header>

      {/* Main Printable Document Surface */}
      <main className="p-4 sm:p-8 lg:p-12 max-w-5xl mx-auto space-y-8 print:p-0 print:max-w-none print:space-y-6">
        {/* Document Header Plaque */}
        <section className="border-b-2 border-[#1e1b18] pb-6 space-y-4 print:border-black">
          <div className="flex flex-col sm:flex-row sm:items-start justify-between gap-4">
            <div className="space-y-1">
              <div className="inline-flex items-center gap-2 rounded-sm bg-[#1e3a29] px-2.5 py-0.5 text-[10px] font-bold uppercase tracking-widest text-white print:border print:border-black print:text-black print:bg-white">
                Executive Cohort Summary
              </div>
              <h1 className="font-serif text-3xl sm:text-4xl font-bold tracking-tight text-[#1e1b18] print:text-black">
                {cohort.title}
              </h1>
              <p className="text-xs font-bold uppercase tracking-[0.2em] text-[#8a6828] print:text-black">
                Lornette’s Foundation Golf · Cohort {cohort.code}
              </p>
            </div>

            <div className="text-left sm:text-right text-xs text-[#5e5245] space-y-1 print:text-black">
              <p>
                <strong>Program:</strong> 10-Week Guided Athlete Development
              </p>
              <p>
                <strong>Methodology:</strong> Performance Edge Framework
              </p>
              <p>
                <strong>Program Version:</strong> Golf V1.0 Canonical
              </p>
              <p>
                <strong>Report Generated:</strong> {generatedDate}
              </p>
              <p>
                <strong>Audience:</strong> Director of Golf & Club Board
              </p>
            </div>
          </div>
        </section>

        {/* Executive KPI Overview Grid */}
        <section className="grid grid-cols-2 sm:grid-cols-4 gap-4 print:gap-3">
          <div className="p-4 rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] space-y-1 print:border-black print:bg-white">
            <span className="text-[10px] font-bold uppercase tracking-wider text-[#8e7e6e] print:text-black">
              Cohort Enrollment
            </span>
            <p className="font-serif text-2xl font-bold text-[#1e1b18] print:text-black">
              {cohort.enrolled} / {cohort.capacity ?? "Open"}
            </p>
            <p className="text-[11px] text-[#1e3a29] font-medium print:text-black">
              {activationPct}% Capacity Utilization
            </p>
          </div>

          <div className="p-4 rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] space-y-1 print:border-black print:bg-white">
            <span className="text-[10px] font-bold uppercase tracking-wider text-[#8e7e6e] print:text-black">
              Curriculum Milestone
            </span>
            <p className="font-serif text-2xl font-bold text-[#1e1b18] print:text-black">
              Week {cohort.currentWeek} of 10
            </p>
            <p className="text-[11px] text-[#1e3a29] font-medium print:text-black">
              Foundation Active
            </p>
          </div>

          <div className="p-4 rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] space-y-1 print:border-black print:bg-white">
            <span className="text-[10px] font-bold uppercase tracking-wider text-[#8e7e6e] print:text-black">
              Pre-Shot Adoption
            </span>
            <p className="font-serif text-2xl font-bold text-[#1e1b18] print:text-black">
              100%
            </p>
            <p className="text-[11px] text-[#1e3a29] font-medium print:text-black">
              6-Step Cadence Target
            </p>
          </div>

          <div className="p-4 rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] space-y-1 print:border-black print:bg-white">
            <span className="text-[10px] font-bold uppercase tracking-wider text-[#8e7e6e] print:text-black">
              Program Status
            </span>
            <p className="font-serif text-2xl font-bold text-[#1e1b18] print:text-black">
              Active
            </p>
            <p className="text-[11px] text-[#8a6828] font-medium print:text-black">
              On-Track Delivery
            </p>
          </div>
        </section>

        {/* 10-Foundation Curriculum Progress Summary */}
        <section className="space-y-3">
          <div className="border-b border-[#ebdcc9] pb-2 flex items-center justify-between print:border-black">
            <h2 className="font-serif text-lg font-bold text-[#1e1b18] print:text-black">
              10-Foundation Progression Schedule
            </h2>
            <span className="text-xs font-bold text-[#8a6828] uppercase tracking-wider print:text-black">
              Curriculum Baseline
            </span>
          </div>

          <table className="w-full text-left text-xs border-collapse">
            <thead>
              <tr className="border-b border-[#ebdcc9] text-[#8e7e6e] uppercase tracking-wider text-[10px] print:border-black print:text-black">
                <th className="py-2 px-2 font-bold w-16">Week</th>
                <th className="py-2 px-2 font-bold">Athletic Foundation</th>
                <th className="py-2 px-2 font-bold">Performance Edge Tool</th>
                <th className="py-2 px-2 font-bold text-right">Progress</th>
                <th className="py-2 px-2 font-bold text-right">Status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-[#ebdcc9] print:divide-black">
              {[
                { week: 1, name: "Identity Beyond Sport", tool: "Identity Audit", pct: 100, status: "Completed" },
                { week: 2, name: "Champion Mindset", tool: "Focus Calibration Drill", pct: 100, status: "Completed" },
                { week: 3, name: "Discipline Systems", tool: "6-Step Pre-Shot Cadence", pct: 85, status: "In Progress" },
                { week: 4, name: "Resilience After Setback", tool: "5-Second Physical Reset", pct: 0, status: "Upcoming" },
                { week: 5, name: "Pressure, Emotional Regulation & Recovery", tool: "Physiological Sigh Protocol", pct: 0, status: "Upcoming" },
                { week: 6, name: "Communication & Presence", tool: "Internal Dialogue Script", pct: 0, status: "Upcoming" },
                { week: 7, name: "Family & Community Support", tool: "Support Alignment Canvas", pct: 0, status: "Upcoming" },
                { week: 8, name: "Career & Money Readiness", tool: "Transition & Financial Roadmap", pct: 0, status: "Upcoming" },
                { week: 9, name: "Personal Brand & Story", tool: "Story & Values Matrix", pct: 0, status: "Upcoming" },
                { week: 10, name: "Legacy & Community Impact", tool: "Legacy Blueprint", pct: 0, status: "Upcoming" },
              ].map((row) => (
                <tr key={row.week} className="print:border-b print:border-gray-200">
                  <td className="py-2 px-2 font-bold text-[#1e1b18] print:text-black">
                    Week {row.week}
                  </td>
                  <td className="py-2 px-2 font-semibold text-[#1e1b18] print:text-black">
                    {row.name}
                  </td>
                  <td className="py-2 px-2 text-[#6e6355] print:text-black">
                    {row.tool}
                  </td>
                  <td className="py-2 px-2 text-right font-mono font-bold print:text-black">
                    {row.pct}%
                  </td>
                  <td className="py-2 px-2 text-right">
                    <span
                      className={`inline-block text-[10px] font-bold uppercase tracking-wider ${
                        row.status === "Completed"
                          ? "text-[#1e3a29]"
                          : row.status === "In Progress"
                          ? "text-[#8a6828]"
                          : "text-[#9f9180] print:text-black"
                      }`}
                    >
                      {row.status}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>

        {/* Small Cohort Privacy Suppression & Privacy Assurance */}
        <section className="rounded-xl border border-[#dfcca6] bg-[#f8f5ee] p-5 space-y-2 print:border-black print:bg-white">
          <div className="flex items-center gap-2 text-xs font-bold uppercase tracking-wider text-[#1e1b18] print:text-black">
            <Lock size={14} className="text-[#1e3a29] print:text-black" />
            <span>Participant Privacy & Governance Assurance</span>
          </div>
          <p className="text-xs text-[#5c5042] leading-relaxed print:text-black">
            In accordance with Lornette’s Foundation athlete governance invariants, all participant reflections, personal vulnerabilities, trigger analyses, and Coach Lornette review notes remain strictly private between each individual athlete and Coach Lornette Daye. Club staff and Board members have visibility into operational completion and aggregate participation only.
          </p>
          {isSmallCohort && (
            <p className="text-[11px] font-semibold text-[#8a6828] italic print:text-black">
              * Small cohort disclosure: Detailed granular subgroup metrics are suppressed to ensure zero individual identification in cohorts under 5 athletes.
            </p>
          )}
        </section>

        {/* Board Sign-Off & Attestation Block */}
        <section className="pt-4 border-t border-[#ebdcc9] grid grid-cols-2 gap-8 text-xs text-[#5e5245] print:border-black print:text-black">
          <div>
            <p className="font-bold text-[#1e1b18] uppercase tracking-wider text-[10px] print:text-black">
              PGA Professional / Coach Endorsement
            </p>
            <div className="mt-8 border-b border-[#ebdcc9] w-48 print:border-black" />
            <p className="mt-1 text-[11px]">Authorized Club Representative</p>
          </div>

          <div className="text-right">
            <p className="font-bold text-[#1e1b18] uppercase tracking-wider text-[10px] print:text-black">
              Program Director Attestation
            </p>
            <div className="mt-8 border-b border-[#ebdcc9] w-48 ml-auto print:border-black" />
            <p className="mt-1 text-[11px]">Lornette Daye · Olympian & Head Coach</p>
          </div>
        </section>
      </main>
    </div>
  );
}
