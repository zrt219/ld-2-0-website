import Image from "next/image";
import {
  AudiencePathways,
  type AudiencePathway,
} from "@/components/AudiencePathways";
import { BlogCard } from "@/components/BlogCard";
import { CTAButton } from "@/components/CTAButton";
import { HeroSplit } from "@/components/HeroSplit";
import { ImageFrame } from "@/components/ImageFrame";
import { MetricStrip } from "@/components/MetricStrip";
import { NewsletterBand } from "@/components/NewsletterBand";
import { PageShell } from "@/components/PageShell";
import { SectionHeader } from "@/components/SectionHeader";
import { TestimonialCard } from "@/components/TestimonialCard";
import { TopicCard } from "@/components/TopicCard";
import { VideoCard } from "@/components/VideoCard";
import {
  audienceTypes,
  images,
  mediaItems,
  metrics,
  posts,
  services,
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
      "Start with the speaker reel and student-focused topics, then ask about availability when the message fits your program.",
    primaryHref: "/speaking",
    topics: [
      topic("Keynotes & Speaking"),
      topic("Resilient Leadership"),
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
      topic("Keynotes & Speaking"),
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
    title: "Athletic associations building mindset, discipline, and performance habits.",
    description:
      "Pair Lornette's elite-athlete story with practical coaching themes for athletes, coaches, and performance-focused teams.",
    primaryHref: "/athlete-coaching",
    topics: [
      topic("Athlete & Performance Coaching"),
      topic("Resilience & Mindset Coaching"),
      topic("Keynotes & Speaking"),
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
      topic("Keynotes & Speaking"),
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
      "Explore inclusion and leadership themes alongside Lornette's speaker materials before starting an inquiry.",
    primaryHref: "/inclusion",
    topics: [
      topic("Diversity & Inclusion"),
      topic("Resilient Leadership"),
      topic("Keynotes & Speaking"),
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
      "Start with the reel, then explore leadership, inclusion, and keynote options for your team.",
    primaryHref: "/leadership",
    topics: [
      topic("Resilient Leadership"),
      topic("Diversity & Inclusion"),
      topic("Keynotes & Speaking"),
    ],
    proofPoints: [
      claim("Professional Keynote Speaker"),
      claim("Project Manager"),
      claim("Certified Transformational Speaker"),
    ],
  },
];

const signatureTopicCards = [
  {
    ...services[0],
    title: "Resilience Under Pressure",
    body: "A practical reset for audiences learning to steady themselves, recover from setbacks, and take the next brave step.",
  },
  {
    ...services[1],
    title: "Women's Wellness & Purpose",
    body: "Encouragement for women navigating change, responsibility, identity, and the need to make room for rest and renewal.",
  },
  {
    ...services[2],
    title: "Belonging in Real Life",
    body: "Grounded conversations that help teams listen across difference, build trust, and make inclusion visible in everyday behavior.",
  },
  {
    ...services[3],
    title: "Burnout, Balance & Renewal",
    body: "A compassionate session for people running on empty who need healthier rhythms, clearer boundaries, and hope for what comes next.",
  },
];

export default function Home() {
  return (
    <PageShell>
      <main>
        <HeroSplit
          eyebrow="Keynotes that build resilience and purpose"
          title={siteCopy.homepageHeadline}
          body={`${siteCopy.mainMessage} ${siteCopy.homepageSubheadline}. ${siteCopy.homepageIntro}`}
          image={images.homeHeroPortrait}
          primaryLabel="Book Lornette"
          secondaryLabel="Watch Speaker Reel"
          secondaryHref="/media"
          video={mediaItems[0]}
        />

        <section className="bg-[var(--ink)] px-4 py-10 text-[var(--ivory)] sm:px-6 lg:px-8">
          <div className="mx-auto grid max-w-7xl gap-6 lg:grid-cols-[0.28fr_1fr_0.32fr] lg:items-center">
            <p className="text-xs font-bold uppercase tracking-[0.24em] text-[var(--champagne)]">
              A Message Audiences Carry Home
            </p>
            <p className="font-serif text-3xl leading-tight text-balance sm:text-4xl lg:text-5xl">
              {siteCopy.mainMessage}
            </p>
            <div className="flex flex-col gap-3 sm:flex-row lg:flex-col">
              <CTAButton href="/speaking">Explore Speaking Topics</CTAButton>
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

        <section className="bg-white px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <div className="grid gap-8 lg:grid-cols-[1.08fr_0.92fr] lg:items-stretch">
              <VideoCard
                {...mediaItems[0]}
                title="Watch Lornette in Action"
                summary="See Lornette's warmth, conviction, and practical encouragement come through as she speaks about resilience, identity, and purpose."
                featured
                className="h-full"
                featuredColumns="lg:grid lg:grid-cols-[0.95fr_1fr]"
                spaciousFeaturedContent
                featuredMediaSize="min-h-[300px] lg:min-h-[360px]"
              />
              <div>
                <div className="border border-[rgba(198,165,92,0.42)] bg-[var(--ivory)] p-7 shadow-[0_18px_70px_rgba(23,20,18,0.08)] sm:p-9 lg:p-10">
                  <p className="text-sm font-bold uppercase text-[var(--gold-dark)]">
                    For the Audience You Care About
                  </p>
                  <h2 className="mt-4 font-serif text-4xl leading-tight text-balance text-[var(--ink)] sm:text-5xl">
                    {siteCopy.homepageHeadline}
                  </h2>
                  <p className="mt-5 text-lg leading-9 text-[#675d50]">
                    {siteCopy.homepageIntro}
                  </p>
                </div>
              </div>
            </div>

            <div className="mt-8 border border-[rgba(198,165,92,0.42)] bg-[var(--ivory)] p-6 shadow-[0_18px_70px_rgba(23,20,18,0.08)] sm:p-8 lg:grid lg:grid-cols-[0.26fr_1fr] lg:items-start lg:gap-8">
              <div className="border-b border-[var(--line)] pb-5 lg:border-b-0 lg:border-r lg:pb-0 lg:pr-8">
                <p className="text-xs font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)]">
                  Signature Keynote
                </p>
              </div>
              <div className="mt-5 lg:mt-0">
                <h3 className="font-serif text-4xl leading-tight text-balance text-[var(--ink)] sm:text-5xl">
                  {speakerSubmissionProfile.primaryKeynote.title}
                </h3>
                <p className="mt-4 max-w-4xl text-lg leading-9 text-[#675d50]">
                  {speakerSubmissionProfile.primaryKeynote.description}
                </p>
              </div>
            </div>

            <div className="mt-8 border border-[rgba(198,165,92,0.42)] bg-[var(--ivory)] p-6 shadow-[0_18px_70px_rgba(23,20,18,0.08)] sm:p-8">
              <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-4">
                {metrics.slice(0, 4).map((metric) => (
                  <div key={metric.label} className="border-l-2 border-[var(--champagne)] bg-white px-4 py-3">
                    <p className="font-serif text-3xl leading-none text-[var(--ink)]">
                      {metric.value}
                    </p>
                    <p className="mt-2 text-xs font-bold uppercase leading-5 text-[#62594d]">
                      {metric.label}
                    </p>
                  </div>
                ))}
              </div>

              <div className="mt-6 flex flex-col gap-3 sm:flex-row sm:justify-center">
                <CTAButton href="/book">Inquire About Availability</CTAButton>
                <CTAButton href="/speaker-kit" variant="secondary">
                  Speaker Kit
                </CTAButton>
              </div>
            </div>
          </div>
        </section>

        <AudiencePathways pathways={audiencePathways} />

        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <div className="flex flex-col gap-6 lg:flex-row lg:items-end lg:justify-between">
              <SectionHeader
                eyebrow="Signature Topics"
                title="Topics that help people rise, reset, and lead with purpose."
                body="Lornette brings championship discipline, lived resilience, and a coach's care to conversations audiences can carry into real life."
              />
              <CTAButton href="/speaking" variant="secondary">
                Explore Speaking
              </CTAButton>
            </div>
            <div className="mt-12 grid gap-5 md:grid-cols-2 lg:grid-cols-4">
              {signatureTopicCards.map((service) => (
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
                eyebrow="Credibility & Recognition"
                title="A champion's discipline, a coach's heart, and a message people can use."
                body="Lornette's work is rooted in national sprint titles, decades of coaching, authored resources, diversity recognition, and community service. She brings lived proof to every room, helping audiences see resilience as something they can practice."
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
            <ImageFrame image={images.recognitionCommunityAwards} ratio="aspect-[5/4]" />
          </div>
        </section>

        <section className="bg-[var(--sand)] px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <SectionHeader
              eyebrow="Audience Impact"
              title="People leave feeling seen, strengthened, and ready to move."
              body="From keynote audiences to coached athletes and wellness communities, these reflections point to the same thing: Lornette meets people with honesty, hope, and practical next steps."
            />
            <div className="mt-12 grid gap-6 md:grid-cols-2 lg:grid-cols-4">
              {testimonials.map((testimonial) => (
                <TestimonialCard key={testimonial.name} {...testimonial} />
              ))}
            </div>
          </div>
        </section>

        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto grid max-w-7xl gap-10 lg:grid-cols-[0.82fr_1.18fr] lg:items-start">
            <div>
              <SectionHeader
                eyebrow="Media & Community References"
                title="Trusted in rooms built for growth, leadership, and community."
                body="Lornette's work has reached audiences through speaking engagements, media conversations, and community-centered partnerships across schools, sports, nonprofits, and public-sector spaces."
              />
              <div className="mt-8 flex flex-col gap-3 sm:flex-row">
                <CTAButton href="/impact" size="large">See Community Impact</CTAButton>
                <CTAButton href="/speaker-kit" variant="secondary" size="large">Open Speaker Kit</CTAButton>
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

        <section className="px-4 pb-16 pt-8 sm:px-6 lg:px-8 lg:pb-24 lg:pt-10">
          <div className="mx-auto max-w-7xl">
            <div className="flex flex-col gap-6 lg:flex-row lg:items-end lg:justify-between">
              <SectionHeader
                eyebrow="Speak Life Blog"
                title="Reflections for the moments that ask you to keep going."
                body="Read short, practical notes from Lornette on resilience, faith, purpose, vulnerability, and the courage to begin again."
              />
              <CTAButton href="/blog" variant="secondary">Read the Speak Life Blog</CTAButton>
            </div>
            <div className="mt-10 grid gap-6 lg:grid-cols-[1.15fr_0.85fr]">
              <div className="grid gap-6">
                {posts[0] ? (
                  <BlogCard post={posts[0]} variant="featured" headingLevel="h3" />
                ) : null}
                {posts[3] ? (
                  <BlogCard post={posts[3]} variant="compact" headingLevel="h3" />
                ) : null}
              </div>
              <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-1">
                {posts.slice(1, 3).map((post) => (
                  <BlogCard
                    key={post.slug}
                    post={post}
                    variant="compact"
                    headingLevel="h3"
                  />
                ))}
              </div>
            </div>
          </div>
        </section>

        <NewsletterBand />

        <section className="px-4 py-16 sm:px-6 lg:px-8">
          <div className="mx-auto flex max-w-7xl flex-col gap-6 border-y border-[rgba(198,165,92,0.5)] py-10 lg:flex-row lg:items-center lg:justify-between">
            <div>
              <p className="font-serif text-4xl text-[var(--ink)]">Ready to help your audience remember what they&apos;re capable of?</p>
              <p className="mt-2 text-[#675d50]">Bring Lornette Daye to your school, team, conference, or community gathering.</p>
            </div>
            <CTAButton href="/book">Start a Booking Inquiry</CTAButton>
          </div>
        </section>
      </main>
    </PageShell>
  );
}
