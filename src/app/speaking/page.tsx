import Image from "next/image";
import Link from "next/link";
import {
  ArrowRight,
  BadgeCheck,
  BookOpenCheck,
  CalendarCheck,
  CheckCircle2,
  ChevronRight,
  Clock3,
  Download,
  HandHeart,
  Mic2,
  Play,
  Sparkles,
  Target,
  UsersRound,
  Video,
} from "lucide-react";

import { CTAButton } from "@/components/CTAButton";
import { PageShell } from "@/components/PageShell";
import { SectionHeader } from "@/components/SectionHeader";
import { VideoCard } from "@/components/VideoCard";
import { createMetadata, images, mediaItems, speakerSubmissionProfile } from "@/content/site";

export const metadata = createMetadata(
  "Lornette Daye Speaking | Resilience, Change & Elite Athlete Mindset",
  "Book Lornette Daye for keynote sessions on resilience, navigating disappointment, regaining perspective after adversity, and lessons from her journey as an elite athlete.",
  "/speaking",
);

const anchorLinks = [
  { label: "Topics", href: "#topics" },
  { label: "Videos", href: "#videos" },
  { label: "Audiences", href: "#audiences" },
  { label: "Formats", href: "#formats" },
  { label: "Book", href: "#book" },
];

const heroStats = [
  "Former National Track Champion",
  "National Coach",
  "Diversity Award Winner",
  "Motivational Speaker",
];

const speakingPillars = [
  {
    number: "01",
    icon: Target,
    title: "Road to the Olympics",
    keynoteName: "Road to the Olympics: Lessons Learned as an Elite Athlete",
    promise:
      "For audiences who want to achieve meaningful goals while learning how to navigate obstacles, adversity, perspective, and self-esteem along the way.",
    description:
      "Everybody wants to achieve great things, but many people are not equipped with the tools to overcome the obstacles that come with pursuing a goal. In this session, Lornette draws from her personal journey to help audiences rise above adversity, maintain perspective, protect their self-worth, and stay connected to what matters as they move toward the life and goals they are called to pursue.",
    bestFor: ["Corporate teams", "Youth programs", "Faith-based gatherings"],
    outcomes: [
      "Understand how childhood and professional foundations can shape personal pursuits",
      "Develop strategies for maintaining a positive self-view and staying motivated",
      "See how the journey toward achievement can build character and transformation",
      "Learn how adversity can strengthen perspective, discipline, and resilience",
      "Discover the role of giving in maintaining clarity and focus",
    ],
    video: "Video Clip: Road to the Olympics",
    cta: "Book This Keynote",
  },
  {
    number: "02",
    icon: Sparkles,
    title: "What Happens When It Doesn't Work?",
    keynoteName: "What Happens When It Doesn't Work?: Navigating Change and Disappointment",
    promise:
      "For audiences facing unexpected change, failure, transition, or disappointment who need practical tools to regain confidence and move forward.",
    description:
      "When the unexpected hits, it can be devastating. A market shift, layoff, personal issue, or major disappointment can leave people off balance and questioning themselves, their direction, and their future. This session helps audiences understand that change does not have to be the end of the story. Lornette shares emotional and professional principles that equip people to grow through the unexpected and make the most of what comes next.",
    bestFor: ["Corporate teams", "Leadership groups", "Career events"],
    outcomes: [
      "Develop resilience and mental flexibility during failure or unexpected change",
      "Reframe challenges as opportunities for growth",
      "Strengthen self-awareness around personal triggers and responses to change",
      "Build supportive networks for difficult transitions",
      "Communicate with greater transparency and trust during uncertainty",
      "Create a proactive mindset that embraces change rather than fearing it",
    ],
    video: "Video Clip: What Happens When It Doesn't Work?",
    cta: "Bring This Message to Your Audience",
  },
  {
    number: "03",
    icon: HandHeart,
    title: "Staying Grounded",
    keynoteName: "Staying Grounded: Regaining Perspective After Adversity",
    promise:
      "For audiences who feel worn down by obstacles, setbacks, or disappointment and need to pause, process, and reconnect with purpose.",
    description:
      "In the face of obstacles and adversity, it is easy to lose sight of purpose and forget why we were striving in the first place. Many people either get stuck in a rut or force themselves to keep going without truly processing what happened. This session explores the importance of pausing to assess our experiences instead of simply pushing through pain. By acknowledging emotions with honesty and care, audiences can begin to regain clarity, reconnect with identity, and move forward with renewed strength.",
    bestFor: ["Women's events", "Faith-based gatherings", "Retreats"],
    outcomes: [
      "Learn techniques for assessing and processing emotional pain",
      "Reconnect with identity and strengthen self-worth",
      "Understand the role of gratitude in resilience and healing",
      "Recognize the positive aspects of life that remain during difficulty",
      "Regain perspective after setbacks, obstacles, and disappointment",
    ],
    video: "Video Clip: Staying Grounded",
    cta: "Book This Transformational Talk",
  },
];

const videoProof = [
  "Speaker Reel",
  "Road to the Olympics",
  "Navigating Change and Disappointment",
  "Staying Grounded After Adversity",
];

const outcomes = [
  "Stronger resilience through setbacks",
  "Healthier perspective under pressure",
  "Practical tools for change and disappointment",
  "Renewed self-worth and motivation",
  "Clearer communication during uncertainty",
  "Grounded confidence to keep moving forward",
];

const eventFits = [
  "Keynote conferences",
  "Corporate teams and leadership groups",
  "Professional development events",
  "Youth programs and schools",
  "Women's events and retreats",
  "Athletic teams and coaching environments",
  "Community organizations",
  "Faith-based gatherings",
  "Church events",
  "Panels and workshops",
];

const bookingOptions = [
  {
    icon: Mic2,
    title: "Keynote Experience",
    description:
      "A powerful main-stage message designed to inspire, equip, and move audiences to action.",
    formats: "30, 45, or 60 minutes",
  },
  {
    icon: BookOpenCheck,
    title: "Workshop Experience",
    description:
      "A deeper interactive session with teaching, reflection, discussion, and practical takeaways.",
    formats: "60, 90, or half-day",
  },
  {
    icon: HandHeart,
    title: "Tailored Audience Experience",
    description:
      "A message adapted for faith-based gatherings, schools, women's events, community rooms, or professional audiences.",
    formats: "Church service, retreat, school session, or women's gathering",
  },
];

const credibility = [
  "Elite athlete experience",
  "Powerful personal story",
  "Faith-based, youth, women's, athletic, and professional audience options",
  "Topics for achievement, adversity, change, disappointment, and perspective",
  "Personal experience turning pressure and setbacks into growth",
  "Customizable keynotes and workshops",
  "Strong focus on audience outcomes",
];

const proofCards = [
  {
    title: "Organizer Feedback",
    body: "Testimonial coming soon",
  },
  {
    title: "Audience Response",
    body: "Words From the Room",
  },
  {
    title: "Video Testimonial",
    body: "Video Coming Soon",
  },
];

function PlaceholderVideo({
  title,
  large = false,
}: {
  title: string;
  large?: boolean;
}) {
  return (
    <div
      className={`group relative overflow-hidden border border-white/15 bg-white/[0.055] shadow-[0_24px_90px_rgba(0,0,0,0.22)] ${
        large ? "min-h-[390px]" : "min-h-[128px]"
      }`}
    >
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_30%_18%,rgba(198,165,92,0.35),transparent_34%),linear-gradient(135deg,rgba(255,255,255,0.12),transparent_52%)]" />
      <div className="relative flex h-full min-h-[inherit] flex-col justify-between p-5">
        <div className="flex items-center justify-between gap-4">
          <span className="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-[0.2em] text-[var(--champagne)]">
            <Video size={15} aria-hidden="true" />
            Video Coming Soon
          </span>
          <span className="inline-flex h-10 w-10 items-center justify-center rounded-full border border-white/20 text-white/70">
            <Play size={15} fill="currentColor" aria-hidden="true" />
          </span>
        </div>
        <div>
          <p className={large ? "font-serif text-4xl leading-tight text-white" : "font-serif text-2xl text-white"}>
            {title}
          </p>
          <p className="mt-2 text-sm leading-6 text-[#d8cdbb]">
            More speaking moments, interviews, and event highlights can be added here as Lornette&apos;s media library grows.
          </p>
        </div>
      </div>
    </div>
  );
}

function SectionLabel({ children }: { children: React.ReactNode }) {
  return (
    <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--gold-dark)]">
      {children}
    </p>
  );
}

export default function SpeakingPage() {
  const profile = speakerSubmissionProfile;

  return (
    <PageShell>
      <main>
        <section
          id="speaking-hero"
          className="relative scroll-mt-28 overflow-hidden border-b border-[var(--line)] bg-[var(--ivory)] px-4 py-14 sm:px-6 lg:px-8 lg:py-16"
        >
          <div className="mx-auto grid max-w-7xl gap-10 lg:grid-cols-[minmax(0,0.96fr)_minmax(420px,0.84fr)] lg:items-start">
            <div className="relative z-10">
              <SectionLabel>Speaking / Keynotes</SectionLabel>
              <h1 className="mt-5 max-w-4xl font-serif text-[3rem] leading-[0.96] text-balance text-[var(--ink)] sm:text-6xl lg:text-[4.65rem] xl:text-[5rem]">
                Speaking That Moves People From Inspiration to Action
              </h1>
              <p className="mt-6 max-w-2xl text-xl leading-8 text-[var(--gold-dark)]">
                Lornette Daye delivers powerful keynote experiences that help audiences rise through adversity, navigate change, and regain perspective when life or leadership does not go as planned.
              </p>
              <div className="mt-7 flex flex-col gap-3 sm:flex-row">
                <CTAButton href="/book">Book Lornette to Speak</CTAButton>
                <CTAButton href="/media" variant="secondary">
                  Watch Speaker Reel
                </CTAButton>
              </div>
              <p className="mt-5 max-w-2xl text-base leading-8 text-[#675d50] sm:text-lg">
                Through her journey as an elite athlete, transformational coach, and purpose-driven communicator, Lornette brings messages that are both deeply personal and practically empowering. Her talks are designed to help audiences leave stronger, clearer, and ready to take action.
              </p>
              <p className="mt-5 max-w-2xl border-l-2 border-[var(--champagne)] pl-4 font-serif text-2xl leading-snug text-[var(--ink)]">
                Clear, heartfelt messages for people who need courage, perspective, and a practical way forward.
              </p>
              <div className="mt-9 grid gap-3 border-y border-[rgba(198,165,92,0.34)] py-5 sm:grid-cols-2 lg:grid-cols-4">
                {heroStats.map((stat) => (
                  <div key={stat} className="flex items-center gap-2 text-sm font-bold text-[var(--charcoal)]">
                    <BadgeCheck size={17} aria-hidden="true" className="shrink-0 text-[var(--gold-dark)]" />
                    {stat}
                  </div>
                ))}
              </div>
              <p className="mt-5 max-w-2xl text-sm leading-7 text-[#675d50]">
                Lornette speaks to faith-based gatherings, corporate events, youth programs, women&apos;s events, athletic organizations, schools, retreats, and community rooms.
              </p>
            </div>

            <div className="relative z-10">
              <div className="absolute -right-8 -top-8 hidden h-36 w-36 border border-[rgba(198,165,92,0.34)] lg:block" />
              <div className="relative border border-[rgba(198,165,92,0.55)] bg-white p-3 shadow-[0_36px_120px_rgba(23,20,18,0.14)]">
                <VideoCard
                  {...mediaItems[0]}
                  title="Watch Lornette in Action"
                  summary="See Lornette&apos;s delivery style, tone, presence, and audience connection in action."
                  featured
                  className="shadow-none"
                />
              </div>
              <div className="mt-4 grid grid-cols-2 gap-3">
                <Link
                  href="/speaker-kit"
                  className="flex min-h-14 items-center justify-center gap-2 border border-[rgba(155,118,46,0.42)] bg-white px-4 text-center text-xs font-bold uppercase tracking-[0.14em] text-[var(--ink)] transition hover:border-[var(--champagne)] hover:bg-[rgba(198,165,92,0.1)]"
                >
                  <Download size={16} aria-hidden="true" />
                  Speaker Kit
                </Link>
                <Link
                  href="#topics"
                  className="flex min-h-14 items-center justify-center gap-2 border border-[rgba(155,118,46,0.42)] bg-white px-4 text-center text-xs font-bold uppercase tracking-[0.14em] text-[var(--ink)] transition hover:border-[var(--champagne)] hover:bg-[rgba(198,165,92,0.1)]"
                >
                  <ChevronRight size={16} aria-hidden="true" />
                  Explore Topics
                </Link>
              </div>
            </div>
          </div>
        </section>

        <nav
          aria-label="Speaking page sections"
          className="sticky top-[72px] z-30 border-y border-[rgba(198,165,92,0.28)] bg-[rgba(250,247,240,0.94)] px-4 backdrop-blur-xl sm:px-6 lg:px-8"
        >
          <div className="mx-auto flex max-w-7xl gap-2 overflow-x-auto py-3">
            {anchorLinks.map((link) => (
              <a
                key={link.href}
                href={link.href}
                className="min-h-11 shrink-0 border border-[rgba(155,118,46,0.28)] bg-white/75 px-5 py-3 text-xs font-bold uppercase tracking-[0.16em] text-[var(--ink)] transition hover:border-[var(--champagne)] hover:bg-white"
              >
                {link.label}
              </a>
            ))}
          </div>
        </nav>

        <section className="border-b border-[var(--line)] bg-white px-4 py-12 sm:px-6 lg:px-8">
          <div className="mx-auto grid max-w-7xl gap-8 lg:grid-cols-[0.82fr_1.18fr] lg:items-start">
            <div>
              <SectionLabel>Speaker Bureau Snapshot</SectionLabel>
              <h2 className="mt-4 font-serif text-4xl leading-tight text-[var(--ink)] sm:text-5xl">
                A quick look at Lornette&apos;s voice, story, and credibility.
              </h2>
              <p className="mt-5 max-w-2xl text-base leading-8 text-[#675d50]">
                {profile.role}. Traveling from {profile.travelingFrom}. Lornette&apos;s speaking platform connects elite athletic achievement, national coaching leadership, lived resilience, authorship, faith, and community impact.
              </p>
            </div>
            <div className="grid gap-4 md:grid-cols-3">
              <div className="self-start border border-[rgba(198,165,92,0.38)] bg-[var(--ivory)] p-5">
                <p className="text-xs font-bold uppercase tracking-[0.18em] text-[var(--gold-dark)]">
                  Recent Speaking
                </p>
                <div className="mt-4 grid gap-3">
                  {profile.videoLinks.map((video) => (
                    <a
                      key={video.href}
                      href={video.href}
                      target="_blank"
                      rel="noreferrer"
                      className="inline-flex items-center justify-between gap-3 text-sm font-bold text-[var(--ink)] underline-offset-4 hover:underline"
                    >
                      {video.label}
                      <span className="sr-only"> opens in a new tab</span>
                      <ArrowRight size={15} aria-hidden="true" className="text-[var(--gold-dark)]" />
                    </a>
                  ))}
                </div>
              </div>
              <div className="border border-[rgba(198,165,92,0.38)] bg-[var(--ivory)] p-5">
                <p className="text-xs font-bold uppercase tracking-[0.18em] text-[var(--gold-dark)]">
                  Engagements
                </p>
                <ul className="mt-4 grid gap-2 text-sm leading-6 text-[var(--charcoal)]">
                  {profile.selectedSpeakingEngagements.map((item) => (
                    <li key={item} className="flex gap-2">
                      <CheckCircle2 size={15} aria-hidden="true" className="mt-1 shrink-0 text-[var(--gold-dark)]" />
                      {item}
                    </li>
                  ))}
                </ul>
              </div>
              <div className="border border-[rgba(198,165,92,0.38)] bg-[var(--ink)] p-5 text-[var(--ivory)]">
                <p className="text-xs font-bold uppercase tracking-[0.18em] text-[var(--champagne)]">
                  Keynote Flagship
                </p>
                <p className="mt-4 font-serif text-2xl leading-tight text-white">
                  {profile.primaryKeynote.title}
                </p>
                <p className="mt-3 text-base leading-7 text-[#d8cdbb]">
                  {profile.primaryKeynote.fit}
                </p>
              </div>
            </div>
          </div>
        </section>

        <section
          id="topics"
          className="scroll-mt-32 px-4 pb-16 pt-8 sm:px-6 lg:px-8 lg:pb-24 lg:pt-12"
        >
          <div className="mx-auto max-w-7xl">
            <div className="grid gap-10 lg:grid-cols-[0.42fr_0.58fr] lg:items-end">
              <div>
                <SectionLabel>Signature Speaking Pillars</SectionLabel>
                <h2 className="mt-4 font-serif text-5xl leading-tight text-balance text-[var(--ink)]">
                  Three Signature Sessions for Real Transformation
                </h2>
              </div>
              <p className="text-lg leading-8 text-[#675d50]">
                Each session is rooted in Lornette&apos;s personal journey, athletic discipline, coaching experience, and commitment to helping people leave with clarity, courage, and practical next steps.
              </p>
            </div>

            <div className="mt-12 grid gap-7">
              {speakingPillars.map((pillar, index) => {
                const Icon = pillar.icon;
                const pillarImage = images.speakingChampionMindset;

                return (
                  <article
                    key={pillar.title}
                    className="group overflow-hidden border border-[rgba(198,165,92,0.38)] bg-white shadow-[0_20px_90px_rgba(23,20,18,0.07)] transition duration-300 hover:-translate-y-1 hover:border-[var(--champagne)] hover:shadow-[0_30px_110px_rgba(23,20,18,0.12)]"
                  >
                    <div className={`grid gap-0 lg:grid-cols-[0.9fr_1.2fr_0.8fr] ${index % 2 === 1 ? "lg:[&>*:first-child]:order-2 lg:[&>*:nth-child(2)]:order-1" : ""}`}>
                      <div className="relative min-h-[290px] overflow-hidden bg-[var(--ink)] p-7 text-[var(--ivory)]">
                        <div className="absolute inset-0 opacity-[0.82]">
                          <Image
                            src={pillarImage.src}
                            alt={pillarImage.alt}
                            fill
                            unoptimized
                            sizes="(max-width: 1024px) 92vw, 32vw"
                            className={`object-cover ${pillarImage.crop ?? "object-center"}`}
                          />
                          <span className="absolute inset-0 bg-gradient-to-t from-black/90 via-black/50 to-black/15" />
                        </div>
                        <div className="relative flex h-full min-h-[236px] flex-col justify-between">
                          <div className="flex items-center justify-between gap-4">
                            <span
                              className="inline-flex rounded-[4px] bg-[#c5aa68] px-2 py-1 text-xs font-bold uppercase leading-none tracking-[0.26em] text-[var(--ink)] shadow-[0_8px_22px_rgba(23,20,18,0.16)]"
                            >
                              Pillar {pillar.number}
                            </span>
                            <Icon size={30} aria-hidden="true" className="text-[var(--champagne)]" />
                          </div>
                          <div>
                            <h3 className="font-serif text-4xl leading-tight text-white">
                              {pillar.title}
                            </h3>
                            <p className="mt-4 text-sm font-semibold uppercase tracking-[0.16em] text-[#d8cdbb]">
                              {pillar.keynoteName}
                            </p>
                          </div>
                        </div>
                      </div>

                      <div className="p-7 lg:p-9">
                        <p className="font-serif text-2xl leading-snug text-[var(--ink)]">
                          {pillar.promise}
                        </p>
                        <p className="mt-5 text-base leading-8 text-[#675d50]">
                          {pillar.description}
                        </p>
                        <div className="mt-7 grid gap-4 sm:grid-cols-[1fr_auto] sm:items-center">
                          <div className="border border-[var(--line)] bg-[var(--ivory)] p-4">
                            <p className="text-xs font-bold uppercase tracking-[0.18em] text-[var(--gold-dark)]">
                              Best For
                            </p>
                            <ul className="mt-2 grid gap-1.5 text-[0.96rem] leading-7 text-[#675d50]">
                              {pillar.bestFor.map((fit) => (
                                <li key={fit} className="flex gap-2">
                                  <span aria-hidden="true" className="mt-2 h-1.5 w-1.5 shrink-0 rounded-full bg-[var(--gold-dark)]" />
                                  <span>{fit}</span>
                                </li>
                              ))}
                            </ul>
                          </div>
                          <CTAButton href="/book" className="sm:self-stretch">
                            {pillar.cta}
                          </CTAButton>
                        </div>
                      </div>

                      <div className="border-t border-[var(--line)] bg-[rgba(250,247,240,0.82)] p-7 lg:border-l lg:border-t-0">
                        <p className="text-xs font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)]">
                          Attendee Results
                        </p>
                        <ul className="mt-5 grid gap-3">
                          {pillar.outcomes.map((outcome) => (
                            <li key={outcome} className="flex gap-3 text-sm leading-6 text-[var(--charcoal)]">
                              <CheckCircle2
                                size={18}
                                aria-hidden="true"
                                className="mt-0.5 shrink-0 text-[var(--gold-dark)]"
                              />
                              {outcome}
                            </li>
                          ))}
                        </ul>
                        <div className="mt-7 border border-[rgba(155,118,46,0.34)] bg-white p-4">
                          <span className="inline-flex items-center gap-2 text-xs font-bold uppercase tracking-[0.16em] text-[var(--gold-dark)]">
                            <Video size={15} aria-hidden="true" />
                            Video Area
                          </span>
                          <p className="mt-3 font-serif text-2xl text-[var(--ink)]">
                            {pillar.video}
                          </p>
                          <p className="mt-2 text-xs font-semibold uppercase tracking-[0.14em] text-[#7d7164]">
                            Video Coming Soon
                          </p>
                        </div>
                      </div>
                    </div>
                  </article>
                );
              })}
            </div>
          </div>
        </section>

        <section
          id="videos"
          className="scroll-mt-32 bg-[var(--ink)] px-4 py-16 text-[var(--ivory)] sm:px-6 lg:px-8 lg:py-24"
        >
          <div className="mx-auto max-w-7xl">
            <div className="grid gap-8 lg:grid-cols-[0.55fr_0.45fr] lg:items-end">
              <div>
                <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--champagne)]">
                  Watch Lornette in Action
                </p>
                <h2 className="mt-4 font-serif text-5xl leading-tight text-white">
                  See the Message. Feel the Presence.
                </h2>
              </div>
              <p className="text-base leading-8 text-[#d8cdbb]">
                Watch Lornette&apos;s voice, energy, story, and connection with an audience come through in these speaking moments.
              </p>
            </div>

            <div className="mt-12 grid gap-6 lg:grid-cols-[1.15fr_0.85fr]">
              <VideoCard
                {...mediaItems[0]}
                title="Speaker Reel"
                summary="Start here for Lornette&apos;s tone, pacing, message, and connection with the room."
                featured
                className="border-white/15 bg-white/[0.04]"
              />
              <div className="grid gap-4">
                {videoProof.slice(1).map((item) => (
                  <PlaceholderVideo key={item} title={item} />
                ))}
              </div>
            </div>
          </div>
        </section>

        <section
          id="audiences"
          className="scroll-mt-32 px-4 py-16 sm:px-6 lg:px-8 lg:py-24"
        >
          <div className="mx-auto grid max-w-7xl gap-12 lg:grid-cols-[0.9fr_1.1fr]">
            <div className="lg:pt-16">
              <SectionHeader
                eyebrow="Audience Experience"
                title="What Audiences Walk Away With"
                body="Lornette's talks are designed to do more than inspire for a moment. They give audiences language, courage, practical next steps, and a renewed belief in what is possible."
              />
            </div>
            <div className="grid gap-4 sm:grid-cols-2">
              {outcomes.map((outcome, index) => (
                <div
                  key={outcome}
                  className="border border-[var(--line)] bg-white p-6 shadow-[0_16px_65px_rgba(23,20,18,0.06)]"
                >
                  <span className="font-serif text-4xl text-[var(--gold-dark)]">
                    {String(index + 1).padStart(2, "0")}
                  </span>
                  <p className="mt-5 font-serif text-2xl leading-tight text-[var(--ink)]">
                    {outcome}
                  </p>
                </div>
              ))}
            </div>
          </div>
        </section>

        <section className="border-y border-[var(--line)] bg-white/70 px-4 py-16 sm:px-6 lg:px-8 lg:py-20">
          <div className="mx-auto grid max-w-7xl gap-10 lg:grid-cols-[0.35fr_0.65fr] lg:items-start">
            <div>
              <SectionLabel>Perfect For</SectionLabel>
              <h2 className="mt-4 font-serif text-5xl leading-tight text-[var(--ink)]">
                Built for Many Rooms, Customized for Each Audience
              </h2>
              <p className="mt-5 text-base leading-8 text-[#675d50]">
                Every message can be shaped for the audience, event theme, time format, and desired result.
              </p>
            </div>
            <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
              {eventFits.map((fit) => (
                <div
                  key={fit}
                  className="flex min-h-20 items-center gap-3 border border-[rgba(198,165,92,0.34)] bg-[var(--ivory)] px-4 text-sm font-bold text-[var(--charcoal)]"
                >
                  <UsersRound size={18} aria-hidden="true" className="shrink-0 text-[var(--gold-dark)]" />
                  {fit}
                </div>
              ))}
            </div>
          </div>
        </section>

        <section
          id="formats"
          className="scroll-mt-32 px-4 py-16 sm:px-6 lg:px-8 lg:py-24"
        >
          <div className="mx-auto max-w-7xl">
            <SectionHeader
              eyebrow="Booking Options"
              title="Choose the Experience That Fits Your Event"
              body="From a main-stage inspirational speaker experience to a deeper workshop or tailored gathering, each format is shaped around the people in the room."
              align="center"
            />
            <div className="mt-12 grid gap-6 lg:grid-cols-3">
              {bookingOptions.map((option) => {
                const Icon = option.icon;
                return (
                  <article
                    key={option.title}
                    className="group border border-[rgba(198,165,92,0.38)] bg-white p-7 shadow-[0_18px_80px_rgba(23,20,18,0.07)] transition hover:-translate-y-1 hover:border-[var(--champagne)]"
                  >
                    <Icon size={32} aria-hidden="true" className="text-[var(--gold-dark)]" />
                    <h3 className="mt-6 font-serif text-3xl text-[var(--ink)]">
                      {option.title}
                    </h3>
                    <p className="mt-4 text-sm leading-7 text-[#675d50]">
                      {option.description}
                    </p>
                    <div className="mt-7 flex items-center gap-3 border-t border-[var(--line)] pt-5 text-sm font-bold text-[var(--charcoal)]">
                      <Clock3 size={17} aria-hidden="true" className="text-[var(--gold-dark)]" />
                      {option.formats}
                    </div>
                  </article>
                );
              })}
            </div>
            <div className="mt-10 text-center">
              <CTAButton href="/book">Request Speaking Availability</CTAButton>
            </div>
          </div>
        </section>

        <section className="bg-[var(--sand)] px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto grid max-w-7xl gap-10 lg:grid-cols-[0.9fr_1.1fr] lg:items-center">
            <div>
              <SectionLabel>Why Lornette</SectionLabel>
              <h2 className="mt-4 font-serif text-5xl leading-tight text-balance text-[var(--ink)]">
                A Voice That Carries Strength, Warmth, and Transformation
              </h2>
              <p className="mt-5 text-lg leading-8 text-[#675d50]">
                Lornette brings a rare combination of lived experience, athletic discipline, faith, emotional depth, and practical encouragement. Her presence is warm, her message is powerful, and her focus is always on helping people leave stronger than they came.
              </p>
            </div>
            <div className="grid gap-3">
              {credibility.map((item) => (
                <div
                  key={item}
                  className="flex gap-3 border border-[rgba(198,165,92,0.38)] bg-white px-5 py-4 text-sm font-bold text-[var(--charcoal)]"
                >
                  <CheckCircle2 size={18} aria-hidden="true" className="mt-0.5 shrink-0 text-[var(--gold-dark)]" />
                  {item}
                </div>
              ))}
            </div>
          </div>
        </section>

        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <div className="grid gap-10 lg:grid-cols-[0.38fr_0.62fr] lg:items-start">
              <div>
                <SectionLabel>Audience Response</SectionLabel>
                <h2 className="mt-4 font-serif text-5xl leading-tight text-[var(--ink)]">
                  Words From the Room
                </h2>
                <p className="mt-5 text-base leading-8 text-[#675d50]">
                  These reflections show how Lornette&apos;s message lands with people who need encouragement, clarity, and a renewed sense of possibility.
                </p>
              </div>
              <div className="grid gap-5 md:grid-cols-3">
                {proofCards.map((card) => (
                  <article
                    key={card.title}
                    className="min-h-56 border border-[rgba(198,165,92,0.38)] bg-white p-6 shadow-[0_18px_70px_rgba(23,20,18,0.06)]"
                  >
                    <p className="font-serif text-3xl text-[var(--champagne)]">&ldquo;</p>
                    <h3 className="mt-4 font-serif text-2xl text-[var(--ink)]">
                      {card.title}
                    </h3>
                    <p className="mt-4 text-sm font-semibold uppercase tracking-[0.16em] text-[#7d7164]">
                      {card.body}
                    </p>
                  </article>
                ))}
              </div>
            </div>
          </div>
        </section>

        <section
          id="book"
          className="scroll-mt-32 bg-[var(--ink)] px-4 py-16 text-[var(--ivory)] sm:px-6 lg:px-8 lg:py-24"
        >
          <div className="mx-auto grid max-w-7xl gap-10 lg:grid-cols-[0.95fr_0.7fr] lg:items-center">
            <div>
              <p className="text-xs font-bold uppercase tracking-[0.26em] text-[var(--champagne)]">
                Book Lornette
              </p>
              <h2 className="mt-4 font-serif text-5xl leading-tight text-white sm:text-6xl">
                Ready to Bring Lornette&apos;s Message to Your Audience?
              </h2>
              <p className="mt-6 max-w-3xl text-lg leading-8 text-[#d8cdbb]">
                Whether your audience needs resilience, perspective, motivation, or practical tools for change and disappointment, Lornette delivers keynote experiences that inspire people to rise, regroup, and take action.
              </p>
              <p className="mt-5 text-sm font-bold uppercase tracking-[0.16em] text-[var(--champagne)]">
                Available for keynotes, workshops, conferences, retreats, schools, churches, corporate events, and community gatherings.
              </p>
              <div className="mt-8 flex flex-col gap-3 sm:flex-row">
                <CTAButton href="/book">Book Lornette to Speak</CTAButton>
                <CTAButton
                  href="/speaker-kit"
                  variant="secondary"
                  className="border-white/25 text-[var(--ivory)] hover:bg-white/10"
                >
                  Download Speaker One-Sheet
                </CTAButton>
                <CTAButton
                  href="/media"
                  variant="secondary"
                  className="border-white/25 text-[var(--ivory)] hover:bg-white/10"
                >
                  Watch Speaker Reel
                </CTAButton>
              </div>
            </div>
            <div className="border border-white/15 bg-white/[0.045] p-6 shadow-[0_30px_120px_rgba(0,0,0,0.28)]">
              <CalendarCheck size={36} aria-hidden="true" className="text-[var(--champagne)]" />
              <h3 className="mt-5 font-serif text-3xl text-white">
                Simple Booking Path
              </h3>
              <ol className="mt-6 grid gap-4 text-sm leading-7 text-[#d8cdbb]">
                {[
                  "Share the event date, location, format, audience, and goals.",
                  "Choose the keynote, workshop, or tailored audience experience that fits.",
                  "Receive next-step guidance for speaker kit, prep, and event fit.",
                ].map((item, index) => (
                  <li key={item} className="flex gap-3">
                    <span className="flex h-7 w-7 shrink-0 items-center justify-center rounded-full bg-[var(--champagne)] text-xs font-bold text-[var(--ink)]">
                      {index + 1}
                    </span>
                    {item}
                  </li>
                ))}
              </ol>
              <Link
                href="/book"
                className="mt-8 inline-flex min-h-12 w-full items-center justify-center gap-2 border border-[var(--champagne)] bg-[var(--champagne)] px-5 text-center text-sm font-bold uppercase text-[var(--ink)] transition hover:bg-[#d8b96e]"
              >
                Start Booking Inquiry
                <ArrowRight size={17} aria-hidden="true" />
              </Link>
            </div>
          </div>
        </section>
      </main>
    </PageShell>
  );
}
