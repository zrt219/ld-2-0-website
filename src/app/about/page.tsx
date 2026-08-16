import { CTAButton } from "@/components/CTAButton";
import { ImageFrame } from "@/components/ImageFrame";
import { MetricStrip } from "@/components/MetricStrip";
import { PageShell } from "@/components/PageShell";
import { SectionHeader } from "@/components/SectionHeader";
import { additionalImages, createMetadata, images, siteCopy, speakerSubmissionProfile } from "@/content/site";

export const metadata = createMetadata(
  "About Lornette",
  "Purpose, performance, and impact with Lornette Daye.",
  "/about",
);

const timeline = ["Early Start", "Elite Athlete", "Coach & Mentor", "Expanding Impact", "Global Transformation"];

export default function AboutPage() {
  return (
    <PageShell>
      <main>
        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto grid max-w-7xl gap-10 lg:grid-cols-[1fr_0.8fr] lg:items-center">
            <div>
              <p className="text-sm font-bold uppercase text-[var(--gold-dark)]">
                About Lornette Daye
              </p>
              <h1 className="mt-5 font-serif text-5xl leading-tight text-balance sm:text-7xl">
                Purpose, performance, and impact.
              </h1>
              <p className="mt-6 max-w-3xl text-lg leading-8 text-[#62594d]">
                {siteCopy.biography}
              </p>
            </div>
            <ImageFrame image={images.heroPortrait} priority ratio="aspect-[4/5]" />
          </div>
        </section>
        <MetricStrip />
        <section className="border-b border-[var(--line)] bg-white px-4 py-16 sm:px-6 lg:px-8">
          <div className="mx-auto grid max-w-7xl gap-10 lg:grid-cols-[0.75fr_1.25fr]">
            <SectionHeader
              eyebrow="Bureau Biography"
              title="A credible voice for resilience, identity, faith, leadership, and community change."
              body={speakerSubmissionProfile.role}
            />
            <div className="grid gap-4">
              {speakerSubmissionProfile.biography.map((paragraph) => (
                <p key={paragraph} className="border-l-2 border-[var(--champagne)] bg-[var(--ivory)] p-5 text-sm leading-7 text-[#675d50]">
                  {paragraph}
                </p>
              ))}
            </div>
          </div>
        </section>
        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <SectionHeader eyebrow="Timeline" title="A journey of discipline. A life of impact." />
            <div className="mt-10 grid gap-4 md:grid-cols-5">
              {timeline.map((item) => (
                <article key={item} className="border border-[var(--line)] bg-white p-5">
                  <p className="font-serif text-2xl text-[var(--ink)]">{item}</p>
                  <p className="mt-3 text-sm leading-7 text-[#675d50]">
                    A chapter in Lornette&apos;s progression from sport and coaching to transformational public speaking.
                  </p>
                </article>
              ))}
            </div>
            <div className="mt-12 grid gap-8 lg:grid-cols-2">
              <ImageFrame image={additionalImages.aboutTimeline} ratio="aspect-[4/5]" />
              <div className="border border-[var(--line)] bg-white p-8">
                <SectionHeader eyebrow="Mission" title="Unlock potential. Strengthen communities. Develop leaders." body={siteCopy.mission} />
                <div className="mt-8 grid gap-3 sm:grid-cols-2">
                  {siteCopy.verifiedClaims.map((claim) => (
                    <div key={claim} className="border-l-2 border-[var(--champagne)] pl-3 text-sm font-semibold">
                      {claim}
                    </div>
                  ))}
                </div>
                <div className="mt-8 border-t border-[var(--line)] pt-6">
                  <p className="font-serif text-3xl">Proud One Woman Member Speaker</p>
                  <p className="mt-3 text-sm leading-7 text-[#675d50]">
                    Displayed as a membership or affiliation badge only, not as an endorsement claim.
                  </p>
                </div>
                <div className="mt-8">
                  <div className="flex flex-col gap-3 sm:flex-row">
                    <CTAButton href="/recognition">Awards & Recognition</CTAButton>
                    <CTAButton href="/book" variant="secondary">Book Lornette</CTAButton>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>
    </PageShell>
  );
}
