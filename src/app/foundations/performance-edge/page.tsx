import Image from "next/image";
import { BadgeCheck } from "lucide-react";

import { CTAButton } from "@/components/CTAButton";
import { PageShell } from "@/components/PageShell";
import { FoundationsSubNav } from "@/components/foundations/FoundationsSubNav";
import { createMetadata } from "@/content/site";

export const metadata = createMetadata(
  "The Performance Edge Framework | Athlete Methodology",
  "The practical performance methodology inside Lornette’s Foundation, equipping athletes with repeatable tools for focus, routine, pressure, and mistake recovery.",
  "/foundations/performance-edge",
);

const pillars = [
  {
    number: "01",
    title: "Focus",
    subtitle: "The Attention Game",
    summary:
      "Learning to control what enters your awareness. In competition, attention is constantly under siege from crowd noise, past errors, future leaderboards, and internal doubt. The framework teaches athletes to establish an attention dial: expanding awareness during downtime and narrowing exclusively to the immediate task upon execution.",
  },
  {
    number: "02",
    title: "Pre-Shot & Execution Routine",
    subtitle: "The Predictable Anchor",
    summary:
      "When external conditions are unpredictable, the routine remains invariant. Athletes build a sequenced, non-negotiable cadence: Assess the environment, Decide on the objective, Visualize the outcome, Reset internal tension, Execute with freedom, and Release the outcome. This turns high-pressure moments into familiar physical sequences.",
  },
  {
    number: "03",
    title: "Pressure Management",
    subtitle: "Notice → Breathe → Target → Commit",
    summary:
      "Pressure triggers natural biological reactions: elevated heart rate, shallower breathing, and accelerated internal pacing. Instead of denying anxiety, the framework gives athletes an actionable 4-step sequence to regulate physiology, anchor visually to the target, and commit 100% to the execution.",
  },
  {
    number: "04",
    title: "Sensory Visualization",
    subtitle: "See It Before You Do It",
    summary:
      "Elite performance is neurological rehearsal. Athletes train sensory visualization through deliberate mental rehearsal, creating vivid sensory simulation incorporating trajectory, physical tension, tactile feel, and environmental conditions before stepping into action.",
  },
  {
    number: "05",
    title: "Mistake Recovery & Reset",
    subtitle: "The Five Seconds After a Mistake",
    summary:
      "Every athlete encounters bad bounces, referee calls, and technical breakdowns. The signature Next Shot Principle dictates: 'Your previous shot cannot hit your next shot.' Athletes master a rapid 5-step reset protocol to process errors, extract information, and recommit within five seconds.",
  },
  {
    number: "06",
    title: "Decisive Decision-Making",
    subtitle: "The Decision Before the Move",
    summary:
      "Hesitation breeds technical failure. Under pressure, athletes must calculate realistic risk-reward percentages, choose the high-probability path, and commit fully without internal second-guessing once execution begins.",
  },
  {
    number: "07",
    title: "Competition Preparation",
    subtitle: "The Competition Day Plan",
    summary:
      "Championship execution is organized hours before the start. The framework structures the entire competition arrival: sleep protocols, nutritional pacing, progressive physical warm-ups, and mental centering so athletes arrive at the start line ready.",
  },
  {
    number: "08",
    title: "Evidence-Based Confidence",
    subtitle: "Confidence From What You Have Built",
    summary:
      "Confidence manufactured from hype vanishes under true pressure. Genuine confidence is built on evidence: logged routines completed, resilient decisions made, pressure situations navigated, and deliberate preparation fulfilled.",
  },
];

const boundaryGuarantees = [
  {
    title: "Complements Technical Coaching",
    description:
      "Performance Edge does not modify swing mechanics, sprint stride lengths, or tactical plays. It trains the mental operating system that executes those mechanics under tournament conditions.",
  },
  {
    title: "Does Not Replace Sport Coaches",
    description:
      "We partner directly with PGA professionals, head track coaches, and athletic staff, reinforcing their technical guidance with mental discipline.",
  },
  {
    title: "Non-Clinical Athletic Specialty",
    description:
      "Lornette Daye does not present herself as a clinical psychologist or therapist. Her authority is rooted in four decades of elite sport, Canadian national championships, and international coaching.",
  },
  {
    title: "Extensible Across Sport Pathways",
    description:
      "While Golf represents our flagship sport pathway, the core Performance Edge framework applies across disciplines where individual composure and decision-making dictate outcomes.",
  },
];

export default function FoundationsPerformanceEdgePage() {
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
                    Athlete Methodology
                  </span>
                </div>

                <h1 className="mt-6 font-serif text-4xl leading-[1.02] text-balance text-[var(--ink)] sm:text-6xl lg:text-[4.2rem]">
                  The Performance Edge Framework
                </h1>

                <p className="mt-5 font-serif text-2xl text-[var(--gold-dark)] sm:text-3xl">
                  The practical performance methodology inside Lornette’s Foundation.
                </p>

                <p className="mt-6 text-base leading-8 text-[#554b40] sm:text-lg">
                  Performance Edge translates forty years of elite athletic competition and national coaching into actionable, repeatable mental game tools. It gives athletes the psychological infrastructure to manage tension, maintain focus, and execute when the stakes are highest.
                </p>

                <div className="mt-8 flex flex-col gap-3 sm:flex-row">
                  <CTAButton href="/foundations/golf">EXPLORE GOLF</CTAButton>
                  <CTAButton href="/foundations/clubs" variant="secondary">
                    BRING THE FOUNDATION TO YOUR ORGANIZATION
                  </CTAButton>
                </div>
              </div>

              <div className="relative lg:col-span-5">
                <div className="relative w-full aspect-[4/5] overflow-hidden border border-[rgba(198,165,92,0.42)] bg-[linear-gradient(180deg,#fffdf8_0%,#f5efe4_100%)] shadow-[0_28px_110px_rgba(23,20,18,0.14)]">
                  <Image
                    src="/foundations/lornette-foundations-armchair-study.png"
                    alt="Lornette Daye seated in modern armchair in executive study with architectural gold circles"
                    fill
                    priority
                    sizes="(max-width: 1024px) 100vw, 42vw"
                    className="object-cover"
                    style={{ objectPosition: "28% 18%" }}
                  />
                  <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/40" />
                  <div className="absolute inset-x-0 bottom-0 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(18,15,13,0.82)] p-4 sm:p-5 backdrop-blur-md shadow-2xl">
                    <p className="text-[11px] font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
                      The Methodology
                    </p>
                    <p className="mt-1 font-serif text-base text-white sm:text-lg">
                      Practical Performance Tools
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* The Performance Tools Detailed */}
        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <div className="grid gap-10 lg:grid-cols-[0.45fr_0.55fr] lg:items-end">
              <div>
                <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--gold-dark)]">
                  The Performance Tools
                </p>
                <h2 className="mt-4 font-serif text-4xl leading-tight text-[var(--ink)] sm:text-5xl">
                  Eight Tools for Repeatable Execution
                </h2>
              </div>
              <p className="text-base leading-8 text-[#675d50]">
                Each tool is designed to be taught quickly, practiced deliberately in training, and deployed reflexively under tournament pressure across the 10 Foundations.
              </p>
            </div>

            <div className="mt-14 grid gap-6 md:grid-cols-2">
              {pillars.map((pillar) => (
                <article
                  key={pillar.title}
                  className="border border-[rgba(198,165,92,0.34)] bg-white p-8 shadow-[0_16px_50px_rgba(23,20,18,0.05)] transition duration-200 hover:border-[var(--champagne)]"
                >
                  <div className="flex items-center justify-between border-b border-[var(--line)] pb-4">
                    <div>
                      <span className="font-serif text-sm font-bold text-[var(--gold-dark)]">
                        Tool {pillar.number}
                      </span>
                      <h3 className="mt-1 font-serif text-2xl text-[var(--ink)]">
                        {pillar.title}
                      </h3>
                    </div>
                    <span className="rounded bg-[var(--ivory)] px-3 py-1 text-xs font-bold uppercase tracking-[0.14em] text-[var(--gold-dark)] border border-[rgba(198,165,92,0.3)]">
                      {pillar.subtitle}
                    </span>
                  </div>

                  <p className="mt-5 text-sm leading-7 text-[#675d50]">
                    {pillar.summary}
                  </p>
                </article>
              ))}
            </div>

            {/* Editorial Feature: Codified Field Playbooks */}
            <div className="mt-14 overflow-hidden border border-[rgba(198,165,92,0.36)] bg-white shadow-[0_16px_50px_rgba(23,20,18,0.06)] grid lg:grid-cols-12">
              <div className="p-8 lg:p-12 lg:col-span-6 flex flex-col justify-center bg-[linear-gradient(135deg,#fffdf8_0%,#faf6ee_100%)] order-2 lg:order-1">
                <span className="text-xs font-bold uppercase tracking-[0.22em] text-[var(--gold-dark)]">
                  Actionable Infrastructure
                </span>
                <h3 className="mt-2 font-serif text-3xl text-[var(--ink)]">
                  Codified Playbooks for High-Stakes Moments
                </h3>
                <p className="mt-4 text-base leading-relaxed text-[#5e5346]">
                  A mental conditioning framework is only as valuable as its durability under tournament pressure. Every athlete and team working with Performance Edge builds a tangible, codified Performance Plan, a personal operating system specifying exact pre-shot routines, emotional reset triggers, and visualization cadences.
                </p>
                <div className="mt-6">
                  <CTAButton href="/foundations/golf">
                    EXPLORE GOLF IMPLEMENTATION
                  </CTAButton>
                </div>
              </div>
              <div className="relative aspect-[16/9] lg:aspect-auto lg:col-span-6 min-h-[320px] order-1 lg:order-2">
                <Image
                  src="/foundations/lornette-foundations-curved-track-athletes.png"
                  alt="Lornette Daye in white tailored suit standing before curved running track lanes with athletes training in a modern sports facility"
                  fill
                  sizes="(max-width: 1024px) 100vw, 50vw"
                  className="object-cover"
                  style={{ objectPosition: "25% 18%" }}
                />
                <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/20" />
              </div>
            </div>
          </div>
        </section>

        {/* Professional Scope & Boundary Guarantees */}
        <section className="border-y border-[var(--line)] bg-[var(--sand)]/40 px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <div className="text-center max-w-3xl mx-auto">
              <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--gold-dark)]">
                Professional Boundaries
              </p>
              <h2 className="mt-4 font-serif text-4xl leading-tight text-[var(--ink)] sm:text-5xl">
                How Performance Edge Works With Your Team
              </h2>
              <p className="mt-4 text-base leading-8 text-[#675d50]">
                We protect clarity and trust by defining exactly where our framework operates.
              </p>
            </div>

            <div className="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
              {boundaryGuarantees.map((item) => (
                <div
                  key={item.title}
                  className="border border-[rgba(198,165,92,0.38)] bg-white p-7 shadow-[0_16px_45px_rgba(23,20,18,0.05)] flex flex-col justify-between"
                >
                  <div>
                    <BadgeCheck size={24} aria-hidden="true" className="text-[var(--gold-dark)]" />
                    <h3 className="mt-4 font-serif text-xl text-[var(--ink)]">
                      {item.title}
                    </h3>
                    <p className="mt-3 text-sm leading-6 text-[#675d50]">
                      {item.description}
                    </p>
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
              src="/foundations/banners/scenic-alpine-training.jpg"
              alt="High-altitude mountain ridgeline athletic training trail at golden hour"
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
              Put The Framework To Work
            </p>
            <h2 className="mt-4 font-serif text-4xl leading-tight text-white sm:text-5xl lg:text-6xl">
              Turn Mental Preparation Into Competitive Advantage
            </h2>
            <p className="mt-6 max-w-2xl mx-auto text-lg leading-8 text-[#d8cdbb]">
              Explore the Golf Performance Program or bring the Performance Edge framework to your athletic academy, federation, or collegiate squad.
            </p>
            <div className="mt-9 flex flex-col justify-center gap-4 sm:flex-row">
              <CTAButton href="/foundations/golf">EXPLORE GOLF PROGRAM</CTAButton>
              <CTAButton
                href="/foundations/clubs"
                variant="secondary"
                className="border-white/30 text-white hover:bg-white/10"
              >
                FOR CLUBS &amp; ORGANIZATIONS
              </CTAButton>
            </div>
          </div>
        </section>
      </main>
    </PageShell>
  );
}
