import Image from "next/image";
import { CheckCircle2, Shield, Users, Target, Wrench, Sparkles, Award, RotateCcw } from "lucide-react";

import { CTAButton } from "@/components/CTAButton";
import { PageShell } from "@/components/PageShell";
import { FoundationsSubNav } from "@/components/foundations/FoundationsSubNav";
import { FoundationsFloatingAction } from "@/components/foundations/FoundationsFloatingAction";
import { CorporateExecutiveGallery } from "@/components/foundations/corporate/CorporateExecutiveGallery";
import {
  MotionFadeIn,
  MotionScaleIn,
  MotionStaggerContainer,
  MotionStaggerItem,
  ScrollProgressBar,
  MotionShimmerButton,
} from "@/components/motion";
import { createMetadata } from "@/content/site";

export const metadata = createMetadata(
  "Lornette’s Foundation Corporate | Executive Mental Performance & Team Composure",
  "High-performance executive composure, team accountability, and pressure management for corporate organizations, leadership teams, and premium automotive dealerships.",
  "/foundations/corporate",
);

const corporateSignatureStandouts = [
  {
    title: "Leadership",
    label: "Calm, Purposeful and People-Centred",
    detail: "Authoritative guidance and emotional poise that anchors teams through market change and daily pressure.",
    icon: Shield,
  },
  {
    title: "Resilience",
    label: "Build Capacity Through Change",
    detail: "Sustainable energy systems and bounce-back protocols for high-pressure quarters and monthly cycles.",
    icon: RotateCcw,
  },
  {
    title: "Culture",
    label: "High-Performing Teams and Environments",
    detail: "Psychological trust, mutual respect, and elite alignment across sales, service, finance, and management.",
    icon: Users,
  },
  {
    title: "Focus",
    label: "Clearer Thinking, Better Decisions",
    detail: "Eliminate distraction, protect cognitive clarity, and commit to key priorities under urgent timelines.",
    icon: Target,
  },
  {
    title: "Execution",
    label: "Turn Strategy Into Lasting Impact",
    detail: "Disciplined operational habits and accountability systems derived from Olympic-level championship pedagogy.",
    icon: Award,
  },
];

const dealershipCards = [
  {
    title: "Sales Floor Composure",
    eyebrow: "SALES & CLIENT CONSULTATION",
    icon: Target,
    image: "/foundations/corporate/lornette-executive-boardroom-dialogue.jpg",
    objectPosition: "center 20%",
    description:
      "Help sales teams stay calm, clear, and customer-centred during objections, negotiations, monthly volume targets, and high-stakes buying decisions.",
    highlights: [
      "Composure during tense trade-in and pricing negotiations",
      "Disciplined customer discovery without pushy urgency",
      "Consistent routine execution on busy showroom floors",
    ],
  },
  {
    title: "Service Lane Confidence",
    eyebrow: "FIXED OPERATIONS & SERVICE DRIVE",
    icon: Wrench,
    image: "/foundations/corporate/lornette-executive-presentation-screen.jpg",
    objectPosition: "center 20%",
    description:
      "Support service advisors and technicians with reset tools, communication habits, and emotional control during urgent or difficult customer moments.",
    highlights: [
      "The 5-Second Reset after heated client interactions",
      "Clear, non-defensive communication on repair timelines",
      "Protecting CSI standards during peak morning intake rushes",
    ],
  },
  {
    title: "Premium Customer Experience",
    eyebrow: "OWNERSHIP JOURNEY & CSI EXCELLENCE",
    icon: Sparkles,
    image: "/foundations/corporate/lornette-executive-one-on-one-consultation.jpg",
    objectPosition: "center 20%",
    description:
      "Train teams to create trust, consistency, and care across the full ownership journey, from first conversation to long-term service relationships.",
    highlights: [
      "Seamless client handoffs between Sales, F&I, and Service",
      "Concierge-level attention to detail and personalized delivery",
      "Elevated customer retention and high-trust referrals",
    ],
  },
  {
    title: "Leadership & Culture",
    eyebrow: "MANAGEMENT & GENERAL MANAGERS",
    icon: Award,
    image: "/foundations/corporate/lornette-executive-leadership-standing-portrait.jpg",
    objectPosition: "center 15%",
    description:
      "Equip managers to reinforce standards, coach through pressure, and build a team culture where performance and people both matter.",
    highlights: [
      "Daily huddles that inspire focus rather than anxiety",
      "Holding accountability without destructive micromanagement",
      "Unifying cross-departmental trust between front and back of house",
    ],
  },
];

const corporatePillars = [
  {
    title: "Executive Composure Under Pressure",
    icon: Shield,
    description:
      "Maintain strategic perspective, emotional regulation, and calm authority during high-stakes reviews, sudden market turbulence, and organizational changes.",
  },
  {
    title: "The Reset Protocol for Leaders",
    icon: RotateCcw,
    description:
      "A proven five-second cognitive reset to shed compounding workplace stress, eliminate rumination, and re-engage teams with clarity and poise.",
  },
  {
    title: "High-Trust Team Accountability",
    icon: Users,
    description:
      "Build organizational cultures where candor, psychological safety, and mutual standards elevate cross-departmental execution across sales, service, and operations.",
  },
  {
    title: "Sustainable Peak Performance",
    icon: Award,
    description:
      "Replace burnout cycles with the disciplined energy-management frameworks practiced by elite multi-decade Olympic coaches.",
  },
];

const corporateAudiences = [
  "Automotive Dealership Groups & Retail Leadership Teams",
  "General Managers, Sales Directors & Service Drive Leaders",
  "C-Suite & Executive Enterprise Leadership Teams",
  "Senior Management & Regional Operations Directors",
  "High-Growth Retail, Technology & Professional Firms",
  "Corporate Retreats, Annual Offsites & Keynote Banquets",
];

export default function FoundationsCorporatePage() {
  return (
    <PageShell>
      <ScrollProgressBar />
      <main className="bg-[var(--ivory)] text-[var(--ink)]">
        <FoundationsSubNav />

        {/* Hero Section */}
        <section className="relative overflow-hidden border-b border-[rgba(198,165,92,0.35)] bg-[var(--ivory)] px-4 py-14 sm:px-6 lg:px-8 lg:py-20">
          <div className="pointer-events-none absolute inset-0 bg-[linear-gradient(115deg,rgba(255,255,255,0.92)_0%,rgba(250,247,240,0.84)_46%,rgba(232,221,203,0.58)_100%)]" />

          <div className="relative mx-auto max-w-7xl">
            <div className="grid gap-12 lg:grid-cols-12 lg:items-center">
              <MotionFadeIn className="lg:col-span-7">
                <div className="flex flex-wrap items-center gap-2">
                  <span className="border border-[rgba(198,165,92,0.48)] bg-white/70 px-3.5 py-1.5 text-xs font-bold uppercase tracking-[0.24em] text-[var(--gold-dark)] shadow-sm">
                    LORNETTE’S FOUNDATION | CORPORATE &amp; RETAIL LEADERSHIP
                  </span>
                </div>

                <h1 className="mt-6 font-serif text-4xl leading-[1.02] text-balance text-[var(--ink)] sm:text-6xl lg:text-[4.2rem]">
                  Bring Championship Composure to Work.
                </h1>

                <p className="mt-5 font-serif text-2xl text-[var(--gold-dark)] sm:text-3xl">
                  Leadership, Culture &amp; Performance Under Pressure
                </p>

                <p className="mt-6 text-base leading-8 text-[#554b40] sm:text-lg">
                  A practical leadership and performance experience for executives, dealership leaders, and organizations navigating pressure, monthly targets, customer expectations, and high-stakes execution.
                </p>

                <div className="mt-8 flex flex-col gap-3 sm:flex-row">
                  <MotionShimmerButton href="#dealerships">Explore Dealership Program</MotionShimmerButton>
                  <CTAButton href="/book" variant="secondary">
                    Request a Strategy Conversation
                  </CTAButton>
                </div>
              </MotionFadeIn>

              <MotionScaleIn className="relative lg:col-span-5" delay={0.15}>
                <div className="relative w-full aspect-[4/5] overflow-hidden border border-[rgba(198,165,92,0.42)] bg-[linear-gradient(180deg,#fffdf8_0%,#f5efe4_100%)] shadow-[0_28px_110px_rgba(23,20,18,0.14)]">
                  <Image
                    src="/foundations/corporate/lornette-corporate-hero.jpg"
                    alt="Lornette Daye leading an executive leadership conversation in high-rise corporate boardroom"
                    fill
                    priority
                    sizes="(max-width: 1024px) 100vw, 42vw"
                    className="object-cover"
                    style={{ objectPosition: "center top" }}
                  />
                  <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/40" />
                  <div className="absolute inset-x-0 bottom-0 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(18,15,13,0.85)] p-4 sm:p-5 backdrop-blur-md shadow-2xl">
                    <p className="text-[11px] font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
                      CORPORATE &amp; DEALERSHIP LEADERSHIP
                    </p>
                    <p className="mt-1 font-serif text-base text-white sm:text-lg leading-snug">
                      Strategic Focus &amp; High-Trust Culture Under Pressure
                    </p>
                  </div>
                </div>
              </MotionScaleIn>
            </div>
          </div>
        </section>

        {/* Signature Standouts Strip */}
        <section
          aria-label="Corporate signature standouts"
          className="border-b border-[var(--line)] bg-white px-4 py-10 sm:px-6 lg:px-8"
        >
          <div className="mx-auto max-w-7xl">
            <MotionStaggerContainer className="grid gap-6 sm:grid-cols-2 lg:grid-cols-5 divide-y divide-[rgba(198,165,92,0.3)] sm:divide-y-0">
              {corporateSignatureStandouts.map((item, idx) => {
                const StatIcon = item.icon;
                return (
                  <MotionStaggerItem
                    key={item.title}
                    className={`text-center border-l-0 lg:border-l lg:first:border-l-0 border-[rgba(198,165,92,0.3)] ${
                      idx > 0 ? "pt-6 sm:pt-0 lg:pl-6" : ""
                    }`}
                  >
                    <div className="mx-auto mb-2.5 flex h-8 w-8 items-center justify-center rounded-full border border-[rgba(198,165,92,0.35)] bg-[var(--sand)]/40 text-[var(--gold-dark)] shadow-xs">
                      <StatIcon size={16} aria-hidden="true" />
                    </div>
                    <p className="font-serif text-2xl sm:text-3xl font-bold tracking-tight text-[var(--gold-dark)]">
                      {item.title}
                    </p>
                    <span className="mt-1 block text-xs font-bold uppercase tracking-[0.16em] text-[var(--ink)]">
                      {item.label}
                    </span>
                    <span className="mt-1.5 block text-xs leading-relaxed text-[#675d50]">
                      {item.detail}
                    </span>
                  </MotionStaggerItem>
                );
              })}
            </MotionStaggerContainer>
          </div>
        </section>

        {/* Dedicated Dealership Section: Built for Dealership Teams Under Pressure */}
        <section id="dealerships" className="scroll-mt-24 px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <MotionFadeIn className="text-center max-w-3xl mx-auto">
              <span className="border border-[rgba(198,165,92,0.48)] bg-white/70 px-3.5 py-1.5 text-xs font-bold uppercase tracking-[0.24em] text-[var(--gold-dark)] shadow-sm inline-block mb-4">
                AUTOMOTIVE RETAIL &amp; DEALER EXCELLENCE
              </span>
              <h2 className="font-serif text-3xl sm:text-5xl text-[var(--ink)] leading-tight">
                Built for Dealership Teams Under Pressure
              </h2>
              <p className="mt-5 text-base sm:text-lg leading-relaxed text-[#554b40]">
                Automotive dealerships operate in a constant performance environment. Sales teams carry monthly targets. Service teams manage urgency, expectations, and trust. Finance teams guide customers through major decisions. Leaders hold the standard across the entire ownership experience.
              </p>
              <p className="mt-3 text-base sm:text-lg leading-relaxed text-[#554b40]">
                Lornette’s Foundation Corporate helps dealership teams build the composure, communication, accountability, and reset skills needed to perform with consistency when the pressure rises.
              </p>
            </MotionFadeIn>

            {/* 4 Dealership Cards */}
            <MotionStaggerContainer className="mt-14 grid gap-8 sm:grid-cols-2 lg:grid-cols-4">
              {dealershipCards.map((card) => {
                const Icon = card.icon;
                return (
                  <MotionStaggerItem
                    key={card.title}
                    className="group flex flex-col justify-between overflow-hidden border border-[rgba(198,165,92,0.36)] bg-white shadow-[0_16px_50px_rgba(23,20,18,0.06)] transition-all duration-300 hover:-translate-y-1 hover:border-[#dfc385] hover:shadow-[0_24px_60px_rgba(23,20,18,0.14)]"
                  >
                    <div>
                      {/* Card Image with Docked Luxury Editorial Plaque */}
                      <div className="relative aspect-[4/5] w-full overflow-hidden bg-[#120f0d]">
                        <Image
                          src={card.image}
                          alt={card.title}
                          fill
                          sizes="(max-width: 1024px) 100vw, 25vw"
                          className="object-cover transition-transform duration-700 ease-out group-hover:scale-105"
                          style={{ objectPosition: card.objectPosition }}
                        />
                        <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-black/85 via-black/25 to-transparent opacity-80 group-hover:opacity-70 transition-opacity" />
                        <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/10" />

                        <div className="absolute inset-x-0 bottom-0 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(18,15,13,0.85)] p-3.5 backdrop-blur-md shadow-2xl">
                          <p className="text-[10px] font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
                            {card.eyebrow}
                          </p>
                          <p className="mt-0.5 font-serif text-base text-white leading-snug">
                            {card.title}
                          </p>
                        </div>
                      </div>

                      <div className="p-6">
                        <div className="flex items-center gap-2 mb-3">
                          <div className="h-8 w-8 rounded-full border border-[rgba(198,165,92,0.4)] bg-[var(--sand)]/40 flex items-center justify-center text-[var(--gold-dark)] shrink-0">
                            <Icon size={16} />
                          </div>
                          <span className="text-[11px] font-bold uppercase tracking-[0.16em] text-[var(--gold-dark)]">
                            Core Standard
                          </span>
                        </div>
                        <p className="text-xs sm:text-sm leading-relaxed text-[#675d50]">
                          {card.description}
                        </p>
                      </div>
                    </div>

                    <div className="border-t border-[rgba(198,165,92,0.22)] p-6 pt-4 bg-[linear-gradient(180deg,#fffdfa_0%,#faf6ee_100%)]">
                      <p className="text-[10px] font-bold uppercase tracking-[0.18em] text-[#7d7164] mb-2.5">
                        Key Applications
                      </p>
                      <ul className="space-y-1.5">
                        {card.highlights.map((point) => (
                          <li key={point} className="flex items-start gap-2 text-xs text-[#5e5346]">
                            <CheckCircle2 size={13} className="text-[var(--gold-dark)] shrink-0 mt-0.5" />
                            <span>{point}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                  </MotionStaggerItem>
                );
              })}
            </MotionStaggerContainer>

            {/* Premium Automotive Retail Precision Editorial Box */}
            <MotionFadeIn className="mt-14 overflow-hidden border border-[rgba(198,165,92,0.48)] bg-[linear-gradient(135deg,#1b1612_0%,#120f0d_100%)] text-white shadow-xl">
              <div className="grid lg:grid-cols-12 items-stretch">
                <div className="flex flex-col justify-between p-8 sm:p-12 lg:col-span-7">
                  <div>
                    <span className="border border-[rgba(198,165,92,0.4)] bg-white/5 px-3 py-1 text-[11px] font-bold uppercase tracking-[0.24em] text-[var(--champagne)] shadow-sm inline-block">
                      RETAIL BENCHMARK EXCELLENCE
                    </span>
                    <h3 className="mt-4 font-serif text-2xl sm:text-3xl lg:text-4xl text-white leading-tight">
                      Consistency, Composure and the Human Element
                    </h3>
                    <p className="mt-4 text-base sm:text-lg leading-relaxed text-[#d5cbbe]">
                      For high-performance dealerships representing premium automotive brands, the customer experience depends on more than product specifications. It depends on composed people, clear communication, consistent standards, and the ability to guide clients through major decisions with steady confidence.
                    </p>
                    <div className="mt-6 flex items-center gap-4 text-xs font-semibold uppercase tracking-[0.18em] text-[var(--champagne)]">
                      <span className="flex items-center gap-1.5">
                        <CheckCircle2 size={15} className="text-[var(--champagne)]" />
                        Executive Alignment
                      </span>
                      <span className="flex items-center gap-1.5">
                        <CheckCircle2 size={15} className="text-[var(--champagne)]" />
                        Dealership Cohorts
                      </span>
                    </div>
                  </div>

                  <div className="mt-8 flex flex-wrap gap-4 pt-6 border-t border-[rgba(198,165,92,0.25)]">
                    <CTAButton href="/book">
                      Request a Strategy Conversation
                    </CTAButton>
                    <CTAButton href="/leadership" variant="secondary">
                      View Foundation Formats
                    </CTAButton>
                  </div>
                </div>

                <div className="relative min-h-[340px] sm:min-h-[420px] lg:col-span-5 overflow-hidden bg-[#120f0d]">
                  <Image
                    src="/foundations/corporate/lornette-executive-podium-full.jpg"
                    alt="Lornette Daye addressing executive leaders at podium assembly"
                    fill
                    sizes="(max-width: 1024px) 100vw, 42vw"
                    className="object-cover"
                    style={{ objectPosition: "center 20%" }}
                  />
                  <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-black/85 via-black/20 to-transparent opacity-75" />
                  <div className="absolute inset-x-0 bottom-0 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(18,15,13,0.88)] p-4 sm:p-5 backdrop-blur-md shadow-2xl">
                    <p className="text-[10px] font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
                      KEYNOTE &amp; EXECUTIVE BRIEFING
                    </p>
                    <p className="mt-1 font-serif text-base text-white sm:text-lg leading-snug">
                      High-Impact Leadership Alignment
                    </p>
                  </div>
                </div>
              </div>
            </MotionFadeIn>

            {/* Featured Executive Workshop Showcase */}
            <MotionFadeIn className="mt-10 overflow-hidden border border-[rgba(198,165,92,0.4)] bg-white shadow-xl">
              <div className="grid lg:grid-cols-12 items-stretch">
                <div className="relative min-h-[360px] sm:min-h-[440px] lg:col-span-5 overflow-hidden bg-[#120f0d]">
                  <Image
                    src="/foundations/corporate/lornette-executive-roundtable-standing.jpg"
                    alt="Lornette Daye leading executive corporate leadership roundtable workshop"
                    fill
                    sizes="(max-width: 1024px) 100vw, 42vw"
                    className="object-cover"
                    style={{ objectPosition: "center 20%" }}
                  />
                  <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-black/85 via-black/25 to-transparent opacity-80" />
                  <div className="absolute inset-x-0 bottom-0 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(18,15,13,0.86)] p-4 sm:p-5 backdrop-blur-md shadow-2xl">
                    <p className="text-[10px] font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
                      THE LEADERSHIP INTENSIVE
                    </p>
                    <p className="mt-1 font-serif text-base text-white sm:text-lg leading-snug">
                      High-Trust Standards in High-Pressure Environments
                    </p>
                  </div>
                </div>

                <div className="flex flex-col justify-between p-8 sm:p-10 lg:col-span-7 bg-[linear-gradient(135deg,#fffdf8_0%,#faf5eb_100%)]">
                  <div>
                    <span className="border border-[rgba(198,165,92,0.48)] bg-white/80 px-3 py-1 text-[11px] font-bold uppercase tracking-[0.22em] text-[var(--gold-dark)] shadow-sm inline-block">
                      EXECUTIVE &amp; DEALERSHIP MASTERCLASS
                    </span>
                    <h3 className="mt-4 font-serif text-2xl sm:text-3xl lg:text-4xl text-[var(--ink)] leading-snug">
                      Translating Elite Athletic Habits into Daily Commercial Execution
                    </h3>
                    <p className="mt-4 text-base leading-relaxed text-[#554b40]">
                      In dealership retail and corporate environments, pressure is not an occasional visitor; it is the daily atmosphere. When monthly quotas converge with customer disputes or supply timelines, emotional composure determines whether a team thrives or fractures.
                    </p>
                    <p className="mt-3 text-base leading-relaxed text-[#554b40]">
                      Lornette Daye equips management teams with practical somatic reset tools, non-defensive communication patterns, and daily accountability structures that create lasting composure across every department.
                    </p>

                    <div className="mt-6 grid gap-4 sm:grid-cols-2">
                      <div className="border border-[rgba(198,165,92,0.3)] bg-white p-4 shadow-sm">
                        <p className="text-xs font-bold uppercase tracking-[0.18em] text-[var(--gold-dark)]">
                          Showroom &amp; Sales Composure
                        </p>
                        <p className="mt-1 text-xs text-[#675d50] leading-relaxed">
                          Patience and emotional poise through complex client negotiations and trade appraisals.
                        </p>
                      </div>
                      <div className="border border-[rgba(198,165,92,0.3)] bg-white p-4 shadow-sm">
                        <p className="text-xs font-bold uppercase tracking-[0.18em] text-[var(--gold-dark)]">
                          Fixed Ops &amp; Service Resilience
                        </p>
                        <p className="mt-1 text-xs text-[#675d50] leading-relaxed">
                          Calm reset protocols that protect CSI scores during urgent customer delivery moments.
                        </p>
                      </div>
                    </div>
                  </div>

                  <div className="mt-8 flex flex-wrap items-center gap-4 pt-6 border-t border-[rgba(198,165,92,0.25)]">
                    <CTAButton href="/book">
                      REQUEST A CORPORATE BRIEFING
                    </CTAButton>
                    <CTAButton href="/leadership" variant="secondary">
                      VIEW EXECUTIVE PILLARS
                    </CTAButton>
                  </div>
                </div>
              </div>
            </MotionFadeIn>
          </div>
        </section>

        {/* Dynamic Framer Motion Executive Spaces & Practices Gallery */}
        <CorporateExecutiveGallery />

        {/* Corporate Pillars Strip */}
        <section className="border-t border-[var(--line)] bg-[var(--sand)]/30 px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <MotionFadeIn className="text-center max-w-3xl mx-auto">
              <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--gold-dark)]">
                EXECUTIVE FRAMEWORK
              </p>
              <h2 className="mt-3 font-serif text-3xl sm:text-4xl text-[var(--ink)]">
                The Principles Behind Leadership Composure
              </h2>
              <p className="mt-4 text-base text-[#675d50]">
                Bridging athletic championship habits with corporate strategy, governance, and daily operational execution.
              </p>
            </MotionFadeIn>

            <MotionStaggerContainer className="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
              {corporatePillars.map((pillar) => {
                const Icon = pillar.icon;
                return (
                  <MotionStaggerItem
                    key={pillar.title}
                    className="border border-[rgba(198,165,92,0.34)] bg-white p-6 shadow-sm transition hover:-translate-y-1 hover:border-[var(--champagne)] flex flex-col justify-between"
                  >
                    <div>
                      <div className="flex h-9 w-9 items-center justify-center rounded-full border border-[rgba(198,165,92,0.35)] bg-[var(--sand)]/35 text-[var(--gold-dark)] shadow-xs mb-4">
                        <Icon size={17} aria-hidden="true" />
                      </div>
                      <h3 className="font-serif text-xl text-[var(--ink)]">{pillar.title}</h3>
                      <div className="mt-3 h-0.5 w-8 bg-[var(--champagne)]" aria-hidden="true" />
                      <p className="mt-3 text-sm leading-6 text-[#675d50]">{pillar.description}</p>
                    </div>
                  </MotionStaggerItem>
                );
              })}
            </MotionStaggerContainer>
          </div>
        </section>

        {/* Audiences */}
        <section className="border-t border-[var(--line)] bg-white px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <div className="grid gap-8 lg:grid-cols-2 lg:items-center">
              <MotionFadeIn>
                <p className="text-xs font-bold uppercase tracking-[0.22em] text-[var(--gold-dark)]">
                  WHO IT IS FOR
                </p>
                <h2 className="mt-3 font-serif text-3xl sm:text-4xl text-[var(--ink)]">
                  Formats Engineered for High-Pressure Teams
                </h2>
                <p className="mt-4 text-base leading-7 text-[#675d50]">
                  Whether coaching an automotive dealership executive team through monthly closing targets or delivering a keynote address to regional corporate directors.
                </p>
              </MotionFadeIn>

              <MotionStaggerContainer className="grid gap-3">
                {corporateAudiences.map((group) => (
                  <MotionStaggerItem
                    key={group}
                    className="flex items-center gap-3 border border-[rgba(198,165,92,0.3)] bg-[var(--ivory)] p-4 shadow-sm"
                  >
                    <CheckCircle2 size={18} className="text-[var(--gold-dark)] shrink-0" />
                    <span className="text-sm font-semibold text-[var(--ink)]">{group}</span>
                  </MotionStaggerItem>
                ))}
              </MotionStaggerContainer>
            </div>
          </div>
        </section>

        {/* Panoramic Closing CTA */}
        <section className="relative overflow-hidden min-h-[380px] sm:min-h-[460px] border-t border-[rgba(198,165,92,0.4)] flex items-center justify-center text-center px-4 py-16">
          <Image
            src="/foundations/corporate/dealership-boardroom-vehicles.jpg"
            alt="Dealership executive boardroom overlooking luxury vehicle lot at sunset"
            fill
            sizes="100vw"
            quality={95}
            className="object-cover object-center"
          />
          <div className="absolute inset-0 bg-gradient-to-t from-black/85 via-black/55 to-black/75" />
          <MotionFadeIn className="relative z-10 max-w-3xl mx-auto text-white">
            <p className="text-xs font-bold uppercase tracking-[0.24em] text-[var(--champagne)]">
              TRANSFORM YOUR ORGANIZATION
            </p>
            <h2 className="mt-3 font-serif text-3xl sm:text-5xl text-white">
              Cultivate Executive Poise and Resilient Teams
            </h2>
            <p className="mt-4 text-base sm:text-lg text-white/85">
              Contact our office to arrange an executive briefing, dealership team intensive, or keynote workshop with Lornette Daye.
            </p>
            <div className="mt-8 flex flex-wrap justify-center gap-4">
              <MotionShimmerButton href="/book">DISCUSS A CORPORATE ENGAGEMENT</MotionShimmerButton>
              <CTAButton href="/leadership" variant="secondary">
                EXPLORE LEADERSHIP PILLARS
              </CTAButton>
            </div>
          </MotionFadeIn>
        </section>
      </main>
      <FoundationsFloatingAction track="corporate" />
    </PageShell>
  );
}
