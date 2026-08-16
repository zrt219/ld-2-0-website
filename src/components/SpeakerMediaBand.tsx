import { ArrowRight, CalendarCheck, Download, Film, Mic2 } from "lucide-react";

import { mediaItems } from "@/content/site";
import { CTAButton } from "./CTAButton";
import { VideoCard } from "./VideoCard";

const plannerLinks = [
  {
    icon: Film,
    title: "Speaker Reel",
    body: "Review presence, delivery style, pacing, and audience fit from the primary reel.",
  },
  {
    icon: Mic2,
    title: "Clip Library",
    body: "Hold space for keynote clips, interviews, podcasts, and short insight videos as assets are approved.",
  },
  {
    icon: Download,
    title: "Planner Files",
    body: "Keep bios, topic sheets, AV needs, intro copy, and headshot resources one click away.",
  },
  {
    icon: CalendarCheck,
    title: "Booking Path",
    body: "Move from media review to availability, format, audience goals, and custom proposal details.",
  },
];

type SpeakerMediaBandProps = {
  eyebrow?: string;
  title?: string;
  body?: string;
};

export function SpeakerMediaBand({
  eyebrow = "Planner Media Room",
  title = "Give decision-makers the reel, proof path, and booking next step in one place.",
  body = "A premium speaker site should make media review feel effortless. This section keeps video, planner resources, and inquiry routes together so organizers can evaluate Lornette without losing momentum.",
}: SpeakerMediaBandProps) {
  return (
    <section className="bg-[var(--ink)] px-4 py-16 text-[var(--ivory)] sm:px-6 lg:px-8 lg:py-24">
      <div className="mx-auto grid max-w-7xl gap-10 lg:grid-cols-[0.78fr_1.22fr] lg:items-center">
        <div>
          <p className="text-xs font-bold uppercase tracking-[0.24em] text-[var(--champagne)]">
            {eyebrow}
          </p>
          <h2 className="mt-5 font-serif text-4xl leading-tight sm:text-5xl">
            {title}
          </h2>
          <p className="mt-5 max-w-xl text-base leading-8 text-[#d8cdbb]">
            {body}
          </p>
          <div className="mt-8 flex flex-col gap-3 sm:flex-row">
            <CTAButton href="/media">Watch The Reel</CTAButton>
            <CTAButton href="/speaker-kit" variant="secondary">
              Speaker Kit
            </CTAButton>
          </div>
        </div>

        <VideoCard
          {...mediaItems[0]}
          title="Speaker Reel for Event Planners"
          summary="Start here for a fast read on tone, story, audience connection, and transformational speaking style."
          featured
          className="shadow-[0_32px_120px_rgba(0,0,0,0.35)]"
        />
      </div>

      <div className="mx-auto mt-10 grid max-w-7xl gap-4 md:grid-cols-2 lg:grid-cols-4">
        {plannerLinks.map((item) => {
          const Icon = item.icon;
          return (
            <article
              key={item.title}
              className="border border-white/12 bg-white/[0.045] p-5 shadow-[0_18px_80px_rgba(0,0,0,0.18)]"
            >
              <Icon className="text-[var(--champagne)]" size={25} aria-hidden="true" />
              <h3 className="mt-4 font-serif text-2xl text-white">{item.title}</h3>
              <p className="mt-3 text-sm leading-7 text-[#d8cdbb]">{item.body}</p>
            </article>
          );
        })}
      </div>

      <div className="mx-auto mt-10 flex max-w-7xl items-center gap-3 border-t border-white/12 pt-6 text-sm font-bold uppercase tracking-[0.18em] text-[var(--champagne)]">
        Media-first review flow
        <ArrowRight size={16} aria-hidden="true" />
      </div>
    </section>
  );
}
