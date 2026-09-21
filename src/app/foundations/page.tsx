import Image from "next/image";
import { CheckCircle2, Trophy } from "lucide-react";

import { CTAButton } from "@/components/CTAButton";
import { PageShell } from "@/components/PageShell";
import { FoundationsSubNav } from "@/components/foundations/FoundationsSubNav";
import { createMetadata } from "@/content/site";

export const metadata = createMetadata(
  "Lornette’s Foundation | Athlete Development",
  "A whole-athlete development program from former national champion and national coach Lornette Daye, helping athletes build performance, resilience, confidence and preparation for sport and life.",
  "/foundations",
);

const credibilityStats = [
  { value: "Multi-Decade", label: "National Record Unsurpassed", detail: "Canadian sprint mark stood unbroken for decades" },
  { value: "Double Gold", label: "Canada Summer Games Champion", detail: "100m & 200m national sprint sweep" },
  { value: "40+", label: "Years Coaching at Olympic Level", detail: "Canadian champion & international coach" },
  { value: "150+", label: "International Podium Athletes", detail: "Mentored across championship arenas" },
  { value: "500+", label: "Championship Competitors Coached", detail: "Juniors, collegiate & tournament leaders" },
];

const philosophyPillars = [
  {
    title: "Performance",
    description:
      "Build the mental discipline and repeatable routines that hold under tournament pressure, ensuring your trained swing executes with absolute clarity.",
  },
  {
    title: "Resilience",
    description:
      "Execute Lornette’s signature principle: 'Your previous shot cannot hit your next shot.' Release frustration, reset somatic focus, and recommit within five seconds.",
  },
  {
    title: "Confidence",
    description:
      "Replace hopeful wishing with earned certainty. Build confidence on a ledger of tangible evidence: completed cadences, disciplined shot decisions, and handled pressure.",
  },
  {
    title: "Identity",
    description:
      "Detach self-worth from the scoreboard. Compete with poise, clarity, and authority, unlocking your highest potential when your identity is unshakeable.",
  },
  {
    title: "Preparation",
    description:
      "Structure deliberate pre-competition systems that align mental composure with physical readiness hours before competition begins.",
  },
  {
    title: "Decision-Making",
    description:
      "Instill calm calculation, course management, and committed choices in high-stakes competitive moments.",
  },
  {
    title: "Leadership",
    description:
      "Empowering competitors to elevate team culture, model accountability, and communicate with clarity and composure.",
  },
  {
    title: "Life Beyond Sport",
    description:
      "Equipping athletes with character, emotional intelligence, and purpose that translate seamlessly into career and life.",
  },
];

const performanceEdgeTools = [
  "Focus",
  "Routine",
  "Pressure",
  "Visualization",
  "Reset",
  "Decision-Making",
  "Competition Preparation",
  "Confidence",
];

const organizationTypes = [
  "Golf Clubs & Country Clubs",
  "High-Performance Sport Academies",
  "Collegiate & Athletic Programs",
  "Sports Federations & Teams",
  "Junior Development Programs",
  "Schools & Athletic Departments",
];

export default function FoundationsPage() {
  const athleteServiceJsonLd = {
    "@context": "https://schema.org",
    "@type": "Service",
    name: "Lornette’s Foundation Athlete Development Program",
    provider: {
      "@type": "Person",
      name: "Lornette Daye",
      jobTitle: "Former National Sprint Champion & National Coach",
    },
    areaServed: "Global",
    description:
      "A whole-athlete development experience built from more than four decades of elite sport, coaching, and mentorship.",
  };

  return (
    <PageShell>
      <main className="bg-[var(--ivory)] text-[var(--ink)]">
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(athleteServiceJsonLd) }}
        />

        {/* Secondary Navigation */}
        <FoundationsSubNav />

        {/* Hero Section */}
        <section className="relative overflow-hidden border-b border-[rgba(198,165,92,0.35)] bg-[var(--ivory)] px-4 py-14 sm:px-6 lg:px-8 lg:py-20">
          <div className="pointer-events-none absolute inset-0 bg-[linear-gradient(115deg,rgba(255,255,255,0.92)_0%,rgba(250,247,240,0.84)_46%,rgba(232,221,203,0.58)_100%)]" />
          <div className="pointer-events-none absolute right-0 top-0 h-full w-1/2 bg-[linear-gradient(132deg,transparent_0%,rgba(198,165,92,0.1)_44%,transparent_78%)]" />
          <div className="pointer-events-none absolute left-0 top-10 h-px w-2/3 bg-gradient-to-r from-transparent via-[rgba(198,165,92,0.28)] to-transparent" />

          <div className="relative mx-auto grid max-w-7xl gap-12 lg:grid-cols-12 lg:items-center">
            <div className="min-w-0 max-w-3xl lg:col-span-7">
              <p className="inline-flex border border-[rgba(198,165,92,0.48)] bg-white/70 px-3.5 py-1.5 text-xs font-bold uppercase tracking-[0.24em] text-[var(--gold-dark)] shadow-sm">
                The Complete Athlete Development System
              </p>
              <h1 className="mt-6 font-serif text-[2.75rem] leading-[0.98] text-balance text-[var(--ink)] sm:text-6xl lg:text-[4.3rem] xl:text-[4.75rem]">
                Lornette’s Foundation
              </h1>
              <p className="mt-5 font-serif text-2xl leading-snug text-[var(--gold-dark)] sm:text-3xl">
                The 10 Athletic Foundations
              </p>
              <p className="mt-6 max-w-2xl text-base leading-8 text-[#554b40] sm:text-lg">
                Most athletes train physical mechanics. Elite champions train what governs them under pressure. Lornette’s Foundation installs the 10 Athletic Foundations, giving competitors the composure, discipline, and grounded identity to execute on demand.
              </p>

              <div className="mt-9 flex flex-col gap-3 sm:flex-row">
                <CTAButton href="/foundations/golf">EXPLORE THE ATHLETE PROGRAM</CTAButton>
                <CTAButton href="/foundations/clubs" variant="secondary">
                  FOR CLUBS & TEAMS
                </CTAButton>
              </div>

              <div className="mt-10 border-l-2 border-[var(--champagne)] pl-4">
                <p className="font-serif text-xl italic text-[var(--ink)] sm:text-2xl">
                  &ldquo;Championship moments are never accidental. They are the harvest of long-term vision, systematic investment, and holistic support.&rdquo;
                </p>
                <p className="mt-2 text-xs font-bold uppercase tracking-[0.2em] text-[#7d7164]">
                  Coach Lornette Daye, 40-Year Olympic Coach · National Sprint Champion · National Record Holder
                </p>
              </div>
            </div>

            <div className="relative lg:col-span-5">
              <div className="relative w-full aspect-[4/5] overflow-hidden border border-[rgba(198,165,92,0.42)] bg-[linear-gradient(180deg,#fffdf8_0%,#f5efe4_100%)] shadow-[0_28px_110px_rgba(23,20,18,0.14)]">
                <Image
                  src="/foundations/lornette-foundations-grand-staircase.png"
                  alt="Former national sprint champion Lornette Daye in tailored white suit standing before the gold LD monogram grand staircase"
                  fill
                  priority
                  sizes="(max-width: 768px) 92vw, 44vw"
                  className="object-cover"
                  style={{ objectPosition: "68% 16%" }}
                />
                <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/30" />
                <div className="absolute inset-x-0 bottom-0 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(18,15,13,0.82)] p-4 sm:p-5 backdrop-blur-md shadow-2xl">
                  <p className="text-[11px] font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
                    Elite Mentorship &amp; Culture
                  </p>
                  <p className="mt-1 font-serif text-base text-white sm:text-lg leading-snug">
                    The Complete Athlete Development Blueprint
                  </p>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Credibility Strip */}
        <section
          aria-label="Foundations credibility statistics"
          className="border-b border-[var(--line)] bg-white px-4 py-12 sm:px-6 lg:px-8"
        >
          <div className="mx-auto max-w-7xl">
            <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-5 divide-y divide-[rgba(198,165,92,0.3)] sm:divide-y-0">
              {credibilityStats.map((item, idx) => (
                <div
                  key={item.label}
                  className={`text-center border-l-0 lg:border-l lg:first:border-l-0 border-[rgba(198,165,92,0.3)] ${
                    idx > 0 ? "pt-6 sm:pt-0 lg:pl-6" : ""
                  }`}
                >
                  <p className="font-serif text-4xl font-bold tracking-tight text-[var(--gold-dark)] sm:text-5xl">
                    {item.value}
                  </p>
                  <p className="mt-2 text-xs font-bold uppercase tracking-[0.16em] text-[var(--ink)]">
                    {item.label}
                  </p>
                  <p className="mt-1 text-xs text-[#6e6355] leading-relaxed">
                    {item.detail}
                  </p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Foundation Philosophy */}
        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <div className="grid gap-10 lg:grid-cols-[0.45fr_0.55fr] lg:items-end">
              <div>
                <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--gold-dark)]">
                  The Philosophy That Changes Scorecards
                </p>
                <h2 className="mt-4 font-serif text-4xl leading-tight text-balance text-[var(--ink)] sm:text-5xl">
                  Develop the Athlete. Prepare the Person.
                </h2>
              </div>
              <p className="text-base leading-8 text-[#675d50] sm:text-lg">
                Technical instruction makes you capable. Mental composure makes you dangerous. A champion&apos;s durability is decided the moment physical skill and competitive nerves collide. Only one wins.
              </p>
            </div>

            <div className="mt-14 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
              {philosophyPillars.map((pillar) => (
                <article
                  key={pillar.title}
                  className="border border-[rgba(198,165,92,0.34)] bg-white p-7 shadow-[0_16px_50px_rgba(23,20,18,0.05)] transition duration-200 hover:-translate-y-1 hover:border-[var(--champagne)]"
                >
                  <h3 className="font-serif text-2xl text-[var(--ink)]">
                    {pillar.title}
                  </h3>
                  <div className="mt-3 h-0.5 w-8 bg-[var(--champagne)]" aria-hidden="true" />
                  <p className="mt-4 text-sm leading-7 text-[#675d50]">
                    {pillar.description}
                  </p>
                </article>
              ))}
            </div>

            {/* Editorial Showcase: The Championship Pathway */}
            <div className="mt-14 overflow-hidden border border-[rgba(198,165,92,0.36)] bg-white shadow-[0_16px_50px_rgba(23,20,18,0.06)] grid grid-cols-1 lg:grid-cols-12">
              <div className="relative w-full aspect-[16/9] lg:aspect-auto lg:col-span-6 lg:min-h-[320px]">
                <Image
                  src="/foundations/lornette-foundations-stadium-tunnel.png"
                  alt="Lornette Daye walking forward in tailored suit through an illuminated stadium tunnel toward the championship lights"
                  fill
                  sizes="(max-width: 1024px) 100vw, 50vw"
                  className="object-cover"
                  style={{ objectPosition: "27% 16%" }}
                />
                <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/20" />
              </div>
              <div className="min-w-0 p-6 sm:p-8 lg:p-12 lg:col-span-6 flex flex-col justify-center bg-[linear-gradient(135deg,#fffdf8_0%,#faf6ee_100%)]">
                <span className="text-xs font-bold uppercase tracking-[0.22em] text-[var(--gold-dark)]">
                  Where Championships Are Won
                </span>
                <h3 className="mt-2 font-serif text-2xl sm:text-3xl text-[var(--ink)]">
                  Stepping Into the Arena With Conviction
                </h3>
                <p className="mt-4 text-base leading-relaxed text-[#5e5346]">
                  Every athlete encounters the moment where physical conditioning and technical skill reach parity with the competition. In that decisive threshold, performance is governed entirely by composure, identity, and the quiet internal certainty built during preparation.
                </p>
                <div className="mt-6">
                  <CTAButton
                    href="/foundations/performance-edge"
                    variant="secondary"
                    className="text-xs sm:text-sm"
                  >
                    EXPLORE THE PERFORMANCE EDGE FRAMEWORK
                  </CTAButton>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Foundation Pathways */}
        <section className="border-y border-[var(--line)] bg-[var(--sand)]/40 px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <div className="text-center max-w-3xl mx-auto">
              <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--gold-dark)]">
                Choose Your Performance Pathway
              </p>
              <h2 className="mt-4 font-serif text-4xl leading-tight text-[var(--ink)] sm:text-5xl">
                FOUNDATION PATHWAYS
              </h2>
              <p className="mt-4 text-base leading-8 text-[#675d50]">
                The same mental conditioning system, applied to the specific demands, pressure moments, and decision patterns of your sport.
              </p>
            </div>

            <div className="mt-12 max-w-4xl mx-auto">
              <div className="overflow-hidden border border-[rgba(198,165,92,0.45)] bg-white shadow-[0_24px_80px_rgba(23,20,18,0.08)]">
                <div className="grid lg:grid-cols-[1.1fr_0.9fr]">
                  <div className="p-8 sm:p-10 flex flex-col justify-between">
                    <div>
                      <div className="flex items-center gap-2 text-xs font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)]">
                        <Trophy size={16} aria-hidden="true" />
                        Flagship Pathway
                      </div>
                      <h3 className="mt-3 font-serif text-3xl sm:text-4xl text-[var(--ink)]">
                        Golf Performance Program
                      </h3>
                      <p className="mt-2 text-xs font-bold uppercase tracking-[0.16em] text-[#7d7164]">
                        Powered by the Performance Edge Framework
                      </p>
                      <p className="mt-5 text-sm leading-7 text-[#675d50]">
                        Built for tournament golfers seeking consistent execution when the championship is on the line. Master the 10 Athletic Foundations and practical Performance Edge tools that turn preparation into podium results.
                      </p>
                    </div>

                    <div className="mt-8 pt-6 border-t border-[var(--line)] flex items-center justify-between">
                      <CTAButton href="/foundations/golf">EXPLORE GOLF PATHWAY</CTAButton>
                      <span className="text-xs font-bold uppercase tracking-[0.18em] text-[var(--gold-dark)] hidden sm:inline-block">
                        Active Pathway &rarr;
                      </span>
                    </div>
                  </div>

                  <div className="relative min-h-[300px] overflow-hidden bg-[#112316] p-8 text-[var(--ivory)] flex flex-col justify-between">
                    <Image
                      src="/foundations/golf/lornette-golf-fairway-mountain-sunset.png"
                      alt="Championship golf fairway overlooking mountains at golden sunset"
                      fill
                      sizes="(max-width: 1024px) 100vw, 45vw"
                      className="object-cover object-center scale-105 filter blur-[2.5px] opacity-45"
                    />
                    <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-[#0b180f]/95 via-[#112316]/82 to-[#14291a]/68" />
                    <div className="relative z-10">
                      <span className="inline-flex rounded-[4px] bg-gradient-to-r from-[#dfc385] to-[#c7a45e] px-2.5 py-1 text-xs font-bold uppercase tracking-[0.22em] text-[#0f2014] shadow-xs">
                        Performance Tools
                      </span>
                      <p className="mt-4 font-serif text-2xl sm:text-[26px] text-white font-medium leading-snug">
                        Playing Your Best When It Matters.
                      </p>
                      <ul className="mt-4 grid grid-cols-2 gap-2.5 text-xs text-[#e2ecdc]">
                        {performanceEdgeTools.map((tool) => (
                          <li key={tool} className="flex items-center gap-2">
                            <span className="h-1.5 w-1.5 rounded-full bg-[#dfcca6] shrink-0" />
                            <span className="font-medium tracking-wide">{tool}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                    <p className="relative z-10 text-xs italic text-[#c8d9c2] pt-4">
                      Complements technical swing instruction without interfering with swing coaches.
                    </p>
                  </div>
                </div>
              </div>

              <div className="mt-8 border border-dashed border-[rgba(198,165,92,0.4)] bg-white/50 p-6 text-center">
                <p className="text-sm font-medium text-[#675d50]">
                  <strong className="text-[var(--ink)]">Future Pathways:</strong> More sport pathways will be introduced intentionally over time as sport-specific curricula are codified with coaches and federations.
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* Performance Edge Framework Section */}
        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <div className="grid gap-12 lg:grid-cols-[0.9fr_1.1fr] lg:items-center">
              <div>
                <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--gold-dark)]">
                  The Mental Performance System
                </p>
                <h2 className="mt-4 font-serif text-4xl leading-tight text-[var(--ink)] sm:text-5xl">
                  THE PERFORMANCE EDGE FRAMEWORK
                </h2>
                <div className="mt-4 h-0.5 w-12 bg-[var(--champagne)]" aria-hidden="true" />
                <p className="mt-6 text-lg leading-8 text-[#554b40]">
                  Performance Edge is the practical performance methodology inside Lornette&apos;s Foundation. It gives athletes the structured, repeatable tools to stop letting pressure hijack their performance and execute their training on demand.
                </p>
                <p className="mt-4 text-base leading-8 text-[#675d50]">
                  Developed from more than four decades of international competition and national coaching, the framework equips athletes to neutralize internal tension, recover from errors in seconds, and step into every competitive moment with calm, unshakeable conviction.
                </p>
                <div className="mt-8">
                  <CTAButton href="/foundations/performance-edge" variant="secondary">
                    LEARN THE PERFORMANCE EDGE FRAMEWORK
                  </CTAButton>
                </div>
              </div>

              <div className="border border-[rgba(198,165,92,0.38)] bg-white p-8 shadow-[0_20px_70px_rgba(23,20,18,0.06)]">
                <p className="text-xs font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)]">
                  Repeatable Tools for Competitors
                </p>
                <h3 className="mt-2 font-serif text-2xl text-[var(--ink)]">
                  Eight Practical Performance Tools
                </h3>
                <div className="mt-6 grid gap-3 sm:grid-cols-2">
                  {performanceEdgeTools.map((tool, idx) => (
                    <div
                      key={tool}
                      className="flex items-center gap-3 border border-[var(--line)] bg-[var(--ivory)] px-4 py-3"
                    >
                      <span className="font-serif text-sm font-bold text-[var(--gold-dark)]">
                        0{idx + 1}
                      </span>
                      <span className="text-sm font-semibold text-[var(--charcoal)]">
                        {tool}
                      </span>
                    </div>
                  ))}
                </div>
                <div className="mt-6 border-t border-[var(--line)] pt-4 text-xs text-[#7d7164]">
                  8 tools. Trained weekly. Applied on the course, track, or field immediately.
                </div>
              </div>
            </div>

            {/* Editorial Showcase: Olympic Heritage & Modern Practice */}
            <div className="mt-14 overflow-hidden border border-[rgba(198,165,92,0.36)] bg-white shadow-[0_16px_50px_rgba(23,20,18,0.06)] grid grid-cols-1 lg:grid-cols-12">
              <div className="relative w-full aspect-[16/9] lg:aspect-auto lg:col-span-6 lg:min-h-[320px]">
                <Image
                  src="/foundations/lornette-foundations-outdoor-track-sunrise.png"
                  alt="Lornette Daye in white tailored suit standing on an Olympic running track at sunrise, symbolizing four decades of elite sport excellence"
                  fill
                  sizes="(max-width: 1024px) 100vw, 50vw"
                  className="object-cover"
                  style={{ objectPosition: "28% 18%" }}
                />
                <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/20" />
              </div>
              <div className="min-w-0 p-6 sm:p-8 lg:p-12 lg:col-span-6 flex flex-col justify-center bg-[linear-gradient(135deg,#fffdf8_0%,#faf6ee_100%)]">
                <span className="text-xs font-bold uppercase tracking-[0.22em] text-[var(--gold-dark)]">
                  Forged in Championship Competition
                </span>
                <h3 className="mt-2 font-serif text-2xl sm:text-3xl text-[var(--ink)]">
                  Composure Forged on the World Stage
                </h3>
                <p className="mt-4 text-base leading-relaxed text-[#5e5346]">
                  Before coaching international contenders, Lornette Daye was a Canadian sprint sensation whose national 100m sprint record stood unbroken for decades. At the 1985 Canada Summer Games, she swept the national sprint titles, capturing Double Gold in both the 100m and 200m championships. She has stood in the blocks, felt the solitary heartbeat before the starter&apos;s gun, and knows exactly what is required to execute with poise when a national championship is on the line.
                </p>
                <div className="mt-6 flex flex-wrap gap-3">
                  <CTAButton href="/foundations/performance-edge">
                    TRAIN LIKE A CHAMPION
                  </CTAButton>
                  <CTAButton href="/foundations/golf" variant="secondary">
                    EXPLORE GOLF PATHWAY
                  </CTAButton>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Clubs & Organizations B2B Section */}
        <section className="border-t border-[var(--line)] bg-[var(--ink)] px-4 py-16 text-[var(--ivory)] sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <div className="grid gap-12 lg:grid-cols-[1fr_1.05fr] lg:items-center">
              <div>
                <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--champagne)]">
                  Institutional &amp; Team Development
                </p>
                <h2 className="mt-4 font-serif text-4xl leading-tight text-white sm:text-5xl">
                  Equip Your Entire Roster for Championship Moments
                </h2>
                <p className="mt-6 text-lg leading-8 text-[#d8cdbb]">
                  Physical training gets athletes into the arena. Mental composure determines who executes when everything is on the line. Lornette’s Foundation brings four decades of Olympic-level wisdom into a practical, repeatable mental framework that elevates coaches, teams, and whole athletic departments.
                </p>

                <div className="mt-8 grid gap-4 sm:grid-cols-3">
                  <div className="border border-white/15 bg-white/[0.03] p-4">
                    <p className="font-serif text-base font-medium text-white">Composure Under Fire</p>
                    <p className="mt-1 text-xs leading-relaxed text-[#b8ab9a]">Somatic regulation to master nervous tension in crunch moments.</p>
                  </div>
                  <div className="border border-white/15 bg-white/[0.03] p-4">
                    <p className="font-serif text-base font-medium text-white">5-Second Reset</p>
                    <p className="mt-1 text-xs leading-relaxed text-[#b8ab9a]">Disciplined post-error recovery so one mistake never compounds.</p>
                  </div>
                  <div className="border border-white/15 bg-white/[0.03] p-4">
                    <p className="font-serif text-base font-medium text-white">Unified Language</p>
                    <p className="mt-1 text-xs leading-relaxed text-[#b8ab9a]">Aligns coaching staff and players under a shared mental code.</p>
                  </div>
                </div>

                <div className="mt-8">
                  <CTAButton href="/foundations/clubs">
                    EXPLORE ORGANIZATIONAL PROGRAMS
                  </CTAButton>
                </div>
              </div>

              <div className="border border-white/15 bg-white/[0.045] p-8 shadow-[0_24px_80px_rgba(0,0,0,0.25)]">
                <div className="flex items-center justify-between border-b border-white/10 pb-4">
                  <div>
                    <p className="text-xs font-bold uppercase tracking-[0.2em] text-[var(--champagne)]">
                      High-Performance Environments
                    </p>
                    <p className="mt-1 font-serif text-xl text-white">
                      Customized For Your Organization
                    </p>
                  </div>
                </div>

                <div className="mt-6 grid gap-3 sm:grid-cols-2">
                  {organizationTypes.map((org) => (
                    <div
                      key={org}
                      className="flex items-center gap-3 border border-white/10 bg-white/[0.03] px-4 py-3.5 text-sm font-medium text-[#e4dbcd]"
                    >
                      <CheckCircle2 size={16} aria-hidden="true" className="shrink-0 text-[var(--champagne)]" />
                      {org}
                    </div>
                  ))}
                </div>
                <p className="mt-6 text-xs leading-relaxed text-[#b8ab9a]">
                  Each format, from high-energy banquet keynotes to interactive member clinics and multi-week guided cohorts, is tailored directly to your season schedule, athlete age brackets, and coaching goals.
                </p>
              </div>
            </div>

            {/* Editorial Academy Feature */}
            <div className="mt-14 overflow-hidden border border-white/15 bg-white/[0.035] grid grid-cols-1 lg:grid-cols-12">
              <div className="min-w-0 p-6 sm:p-8 lg:p-12 lg:col-span-6 flex flex-col justify-center order-2 lg:order-1">
                <span className="text-xs font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
                  Coaching Culture &amp; Leadership
                </span>
                <h3 className="mt-2 font-serif text-2xl sm:text-3xl text-white">
                  One Shared Standard From Practice to Podium
                </h3>
                <p className="mt-4 text-base leading-relaxed text-[#d8cdbb]">
                  When organizations integrate Lornette&apos;s Foundation, coaches, parents, and athletes speak the same mental performance language. Practice execution translates seamlessly into tournament composure, setbacks become catalysts for growth, and athletes develop unshakeable character for sport and life.
                </p>
                <div className="mt-6 flex flex-wrap gap-3">
                  <CTAButton href="/foundations/clubs">
                    VIEW CLUB &amp; TEAM FORMATS
                  </CTAButton>
                  <CTAButton
                    href="/speaker-kit"
                    variant="secondary"
                    className="border-white/30 text-white hover:bg-white/10 text-xs sm:text-sm"
                  >
                    VIEW SPEAKER &amp; PROGRAM KIT
                  </CTAButton>
                </div>
              </div>
              <div className="relative w-full aspect-[16/9] lg:aspect-auto lg:col-span-6 lg:min-h-[320px] order-1 lg:order-2">
                <Image
                  src="/foundations/lornette-foundations-academy-hallway.png"
                  alt="Lornette Daye in white tailored suit standing in a sunlit training facility corridor with student athletes"
                  fill
                  sizes="(max-width: 1024px) 100vw, 50vw"
                  className="object-cover"
                  style={{ objectPosition: "68% 18%" }}
                />
                <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/15" />
              </div>
            </div>
          </div>
        </section>

        {/* Panoramic Closing Bottom Banner */}
        <section className="relative overflow-hidden border-t border-[rgba(198,165,92,0.4)] min-h-[340px] sm:min-h-[400px] flex items-center px-4 py-16 text-center text-[var(--ivory)] sm:px-6 lg:px-8 lg:py-24">
          <div className="absolute inset-0 pointer-events-none overflow-hidden">
            <Image
              src="/foundations/banners/scenic-beach-track.jpg"
              alt="Scenic coastal running track along ocean shoreline at golden sunrise"
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
              The Next Step Forward
            </p>
            <h2 className="mt-4 font-serif text-4xl leading-tight text-white sm:text-5xl lg:text-6xl">
              Build a Stronger Athlete. Build a Stronger Future.
            </h2>
            <p className="mt-6 max-w-2xl mx-auto text-lg leading-8 text-[#d8cdbb]">
              Your athletes are physically ready. Give them the mental game that matches their talent, and discover what they&apos;re truly capable of achieving.
            </p>
            <div className="mt-9 flex flex-col justify-center gap-4 sm:flex-row">
              <CTAButton href="/foundations/golf">EXPLORE LORNETTE’S FOUNDATION</CTAButton>
              <CTAButton
                href="/book"
                variant="secondary"
                className="border-white/30 text-white hover:bg-white/10"
              >
                WORK WITH LORNETTE
              </CTAButton>
            </div>
          </div>
        </section>
      </main>
    </PageShell>
  );
}
