import Image from "next/image";
import { CalendarCheck } from "lucide-react";
import {
  AudiencePathways,
  type AudiencePathway,
} from "@/components/AudiencePathways";
import { BlogCard } from "@/components/BlogCard";
import { CTAButton } from "@/components/CTAButton";
import { HeroSplit } from "@/components/HeroSplit";
import { HomepageReelTheater } from "@/components/HomepageReelTheater";
import { ImageFrame } from "@/components/ImageFrame";
import { MetricStrip } from "@/components/MetricStrip";
import { NewsletterBand } from "@/components/NewsletterBand";
import { PageShell } from "@/components/PageShell";
import { SectionHeader } from "@/components/SectionHeader";
import { TestimonialCard } from "@/components/TestimonialCard";
import { TopicCard } from "@/components/TopicCard";
import {
  audienceTypes,
  images,
  bookListings,
  mediaItems,
  posts,
  services,
  speakerKitDownloads,
  speakerSubmissionProfile,
  siteCopy,
  testimonials,
} from "@/content/site";

function topic(title: string) {
  const service = services.find((item) => item.title === title);

  if (!service) {
    throw new Error(`Missing homepage service topic: ${title}`);
  }

  return service;
}

function claim(label: string) {
  const verifiedClaim = siteCopy.verifiedClaims.find((item) => item === label);

  if (!verifiedClaim) {
    throw new Error(`Missing verified homepage claim: ${label}`);
  }

  return verifiedClaim;
}

const audiencePathways: AudiencePathway[] = [
  {
    audience: audienceTypes[0],
    title: "Universities planning leadership, resilience, or purpose-driven programming.",
    description:
      "Use the speaker reel, keynote platform, and student-ready mentorship topics to review fit before moving to availability.",
    primaryHref: "/speaking",
    topics: [
      topic("Public Speaking"),
      topic("Leadership Development"),
      topic("Mentorship and Youth Development"),
    ],
    proofPoints: [
      claim("Professional Keynote Speaker"),
      claim("Certified Transformational Speaker"),
      claim("Author"),
    ],
  },
  {
    audience: audienceTypes[1],
    title: "Schools looking for confidence, discipline, and practical motivation.",
    description:
      "Start with mentorship and youth development, then add keynote or athlete-performance programming where the room needs it.",
    primaryHref: "/mentorship",
    topics: [
      topic("Mentorship and Youth Development"),
      topic("Public Speaking"),
      topic("Athlete & Performance Coaching"),
    ],
    proofPoints: [
      claim("Youth Leader & Mentor"),
      claim("Certified Transformational Speaker"),
      claim("Author"),
    ],
  },
  {
    audience: audienceTypes[2],
    title: "Athletic associations reviewing mindset, discipline, and performance coaching.",
    description:
      "Pair Lornette's elite-athlete story with practical coaching themes for athletes, coaches, and performance-focused teams.",
    primaryHref: "/athlete-coaching",
    topics: [
      topic("Athlete & Performance Coaching"),
      topic("Resilience & Mindset Coaching"),
      topic("Public Speaking"),
    ],
    proofPoints: [
      claim("Olympic-level Athlete & Coach"),
      claim("Canadian National Sprint Champion"),
      claim("National Coach"),
    ],
  },
  {
    audience: audienceTypes[3],
    title: "Nonprofit organizations creating room for resilience, belonging, and service.",
    description:
      "Lead with a keynote or inclusion conversation, then deepen the work with mentorship and youth-development pathways.",
    primaryHref: "/programs",
    topics: [
      topic("Public Speaking"),
      topic("Diversity & Inclusion"),
      topic("Mentorship and Youth Development"),
    ],
    proofPoints: [
      claim("Diversity Award Winner"),
      claim("Youth Leader & Mentor"),
      claim("Author"),
    ],
  },
  {
    audience: audienceTypes[4],
    title: "Government agencies planning inclusion, leadership, or public-sector team sessions.",
    description:
      "Review the inclusion and leadership pathways alongside Lornette's speaker materials before starting an inquiry.",
    primaryHref: "/inclusion",
    topics: [
      topic("Diversity & Inclusion"),
      topic("Leadership Development"),
      topic("Public Speaking"),
    ],
    proofPoints: [
      claim("Diversity Award Winner"),
      claim("Certified Transformational Speaker"),
      claim("Project Manager"),
    ],
  },
  {
    audience: audienceTypes[5],
    title: "Corporate teams building resilient leadership and stronger performance habits.",
    description:
      "Use the reel for presence, then review leadership, inclusion, and keynote options for the event brief.",
    primaryHref: "/leadership",
    topics: [
      topic("Leadership Development"),
      topic("Diversity & Inclusion"),
      topic("Public Speaking"),
    ],
    proofPoints: [
      claim("Professional Keynote Speaker"),
      claim("Project Manager"),
      claim("Certified Transformational Speaker"),
    ],
  },
];

export default function Home() {
  return (
    <PageShell>
      <main>
        <HeroSplit
          eyebrow="Transformational speaker message"
          title={siteCopy.homepageHeadline}
          body={`${siteCopy.mainMessage} ${siteCopy.homepageSubheadline}. ${siteCopy.homepageIntro}`}
          image={images.heroPortrait}
          primaryLabel="Book Lornette"
          secondaryLabel="Watch Speaker Reel"
          secondaryHref="/media"
          video={mediaItems[0]}
        />

        <section className="bg-[var(--ink)] px-4 py-10 text-[var(--ivory)] sm:px-6 lg:px-8">
          <div className="mx-auto grid max-w-7xl gap-6 lg:grid-cols-[0.28fr_1fr_0.32fr] lg:items-center">
            <p className="text-xs font-bold uppercase tracking-[0.24em] text-[var(--champagne)]">
              Main Message
            </p>
            <p className="font-serif text-3xl leading-tight text-balance sm:text-4xl lg:text-5xl">
              {siteCopy.mainMessage}
            </p>
            <div className="flex flex-col gap-3 sm:flex-row lg:flex-col">
              <CTAButton href="/speaking">Explore The Message</CTAButton>
              <CTAButton
                href="/media"
                variant="secondary"
                className="border-white/25 text-[var(--ivory)] hover:border-[var(--champagne)] hover:text-[var(--champagne)]"
              >
                Watch Reel
              </CTAButton>
            </div>
          </div>
        </section>

        <HomepageReelTheater video={mediaItems[0]} />

        <AudiencePathways pathways={audiencePathways} />

        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <div className="flex flex-col gap-6 lg:flex-row lg:items-end lg:justify-between">
              <SectionHeader
                eyebrow="Signature Topics"
                title="A speaker platform built around proof, presence, and planner clarity."
                body="Every path keeps the essentials visible: the reel, signature topics, audience outcomes, and a clear route to inquiry."
              />
              <CTAButton href="/speaking" variant="secondary">
                Explore Speaking
              </CTAButton>
            </div>
            <div className="mt-12 grid gap-5 md:grid-cols-2 lg:grid-cols-4">
              {services.slice(0, 4).map((service) => (
                <TopicCard key={service.title} title={service.title} body={service.body} href={service.href} />
              ))}
            </div>
          </div>
        </section>

        <MetricStrip />

        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto grid max-w-7xl gap-10 lg:grid-cols-[0.9fr_1.1fr] lg:items-center">
            <div>
              <SectionHeader
                eyebrow="Recognition & Authority"
                title="Elite athletic credibility, national coaching leadership, and award-recognized community impact."
                body="For speaker bureaus and event planners, Lornette's platform is grounded in lived achievement: national sprint titles, decades of coaching, authorship, diversity recognition, and selected engagements across schools, community organizations, podcasts, and leadership rooms."
              />
              <div className="mt-8 grid gap-3 sm:grid-cols-2">
                {speakerSubmissionProfile.recognitionHighlights.slice(0, 4).map((item) => (
                  <div key={item} className="border-l-2 border-[var(--champagne)] bg-white px-4 py-3 text-sm font-semibold leading-6 text-[#62594d]">
                    {item}
                  </div>
                ))}
              </div>
              <div className="mt-8 flex flex-col gap-3 sm:flex-row">
                <CTAButton href="/recognition">View Awards & Recognition</CTAButton>
                <CTAButton href="/books" variant="secondary">
                  View Authored Books
                </CTAButton>
              </div>
            </div>
            <ImageFrame image={images.recognitionDiversityAward} ratio="aspect-[5/4]" />
          </div>
        </section>

        <section className="bg-[var(--sand)] px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <SectionHeader
              eyebrow="Impact"
              title="What people are saying."
              body="Testimonials are drawn from provided brand materials and kept separate from media proof claims."
            />
            <div className="mt-12 grid gap-6 md:grid-cols-2 xl:grid-cols-4">
              {testimonials.map((testimonial) => (
                <TestimonialCard
                  key={testimonial.name}
                  quote={testimonial.excerpt}
                  name={testimonial.name}
                  context={testimonial.context}
                  category={testimonial.category}
                />
              ))}
            </div>
          </div>
        </section>

        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto grid max-w-7xl gap-10 lg:grid-cols-[0.82fr_1.18fr] lg:items-start">
            <div>
              <SectionHeader
                eyebrow="Media & Community References"
                title="A brand-provided reference collage for planner review."
                body="The collage is presented as a single brand asset while final media permissions and individual logo usage are confirmed."
              />
              <div className="mt-8 flex gap-3">
                <CTAButton href="/impact">View Impact</CTAButton>
                <CTAButton href="/speaker-kit" variant="secondary">Speaker Kit</CTAButton>
              </div>
            </div>
            <div className="border border-[var(--line)] bg-white p-4">
              <Image
                src={images.featuredOn.src}
                alt={images.featuredOn.alt}
                unoptimized
                className="h-auto w-full"
                sizes="(max-width: 768px) 92vw, 720px"
              />
            </div>
          </div>
        </section>

        <section className="bg-[var(--ink)] px-4 py-16 text-[var(--ivory)] sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <div className="grid gap-10 lg:grid-cols-[0.92fr_1.08fr] lg:items-end">
              <div>
                <p className="text-xs font-bold uppercase tracking-[0.28em] text-[var(--champagne)]">
                  Speaker Assets
                </p>
                <h2 className="mt-4 max-w-3xl font-serif text-5xl leading-tight text-balance text-white sm:text-6xl">
                  A cleaner planner kit for booking, promoting, and preparing the room.
                </h2>
                <p className="mt-5 max-w-2xl text-base leading-8 text-[#d8cdbb]">
                  Event teams can review Lornette&apos;s reel, download planning materials, and connect the message to books, keynotes, and audience outcomes without sorting through crowded graphics.
                </p>
              </div>

              <div className="border border-white/10 bg-white/[0.04] p-6 shadow-[0_24px_90px_rgba(0,0,0,0.24)]">
                <p className="text-xs font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
                  Best starting point
                </p>
                <div className="mt-5 grid gap-4 sm:grid-cols-3">
                  {[
                    {
                      title: "Speaker Reel",
                      meta: mediaItems[0].duration ? `${mediaItems[0].duration} preview` : "Preview",
                      href: "/media",
                    },
                    {
                      title: "One-Sheet",
                      meta: "Planner overview",
                      href: speakerKitDownloads.find((item) => item.id === "speaker-one-sheet")?.href ?? "/speaker-kit",
                    },
                    {
                      title: "Books",
                      meta: `${bookListings.length} PDF resources`,
                      href: "/books",
                    },
                  ].map((asset) => (
                    <a
                      key={asset.title}
                      href={asset.href}
                      className="group border border-white/12 bg-[var(--ivory)] px-5 py-4 text-[var(--ink)] transition hover:-translate-y-0.5 hover:border-[var(--champagne)] hover:bg-white"
                    >
                      <span className="block text-[0.68rem] font-bold uppercase tracking-[0.18em] text-[var(--gold-dark)]">
                        {asset.meta}
                      </span>
                      <span className="mt-3 block font-serif text-2xl leading-tight">
                        {asset.title}
                      </span>
                      <span className="mt-5 block text-xs font-bold uppercase tracking-[0.16em] text-[var(--gold-dark)]">
                        Open asset
                      </span>
                    </a>
                  ))}
                </div>
              </div>
            </div>

            <div className="mt-12 grid gap-6 lg:grid-cols-[0.9fr_1.1fr]">
              <div className="grid gap-4 sm:grid-cols-2">
                <div className="relative overflow-hidden border border-white/10 bg-black/25 p-3">
                  <ImageFrame
                    image={images.diversityAwardAcceptance}
                    ratio="aspect-[4/5]"
                    framed={false}
                    sizes="(max-width: 768px) 92vw, 360px"
                  />
                  <div className="absolute inset-x-3 bottom-3 bg-gradient-to-t from-black/82 to-transparent p-5">
                    <p className="text-xs font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
                      Recognition Moment
                    </p>
                    <p className="mt-2 font-serif text-2xl leading-tight text-white">
                      Diversity Awards acceptance.
                    </p>
                  </div>
                </div>
                <div className="relative overflow-hidden border border-white/10 bg-black/25 p-3">
                  <ImageFrame
                    image={images.podcastCard}
                    ratio="aspect-[4/5]"
                    framed={false}
                    sizes="(max-width: 768px) 92vw, 360px"
                  />
                  <div className="absolute inset-x-3 bottom-3 bg-gradient-to-t from-black/82 to-transparent p-5">
                    <p className="text-xs font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
                      Media Reference
                    </p>
                    <p className="mt-2 font-serif text-2xl leading-tight text-white">
                      Podcast and interview support.
                    </p>
                  </div>
                </div>
              </div>

              <div className="border border-white/10 bg-[linear-gradient(135deg,rgba(250,247,240,0.98),rgba(232,221,203,0.9))] p-6 text-[var(--ink)] shadow-[0_24px_90px_rgba(0,0,0,0.24)] sm:p-8">
                <p className="text-xs font-bold uppercase tracking-[0.24em] text-[var(--gold-dark)]">
                  What planners can pull quickly
                </p>
                <div className="mt-6 grid gap-3 sm:grid-cols-2">
                  {speakerKitDownloads.slice(0, 6).map((item) => (
                    <a
                      key={item.id}
                      href={item.href}
                      download
                      className="flex min-h-16 items-center justify-between gap-4 border border-[rgba(155,118,46,0.24)] bg-white/70 px-4 py-3 transition hover:border-[var(--champagne)] hover:bg-white"
                    >
                      <span className="font-semibold text-[var(--charcoal)]">{item.title}</span>
                      <span className="text-xs font-bold uppercase tracking-[0.14em] text-[var(--gold-dark)]">
                        Download
                      </span>
                    </a>
                  ))}
                </div>
                <div className="mt-8 flex flex-col gap-3 sm:flex-row">
                  <CTAButton href="/speaker-kit">Open Full Speaker Kit</CTAButton>
                  <CTAButton href="/book" variant="secondary">Book Lornette</CTAButton>
                </div>
              </div>
            </div>
          </div>
        </section>

        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <div className="flex flex-col gap-6 lg:flex-row lg:items-end lg:justify-between">
              <SectionHeader
                eyebrow="From The Blog"
                title="Insights for resilience, leadership, and performance."
              />
              <CTAButton href="/blog" variant="secondary">All Articles</CTAButton>
            </div>
            <div className="mt-10 grid gap-6 md:grid-cols-3">
              {posts.slice(0, 3).map((post) => (
                <BlogCard key={post.slug} post={post} />
              ))}
            </div>
          </div>
        </section>

        <NewsletterBand />

        <section
          id="book"
          className="bg-[var(--ink)] px-4 py-16 text-[var(--ivory)] sm:px-6 lg:px-8 lg:py-24"
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
                Whether your audience needs resilience, confidence, faith, leadership, healing, or future-ready tools, Lornette delivers keynote experiences that inspire people to rise, believe again, and take action.
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
                Fast Planner Path
              </h3>
              <ol className="mt-6 grid gap-4 text-sm leading-7 text-[#d8cdbb]">
                {[
                  "Share the event date, location, format, audience, and goals.",
                  "Choose the keynote, workshop, or faith-based experience that fits.",
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
              <div className="mt-8">
                <CTAButton href="/book" className="w-full">
                  Start Booking Inquiry
                </CTAButton>
              </div>
            </div>
          </div>
        </section>
      </main>
    </PageShell>
  );
}
