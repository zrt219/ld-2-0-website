import Image from "next/image";
import { GraduationCap, Users, Trophy, BarChart3, FileCheck, CheckCircle2, Award, Globe, Sparkles } from "lucide-react";

import { CTAButton } from "@/components/CTAButton";
import { PageShell } from "@/components/PageShell";
import { EuropeanBannerSlideshow } from "@/components/foundations/EuropeanBannerSlideshow";
import { EuropeanExecutiveVisual } from "@/components/foundations/EuropeanExecutiveVisual";
import { FoundationsAccessibilityDock } from "@/components/foundations/FoundationsAccessibilityDock";
import { FoundationsFloatingAction } from "@/components/foundations/FoundationsFloatingAction";
import { FoundationsSubNav } from "@/components/foundations/FoundationsSubNav";
import { RobustImage } from "@/components/ui/RobustImage";
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
  "Lornette’s Foundations Europe | European Sport Excellence & Partnerships",
  "A partnership pathway for international sport clubs, regional federations, and European sport ecosystems seeking practical mental performance, leadership, and athlete development programming.",
  "/foundations/europe",
);

const europeSignatureStandouts = [
  {
    title: "High Performance",
    label: "Athlete Development Systems",
    detail: "Whole-athlete development models refined across 40+ years of elite international sport.",
    icon: Trophy,
  },
  {
    title: "Sport Culture",
    label: "Championship Mindset and Habits",
    detail: "Mental discipline, character, and emotional poise embedded into club and team identity.",
    icon: Sparkles,
  },
  {
    title: "Leadership",
    label: "Olympic-Standard Coach Guidance",
    detail: "Strategic mentorship for sports directors, coaches, and athletic leaders.",
    icon: Award,
  },
  {
    title: "Global Exchange",
    label: "International Sport Insights",
    detail: "Transatlantic best practices bridging North American and European sport systems.",
    icon: Globe,
  },
  {
    title: "Partnerships",
    label: "Collaborative Program Design",
    detail: "Custom initiatives designed alongside European sport clubs, academies, and federations.",
    icon: Users,
  },
];

const collaborationTiers = [
  {
    title: "Applied Performance Science & Biomechanics",
    image: "/foundations/europe/europe-biomechanics-lab.jpg",
    objectPosition: "center 30%",
    description:
      "High-precision motion capture analysis, instrumented sensor track testing, and physiological feedback protocols tailored for European youth and elite academies.",
    tag: "Biomechanics & Testing",
    highlights: [
      "Motion Capture & Sensor Track Telemetry",
      "Neuromuscular Composure Protocols",
      "Youth & Elite Performance Baselines",
    ],
  },
  {
    title: "Sports Technology & Innovation Networks",
    image: "/foundations/europe/europe-innovation-expo.jpg",
    objectPosition: "center 25%",
    description:
      "Collaborative exploration of sports engineering, equipment innovation, digital performance tracking, and pan-European athletic technology partnerships.",
    tag: "Innovation Networks",
    highlights: [
      "Advanced Sports Equipment & Engineering",
      "Pan-European Technology Partnerships",
      "Digital Biometrics & Longitudinal Tracking",
    ],
  },
  {
    title: "Strategic Delegations & Club Alignment",
    image: "/foundations/europe/europe-strategic-delegations.jpg",
    objectPosition: "center 30%",
    description:
      "Morning bilateral briefings and strategic planning sessions structured for sports directors, federation officials, and academy leaders across Europe.",
    tag: "Club Partnerships",
    highlights: [
      "Bilateral Federation Consultations",
      "Academy Leadership & Club Culture",
      "Sustainable Athlete Retention Pathways",
    ],
  },
];



const partnershipAreas = [
  {
    title: "Sport Education",
    icon: GraduationCap,
    description:
      "Integrating practical performance, leadership, and well-being into athletic academy and sports school programs.",
  },
  {
    title: "Coach Development",
    icon: Users,
    description:
      "Equipping coaches with modern tools, somatic frameworks, and repeatable communication strategies for high-stakes competition.",
  },
  {
    title: "Athlete Leadership",
    icon: Trophy,
    description:
      "Developing confident, resilient, and purpose-driven competitors who lead by example on and off the field.",
  },
  {
    title: "Applied Research",
    icon: BarChart3,
    description:
      "Supporting real-world applications of performance science, leadership habits, and longitudinal athlete development metrics.",
  },
  {
    title: "Pilot Programs",
    icon: FileCheck,
    description:
      "Designing and testing practical athlete development modules for clubs, regional hubs, and collaborative athletic networks.",
  },
];

export default function FoundationsEuropePage() {
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
                    LORNETTE’S FOUNDATIONS | EUROPEAN PARTNERSHIPS
                  </span>
                </div>

                <h1 className="mt-6 font-serif text-4xl leading-[1.02] text-balance text-[var(--ink)] sm:text-6xl lg:text-[4rem]">
                  Sport Education for European Partners.
                </h1>

                <p className="mt-5 font-serif text-2xl text-[var(--gold-dark)] sm:text-3xl">
                  Innovation Networks &amp; Regional Sport Ecosystems
                </p>

                <p className="mt-6 text-base leading-8 text-[#554b40] sm:text-lg">
                  A partnership pathway for European sport partners seeking practical athlete development, leadership, and mental performance programming.
                </p>

                <div className="mt-8 flex flex-col gap-3 sm:flex-row">
                  <MotionShimmerButton href="/book">Start a Partnership Conversation</MotionShimmerButton>
                  <CTAButton href="/foundations" variant="secondary">
                    View Foundations Framework
                  </CTAButton>
                </div>
              </MotionFadeIn>

              <MotionScaleIn className="relative lg:col-span-5" delay={0.15}>
                <div className="relative w-full aspect-[4/5] overflow-hidden border border-[rgba(198,165,92,0.42)] bg-[linear-gradient(180deg,#fffdf8_0%,#f5efe4_100%)] shadow-[0_28px_110px_rgba(23,20,18,0.14)]">
                  <RobustImage
                    src="/foundations/europe/lornette-europe-conference-hero.jpg"
                    fallbackSrcs={[
                      "/foundations/pathways/europe/lornette-europe-summit-hero.jpg",
                      "/foundations/pathways/europe-pathway.jpg",
                      "/foundations/select-stock/europe.jpg",
                    ]}
                    alt="Olympic-level coach Lornette Daye presenting to European sports directors and academy delegates"
                    fill
                    priority
                    sizes="(max-width: 1024px) 100vw, 42vw"
                    className="object-cover"
                    style={{ objectPosition: "center top" }}
                  />
                  <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/40" />
                  <div className="absolute inset-x-0 bottom-0 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(18,15,13,0.85)] p-4 sm:p-5 backdrop-blur-md shadow-2xl">
                    <p className="text-[11px] font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
                      PEOPLE · KNOWLEDGE · PERFORMANCE
                    </p>
                    <p className="mt-1 font-serif text-base text-white sm:text-lg leading-snug">
                      Building stronger athletes, coaches and sport systems.
                    </p>
                  </div>
                </div>
              </MotionScaleIn>
            </div>
          </div>
        </section>

        {/* Signature Standouts Strip */}
        <section
          aria-label="Europe signature standouts"
          className="border-b border-[var(--line)] bg-white px-4 py-10 sm:px-6 lg:px-8"
        >
          <div className="mx-auto max-w-7xl">
            <MotionStaggerContainer className="grid gap-6 sm:grid-cols-2 lg:grid-cols-5 divide-y divide-[rgba(198,165,92,0.3)] sm:divide-y-0">
              {europeSignatureStandouts.map((item, idx) => {
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

        {/* Section 1: Designed for European Sport Ecosystems, Innovation Networks & Regional Partners */}
        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <MotionFadeIn className="text-center max-w-3xl mx-auto">
              <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--gold-dark)]">
                COLLABORATION PATHWAYS
              </p>
              <h2 className="mt-3 font-serif text-3xl sm:text-4xl text-[var(--ink)]">
                Designed for Sport Ecosystems, Innovation Networks &amp; Regional Partners
              </h2>
              <p className="mt-4 text-base leading-relaxed text-[#675d50]">
                Tailored collaboration opportunities for European sport partners seeking practical, real-world development in athlete performance, coaching, and leadership.
              </p>
            </MotionFadeIn>

            <MotionStaggerContainer className="mt-12 grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
              {collaborationTiers.map((tier) => (
                <MotionStaggerItem
                  key={tier.title}
                  className="group flex flex-col overflow-hidden border border-[rgba(198,165,92,0.36)] bg-white shadow-[0_16px_50px_rgba(23,20,18,0.06)] transition-all duration-300 hover:-translate-y-1 hover:border-[#dfc385] hover:shadow-[0_24px_60px_rgba(23,20,18,0.14)]"
                >
                  <div className="relative aspect-[4/5] w-full overflow-hidden bg-[#120f0d]">
                    <RobustImage
                      src={tier.image}
                      fallbackSrcs={[
                        "/foundations/pathways/europe/lornette-europe-summit-hero.jpg",
                        "/foundations/pathways/europe-pathway.jpg",
                        "/foundations/select-stock/europe.jpg",
                      ]}
                      alt={tier.title}
                      fill
                      sizes="(max-width: 1024px) 100vw, 33vw"
                      className="object-cover transition-transform duration-700 ease-out group-hover:scale-105"
                      style={{ objectPosition: tier.objectPosition }}
                    />
                    <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-black/85 via-black/25 to-transparent opacity-80 group-hover:opacity-70 transition-opacity" />
                    <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/10" />

                    <div className="absolute inset-x-0 bottom-0 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(18,15,13,0.86)] p-4 backdrop-blur-md shadow-2xl">
                      <p className="text-[10px] font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
                        {tier.tag}
                      </p>
                      <p className="mt-1 font-serif text-base text-white leading-snug">
                        {tier.title}
                      </p>
                    </div>
                  </div>

                  <div className="flex flex-1 flex-col justify-between p-6 bg-[linear-gradient(180deg,#fffdfa_0%,#faf6ee_100%)]">
                    <div>
                      <p className="text-sm leading-relaxed text-[#554b40]">
                        {tier.description}
                      </p>
                    </div>

                    <div className="mt-5 border-t border-[rgba(198,165,92,0.22)] pt-4">
                      <p className="text-[10px] font-bold uppercase tracking-[0.2em] text-[#7d7164] mb-2.5">
                        Pillar Deliverables
                      </p>
                      <ul className="space-y-1.5">
                        {tier.highlights.map((item) => (
                          <li key={item} className="flex items-start gap-2 text-xs text-[#5e5346]">
                            <CheckCircle2 size={13} className="text-[var(--gold-dark)] shrink-0 mt-0.5" />
                            <span>{item}</span>
                          </li>
                        ))}
                      </ul>
                    </div>
                  </div>
                </MotionStaggerItem>
              ))}
            </MotionStaggerContainer>
          </div>
        </section>

        {/* Section 2: Partnership Areas (5 Icon Cards) */}
        <section className="border-t border-[var(--line)] bg-[var(--sand)]/30 px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <MotionFadeIn className="text-center max-w-3xl mx-auto">
              <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--gold-dark)]">
                AREAS OF FOCUS
              </p>
              <h2 className="mt-3 font-serif text-3xl sm:text-4xl text-[var(--ink)]">
                Partnership Areas
              </h2>
              <p className="mt-4 text-base text-[#675d50]">
                Focused areas for collaboration, designed to create meaningful and practical impact across European sport ecosystems.
              </p>
            </MotionFadeIn>

            <MotionStaggerContainer className="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-5">
              {partnershipAreas.map((area) => {
                const Icon = area.icon;
                return (
                  <MotionStaggerItem
                    key={area.title}
                    className="border border-[rgba(198,165,92,0.34)] bg-white p-6 shadow-sm transition-all duration-300 hover:-translate-y-1 hover:border-[var(--champagne)] flex flex-col justify-between"
                  >
                    <div>
                      <div className="h-12 w-12 rounded-full border border-[rgba(198,165,92,0.4)] bg-[var(--sand)]/40 flex items-center justify-center text-[var(--gold-dark)] mb-4">
                        <Icon size={22} />
                      </div>
                      <h3 className="font-serif text-lg font-bold text-[var(--ink)]">{area.title}</h3>
                      <div className="mt-2.5 h-0.5 w-7 bg-[var(--champagne)]" aria-hidden="true" />
                      <p className="mt-3 text-xs leading-relaxed text-[#675d50]">{area.description}</p>
                    </div>
                  </MotionStaggerItem>
                );
              })}
            </MotionStaggerContainer>
          </div>
        </section>

        {/* Featured Transatlantic Leadership Showcase */}
        <section className="border-t border-[var(--line)] bg-white px-4 py-16 sm:px-6 lg:px-8 lg:py-20">
          <div className="mx-auto max-w-7xl">
            <MotionFadeIn className="overflow-hidden border border-[rgba(198,165,92,0.4)] bg-[linear-gradient(135deg,#fffdf8_0%,#fbf6ec_100%)] shadow-xl">
              <div className="grid lg:grid-cols-12 items-stretch">
                <EuropeanExecutiveVisual />

                <div className="flex flex-col justify-between p-8 sm:p-10 lg:col-span-7">
                  <div>
                    <span className="border border-[rgba(198,165,92,0.48)] bg-white/80 px-3 py-1 text-[11px] font-bold uppercase tracking-[0.22em] text-[var(--gold-dark)] shadow-sm inline-block">
                      EXECUTIVE COACHING &amp; ADVISORY
                    </span>
                    <h3 className="mt-4 font-serif text-2xl sm:text-3xl lg:text-4xl text-[var(--ink)] leading-snug">
                      Bridging High-Performance Principles Across Borders
                    </h3>
                    <p className="mt-4 text-base leading-relaxed text-[#554b40]">
                      Lornette Daye brings four decades of elite international championship experience to European sports directors, academy leaders, and performance scientists.
                    </p>
                    <p className="mt-3 text-base leading-relaxed text-[#554b40]">
                      Through targeted seminars, coach development frameworks, and executive consultations, Lornette helps organizations instill emotional poise, mental resilience, and sustainable competitive standards across youth and professional divisions.
                    </p>

                    <div className="mt-6 grid gap-4 sm:grid-cols-2">
                      <div className="border border-[rgba(198,165,92,0.3)] bg-white p-4 shadow-sm">
                        <p className="text-xs font-bold uppercase tracking-[0.18em] text-[var(--gold-dark)]">
                          Coach Development
                        </p>
                        <p className="mt-1 text-xs text-[#675d50] leading-relaxed">
                          Somatic composure protocols and non-defensive communication for high-stakes competition.
                        </p>
                      </div>
                      <div className="border border-[rgba(198,165,92,0.3)] bg-white p-4 shadow-sm">
                        <p className="text-xs font-bold uppercase tracking-[0.18em] text-[var(--gold-dark)]">
                          Academy Leadership
                        </p>
                        <p className="mt-1 text-xs text-[#675d50] leading-relaxed">
                          Structured character habits, academic balance, and identity foundations beyond sport.
                        </p>
                      </div>
                    </div>
                  </div>

                  <div className="mt-8 flex flex-wrap items-center gap-4 pt-6 border-t border-[rgba(198,165,92,0.25)]">
                    <CTAButton href="/book">
                      SCHEDULE A TRANSATLANTIC DIALOGUE
                    </CTAButton>
                    <CTAButton href="/foundations" variant="secondary">
                      EXPLORE FOUNDATIONS
                    </CTAButton>
                  </div>
                </div>
              </div>
            </MotionFadeIn>
          </div>
        </section>



        {/* Panoramic Ecosystem Closing Slideshow */}
        <EuropeanBannerSlideshow />
      </main>
      <FoundationsAccessibilityDock />
      <FoundationsFloatingAction track="europe" />
    </PageShell>
  );
}
