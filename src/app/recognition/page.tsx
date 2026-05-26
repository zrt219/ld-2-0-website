import {
  ArrowUpRight,
  Award,
  BadgeCheck,
  BookOpenCheck,
  CheckCircle2,
  MapPin,
  Mic2,
  Plane,
  Play,
  Trophy,
} from "lucide-react";

import { CTAButton } from "@/components/CTAButton";
import { ImageFrame } from "@/components/ImageFrame";
import { PageShell } from "@/components/PageShell";
import { SectionHeader } from "@/components/SectionHeader";
import { createMetadata, images, speakerSubmissionProfile } from "@/content/site";

export const metadata = createMetadata(
  "Awards & Recognition",
  "Awards, recognition, athletic credibility, selected engagements, authored books, and bureau-ready speaker proof for Lornette Daye.",
  "/recognition",
);

const credibilityBlocks = [
  {
    title: "Elite Athlete",
    body: "Former national track champion in the 100m and 200m sprint events, with competition experience across Canada, the United States, and Europe.",
    icon: Trophy,
  },
  {
    title: "National Coach",
    body: "Decades of athlete mentorship, coaching leadership, and youth development rooted in discipline, confidence, and resilience.",
    icon: BadgeCheck,
  },
  {
    title: "Diversity Award Winner",
    body: "Recognition connected to inclusion, community impact, lived resilience, and helping people rise through adversity.",
    icon: Award,
  },
  {
    title: "Author & Speaker",
    body: "Books, keynotes, workshops, and faith-friendly messages designed for schools, leaders, teams, women, youth, and communities.",
    icon: BookOpenCheck,
  },
];

export default function RecognitionPage() {
  const profile = speakerSubmissionProfile;

  return (
    <PageShell>
      <main className="bg-[var(--ivory)]">
        <section className="relative overflow-hidden border-b border-[var(--line)] px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="absolute inset-y-0 right-0 hidden w-1/2 bg-[radial-gradient(circle_at_70%_28%,rgba(198,165,92,0.24),transparent_35%),linear-gradient(135deg,transparent,rgba(232,221,203,0.5))] lg:block" />
          <div className="relative mx-auto grid max-w-7xl gap-12 lg:grid-cols-[0.86fr_1.14fr] lg:items-center">
            <div>
              <p className="text-xs font-bold uppercase tracking-[0.32em] text-[var(--gold-dark)]">
                Awards & Recognition
              </p>
              <h1 className="mt-5 font-serif text-5xl leading-[0.96] text-[var(--ink)] sm:text-6xl lg:text-7xl">
                Credibility Forged Through Competition, Coaching, and Community.
              </h1>
              <p className="mt-7 max-w-3xl text-lg leading-8 text-[var(--charcoal)]">
                {profile.role}
              </p>
              <div className="mt-8 flex flex-col gap-3 sm:flex-row">
                <CTAButton href="/book">Request Availability</CTAButton>
                <CTAButton href="/media" variant="secondary">
                  Watch Media
                </CTAButton>
              </div>
              <div className="mt-8 flex flex-wrap gap-3 text-sm font-semibold text-[#62594d]">
                <span className="inline-flex min-h-11 items-center gap-2 border border-[rgba(198,165,92,0.35)] bg-white/70 px-4">
                  <MapPin size={17} className="text-[var(--gold-dark)]" aria-hidden="true" />
                  Traveling from {profile.travelingFrom}
                </span>
                <span className="inline-flex min-h-11 items-center gap-2 border border-[rgba(198,165,92,0.35)] bg-white/70 px-4">
                  <Mic2 size={17} className="text-[var(--gold-dark)]" aria-hidden="true" />
                  Motivational speaker and thought leader
                </span>
              </div>
            </div>
            <ImageFrame
              image={images.recognitionDiversityAward}
              priority
              ratio="aspect-[5/4]"
              sizes="(max-width: 1024px) 92vw, 58vw"
            />
          </div>
        </section>

        <section className="border-b border-[var(--line)] bg-white px-4 py-10 sm:px-6 lg:px-8">
          <div className="mx-auto grid max-w-7xl gap-4 md:grid-cols-2 lg:grid-cols-4">
            {credibilityBlocks.map((block) => {
              const Icon = block.icon;
              return (
                <article key={block.title} className="border border-[var(--line)] bg-[var(--ivory)] p-6">
                  <Icon size={30} className="text-[var(--gold-dark)]" aria-hidden="true" />
                  <h2 className="mt-5 font-serif text-2xl text-[var(--ink)]">{block.title}</h2>
                  <p className="mt-3 text-sm leading-7 text-[#675d50]">{block.body}</p>
                </article>
              );
            })}
          </div>
        </section>

        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto grid max-w-7xl gap-10 lg:grid-cols-[0.8fr_1.2fr]">
            <SectionHeader
              eyebrow="Speaker Biography"
              title="A story with weight, warmth, and real-world authority."
              body="Lornette's credibility comes from lived experience: elite competition, decades of coaching, authorship, community service, faith, and resilience."
            />
            <div className="grid gap-5">
              {profile.biography.map((paragraph) => (
                <p key={paragraph} className="border-l-2 border-[var(--champagne)] bg-white p-5 text-base leading-8 text-[#675d50]">
                  {paragraph}
                </p>
              ))}
            </div>
          </div>
        </section>

        <section className="bg-[var(--ink)] px-4 py-16 text-[var(--ivory)] sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto grid max-w-7xl gap-10 lg:grid-cols-[0.9fr_1.1fr]">
            <div>
              <p className="text-xs font-bold uppercase tracking-[0.32em] text-[var(--champagne)]">
                Signature Keynote
              </p>
              <h2 className="mt-4 font-serif text-4xl leading-tight sm:text-5xl">
                {profile.primaryKeynote.title}
              </h2>
              <p className="mt-6 text-base leading-8 text-[#d8cdbb]">
                {profile.primaryKeynote.description}
              </p>
              <p className="mt-5 border-l-2 border-[var(--champagne)] pl-4 text-sm leading-7 text-[#d8cdbb]">
                {profile.primaryKeynote.fit}
              </p>
            </div>
            <div className="border border-white/15 bg-white/[0.04] p-7">
              <h3 className="font-serif text-3xl">Attendee Results</h3>
              <ul className="mt-6 grid gap-4">
                {profile.primaryKeynote.attendeeResults.map((result) => (
                  <li key={result} className="flex gap-3 text-sm leading-7 text-[#d8cdbb]">
                    <CheckCircle2
                      size={18}
                      className="mt-1 shrink-0 text-[var(--champagne)]"
                      aria-hidden="true"
                    />
                    <span>{result}</span>
                  </li>
                ))}
              </ul>
              <div className="mt-8">
                <CTAButton href="/speaking" className="border-white/15">
                  View Speaking Page
                </CTAButton>
              </div>
            </div>
          </div>
        </section>

        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto grid max-w-7xl gap-10 lg:grid-cols-3">
              <div className="lg:col-span-1">
                <SectionHeader
                eyebrow="Recognition Highlights"
                title="Achievements that give her message depth."
                body="These highlights trace the experiences behind Lornette's voice, from athletic excellence to community impact and authored resources."
              />
            </div>
            <div className="grid gap-6 lg:col-span-2">
              <div className="grid gap-5 md:grid-cols-2">
                <article className="border border-[var(--line)] bg-white p-7">
                  <h3 className="font-serif text-3xl text-[var(--ink)]">Selected Speaking Engagements</h3>
                  <ul className="mt-6 grid gap-3">
                    {profile.selectedSpeakingEngagements.map((item) => (
                      <li key={item} className="flex gap-3 text-sm leading-7 text-[#675d50]">
                        <CheckCircle2 size={17} className="mt-1 shrink-0 text-[var(--gold-dark)]" aria-hidden="true" />
                        {item}
                      </li>
                    ))}
                  </ul>
                </article>
                <article className="border border-[var(--line)] bg-white p-7">
                  <h3 className="font-serif text-3xl text-[var(--ink)]">Recognition Highlights</h3>
                  <ul className="mt-6 grid gap-3">
                    {profile.recognitionHighlights.map((item) => (
                      <li key={item} className="flex gap-3 text-sm leading-7 text-[#675d50]">
                        <Award size={17} className="mt-1 shrink-0 text-[var(--gold-dark)]" aria-hidden="true" />
                        {item}
                      </li>
                    ))}
                  </ul>
                </article>
              </div>

              <article className="border border-[var(--line)] bg-white p-7">
                <h3 className="font-serif text-3xl text-[var(--ink)]">Video Highlights</h3>
                <div className="mt-6 grid gap-4 sm:grid-cols-2">
                  {profile.videoLinks.map((link) => (
                    <a
                      key={link.href}
                      href={link.href}
                      target="_blank"
                      rel="noreferrer"
                      className="group flex min-h-16 items-center justify-between gap-4 border border-[rgba(198,165,92,0.34)] bg-[var(--ivory)] px-5 text-sm font-bold text-[var(--ink)] transition hover:border-[var(--champagne)]"
                    >
                      <span className="inline-flex items-center gap-3">
                        <Play fill="currentColor" size={16} className="text-[var(--gold-dark)]" aria-hidden="true" />
                        {link.label}
                      </span>
                      <ArrowUpRight size={16} className="transition group-hover:-translate-y-0.5 group-hover:translate-x-0.5" aria-hidden="true" />
                    </a>
                  ))}
                </div>
              </article>

              <article className="border border-[var(--line)] bg-white p-7">
                <h3 className="font-serif text-3xl text-[var(--ink)]">Authored Books</h3>
                <div className="mt-6 grid gap-3 md:grid-cols-2">
                  {profile.authoredBooks.map((book) => (
                    <div key={book} className="border-l-2 border-[var(--champagne)] pl-4 text-sm leading-7 text-[#675d50]">
                      {book}
                    </div>
                  ))}
                </div>
                <div className="mt-7">
                  <CTAButton href="/books" variant="secondary">
                    View PDF Books for Sale
                  </CTAButton>
                </div>
              </article>

              <article className="grid gap-5 border border-[rgba(198,165,92,0.45)] bg-[linear-gradient(135deg,#fff,rgba(232,221,203,0.56))] p-7 md:grid-cols-[auto_1fr] md:items-start">
                <Plane size={34} className="text-[var(--gold-dark)]" aria-hidden="true" />
                <div>
                  <h3 className="font-serif text-3xl text-[var(--ink)]">Travel & Booking Notes</h3>
                  <p className="mt-3 text-sm leading-7 text-[#675d50]">{profile.travelRequirements}</p>
                  <div className="mt-6">
                    <CTAButton href="/book">Start Booking Inquiry</CTAButton>
                  </div>
                </div>
              </article>
            </div>
          </div>
        </section>
      </main>
    </PageShell>
  );
}
