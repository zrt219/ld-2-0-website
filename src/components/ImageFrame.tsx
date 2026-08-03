import Image from "next/image";

import type { SiteImage } from "@/content/site";

type ImageFrameProps = {
  image: SiteImage;
  ratio?: string;
  priority?: boolean;
  className?: string;
  sizes?: string;
  framed?: boolean;
};

export function ImageFrame({
  image,
  ratio = "aspect-[4/5]",
  priority = false,
  className = "",
  sizes = "(max-width: 768px) 92vw, (max-width: 1200px) 44vw, 32vw",
  framed = true,
}: ImageFrameProps) {
  return (
    <div
      className={`relative overflow-hidden ${ratio} ${
        framed
          ? "border border-[rgba(198,165,92,0.42)] bg-[var(--sand)] shadow-[0_24px_80px_rgba(23,20,18,0.13)]"
          : ""
      } ${className}`}
    >
      <Image
        src={image.src}
        alt={image.alt}
        fill
        priority={priority}
        unoptimized
        sizes={sizes}
        className={`h-full w-full origin-top object-cover transition duration-500 ${image.crop ?? "object-center"}`}
      />
      {framed ? (
        <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/25" />
      ) : null}
    </div>
  );
}
