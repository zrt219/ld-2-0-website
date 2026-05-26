"use client";

import Image from "next/image";
import { Play, X } from "lucide-react";
import { useEffect, useRef, useState } from "react";

import type { SiteImage } from "@/content/site";

type VideoCardProps = {
  title: string;
  summary: string;
  image: SiteImage;
  videoSrc?: string;
  duration?: string;
  status?: string;
  featured?: boolean;
  compact?: boolean;
  className?: string;
  featuredColumns?: string;
  spaciousFeaturedContent?: boolean;
  featuredMediaSize?: string;
};

export function VideoCard({
  title,
  summary,
  image,
  videoSrc,
  duration,
  status,
  featured = false,
  compact = false,
  className = "",
  featuredColumns,
  spaciousFeaturedContent = false,
  featuredMediaSize,
}: VideoCardProps) {
  const [open, setOpen] = useState(false);
  const isExternalVideo = Boolean(videoSrc?.startsWith("http"));
  const canPlay = Boolean(videoSrc) && !isExternalVideo;
  const canWatch = canPlay || isExternalVideo;
  const closeButtonRef = useRef<HTMLButtonElement>(null);

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
      <article
        className={`group overflow-hidden border border-[rgba(198,165,92,0.42)] bg-white shadow-[0_18px_70px_rgba(23,20,18,0.1)] transition duration-300 hover:-translate-y-0.5 hover:shadow-[0_24px_90px_rgba(23,20,18,0.14)] ${
          featured ? featuredColumns ?? "lg:grid lg:grid-cols-[1.35fr_0.65fr]" : ""
        } ${className}`}
      >
        <div
          className={`relative block w-full overflow-hidden text-left ${
            featured ? featuredMediaSize ?? "min-h-[330px] lg:min-h-[430px]" : "aspect-video"
          }`}
        >
          <Image
            src={image.src}
            alt={image.alt}
            fill
            unoptimized
            priority={featured}
            sizes={featured ? "92vw" : "(max-width: 768px) 92vw, 42vw"}
            className={`object-cover transition duration-700 group-hover:scale-[1.035] ${image.crop ?? "object-center"}`}
          />
          <span className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/20 to-black/5 transition group-hover:from-black/86" />
          {canPlay ? (
            <button
              type="button"
              onClick={() => setOpen(true)}
              className="absolute left-1/2 top-1/2 inline-flex h-16 w-16 -translate-x-1/2 -translate-y-1/2 items-center justify-center rounded-full border border-white/35 bg-[var(--champagne)] text-[var(--ink)] shadow-2xl ring-8 ring-black/20 transition hover:scale-105 focus:outline-none focus:ring-4 focus:ring-[rgba(198,165,92,0.45)]"
              aria-label={`Play ${title}`}
            >
              <Play fill="currentColor" size={24} aria-hidden="true" />
            </button>
          ) : isExternalVideo && videoSrc ? (
            <a
              href={videoSrc}
              target="_blank"
              rel="noreferrer"
              className="absolute left-1/2 top-1/2 inline-flex h-16 w-16 -translate-x-1/2 -translate-y-1/2 items-center justify-center rounded-full border border-white/35 bg-[var(--champagne)] text-[var(--ink)] shadow-2xl ring-8 ring-black/20 transition hover:scale-105 focus:outline-none focus:ring-4 focus:ring-[rgba(198,165,92,0.45)]"
              aria-label={`Open ${title}`}
            >
              <Play fill="currentColor" size={24} aria-hidden="true" />
            </a>
          ) : (
            <span className="absolute right-4 top-4 border border-white/25 bg-black/55 px-3 py-1 text-[0.68rem] font-bold uppercase tracking-[0.18em] text-white">
              {status ?? "Coming soon"}
            </span>
          )}
          <span className="absolute left-4 top-4 border border-white/25 bg-black/45 px-3 py-1 text-[0.68rem] font-bold uppercase tracking-[0.18em] text-white">
            {canWatch ? "Watch" : "Preview"}
          </span>
          {canWatch && duration ? (
            <span className="absolute right-4 top-4 border border-white/20 bg-black/50 px-3 py-1 text-xs font-bold text-white">
              {duration}
            </span>
          ) : null}
          {compact ? (
            <span className="absolute inset-x-0 bottom-0 p-5 text-white">
              <span className="block text-xs font-bold uppercase tracking-[0.2em] text-[var(--champagne)]">
                Speaker Reel
              </span>
              <span className="mt-2 block font-serif text-2xl leading-tight">
                {title}
              </span>
            </span>
          ) : null}
        </div>

        {!compact ? (
          <div
            className={`p-6 ${
              featured
                ? `bg-[var(--ink)] text-[var(--ivory)] ${
                    spaciousFeaturedContent
                      ? "flex h-full flex-col justify-center lg:p-10 xl:p-12"
                      : "lg:p-8"
                  }`
                : ""
            }`}
          >
            <p
              className={`text-xs font-bold uppercase tracking-[0.2em] ${
                featured ? "text-[var(--champagne)]" : "text-[var(--gold-dark)]"
              }`}
            >
              Video
            </p>
            <h3
              className={`mt-3 font-serif text-3xl leading-tight ${
                featured ? "text-white" : "text-[var(--ink)]"
              }`}
            >
              {title}
            </h3>
            <p
              className={`mt-4 ${
                featured && spaciousFeaturedContent
                  ? "text-base leading-8 lg:text-lg lg:leading-9"
                  : "text-sm leading-7"
              } ${featured ? "text-[#d8cdbb]" : "text-[#675d50]"
              }`}
            >
              {summary}
            </p>
            {canPlay ? (
              <button
                type="button"
                onClick={() => setOpen(true)}
                className={`inline-flex items-center justify-center gap-2 border text-center font-bold uppercase transition hover:bg-[rgba(198,165,92,0.1)] focus:outline-none focus:ring-4 focus:ring-[rgba(198,165,92,0.24)] ${
                  featured && spaciousFeaturedContent
                    ? "mt-10 min-h-16 w-full px-7 py-4 text-base tracking-[0.16em]"
                    : "mt-7 min-h-11 px-4 text-xs tracking-[0.16em]"
                } ${
                  featured
                    ? "border-white/20 text-[var(--champagne)]"
                    : "border-[rgba(155,118,46,0.34)] text-[var(--gold-dark)]"
                }`}
              >
                Play video
                <Play
                  fill="currentColor"
                  size={featured && spaciousFeaturedContent ? 16 : 13}
                  aria-hidden="true"
                />
              </button>
            ) : isExternalVideo && videoSrc ? (
              <a
                href={videoSrc}
                target="_blank"
                rel="noreferrer"
                className={`inline-flex items-center justify-center gap-2 border text-center font-bold uppercase transition hover:bg-[rgba(198,165,92,0.1)] focus:outline-none focus:ring-4 focus:ring-[rgba(198,165,92,0.24)] ${
                  featured && spaciousFeaturedContent
                    ? "mt-10 min-h-16 w-full px-7 py-4 text-base tracking-[0.16em]"
                    : "mt-7 min-h-11 px-4 text-xs tracking-[0.16em]"
                } ${
                  featured
                    ? "border-white/20 text-[var(--champagne)]"
                    : "border-[rgba(155,118,46,0.34)] text-[var(--gold-dark)]"
                }`}
              >
                Open video
                <Play
                  fill="currentColor"
                  size={featured && spaciousFeaturedContent ? 16 : 13}
                  aria-hidden="true"
                />
              </a>
            ) : (
              <span
                className={`mt-7 inline-flex min-h-11 items-center gap-2 border px-4 text-xs font-bold uppercase tracking-[0.16em] ${
                  featured
                    ? "border-white/20 text-[var(--champagne)]"
                    : "border-[rgba(155,118,46,0.34)] text-[var(--gold-dark)]"
                }`}
              >
                {status ?? "Coming soon"}
              </span>
            )}
          </div>
        ) : null}
      </article>

      {open && videoSrc ? (
        <div
          role="dialog"
          aria-modal="true"
          aria-label={`${title} video`}
          className="fixed inset-0 z-[80] flex items-center justify-center bg-black/78 p-4"
          onClick={(event) => {
            if (event.target === event.currentTarget) {
              setOpen(false);
            }
          }}
        >
          <div className="w-full max-w-5xl border border-white/15 bg-[var(--ink)] p-3 shadow-2xl">
            <div className="mb-3 flex items-center justify-between gap-4 text-white">
              <p className="font-semibold">{title}</p>
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
              src={videoSrc}
              controls
              className="aspect-video w-full bg-black"
              aria-label={`${title} video player`}
            />
          </div>
        </div>
      ) : null}
    </>
  );
}
