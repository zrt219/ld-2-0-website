import Image from "next/image";
import Link from "next/link";
import {
  ChevronDown,
  Clock,
  Compass,
  Crosshair,
  Eye,
  Flag,
  Layers,
  RotateCcw,
  ShieldCheck,
  Sparkles,
  Target,
} from "lucide-react";

import { CTAButton } from "@/components/CTAButton";
import { PageShell } from "@/components/PageShell";
import { FoundationsSubNav } from "@/components/foundations/FoundationsSubNav";
import { createMetadata } from "@/content/site";

export const metadata = createMetadata(
  "Lornette’s Foundation Golf | 10-Week Guided Program",
  "A specialized 10-week guided athlete development program powered by the Performance Edge Framework, helping golfers master the 10 Athletic Foundations and practical mental game tools.",
  "/foundations/golf",
);

const credibilityStats = [
  { value: "Multi-Decade", label: "National Record Unsurpassed", detail: "Canadian sprint mark stood for decades · Canada Summer Games Double Gold Champion" },
  { value: "40+", label: "Years Coaching at Olympic Level", detail: "Canadian national sprint champion, multi-decade record holder, elite international coach" },
  { value: "150+", label: "International Competitors", detail: "Mentored across Olympic Trials, World Championships & national arenas" },
  { value: "500+", label: "Championship Athletes Coached", detail: "Elite juniors, collegiate NCAA contenders & tournament leaders coached to peak poise" },
  { value: "10", label: "Athletic Foundations", detail: "Comprehensive life & competition curriculum powered by Performance Edge" },
];

const coreOutcomes = [
  {
    title: "Composure Under Pressure",
    description:
      "Master physiological regulation when the tournament is on the line. Learn to recognize early tension cues, synchronize your breathing cadence, and commit unconditionally to every stroke.",
  },
  {
    title: "Automated Pre-Shot Cadence",
    description:
      "Develop a personalized, non-negotiable 6-step routine (Assess → Decide → Visualize → Reset → Execute → Release) that anchors focus and delivers absolute clarity across all conditions.",
  },
  {
    title: "Five-Second Mistake Recovery",
    description:
      "Apply Lornette’s signature principle: 'Your previous shot cannot hit your next shot.' Neutralize emotional frustration in five seconds, step onto the next tee clear, and protect your round.",
  },
  {
    title: "Evidence-Based Confidence",
    description:
      "Build genuine self-assurance founded on disciplined preparation rather than fragile optimism. Construct an internal ledger of executed routines that holds firm in championship moments.",
  },
  {
    title: "Identity Grounded Beyond the Score",
    description:
      "Separate your core self-worth from the numbers on the scorecard. Compete with freedom, discipline, and authority knowing your identity and worth remains unbroken regardless of outcome.",
  },
];

const curriculumPhases = [
  {
    phase: "Phase 1",
    title: "Build Your Foundation",
    weeksLabel: "Weeks 1–3",
    theme: "Internal Identity & Daily Preparation Systems",
    description:
      "Championship performance begins with unshakeable preparation. Phase 1 anchors your self-worth beyond the scorecard, refines your attention discipline, and establishes a repeatable pre-shot routine that holds steady in any competitive environment.",
    weeks: [
      { number: "01", name: "Identity Beyond Sport", focus: "Self-Worth & Scorecard Detachment" },
      { number: "02", name: "Champion Mindset", focus: "Attention Dial & Sensory Visualization" },
      { number: "03", name: "Discipline Systems", focus: "Repeatable 6-Step Pre-Shot Cadence" },
    ],
    milestone: "Codified personal pre-shot routine & scorecard boundary agreement.",
  },
  {
    phase: "Phase 2",
    title: "Perform & Respond",
    weeksLabel: "Weeks 4–6",
    theme: "Tournament Pressure & In-Round Recovery",
    description:
      "True composure is demonstrated in how quickly you reset after adversity. Phase 2 installs elite recovery protocols, physiological regulation skills, and competitive poise that allow you to execute each shot on its own terms.",
    weeks: [
      { number: "04", name: "Resilience After Setback", focus: "The Next Shot Principle & 5-Second Reset" },
      { number: "05", name: "Pressure, Emotional Regulation & Recovery", focus: "Breathing Cadence & Pressure Simulation" },
      { number: "06", name: "Communication & Presence", focus: "Internal Self-Talk & Body Language" },
    ],
    milestone: "5-second mistake reset mastery & live pressure simulation drill.",
  },
  {
    phase: "Phase 3",
    title: "Build What Comes Next",
    weeksLabel: "Weeks 7–10",
    theme: "Ecosystem, Career, Brand & Legacy",
    description:
      "A complete champion builds an enduring foundation: establishing healthy support ecosystems, professional financial literacy, and a capstone performance plan.",
    weeks: [
      { number: "07", name: "Family & Community Support", focus: "Support Ecosystem & Boundary Agreements" },
      { number: "08", name: "Career & Money Readiness", focus: "Professional Discipline & Transition Roadmap" },
      { number: "09", name: "Personal Brand & Story", focus: "Authentic Voice & Narrative Ownership" },
      { number: "10", name: "Legacy & Community Impact", focus: "Capstone 30-Day Performance Plan" },
    ],
    milestone: "Completed My 30-Day Performance Plan & season competition roadmap.",
  },
];

const weeklyRhythmSteps = [
  {
    step: "01",
    name: "Lornette Guidance",
    time: "15–20 Mins",
    description:
      "A focused video and audio orientation breaking down the week's athletic foundation and competitive significance.",
  },
  {
    step: "02",
    name: "One Focused Idea",
    time: "10 Mins",
    description:
      "A single, clear psychological concept grounded in 40+ years of elite Olympic and national champion coaching.",
  },
  {
    step: "03",
    name: "Practical Performance Tool",
    time: "15 Mins",
    description:
      "An actionable Performance Edge framework exercise (e.g., Attention Dial, 5-Second Mistake Reset, Pre-Shot Cadence).",
  },
  {
    step: "04",
    name: "Real-World Golf Application",
    time: "On-Course / Range",
    description:
      "Structured drills to execute on the practice green, driving range, or during your weekly competition round.",
  },
  {
    step: "05",
    name: "Short Reflection",
    time: "10 Mins",
    description:
      "A concise guided check-in to log evidence, note performance discoveries, and anchor mental growth in your ledger.",
  },
];

const golfFaqs = [
  {
    question: "Who is Lornette’s Foundations Golf designed for?",
    answer:
      "This program is crafted for dedicated competitive golfers: junior tournament competitors preparing for collegiate recruiting, high school and collegiate athletes, mid-amateur tournament players, and aspiring professionals seeking an evidence-based mental edge under intense pressure.",
  },
  {
    question: "How does this program work alongside my technical swing coach?",
    answer:
      "Lornette’s program does not interfere with your swing mechanics; it empowers them. Most tournament errors occur not from flawed mechanics, but from elevated tension, rushing, or indecision. The Performance Edge Framework ensures your mind and nervous system allow your trained swing to execute freely.",
  },
  {
    question: "What is the weekly time commitment during tournament season?",
    answer:
      "The program is engineered specifically for active athletes: approximately 60 to 90 minutes of guided study per week, plus integrated on-course field exercises that you can incorporate directly into your scheduled range sessions and practice rounds.",
  },
  {
    question: "Can golf clubs, collegiate teams, or junior academies host this?",
    answer:
      "Yes. In addition to individual guided cohorts, Lornette delivers on-site member clinics, coaches symposiums, and multi-week club partnerships customized for member engagement or team competitive readiness.",
  },
  {
    question: "How is the 10-week guided program delivered?",
    answer:
      "The 10-week program is cohort-based and guided directly by Lornette Daye. Participants receive weekly structured modules, clear field assignments, video orientations, and direct check-ins to review progress and refine on-course performance plans.",
  },
];

const golfTools = [
  {
    number: "01",
    title: "Focus",
    icon: Target,
    whiteboard: "The Attention Game",
    tagline: "Win the internal battle for your eyes and mind.",
    description:
      "In a 4-hour round, you swing for less than 4 minutes. We teach you to own the other 236. Activate focus more effectively, silence internal noise, and arrive at every location fully present.",
  },
  {
    number: "02",
    title: "Pre-Shot Routine",
    icon: Crosshair,
    whiteboard: "Build Your Pre-Shot Routine",
    tagline: "Six-step repeatable execution on every single shot.",
    description:
      "A great swing begins before the takeaway. Players codify a non-negotiable cadence: Assess → Decide → Visualize → Reset → Execute → Release. When pressure mounts, the routine acts as a steady psychological anchor.",
  },
  {
    number: "03",
    title: "Pressure",
    icon: Sparkles,
    whiteboard: "What Pressure Does",
    tagline: "Notice → Breathe → Target → Commit.",
    description:
      "Pressure is biological, not personal. We teach golfers to recognize physical tension, regulate breathing cadence, recenter on the physical target, and swing with full commitment instead of defensive hesitation.",
  },
  {
    number: "04",
    title: "Visualization",
    icon: Eye,
    whiteboard: "See It Before You Hit It",
    tagline: "Mental rehearsal before physical execution.",
    description:
      "Elite competitors prime their nervous system with clear sensory imagery. Golfers learn to vividly picture shot shape, trajectory apex, landing zone, and the feel of solid contact before stepping into the stance.",
  },
  {
    number: "05",
    title: "Reset",
    icon: RotateCcw,
    whiteboard: "The Five Seconds After a Mistake",
    tagline: "Your previous shot cannot hit your next shot.",
    description:
      "Bad breaks and poor strikes happen in every tournament round. The Next Shot Principle provides a five-step recovery protocol: Acknowledge → Evaluate → Release → Reset → Recommit, neutralizing emotional residue within five seconds.",
  },
  {
    number: "06",
    title: "Decision-Making",
    icon: Compass,
    whiteboard: "The Decision Before the Shot",
    tagline: "Calculate percentages. Commit without second-guessing.",
    description:
      "Double bogeys often stem from poor decisions rather than poor swings. We teach risk assessment, margin management, and the discipline to execute high-percentage plays under tournament heat.",
  },
  {
    number: "07",
    title: "Competition Preparation",
    icon: Flag,
    whiteboard: "Your Competition Plan",
    tagline: "Structure your arrival, warm-up, and first tee readiness.",
    description:
      "Stepping onto the first tee with calm confidence requires intentional structure. Athletes build personalized competition day plans spanning sleep, nutrition, range warm-up sequencing, and emotional grounding.",
  },
  {
    number: "08",
    title: "Confidence",
    icon: ShieldCheck,
    whiteboard: "Confidence From Evidence",
    tagline: "Earned self-assurance built on verifiable facts.",
    description:
      "True competitive confidence is not false positivity; it is evidence-based. Golfers track completed routines, disciplined choices, successful resets, and handled pressure to build an undeniable internal ledger of capability.",
  },
];

const curriculumWeeks = [
  {
    week: "Week 1",
    title: "Identity Beyond Sport",
    pillars: "Self-Worth & Athlete Identity",
    sequence: "Athlete Identity → Scorecard Detachment → Mental Boundary",
    assignment: "Reflection on self-worth anchors independent of golf scorecards and rankings.",
    lornetteMessage: "Before the Start",
  },
  {
    week: "Week 2",
    title: "Champion Mindset",
    pillars: "Focus & Visualization",
    sequence: "Attention Dial → Sensory Visualization → Evidence Ledger",
    assignment: "9-hole focus toggle drill; sensory visualization prior to execution.",
    lornetteMessage: "The Mindset of a Champion",
  },
  {
    week: "Week 3",
    title: "Discipline Systems",
    pillars: "Pre-Shot Routine & Preparation",
    sequence: "Assess → Decide → Visualize → Reset → Execute → Release",
    assignment: "Execute routine on every full shot for 9 holes; log completion consistency.",
    lornetteMessage: "Routine as Your Anchor",
  },
  {
    week: "Week 4",
    title: "Resilience After Setback",
    pillars: "Mistake Reset & The Next Shot",
    sequence: "Acknowledge → Evaluate → Release → Reset → Recommit",
    assignment: "5-second emotional reset drill; audit recovery time after missed greens or bogeys.",
    lornetteMessage: "The Next Shot Principle",
  },
  {
    week: "Week 5",
    title: "Pressure, Emotional Regulation & Recovery",
    pillars: "Pressure Response & Recovery",
    sequence: "Notice → Breathe → Target → Commit",
    assignment: "The Pressure 5 field drill: executing deliberate pressure simulations on practice grounds.",
    lornetteMessage: "When It Actually Matters",
  },
  {
    week: "Week 6",
    title: "Communication & Presence",
    pillars: "Self-Talk & Tournament Presence",
    sequence: "Internal Self-Talk → Coach Alignment → Composure",
    assignment: "On-course internal dialogue audit; competition presence and posture checklist.",
    lornetteMessage: "Commanding Your Space",
  },
  {
    week: "Week 7",
    title: "Family & Community Support",
    pillars: "Expectations & Support Circle",
    sequence: "Ecosystem Mapping → Boundary Agreements → Team Alignment",
    assignment: "Map athlete support ecosystem and define healthy communication boundaries.",
    lornetteMessage: "The Support Team",
  },
  {
    week: "Week 8",
    title: "Career & Money Readiness",
    pillars: "Professional Mindset & Transition",
    sequence: "Career Roadmap → Professional Discipline → Budgeting",
    assignment: "Personal career roadmap and professional readiness inventory.",
    lornetteMessage: "The Professional Standard",
  },
  {
    week: "Week 9",
    title: "Personal Brand & Story",
    pillars: "Authentic Voice & Narrative",
    sequence: "Authentic Voice → Representative Excellence → Narrative Ownership",
    assignment: "Craft personal mission statement and core story pillars.",
    lornetteMessage: "Owning Your Story",
  },
  {
    week: "Week 10",
    title: "Legacy & Community Impact",
    pillars: "Mentorship & Life Beyond Sport",
    sequence: "Capstone Performance Plan → Mentorship → Leadership",
    assignment: "Complete My 30-Day Performance Plan and define community contribution goals.",
    lornetteMessage: "What Champions Take With Them",
  },
];

const deliveryFormats = [
  {
    title: "Keynote Experience",
    subtitle: "Playing Your Best When It Matters",
    time: "60–90 Minutes",
    href: "/foundations/golf/keynote",
    description:
      "A dynamic, inspiring address for club banquets, member tournaments, or coach symposiums introducing the core principles of competitive mental toughness.",
  },
  {
    title: "Member Workshop & Clinic",
    subtitle: "The Performance Edge Workshop & Member Clinic",
    time: "Approx. 2 Hours",
    href: "/foundations/golf/workshop",
    description:
      "Our flagship hands-on member clinic combining whiteboard instruction with live pre-shot routine development, pressure breathing, and mistake recovery drills.",
  },
  {
    title: "10-Week Guided Program",
    subtitle: "Lornette’s Foundation Golf 10-Week Guided Program",
    time: "10 Weeks Structured",
    href: "/foundations/golf/program",
    description:
      "A 10-week cohort-based guided journey led by Lornette, combining 10 Foundation modules, structured on-course field assignments, and peer accountability for competitive players.",
  },
  {
    title: "Club Partnership",
    subtitle: "Lornette’s Foundation Golf Club Partnership",
    time: "Seasonal / Annual",
    href: "/foundations/golf/club-partnership",
    description:
      "Complete club alignment including keynotes, member clinics, junior development integration, and coach collaboration to elevate the club's golf culture.",
  },
];

export default function FoundationsGolfPage() {
  return (
    <PageShell>
      <main className="bg-[var(--ivory)] text-[var(--ink)]">
        <FoundationsSubNav />

        {/* Hero Section */}
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
                    Mental Game &amp; Performance
                  </span>
                </div>

                <h1 className="mt-6 font-serif text-4xl leading-[1.04] text-balance text-[var(--ink)] sm:text-6xl lg:text-[3.9rem]">
                  Play Your Best When It Matters.
                </h1>

                <p className="mt-4 font-serif text-2xl text-[var(--gold-dark)] sm:text-3xl">
                  Lornette’s Foundation Golf
                </p>

                <p className="mt-2 text-xs font-bold uppercase tracking-[0.22em] text-[var(--gold-dark)]">
                  Powered by the Performance Edge Framework
                </p>

                <p className="mt-6 text-base leading-8 text-[#4f4438] sm:text-lg">
                  The mental side of golf performance, focus under pressure, and repeatable execution. Guided by Olympic-level coach Lornette Daye, the 10-Week Guided Program develops the 10 Athletic Foundations alongside practical Performance Edge routines to help competitive golfers play their best when it matters most.
                </p>

                <div className="mt-8 flex flex-col gap-3 sm:flex-row">
                  <CTAButton href="/foundations/golf/program">
                    EXPLORE THE 10-WEEK PROGRAM
                  </CTAButton>
                  <CTAButton href="/foundations/clubs" variant="secondary">
                    FOR CLUBS & TEAMS
                  </CTAButton>
                </div>
              </div>

              <div className="relative lg:col-span-5">
                <div className="relative w-full aspect-[4/5] overflow-hidden border border-[rgba(198,165,92,0.42)] bg-[linear-gradient(180deg,#fffdf8_0%,#f5efe4_100%)] shadow-[0_28px_110px_rgba(23,20,18,0.14)]">
                  <Image
                    src="/foundations/golf/lornette-golf-putting-green-sunrise.png"
                    alt="Lornette Daye coaching a competitive golfer on the putting green at sunrise"
                    fill
                    priority
                    sizes="(max-width: 1024px) 100vw, 42vw"
                    className="object-cover"
                    style={{ objectPosition: "82% 18%" }}
                  />
                  <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/40" />
                  <div className="absolute inset-x-0 bottom-0 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(18,15,13,0.82)] p-4 sm:p-5 backdrop-blur-md shadow-2xl">
                    <p className="text-[11px] font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
                      Your Mental Game Starts Here
                    </p>
                    <p className="mt-1 font-serif text-base text-white sm:text-lg">
                      Your previous shot cannot hit your next shot.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Verified Credibility Strip */}
        <section
          aria-label="Verified athletic credentials"
          className="border-b border-[rgba(198,165,92,0.3)] bg-white/70 px-4 py-10 sm:px-6 lg:px-8"
        >
          <div className="mx-auto max-w-7xl">
            <div className="grid grid-cols-2 gap-6 sm:grid-cols-3 lg:grid-cols-5 lg:gap-8">
              {credibilityStats.map((stat) => (
                <div
                  key={stat.label}
                  className="border-l-2 border-[var(--gold-dark)] pl-4 sm:pl-6"
                >
                  <span className="block font-serif text-3xl font-bold text-[var(--gold-dark)] sm:text-4xl">
                    {stat.value}
                  </span>
                  <span className="mt-1 block text-xs font-bold uppercase tracking-[0.14em] text-[var(--ink)]">
                    {stat.label}
                  </span>
                  <span className="mt-1 block text-xs text-[#6e6355]">
                    {stat.detail}
                  </span>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Core Outcomes: What This Program Helps Build */}
        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <div className="max-w-3xl">
              <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--gold-dark)]">
                Proven Competitive Capabilities
              </p>
              <h2 className="mt-4 font-serif text-4xl leading-tight text-[var(--ink)] sm:text-5xl">
                What This Program Helps You Build
              </h2>
              <p className="mt-4 text-base leading-8 text-[#5b5043]">
                Real breakthroughs on the course are not built on swing gimmicks or false positivity. They are built on repeatable psychological systems tested under tournament pressure.
              </p>
            </div>

            <div className="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
              {coreOutcomes.map((outcome, idx) => (
                <div
                  key={outcome.title}
                  className="border border-[rgba(198,165,92,0.34)] bg-white p-7 shadow-[0_16px_50px_rgba(23,20,18,0.04)]"
                >
                  <div className="flex items-center gap-3">
                    <span className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-[#c5aa68]/20 font-serif text-sm font-bold text-[var(--gold-dark)]">
                      {idx + 1}
                    </span>
                    <h3 className="font-serif text-xl text-[var(--ink)]">
                      {outcome.title}
                    </h3>
                  </div>
                  <p className="mt-4 text-sm leading-7 text-[#5b5043]">
                    {outcome.description}
                  </p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* The Practical Performance Tools */}
        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <div className="text-center max-w-3xl mx-auto">
              <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--gold-dark)]">
                The Performance Edge Framework
              </p>
              <h2 className="mt-4 font-serif text-4xl leading-tight text-[var(--ink)] sm:text-5xl">
                Practical Golf Performance Tools
              </h2>
              <p className="mt-4 text-base leading-8 text-[#675d50]">
                Actionable mental game tools integrated across the 10 Athletic Foundations to address decisive psychological challenges golfers face on the course.
              </p>
            </div>

            <div className="mt-14 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
              {golfTools.map((tool) => {
                const Icon = tool.icon;
                return (
                  <article
                    key={tool.title}
                    className="border border-[rgba(198,165,92,0.34)] bg-white p-7 shadow-[0_16px_50px_rgba(23,20,18,0.05)] transition duration-200 hover:-translate-y-1 hover:border-[var(--champagne)]"
                  >
                    <div className="flex items-center justify-between">
                      <span className="font-serif text-sm font-bold text-[var(--gold-dark)]">
                        {tool.number}
                      </span>
                      <Icon size={20} aria-hidden="true" className="text-[var(--champagne)]" />
                    </div>

                    <h3 className="mt-4 font-serif text-2xl text-[var(--ink)]">
                      {tool.title}
                    </h3>
                    <p className="mt-1 text-xs font-bold uppercase tracking-[0.14em] text-[var(--gold-dark)]">
                      {tool.whiteboard}
                    </p>

                    <p className="mt-4 text-sm font-medium italic text-[var(--charcoal)]">
                      {tool.tagline}
                    </p>

                    <p className="mt-3 text-sm leading-7 text-[#675d50]">
                      {tool.description}
                    </p>
                  </article>
                );
              })}
            </div>

            {/* Editorial Sunlight Feature: The Attention Game */}
            <div className="mt-14 overflow-hidden border border-[rgba(198,165,92,0.36)] bg-white shadow-[0_16px_50px_rgba(23,20,18,0.06)] grid lg:grid-cols-12">
              <div className="relative aspect-[16/9] lg:aspect-auto lg:col-span-6 min-h-[300px]">
                <Image
                  src="/foundations/golf/sunlight-golf-dew-flag.jpg"
                  alt="Morning dew on championship putting green with golf ball and cup in golden sunrise"
                  fill
                  sizes="(max-width: 1024px) 100vw, 50vw"
                  className="object-cover"
                />
                <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/20" />
              </div>
              <div className="p-8 lg:p-12 lg:col-span-6 flex flex-col justify-center bg-[linear-gradient(135deg,#fffdf8_0%,#faf6ee_100%)]">
                <span className="text-xs font-bold uppercase tracking-[0.22em] text-[var(--gold-dark)]">
                  Performance Edge in Practice · The Attention Game
                </span>
                <h3 className="mt-2 font-serif text-3xl text-[var(--ink)]">
                  The Silence Between Shots
                </h3>
                <p className="mt-4 text-base leading-relaxed text-[#5e5346]">
                  In an 18-hole tournament round lasting over four hours, the physical swing consumes less than four minutes of actual motion. The remaining 236 minutes are spent walking, waiting, calculating, and managing the mind. The Performance Edge Framework equips golfers with repeatable rituals to govern attention during those silent intervals.
                </p>
              </div>
            </div>

            {/* Editorial Showcase: Championship Presence & Coastal Discipline */}
            <div className="mt-10 overflow-hidden border border-[rgba(198,165,92,0.36)] bg-white shadow-[0_16px_50px_rgba(23,20,18,0.06)] grid grid-cols-1 lg:grid-cols-12">
              <div className="min-w-0 p-6 sm:p-8 lg:p-12 lg:col-span-6 flex flex-col justify-center bg-[linear-gradient(135deg,#fffdf8_0%,#faf6ee_100%)] order-2 lg:order-1">
                <span className="text-xs font-bold uppercase tracking-[0.22em] text-[var(--gold-dark)]">
                  Championship Demeanor & Composure
                </span>
                <h3 className="mt-2 font-serif text-2xl sm:text-3xl text-[var(--ink)]">
                  Composure Across All Conditions
                </h3>
                <p className="mt-4 text-base leading-relaxed text-[#5e5346]">
                  Championship golf is not contested in a vacuum. Changing winds, pressure pin placements, and shifting coastal tides test whether an athlete&apos;s routine is an intellectual idea or an ingrained habit. Lornette instills the mental conditioning required to stand tall and execute when conditions demand absolute focus.
                </p>
                <div className="mt-6 flex flex-wrap gap-3">
                  <CTAButton href="/foundations/golf/program">
                    EXPLORE 10-WEEK CURRICULUM
                  </CTAButton>
                  <CTAButton href="/foundations/golf/club-partnership" variant="secondary">
                    CLUB INTEGRATION
                  </CTAButton>
                </div>
              </div>
              <div className="relative w-full aspect-[16/9] lg:aspect-auto lg:col-span-6 lg:min-h-[320px] order-1 lg:order-2">
                <Image
                  src="/foundations/golf/golfer-composure-green.jpg"
                  alt="Competitive golfer crouching on putting green lining up putt under tournament pressure"
                  fill
                  sizes="(max-width: 1024px) 100vw, 50vw"
                  className="object-cover"
                  style={{ objectPosition: "35% 25%" }}
                />
                <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/20" />
              </div>
            </div>
          </div>
        </section>

        {/* 10-Week Curriculum: 3-Phase Presentation + Accessible Progressive Disclosure */}
        <section className="border-y border-[var(--line)] bg-[var(--sand)]/35 px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <div className="grid gap-8 lg:grid-cols-[0.5fr_0.5fr] lg:items-end">
              <div>
                <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--gold-dark)]">
                  Curriculum Architecture
                </p>
                <h2 className="mt-4 font-serif text-4xl leading-tight text-[var(--ink)] sm:text-5xl">
                  The 10-Week Athlete Development Journey
                </h2>
              </div>
              <p className="text-base leading-8 text-[#5b5043]">
                Structured for sustainable athletic mastery, the curriculum unfolds across three progressive phases, guiding competitors from foundational identity to tournament execution and enduring legacy.
              </p>
            </div>

            {/* 3 Phases High-Level Cards */}
            <div className="mt-14 grid gap-8 lg:grid-cols-3">
              {curriculumPhases.map((phase) => (
                <div
                  key={phase.phase}
                  className="border border-[rgba(198,165,92,0.4)] bg-white p-7 shadow-[0_16px_50px_rgba(23,20,18,0.06)] flex flex-col justify-between"
                >
                  <div>
                    <div className="flex items-center justify-between border-b border-[var(--line)] pb-4">
                      <span className="inline-block rounded-sm bg-[#c5aa68]/20 px-3 py-1 text-xs font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)]">
                        {phase.phase} · {phase.weeksLabel}
                      </span>
                      <Layers size={18} aria-hidden="true" className="text-[var(--champagne)]" />
                    </div>

                    <h3 className="mt-4 font-serif text-2xl text-[var(--ink)]">
                      {phase.title}
                    </h3>
                    <p className="mt-1 text-xs font-bold uppercase tracking-[0.14em] text-[var(--gold-dark)]">
                      {phase.theme}
                    </p>

                    <p className="mt-4 text-sm leading-relaxed text-[#5b5043]">
                      {phase.description}
                    </p>

                    <div className="mt-6 space-y-2.5">
                      <p className="text-[11px] font-bold uppercase tracking-[0.18em] text-[#786b5d]">
                        Core Foundations:
                      </p>
                      {phase.weeks.map((w) => (
                        <div key={w.number} className="flex items-start gap-2.5 text-xs text-[#4f4438]">
                          <span className="font-serif font-bold text-[var(--gold-dark)] shrink-0">
                            W{w.number}
                          </span>
                          <span>
                            <strong className="text-[var(--ink)]">{w.name}</strong>: {w.focus}
                          </span>
                        </div>
                      ))}
                    </div>
                  </div>

                  <div className="mt-6 pt-4 border-t border-[var(--line)]">
                    <p className="text-[11px] font-bold uppercase tracking-[0.16em] text-[#786b5d]">
                      Phase Milestone
                    </p>
                    <p className="mt-1 text-xs font-semibold text-[var(--ink)]">
                      {phase.milestone}
                    </p>
                  </div>
                </div>
              ))}
            </div>

            {/* Accessible Progressive Disclosure for All 10 Weeks */}
            <details className="group mt-12 rounded-sm border border-[rgba(198,165,92,0.4)] bg-white p-6 sm:p-8 shadow-sm">
              <summary className="flex cursor-pointer items-center justify-between font-serif text-xl sm:text-2xl text-[var(--ink)] hover:text-[var(--gold-dark)] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)] select-none">
                <span className="flex items-center gap-3">
                  <span className="flex h-7 w-7 items-center justify-center rounded-full bg-[#c5aa68]/20 text-xs font-bold text-[var(--gold-dark)]">
                    10
                  </span>
                  See the Full 10-Week Journey & Field Assignments
                </span>
                <ChevronDown
                  size={20}
                  aria-hidden="true"
                  className="text-[var(--gold-dark)] transition-transform duration-200 group-open:rotate-180"
                />
              </summary>

              <div className="mt-8 border-t border-[var(--line)] pt-6">
                <p className="text-xs uppercase tracking-[0.18em] text-[#786b5d] mb-6">
                  Complete 10-Week Syllabus Breakdown:
                </p>

                <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-5">
                  {curriculumWeeks.map((week) => (
                    <div
                      key={week.week}
                      className="border border-[rgba(198,165,92,0.32)] bg-[#fffdfa] p-5 shadow-sm flex flex-col justify-between"
                    >
                      <div>
                        <span className="inline-block rounded-sm bg-[#c5aa68]/20 px-2.5 py-1 text-xs font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)]">
                          {week.week}
                        </span>
                        <h4 className="mt-3 font-serif text-base text-[var(--ink)] leading-snug">
                          {week.title}
                        </h4>
                        <p className="mt-1 text-xs font-bold uppercase tracking-[0.12em] text-[var(--gold-dark)]">
                          {week.pillars}
                        </p>

                        <div className="mt-3 pt-3 border-t border-[var(--line)]">
                          <p className="text-[10px] font-bold uppercase tracking-[0.16em] text-[#786b5d]">
                            Core Sequence
                          </p>
                          <p className="mt-1 text-xs font-semibold text-[var(--charcoal)] leading-relaxed">
                            {week.sequence}
                          </p>
                        </div>

                        <div className="mt-3 pt-3 border-t border-[var(--line)]">
                          <p className="text-[10px] font-bold uppercase tracking-[0.16em] text-[#786b5d]">
                            Field Assignment
                          </p>
                          <p className="mt-1 text-xs leading-5 text-[#5b5043]">
                            {week.assignment}
                          </p>
                        </div>
                      </div>

                      <div className="mt-4 pt-3 border-t border-[var(--line)] flex items-center justify-between text-xs text-[#786b5d]">
                        <span>Focus:</span>
                        <span className="font-bold text-[var(--ink)] text-right">{week.lornetteMessage}</span>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            </details>

            {/* Editorial Feature: On-Course Execution */}
            <div className="mt-14 overflow-hidden border border-[rgba(198,165,92,0.36)] bg-white shadow-[0_16px_50px_rgba(23,20,18,0.06)] grid lg:grid-cols-12">
              <div className="p-8 lg:p-12 lg:col-span-6 flex flex-col justify-center bg-[linear-gradient(135deg,#fffdf8_0%,#faf6ee_100%)] order-2 lg:order-1">
                <span className="text-xs font-bold uppercase tracking-[0.22em] text-[var(--gold-dark)]">
                  On-Course Field Work
                </span>
                <h3 className="mt-2 font-serif text-3xl text-[var(--ink)]">
                  Turning Principles Into Scorecard Results
                </h3>
                <p className="mt-4 text-base leading-relaxed text-[#554a3e]">
                  Every week combines Foundation insights with structured field assignments on the practice range and course. Players codify non-negotiable routines, audit decision choices, and build a permanent evidence ledger that withstands tournament heat.
                </p>
                <div className="mt-6">
                  <CTAButton href="/foundations/golf/program">
                    EXPLORE THE 10-WEEK COHORT
                  </CTAButton>
                </div>
              </div>
              <div className="relative aspect-[16/9] lg:aspect-auto lg:col-span-6 min-h-[300px] order-1 lg:order-2">
                <Image
                  src="/foundations/golf/sunlight-golf-fairway-sunrise.jpg"
                  alt="Championship golf course fairway at golden sunrise with morning mist"
                  fill
                  sizes="(max-width: 1024px) 100vw, 50vw"
                  className="object-cover"
                />
                <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/20" />
              </div>
            </div>
          </div>
        </section>

        {/* One Foundation at a Time: The Learning Rhythm */}
        <section className="px-4 pt-16 pb-8 sm:px-6 sm:pt-20 sm:pb-10 lg:px-8 lg:pt-24 lg:pb-12">
          <div className="mx-auto max-w-7xl">
            <div className="text-center max-w-3xl mx-auto">
              <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--gold-dark)]">
                The Learning Rhythm
              </p>
              <h2 className="mt-4 font-serif text-4xl leading-tight text-[var(--ink)] sm:text-5xl">
                One Foundation at a Time
              </h2>
              <p className="mt-4 text-base leading-8 text-[#5b5043]">
                Master one Athletic Foundation at a time through a structured weekly cadence engineered to integrate seamlessly with school, training, and competitive tournament schedules.
              </p>
            </div>

            <div className="mt-14 grid gap-6 sm:grid-cols-2 lg:grid-cols-5">
              {weeklyRhythmSteps.map((step) => (
                <div
                  key={step.step}
                  className="border border-[rgba(198,165,92,0.35)] bg-white p-6 shadow-sm flex flex-col justify-between"
                >
                  <div>
                    <div className="flex items-center justify-between">
                      <span className="font-serif text-xl font-bold text-[var(--gold-dark)]">
                        {step.step}
                      </span>
                      <span className="inline-flex items-center gap-1 text-[11px] font-semibold text-[#786b5d]">
                        <Clock size={12} aria-hidden="true" />
                        {step.time}
                      </span>
                    </div>
                    <h3 className="mt-4 font-serif text-lg text-[var(--ink)]">
                      {step.name}
                    </h3>
                    <p className="mt-3 text-xs leading-6 text-[#5b5043]">
                      {step.description}
                    </p>
                  </div>
                </div>
              ))}
            </div>

            <div className="mt-10 rounded-sm border border-[rgba(198,165,92,0.35)] bg-[#faf6ee] p-6 text-center max-w-2xl mx-auto">
              <p className="text-xs font-bold uppercase tracking-[0.18em] text-[var(--gold-dark)]">
                Weekly Time Commitment
              </p>
              <p className="mt-2 text-sm text-[#4f4438] leading-relaxed">
                <strong>~60–90 minutes</strong> of guided online study per week, plus integrated on-course drills during your regular practice rounds. Zero busywork. Pure performance leverage.
              </p>
            </div>
          </div>
        </section>

        {/* Formats & Engagement */}
        <section className="px-4 pt-4 pb-16 sm:px-6 sm:pt-6 sm:pb-20 lg:px-8 lg:pt-8 lg:pb-24">
          <div className="mx-auto max-w-7xl">
            <div className="text-center max-w-3xl mx-auto">
              <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--gold-dark)]">
                Program Delivery
              </p>
              <h2 className="mt-4 font-serif text-4xl leading-tight text-[var(--ink)] sm:text-5xl">
                Ways to Engage
              </h2>
              <p className="mt-4 text-base leading-8 text-[#5b5043]">
                Available as member clinics, keynote addresses, structured 10-week cohorts, or full club partnerships.
              </p>
            </div>

            <div className="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
              {deliveryFormats.map((format) => (
                <div
                  key={format.title}
                  className="border border-[rgba(198,165,92,0.34)] bg-white p-7 shadow-[0_16px_50px_rgba(23,20,18,0.05)] flex flex-col justify-between"
                >
                  <div>
                    <span className="text-xs font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)]">
                      {format.time}
                    </span>
                    <h3 className="mt-3 font-serif text-2xl text-[var(--ink)]">
                      {format.title}
                    </h3>
                    <p className="mt-1 text-xs font-semibold text-[#786b5d]">
                      {format.subtitle}
                    </p>
                    <p className="mt-4 text-sm leading-7 text-[#5b5043]">
                      {format.description}
                    </p>
                  </div>
                  <div className="mt-6 pt-4 border-t border-[var(--line)]">
                    <Link
                      href={format.href}
                      className="inline-flex min-h-11 items-center gap-1 text-xs font-bold uppercase tracking-[0.16em] text-[var(--gold-dark)] hover:underline focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)]"
                    >
                      Explore Format Details &rarr;
                    </Link>
                  </div>
                </div>
              ))}
            </div>

            {/* Editorial Feature: Modern Studio Precision */}
            <div className="mt-14 overflow-hidden border border-[rgba(198,165,92,0.36)] bg-white shadow-[0_16px_50px_rgba(23,20,18,0.06)] grid lg:grid-cols-12">
              <div className="relative aspect-[16/9] lg:aspect-auto lg:col-span-6 min-h-[320px]">
                <Image
                  src="/foundations/golf/golf-range-tablet-analytics.jpg"
                  alt="Golf coach and competitive player analyzing swing data on a tablet at the outdoor practice range with launch monitor"
                  fill
                  sizes="(max-width: 1024px) 100vw, 50vw"
                  className="object-cover"
                  style={{ objectPosition: "center 20%" }}
                />
                <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/20" />
              </div>
              <div className="p-8 lg:p-12 lg:col-span-6 flex flex-col justify-center bg-[linear-gradient(135deg,#fffdf8_0%,#faf6ee_100%)]">
                <span className="text-xs font-bold uppercase tracking-[0.22em] text-[var(--gold-dark)]">
                  Data Meets Psychology
                </span>
                <h3 className="mt-2 font-serif text-3xl text-[var(--ink)]">
                  Translating Analytics into Tournament Conviction
                </h3>
                <p className="mt-4 text-base leading-relaxed text-[#554a3e]">
                  Trackman data and high-speed cameras tell players what their clubface did, but they cannot teach how to quiet a racing heart over a four-foot putt. The Performance Edge Framework complements technical golf coaching by ensuring mental stability matches physical swing mechanics.
                </p>
                <div className="mt-6 flex flex-wrap gap-3">
                  <CTAButton href="/foundations/golf/workshop">
                    EXPLORE WORKSHOPS
                  </CTAButton>
                  <CTAButton href="/foundations/golf/program" variant="secondary">
                    10-WEEK COHORT
                  </CTAButton>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Frequently Asked Questions */}
        <section className="border-t border-[var(--line)] bg-white/60 px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-4xl">
            <div className="text-center max-w-2xl mx-auto">
              <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--gold-dark)]">
                Got Questions?
              </p>
              <h2 className="mt-4 font-serif text-4xl leading-tight text-[var(--ink)] sm:text-5xl">
                Frequently Asked Questions
              </h2>
              <p className="mt-4 text-base leading-8 text-[#5b5043]">
                Clear answers regarding the curriculum, coaching integration, and engagement options.
              </p>
            </div>

            <div className="mt-12 space-y-4">
              {golfFaqs.map((faq) => (
                <details
                  key={faq.question}
                  className="group rounded-sm border border-[rgba(198,165,92,0.35)] bg-white p-5 sm:p-6 shadow-sm transition duration-150 open:border-[var(--champagne)]"
                >
                  <summary className="flex cursor-pointer items-center justify-between text-base sm:text-lg font-serif font-medium text-[var(--ink)] hover:text-[var(--gold-dark)] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)] select-none">
                    <span>{faq.question}</span>
                    <ChevronDown
                      size={18}
                      aria-hidden="true"
                      className="text-[var(--gold-dark)] shrink-0 ml-4 transition-transform duration-200 group-open:rotate-180"
                    />
                  </summary>
                  <p className="mt-4 text-sm leading-7 text-[#554a3e] border-t border-[var(--line)] pt-4">
                    {faq.answer}
                  </p>
                </details>
              ))}
            </div>
          </div>
        </section>

        {/* Panoramic Closing Bottom Banner */}
        <section className="relative overflow-hidden border-t border-[rgba(198,165,92,0.4)] min-h-[340px] sm:min-h-[400px] flex items-center px-4 py-16 text-center text-[var(--ivory)] sm:px-6 lg:px-8 lg:py-24">
          <div className="absolute inset-0 pointer-events-none overflow-hidden">
            <Image
              src="/foundations/golf/scenic-beach-links.jpg"
              alt="Coastal links golf course fairway along ocean cliffside at sunset"
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
              Next Action
            </p>
            <h2 className="mt-4 font-serif text-4xl leading-tight text-white sm:text-5xl lg:text-6xl">
              Elevate Your Mental Game On The Course
            </h2>
            <p className="mt-6 max-w-2xl mx-auto text-lg leading-8 text-[#d8cdbb]">
              Whether you are an individual competitor looking to break through tournament plateaus or a golf club seeking an exceptional member clinic, connect with Lornette Daye to discuss upcoming programs.
            </p>
            <div className="mt-9 flex flex-col justify-center gap-4 sm:flex-row">
              <CTAButton href="/book">INQUIRE ABOUT GOLF PROGRAMS</CTAButton>
              <CTAButton
                href="/foundations/clubs"
                variant="secondary"
                className="border-white/30 text-white hover:bg-white/10"
              >
                FOR CLUBS & CLINICS
              </CTAButton>
            </div>
          </div>
        </section>
      </main>
    </PageShell>
  );
}
