import {
  Building2,
  CheckCircle2,
  GraduationCap,
  HeartHandshake,
  Medal,
  Trophy,
  Users2,
} from "lucide-react";

import { CTAButton } from "@/components/CTAButton";
import { PageShell } from "@/components/PageShell";
import Image from "next/image";
import { FoundationsSubNav } from "@/components/foundations/FoundationsSubNav";
import { createMetadata } from "@/content/site";

export const metadata = createMetadata(
  "Lornette’s Foundation For Clubs & Teams",
  "Partner with Lornette Daye to deliver athlete-development keynotes, member clinics, guided cohorts, and institutional athletic partnerships.",
  "/foundations/clubs",
);

const audiences = [
  {
    title: "Golf & Country Clubs",
    description:
      "Member clinics, junior golf academy intensives, and tournament banquet keynotes designed to elevate competitive play and member engagement.",
    icon: Trophy,
  },
  {
    title: "Sport Academies & High-Performance Centres",
    description:
      "Structured mental game and mistake recovery modules integrated into full-time athlete training schedules.",
    icon: Medal,
  },
  {
    title: "Sport Federations & Governing Bodies",
    description:
      "Provincial and national squad clinics on competition preparation, pressure management, and culture building.",
    icon: Building2,
  },
  {
    title: "Collegiate & Competitive Teams",
    description:
      "Pre-season retreats and team cohesion workshops teaching accountability, shared standards, and resilient communication.",
    icon: Users2,
  },
  {
    title: "Schools & Athletic Departments",
    description:
      "Whole-athlete character, discipline, and championship composure keynotes for student-athletes, coaches, and parents.",
    icon: GraduationCap,
  },
  {
    title: "Athlete-Development Organizations",
    description:
      "Custom partnerships delivering holistic mentorship, life-skills training, and leadership frameworks beyond sport.",
    icon: HeartHandshake,
  },
];

const engagementFormats = [
  {
    format: "Keynote Presentation",
    timeframe: "60–90 Minutes",
    focus: "Main-Stage Inspiration & Practical Principles",
    description:
      "High-energy address for banquets, seasonal kickoffs, or coach symposiums introducing the core principles of elite composure and resilience.",
  },
  {
    format: "Workshop & Member Clinic",
    timeframe: "90 Minutes to 2 Hours",
    focus: "Interactive & Applied Skill Building",
    description:
      "Hands-on clinic breaking down pre-shot routines, pressure breathing, decision-making discipline, and the five-second reset protocol.",
  },
  {
    format: "Guided Cohort Experience",
    timeframe: "10 Weeks Structured",
    focus: "Field Assignments & Longitudinal Growth",
    description:
      "A 10-week guided athlete development program combining 10 Foundation modules, practical field assignments, and accountability tracking for competitive athletes.",
  },
  {
    format: "Athlete Development Program",
    timeframe: "Multi-Session Seasonal",
    focus: "Comprehensive Whole-Athlete Curriculum",
    description:
      "A seasonal partnership embedding Lornette’s Foundation curriculum into your academy or team’s ongoing training calendar.",
  },
  {
    format: "Club / Federation Partnership",
    timeframe: "Annual / Strategic",
    focus: "Institutional Alignment & Culture Integration",
    description:
      "A customized institutional partnership encompassing coach alignment sessions, athlete clinics, leadership workshops, and aggregate reporting.",
  },
];

const verifiedProof = [
  "40+ Years of Elite Sport, National Coaching & Mentoring",
  "Over 500 Athletes Mentored and Coached Across Disciplines",
  "150+ International-Level Competitors Guided",
  "Canadian National Sprint Champion & National Coach",
  "Diversity Award Winner Committed to Inclusion in Sport",
];

export default function FoundationsClubsPage() {
  return (
    <PageShell>
      <main className="bg-[var(--ivory)] text-[var(--ink)]">
        <FoundationsSubNav />

        {/* Hero */}
        <section className="relative overflow-hidden border-b border-[rgba(198,165,92,0.35)] bg-[var(--ivory)] px-4 py-14 sm:px-6 lg:px-8 lg:py-20">
          <div className="pointer-events-none absolute inset-0 bg-[linear-gradient(115deg,rgba(255,255,255,0.92)_0%,rgba(250,247,240,0.84)_46%,rgba(232,221,203,0.58)_100%)]" />

          <div className="relative mx-auto max-w-7xl">
            <div className="grid gap-12 lg:grid-cols-12 lg:items-center">
              <div className="lg:col-span-7">
                <div className="flex flex-wrap items-center gap-2">
                  <span className="border border-[rgba(198,165,92,0.48)] bg-white/70 px-3.5 py-1.5 text-xs font-bold uppercase tracking-[0.24em] text-[var(--gold-dark)] shadow-sm">
                    Lornette’s Foundation
                  </span>
                  <span className="text-xs font-bold uppercase tracking-[0.2em] text-[#7d7164]">
                    Institutional Partnerships
                  </span>
                </div>

                <h1 className="mt-6 font-serif text-4xl leading-[1.02] text-balance text-[var(--ink)] sm:text-6xl lg:text-[3.8rem]">
                  Lornette’s Foundation for Clubs &amp; Teams
                </h1>

                <p className="mt-5 font-serif text-2xl text-[var(--gold-dark)] sm:text-3xl">
                  Develop stronger athletes. Build stronger environments.
                </p>

                <p className="mt-6 text-base leading-8 text-[#554b40] sm:text-lg">
                  Partner with Lornette Daye to bring elite athletic perspective, structured mental performance clinics, and whole-athlete development experiences to your club, academy, federation, school, or sport organization.
                </p>

                <div className="mt-8 flex flex-col gap-3 sm:flex-row">
                  <CTAButton href="/book">DISCUSS A PARTNERSHIP</CTAButton>
                  <CTAButton href="/speaker-kit" variant="secondary">
                    VIEW SPEAKER &amp; PROGRAM KIT
                  </CTAButton>
                </div>
              </div>

              <div className="relative lg:col-span-5">
                <div className="relative w-full aspect-[4/5] overflow-hidden border border-[rgba(198,165,92,0.42)] bg-[linear-gradient(180deg,#fffdf8_0%,#f5efe4_100%)] shadow-[0_28px_110px_rgba(23,20,18,0.14)]">
                  <Image
                    src="/foundations/lornette-foundations-executive-desk-runner.png"
                    alt="Lornette Daye in executive study with performance runners and championship trophies"
                    fill
                    priority
                    sizes="(max-width: 1024px) 100vw, 42vw"
                    className="object-cover"
                    style={{ objectPosition: "90% 18%" }}
                  />
                  <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/40" />
                  <div className="absolute inset-x-0 bottom-0 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(18,15,13,0.82)] p-4 sm:p-5 backdrop-blur-md shadow-2xl">
                    <p className="text-[11px] font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
                      Institutional Advisory
                    </p>
                    <p className="mt-1 font-serif text-base text-white sm:text-lg">
                      Executive &amp; Athletic Leadership
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Audiences Served */}
        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <div className="text-center max-w-3xl mx-auto">
              <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--gold-dark)]">
                Tailored Engagements
              </p>
              <h2 className="mt-4 font-serif text-4xl leading-tight text-[var(--ink)] sm:text-5xl">
                Organizations We Partner With
              </h2>
              <p className="mt-4 text-base leading-8 text-[#675d50]">
                Every engagement is customized to align with your organization&apos;s training calendar, coaching staff, and competitive objectives.
              </p>
            </div>

            <div className="mt-14 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
              {audiences.map((aud) => {
                const Icon = aud.icon;
                return (
                  <article
                    key={aud.title}
                    className="border border-[rgba(198,165,92,0.34)] bg-white p-8 shadow-[0_16px_50px_rgba(23,20,18,0.05)] transition duration-200 hover:-translate-y-1 hover:border-[var(--champagne)]"
                  >
                    <Icon size={28} aria-hidden="true" className="text-[var(--gold-dark)]" />
                    <h3 className="mt-5 font-serif text-2xl text-[var(--ink)]">
                      {aud.title}
                    </h3>
                    <p className="mt-3 text-sm leading-7 text-[#675d50]">
                      {aud.description}
                    </p>
                  </article>
                );
              })}
            </div>
          </div>
        </section>

        {/* Engagement Formats */}
        <section className="border-y border-[var(--line)] bg-[var(--sand)]/40 px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <div className="grid gap-8 lg:grid-cols-[0.45fr_0.55fr] lg:items-end">
              <div>
                <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--gold-dark)]">
                  Flexible Delivery
                </p>
                <h2 className="mt-4 font-serif text-4xl leading-tight text-[var(--ink)] sm:text-5xl">
                  Possible Engagement Formats
                </h2>
              </div>
              <p className="text-base leading-8 text-[#675d50]">
                From a single high-impact keynote to full seasonal cohort partnerships, choose the format that fits your organization&apos;s goals.
              </p>
            </div>

            <div className="mt-12 grid gap-6 md:grid-cols-2 lg:grid-cols-3">
              {engagementFormats.map((fmt) => (
                <div
                  key={fmt.format}
                  className="border border-[rgba(198,165,92,0.38)] bg-white p-7 shadow-[0_16px_50px_rgba(23,20,18,0.06)] flex flex-col justify-between"
                >
                  <div>
                    <span className="text-xs font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)]">
                      {fmt.timeframe}
                    </span>
                    <h3 className="mt-3 font-serif text-2xl text-[var(--ink)]">
                      {fmt.format}
                    </h3>
                    <p className="mt-1 text-xs font-semibold uppercase tracking-[0.12em] text-[#7d7164]">
                      {fmt.focus}
                    </p>
                    <p className="mt-4 text-sm leading-7 text-[#675d50]">
                      {fmt.description}
                    </p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Verified Credibility */}
        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <div className="grid gap-12 lg:grid-cols-[0.9fr_1.1fr] lg:items-center">
              <div>
                <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--gold-dark)]">
                  Proven Experience
                </p>
                <h2 className="mt-4 font-serif text-4xl leading-tight text-[var(--ink)] sm:text-5xl">
                  Why Leaders Choose Lornette
                </h2>
                <p className="mt-6 text-base leading-8 text-[#554b40] sm:text-lg">
                  Lornette brings lived championship experience combined with decades of practical coaching across hundreds of competitive athletes. Her sessions deliver usable mental tools that athletes understand immediately and coaches respect.
                </p>
                <div className="mt-8">
                  <CTAButton href="/book">DISCUSS A PARTNERSHIP</CTAButton>
                </div>
              </div>

              <div className="border border-[rgba(198,165,92,0.38)] bg-white p-8 shadow-[0_20px_70px_rgba(23,20,18,0.06)]">
                <p className="text-xs font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)]">
                  Verified Track Record
                </p>
                <div className="mt-6 grid gap-4">
                  {verifiedProof.map((claim) => (
                    <div key={claim} className="flex gap-3 text-sm font-semibold text-[var(--charcoal)]">
                      <CheckCircle2 size={18} aria-hidden="true" className="shrink-0 text-[var(--gold-dark)] mt-0.5" />
                      <span>{claim}</span>
                    </div>
                  ))}
                </div>
              </div>
            </div>

            {/* Editorial Feature: Elevating Institutional Culture */}
            <div className="mt-14 overflow-hidden border border-[rgba(198,165,92,0.36)] bg-white shadow-[0_16px_50px_rgba(23,20,18,0.06)] grid lg:grid-cols-12">
              <div className="relative aspect-[16/9] lg:aspect-auto lg:col-span-6 min-h-[320px]">
                <Image
                  src="/foundations/lornette-foundations-tactical-playbook-board.png"
                  alt="Lornette Daye holding a tactical playbook beside an architectural glass strategy board in an executive athletic facility"
                  fill
                  sizes="(max-width: 1024px) 100vw, 50vw"
                  className="object-cover"
                  style={{ objectPosition: "75% 20%" }}
                />
                <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/20" />
              </div>
              <div className="p-8 lg:p-12 lg:col-span-6 flex flex-col justify-center bg-[linear-gradient(135deg,#fffdf8_0%,#faf6ee_100%)]">
                <span className="text-xs font-bold uppercase tracking-[0.22em] text-[var(--gold-dark)]">
                  Institutional Elevation
                </span>
                <h3 className="mt-2 font-serif text-3xl text-[var(--ink)]">
                  Building Next-Level Championship Standards
                </h3>
                <p className="mt-4 text-base leading-relaxed text-[#5e5346]">
                  Whether preparing collegiate rosters for post-season pressure or helping country clubs build distinction through elite member programming, Lornette brings world-class coaching structure that leaves a permanent cultural imprint on your organization.
                </p>
                <div className="mt-6">
                  <CTAButton href="/book">
                    DISCUSS A PARTNERSHIP
                  </CTAButton>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Panoramic Closing Bottom Banner */}
        <section className="relative overflow-hidden border-t border-[rgba(198,165,92,0.4)] min-h-[340px] sm:min-h-[400px] flex items-center px-4 py-16 text-center text-[var(--ivory)] sm:px-6 lg:px-8 lg:py-24">
          <div className="absolute inset-0 pointer-events-none overflow-hidden">
            <Image
              src="/foundations/banners/scenic-stadium-mountains.jpg"
              alt="Athletics stadium overlooking majestic alpine mountain range"
              role="presentation"
              fill
              quality={95}
              sizes="100vw"
              className="object-cover object-center"
            />
            <div className="absolute inset-0 bg-gradient-to-t from-black/85 via-black/60 to-black/75" />
          </div>

          <div className="relative z-10 mx-auto max-w-4xl">
            <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--champagne)]">
              Partner With Us
            </p>
            <h2 className="mt-4 font-serif text-4xl leading-tight text-white sm:text-5xl lg:text-6xl">
              Equip Your Organization for Championship Culture
            </h2>
            <p className="mt-6 max-w-2xl mx-auto text-lg leading-8 text-[#d8cdbb]">
              Contact Lornette Daye to discuss availability, customized clinic formats, and collaborative partnerships for your upcoming season.
            </p>
            <div className="mt-9 flex flex-col justify-center gap-4 sm:flex-row">
              <CTAButton href="/book">DISCUSS A PARTNERSHIP</CTAButton>
              <CTAButton
                href="/speaker-kit"
                variant="secondary"
                className="border-white/30 text-white hover:bg-white/10"
              >
                VIEW SPEAKER & PROGRAM KIT
              </CTAButton>
            </div>
          </div>
        </section>
      </main>
    </PageShell>
  );
}
