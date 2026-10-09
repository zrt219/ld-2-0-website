import Image from "next/image";
import Link from "next/link";
import { ArrowRight } from "lucide-react";

export type FoundationsPathway = {
  title: string;
  tagline: string;
  description: string;
  ctaText: string;
  href: string;
  imageSrc: string;
  imageAlt: string;
  objectPosition?: string;
};

export const foundationsPathways: FoundationsPathway[] = [
  {
    title: "Golf",
    tagline: "ATHLETE PATHWAY",
    description: "Mental performance, composure, and repeatable routines for competitive golfers.",
    ctaText: "Explore Golf",
    href: "/foundations/golf",
    imageSrc: "/foundations/pathways/golf-pathway.jpg",
    imageAlt: "Competitive golfer swing follow-through at golden sunset",
    objectPosition: "center 30%",
  },
  {
    title: "Hockey",
    tagline: "TEAM PATHWAY",
    description: "Pressure tools, recovery, leadership, and team culture for hockey athletes and programs.",
    ctaText: "Explore Hockey",
    href: "/foundations/hockey",
    imageSrc: "/foundations/pathways/hockey-pathway.jpg",
    imageAlt: "Elite hockey player jersey #10 standing in packed arena lights",
    objectPosition: "center 20%",
  },
  {
    title: "Corporate",
    tagline: "ORGANIZATIONAL PATHWAY",
    description: "Championship composure, leadership, and performance under pressure for organizations.",
    ctaText: "View Corporate",
    href: "/foundations/corporate",
    imageSrc: "/foundations/pathways/corporate-pathway.jpg",
    imageAlt: "Executive speaker addressing high-level corporate audience",
    objectPosition: "center 20%",
  },
  {
    title: "Europe",
    tagline: "EUROPEAN PARTNERSHIPS",
    description: "For international sport clubs, regional federations, and European sport ecosystems.",
    ctaText: "Explore Europe",
    href: "/foundations/europe",
    imageSrc: "/foundations/pathways/europe-pathway.jpg",
    imageAlt: "Sunlit luxury European lounge with international flags overlooking historic cathedral waterfront",
    objectPosition: "center 25%",
  },
];

interface FoundationsMegaMenuProps {
  onClose: () => void;
}

export function FoundationsMegaMenu({ onClose }: FoundationsMegaMenuProps) {
  return (
    <div className="w-full max-w-6xl mx-auto rounded-[2px] border border-[#dfd1b4] bg-[#fbf8f0] p-5 sm:p-6 shadow-[0_22px_50px_rgba(30,24,15,0.14)]">
      {/* Header bar */}
      <div className="flex items-center justify-between pb-3.5 border-b border-[#dfd1b4]/80">
        <div className="flex items-center gap-2">
          <span className="text-[11px] font-extrabold uppercase tracking-[0.24em] text-[var(--gold-dark)]">
            PROGRAMS
          </span>
          <span className="text-[#c2b49e]">•</span>
          <span className="text-[11px] font-bold uppercase tracking-[0.2em] text-[#6f655a]">
            Signature Pathways
          </span>
        </div>
        <Link
          href="/foundations"
          onClick={onClose}
          className="group inline-flex items-center gap-1.5 text-[11px] font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)] hover:text-[#171412] transition-colors"
        >
          <span>View Foundations Overview</span>
          <ArrowRight size={12} className="transition-transform group-hover:translate-x-0.5" />
        </Link>
      </div>

      {/* 4 Immersive Cinematic Cards */}
      <div className="mt-5 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-4.5">
        {foundationsPathways.map((pathway) => (
          <Link
            key={pathway.title}
            href={pathway.href}
            onClick={onClose}
            className="group relative flex flex-col justify-end w-full min-w-0 aspect-[3/4] overflow-hidden rounded-[2px] border border-[rgba(198,165,92,0.45)] bg-[#120f0d] p-4 sm:p-4.5 shadow-[0_12px_28px_rgba(0,0,0,0.18)] transition-all duration-300 hover:-translate-y-1 hover:border-[#dfc385] hover:shadow-[0_20px_45px_rgba(0,0,0,0.3)]"
          >
            {/* Background Image */}
            <Image
              src={pathway.imageSrc}
              alt={pathway.imageAlt}
              fill
              sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 25vw"
              className="object-cover transition-transform duration-700 ease-out group-hover:scale-108"
              style={{ objectPosition: pathway.objectPosition || "center" }}
            />

            {/* Cinematic Gradient Overlays */}
            <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-black/92 via-black/45 to-black/15 transition-opacity duration-300 group-hover:opacity-95" />
            <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/10" />

            {/* Text & Overlay Content */}
            <div className="relative z-10 flex flex-col justify-end">
              <span className="block text-[9.5px] font-extrabold uppercase tracking-[0.24em] text-[var(--champagne)] mb-1">
                {pathway.tagline}
              </span>
              <p className="font-serif text-xl sm:text-2xl font-bold tracking-tight text-white leading-tight">
                {pathway.title}
              </p>

              {/* Gold Gradient CTA Button Badge */}
              <div className="mt-3.5 inline-flex w-full items-center justify-center gap-2 rounded-[2px] border border-[rgba(223,195,133,0.55)] bg-[linear-gradient(180deg,rgba(198,165,92,0.24)_0%,rgba(146,118,58,0.4)_100%)] px-3 py-2 text-[11px] font-bold uppercase tracking-[0.18em] text-[var(--champagne)] backdrop-blur-sm transition-all duration-200 group-hover:bg-[linear-gradient(180deg,rgba(223,195,133,0.42)_0%,rgba(198,165,92,0.6)_100%)] group-hover:text-white group-hover:border-[#dfc385]">
                <span>{pathway.ctaText}</span>
                <ArrowRight size={12} className="transition-transform duration-200 group-hover:translate-x-1" />
              </div>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}

