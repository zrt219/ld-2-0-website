"use client";

import Image from "next/image";
import Link from "next/link";
import { motion } from "framer-motion";
import { ArrowUpRight } from "lucide-react";

export interface PathwayCardItem {
  id: string;
  category: string;
  title: string;
  href: string;
  ctaText: string;
  imageSrc: string;
  imageAlt: string;
  objectPosition?: string;
  description: string;
}

export const pathwayCardItems: PathwayCardItem[] = [
  {
    id: "golf",
    category: "ATHLETE PATHWAY",
    title: "Golf",
    href: "/foundations/golf",
    ctaText: "Explore Golf",
    imageSrc: "/foundations/pathways/golf-pathway.jpg",
    imageAlt: "Competitive golfer swing follow-through at golden sunset",
    objectPosition: "center 30%",
    description: "Mental performance, composure, and repeatable execution for competitive golfers.",
  },
  {
    id: "hockey",
    category: "TEAM PATHWAY",
    title: "Hockey",
    href: "/foundations/hockey",
    ctaText: "Explore Hockey",
    imageSrc: "/foundations/pathways/hockey-pathway.jpg",
    imageAlt: "Elite hockey player jersey #10 standing in packed arena lights",
    objectPosition: "center 20%",
    description: "Pressure regulation, recovery, leadership, and cohesive championship team culture.",
  },
  {
    id: "corporate",
    category: "ORGANIZATIONAL PATHWAY",
    title: "Corporate",
    href: "/foundations/corporate",
    ctaText: "View Corporate",
    imageSrc: "/foundations/pathways/corporate-pathway.jpg",
    imageAlt: "Executive speaker addressing high-level corporate audience",
    objectPosition: "center 20%",
    description: "Executive composure, poise under high-stakes pressure, and corporate leadership excellence.",
  },
  {
    id: "europe",
    category: "EUROPEAN PARTNERSHIPS",
    title: "Europe",
    href: "/foundations/europe",
    ctaText: "Explore Europe",
    imageSrc: "/foundations/pathways/europe-pathway.jpg",
    imageAlt: "Sunlit luxury European lounge with international flags overlooking historic cathedral waterfront",
    objectPosition: "center 25%",
    description: "International athletic development, multi-nation partnerships, and European federations.",
  },
];

export function FoundationsPathwayCards() {
  return (
    <div className="mt-12 sm:mt-16 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 sm:gap-7 lg:gap-8 max-w-7xl mx-auto">
      {pathwayCardItems.map((item, index) => (
        <motion.div
          key={item.id}
          initial={{ opacity: 0, y: 28 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-40px" }}
          transition={{ duration: 0.55, delay: index * 0.12, ease: [0.22, 1, 0.36, 1] }}
          whileHover={{ y: -10 }}
          className="relative group w-full"
        >
          <Link
            href={item.href}
            className="relative flex flex-col justify-end w-full min-w-0 aspect-[10/16] sm:aspect-[10/15] overflow-hidden rounded-[4px] border border-[rgba(198,165,92,0.45)] bg-[#120f0d] p-5 sm:p-6 lg:p-6.5 shadow-[0_20px_50px_rgba(0,0,0,0.32)] transition-all duration-500 group-hover:border-[#dfc385] group-hover:shadow-[0_32px_75px_rgba(198,165,92,0.28)] block"
          >
            {/* Background Photographic Asset */}
            <Image
              src={item.imageSrc}
              alt={item.imageAlt}
              fill
              unoptimized
              sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 25vw"
              className="object-cover transition-transform duration-700 ease-out group-hover:scale-110"
              style={{ objectPosition: item.objectPosition || "center 20%" }}
            />

            {/* Cinematic Gradient Overlays */}
            <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-black/95 via-black/50 to-black/15 transition-opacity duration-300 group-hover:opacity-90" />
            <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/10 group-hover:ring-[rgba(223,195,133,0.35)] transition-all duration-300" />

            {/* Glowing Accent Aura on Hover */}
            <div className="pointer-events-none absolute -inset-px rounded-[4px] opacity-0 transition-opacity duration-500 group-hover:opacity-100 bg-[radial-gradient(ellipse_at_bottom,rgba(223,195,133,0.22)_0%,transparent_70%)]" />

            {/* Card Content */}
            <div className="relative z-10 flex flex-col justify-end">
              <span className="block text-[10.5px] font-extrabold uppercase tracking-[0.24em] text-[var(--champagne)] mb-2">
                {item.category}
              </span>
              <p className="font-serif text-2xl sm:text-3xl lg:text-[2rem] font-bold tracking-tight text-white leading-tight">
                {item.title}
              </p>
              <p className="mt-2 text-xs text-[#cfc5b4] leading-relaxed line-clamp-2 opacity-90 transition-opacity duration-300 group-hover:opacity-100">
                {item.description}
              </p>

              {/* Pulsing Eager CTA Button */}
              <div className="mt-4 sm:mt-5 inline-flex w-full items-center justify-center gap-2 rounded-[3px] border border-[rgba(223,195,133,0.65)] bg-[linear-gradient(180deg,rgba(198,165,92,0.28)_0%,rgba(146,118,58,0.52)_100%)] px-3 py-2.5 text-[11px] sm:text-xs font-bold uppercase tracking-[0.16em] text-[var(--champagne)] backdrop-blur-md shadow-lg transition-all duration-300 group-hover:bg-[linear-gradient(180deg,rgba(223,195,133,0.55)_0%,rgba(198,165,92,0.85)_100%)] group-hover:text-white group-hover:border-[#f3dfa7] group-hover:shadow-[0_0_24px_rgba(223,195,133,0.45)]">
                <span>{item.ctaText}</span>
                <motion.span
                  className="inline-flex items-center"
                  animate={{ x: [0, 3, 0] }}
                  transition={{ repeat: Infinity, duration: 1.8, ease: "easeInOut" }}
                >
                  <ArrowUpRight size={15} className="transition-transform duration-300 group-hover:translate-x-0.5 group-hover:-translate-y-0.5" />
                </motion.span>
              </div>
            </div>
          </Link>
        </motion.div>
      ))}
    </div>
  );
}
