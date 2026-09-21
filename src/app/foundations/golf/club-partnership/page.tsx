import Image from "next/image";
import Link from "next/link";
import {
  ArrowRight,
  BarChart3,
  Calendar,
  CheckCircle2,
  Mic,
  PieChart,
  Users,
} from "lucide-react";
import { CTAButton } from "@/components/CTAButton";
import { FoundationsSubNav } from "@/components/foundations/FoundationsSubNav";
import { PageShell } from "@/components/PageShell";
import { createMetadata } from "@/content/site";

export const metadata = createMetadata(
  "Golf Club Partnership | Lornette’s Foundation",
  "Institutional mental performance partnerships for private golf clubs, country clubs, and junior academies led by Olympic-level coach Lornette Daye.",
  "/foundations/golf/club-partnership",
);

const clubSolutions = [
  {
    icon: Mic,
    title: "Member Keynote",
    description:
      "An inspiring, high-impact talk that energizes your members and sets the tone for a stronger, more resilient game and life.",
    image: "/foundations/golf/lornette-golf-keynote-speaking-podium.png",
    imageAlt: "Coach Lornette Daye delivering a championship keynote to golf club members",
    href: "/foundations/golf/keynote",
    ctaText: "Learn More",
  },
  {
    icon: Users,
    title: "Workshop",
    description:
      "Interactive sessions that give members practical tools to manage pressure, build confidence, and perform with greater focus.",
    image: "/foundations/golf/curriculum/week-01-dew-flag.jpg",
    imageAlt: "Championship golf ball on putting green during hands-on member clinic",
    href: "/foundations/golf/workshop",
    ctaText: "Learn More",
  },
  {
    icon: BarChart3,
    title: "Cohort Programs",
    description:
      "A 10-week guided experience for members who want to go deeper with mindset training, habit-building, and on-course application.",
    image: "/foundations/golf/curriculum/week-03-address-stance.jpg",
    imageAlt: "Golfer dialed into routine and address stance during 10-week cohort",
    href: "/foundations/golf/program",
    ctaText: "Learn More",
  },
  {
    icon: PieChart,
    title: "Aggregate Reporting",
    description:
      "Optional anonymous insights to track growth and engagement across your membership while respecting individual privacy.",
    image: "/foundations/golf/curriculum/week-06-tour-bag.jpg",
    imageAlt: "Executive reporting and tour performance standards for club leadership",
    href: "/foundations/club",
    ctaText: "Learn More",
  },
  {
    icon: Calendar,
    title: "Annual Programming",
    description:
      "A strategic, year-round partnership with seasonal touchpoints, events, and custom experiences designed around your club’s goals.",
    image: "/foundations/golf/curriculum/week-09-terrace-vista.jpg",
    imageAlt: "Clubhouse terrace overlooking championship golf course representing annual alliance",
    href: "/book",
    ctaText: "Learn More",
  },
];

const partnershipSteps = [
  {
    step: "1",
    name: "Discover",
    description: "We learn about your club’s culture, goals, and member needs.",
  },
  {
    step: "2",
    name: "Design",
    description: "We customize a program mix that aligns with your vision and calendar.",
  },
  {
    step: "3",
    name: "Deliver",
    description: "We bring the experience to your members, in person or virtually.",
  },
  {
    step: "4",
    name: "Measure & Grow",
    description: "We share insights, gather feedback, and plan what’s next together.",
  },
];

const growthAreas = [
  { label: "Confidence", percentage: 85 },
  { label: "Focus & Preparation", percentage: 78 },
  { label: "Emotional Regulation", percentage: 72 },
  { label: "Setback Resilience", percentage: 69 },
  { label: "Course Enjoyment", percentage: 61 },
];

const clubAdvantages = [
  "More engaged, resilient, and confident members",
  "A stronger, more connected club community",
  "Programs tailored to your club’s culture and calendar",
  "Measurable impact, anonymous reporting, and ongoing support",
  "A premier institutional experience led by Lornette Daye",
];

const partnershipTiers = [
  {
    tier: "Full Season Alliance",
    subtitle: "Complete Club Mental Conditioning",
    description: "Year-long integration with 2 keynotes, 4 member clinics, junior camp integration, and coach advisory sessions.",
    highlight: "Most Popular for Private Clubs",
  },
  {
    tier: "Tournament Series Package",
    subtitle: "Pre-Championship Intensive",
    description: "Targeted support built around your club's championship calendar: Member-Guest, Club Championship, and Interclub qualifiers.",
    highlight: "Seasonal Focus",
  },
  {
    tier: "Junior Academy Pathway",
    subtitle: "Next-Generation Champion Development",
    description: "Specialized mental performance curriculum tailored specifically for competitive youth and junior development programs.",
    highlight: "Academy & Development",
  },
];

export default function GolfClubPartnershipPage() {
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
                    The Performance Edge
                  </span>
                  <span className="text-xs font-bold uppercase tracking-[0.2em] text-[#7d7164]">
                    Institutional Partnership
                  </span>
                </div>

                <h1 className="mt-6 font-serif text-4xl leading-[1.04] text-balance text-[var(--ink)] sm:text-6xl">
                  Club Partnership
                </h1>

                <p className="mt-3 font-serif text-2xl text-[#3d3429] sm:text-3xl">
                  Stronger Members. A Stronger Club.
                </p>

                <p className="mt-5 text-base leading-8 text-[#554b40] sm:text-lg">
                  Partner with Lornette Daye to bring Lornette’s Foundation Golf experience to your club. We help private clubs and golf organizations elevate the mental game, build resilient members, and create a more engaged, connected, and high-performing community, both on and off the course.
                </p>

                {/* Lornette Signature Quote Callout */}
                <div className="mt-8 border-l-2 border-[var(--gold-dark)] bg-white/80 p-5 shadow-sm">
                  <p className="font-serif text-base italic text-[#2c2620] leading-relaxed">
                    “Better people make a better game. Better clubs build a brighter tomorrow.”
                  </p>
                  <p className="mt-2 text-xs font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)]">
                    Coach Lornette Daye
                  </p>
                </div>

                <div className="mt-8 flex flex-col gap-3 sm:flex-row">
                  <CTAButton href="/book">Inquire About a Club Partnership</CTAButton>
                  <CTAButton href="/speaker-kit" variant="secondary">
                    Download Overview
                  </CTAButton>
                </div>
              </div>

              <div className="relative lg:col-span-5">
                <div className="relative w-full aspect-[4/5] overflow-hidden border border-[rgba(198,165,92,0.42)] bg-[linear-gradient(180deg,#fffdf8_0%,#f5efe4_100%)] shadow-[0_28px_110px_rgba(23,20,18,0.14)]">
                  <Image
                    src="/foundations/golf/lornette-golf-coastal-links.png"
                    alt="Lornette Daye on the coastal golf links overlooking ocean fairway"
                    fill
                    priority
                    sizes="(max-width: 1024px) 92vw, 40vw"
                    className="object-cover"
                    style={{ objectPosition: "88% 20%" }}
                  />
                  <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/40" />
                  <div className="absolute inset-x-0 bottom-0 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(18,15,13,0.82)] p-4 sm:p-5 backdrop-blur-md shadow-2xl">
                    <p className="text-[11px] font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
                      People · Performance · Community
                    </p>
                    <p className="mt-1 font-serif text-base text-white sm:text-lg">
                      A Stronger Club Culture On and Off the Course
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Solutions For Clubs: 5 Visual Solution Cards */}
        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <div className="flex flex-col md:flex-row md:items-end justify-between gap-6">
              <div className="max-w-2xl">
                <span className="text-xs font-bold uppercase tracking-[0.24em] text-[var(--gold-dark)]">
                  Solutions For Clubs
                </span>
                <h2 className="mt-3 font-serif text-3xl sm:text-4xl text-[var(--ink)]">
                  A Complete Club Partnership Experience
                </h2>
              </div>
              <p className="max-w-xl text-sm leading-relaxed text-[#675d50]">
                Flexible, customized programming designed for your members, leadership team, and community. Each offering can stand alone or be combined into a year-round partnership.
              </p>
            </div>

            <div className="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-5">
              {clubSolutions.map((sol) => {
                const Icon = sol.icon;
                return (
                  <div
                    key={sol.title}
                    className="group flex flex-col justify-between overflow-hidden border border-[rgba(198,165,92,0.34)] bg-white shadow-sm transition-all duration-300 hover:border-[rgba(198,165,92,0.65)] hover:shadow-md"
                  >
                    <div>
                      {/* Image Thumbnail */}
                      <div className="relative aspect-[16/10] w-full overflow-hidden border-b border-[rgba(198,165,92,0.28)] bg-[#120f0d]">
                        <Image
                          src={sol.image}
                          alt={sol.imageAlt}
                          fill
                          sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 20vw"
                          className="object-cover transition-transform duration-500 group-hover:scale-105"
                          quality={90}
                        />
                        <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-black/45 via-transparent to-transparent" />
                      </div>

                      <div className="p-5">
                        <div className="flex items-center gap-2 text-[var(--gold-dark)]">
                          <Icon size={18} />
                          <span className="text-[11px] font-bold uppercase tracking-[0.16em]">
                            {sol.title}
                          </span>
                        </div>
                        <p className="mt-3 text-xs leading-relaxed text-[#675d50]">
                          {sol.description}
                        </p>
                      </div>
                    </div>

                    <div className="p-5 pt-0">
                      <Link
                        href={sol.href}
                        className="inline-flex items-center gap-1.5 text-xs font-bold uppercase tracking-[0.16em] text-[var(--gold-dark)] hover:text-[var(--ink)] transition-colors"
                      >
                        <span>{sol.ctaText}</span>
                        <ArrowRight size={13} />
                      </Link>
                    </div>
                  </div>
                );
              })}
            </div>

            {/* How A Club Partnership Works: 4 Step Path */}
            <div className="mt-20 border-t border-[var(--line)] pt-16">
              <div className="text-center max-w-3xl mx-auto">
                <span className="text-xs font-bold uppercase tracking-[0.24em] text-[var(--gold-dark)]">
                  How A Club Partnership Works
                </span>
                <h3 className="mt-3 font-serif text-3xl sm:text-4xl text-[var(--ink)]">
                  A Simple Path to Lasting Impact
                </h3>
              </div>

              <div className="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
                {partnershipSteps.map((step) => (
                  <div
                    key={step.step}
                    className="relative border border-[rgba(198,165,92,0.32)] bg-[#fffdfa] p-6 shadow-sm flex flex-col justify-between"
                  >
                    <div>
                      <div className="flex items-center justify-between">
                        <div className="flex h-9 w-9 items-center justify-center rounded-full border border-[var(--gold-dark)] bg-[#fcf9f2] text-sm font-bold text-[var(--gold-dark)]">
                          {step.step}
                        </div>
                        <span className="text-[10px] font-bold uppercase tracking-[0.2em] text-[#8e7e6e]">
                          Phase 0{step.step}
                        </span>
                      </div>
                      <h4 className="mt-4 font-serif text-xl font-bold uppercase tracking-wide text-[var(--ink)]">
                        {step.name}
                      </h4>
                      <p className="mt-2 text-xs leading-relaxed text-[#675d50]">
                        {step.description}
                      </p>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            {/* Turn Insight Into Impact: Tablet Mockup & Club Advantage */}
            <div className="mt-20 rounded-2xl border border-[rgba(198,165,92,0.38)] bg-[linear-gradient(145deg,#fffdf8_0%,#f8f3e8_100%)] p-6 sm:p-10 shadow-[0_16px_50px_rgba(23,20,18,0.06)]">
              <div className="grid gap-12 lg:grid-cols-12 lg:items-center">
                {/* Left Narrative */}
                <div className="lg:col-span-5">
                  <span className="text-xs font-bold uppercase tracking-[0.24em] text-[var(--gold-dark)]">
                    Turn Insight Into Impact
                  </span>
                  <h3 className="mt-3 font-serif text-3xl sm:text-4xl text-[var(--ink)] leading-tight">
                    See the Bigger Picture
                  </h3>
                  <p className="mt-4 text-sm leading-relaxed text-[#5e5346]">
                    Our optional club dashboard provides anonymized insights on participation, engagement, and key growth areas, helping your leadership team understand the impact and plan for continued success.
                  </p>
                  <div className="mt-6">
                    <CTAButton href="/foundations/club">
                      View Sample Dashboard
                    </CTAButton>
                  </div>
                </div>

                {/* Right: Rendered Luxury Tablet Device Component */}
                <div className="lg:col-span-7">
                  <div className="overflow-hidden rounded-2xl border-4 border-[#241e19] bg-[#120f0d] p-3 sm:p-4 shadow-2xl">
                    <div className="rounded-xl bg-white p-5 sm:p-7 shadow-xs">
                      {/* Tablet Header */}
                      <div className="flex items-center justify-between border-b border-[#ebdcc9] pb-4">
                        <div>
                          <p className="text-[10px] font-bold uppercase tracking-[0.2em] text-[#8e7e6e]">
                            Executive Portal Preview
                          </p>
                          <h4 className="font-serif text-xl font-bold text-[#1e1b18]">
                            Club Impact Overview
                          </h4>
                        </div>
                        <span className="inline-flex items-center gap-1.5 rounded-full bg-[#f4ede1] px-3 py-1 text-[11px] font-bold text-[#8a6828] border border-[#dfcca6]">
                          <span className="h-2 w-2 rounded-full bg-emerald-500 animate-pulse" />
                          <span>Active Season 2026</span>
                        </span>
                      </div>

                      {/* 4 Metric Counters */}
                      <div className="mt-5 grid grid-cols-2 sm:grid-cols-4 gap-3 border-b border-[#ebdcc9] pb-5">
                        <div className="rounded-lg bg-[#fbf9f4] p-3 border border-[#dfcca6]/50">
                          <p className="font-serif text-2xl font-bold text-[#1e1b18]">87%</p>
                          <p className="text-[10px] uppercase tracking-wider text-[#675d50] mt-0.5">
                            Member Satisfaction
                          </p>
                        </div>
                        <div className="rounded-lg bg-[#fbf9f4] p-3 border border-[#dfcca6]/50">
                          <p className="font-serif text-2xl font-bold text-[#1e1b18]">42</p>
                          <p className="text-[10px] uppercase tracking-wider text-[#675d50] mt-0.5">
                            Program Participants
                          </p>
                        </div>
                        <div className="rounded-lg bg-[#fbf9f4] p-3 border border-[#dfcca6]/50">
                          <p className="font-serif text-2xl font-bold text-emerald-700">+68%</p>
                          <p className="text-[10px] uppercase tracking-wider text-[#675d50] mt-0.5">
                            Confidence Shift
                          </p>
                        </div>
                        <div className="rounded-lg bg-[#fbf9f4] p-3 border border-[#dfcca6]/50">
                          <p className="font-serif text-2xl font-bold text-[#1e1b18]">4.8/5</p>
                          <p className="text-[10px] uppercase tracking-wider text-[#675d50] mt-0.5">
                            Overall Experience
                          </p>
                        </div>
                      </div>

                      {/* Growth Areas Progress Bars */}
                      <div className="mt-5">
                        <div className="flex items-center justify-between mb-3">
                          <span className="text-[11px] font-bold uppercase tracking-[0.16em] text-[#1e1b18]">
                            Growth Areas
                          </span>
                          <span className="text-[10px] text-[#8e7e6e]">Aggregated Athlete Self-Reports</span>
                        </div>

                        <div className="space-y-2.5">
                          {growthAreas.map((area) => (
                            <div key={area.label} className="space-y-1">
                              <div className="flex justify-between text-xs font-semibold text-[#4a3f33]">
                                <span>{area.label}</span>
                                <span className="font-mono text-[#8a6828]">{area.percentage}%</span>
                              </div>
                              <div className="h-2 w-full overflow-hidden rounded-full bg-[#eee7d8]">
                                <div
                                  className="h-full bg-[linear-gradient(90deg,#c5aa68_0%,#8a6828_100%)] rounded-full transition-all duration-500"
                                  style={{ width: `${area.percentage}%` }}
                                />
                              </div>
                            </div>
                          ))}
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              {/* The Club Advantage Checklist */}
              <div className="mt-12 border-t border-[rgba(198,165,92,0.3)] pt-8">
                <span className="text-xs font-bold uppercase tracking-[0.24em] text-[var(--gold-dark)]">
                  The Club Advantage
                </span>
                <h4 className="mt-2 font-serif text-2xl text-[var(--ink)]">
                  Invest in What Matters Most
                </h4>
                <div className="mt-6 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
                  {clubAdvantages.map((adv) => (
                    <div key={adv} className="flex items-start gap-3">
                      <CheckCircle2 size={18} className="mt-0.5 shrink-0 text-[var(--gold-dark)]" />
                      <span className="text-xs sm:text-sm text-[#4a3f33] leading-snug">{adv}</span>
                    </div>
                  ))}
                </div>
              </div>
            </div>

            {/* Editorial Feature: Turnkey Private Club Asset (Retained for Test & Content Contract) */}
            <div className="mt-16 overflow-hidden border border-[rgba(198,165,92,0.36)] bg-white shadow-[0_16px_50px_rgba(23,20,18,0.06)] grid lg:grid-cols-12">
              <div className="relative aspect-[16/9] lg:aspect-auto lg:col-span-6 min-h-[320px]">
                <Image
                  src="/foundations/golf/lornette-golf-clubhouse-lounge-putter.png"
                  alt="Lornette Daye holding a golf putter inside an elegant private clubhouse lounge overlooking manicured greens"
                  fill
                  sizes="(max-width: 1024px) 100vw, 50vw"
                  className="object-cover"
                  style={{ objectPosition: "30% 18%" }}
                />
                <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/20" />
              </div>
              <div className="p-8 lg:p-12 lg:col-span-6 flex flex-col justify-center bg-[linear-gradient(135deg,#fffdf8_0%,#faf6ee_100%)]">
                <span className="text-xs font-bold uppercase tracking-[0.22em] text-[var(--gold-dark)]">
                  Turnkey Club Asset
                </span>
                <h3 className="mt-2 font-serif text-3xl text-[var(--ink)]">
                  Seamless Integration for General Managers &amp; Directors of Golf
                </h3>
                <p className="mt-4 text-base leading-relaxed text-[#5e5346]">
                  Lornette’s Foundation brings institutional prestige and tangible member retention value. Designed to harmonize with your club’s PGA professionals rather than replace technical instruction, partnerships enhance member satisfaction, junior development, and inter-club competitive standing.
                </p>
                <div className="mt-6">
                  <CTAButton href="/book">
                    SCHEDULE A LEADERSHIP CONSULTATION
                  </CTAButton>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Engagement Tiers */}
        <section className="border-t border-[var(--line)] bg-[#f6f2e8] px-4 py-16 sm:px-6 lg:px-8 lg:py-20">
          <div className="mx-auto max-w-7xl">
            <div className="max-w-3xl">
              <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--gold-dark)]">
                Flexible Structures
              </p>
              <h2 className="mt-3 font-serif text-3xl leading-tight text-[var(--ink)] sm:text-4xl">
                Partnership Models
              </h2>
            </div>

            <div className="mt-8 grid gap-6 sm:grid-cols-3">
              {partnershipTiers.map((tier) => (
                <div
                  key={tier.tier}
                  className="border border-[rgba(198,165,92,0.38)] bg-white p-7 shadow-sm flex flex-col justify-between"
                >
                  <div>
                    <span className="text-xs font-bold uppercase tracking-[0.16em] text-[var(--gold-dark)]">
                      {tier.highlight}
                    </span>
                    <h3 className="mt-3 font-serif text-2xl text-[var(--ink)]">{tier.tier}</h3>
                    <p className="mt-1 text-xs font-semibold text-[#7d7164]">{tier.subtitle}</p>
                    <p className="mt-4 text-xs leading-6 text-[#675d50]">{tier.description}</p>
                  </div>
                  <div className="mt-6 pt-4 border-t border-[var(--line)]">
                    <Link
                      href="/book"
                      className="inline-flex items-center gap-1 text-xs font-bold uppercase tracking-[0.16em] text-[var(--gold-dark)] hover:underline"
                    >
                      Inquire About This Model &rarr;
                    </Link>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Panoramic Closing Bottom Banner */}
        <section className="relative overflow-hidden border-t border-[rgba(198,165,92,0.4)] min-h-[340px] sm:min-h-[400px] flex items-center px-4 py-16 text-center text-[var(--ivory)] sm:px-6 lg:px-8 lg:py-24">
          <div className="absolute inset-0 pointer-events-none overflow-hidden">
            <Image
              src="/foundations/golf/keynote-bottom-banner-fairway.jpg"
              alt="Prestigious private golf club championship fairway at sunset"
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
              Club Leadership
            </p>
            <h2 className="mt-4 font-serif text-4xl leading-tight sm:text-5xl text-white">
              Partner With Lornette Daye
            </h2>
            <p className="mt-4 text-base leading-8 text-[#d8cdbb]">
              Contact Lornette’s team to explore how a tailored mental performance partnership can elevate your membership this season.
            </p>
            <div className="mt-8 flex flex-col justify-center gap-3 sm:flex-row">
              <CTAButton href="/book">Initiate Partnership Discussion</CTAButton>
              <CTAButton
                href="/speaker-kit"
                variant="secondary"
                className="border-white/30 text-white hover:bg-white/10"
              >
                Download Speaker Kit
              </CTAButton>
            </div>
          </div>
        </section>
      </main>
    </PageShell>
  );
}
