import { CalendarCheck, Download, FileText, Mic2 } from "lucide-react";

import { CTAButton } from "@/components/CTAButton";
import { MediaGrid } from "@/components/MediaGrid";
import { PageShell } from "@/components/PageShell";
import { SectionHeader } from "@/components/SectionHeader";
import { VideoCard } from "@/components/VideoCard";
import { createMetadata, mediaItems, speakerKitDownloads } from "@/content/site";

export const metadata = createMetadata(
  "Media / Speaker Reel",
  "Watch, listen, and experience the impact of Lornette Daye through speaker reels, interviews, and media clips.",
  "/media",
);

export default function MediaPage() {
  return (
    <PageShell>
      <main>
        <section className="relative overflow-hidden border-b border-[var(--line)] bg-[var(--ivory)] px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="pointer-events-none absolute inset-x-0 top-0 h-px bg-gradient-to-r from-transparent via-[rgba(198,165,92,0.34)] to-transparent" />
          <div className="mx-auto grid max-w-7xl gap-10 lg:grid-cols-[0.82fr_1.18fr] lg:items-center">
            <div>
              <SectionHeader
                eyebrow="Media / Speaker Reel"
                title="Watch. Listen. Experience the Impact."
                body="Explore Lornette's warmth, conviction, and message through video clips, speaking moments, and media features."
                headingLevel="h1"
              />
              <div className="mt-8 grid gap-4 sm:grid-cols-3">
                {[
                  ["Speaker Reel", "Watch first"],
                  ["Speaker Kit", "Host resources"],
                  ["Booking", "Start the conversation"],
                ].map(([title, body]) => (
                  <div key={title} className="border border-[var(--line)] bg-white/80 p-4">
                    <p className="font-serif text-2xl text-[var(--ink)]">{title}</p>
                    <p className="mt-1 text-xs font-bold uppercase tracking-[0.14em] text-[var(--gold-dark)]">
                      {body}
                    </p>
                  </div>
                ))}
              </div>
            </div>
            <VideoCard {...mediaItems[0]} featured className="shadow-[0_30px_120px_rgba(23,20,18,0.16)]" />
          </div>
        </section>

        <section className="bg-[var(--ink)] px-4 py-10 text-[var(--ivory)] sm:px-6 lg:px-8">
          <div className="mx-auto grid max-w-7xl gap-6 lg:grid-cols-[0.8fr_1.2fr_auto] lg:items-center">
            <div>
              <p className="text-xs font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
                Media Hub
              </p>
              <h2 className="mt-2 font-serif text-3xl leading-tight">
                Start with video, then keep exploring the message.
              </h2>
            </div>
            <div className="grid gap-3 text-sm text-[#d8cdbb] sm:grid-cols-3">
              <span className="inline-flex items-center gap-2">
                <Mic2 size={18} aria-hidden="true" className="text-[var(--champagne)]" />
                Keynote clips
              </span>
              <span className="inline-flex items-center gap-2">
                <FileText size={18} aria-hidden="true" className="text-[var(--champagne)]" />
                Speaker-kit files
              </span>
              <span className="inline-flex items-center gap-2">
                <CalendarCheck size={18} aria-hidden="true" className="text-[var(--champagne)]" />
                Availability inquiry
              </span>
            </div>
            <CTAButton href="/book">Book Lornette</CTAButton>
          </div>
        </section>

        <section className="px-4 pb-16 sm:px-6 lg:px-8 lg:pb-24">
          <div className="mx-auto grid max-w-7xl gap-8 py-12 lg:grid-cols-[1fr_0.34fr]">
            <MediaGrid />
            <aside className="h-fit border border-[rgba(198,165,92,0.45)] bg-white p-6 shadow-[0_20px_80px_rgba(23,20,18,0.08)]">
              <p className="text-xs font-bold uppercase tracking-[0.22em] text-[var(--gold-dark)]">
                Media Kit & Resources
              </p>
              <h2 className="mt-3 font-serif text-3xl leading-tight text-[var(--ink)]">
                Everything a host needs to introduce Lornette.
              </h2>
              <div className="mt-6 grid gap-2">
                {speakerKitDownloads.map((download) => (
                  <a
                    key={download.title}
                    href={download.href}
                    className="group flex min-h-14 items-center justify-between gap-4 border-b border-[var(--line)] py-3 text-sm font-semibold"
                  >
                    <span>
                      {download.title}
                      <span className="mt-1 block text-xs font-normal text-[#7d7164]">
                        Host resource
                      </span>
                    </span>
                    <Download
                      size={17}
                      aria-hidden="true"
                      className="text-[var(--gold-dark)] transition group-hover:translate-y-0.5"
                    />
                  </a>
                ))}
              </div>
              <div className="mt-8 grid gap-3">
                <CTAButton href="/speaker-kit">View Speaker Kit</CTAButton>
                <CTAButton href="/book" variant="secondary">Book Lornette</CTAButton>
              </div>
            </aside>
          </div>
        </section>
      </main>
    </PageShell>
  );
}
