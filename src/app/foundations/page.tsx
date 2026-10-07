import Image from "next/image";
import Link from "next/link";
import {
  CheckCircle2,
  Trophy,
  Compass,
  Users,
  Brain,
  Target,
  ArrowRight,
  ShieldCheck,
  Sparkles,
  Award,
  BookOpen,
  ClipboardList,
  FileText,
} from "lucide-react";

import { CTAButton } from "@/components/CTAButton";
import { PageShell } from "@/components/PageShell";
import { FoundationsSubNav } from "@/components/foundations/FoundationsSubNav";
import { FoundationsEnvironmentGallery } from "@/components/foundations/FoundationsEnvironmentGallery";
import { FoundationsPathwayCards } from "@/components/foundations/FoundationsPathwayCards";
import { FoundationsOrientationSteps } from "@/components/foundations/FoundationsOrientationSteps";
import { FoundationsAccessibilityDock } from "@/components/foundations/FoundationsAccessibilityDock";
import { FoundationsFloatingAction } from "@/components/foundations/FoundationsFloatingAction";
import {
  MotionFadeIn,
  MotionStaggerContainer,
  MotionStaggerItem,
  MotionScaleIn,
  ScrollProgressBar,
  MotionShimmerButton,
} from "@/components/motion";
import { createMetadata } from "@/content/site";

export const metadata = createMetadata(
  "Lornette’s Foundations | Athlete Development",
  "A whole-athlete development program from former national sprint champion and Olympian Lornette Daye, helping athletes build performance, resilience, confidence and preparation for sport and life.",
  "/foundations",
);

const credibilityStats = [
  { value: "Multi-Decade", label: "National Record Unsurpassed", detail: "Canadian sprint mark stood unbroken for decades", icon: Award },
  { value: "Double Gold", label: "Canada Summer Games Champion", detail: "100m & 200m national sprint sweep", icon: Trophy },
  { value: "40+", label: "Years Coaching at Olympic Level", detail: "Canadian champion & international coach", icon: ShieldCheck },
  { value: "150+", label: "International Podium Athletes", detail: "Mentored across championship arenas", icon: Target },
  { value: "500+", label: "Championship Competitors Coached", detail: "Juniors, collegiate & tournament leaders", icon: Users },
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
    name: "Lornette’s Foundations Athlete Development Program",
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
      <ScrollProgressBar />
      <main className="bg-[var(--ivory)] text-[var(--ink)]">
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(athleteServiceJsonLd) }}
        />

        {/* Secondary Navigation */}
        <FoundationsSubNav />

        {/* SECTION 1: HERO */}
        <section className="relative overflow-hidden border-b border-[rgba(198,165,92,0.35)] bg-[var(--ivory)] px-4 py-14 sm:px-6 lg:px-8 lg:py-20">
          <div className="pointer-events-none absolute inset-0 bg-[linear-gradient(115deg,rgba(255,255,255,0.92)_0%,rgba(250,247,240,0.84)_46%,rgba(232,221,203,0.58)_100%)]" />
          <div className="pointer-events-none absolute right-0 top-0 h-full w-1/2 bg-[linear-gradient(132deg,transparent_0%,rgba(198,165,92,0.1)_44%,transparent_78%)]" />

          <div className="relative mx-auto grid max-w-7xl gap-12 lg:grid-cols-12 lg:items-center">
            <div className="min-w-0 max-w-3xl lg:col-span-7">
              <MotionFadeIn delay={0.05}>
                <p className="inline-flex border border-[rgba(198,165,92,0.48)] bg-white/70 px-3.5 py-1.5 text-xs font-bold uppercase tracking-[0.24em] text-[var(--gold-dark)] shadow-sm">
                  THE COMPLETE ATHLETE DEVELOPMENT SYSTEM
                </p>
              </MotionFadeIn>
              <MotionFadeIn delay={0.15}>
                <h1 className="mt-6 font-serif text-[2.75rem] leading-[0.98] text-balance text-[var(--ink)] sm:text-6xl lg:text-[4.3rem] xl:text-[4.75rem]">
                  Lornette’s Foundations
                </h1>
                <p className="mt-5 font-serif text-2xl leading-snug text-[var(--gold-dark)] sm:text-3xl">
                  The 10 Foundations Built by Lornette
                </p>
              </MotionFadeIn>
              <MotionFadeIn delay={0.25}>
                <p className="mt-6 max-w-2xl text-base leading-8 text-[#554b40] sm:text-lg">
                  Most athletes train physical mechanics. Elite competitors train what governs them under pressure. Lornette’s Foundations builds composure, discipline, identity, leadership, and grounded execution through practical 10-week pathway experiences.
                </p>
              </MotionFadeIn>

              <MotionFadeIn delay={0.35}>
                <div className="mt-9 flex flex-col gap-3 sm:flex-row">
                  <MotionShimmerButton href="#start-here">Start Here</MotionShimmerButton>
                  <CTAButton href="#pathways" variant="secondary">
                    Choose Your Pathway
                  </CTAButton>
                </div>
              </MotionFadeIn>

              <MotionFadeIn delay={0.45}>
                <div className="mt-10 border-l-2 border-[var(--champagne)] pl-4">
                  <p className="font-serif text-xl italic text-[var(--ink)] sm:text-2xl">
                    &ldquo;Championship moments are never accidental. They are the harvest of long-term vision, systematic investment, and holistic support.&rdquo;
                  </p>
                  <p className="mt-2 text-xs font-bold uppercase tracking-[0.2em] text-[#7d7164]">
                    Lornette Daye · 40-Year Olympic Coach · Canadian National Sprint Champion
                  </p>
                </div>
              </MotionFadeIn>
            </div>

            <div className="relative lg:col-span-5">
              <MotionScaleIn delay={0.2}>
                <div className="relative w-full aspect-[4/5] overflow-hidden border border-[rgba(198,165,92,0.42)] bg-[linear-gradient(180deg,#fffdf8_0%,#f5efe4_100%)] shadow-[0_28px_110px_rgba(23,20,18,0.14)]">
                  <Image
                    src="/foundations/lornette-foundations-grand-staircase.png"
                    alt="Former national sprint champion Lornette Daye in tailored white suit standing before the gold LD monogram grand staircase"
                    fill
                    priority
                    unoptimized
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
              </MotionScaleIn>
            </div>
          </div>
        </section>

        {/* Credibility Statistics Strip */}
        <section
          aria-label="Foundations credibility statistics"
          className="border-b border-[var(--line)] bg-white px-4 py-10 sm:px-6 lg:px-8 overflow-hidden"
        >
          <div className="mx-auto max-w-7xl">
            <MotionStaggerContainer staggerDelay={0.1} className="grid gap-6 sm:grid-cols-2 lg:grid-cols-5 divide-y divide-[rgba(198,165,92,0.3)] sm:divide-y-0">
              {credibilityStats.map((item, idx) => {
                const StatIcon = item.icon;
                return (
                  <MotionStaggerItem
                    key={item.label}
                    className={`text-center border-l-0 lg:border-l lg:first:border-l-0 border-[rgba(198,165,92,0.3)] ${
                      idx > 0 ? "pt-6 sm:pt-0 lg:pl-6" : ""
                    }`}
                  >
                    <div className="mx-auto mb-2.5 flex h-8 w-8 items-center justify-center rounded-full border border-[rgba(198,165,92,0.35)] bg-[var(--sand)]/40 text-[var(--gold-dark)] shadow-xs">
                      <StatIcon size={16} aria-hidden="true" />
                    </div>
                    <p className="font-serif text-3xl font-bold tracking-tight text-[var(--gold-dark)] sm:text-4xl">
                      {item.value}
                    </p>
                    <p className="mt-2 text-xs font-bold uppercase tracking-[0.16em] text-[var(--ink)]">
                      {item.label}
                    </p>
                    <p className="mt-1 text-xs text-[#6e6355] leading-relaxed">
                      {item.detail}
                    </p>
                  </MotionStaggerItem>
                );
              })}
            </MotionStaggerContainer>
          </div>
        </section>

        {/* SECTION 2: START HERE */}
        <section id="start-here" className="px-4 py-16 sm:px-6 lg:px-8 lg:py-20 scroll-mt-24">
          <div className="mx-auto max-w-7xl">
            <MotionFadeIn className="text-center max-w-3xl mx-auto">
              <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--gold-dark)]">
                ORIENTATION
              </p>
              <h2 className="mt-3 font-serif text-3xl sm:text-4xl text-[var(--ink)]">
                Start Here
              </h2>
              <p className="mt-3 text-base text-[#675d50]">
                Find the right Foundation pathway in less than a minute.
              </p>
            </MotionFadeIn>

            <FoundationsOrientationSteps />
          </div>
        </section>

        {/* SECTION 2.5: HIGH-PERFORMANCE ENVIRONMENTS GALLERY */}
        <FoundationsEnvironmentGallery />

        {/* SECTION 3: SIGNATURE PATHWAYS */}
        <section id="pathways" className="border-y border-[var(--line)] bg-[var(--sand)]/40 px-4 py-16 sm:px-6 lg:px-8 lg:py-24 scroll-mt-24">
          <div className="mx-auto max-w-7xl">
            <div className="text-center max-w-3xl mx-auto">
              <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--gold-dark)]">
                SIGNATURE PATHWAYS
              </p>
              <h2 className="mt-3 font-serif text-3xl sm:text-4xl text-[var(--ink)]">
                Signature Pathways
              </h2>
              <p className="mt-3 text-base leading-8 text-[#675d50]">
                Choose the pathway that fits your athlete, team, organization, or partnership goal.
              </p>
            </div>

            <FoundationsPathwayCards />
          </div>
        </section>

        {/* SECTION 4: RESOURCES */}
        <section id="resources" className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24 scroll-mt-24">
          <div className="mx-auto max-w-7xl">
            <div className="text-center max-w-3xl mx-auto">
              <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--gold-dark)]">
                SUPPORTING MATERIALS
              </p>
              <h2 className="mt-3 font-serif text-3xl sm:text-4xl text-[var(--ink)]">
                Resources
              </h2>
              <p className="mt-3 text-base text-[#675d50]">
                Books, tools, and practical guidance to support the Foundation experience.
              </p>
            </div>

            <div className="mt-12 grid gap-6 sm:grid-cols-3">
              {/* Resource 1: Books */}
              <div className="border border-[rgba(198,165,92,0.34)] bg-white p-7 shadow-sm transition hover:-translate-y-1 hover:border-[var(--champagne)] flex flex-col justify-between">
                <div>
                  <div className="flex items-center justify-between">
                    <h3 className="font-serif text-2xl text-[var(--ink)]">Books</h3>
                    <div className="flex h-9 w-9 items-center justify-center rounded-full border border-[rgba(198,165,92,0.35)] bg-[var(--sand)]/35 text-[var(--gold-dark)] shadow-xs">
                      <BookOpen size={17} aria-hidden="true" />
                    </div>
                  </div>
                  <div className="mt-3 h-0.5 w-8 bg-[var(--champagne)]" aria-hidden="true" />
                  <p className="mt-4 text-sm leading-7 text-[#675d50]">
                    Lornette’s books, journals, guides, and published resources.
                  </p>
                </div>
                <div className="mt-6 pt-4 border-t border-[var(--line)]">
                  <CTAButton href="/books" variant="secondary" className="w-full text-xs">
                    View Books
                  </CTAButton>
                </div>
              </div>

              {/* Resource 2: Tools & Checklists */}
              <div className="border border-[rgba(198,165,92,0.34)] bg-white p-7 shadow-sm transition hover:-translate-y-1 hover:border-[var(--champagne)] flex flex-col justify-between">
                <div>
                  <div className="flex items-center justify-between">
                    <h3 className="font-serif text-2xl text-[var(--ink)]">Tools &amp; Checklists</h3>
                    <div className="flex h-9 w-9 items-center justify-center rounded-full border border-[rgba(198,165,92,0.35)] bg-[var(--sand)]/35 text-[var(--gold-dark)] shadow-xs">
                      <ClipboardList size={17} aria-hidden="true" />
                    </div>
                  </div>
                  <div className="mt-3 h-0.5 w-8 bg-[var(--champagne)]" aria-hidden="true" />
                  <p className="mt-4 text-sm leading-7 text-[#675d50]">
                    Worksheets, reflection tools, action plans, and practical exercises.
                  </p>
                </div>
                <div className="mt-6 pt-4 border-t border-[var(--line)]">
                  <CTAButton href="/foundations/quick-tools" variant="secondary" className="w-full text-xs">
                    View Tools
                  </CTAButton>
                </div>
              </div>

              {/* Resource 3: Articles */}
              <div className="border border-[rgba(198,165,92,0.34)] bg-white p-7 shadow-sm transition hover:-translate-y-1 hover:border-[var(--champagne)] flex flex-col justify-between">
                <div>
                  <div className="flex items-center justify-between">
                    <h3 className="font-serif text-2xl text-[var(--ink)]">Articles</h3>
                    <div className="flex h-9 w-9 items-center justify-center rounded-full border border-[rgba(198,165,92,0.35)] bg-[var(--sand)]/35 text-[var(--gold-dark)] shadow-xs">
                      <FileText size={17} aria-hidden="true" />
                    </div>
                  </div>
                  <div className="mt-3 h-0.5 w-8 bg-[var(--champagne)]" aria-hidden="true" />
                  <p className="mt-4 text-sm leading-7 text-[#675d50]">
                    Insights, stories, and teaching connected to performance, leadership, and growth.
                  </p>
                </div>
                <div className="mt-6 pt-4 border-t border-[var(--line)]">
                  <CTAButton href="/blog" variant="secondary" className="w-full text-xs">
                    Read Articles
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
              src="/foundations/banners/scenic-beach-track.jpg"
              alt="Scenic coastal running track along ocean shoreline at golden sunrise"
              role="presentation"
              fill
              unoptimized
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
              <MotionShimmerButton href="/foundations/golf">EXPLORE LORNETTE’S FOUNDATIONS</MotionShimmerButton>
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
      <FoundationsAccessibilityDock />
      <FoundationsFloatingAction track="foundations" />
    </PageShell>
  );
}
