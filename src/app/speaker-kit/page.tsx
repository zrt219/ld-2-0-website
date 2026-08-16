import { CTAButton } from "@/components/CTAButton";
import { PageShell } from "@/components/PageShell";
import { SectionHeader } from "@/components/SectionHeader";
import { SpeakerKitDownload } from "@/components/SpeakerKitDownload";
import { createMetadata, servicePages, speakerKitDownloads, siteCopy } from "@/content/site";

export const metadata = createMetadata(
  "Speaker Kit",
  "Planner-ready speaker kit materials for Lornette Daye, prepared for final approved files before launch.",
  "/speaker-kit",
);

export default function SpeakerKitPage() {
  return (
    <PageShell>
      <main className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
        <div className="mx-auto max-w-7xl">
          <SectionHeader
            eyebrow="Speaker Kit"
            title="Everything You Need to Introduce Lornette."
            body={siteCopy.descriptor}
          />
          <div className="mt-10 grid gap-4 md:grid-cols-2 lg:grid-cols-4">
            {speakerKitDownloads.map((item) => (
              <div id={item.id} key={item.title}>
                <SpeakerKitDownload title={item.title} href={item.href} />
              </div>
            ))}
          </div>
          <div className="mt-12 grid gap-8 lg:grid-cols-[0.8fr_1.2fr]">
            <section className="border border-[var(--line)] bg-white p-7">
              <h2 className="font-serif text-3xl text-[var(--ink)]">Speaker Topics</h2>
              <ul className="mt-5 grid gap-3">
                {servicePages.speaking.pillars.map((topic) => (
                  <li key={topic} className="border-l-2 border-[var(--champagne)] pl-3 text-sm font-semibold">
                    {topic}
                  </li>
                ))}
              </ul>
            </section>
            <section className="border border-[var(--line)] bg-white p-7">
              <h2 className="font-serif text-3xl text-[var(--ink)]">Event Planner Checklist</h2>
              <div className="mt-5 grid gap-3 text-sm leading-7 text-[#675d50] sm:grid-cols-2">
                <p>Confirm event date, audience size, room format, and desired outcome.</p>
                <p>Share AV needs, intro script preference, timing, and onsite contact details.</p>
                <p>Use the planning files until final approved assets are available for distribution.</p>
                <p>Submit the booking form for a custom proposal and availability review.</p>
              </div>
            </section>
          </div>
          <div className="mt-10 flex flex-col gap-3 sm:flex-row">
            <CTAButton href="/book">Inquire About Availability</CTAButton>
            <CTAButton href="/media" variant="secondary">Watch Speaker Reel</CTAButton>
          </div>
        </div>
      </main>
    </PageShell>
  );
}
