import Image from "next/image";
import Link from "next/link";
import { ArrowRight, Clock, MapPin, Target, Users } from "lucide-react";
import { CTAButton } from "@/components/CTAButton";
import { FoundationsSubNav } from "@/components/foundations/FoundationsSubNav";
import { PageShell } from "@/components/PageShell";
import { SectionHeader } from "@/components/SectionHeader";
import { createMetadata } from "@/content/site";

export const metadata = createMetadata(
  "The Performance Edge Workshop & Member Clinic | Golf Mental Conditioning",
  "Hands-on mental performance workshop and member clinic for golf clubs, combining whiteboard instruction with live pre-shot routine and pressure drills.",
  "/foundations/golf/workshop",
);

const clinicModules = [
  {
    title: "1. The Attention & Focus Protocol",
    setting: "Clubhouse / Meeting Room (35 mins)",
    description:
      "Interactive whiteboard breakdown of attentional narrowing, target selection, and internal dialogue management. Golfers learn to distinguish between process cues and outcome dread.",
  },
  {
    title: "2. The 6-Step Pre-Shot Routine Engineering",
    setting: "Practice Range / Simulator (35 mins)",
    description:
      "Active construction and timing of each golfer's personal routine sequence: Assess → Decide → Visualize → Reset → Execute → Release. Timing standardized between 12–18 seconds.",
  },
  {
    title: "3. The Pressure 5 Field Drill",
    setting: "Putting Green / Chipping Complex (30 mins)",
    description:
      "Live simulated pressure stakes where failure incurs immediate consequence resets. Golfers practice down-regulation breathing and committed execution when hands feel cold or tight.",
  },
  {
    title: "4. The 5-Second Post-Mistake Reset Protocol",
    setting: "Practice Tee / Green (20 mins)",
    description:
      "A structured three-step somatic release (physical trigger, breath exhalation, club reset) to prevent one bad swing or lip-out from bleeding into subsequent holes.",
  },
];

const formats = [
  {
    title: "2-Hour Member Intensive",
    description: "Ideal for club evenings, twilight clinic series, or tournament prep sessions.",
  },
  {
    title: "Extended / Custom Club Clinic (3+ Hours)",
    description: "Includes on-course simulated play for 3 holes with live routine auditing.",
  },
  {
    title: "Junior Academy Mental Training Camp",
    description: "Focused on elite junior competitors preparing for provincial/state qualifiers.",
  },
];

export default function GolfWorkshopPage() {
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
                    Hands-on Clinic
                  </span>
                </div>

                <h1 className="mt-6 font-serif text-4xl leading-[1.04] text-balance text-[var(--ink)] sm:text-6xl">
                  The Performance Edge Workshop &amp; Member Clinic
                </h1>

                <p className="mt-4 text-sm font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)]">
                  Powered by the Performance Edge Framework
                </p>

                <p className="mt-6 text-base leading-8 text-[#554b40] sm:text-lg">
                  Mental toughness is not an abstract concept; it is a trainable physical discipline. This hands-on clinic bridges the gap between indoor classroom instruction and live execution on the practice green and tee line.
                </p>

                <div className="mt-8 flex flex-wrap gap-4 text-xs font-semibold text-[#6e6355]">
                  <div className="flex items-center gap-2 border border-[rgba(198,165,92,0.4)] bg-white/60 px-3 py-1.5">
                    <Clock size={14} className="text-[var(--gold-dark)]" />
                    <span>Duration: Approx. 2 Hours (90-Min &amp; Custom Available)</span>
                  </div>
                  <div className="flex items-center gap-2 border border-[rgba(198,165,92,0.4)] bg-white/60 px-3 py-1.5">
                    <Users size={14} className="text-[var(--gold-dark)]" />
                    <span>Group Size: 12–24 Members (Intimate Cohort)</span>
                  </div>
                  <div className="flex items-center gap-2 border border-[rgba(198,165,92,0.4)] bg-white/60 px-3 py-1.5">
                    <MapPin size={14} className="text-[var(--gold-dark)]" />
                    <span>Setting: Clubhouse + Short Game / Practice Range</span>
                  </div>
                </div>

                <div className="mt-10 flex flex-col gap-3 sm:flex-row">
                  <CTAButton href="/book">Host a Member Clinic at Your Club</CTAButton>
                  <CTAButton href="/foundations/golf/club-partnership" variant="secondary">
                    Explore Full Club Partnerships
                  </CTAButton>
                </div>
              </div>

              <div className="relative lg:col-span-5">
                <div className="relative w-full aspect-[4/5] overflow-hidden border border-[rgba(198,165,92,0.42)] bg-[linear-gradient(180deg,#fffdf8_0%,#f5efe4_100%)] shadow-[0_28px_110px_rgba(23,20,18,0.14)]">
                  <Image
                    src="/foundations/golf/lornette-golf-indoor-studio.png"
                    alt="Lornette Daye in a modern indoor golf studio coaching players with putting green and telemetry screens"
                    fill
                    priority
                    sizes="(max-width: 1024px) 92vw, 40vw"
                    className="object-cover"
                    style={{ objectPosition: "15% 18%" }}
                  />
                  <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/40" />
                  <div className="absolute inset-x-0 bottom-0 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(18,15,13,0.82)] p-4 sm:p-5 backdrop-blur-md shadow-2xl">
                    <p className="text-[11px] font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
                      Member Clinic &amp; Workshop
                    </p>
                    <p className="mt-1 font-serif text-base text-white sm:text-lg">
                      From Strategy to Swing Execution
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Clinic Curriculum Modules */}
        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <SectionHeader
              eyebrow="Clinic Flow"
              title="Classroom Strategy to Practice Green Execution"
              body="Every participant leaves with a personalized routine checklist, somatic breathing protocol, and self-auditing tracking sheets."
            />

            <div className="mt-12 grid gap-6 sm:grid-cols-2">
              {clinicModules.map((mod) => (
                <div
                  key={mod.title}
                  className="border border-[rgba(198,165,92,0.34)] bg-white p-8 shadow-[0_16px_40px_rgba(23,20,18,0.04)] flex flex-col justify-between"
                >
                  <div>
                    <span className="text-xs font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)]">
                      {mod.setting}
                    </span>
                    <h2 className="mt-3 font-serif text-2xl text-[var(--ink)]">{mod.title}</h2>
                    <p className="mt-3 text-sm leading-7 text-[#675d50]">{mod.description}</p>
                  </div>
                </div>
              ))}
            </div>

            {/* Editorial Showcase: Live Turf Execution & Champion Posture */}
            <div className="mt-14 overflow-hidden border border-[rgba(198,165,92,0.36)] bg-white shadow-[0_16px_50px_rgba(23,20,18,0.06)] grid grid-cols-1 lg:grid-cols-12">
              <div className="relative w-full aspect-[16/9] lg:aspect-auto lg:col-span-6 lg:min-h-[340px]">
                <Image
                  src="/foundations/golf/lornette-golf-fairway-composure-sunset.jpg"
                  alt="Lornette Daye in white tailored suit standing alongside a custom golf bag on an immaculate fairway with lakeside view in warm sunset light"
                  fill
                  sizes="(max-width: 1024px) 100vw, 50vw"
                  className="object-cover"
                  style={{ objectPosition: "78% 22%" }}
                />
                <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/20" />
              </div>
              <div className="min-w-0 p-8 lg:p-12 lg:col-span-6 flex flex-col justify-center bg-[linear-gradient(135deg,#fffdf8_0%,#faf6ee_100%)]">
                <span className="text-xs font-bold uppercase tracking-[0.22em] text-[var(--gold-dark)]">
                  Live Drills in Action · Turf Execution
                </span>
                <h3 className="mt-2 font-serif text-3xl text-[var(--ink)]">
                  Commanding Presence on the Fairway
                </h3>
                <p className="mt-4 text-base leading-relaxed text-[#5e5346]">
                  On the range and practice greens, players take the theory directly to the turf. Through repetitive cadence drills and somatic breathing resets, routine becomes an automatic physical defense against nervous tension, cultivating unshakeable composure from the first tee to the 18th green.
                </p>
                <div className="mt-6 flex flex-wrap gap-3">
                  <CTAButton href="/book">
                    RESERVE A CLINIC DATE
                  </CTAButton>
                  <CTAButton href="/foundations/golf/program" variant="secondary">
                    EXPLORE 10-WEEK PROGRAM
                  </CTAButton>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Format Options */}
        <section className="border-t border-[var(--line)] bg-[#f6f2e8] px-4 py-16 sm:px-6 lg:px-8 lg:py-20">
          <div className="mx-auto max-w-7xl">
            <div className="max-w-3xl">
              <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--gold-dark)]">
                Flexible Scheduling
              </p>
              <h2 className="mt-3 font-serif text-3xl leading-tight text-[var(--ink)] sm:text-4xl">
                Choose the Delivery Format for Your Club
              </h2>
            </div>

            <div className="mt-8 grid gap-6 sm:grid-cols-3">
              {formats.map((fmt) => (
                <div
                  key={fmt.title}
                  className="border border-[rgba(198,165,92,0.38)] bg-white p-6 shadow-sm"
                >
                  <Target size={22} className="text-[var(--gold-dark)]" />
                  <h3 className="mt-3 font-serif text-xl text-[var(--ink)]">{fmt.title}</h3>
                  <p className="mt-2 text-xs leading-6 text-[#675d50]">{fmt.description}</p>
                </div>
              ))}
            </div>

            {/* Editorial Feature: Intimate Cohort Analysis */}
            <div className="mt-14 overflow-hidden border border-[rgba(198,165,92,0.36)] bg-white shadow-[0_16px_50px_rgba(23,20,18,0.06)] grid grid-cols-1 lg:grid-cols-12">
              <div className="relative w-full aspect-[16/9] lg:aspect-auto lg:col-span-6 lg:min-h-[300px]">
                <Image
                  src="/foundations/golf/lornette-golf-indoor-green-notebook.png"
                  alt="Lornette Daye holding a coaching notebook on an indoor putting green with golf balls and clubs, ready for diagnostic clinic drills"
                  fill
                  sizes="(max-width: 1024px) 100vw, 50vw"
                  className="object-cover"
                  style={{ objectPosition: "68% 18%" }}
                />
                <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/20" />
              </div>
              <div className="p-8 lg:p-12 lg:col-span-6 flex flex-col justify-center bg-[linear-gradient(135deg,#fffdf8_0%,#faf6ee_100%)]">
                <span className="text-xs font-bold uppercase tracking-[0.22em] text-[var(--gold-dark)]">
                  Intimate Clinic Dynamics
                </span>
                <h3 className="mt-2 font-serif text-3xl text-[var(--ink)]">
                  Individual Diagnostic Attention
                </h3>
                <p className="mt-4 text-base leading-relaxed text-[#5e5346]">
                  Every workshop is capped at 12–24 participants to ensure direct observation of each golfer’s pre-shot timing, eye patterns, and post-shot reactions. Athletes receive real-time pacing adjustments from Lornette that immediately settle physical tension.
                </p>
                <div className="mt-6">
                  <CTAButton href="/book">
                    HOST A CLINIC AT YOUR CLUB
                  </CTAButton>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Commercial Ladder Cross-Link */}
        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-20 border-t border-[var(--line)]">
          <div className="mx-auto max-w-7xl">
            <div className="flex flex-col md:flex-row items-center justify-between gap-6 border border-[rgba(198,165,92,0.4)] bg-white p-8">
              <div>
                <p className="text-xs font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)]">
                  Next Step in the Pathway
                </p>
                <h3 className="mt-2 font-serif text-2xl text-[var(--ink)]">
                  Ready for the full 10-week competitive cohort?
                </h3>
                <p className="mt-1 text-sm text-[#675d50]">
                  Explore the flagship 10-Week Guided Program with 10 Athletic Foundations, weekly lessons, and field assignments.
                </p>
              </div>
              <Link
                href="/foundations/golf/program"
                className="inline-flex items-center gap-2 bg-[var(--ink)] px-6 py-3 text-xs font-bold uppercase tracking-[0.16em] text-[var(--ivory)] hover:bg-[var(--charcoal)] transition shrink-0"
              >
                View 10-Week Program <ArrowRight size={14} />
              </Link>
            </div>
          </div>
        </section>

        {/* Panoramic Closing Bottom Banner */}
        <section className="relative overflow-hidden border-t border-[rgba(198,165,92,0.4)] min-h-[340px] sm:min-h-[400px] flex items-center px-4 py-16 text-center text-[var(--ivory)] sm:px-6 lg:px-8 lg:py-24">
          <div className="absolute inset-0 pointer-events-none overflow-hidden">
            <Image
              src="/foundations/golf/scenic-gold-sunrise.jpg"
              alt="Golf practice green and driving range in golden morning sunrise"
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
              Club Coordination
            </p>
            <h2 className="mt-4 font-serif text-4xl leading-tight sm:text-5xl text-white">
              Schedule a Clinic for Your Members
            </h2>
            <p className="mt-4 text-base leading-8 text-[#d8cdbb]">
              We work directly with your Head Professional or Golf Committee to seamlessly coordinate range facilities and member signups.
            </p>
            <div className="mt-8 flex flex-col justify-center gap-3 sm:flex-row">
              <CTAButton href="/book">Inquire About Member Clinic Dates</CTAButton>
              <CTAButton
                href="/foundations/clubs"
                variant="secondary"
                className="border-white/30 text-white hover:bg-white/10"
              >
                View Club Partnership Options
              </CTAButton>
            </div>
          </div>
        </section>
      </main>
    </PageShell>
  );
}
