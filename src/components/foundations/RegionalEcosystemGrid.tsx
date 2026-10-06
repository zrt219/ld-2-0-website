"use client";

import Image from "next/image";
import { motion, useReducedMotion } from "framer-motion";
import { MapPin, CheckCircle2 } from "lucide-react";

interface RegionalCard {
  id: string;
  eyebrow: string;
  title: string;
  regionLabel: string;
  description: string;
  image: string;
  objectPosition?: string;
  highlights: string[];
}

const REGIONAL_ECOSYSTEMS: RegionalCard[] = [
  {
    id: "mediterranean-basin",
    eyebrow: "ACADEMY HERITAGE & POISE",
    title: "Mediterranean Basin & Southern Maritime Hubs",
    regionLabel: "Southern European & Maritime Athletic Centers",
    description:
      "Historic sports academies, coastal training complexes, and multi-sport development centers cultivating athletic poise, emotional regulation, and long-term talent retention.",
    image: "/foundations/europe/italy-sports-partnership.png",
    objectPosition: "center 25%",
    highlights: [
      "Holistic Athletic Poise & Composure",
      "Academy Development Pathways",
      "Coastal High-Performance Conditioning",
    ],
  },
  {
    id: "nordic-baltic",
    eyebrow: "APPLIED PERFORMANCE SCIENCE",
    title: "Nordic & Baltic Applied Science Centers",
    regionLabel: "Northern & Baltic High-Performance Hubs",
    description:
      "Advanced sports science networks, physiological testing centers, and endurance traditions exploring modern mental performance models, bio-data integration, and resilient athlete well-being.",
    image: "/foundations/europe/finland-sports-innovation.png",
    objectPosition: "center 35%",
    highlights: [
      "Biomechanics & Movement Analysis",
      "Data-Informed Training Environments",
      "Somatic Reset & Focus Protocols",
    ],
  },
  {
    id: "central-western",
    eyebrow: "TRANS-REGIONAL ALLIANCES",
    title: "Central & Western European Corridor",
    regionLabel: "Central & Western European Performance Networks",
    description:
      "Continental sports institutes, multi-club development networks, and athletic academies advancing dual-career education, coach leadership standards, and championship culture.",
    image: "/foundations/europe/lornette-europe-continental-briefing.jpg",
    objectPosition: "center 20%",
    highlights: [
      "Dual-Career Athlete Development",
      "Transatlantic Knowledge Exchange",
      "High-Standard Coaching Frameworks",
    ],
  },
];

export function RegionalEcosystemGrid() {
  const reduce = useReducedMotion();

  return (
    <div className="mt-12">
      <div className="grid gap-8 sm:grid-cols-2 lg:grid-cols-3">
        {REGIONAL_ECOSYSTEMS.map((card, idx) => (
          <motion.div
            key={card.id}
            initial={reduce ? { opacity: 1 } : { opacity: 0, y: 22 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-30px" }}
            transition={{ duration: 0.5, delay: idx * 0.12, ease: [0.22, 1, 0.36, 1] }}
            whileHover={reduce ? undefined : { y: -6, transition: { duration: 0.25 } }}
            className="group flex flex-col overflow-hidden border border-[rgba(198,165,92,0.36)] bg-white shadow-[0_16px_50px_rgba(23,20,18,0.06)] transition-all duration-300 hover:border-[#dfc385] hover:shadow-[0_24px_60px_rgba(23,20,18,0.14)]"
          >
            {/* Card Image with Docked Luxury Editorial Plaque */}
            <div className="relative aspect-[16/10] sm:aspect-[4/3] w-full overflow-hidden bg-[#120f0d]">
              <Image
                src={card.image}
                alt={card.title}
                fill
                sizes="(max-width: 1024px) 100vw, 33vw"
                className="object-cover transition-transform duration-700 ease-out group-hover:scale-105"
                style={{ objectPosition: card.objectPosition ?? "center" }}
              />
              <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-black/85 via-black/25 to-transparent opacity-80 group-hover:opacity-70 transition-opacity" />
              <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/10" />

              {/* Docked Luxury Editorial Plaque */}
              <div className="absolute inset-x-0 bottom-0 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(18,15,13,0.86)] p-4 backdrop-blur-md shadow-2xl">
                <p className="text-[10px] font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
                  {card.eyebrow}
                </p>
                <p className="mt-1 font-serif text-base text-white leading-snug">
                  {card.title}
                </p>
              </div>
            </div>

            {/* Card Content */}
            <div className="flex flex-1 flex-col justify-between p-6 bg-[linear-gradient(180deg,#fffdfa_0%,#faf6ee_100%)]">
              <div>
                <div className="flex items-center gap-1.5 text-xs font-semibold text-[var(--gold-dark)] mb-2.5">
                  <MapPin size={13} className="shrink-0" />
                  <span>{card.regionLabel}</span>
                </div>
                <p className="text-sm leading-relaxed text-[#554b40]">
                  {card.description}
                </p>
              </div>

              {/* Highlights */}
              <div className="mt-5 border-t border-[rgba(198,165,92,0.22)] pt-4">
                <p className="text-[10px] font-bold uppercase tracking-[0.2em] text-[#7d7164] mb-2.5">
                  Collaboration Focus
                </p>
                <ul className="space-y-1.5">
                  {card.highlights.map((item) => (
                    <li key={item} className="flex items-start gap-2 text-xs text-[#5e5346]">
                      <CheckCircle2 size={13} className="text-[var(--gold-dark)] shrink-0 mt-0.5" />
                      <span>{item}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          </motion.div>
        ))}
      </div>
    </div>
  );
}

