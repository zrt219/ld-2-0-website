import Image from "next/image";
import Link from "next/link";
import { ArrowRight, Calendar, CheckCircle2, FileText, ShieldCheck, Video } from "lucide-react";
import { CTAButton } from "@/components/CTAButton";
import { FoundationsSubNav } from "@/components/foundations/FoundationsSubNav";
import { GolfRegistrationForm } from "@/components/foundations/GolfRegistrationForm";
import { PageShell } from "@/components/PageShell";
import { SectionHeader } from "@/components/SectionHeader";
import { createMetadata } from "@/content/site";

export const metadata = createMetadata(
  "Lornette’s Foundation Golf | 10-Week Guided Program",
  "The flagship 10-week guided athlete development program for competitive golfers, elite juniors, and club players led by Olympic-level coach Lornette Daye. Powered by the Performance Edge Framework.",
  "/foundations/golf/program",
);

const curriculumWeeks = [
  {
    week: "Week 1",
    title: "Identity Beyond Sport",
    pillars: "Athlete Identity & Self-Worth Beyond Score",
    sequence: "Athlete Identity → Scorecard Detachment → Foundational Mental Boundary",
    assignment: "Reflection on self-worth anchors independent of golf scorecards and rankings.",
    lornetteMessage: "Establishing your non-negotiable mental boundary.",
    image: "/foundations/golf/curriculum/week-01-dew-flag.jpg",
    imageAlt: "Championship golf ball resting on dewy putting green at dawn",
  },
  {
    week: "Week 2",
    title: "Champion Mindset",
    pillars: "Focus, Visualization & Evidence-Based Confidence",
    sequence: "Attention Dial → Sensory Visualization → Evidence Ledger",
    assignment: "9-hole focus toggle drill; sensory visualization prior to execution.",
    lornetteMessage: "Focus control and deliberate mental imagery.",
    image: "/foundations/golf/curriculum/week-02-fairway-sunrise.jpg",
    imageAlt: "Golfer walking golden morning fairway with focused champion mindset",
  },
  {
    week: "Week 3",
    title: "Discipline Systems",
    pillars: "Pre-Shot Routine & Deliberate Practice",
    sequence: "Assess → Decide → Visualize → Reset → Execute → Release",
    assignment: "Execute pre-shot routine on every full shot for 9 holes; log completion consistency.",
    lornetteMessage: "Repeatable execution under tournament heat.",
    image: "/foundations/golf/curriculum/week-03-address-stance.jpg",
    imageAlt: "Golfer dialed into deliberate pre-shot routine and address stance",
  },
  {
    week: "Week 4",
    title: "Resilience After Setback",
    pillars: "Mistake Reset & The Next Shot Principle",
    sequence: "Acknowledge → Evaluate → Release → Reset → Recommit",
    assignment: "5-second emotional reset drill; audit recovery time after missed greens or bogeys.",
    lornetteMessage: "The Next Shot Principle: Your previous shot cannot hit your next shot.",
    image: "/foundations/golf/curriculum/week-04-keynote-fairway.jpg",
    imageAlt: "Championship fairway with calm bunker and golden hour tree shadows",
  },
  {
    week: "Week 5",
    title: "Pressure, Emotional Regulation & Recovery",
    pillars: "Pressure Response & Physiological Recovery",
    sequence: "Notice → Breathe → Target → Commit",
    assignment: "The Pressure 5 field drill: executing deliberate pressure simulations on practice grounds.",
    lornetteMessage: "Physiological self-regulation under stress.",
    image: "/foundations/golf/curriculum/week-05-sunrise-lake.jpg",
    imageAlt: "Serene golf course lake reflecting golden morning sunrise with morning mist",
  },
  {
    week: "Week 6",
    title: "Communication & Presence",
    pillars: "Self-Talk & Tournament Demeanor",
    sequence: "Internal Dialogue → Coach Alignment → Competitive Presence",
    assignment: "On-course internal dialogue audit; competition presence and posture checklist.",
    lornetteMessage: "Body language, self-talk, and executive presence.",
    image: "/foundations/golf/curriculum/week-06-tour-bag.jpg",
    imageAlt: "Luxury tour golf bag with precision irons on manicured fairway turf",
  },
  {
    week: "Week 7",
    title: "Family & Community Support",
    pillars: "Expectation Management & Support Circle",
    sequence: "Ecosystem Mapping → Boundary Agreements → Team Alignment",
    assignment: "Map athlete support ecosystem and define healthy communication boundaries.",
    lornetteMessage: "Aligning expectations with family, coaches, and peers.",
    image: "/foundations/golf/curriculum/week-07-coastal-bag.jpg",
    imageAlt: "Coastal golf green with tournament pin and tour clubs against evening ocean",
  },
  {
    week: "Week 8",
    title: "Career & Money Readiness",
    pillars: "Professional Mindset & Life Transition",
    sequence: "Career Roadmap → Professional Discipline → Tournament Budgeting",
    assignment: "Personal career roadmap and professional readiness inventory.",
    lornetteMessage: "Thinking long-term about your athletic career.",
    image: "/foundations/golf/curriculum/week-08-mentorship.jpg",
    imageAlt: "Coach Lornette Daye in focused one-on-one mentorship dialogue with an athlete",
  },
  {
    week: "Week 9",
    title: "Personal Brand & Story",
    pillars: "Authentic Voice & Representative Excellence",
    sequence: "Authentic Voice → Representative Conduct → Narrative Ownership",
    assignment: "Craft personal mission statement and core story pillars.",
    lornetteMessage: "Public presence, integrity, and authentic representation.",
    image: "/foundations/golf/curriculum/week-09-terrace-vista.jpg",
    imageAlt: "Clubhouse terrace view overlooking championship golf course and distant mountains",
  },
  {
    week: "Week 10",
    title: "Legacy & Community Impact",
    pillars: "Mentorship, Leadership & Capstone Plan",
    sequence: "Capstone Performance Plan → Mentorship → Leadership Commitment",
    assignment: "Complete My 30-Day Performance Plan and define community contribution goals.",
    lornetteMessage: "Capstone 30-Day Performance Plan: Translating preparation into tournament execution.",
    image: "/foundations/golf/curriculum/week-10-ocean-links.jpg",
    imageAlt: "Golfer holding club overlooking majestic coastal ocean cliffs and championship green",
  },
];

const programComponents = [
  {
    icon: Video,
    title: "10 Foundation Video Briefings",
    description: "High-density strategic coaching modules and practical Performance Edge tool frameworks delivered directly by Lornette Daye.",
  },
  {
    icon: FileText,
    title: "Tour-Grade Workbooks & Audits",
    description: "Printable and digital performance logs for pre-shot cadence timing, in-round emotional audits, and margin calculations.",
  },
  {
    icon: Calendar,
    title: "Live Mastermind Sessions",
    description: "Opening kickoff, mid-season calibration, and capstone synthesis coaching sessions led directly by Lornette Daye with cohort peers.",
  },
  {
    icon: ShieldCheck,
    title: "The Evidence Ledger",
    description: "A permanent psychological framework documenting executed routines and handled pressure to build unshakeable tournament conviction.",
  },
];

export default function GolfProgramPage() {
  return (
    <PageShell>
      <main className="bg-[var(--ivory)] text-[var(--ink)]">
        <FoundationsSubNav />

        {/* Hero Section */}
        <section className="relative overflow-hidden border-b border-[rgba(198,165,92,0.35)] bg-[var(--ivory)] px-4 py-14 sm:px-6 lg:px-8 lg:py-20">
          <div className="pointer-events-none absolute inset-0 bg-[linear-gradient(115deg,rgba(255,255,255,0.94)_0%,rgba(250,247,240,0.85)_46%,rgba(232,221,203,0.6)_100%)]" />

          <div className="relative mx-auto max-w-7xl">
            <div className="grid gap-12 lg:grid-cols-12 lg:items-center">
              <div className="lg:col-span-7">
                <div className="flex flex-wrap items-center gap-2">
                  <span className="border border-[rgba(198,165,92,0.48)] bg-white/70 px-3.5 py-1.5 text-xs font-bold uppercase tracking-[0.24em] text-[var(--gold-dark)] shadow-sm">
                    Lornette’s Foundation Golf
                  </span>
                  <span className="text-xs font-bold uppercase tracking-[0.2em] text-[#7d7164]">
                    10-Week Guided Program
                  </span>
                </div>

                <h1 className="mt-6 font-serif text-4xl leading-[1.04] text-balance text-[var(--ink)] sm:text-6xl">
                  Lornette’s Foundation Golf: 10-Week Guided Program
                </h1>

                <p className="mt-4 text-sm font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)]">
                  Powered by the Performance Edge Framework
                </p>

                <p className="mt-6 text-base leading-8 text-[#554b40] sm:text-lg">
                  The comprehensive mental conditioning and athlete development cohort designed for tournament competitors, elite junior golfers, and dedicated club players. Over ten weeks, master the 10 Athletic Foundations and practical Performance Edge tools to transform your relationship with pressure, mistakes, and competition.
                </p>

                <div className="mt-8 flex flex-wrap gap-4 text-xs font-semibold text-[#6e6355]">
                  <div className="flex items-center gap-2 border border-[rgba(198,165,92,0.4)] bg-white/60 px-3 py-1.5">
                    <Calendar size={14} className="text-[var(--gold-dark)]" />
                    <span>Format: 10 Weeks Cohort-Based</span>
                  </div>
                  <div className="flex items-center gap-2 border border-[rgba(198,165,92,0.4)] bg-white/60 px-3 py-1.5">
                    <Video size={14} className="text-[var(--gold-dark)]" />
                    <span>Delivery: Online Modules + Live Coaching Sessions</span>
                  </div>
                  <div className="flex items-center gap-2 border border-[rgba(198,165,92,0.4)] bg-white/60 px-3 py-1.5">
                    <FileText size={14} className="text-[var(--gold-dark)]" />
                    <span>Application: Structured On-Course Field Drills</span>
                  </div>
                </div>

                <div className="mt-10 flex flex-col gap-3 sm:flex-row">
                  <CTAButton href="/foundations/golf/register">Register for the Next Cohort</CTAButton>
                  <CTAButton href="/foundations/golf" variant="secondary">
                    Explore Program Overview
                  </CTAButton>
                </div>
              </div>

              <div className="relative lg:col-span-5">
                <div className="relative w-full aspect-[4/5] overflow-hidden border border-[rgba(198,165,92,0.42)] bg-[linear-gradient(180deg,#fffdf8_0%,#f5efe4_100%)] shadow-[0_28px_110px_rgba(23,20,18,0.14)]">
                  <Image
                    src="/foundations/golf/lornette-golf-tournament-prep.png"
                    alt="Lornette Daye on the championship tournament tee line preparing players for competition"
                    fill
                    priority
                    sizes="(max-width: 1024px) 92vw, 40vw"
                    className="object-cover"
                    style={{ objectPosition: "80% 18%" }}
                  />
                  <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/40" />
                  <div className="absolute inset-x-0 bottom-0 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(18,15,13,0.82)] p-4 sm:p-5 backdrop-blur-md shadow-2xl">
                    <p className="text-[11px] font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
                      Tournament Readiness
                    </p>
                    <p className="mt-1 font-serif text-base text-white sm:text-lg">
                      Preparation From Verified Evidence
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* 10-Week Curriculum */}
        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <SectionHeader
              eyebrow="The 10-Week Journey"
              title="10 Athletic Foundations for Complete Golf Performance"
              body="A systematic 10-week curriculum guiding players through Lornette Daye's established 10 Athletic Foundations, pairing whole-athlete development with practical on-course mental game tools."
            />

            <div className="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-5">
              {curriculumWeeks.map((week) => (
                <div
                  key={week.week}
                  className="group flex flex-col justify-between overflow-hidden border border-[rgba(198,165,92,0.38)] bg-white shadow-[0_16px_40px_rgba(23,20,18,0.04)] transition-all duration-300 hover:border-[rgba(198,165,92,0.65)] hover:shadow-[0_20px_50px_rgba(23,20,18,0.08)]"
                >
                  <div>
                    {/* Top Photographic Card Header */}
                    <div className="relative aspect-[16/10] w-full overflow-hidden border-b border-[rgba(198,165,92,0.3)] bg-[#120f0d]">
                      <Image
                        src={week.image}
                        alt={week.imageAlt}
                        fill
                        sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 20vw"
                        className="object-cover transition-transform duration-500 group-hover:scale-105"
                        quality={90}
                      />
                      <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-black/55 via-black/10 to-transparent" />
                      <div className="absolute top-3 left-3">
                        <span className="border border-[rgba(198,165,92,0.6)] bg-[rgba(18,15,13,0.85)] px-2.5 py-1 text-[11px] font-bold uppercase tracking-[0.2em] text-[var(--champagne)] backdrop-blur-xs shadow-md">
                          {week.week}
                        </span>
                      </div>
                    </div>

                    {/* Content Body */}
                    <div className="p-5 sm:p-6">
                      <h2 className="font-serif text-lg font-semibold leading-snug text-[var(--ink)]">
                        {week.title}
                      </h2>
                      <p className="mt-1 text-[11px] font-bold uppercase tracking-[0.14em] text-[var(--gold-dark)]">
                        {week.pillars}
                      </p>

                      <div className="mt-4 space-y-3">
                        <div className="flex items-start gap-2.5">
                          <CheckCircle2 size={14} className="mt-0.5 shrink-0 text-[var(--gold-dark)]" />
                          <div className="text-xs text-[#5f5446] leading-relaxed">
                            <strong className="font-semibold text-[var(--ink)] block text-[11px] uppercase tracking-wider mb-0.5">
                              Sequence
                            </strong>
                            <span>{week.sequence}</span>
                          </div>
                        </div>

                        <div className="flex items-start gap-2.5">
                          <CheckCircle2 size={14} className="mt-0.5 shrink-0 text-[#b89456]" />
                          <div className="text-xs text-[#5f5446] leading-relaxed">
                            <strong className="font-semibold text-[var(--ink)] block text-[11px] uppercase tracking-wider mb-0.5">
                              Field Drill
                            </strong>
                            <span>{week.assignment}</span>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>

                  <div className="mx-5 mb-5 sm:mx-6 sm:mb-6 border-t border-[var(--line)] pt-3 text-xs text-[#7d7164]">
                    <span className="text-[10px] font-bold uppercase tracking-[0.18em] text-[#8a6828]">Focus: </span>
                    <span className="font-medium text-[var(--ink)]">{week.lornetteMessage}</span>
                  </div>
                </div>
              ))}
            </div>

            {/* Editorial Feature: On-Course Validation */}
            <div className="mt-14 overflow-hidden border border-[rgba(198,165,92,0.36)] bg-white shadow-[0_16px_50px_rgba(23,20,18,0.06)] grid lg:grid-cols-12">
              <div className="p-8 lg:p-12 lg:col-span-6 flex flex-col justify-center bg-[linear-gradient(135deg,#fffdf8_0%,#faf6ee_100%)] order-2 lg:order-1">
                <span className="text-xs font-bold uppercase tracking-[0.22em] text-[var(--gold-dark)]">
                  Turf Application
                </span>
                <h3 className="mt-2 font-serif text-3xl text-[var(--ink)]">
                  On-Course Validation Under Real Stakes
                </h3>
                <p className="mt-4 text-base leading-relaxed text-[#5e5346]">
                  Every weekly lesson is paired with specific field drills performed directly during practice rounds. Golfers test their pre-shot cadence, log internal tension metrics, and build tangible evidence that their mental routine works under tournament pressure.
                </p>
                <div className="mt-6">
                  <CTAButton href="/foundations/golf/register">
                    REGISTER FOR THE NEXT COHORT
                  </CTAButton>
                </div>
              </div>
              <div className="relative aspect-[16/9] lg:aspect-auto lg:col-span-6 min-h-[320px] order-1 lg:order-2">
                <Image
                  src="/foundations/golf/lornette-golf-fairway-mountain-sunset.png"
                  alt="Lornette Daye walking along a championship golf fairway with scenic mountain backdrop at golden sunset"
                  fill
                  sizes="(max-width: 1024px) 100vw, 50vw"
                  className="object-cover"
                  style={{ objectPosition: "27% 18%" }}
                />
                <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/20" />
              </div>
            </div>
          </div>
        </section>

        {/* Program Experience Components */}
        <section className="border-t border-[var(--line)] bg-[#f6f2e8] px-4 py-16 sm:px-6 lg:px-8 lg:py-20">
          <div className="mx-auto max-w-7xl">
            <div className="max-w-3xl">
              <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--gold-dark)]">
                Program Deliverables
              </p>
              <h2 className="mt-3 font-serif text-3xl leading-tight text-[var(--ink)] sm:text-4xl">
                What Each Participant Receives
              </h2>
            </div>

            <div className="mt-8 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
              {programComponents.map((comp) => {
                const Icon = comp.icon;
                return (
                  <div
                    key={comp.title}
                    className="border border-[rgba(198,165,92,0.38)] bg-white p-6 shadow-sm"
                  >
                    <Icon size={24} className="text-[var(--gold-dark)]" />
                    <h3 className="mt-4 font-serif text-xl text-[var(--ink)]">{comp.title}</h3>
                    <p className="mt-2 text-xs leading-6 text-[#675d50]">{comp.description}</p>
                  </div>
                );
              })}
            </div>

            {/* Editorial Feature: Personal Plan Review */}
            <div className="mt-14 overflow-hidden border border-[rgba(198,165,92,0.36)] bg-white shadow-[0_16px_50px_rgba(23,20,18,0.06)] grid lg:grid-cols-12">
              <div className="relative aspect-[16/9] lg:aspect-auto lg:col-span-6 min-h-[320px]">
                <Image
                  src="/foundations/golf/lornette-golf-executive-desk.png"
                  alt="Lornette Daye at executive desk reviewing player competition plan framing championship golf fairway"
                  fill
                  sizes="(max-width: 1024px) 100vw, 50vw"
                  className="object-cover object-top"
                />
                <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/20" />
              </div>
              <div className="p-8 lg:p-12 lg:col-span-6 flex flex-col justify-center bg-[linear-gradient(135deg,#fffdf8_0%,#faf6ee_100%)]">
                <span className="text-xs font-bold uppercase tracking-[0.22em] text-[var(--gold-dark)]">
                  1-on-1 Milestone Deliverable
                </span>
                <h3 className="mt-2 font-serif text-3xl text-[var(--ink)]">
                  Personal Competition Plan Review
                </h3>
                <p className="mt-4 text-base leading-relaxed text-[#5e5346]">
                  Every participant submits their completed Competition Day Plan and Pre-Shot Cadence workbook directly to Lornette Daye. Lornette provides targeted personal feedback to refine arrival sequencing, somatic reset timing, and course-management margins before competition.
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* Embedded Cohort Registration Section */}
        <section id="register" className="scroll-mt-16 border-t border-[var(--line)] bg-[#faf7f2] px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <div className="mx-auto max-w-3xl text-center mb-12 space-y-3">
              <p className="text-xs font-bold uppercase tracking-[0.24em] text-[var(--gold-dark)]">
                Program Registration
              </p>
              <h2 className="font-serif text-3xl sm:text-4xl text-[var(--ink)]">
                Secure Your Spot in the 10-Week Guided Program
              </h2>
              <p className="text-sm sm:text-base text-[#675d50] max-w-2xl mx-auto leading-relaxed">
                Join a cohort of dedicated golfers building tournament composure, discipline systems, and emotional recovery. Or visit our{" "}
                <Link href="/foundations/golf/register" className="font-semibold text-[var(--gold-dark)] hover:underline">
                  dedicated registration page ↗
                </Link>
                .
              </p>
            </div>

            <GolfRegistrationForm />
          </div>
        </section>

        {/* Commercial Ladder Cross-Link */}
        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-20 border-t border-[var(--line)]">
          <div className="mx-auto max-w-7xl">
            <div className="flex flex-col md:flex-row items-center justify-between gap-6 border border-[rgba(198,165,92,0.4)] bg-white p-8">
              <div>
                <p className="text-xs font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)]">
                  For Clubs &amp; Academies
                </p>
                <h3 className="mt-2 font-serif text-2xl text-[var(--ink)]">
                  Interested in Bringing Lornette’s Foundation to Your Entire Golf Club?
                </h3>
                <p className="mt-1 text-sm text-[#675d50]">
                  Explore full club partnerships with custom cohort scheduling and coach integration.
                </p>
              </div>
              <Link
                href="/foundations/golf/club-partnership"
                className="inline-flex items-center gap-2 bg-[var(--ink)] px-6 py-3 text-xs font-bold uppercase tracking-[0.16em] text-[var(--ivory)] hover:bg-[var(--charcoal)] transition shrink-0"
              >
                View Club Partnership <ArrowRight size={14} />
              </Link>
            </div>
          </div>
        </section>

        {/* Panoramic Closing Bottom Banner */}
        <section className="relative overflow-hidden border-t border-[rgba(198,165,92,0.4)] min-h-[340px] sm:min-h-[400px] flex items-center px-4 py-16 text-center text-[var(--ivory)] sm:px-6 lg:px-8 lg:py-24">
          <div className="absolute inset-0 pointer-events-none overflow-hidden">
            <Image
              src="/foundations/golf/scenic-mountain-fairway.jpg"
              alt="Championship golf fairway with mountain backdrop and morning mist"
              role="presentation"
              fill
              quality={95}
              sizes="100vw"
              className="object-cover object-center"
            />
            <div className="absolute inset-0 bg-gradient-to-t from-black/85 via-black/60 to-black/75" />
          </div>

          <div className="relative z-10 mx-auto max-w-3xl">
            <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--champagne)]">
              Next Cohort Starting Soon
            </p>
            <h2 className="mt-4 font-serif text-4xl leading-tight sm:text-5xl text-white">
              Step Onto the First Tee With Earned Certainty
            </h2>
            <p className="mt-4 text-base leading-8 text-[#d8cdbb]">
              Cohort enrollment is strictly capped to ensure direct personal feedback and comprehensive review from Coach Lornette Daye on every player&apos;s competition plan.
            </p>
            <div className="mt-8 flex flex-col justify-center gap-3 sm:flex-row">
              <CTAButton href="/foundations/golf/register">Apply for the Next Guided Cohort</CTAButton>
              <CTAButton
                href="/book"
                variant="secondary"
                className="border-white/30 text-white hover:bg-white/10"
              >
                Inquire About Group Enrollment
              </CTAButton>
            </div>
          </div>
        </section>
      </main>
    </PageShell>
  );
}
