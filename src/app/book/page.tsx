import { CalendarCheck, CheckCircle2, Mail, PlayCircle } from "lucide-react";

import { BookingForm } from "@/components/BookingForm";
import { CTAButton } from "@/components/CTAButton";
import { FAQAccordion } from "@/components/FAQAccordion";
import { PageShell } from "@/components/PageShell";
import { VideoCard } from "@/components/VideoCard";
import { createMetadata, mediaItems, services, siteCopy } from "@/content/site";

export const metadata = createMetadata(
  "Book Lornette",
  "Share event details and request Lornette Daye for a keynote, workshop, panel, or coaching engagement.",
  "/book",
);

const hiddenBookingTopics = new Set([
  "Athlete & Performance Coaching",
  "Resilient Leadership",
  "Diversity & Inclusion",
  "Resilience & Mindset Coaching",
  "Workshops & Training",
]);

export default function BookPage() {
  return (
    <PageShell>
      <main className="bg-[var(--ivory)]">
        <section className="relative overflow-hidden border-b border-[var(--line)] px-4 py-14 sm:px-6 lg:px-8 lg:py-20">
          <div className="pointer-events-none absolute inset-0 bg-[linear-gradient(120deg,rgba(255,255,255,0.94)_0%,rgba(250,247,240,0.82)_58%,rgba(232,221,203,0.5)_100%)]" />
          <div className="relative mx-auto max-w-5xl">
            <div>
              <p className="text-xs font-bold uppercase tracking-[0.24em] text-[var(--gold-dark)]">
                Book Lornette / Contact
              </p>
              <h1 className="mt-5 max-w-4xl font-serif text-5xl leading-[0.98] text-balance text-[var(--ink)] sm:text-7xl">
                Bring powerful impact to your next event.
              </h1>
              <p className="mt-6 max-w-2xl text-lg leading-8 text-[#554b40]">
                Share the event date, audience, location, and desired outcome so
                the right keynote, workshop, panel, or coaching format can be
                shaped with care.
              </p>
              <div className="mt-8 grid gap-4 sm:grid-cols-3">
                {[
                  ["Prompt response", "Inquiry details handled with care"],
                  ["Custom fit", "Topic and format matched to audience"],
                  ["Reliable next step", "Prepared email fallback if delivery is unavailable"],
                ].map(([title, body]) => (
                  <div key={title} className="border border-[var(--line)] bg-white/80 p-4">
                    <CheckCircle2 size={19} aria-hidden="true" className="text-[var(--gold-dark)]" />
                    <p className="mt-3 font-serif text-xl text-[var(--ink)]">{title}</p>
                    <p className="mt-1 text-sm leading-6 text-[#675d50]">{body}</p>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </section>

        <section className="px-4 py-12 sm:px-6 lg:px-8 lg:py-16">
          <div className="mx-auto grid max-w-7xl gap-8 lg:grid-cols-[0.34fr_1fr_0.34fr] lg:items-start">
            <aside className="grid gap-5">
              <div className="border border-[var(--line)] bg-white p-6 shadow-[0_16px_70px_rgba(23,20,18,0.07)]">
                <p className="text-xs font-bold uppercase tracking-[0.22em] text-[var(--gold-dark)]">
                  Speaking Topics
                </p>
                <div className="mt-5 grid gap-4">
                  {services
                    .filter((service) => !hiddenBookingTopics.has(service.title))
                    .slice(0, 5)
                    .map((service) => (
                      <a
                        key={service.title}
                        href={service.href}
                        className="group border-b border-[var(--line)] pb-4 last:border-b-0 last:pb-0"
                      >
                        <p className="font-serif text-xl leading-tight text-[var(--ink)] group-hover:text-[var(--gold-dark)]">
                          {service.title}
                        </p>
                        <p className="mt-1 text-sm leading-6 text-[#675d50]">{service.body}</p>
                      </a>
                    ))}
                </div>
              </div>
              <VideoCard
                {...mediaItems[0]}
                title="Preview the Speaker Reel"
                summary="Use the reel to prepare the booking conversation."
              />
            </aside>

            <div className="border border-[rgba(198,165,92,0.5)] bg-white p-5 shadow-[0_28px_100px_rgba(23,20,18,0.1)] sm:p-8">
              <div className="mb-8 border-b border-[var(--line)] pb-6">
                <p className="text-xs font-bold uppercase tracking-[0.22em] text-[var(--gold-dark)]">
                  Event Inquiry & Booking Form
                </p>
                <h2 className="mt-3 font-serif text-4xl leading-tight text-[var(--ink)]">
                  Tell us what the room needs to leave with.
                </h2>
              </div>
              <BookingForm />
            </div>

            <aside className="grid gap-5">
              <div className="border border-[var(--line)] bg-white p-6 shadow-[0_16px_70px_rgba(23,20,18,0.07)]">
                <p className="text-xs font-bold uppercase tracking-[0.22em] text-[var(--gold-dark)]">
                  Let&apos;s Connect
                </p>
                <div className="mt-5 grid gap-4 text-sm text-[#675d50]">
                  <a
                    href={`mailto:${siteCopy.contactEmail}`}
                    className="inline-flex items-center gap-3 font-semibold text-[var(--ink)] hover:text-[var(--gold-dark)]"
                  >
                    <Mail size={18} aria-hidden="true" />
                    {siteCopy.contactEmail}
                  </a>
                  <span className="inline-flex items-start gap-3">
                    <CalendarCheck size={18} aria-hidden="true" className="mt-1 text-[var(--gold-dark)]" />
                    Share preferred and alternate dates for faster scheduling.
                  </span>
                </div>
              </div>

              <div className="border border-[var(--line)] bg-white p-6 shadow-[0_16px_70px_rgba(23,20,18,0.07)]">
                <p className="text-xs font-bold uppercase tracking-[0.22em] text-[var(--gold-dark)]">
                  Frequently Asked Questions
                </p>
                <div className="mt-5">
                  <FAQAccordion />
                </div>
              </div>

              <div className="border border-[rgba(198,165,92,0.5)] bg-[var(--ink)] p-6 text-[var(--ivory)] shadow-[0_16px_70px_rgba(23,20,18,0.12)]">
                <PlayCircle size={24} aria-hidden="true" className="text-[var(--champagne)]" />
                <h2 className="mt-4 font-serif text-3xl leading-tight">
                  Need materials first?
                </h2>
                <p className="mt-3 text-sm leading-7 text-[#d8cdbb]">
                  Explore Lornette&apos;s bio, topics, and host resources before
                  sharing final event details.
                </p>
                <div className="mt-5">
                  <CTAButton
                    href="/speaker-kit"
                    variant="secondary"
                    className="border-[#d8b96e] text-[var(--ivory)] hover:bg-white/10"
                  >
                    View Speaker Kit
                  </CTAButton>
                </div>
              </div>
            </aside>
          </div>
        </section>
      </main>
    </PageShell>
  );
}
