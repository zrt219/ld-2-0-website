"use client";

import { useState } from "react";
import Image from "next/image";
import { motion, AnimatePresence, useReducedMotion } from "framer-motion";
import { MapPin, Globe, Compass, CheckCircle2 } from "lucide-react";

interface RegionalCard {
  id: string;
  country: string;
  eyebrow: string;
  title: string;
  regionLabel: string;
  description: string;
  image: string;
  objectPosition?: string;
  highlights: string[];
}

interface RegionalCluster {
  id: string;
  name: string;
  badge: string;
  tagline: string;
  cards: RegionalCard[];
}

const REGIONAL_CLUSTERS: RegionalCluster[] = [
  {
    id: "mediterranean",
    name: "Mediterranean & Maritime Hubs",
    badge: "2 Regional Ecosystems",
    tagline: "Historic sporting academies, coastal training environments, and holistic athletic development.",
    cards: [
      {
        id: "historic-academies",
        country: "Historic Southern European Academies",
        eyebrow: "ACADEMY HERITAGE & POISE",
        title: "Historic Academies & High-Performance Foundations",
        regionLabel: "Southern European Performance Centers",
        description:
          "Traditional athletic environments and historic sporting academies exploring holistic athlete development, emotional poise, and high-performance leadership.",
        image: "/foundations/europe/italy-sports-partnership.png",
        objectPosition: "center 25%",
        highlights: [
          "Holistic Athletic Poise & Composure",
          "Historic Academy Development Pathways",
          "High-Performance Leadership Systems",
        ],
      },
      {
        id: "maritime-academies",
        country: "Mediterranean Coastal Training Centers",
        eyebrow: "COASTAL ATHLETIC HUBS",
        title: "Athletic Heritage & Coastal Conditioning Hubs",
        regionLabel: "Maritime Coastal & Island Academies",
        description:
          "Ancient athletic heritage combined with modern high-performance coastal conditioning centers and multi-sport youth athlete development environments.",
        image: "/foundations/europe/greece-mediterranean-academy.png",
        objectPosition: "center 30%",
        highlights: [
          "Coastal High-Performance Conditioning",
          "Multi-Sport Youth Athlete Development",
          "Athletic Heritage & Character Foundations",
        ],
      },
    ],
  },
  {
    id: "nordic",
    name: "Nordic & Applied Science Centers",
    badge: "3 Regional Ecosystems",
    tagline: "Endurance traditions, applied sports science laboratories, and community-first club cultures.",
    cards: [
      {
        id: "altitude-endurance",
        country: "Northern Winter & Outdoor Centers",
        eyebrow: "COLD-CLIMATE RESILIENCE",
        title: "Endurance Culture & Environmental Resilience",
        regionLabel: "Northern Altitude & Winter Facilities",
        description:
          "Northern endurance culture and outdoor sport ecosystems focusing on sustainable athletic resilience, recovery systems, and long-term athlete retention.",
        image: "/foundations/europe/norway-nordic-pavilion.png",
        objectPosition: "center 30%",
        highlights: [
          "Environmental Resilience Under Pressure",
          "Sustainable In-Season Recovery Systems",
          "Long-Term Athletic Career Retention",
        ],
      },
      {
        id: "sports-science-tech",
        country: "Sports Science & Technology Centers",
        eyebrow: "APPLIED PERFORMANCE SCIENCE",
        title: "Applied Sports Science & Biomechanics Research",
        regionLabel: "High-Tech Performance Research Centers",
        description:
          "Advanced sport science, physiological testing, and data-informed training environments exploring modern mental performance models.",
        image: "/foundations/europe/finland-sports-innovation.png",
        objectPosition: "center 35%",
        highlights: [
          "Biomechanics & Movement Analysis",
          "Data-Informed Training Environments",
          "Somatic Reset & Focus Protocols",
        ],
      },
      {
        id: "collaborative-clubs",
        country: "Collaborative Club & Academy Systems",
        eyebrow: "CULTURE & WELL-BEING",
        title: "Athlete Well-Being & Collaborative Culture",
        regionLabel: "Integrated Academy & Club Systems",
        description:
          "Community-driven club models and youth development structures prioritizing positive team culture, psychological safety, and athletic longevity.",
        image: "/foundations/europe/denmark-nordic-delegation.png",
        objectPosition: "center 20%",
        highlights: [
          "Club Culture & Mutual Accountability",
          "Psychological Safety in Competition",
          "Youth Talent Development Pathways",
        ],
      },
    ],
  },
  {
    id: "continental",
    name: "Continental & Cross-Border Gateways",
    badge: "2 Regional Ecosystems",
    tagline: "Pan-European athletic policy frameworks and cross-border sports gateways.",
    cards: [
      {
        id: "policy-governance",
        country: "Continental Governance Coordination",
        eyebrow: "TRANS-EUROPEAN FORUMS",
        title: "Multi-Nation Governance & Athletic Standards",
        regionLabel: "Continental Governance & Coordination Centers",
        description:
          "Pan-European policy frameworks and multi-nation sports initiatives advancing coach standards, athletic ethics, and dual-career athlete development.",
        image: "/foundations/europe/lornette-europe-continental-briefing.jpg",
        objectPosition: "center 20%",
        highlights: [
          "Dual-Career Athlete Development",
          "Transatlantic Knowledge Exchange",
          "High-Standard Coaching Frameworks",
        ],
      },
      {
        id: "gateway-academies",
        country: "Cross-Border Performance Academies",
        eyebrow: "MULTI-SPORT GATEWAYS",
        title: "Emerging Performance & Cross-Border Sports Academies",
        regionLabel: "Cross-Border Athletic Exchange Hubs",
        description:
          "Dynamic cross-continental sports academies and emerging performance networks bridging diverse regional traditions of athletic excellence.",
        image: "/foundations/europe/turkiye-innovation-partnership.png",
        objectPosition: "center 30%",
        highlights: [
          "Cross-Border Sports Gateways",
          "Emerging Academy Performance Hubs",
          "Dynamic High-Speed Talent Cultivation",
        ],
      },
    ],
  },
];

export function RegionalEcosystemTabs() {
  const [activeClusterId, setActiveClusterId] = useState<string>("mediterranean");
  const reduce = useReducedMotion();

  const activeCluster =
    REGIONAL_CLUSTERS.find((c) => c.id === activeClusterId) ?? REGIONAL_CLUSTERS[0];

  return (
    <div className="mt-10">
      {/* Cluster Navigation Tabs */}
      <div className="flex flex-wrap items-center justify-center gap-2 sm:gap-3 border-b border-[rgba(198,165,92,0.35)] pb-4">
        {REGIONAL_CLUSTERS.map((cluster) => {
          const isActive = cluster.id === activeClusterId;
          return (
            <button
              key={cluster.id}
              onClick={() => setActiveClusterId(cluster.id)}
              className={`group relative flex items-center gap-2.5 rounded-[2px] px-4 py-2.5 text-xs font-bold uppercase tracking-[0.2em] transition-all duration-200 cursor-pointer ${
                isActive
                  ? "bg-[linear-gradient(180deg,#1f1a16_0%,#120f0d_100%)] text-[var(--champagne)] shadow-md border border-[rgba(198,165,92,0.6)]"
                  : "bg-white/80 text-[#675d50] hover:bg-white hover:text-[var(--ink)] border border-[rgba(198,165,92,0.25)]"
              }`}
            >
              <span>{cluster.name}</span>
              <span
                className={`text-[10px] px-2 py-0.5 rounded-[2px] font-semibold tracking-wider ${
                  isActive
                    ? "bg-[rgba(198,165,92,0.22)] text-[var(--champagne)] border border-[rgba(198,165,92,0.4)]"
                    : "bg-[var(--sand)] text-[#7d7164]"
                }`}
              >
                {cluster.badge}
              </span>
            </button>
          );
        })}
      </div>

      {/* Cluster Subtitle / Tagline */}
      <div className="mt-6 text-center">
        <p className="text-sm font-medium text-[#7d7164] max-w-2xl mx-auto italic">
          {activeCluster.tagline}
        </p>
      </div>

      {/* Cluster Cards Grid with AnimatePresence */}
      <AnimatePresence mode="wait">
        <motion.div
          key={activeCluster.id}
          initial={reduce ? { opacity: 1 } : { opacity: 0, y: 14 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -10 }}
          transition={{ duration: 0.35, ease: [0.22, 1, 0.36, 1] }}
          className={`mt-8 grid gap-8 ${
            activeCluster.cards.length === 3
              ? "sm:grid-cols-2 lg:grid-cols-3"
              : "sm:grid-cols-2 lg:grid-cols-2 max-w-5xl mx-auto"
          }`}
        >
          {activeCluster.cards.map((card, idx) => (
            <motion.div
              key={card.id}
              initial={reduce ? { opacity: 1 } : { opacity: 0, y: 18 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.45, delay: idx * 0.1, ease: [0.22, 1, 0.36, 1] }}
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
        </motion.div>
      </AnimatePresence>
    </div>
  );
}

