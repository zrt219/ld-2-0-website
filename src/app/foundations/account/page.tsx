"use client";

import { useState } from "react";
import Link from "next/link";
import { LearnerShell } from "@/components/foundations/learner/LearnerShell";
import { useFoundationsStore } from "@/lib/foundations/store";
import {
  CheckCircle2,
  LogOut,
  Save,
  ShieldCheck,
} from "lucide-react";

export default function FoundationsAccountPage() {
  const { activeAthlete, updateAthleteProfile } = useFoundationsStore();

  const [name, setName] = useState(activeAthlete?.golferName || "Alex Harrison");
  const [email, setEmail] = useState(activeAthlete?.email || "alex.harrison@golfclub.com");
  const [homeClub, setHomeClub] = useState(activeAthlete?.club || "Capilano Golf and Country Club");
  const [handicap, setHandicap] = useState(activeAthlete?.handicap || "2.4 Index");
  const [division, setDivision] = useState(activeAthlete?.division || "Tournament Amateur");
  const [coachName, setCoachName] = useState(activeAthlete?.coachName || "David Miller, PGA of Canada");
  const [emailNotifications, setEmailNotifications] = useState(true);
  const [isSaved, setIsSaved] = useState(false);

  // Sync state if active athlete ID changes
  const [prevAthleteId, setPrevAthleteId] = useState(activeAthlete?.id);
  if (activeAthlete && activeAthlete.id !== prevAthleteId) {
    setPrevAthleteId(activeAthlete.id);
    setName(activeAthlete.golferName);
    setEmail(activeAthlete.email);
    setHomeClub(activeAthlete.club);
    setHandicap(activeAthlete.handicap);
    setDivision(activeAthlete.division);
    setCoachName(activeAthlete.coachName);
  }

  const handleSave = (e: React.FormEvent) => {
    e.preventDefault();
    updateAthleteProfile({
      golferName: name,
      email,
      club: homeClub,
      handicap,
      division,
      coachName,
    });
    setIsSaved(true);
    setTimeout(() => setIsSaved(false), 3500);
  };

  return (
    <LearnerShell>
      <div className="p-4 sm:p-6 lg:p-8 max-w-5xl mx-auto space-y-6">
        {/* Top Header */}
        <section className="relative overflow-hidden rounded-2xl border border-[#dfcca6] bg-[#fbf9f4] p-6 sm:p-8 shadow-[0_4px_24px_rgba(30,24,15,0.04)]">
          <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
            <div>
              <p className="font-sans text-[11px] font-bold uppercase tracking-[0.28em] text-[#8e7e6e]">
                PARTICIPANT PROFILE & CLUB AFFILIATION
              </p>
              <h1 className="mt-1 font-serif text-3xl sm:text-4xl font-semibold tracking-tight text-[#1e1b18]">
                Account & Settings
              </h1>
              <p className="mt-2 font-sans text-xs sm:text-sm text-[#665a4c]">
                Manage your tournament division, PGA teaching professional alignment, and cohort preferences.
              </p>
            </div>

            <div className="inline-flex items-center gap-2 rounded-full border border-[rgba(198,165,92,0.4)] bg-[#f5ede2] px-3.5 py-1.5 text-xs font-semibold text-[#1e3a29] shadow-xs">
              <ShieldCheck size={15} className="text-[#1e3a29]" />
              <span>Active Cohort · 10-Week Guided</span>
            </div>
          </div>
        </section>

        {/* Form Details */}
        <form onSubmit={handleSave} className="rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-6 sm:p-8 shadow-[0_2px_12px_rgba(30,24,15,0.03)] space-y-6">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
            <div>
              <label className="block text-xs font-bold uppercase tracking-wider text-[#4e4337] mb-1.5">
                Participant Full Name
              </label>
              <input
                type="text"
                value={name}
                onChange={(e) => setName(e.target.value)}
                className="w-full rounded-md border border-[#dac8b2] bg-white p-3 text-sm text-[#1e1b18] shadow-xs focus:border-[var(--gold-dark)] focus:outline-none"
              />
            </div>

            <div>
              <label className="block text-xs font-bold uppercase tracking-wider text-[#4e4337] mb-1.5">
                Registered Email
              </label>
              <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="w-full rounded-md border border-[#dac8b2] bg-white p-3 text-sm text-[#1e1b18] shadow-xs focus:border-[var(--gold-dark)] focus:outline-none"
              />
            </div>

            <div>
              <label className="block text-xs font-bold uppercase tracking-wider text-[#4e4337] mb-1.5">
                Home Golf Club / Academy
              </label>
              <input
                type="text"
                value={homeClub}
                onChange={(e) => setHomeClub(e.target.value)}
                className="w-full rounded-md border border-[#dac8b2] bg-white p-3 text-sm text-[#1e1b18] shadow-xs focus:border-[var(--gold-dark)] focus:outline-none"
              />
            </div>

            <div>
              <label className="block text-xs font-bold uppercase tracking-wider text-[#4e4337] mb-1.5">
                Current Handicap Index & Division
              </label>
              <input
                type="text"
                value={handicap}
                onChange={(e) => setHandicap(e.target.value)}
                className="w-full rounded-md border border-[#dac8b2] bg-white p-3 text-sm text-[#1e1b18] shadow-xs focus:border-[var(--gold-dark)] focus:outline-none"
              />
            </div>

            <div>
              <label className="block text-xs font-bold uppercase tracking-wider text-[#4e4337] mb-1.5">
                PGA Teaching Professional (Alignment)
              </label>
              <input
                type="text"
                value={coachName}
                onChange={(e) => setCoachName(e.target.value)}
                className="w-full rounded-md border border-[#dac8b2] bg-white p-3 text-sm text-[#1e1b18] shadow-xs focus:border-[var(--gold-dark)] focus:outline-none"
              />
            </div>

            <div>
              <label className="block text-xs font-bold uppercase tracking-wider text-[#4e4337] mb-1.5">
                Tournament Division
              </label>
              <select
                value={division}
                onChange={(e) => setDivision(e.target.value)}
                className="w-full rounded-md border border-[#dac8b2] bg-white p-3 text-sm text-[#1e1b18] shadow-xs focus:border-[var(--gold-dark)] focus:outline-none"
              >
                <option>Tournament Amateur</option>
                <option>Collegiate Athlete (NCAA / U Sports)</option>
                <option>Junior Elite Pathway</option>
                <option>Club Championship Division</option>
              </select>
            </div>
          </div>

          <div className="pt-4 border-t border-[#ebdcc9]">
            <h3 className="font-serif text-base font-semibold text-[#1e1b18] mb-3">
              Cohort Notifications & Coaching Reminders
            </h3>
            <label className="flex items-center gap-3 cursor-pointer">
              <input
                type="checkbox"
                checked={emailNotifications}
                onChange={(e) => setEmailNotifications(e.target.checked)}
                className="h-4 w-4 rounded border-[#dac8b2] text-[#1e3a29] focus:ring-[var(--gold-dark)]"
              />
              <span className="text-xs sm:text-sm text-[#4e4337]">
                Send weekly coaching email prior to live Q&A with Coach Lornette Daye.
              </span>
            </label>
          </div>

          <div className="pt-4 border-t border-[#ebdcc9] flex items-center justify-between">
            <div role="status" aria-live="polite" aria-atomic="true">
              {isSaved ? (
                <span className="inline-flex items-center gap-1.5 text-xs font-semibold text-[#1e3a29]">
                  <CheckCircle2 size={15} aria-hidden="true" />
                  <span>Profile preferences updated.</span>
                </span>
              ) : null}
            </div>
            {!isSaved && (
              <Link
                href="/foundations/login"
                className="inline-flex items-center gap-2 text-xs font-semibold text-[#8a3828] hover:underline"
              >
                <LogOut size={14} aria-hidden="true" />
                <span>Sign Out of Workspace</span>
              </Link>
            )}

            <button
              type="submit"
              className="inline-flex items-center gap-2 rounded-md bg-gradient-to-r from-[#dfc385] via-[#ceab68] to-[#b38f4a] px-6 py-2.5 text-xs font-bold uppercase tracking-[0.14em] text-white shadow-xs hover:brightness-105 transition-all"
            >
              <Save size={15} />
              <span>Save Changes</span>
            </button>
          </div>
        </form>
      </div>
    </LearnerShell>
  );
}
