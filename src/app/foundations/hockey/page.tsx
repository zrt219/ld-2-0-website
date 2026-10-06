import Image from "next/image";
import { Target, Activity, Users, Shield, Award, GraduationCap, RotateCcw } from "lucide-react";

import { CTAButton } from "@/components/CTAButton";
import { PageShell } from "@/components/PageShell";
import { FoundationsSubNav } from "@/components/foundations/FoundationsSubNav";
import { FoundationsFloatingAction } from "@/components/foundations/FoundationsFloatingAction";
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
  "Lornette’s Foundation Hockey | High-Performance Team Composure",
  "Mental performance, composure under contact, and championship resilience for competitive hockey players, academies, and teams.",
  "/foundations/hockey",
);

const hockeySignatureStandouts = [
  {
    title: "Focus",
    label: "Mental Clarity in the Moment",
    detail: "Stay locked in through high-speed transitions and physical pressure.",
    icon: Target,
  },
  {
    title: "Recovery",
    label: "Tools to Reset and Perform Again",
    detail: "Neutralize emotion in five seconds, step onto the ice clear for your next shift.",
    icon: RotateCcw,
  },
  {
    title: "Team Culture",
    label: "Stronger Teams Through Shared Mindset",
    detail: "Unified accountability, non-defensive communication standards, and mutual trust.",
    icon: Users,
  },
  {
    title: "Pressure",
    label: "Stay Calm When It Intensifies",
    detail: "Calm decision-making and decisive execution in third-period intensity.",
    icon: Shield,
  },
  {
    title: "Leadership",
    label: "Athletes Who Lead From Within",
    detail: "Personal composure and character that set the standard in every locker room.",
    icon: Award,
  },
];

const builtForCards = [
  {
    title: "Athletes",
    eyebrow: "ATHLETE PATHWAY",
    icon: Target,
    image: "/foundations/hockey/lornette-hockey-ice-huddle.jpg",
    objectPosition: "center 20%",
    description: "Develop focus, emotional control and confidence to perform at your best.",
  },
  {
    title: "Teams",
    eyebrow: "TEAM CULTURE",
    icon: Users,
    image: "/foundations/hockey/lornette-hockey-boardroom-executive.jpg",
    objectPosition: "center 25%",
    description: "Build a stronger culture, leadership standards, and unified team alignment.",
  },
  {
    title: "Academies",
    eyebrow: "ACADEMY FOUNDATIONS",
    icon: GraduationCap,
    image: "/foundations/pathways/hockey/lornette-hockey-ice-portrait.png",
    objectPosition: "center 25%",
    description: "Equip the next generation with the mental tools to thrive on and off the ice.",
  },
];

const fiveFoundations = [
  {
    title: "Focus",
    icon: Target,
    description: "Be present, make better decisions, and stay in the moment.",
  },
  {
    title: "Recovery",
    icon: Activity,
    description: "Reset quickly, manage emotions, and bounce back stronger.",
  },
  {
    title: "Team Culture",
    icon: Users,
    description: "Communicate clearly, build trust, and play with purpose.",
  },
  {
    title: "Pressure",
    icon: Shield,
    description: "Stay composed in high-stakes moments and perform under pressure.",
  },
  {
    title: "Leadership",
    icon: Award,
    description: "Lead by example, elevate others, and create a positive standard.",
  },
];

const gameSpeedComposureCards = [
  {
    title: "Reset After Mistakes",
    eyebrow: "SHIFT-TO-SHIFT COMPOSURE",
    image: "/foundations/hockey/lornette-hockey-bench-coaching.jpg",
    objectPosition: "center 20%",
    description: "Let go, refocus, and get back into the game with a clear mind.",
  },
  {
    title: "Stronger Communication",
    eyebrow: "BOARDS & ICE CONNECTION",
    image: "/foundations/hockey/lornette-hockey-boards-rink.jpg",
    objectPosition: "center 25%",
    description: "Build trust, stay connected, and support each other through intense shifts.",
  },
  {
    title: "Confidence Under Pressure",
    eyebrow: "DECISIVE EXECUTION",
    image: "/foundations/hockey/lornette-hockey-digital-tactics.jpg",
    objectPosition: "center 20%",
    description: "Stay calm, trust your preparation, and perform when it matters most.",
  },
];

const tacticalShowcaseCards = [
  {
    title: "Locker Room Strategy Alignment",
    eyebrow: "STRATEGIC INTENT",
    image: "/foundations/hockey/lornette-hockey-whiteboard-strategy.jpg",
    objectPosition: "center 20%",
    description: "Whiteboard breakdowns that transform high-pressure assignments into clear, instinctive execution before the puck drops.",
  },
  {
    title: "Bench Composure & Shift Cadence",
    eyebrow: "EMOTIONAL REGULATION",
    image: "/foundations/hockey/hockey-boards-communication.png",
    objectPosition: "center 20%",
    description: "Direct real-time reset coaching between whistles to keep players grounded, non-reactive, and prepared for the next shift.",
  },
  {
    title: "On-Ice Huddle & Athlete Poise",
    eyebrow: "TEAM SYNCHRONICITY",
    image: "/foundations/hockey/lornette-hockey-on-ice-huddle.jpg",
    objectPosition: "center 20%",
    description: "Unified athlete presence where Lornette Daye instills calm authority, accountable peer support, and collective resilience.",
  },
  {
    title: "Video Room Analytics & Reads",
    eyebrow: "DECISION PRECISION",
    image: "/foundations/pathways/hockey/lornette-hockey-video-analytics.png",
    objectPosition: "center 20%",
    description: "Deep game analysis and perceptual training translating film breakdowns directly into instinctive ice execution.",
  },
];

const onIceActionStockCards = [
  {
    title: "High-Speed Shift Transitions",
    eyebrow: "GAME-SPEED READS",
    image: "/foundations/hockey/hockey-action-pressure.png",
    objectPosition: "center 25%",
    description: "Processing dynamic lane coverage and high-speed neutral zone transitions without hesitation.",
  },
  {
    title: "Locker Room Focus & Chemistry",
    eyebrow: "TEAM HUDDLE",
    image: "/foundations/hockey/hockey-coach-huddle.png",
    objectPosition: "center 20%",
    description: "Establishing mutual trust and shared team standards in the locker room before stepping onto the ice.",
  },
  {
    title: "Bench Reset Between Whistles",
    eyebrow: "RAPID RECOVERY",
    image: "/foundations/hockey/hockey-bench-reset-stock.jpg",
    objectPosition: "center 20%",
    description: "Breath regulation and shift neutrality that ensure errors do not carry over to the next possession.",
  },
  {
    title: "Tactical Execution on the Fly",
    eyebrow: "PLAYBOOK PRECISION",
    image: "/foundations/hockey/hockey-tactical-playbook.png",
    objectPosition: "center 20%",
    description: "Translating team systems into instant muscle memory and synchronized five-man execution.",
  },
];

export default function FoundationsHockeyPage() {
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
                    LORNETTE’S FOUNDATION | HOCKEY PERFORMANCE
                  </span>
                </div>

                <h1 className="mt-6 font-serif text-4xl leading-[1.02] text-balance text-[var(--ink)] sm:text-6xl lg:text-[4.2rem]">
                  Stay Composed When the Game Speeds Up.
                </h1>

                <p className="mt-5 font-serif text-2xl text-[var(--gold-dark)] sm:text-3xl">
                  Lornette’s Foundation Hockey
                </p>

                <p className="mt-6 text-base leading-8 text-[#554b40] sm:text-lg">
                  A mental performance and team culture pathway for hockey athletes, teams, academies, and programs that need focus, recovery, leadership, and composure in high-pressure moments.
                </p>

                <div className="mt-8 flex flex-col gap-3 sm:flex-row">
                  <MotionShimmerButton href="#built-for">Explore Hockey Program</MotionShimmerButton>
                  <CTAButton href="/book" variant="secondary">
                    For Teams &amp; Academies
                  </CTAButton>
                </div>
              </MotionFadeIn>

              <MotionScaleIn className="relative lg:col-span-5" delay={0.15}>
                <div className="relative w-full aspect-[4/5] overflow-hidden border border-[rgba(198,165,92,0.42)] bg-[linear-gradient(180deg,#fffdf8_0%,#f5efe4_100%)] shadow-[0_28px_110px_rgba(23,20,18,0.14)]">
                  <Image
                    src="/foundations/hockey/lornette-hockey-hero.jpg"
                    alt="Olympic-level coach Lornette Daye speaking with competitive hockey players on the ice"
                    fill
                    priority
                    sizes="(max-width: 1024px) 100vw, 42vw"
                    className="object-cover"
                    style={{ objectPosition: "center top" }}
                  />
                  <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/40" />
                  <div className="absolute inset-x-0 bottom-0 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(18,15,13,0.85)] p-4 sm:p-5 backdrop-blur-md shadow-2xl">
                    <p className="text-[11px] font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
                      YOUR MIND LEADS YOUR GAME
                    </p>
                    <p className="mt-1 font-serif text-base text-white sm:text-lg leading-snug">
                      A calmer mind. A stronger team. A higher standard.
                    </p>
                  </div>
                </div>
              </MotionScaleIn>
            </div>
          </div>
        </section>

        {/* Signature Standouts Strip */}
        <section
          aria-label="Hockey signature standouts"
          className="border-b border-[var(--line)] bg-white px-4 py-10 sm:px-6 lg:px-8"
        >
          <div className="mx-auto max-w-7xl">
            <MotionStaggerContainer className="grid gap-6 sm:grid-cols-2 lg:grid-cols-5 divide-y divide-[rgba(198,165,92,0.3)] sm:divide-y-0">
              {hockeySignatureStandouts.map((item, idx) => {
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

        {/* Section 1: Built For (3 Photo Cards) */}
        <section id="built-for" className="scroll-mt-24 px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <MotionFadeIn className="text-center max-w-3xl mx-auto">
              <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--gold-dark)]">
                BUILT FOR
              </p>
              <h2 className="mt-3 font-serif text-3xl sm:text-4xl text-[var(--ink)]">
                Athletes, Teams &amp; Academies
              </h2>
              <p className="mt-4 text-base text-[#675d50]">
                Practical mental systems tailored to the intensity, speed, and physical demands of modern competitive hockey.
              </p>
            </MotionFadeIn>

            <MotionStaggerContainer className="mt-12 grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
              {builtForCards.map((card) => {
                const Icon = card.icon;
                return (
                  <MotionStaggerItem
                    key={card.title}
                    className="group flex flex-col overflow-hidden border border-[rgba(198,165,92,0.36)] bg-white shadow-[0_16px_50px_rgba(23,20,18,0.06)] transition-all duration-300 hover:-translate-y-1 hover:border-[#dfc385] hover:shadow-[0_24px_60px_rgba(23,20,18,0.14)]"
                  >
                    <div className="relative aspect-[16/10] w-full overflow-hidden bg-[#120f0d]">
                      <Image
                        src={card.image}
                        alt={card.title}
                        fill
                        sizes="(max-width: 1024px) 100vw, 33vw"
                        className="object-cover transition-transform duration-700 ease-out group-hover:scale-105"
                        style={{ objectPosition: card.objectPosition }}
                      />
                      <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent opacity-75 group-hover:opacity-60 transition-opacity" />
                      <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/10" />

                      <div className="absolute inset-x-0 bottom-0 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(18,15,13,0.85)] p-4 backdrop-blur-md shadow-2xl">
                        <p className="text-[10px] font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
                          {card.eyebrow}
                        </p>
                        <p className="mt-1 font-serif text-base text-white leading-snug">
                          {card.title}
                        </p>
                      </div>
                    </div>

                    <div className="flex flex-1 flex-col justify-between p-6 bg-[linear-gradient(180deg,#fffdfa_0%,#faf6ee_100%)]">
                      <div>
                        <div className="flex items-center gap-2 mb-3">
                          <div className="h-8 w-8 rounded-full border border-[rgba(198,165,92,0.4)] bg-[var(--sand)]/40 flex items-center justify-center text-[var(--gold-dark)] shrink-0">
                            <Icon size={16} />
                          </div>
                          <span className="text-[11px] font-bold uppercase tracking-[0.16em] text-[var(--gold-dark)]">
                            Pathway Focus
                          </span>
                        </div>
                        <p className="text-sm leading-relaxed text-[#554b40]">
                          {card.description}
                        </p>
                      </div>
                    </div>
                  </MotionStaggerItem>
                );
              })}
            </MotionStaggerContainer>
          </div>
        </section>

        {/* Section 2: What Hockey Players Train With (Five Foundations) */}
        <section className="border-t border-[var(--line)] bg-[var(--sand)]/30 px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <MotionFadeIn className="text-center max-w-3xl mx-auto">
              <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--gold-dark)]">
                WHAT HOCKEY PLAYERS TRAIN WITH
              </p>
              <h2 className="mt-3 font-serif text-3xl sm:text-4xl text-[var(--ink)]">
                Five Foundations for a Stronger Game
              </h2>
              <p className="mt-4 text-base text-[#675d50]">
                Repeatable tools designed to withstand contact, momentum swings, and high-pressure moments.
              </p>
            </MotionFadeIn>

            <MotionStaggerContainer className="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-5">
              {fiveFoundations.map((foundation) => {
                const Icon = foundation.icon;
                return (
                  <MotionStaggerItem
                    key={foundation.title}
                    className="border border-[rgba(198,165,92,0.34)] bg-white p-6 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:border-[var(--champagne)] flex flex-col justify-between"
                  >
                    <div>
                      <div className="h-12 w-12 rounded-full border border-[rgba(198,165,92,0.4)] bg-[var(--sand)]/40 flex items-center justify-center text-[var(--gold-dark)] mb-4">
                        <Icon size={22} />
                      </div>
                      <h3 className="font-serif text-lg font-bold text-[var(--ink)]">{foundation.title}</h3>
                      <div className="mt-2.5 h-0.5 w-7 bg-[var(--champagne)]" aria-hidden="true" />
                      <p className="mt-3 text-xs leading-relaxed text-[#675d50]">{foundation.description}</p>
                    </div>
                  </MotionStaggerItem>
                );
              })}
            </MotionStaggerContainer>
          </div>
        </section>

        {/* Tactical Preparation & Locker Room Standards Showcase */}
        <section className="border-t border-[var(--line)] bg-white px-4 py-16 sm:px-6 lg:px-8 lg:py-20">
          <div className="mx-auto max-w-7xl">
            <MotionFadeIn className="overflow-hidden border border-[rgba(198,165,92,0.4)] bg-[linear-gradient(135deg,#fffdf8_0%,#fbf6ec_100%)] shadow-xl">
              <div className="grid lg:grid-cols-12 items-stretch">
                <div className="relative min-h-[360px] sm:min-h-[440px] lg:col-span-5 overflow-hidden bg-[#120f0d]">
                  <Image
                    src="/foundations/hockey/hockey-locker-room-standards.png"
                    alt="Olympic-level coach Lornette Daye leading tactical strategy session at locker room whiteboard"
                    fill
                    sizes="(max-width: 1024px) 100vw, 42vw"
                    className="object-cover"
                    style={{ objectPosition: "center 20%" }}
                  />
                  <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-black/85 via-black/25 to-transparent opacity-80" />
                  <div className="absolute inset-x-0 bottom-0 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(18,15,13,0.86)] p-4 sm:p-5 backdrop-blur-md shadow-2xl">
                    <p className="text-[10px] font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
                      TACTICAL PREPARATION &amp; CULTURE
                    </p>
                    <p className="mt-1 font-serif text-base text-white sm:text-lg leading-snug">
                      The Playbook for Pressure &amp; Execution
                    </p>
                  </div>
                </div>

                <div className="flex flex-col justify-between p-8 sm:p-10 lg:col-span-7 bg-[linear-gradient(135deg,#fffdf8_0%,#faf5eb_100%)]">
                  <div>
                    <span className="border border-[rgba(198,165,92,0.48)] bg-white/80 px-3 py-1 text-[11px] font-bold uppercase tracking-[0.22em] text-[var(--gold-dark)] shadow-sm inline-block">
                      PRE-GAME · BENCH · POST-SHIFT CADENCE
                    </span>
                    <h3 className="mt-4 font-serif text-2xl sm:text-3xl lg:text-4xl text-[var(--ink)] leading-snug">
                      Where Mental Poise Translates Into Ice Execution
                    </h3>
                    <p className="mt-4 text-base leading-relaxed text-[#554b40]">
                      Championship composure is not an accident that happens during the third period; it is built into the weekly cadence of video analysis, whiteboard strategy, and bench resets.
                    </p>
                    <p className="mt-3 text-base leading-relaxed text-[#554b40]">
                      Lornette’s Foundation Hockey equips players and coaches with shared vocabulary and emotional reset protocols so every shift is approached with focus, trust, and deliberate intent.
                    </p>

                    <div className="mt-6 grid gap-4 sm:grid-cols-2">
                      <div className="border border-[rgba(198,165,92,0.3)] bg-white p-4 shadow-sm">
                        <p className="text-xs font-bold uppercase tracking-[0.18em] text-[var(--gold-dark)]">
                          Video Analytics &amp; Decision Speed
                        </p>
                        <p className="mt-1 text-xs text-[#675d50] leading-relaxed">
                          Translating game review into proactive reads on the ice without hesitation or second-guessing.
                        </p>
                      </div>
                      <div className="border border-[rgba(198,165,92,0.3)] bg-white p-4 shadow-sm">
                        <p className="text-xs font-bold uppercase tracking-[0.18em] text-[var(--gold-dark)]">
                          Locker Room Culture &amp; Standards
                        </p>
                        <p className="mt-1 text-xs text-[#675d50] leading-relaxed">
                          Non-defensive communication standards that protect team chemistry after tough losses or momentum swings.
                        </p>
                      </div>
                    </div>
                  </div>

                  <div className="mt-8 flex flex-wrap items-center gap-4 pt-6 border-t border-[rgba(198,165,92,0.25)]">
                    <CTAButton href="/book">
                      REQUEST A TEAM INTENSIVE
                    </CTAButton>
                    <CTAButton href="#built-for" variant="secondary">
                      VIEW ATHLETE PATHWAYS
                    </CTAButton>
                  </div>
                </div>
              </div>
            </MotionFadeIn>
          </div>
        </section>

        {/* Section 3: Game-Speed Composure (Real Skills. Real Moments. Real Impact.) */}
        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <MotionFadeIn className="text-center max-w-3xl mx-auto">
              <p className="text-xs font-bold uppercase tracking-[0.24em] text-[var(--gold-dark)]">
                GAME-SPEED COMPOSURE
              </p>
              <h2 className="mt-3 font-serif text-3xl sm:text-4xl text-[var(--ink)]">
                Real Skills. Real Moments. Real Impact.
              </h2>
              <p className="mt-4 text-base leading-relaxed text-[#554b40]">
                Directly addressing high-speed transitions, bench composure, and performance under pressure.
              </p>
            </MotionFadeIn>

            <MotionStaggerContainer className="mt-12 grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
              {gameSpeedComposureCards.map((card) => (
                <MotionStaggerItem
                  key={card.title}
                  className="group flex flex-col overflow-hidden border border-[rgba(198,165,92,0.36)] bg-white shadow-[0_16px_50px_rgba(23,20,18,0.06)] transition-all duration-300 hover:-translate-y-1 hover:border-[#dfc385] hover:shadow-[0_24px_60px_rgba(23,20,18,0.14)]"
                >
                  <div className="relative aspect-[16/10] w-full overflow-hidden bg-[#120f0d]">
                    <Image
                      src={card.image}
                      alt={card.title}
                      fill
                      sizes="(max-width: 1024px) 100vw, 33vw"
                      className="object-cover transition-transform duration-700 ease-out group-hover:scale-105"
                      style={{ objectPosition: card.objectPosition }}
                    />
                    <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent opacity-75 group-hover:opacity-60 transition-opacity" />
                    <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/10" />

                    <div className="absolute inset-x-0 bottom-0 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(18,15,13,0.85)] p-4 backdrop-blur-md shadow-2xl">
                      <p className="text-[10px] font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
                        {card.eyebrow}
                      </p>
                      <p className="mt-1 font-serif text-base text-white leading-snug">
                        {card.title}
                      </p>
                    </div>
                  </div>

                  <div className="flex flex-1 flex-col justify-between p-6 bg-[linear-gradient(180deg,#fffdfa_0%,#faf6ee_100%)]">
                    <p className="text-sm leading-relaxed text-[#554b40]">
                      {card.description}
                    </p>
                  </div>
                </MotionStaggerItem>
              ))}
            </MotionStaggerContainer>
          </div>
        </section>

        {/* Section 4: Tactical Leadership and Composure On The Ice Showcase */}
        <section className="border-t border-[var(--line)] bg-[var(--sand)]/25 px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <MotionFadeIn className="text-center max-w-3xl mx-auto">
              <p className="text-xs font-bold uppercase tracking-[0.24em] text-[var(--gold-dark)]">
                CHAMPIONSHIP CULTURE &amp; PRESENCE
              </p>
              <h2 className="mt-3 font-serif text-3xl sm:text-4xl text-[var(--ink)]">
                Tactical Leadership on the Ice
              </h2>
              <p className="mt-4 text-base leading-relaxed text-[#554b40]">
                Watch Olympic-level coach Lornette Daye guide athletes through high-pressure game reads, bench resets, and shared culture standards.
              </p>
            </MotionFadeIn>

            <MotionStaggerContainer className="mt-12 grid gap-8 sm:grid-cols-2 lg:grid-cols-4">
              {tacticalShowcaseCards.map((card) => (
                <MotionStaggerItem
                  key={card.title}
                  className="group flex flex-col overflow-hidden border border-[rgba(198,165,92,0.36)] bg-white shadow-[0_16px_50px_rgba(23,20,18,0.06)] transition-all duration-300 hover:-translate-y-1 hover:border-[#dfc385] hover:shadow-[0_24px_60px_rgba(23,20,18,0.14)]"
                >
                  <div className="relative aspect-[4/3] w-full overflow-hidden bg-[#120f0d]">
                    <Image
                      src={card.image}
                      alt={card.title}
                      fill
                      sizes="(max-width: 1024px) 100vw, 25vw"
                      className="object-cover transition-transform duration-700 ease-out group-hover:scale-105"
                      style={{ objectPosition: card.objectPosition }}
                    />
                    <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent opacity-75 group-hover:opacity-60 transition-opacity" />
                    <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/10" />

                    <div className="absolute inset-x-0 bottom-0 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(18,15,13,0.85)] p-4 backdrop-blur-md shadow-2xl">
                      <p className="text-[10px] font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
                        {card.eyebrow}
                      </p>
                      <p className="mt-1 font-serif text-sm font-semibold text-white leading-snug">
                        {card.title}
                      </p>
                    </div>
                  </div>

                  <div className="flex flex-1 flex-col justify-between p-5 bg-[linear-gradient(180deg,#fffdfa_0%,#faf6ee_100%)]">
                    <p className="text-xs leading-relaxed text-[#554b40]">
                      {card.description}
                    </p>
                  </div>
                </MotionStaggerItem>
              ))}
            </MotionStaggerContainer>
          </div>
        </section>

        {/* Section 5: On-Ice Action & Game-Speed Composure Stock Gallery */}
        <section className="border-t border-[var(--line)] bg-white px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <MotionFadeIn className="text-center max-w-3xl mx-auto">
              <p className="text-xs font-bold uppercase tracking-[0.24em] text-[var(--gold-dark)]">
                HIGH-SPEED EXECUTION
              </p>
              <h2 className="mt-3 font-serif text-3xl sm:text-4xl text-[var(--ink)]">
                On-Ice Action &amp; Game-Speed Scenarios
              </h2>
              <p className="mt-4 text-base leading-relaxed text-[#554b40]">
                Every drill, reset protocol, and communication habit is tested at full speed during competitive momentum swings and physical board battles.
              </p>
            </MotionFadeIn>

            <MotionStaggerContainer className="mt-12 grid gap-8 sm:grid-cols-2 lg:grid-cols-4">
              {onIceActionStockCards.map((card) => (
                <MotionStaggerItem
                  key={card.title}
                  className="group flex flex-col overflow-hidden border border-[rgba(198,165,92,0.36)] bg-white shadow-[0_16px_50px_rgba(23,20,18,0.06)] transition-all duration-300 hover:-translate-y-1 hover:border-[#dfc385] hover:shadow-[0_24px_60px_rgba(23,20,18,0.14)]"
                >
                  <div className="relative aspect-[4/3] w-full overflow-hidden bg-[#120f0d]">
                    <Image
                      src={card.image}
                      alt={card.title}
                      fill
                      sizes="(max-width: 1024px) 100vw, 25vw"
                      className="object-cover transition-transform duration-700 ease-out group-hover:scale-105"
                      style={{ objectPosition: card.objectPosition }}
                    />
                    <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-transparent opacity-75 group-hover:opacity-60 transition-opacity" />
                    <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/10" />

                    <div className="absolute inset-x-0 bottom-0 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(18,15,13,0.85)] p-4 backdrop-blur-md shadow-2xl">
                      <p className="text-[10px] font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
                        {card.eyebrow}
                      </p>
                      <p className="mt-1 font-serif text-sm font-semibold text-white leading-snug">
                        {card.title}
                      </p>
                    </div>
                  </div>

                  <div className="flex flex-1 flex-col justify-between p-5 bg-[linear-gradient(180deg,#fffdfa_0%,#faf6ee_100%)]">
                    <p className="text-xs leading-relaxed text-[#554b40]">
                      {card.description}
                    </p>
                  </div>
                </MotionStaggerItem>
              ))}
            </MotionStaggerContainer>
          </div>
        </section>

        {/* Panoramic Closing CTA */}
        <section className="relative overflow-hidden min-h-[360px] sm:min-h-[420px] border-t border-[rgba(198,165,92,0.4)] flex items-center justify-center text-center px-4 py-16">
          <div className="absolute inset-0 pointer-events-none overflow-hidden">
            <Image
              src="/foundations/banners/cinematic-hockey-rink.jpg"
              alt="Championship hockey arena ice rink under gleaming golden stadium lights"
              role="presentation"
              fill
              quality={95}
              sizes="100vw"
              className="object-cover object-center"
            />
            <div className="absolute inset-0 bg-gradient-to-t from-black/75 via-black/40 to-black/65" />
          </div>
          <MotionFadeIn className="relative z-10 max-w-3xl mx-auto text-white">
            <p className="text-xs font-bold uppercase tracking-[0.24em] text-[var(--champagne)]">
              LORNETTE’S FOUNDATION HOCKEY
            </p>
            <h2 className="mt-3 font-serif text-3xl sm:text-5xl text-white">
              Take the Next Step.
            </h2>
            <p className="mt-4 text-base sm:text-lg text-white/85">
              Build a stronger mind, a stronger team and a higher standard for what&apos;s possible.
            </p>
            <div className="mt-8 flex flex-wrap justify-center gap-4">
              <MotionShimmerButton href="#built-for">EXPLORE HOCKEY PROGRAM</MotionShimmerButton>
              <CTAButton href="/book" variant="secondary">
                FOR TEAMS &amp; ACADEMIES
              </CTAButton>
            </div>
          </MotionFadeIn>
        </section>
      </main>
      <FoundationsFloatingAction track="hockey" />
    </PageShell>
  );
}
