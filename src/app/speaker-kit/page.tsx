import { CTAButton } from "@/components/CTAButton";
import { PageShell } from "@/components/PageShell";
import { SectionHeader } from "@/components/SectionHeader";
import { SpeakerKitDownload } from "@/components/SpeakerKitDownload";
import { createMetadata, servicePages, speakerKitDownloads, siteCopy } from "@/content/site";

export const metadata = createMetadata(
  "Speaker Kit",
  "Speaker kit materials for introducing Lornette Daye and planning a meaningful event.",
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
                <SpeakerKitDownload title={item.cardTitle ?? item.title} href={item.href} />
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
            <div className="flex h-full items-start lg:pt-[8px]">
              <a
                href="https://ld-speaker-onesheet.vercel.app"
                className="inline-flex min-h-16 w-full max-w-[26rem] items-center justify-center border border-transparent bg-[var(--champagne)] px-8 py-5 text-base font-bold uppercase tracking-[0.12em] text-[var(--ink)] shadow-[0_18px_36px_rgba(155,118,46,0.18)] transition hover:bg-[#d8b96e] focus:outline-none focus:ring-4 focus:ring-[rgba(198,165,92,0.24)]"
              >
                One Sheet Site
              </a>
            </div>
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
