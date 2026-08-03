import { CTAButton } from "@/components/CTAButton";
import { ImageFrame } from "@/components/ImageFrame";
import { PageShell } from "@/components/PageShell";
import { SectionHeader } from "@/components/SectionHeader";
import { TopicCard } from "@/components/TopicCard";
import { additionalImages, createMetadata, services } from "@/content/site";

export const metadata = createMetadata(
  "Programs & Services",
  "Programs and services from Lornette Daye for speaking, leadership, inclusion, mentorship, performance coaching, training, and life coaching.",
  "/programs",
);

const processSteps = [
  "Discover the audience, pressure points, and event goals.",
  "Design a custom proposal with the right format and topic focus.",
  "Deliver a keynote, workshop, or coaching experience with practical tools.",
  "Follow through with next steps that help momentum continue.",
];

export default function ProgramsPage() {
  return (
    <PageShell>
      <main>
        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto grid max-w-7xl gap-10 lg:grid-cols-[0.92fr_1.08fr] lg:items-center">
            <SectionHeader
              eyebrow="Programs & Services"
              title="Speaking, coaching, and development experiences for the people you serve."
              body="Choose a focused keynote, workshop, mentorship session, or coaching experience, or combine formats around the needs of your audience."
              headingLevel="h1"
            />
            <ImageFrame image={additionalImages.programOverview} ratio="aspect-[16/10]" priority />
          </div>
        </section>

        <section className="px-4 pb-16 sm:px-6 lg:px-8 lg:pb-24">
          <div className="mx-auto max-w-7xl">
            <div className="grid gap-5 md:grid-cols-2 lg:grid-cols-4">
              {services.map((service) => (
                <TopicCard key={service.title} title={service.title} body={service.body} href={service.href} />
              ))}
            </div>
          </div>
        </section>

        <section className="bg-[var(--sand)] px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto grid max-w-7xl gap-10 lg:grid-cols-[0.8fr_1.2fr]">
            <SectionHeader
              eyebrow="Process"
              title="Start with the people in the room."
              body="Lornette shapes each experience around your audience's pressure points, goals, format, and the next steps you want them to carry forward."
            />
            <div className="grid gap-4 md:grid-cols-2">
              {processSteps.map((step, index) => (
                <article key={step} className="border border-[var(--line)] bg-white p-6">
                  <p className="font-serif text-4xl text-[var(--gold-dark)]">0{index + 1}</p>
                  <p className="mt-4 text-sm font-semibold leading-7 text-[var(--charcoal)]">{step}</p>
                </article>
              ))}
            </div>
          </div>
        </section>

        <section className="px-4 py-16 sm:px-6 lg:px-8">
          <div className="mx-auto flex max-w-7xl flex-col gap-5 border-y border-[rgba(198,165,92,0.5)] py-10 lg:flex-row lg:items-center lg:justify-between">
            <p className="max-w-2xl font-serif text-3xl text-[var(--ink)]">
              Ready to shape a custom proposal for your audience?
            </p>
            <CTAButton href="/book">Explore Programs</CTAButton>
          </div>
        </section>
      </main>
    </PageShell>
  );
}
