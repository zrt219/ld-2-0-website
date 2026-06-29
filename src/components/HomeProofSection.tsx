import Image, { type StaticImageData } from "next/image";

import { canadaSummerGamesSlide } from "@/content/aboutGallery";

export type HomeProofImage = {
  src: StaticImageData | string;
  alt: string;
  crop?: string;
};

export type HomeProofPoint = {
  label: string;
  detail: string;
};

export type HomeProofSectionProps = {
  title?: string;
  image?: HomeProofImage;
  imageLabel?: string;
  imageCaption?: string;
  proofPoints?: readonly HomeProofPoint[];
  className?: string;
};

const defaultProofPoints: readonly HomeProofPoint[] = [
  {
    label: "Provincial & National Titles",
    detail: "Earned from high school championships through professional sprinting.",
  },
  {
    label: "Records Still Unbroken",
    detail: "Proof of a standard strong enough to last well beyond one season.",
  },
  {
    label: "Built for the Long Run",
    detail: "She knows what it takes to sustain excellence over time, not just reach it once.",
  },
];

export function HomeProofSection({
  title = "Years of Proof.",
  image = canadaSummerGamesSlide.image,
  imageLabel = "Canada Summer Games, 1985",
  imageCaption = canadaSummerGamesSlide.title,
  proofPoints = defaultProofPoints,
  className = "",
}: HomeProofSectionProps) {
  return (
    <section className={`bg-white px-4 pb-16 sm:px-6 lg:px-8 lg:pb-24 ${className}`}>
      <div className="mx-auto max-w-7xl">
        <div className="relative overflow-hidden border border-[rgba(198,165,92,0.38)] bg-[linear-gradient(140deg,rgba(255,255,255,0.98)_0%,rgba(250,247,240,0.96)_52%,rgba(232,221,203,0.78)_100%)] p-6 shadow-[0_20px_80px_rgba(23,20,18,0.08)] sm:p-8 lg:p-10">
          <div className="pointer-events-none absolute inset-x-0 top-0 h-px bg-gradient-to-r from-transparent via-[rgba(198,165,92,0.5)] to-transparent" />
          <div className="pointer-events-none absolute -right-24 top-0 h-52 w-52 rounded-full bg-[radial-gradient(circle,rgba(198,165,92,0.18),transparent_68%)]" />

          <div className="relative grid gap-8 lg:grid-cols-[minmax(0,1fr)_minmax(280px,0.8fr)] lg:items-center">
            <div className="min-w-0">
              <h2 className="font-serif text-4xl leading-tight text-balance text-[var(--ink)] sm:text-5xl">
                {title}
              </h2>

              {proofPoints.length > 0 ? (
                <div className="mt-7 grid gap-3 sm:grid-cols-2 xl:grid-cols-3">
                  {proofPoints.map((point) => (
                    <article
                      key={point.label}
                      className="border border-[rgba(198,165,92,0.24)] bg-white/78 p-4"
                    >
                      <p className="text-[11px] font-bold uppercase tracking-[0.18em] text-[var(--gold-dark)]">
                        {point.label}
                      </p>
                      <p className="mt-2 text-sm leading-7 text-[#5f5548]">
                        {point.detail}
                      </p>
                    </article>
                  ))}
                </div>
              ) : null}
            </div>

            <div className="min-w-0 lg:justify-self-end">
              <div className="mx-auto max-w-[34rem] border border-[rgba(198,165,92,0.42)] bg-[var(--sand)] p-4 shadow-[0_24px_80px_rgba(23,20,18,0.14)]">
                <div className="relative aspect-[690/446] overflow-hidden border border-white/70 bg-[#efe6d7]">
                  <Image
                    src={image.src}
                    alt={image.alt}
                    fill
                    unoptimized
                    sizes="(max-width: 1024px) 92vw, 34rem"
                    className={`h-full w-full object-contain ${image.crop ?? "object-center"}`}
                  />
                </div>
                <div className="mt-4 border-l-2 border-[var(--champagne)] pl-4">
                  <p className="text-[10px] font-bold uppercase tracking-[0.26em] text-[var(--gold-dark)]">
                    {imageLabel}
                  </p>
                  <p className="mt-2 text-sm leading-6 text-[#5f5548]">
                    {imageCaption}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
