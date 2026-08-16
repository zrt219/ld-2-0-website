"use client";

import Image from "next/image";
import { CheckCircle2, Play, X } from "lucide-react";
import { useEffect, useRef, useState } from "react";

import type { MediaItem } from "@/content/site";
import { CTAButton } from "./CTAButton";

type HomepageReelTheaterProps = {
  video: MediaItem;
};

const plannerPoints = [
  "Stage presence and storytelling",
  "Signature keynote message",
  "Audience fit and booking path",
];

export function HomepageReelTheater({ video }: HomepageReelTheaterProps) {
  const [open, setOpen] = useState(false);
  const closeButtonRef = useRef<HTMLButtonElement>(null);
  const canPlay = Boolean(video.videoSrc) && !video.videoSrc?.startsWith("http");

  useEffect(() => {
    function onKeyDown(event: KeyboardEvent) {
      if (event.key === "Escape") {
        setOpen(false);
      }
    }

    window.addEventListener("keydown", onKeyDown);
    return () => window.removeEventListener("keydown", onKeyDown);
  }, []);

  useEffect(() => {
    if (!open) {
      return;
    }

    const previousOverflow = document.body.style.overflow;
    document.body.style.overflow = "hidden";
    closeButtonRef.current?.focus();

    return () => {
      document.body.style.overflow = previousOverflow;
    };
  }, [open]);

  return (
    <>
      <section className="relative overflow-hidden bg-white px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_18%_12%,rgba(198,165,92,0.18),transparent_34%),linear-gradient(135deg,rgba(250,247,240,0.92),rgba(255,255,255,0.96)_48%,rgba(232,221,203,0.46))]" />
        <div className="absolute right-[-14rem] top-[-12rem] h-[30rem] w-[30rem] rounded-full border border-[rgba(198,165,92,0.24)]" />
        <div className="relative mx-auto grid max-w-7xl gap-10 lg:grid-cols-[1.2fr_0.8fr] lg:items-center">
          <div>
            <p className="text-xs font-bold uppercase tracking-[0.28em] text-[var(--gold-dark)]">
              Watch Lornette in Action
            </p>
            <h2 className="mt-4 max-w-3xl font-serif text-5xl leading-tight text-balance text-[var(--ink)] sm:text-6xl">
              See the Message. Feel the Presence.
            </h2>
            <p className="mt-5 max-w-2xl text-lg leading-8 text-[#675d50]">
              Lornette helps audiences recognize they matter, rise through adversity, and leave ready to take action.
            </p>

            <div className="mt-10 overflow-hidden border border-[rgba(198,165,92,0.45)] bg-[var(--ink)] p-3 shadow-[0_30px_90px_rgba(23,20,18,0.22)]">
              <button
                type="button"
                onClick={() => canPlay && setOpen(true)}
                className="group relative block aspect-video w-full overflow-hidden bg-black text-left focus:outline-none focus:ring-4 focus:ring-[rgba(198,165,92,0.34)]"
                aria-label={`Play ${video.title}`}
              >
                <Image
                  src={video.image.src}
                  alt={video.image.alt}
                  fill
                  unoptimized
                  sizes="(max-width: 1024px) 92vw, 760px"
                  className={`object-cover transition duration-700 group-hover:scale-[1.035] ${video.image.crop ?? "object-center"}`}
                />
                <span className="absolute inset-0 bg-gradient-to-t from-black/86 via-black/28 to-black/8" />
                <span className="absolute left-4 top-4 border border-white/25 bg-black/55 px-3 py-1 text-[0.68rem] font-bold uppercase tracking-[0.18em] text-white">
                  Watch
                </span>
                {video.duration ? (
                  <span className="absolute right-4 top-4 border border-white/20 bg-black/55 px-3 py-1 text-xs font-bold text-white">
                    {video.duration}
                  </span>
                ) : null}
                <span className="absolute left-1/2 top-1/2 inline-flex h-20 w-20 -translate-x-1/2 -translate-y-1/2 items-center justify-center rounded-full border border-white/35 bg-[var(--champagne)] text-[var(--ink)] shadow-2xl ring-8 ring-black/25 transition group-hover:scale-105">
                  <Play fill="currentColor" size={30} aria-hidden="true" />
                </span>
                <span className="absolute inset-x-0 bottom-0 p-6 text-white">
                  <span className="block text-xs font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
                    Speaker Reel
                  </span>
                  <span className="mt-2 block font-serif text-3xl leading-tight">
                    {video.title}
                  </span>
                </span>
              </button>
            </div>
          </div>

          <aside className="border border-[rgba(198,165,92,0.42)] bg-[var(--ivory)] p-7 shadow-[0_22px_70px_rgba(23,20,18,0.08)] sm:p-9">
            <p className="text-xs font-bold uppercase tracking-[0.24em] text-[var(--gold-dark)]">
              For Event Planners
            </p>
            <h3 className="mt-4 font-serif text-4xl leading-tight text-[var(--ink)]">
              Review the room fit before you book.
            </h3>
            <p className="mt-5 text-base leading-8 text-[#675d50]">
              Use the reel to evaluate Lornette&apos;s presence, then move into the speaker kit or booking inquiry when the event brief is ready.
            </p>
            <div className="mt-7 grid gap-3">
              {plannerPoints.map((point) => (
                <div
                  key={point}
                  className="flex items-center gap-3 border border-[rgba(198,165,92,0.28)] bg-white px-4 py-3 text-sm font-bold text-[var(--charcoal)]"
                >
                  <CheckCircle2 size={18} aria-hidden="true" className="shrink-0 text-[var(--gold-dark)]" />
                  {point}
                </div>
              ))}
            </div>
            <div className="mt-8 grid gap-3">
              <button
                type="button"
                onClick={() => canPlay && setOpen(true)}
                className="inline-flex min-h-12 items-center justify-center gap-2 border border-transparent bg-[var(--champagne)] px-5 py-3 text-sm font-bold uppercase leading-5 text-[var(--ink)] shadow-[0_14px_34px_rgba(155,118,46,0.22)] transition hover:bg-[#d8b96e] focus:outline-none focus:ring-4 focus:ring-[rgba(198,165,92,0.3)]"
              >
                Watch Speaker Reel
                <Play fill="currentColor" size={15} aria-hidden="true" />
              </button>
              <CTAButton href="/book" variant="dark">Book Lornette</CTAButton>
              <CTAButton href="/speaker-kit" variant="secondary">Download Speaker Kit</CTAButton>
            </div>
          </aside>
        </div>
      </section>

      {open && video.videoSrc ? (
        <div
          role="dialog"
          aria-modal="true"
          aria-label={`${video.title} video`}
          className="fixed inset-0 z-[80] flex items-center justify-center bg-black/78 p-4"
          onClick={(event) => {
            if (event.target === event.currentTarget) {
              setOpen(false);
            }
          }}
        >
          <div className="w-full max-w-5xl border border-white/15 bg-[var(--ink)] p-3 shadow-2xl">
            <div className="mb-3 flex items-center justify-between gap-4 text-white">
              <p className="font-semibold">{video.title}</p>
              <button
                ref={closeButtonRef}
                type="button"
                onClick={() => setOpen(false)}
                className="inline-flex min-h-10 min-w-10 items-center justify-center border border-white/20 transition hover:border-[var(--champagne)] hover:text-[var(--champagne)] focus:outline-none focus:ring-4 focus:ring-[rgba(198,165,92,0.32)]"
                aria-label="Close video"
              >
                <X size={20} aria-hidden="true" />
              </button>
            </div>
            <video
              src={video.videoSrc}
              controls
              className="aspect-video w-full bg-black"
              aria-label={`${video.title} video player`}
            />
          </div>
        </div>
      ) : null}
    </>
  );
}
