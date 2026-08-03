import { CTAButton } from "@/components/CTAButton";
import { AboutGallery } from "@/components/AboutGallery";
import { MetricStrip } from "@/components/MetricStrip";
import { PageShell } from "@/components/PageShell";
import { SectionHeader } from "@/components/SectionHeader";
import { aboutGallerySlides } from "@/content/aboutGallery";
import { createMetadata, siteCopy, speakerSubmissionProfile } from "@/content/site";

export const metadata = createMetadata(
  "About Lornette",
  "Purpose, performance, and impact with Lornette Daye.",
  "/about",
);

const timeline = [
  {
    title: "Early Start",
    description:
      "After moving from Jamaica to Canada at ten, Lornette explored every sport she could. Track and Field became the passion that shaped her discipline and confidence.",
  },
  {
    title: "Elite Athlete",
    description:
      "That passion became performance. Through discipline and focus, Lornette earned provincial and national titles, turning natural speed into a career shaped by resilience and purpose.",
  },
  {
    title: "Coach & Mentor",
    description:
      "Even while competing, Lornette made time to encourage others. As a coach, she spent more than two decades helping athletes grow in sport, school, confidence, and wellness.",
  },
  {
    title: "Expanding Impact",
    description:
      "After athletics, Lornette brought the same drive into corporate, nonprofit, and community work, helping organizations, families, and young athletes move forward with practical support.",
  },
  {
    title: "Global Transformation",
    description:
      "Today, as a certified speaker, Lornette uses her story to reach the whole person, helping audiences leave with greater clarity, courage, and belief.",
  },
];

export default function AboutPage() {
  return (
    <PageShell>
      <main>
        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-5xl">
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
        </section>
        <MetricStrip />
        <section className="border-b border-[var(--line)] bg-white px-4 py-16 sm:px-6 lg:px-8">
          <div className="mx-auto grid max-w-7xl gap-10 lg:grid-cols-[0.75fr_1.25fr]">
            <SectionHeader
              eyebrow="Biography"
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
            <div className="mt-10 grid gap-4 sm:grid-cols-2 lg:grid-cols-5">
              {timeline.map((item) => (
                <article key={item.title} className="border border-[var(--line)] bg-white p-5">
                  <p className="mx-auto max-w-full break-words text-center font-serif text-2xl leading-tight text-balance text-[var(--ink)] md:text-[1.35rem] xl:text-2xl">
                    {item.title}
                  </p>
                  <p className="mt-3 text-sm leading-7 text-[#675d50]">
                    {item.description}
                  </p>
                </article>
              ))}
            </div>
            <AboutGallery slides={aboutGallerySlides} />
            <div className="mt-12">
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
