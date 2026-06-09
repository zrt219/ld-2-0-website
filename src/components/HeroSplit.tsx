import Image from "next/image";

import { CTAButton } from "./CTAButton";
import { VideoCard } from "./VideoCard";
import type { SiteImage } from "@/content/site";

type HeroVideo = {
  title: string;
  summary: string;
  image: SiteImage;
  videoSrc?: string;
  duration?: string;
  status?: string;
};

type HeroSplitProps = {
  eyebrow?: string;
  title: string;
  body: string;
  image: SiteImage;
  primaryHref?: string;
  primaryLabel?: string;
  secondaryHref?: string;
  secondaryLabel?: string;
  video?: HeroVideo;
};

function renderHeroTitle(title: string) {
  const emphasis = "They Matter.";

  if (!title.endsWith(emphasis)) {
    return title;
  }

  return (
    <>
      {title.slice(0, -emphasis.length)}
      <span className="underline decoration-[var(--champagne)] decoration-4 underline-offset-[0.14em]">
        {emphasis}
      </span>
    </>
  );
}

export function HeroSplit({
  eyebrow,
  title,
  body,
  image,
  primaryHref = "/book",
  primaryLabel = "Book Lornette",
  secondaryHref = "/media",
  secondaryLabel = "Watch Speaker Reel",
  video,
}: HeroSplitProps) {
  const imageFrameTone =
    image.frameTone === "warm-ivory"
      ? "bg-[linear-gradient(180deg,#fffdf8_0%,#f5efe4_100%)]"
      : "bg-white";

  return (
    <section className="relative overflow-hidden border-b border-[rgba(198,165,92,0.35)] bg-[var(--ivory)]">
      <div className="pointer-events-none absolute inset-0 bg-[linear-gradient(115deg,rgba(255,255,255,0.92)_0%,rgba(250,247,240,0.84)_46%,rgba(232,221,203,0.58)_100%)]" />
      <div className="pointer-events-none absolute right-0 top-0 h-full w-1/2 bg-[linear-gradient(132deg,transparent_0%,rgba(198,165,92,0.1)_44%,transparent_78%)]" />
      <div className="pointer-events-none absolute left-0 top-10 h-px w-2/3 bg-gradient-to-r from-transparent via-[rgba(198,165,92,0.28)] to-transparent" />

      <div className="relative mx-auto grid max-w-7xl gap-10 px-4 py-12 sm:px-6 lg:min-h-[760px] lg:grid-cols-[minmax(0,0.92fr)_minmax(0,0.88fr)] lg:items-center lg:px-8 lg:py-16 xl:py-20">
        <div className="min-w-0 max-w-3xl">
          {eyebrow ? (
            <p className="inline-flex border border-[rgba(198,165,92,0.48)] bg-white/70 px-3 py-2 text-xs font-bold uppercase tracking-[0.22em] text-[var(--gold-dark)] shadow-sm">
              {eyebrow}
            </p>
          ) : null}
          <h1 className="mt-6 max-w-4xl font-serif text-[2.38rem] leading-[0.98] text-balance text-[var(--ink)] sm:text-6xl lg:text-[4.1rem] xl:text-[4.72rem]">
            {renderHeroTitle(title)}
          </h1>
          <p className="mt-7 max-w-2xl text-lg leading-8 text-[#554b40]">
            {body}
          </p>
          <div className="mt-9 flex flex-col gap-3 sm:flex-row">
            <CTAButton href={primaryHref}>{primaryLabel}</CTAButton>
            <CTAButton href={secondaryHref} variant="secondary">
              {secondaryLabel}
            </CTAButton>
          </div>
        </div>

        <div className="relative min-w-0 w-full max-w-[560px] lg:justify-self-end">
          <div className={`relative mx-auto aspect-[4/5] max-h-[590px] w-full max-w-[500px] overflow-hidden border border-[rgba(198,165,92,0.42)] shadow-[0_28px_110px_rgba(23,20,18,0.14)] ${imageFrameTone}`}>
            <Image
              src={image.src}
              alt={image.alt}
              fill
              priority
              sizes="(max-width: 768px) 92vw, 44vw"
              unoptimized
              className={`object-cover ${image.crop ?? "object-center"}`}
            />
            <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/40" />
            {image.showBottomFade === false ? null : (
              <div className="pointer-events-none absolute inset-x-0 bottom-0 h-32 bg-gradient-to-t from-[rgba(23,20,18,0.42)] to-transparent" />
            )}
          </div>

          {video ? (
            <div className="relative z-10 mx-auto -mt-10 w-full max-w-[470px] lg:-ml-8 lg:-mt-16">
              <VideoCard {...video} compact />
            </div>
          ) : null}
        </div>
      </div>
    </section>
  );
}
