import { CTAButton } from "@/components/CTAButton";
import { ImageFrame } from "@/components/ImageFrame";
import { PageShell } from "@/components/PageShell";
import { SectionHeader } from "@/components/SectionHeader";
import { additionalImages, createMetadata } from "@/content/site";

export const metadata = createMetadata(
  "Events & Workshops",
  "Events and workshop formats from Lornette Daye for keynotes, leadership sessions, inclusion workshops, mentorship programs, and performance coaching.",
  "/events",
);

const sampleEvents = [
  "Sample: Leadership That Lasts Workshop",
  "Sample: Youth Mentorship Intensive",
  "Sample: Inclusion in Action Session",
];

const workshops = [
  "Training & Workshops",
  "Resilience & Mindset Coaching",
  "Athlete Performance Lab",
  "Staying Grounded Retreat",
];

export default function EventsPage() {
  return (
    <PageShell>
      <main>
        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto grid max-w-7xl gap-10 lg:grid-cols-[0.92fr_1.08fr] lg:items-center">
            <SectionHeader
              eyebrow="Events & Workshops"
              title="Be in the Room Where It Happens."
              body="Plan keynotes, trainings, workshops, panels, school sessions, and community events with a clear inquiry path."
            />
            <ImageFrame image={additionalImages.eventWorkshop} ratio="aspect-[16/10]" priority />
          </div>
        </section>

        <section className="px-4 pb-16 sm:px-6 lg:px-8 lg:pb-24">
          <div className="mx-auto grid max-w-7xl gap-8 lg:grid-cols-[0.75fr_1.25fr]">
            <section className="border border-[var(--line)] bg-white p-7">
              <h2 className="font-serif text-3xl text-[var(--ink)]">Upcoming Events</h2>
              <p className="mt-4 text-sm leading-7 text-[#675d50]">
                Dates below are planning examples until confirmed public events are announced.
              </p>
              <div className="mt-6 grid gap-3">
                {sampleEvents.map((event) => (
                  <div key={event} className="border-l-2 border-[var(--champagne)] pl-4 text-sm font-semibold">
                    {event}
                  </div>
                ))}
              </div>
            </section>
            <section>
              <h2 className="font-serif text-3xl text-[var(--ink)]">Workshop Formats</h2>
              <div className="mt-6 grid gap-4 md:grid-cols-2">
                {workshops.map((workshop) => (
                  <article key={workshop} className="border border-[var(--line)] bg-white p-6">
                    <p className="font-serif text-2xl text-[var(--ink)]">{workshop}</p>
                    <p className="mt-3 text-sm leading-7 text-[#675d50]">
                      Custom proposal based on audience, format, timeline, and desired outcomes.
                    </p>
                  </article>
                ))}
              </div>
            </section>
          </div>
        </section>

        <section className="bg-[var(--sand)] px-4 py-16 sm:px-6 lg:px-8">
          <div className="mx-auto grid max-w-7xl gap-5 md:grid-cols-3">
            <ImageFrame image={additionalImages.trainingPoster} ratio="aspect-[4/5]" />
            <ImageFrame image={additionalImages.resiliencePoster} ratio="aspect-[4/5]" />
            <ImageFrame image={additionalImages.athleteStrategy} ratio="aspect-[4/5]" />
          </div>
        </section>

        <section className="px-4 py-16 sm:px-6 lg:px-8">
          <div className="mx-auto flex max-w-7xl flex-col gap-5 border-y border-[rgba(198,165,92,0.5)] py-10 lg:flex-row lg:items-center lg:justify-between">
            <p className="max-w-2xl font-serif text-3xl text-[var(--ink)]">
              Bring Lornette and her experience to your next room.
            </p>
            <CTAButton href="/book">Inquire About Events</CTAButton>
          </div>
        </section>
      </main>
    </PageShell>
  );
}
