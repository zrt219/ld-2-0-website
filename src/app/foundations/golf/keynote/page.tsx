import Image from "next/image";
import Link from "next/link";
import { ArrowRight, CheckCircle2, Clock, Trophy, Users } from "lucide-react";
import { CTAButton } from "@/components/CTAButton";
import { FoundationsSubNav } from "@/components/foundations/FoundationsSubNav";
import { PageShell } from "@/components/PageShell";
import { SectionHeader } from "@/components/SectionHeader";
import { createMetadata } from "@/content/site";

export const metadata = createMetadata(
  "Playing Your Best When It Matters | Golf Keynote Experience",
  "An inspiring, high-impact keynote for golf clubs, tournaments, and banquets by Olympic coach Lornette Daye. Transform member culture and tournament composure.",
  "/foundations/golf/keynote",
);

const keynoteHighlights = [
  {
    title: "The Mental Space Between Shots",
    description:
      "In a four-hour round, a golfer swings for less than four minutes. How to command attention, silence internal narrative, and conserve nervous energy across the other 236 minutes.",
  },
  {
    title: "Composure When Pulse Rates Elevate",
    description:
      "Physiological arousal spikes on first tees, pressurized putts, and leaderboard turns. Practical somatic regulation to keep tempo and release clubhead tension under stress.",
  },
  {
    title: "The 5-Second Post-Mistake Reset",
    description:
      "A poor bounce or mis-struck iron cannot ruin a scorecard if the recovery protocol is disciplined. Transition cleanly from reaction to evaluation to total release before the next address.",
  },
  {
    title: "Building an Evidence Ledger",
    description:
      "Replace fragile optimism with grounded self-assurance. How elite competitors log committed routines and executed choices so confidence remains unshakeable in competition.",
  },
];

const audiences = [
  "Private Golf Clubs & Country Clubs",
  "Member-Guest & Club Championship Banquets",
  "PGA Section Coaching Symposiums",
  "Collegiate & Junior Development Programs",
  "Corporate Golf Days & Charity Invitationals",
];

export default function GolfKeynotePage() {
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
                    Keynote Experience
                  </span>
                </div>

                <h1 className="mt-6 font-serif text-4xl leading-[1.04] text-balance text-[var(--ink)] sm:text-6xl">
                  Playing Your Best When It Matters
                </h1>

                <p className="mt-4 text-sm font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)]">
                  Powered by the Performance Edge Framework
                </p>

                <p className="mt-6 text-base leading-8 text-[#554b40] sm:text-lg">
                  A 60–90 minute high-impact keynote crafted specifically for golf audiences. Lornette Daye brings four decades of elite sport, national sprint championships, and Olympic-level coaching to the psychological realities of the game.
                </p>

                <div className="mt-8 flex flex-wrap gap-4 text-xs font-semibold text-[#6e6355]">
                  <div className="flex items-center gap-2 border border-[rgba(198,165,92,0.4)] bg-white/60 px-3 py-1.5">
                    <Clock size={14} className="text-[var(--gold-dark)]" />
                    <span>Duration: 60–90 Minutes</span>
                  </div>
                  <div className="flex items-center gap-2 border border-[rgba(198,165,92,0.4)] bg-white/60 px-3 py-1.5">
                    <Users size={14} className="text-[var(--gold-dark)]" />
                    <span>Format: In-Person Banquet or Opening Address</span>
                  </div>
                  <div className="flex items-center gap-2 border border-[rgba(198,165,92,0.4)] bg-white/60 px-3 py-1.5">
                    <Trophy size={14} className="text-[var(--gold-dark)]" />
                    <span>Level: Club Members to Touring Amateurs</span>
                  </div>
                </div>

                <div className="mt-10 flex flex-col gap-3 sm:flex-row">
                  <CTAButton href="/book">Inquire About Keynote Availability</CTAButton>
                  <CTAButton href="/foundations/golf/workshop" variant="secondary">
                    Explore Hands-On Clinics
                  </CTAButton>
                </div>
              </div>

              <div className="relative lg:col-span-5">
                <div className="relative w-full aspect-[4/5] overflow-hidden border border-[rgba(198,165,92,0.42)] bg-[linear-gradient(180deg,#fffdf8_0%,#f5efe4_100%)] shadow-[0_28px_110px_rgba(23,20,18,0.14)]">
                  <Image
                    src="/foundations/golf/lornette-golf-keynote-podium.png"
                    alt="Lornette Daye speaking with open hands at a gold podium addressing an attentive banquet audience overlooking a golf course"
                    fill
                    priority
                    sizes="(max-width: 1024px) 92vw, 40vw"
                    className="object-cover"
                    style={{ objectPosition: "85% 18%" }}
                  />
                  <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/40" />
                  <div className="absolute inset-x-0 bottom-0 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(18,15,13,0.82)] p-4 sm:p-5 backdrop-blur-md shadow-2xl">
                    <p className="text-[11px] font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
                      Keynote Experience
                    </p>
                    <p className="mt-1 font-serif text-base text-white sm:text-lg">
                      Commanding Attention &amp; Composure
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Keynote Focus Pillars */}
        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <SectionHeader
              eyebrow="Keynote Curriculum"
              title="What Your Members and Players Take Home"
              body="Every story, concept, and framework delivers immediate on-course utility without conflicting with technical swing instruction."
            />

            <div className="mt-12 grid gap-6 sm:grid-cols-2">
              {keynoteHighlights.map((item, idx) => (
                <div
                  key={item.title}
                  className="border border-[rgba(198,165,92,0.34)] bg-white p-8 shadow-[0_16px_40px_rgba(23,20,18,0.04)]"
                >
                  <span className="font-serif text-3xl font-light text-[var(--champagne)]">
                    0{idx + 1}
                  </span>
                  <h2 className="mt-3 font-serif text-2xl text-[var(--ink)]">{item.title}</h2>
                  <p className="mt-3 text-sm leading-7 text-[#675d50]">{item.description}</p>
                </div>
              ))}
            </div>

            {/* Editorial Feature: Commanding the Clubhouse Room */}
            <div className="mt-14 overflow-hidden border border-[rgba(198,165,92,0.36)] bg-white shadow-[0_16px_50px_rgba(23,20,18,0.06)] grid grid-cols-1 lg:grid-cols-12">
              <div className="relative w-full aspect-[16/9] lg:aspect-auto lg:col-span-6 lg:min-h-[320px]">
                <Image
                  src="/foundations/golf/lornette-golf-terrace-skyline-view.png"
                  alt="Lornette Daye on private club terrace overlooking championship fairway and city skyline at golden sunset"
                  fill
                  sizes="(max-width: 1024px) 100vw, 50vw"
                  className="object-cover"
                  style={{ objectPosition: "66% 18%" }}
                />
                <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/20" />
              </div>
              <div className="p-8 lg:p-12 lg:col-span-6 flex flex-col justify-center bg-[linear-gradient(135deg,#fffdf8_0%,#faf6ee_100%)]">
                <span className="text-xs font-bold uppercase tracking-[0.22em] text-[var(--gold-dark)]">
                  Championship Atmosphere
                </span>
                <h3 className="mt-2 font-serif text-3xl text-[var(--ink)]">
                  An Unforgettable Clubhouse Experience
                </h3>
                <p className="mt-4 text-base leading-relaxed text-[#5e5346]">
                  Whether opening an invitational tournament or addressing a prestigious awards gala, Lornette Daye delivers an electric blend of Olympic wisdom, humorous real-world honesty, and practical mental frameworks that resonate with scratch players and high-handicappers alike.
                </p>
                <div className="mt-6">
                  <CTAButton href="/book">
                    INQUIRE ABOUT KEYNOTE DATES
                  </CTAButton>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Audiences Served */}
        <section className="border-t border-[var(--line)] bg-[#f6f2e8] px-4 py-16 sm:px-6 lg:px-8 lg:py-20">
          <div className="mx-auto max-w-7xl">
            <div className="grid gap-10 lg:grid-cols-[1fr_1.1fr] lg:items-center">
              <div>
                <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--gold-dark)]">
                  Ideal Audiences
                </p>
                <h2 className="mt-3 font-serif text-3xl leading-tight text-[var(--ink)] sm:text-4xl">
                  Tailored for Championship Dinners, Club Banquets & Coach Conferences
                </h2>
                <p className="mt-4 text-sm leading-7 text-[#675d50]">
                  Lornette customizes the opening anecdotes and practical takeaways to match your club’s calendar, tournament format, or competitive goals.
                </p>
              </div>

              <div className="grid gap-3">
                {audiences.map((aud) => (
                  <div
                    key={aud}
                    className="flex items-center gap-3 border border-[rgba(198,165,92,0.38)] bg-white p-4 shadow-sm"
                  >
                    <CheckCircle2 size={18} className="text-[var(--gold-dark)] shrink-0" />
                    <span className="text-sm font-semibold text-[var(--ink)]">{aud}</span>
                  </div>
                ))}
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
                  Looking for hands-on on-green instruction?
                </h3>
                <p className="mt-1 text-sm text-[#675d50]">
                  Explore the Performance Edge Member Workshop & Clinic for interactive drills.
                </p>
              </div>
              <Link
                href="/foundations/golf/workshop"
                className="inline-flex items-center gap-2 bg-[var(--ink)] px-6 py-3 text-xs font-bold uppercase tracking-[0.16em] text-[var(--ivory)] hover:bg-[var(--charcoal)] transition shrink-0"
              >
                View Workshop Details <ArrowRight size={14} />
              </Link>
            </div>
          </div>
        </section>

        {/* Panoramic Closing Bottom Banner matching user mockup */}
        <section className="relative overflow-hidden border-t border-[rgba(198,165,92,0.4)] min-h-[320px] sm:min-h-[380px] flex items-center px-4 py-16 text-center text-[var(--ivory)] sm:px-6 lg:px-8 lg:py-24">
          {/* Full-bleed panoramic golden-hour fairway background */}
          <div className="absolute inset-0 pointer-events-none overflow-hidden">
            <Image
              src="/foundations/golf/keynote-bottom-banner-fairway.jpg"
              alt="Championship golf course fairway in warm golden hour sunset"
              role="presentation"
              fill
              quality={95}
              sizes="100vw"
              className="object-cover object-center"
            />
            <div className="absolute inset-0 bg-gradient-to-t from-black/92 via-black/75 to-black/85" />
          </div>

          <div className="relative z-10 mx-auto max-w-3xl">
            <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--champagne)]">
              Reserve Your Date
            </p>
            <h2 className="mt-4 font-serif text-3xl sm:text-4xl lg:text-5xl leading-tight text-white font-normal">
              Bring Lornette to Your Club or Tournament
            </h2>
            <p className="mt-4 text-base leading-8 text-[#d8cdbb]">
              Inquire early to align keynotes with your club championship or season calendar.
            </p>
            <div className="mt-8 flex flex-col justify-center gap-3 sm:flex-row">
              <CTAButton href="/book">Inquire About Keynote Availability</CTAButton>
              <CTAButton href="/speaker-kit" variant="secondary">
                View Speaker Kit Materials
              </CTAButton>
            </div>
          </div>
        </section>
      </main>
    </PageShell>
  );
}
