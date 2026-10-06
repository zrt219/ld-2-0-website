"use client";

import { useState } from "react";
import Image from "next/image";

interface VisualPerspective {
  id: "session" | "envoy";
  label: string;
  image: string;
  alt: string;
  objectPosition: string;
  eyebrow: string;
  title: string;
}

const PERSPECTIVES: VisualPerspective[] = [
  {
    id: "session",
    label: "In Session",
    image: "/foundations/europe/lornette-europe-salon-session.jpg",
    alt: "Olympic-level coach Lornette Daye in white suit standing and facilitating an executive salon consultation with European delegates",
    objectPosition: "center 25%",
    eyebrow: "TRANSATLANTIC KNOWLEDGE EXCHANGE",
    title: "Olympic Pedagogy for European Sport Directors",
  },
  {
    id: "envoy",
    label: "Strategic Envoy",
    image: "/foundations/europe/lornette-europe-standing-portrait.jpg",
    alt: "Lornette Daye in white suit standing with hands in pockets in front of European flags and Nordic waterfront skyline",
    objectPosition: "center 20%",
    eyebrow: "EXECUTIVE LEADERSHIP & ENVOY",
    title: "Olympic-Level Coaching & Transatlantic Advisory",
  },
];

export function EuropeanExecutiveVisual() {
  const [activeTab, setActiveTab] = useState<"session" | "envoy">("session");
  const active = PERSPECTIVES.find((p) => p.id === activeTab) || PERSPECTIVES[0];

  return (
    <div className="relative min-h-[380px] sm:min-h-[460px] lg:col-span-5 overflow-hidden bg-[#120f0d]">
      {PERSPECTIVES.map((p) => {
        const isCurrent = p.id === activeTab;
        return (
          <div
            key={p.id}
            id={`perspective-panel-${p.id}`}
            role="tabpanel"
            aria-hidden={!isCurrent}
            className={`absolute inset-0 transition-opacity duration-700 ease-in-out ${
              isCurrent ? "opacity-100 z-10" : "opacity-0 z-0"
            }`}
          >
            <Image
              src={p.image}
              alt={p.alt}
              fill
              sizes="(max-width: 1024px) 100vw, 42vw"
              className="object-cover"
              style={{ objectPosition: p.objectPosition }}
            />
          </div>
        );
      })}

      {/* Subtle border ring without dark tint */}
      <div className="pointer-events-none absolute inset-0 z-20 ring-1 ring-inset ring-white/20" />

      {/* Perspective Toggle Pills */}
      <div
        role="tablist"
        aria-label="Executive leadership perspectives"
        className="absolute top-4 right-4 z-30 flex items-center rounded-full border border-[rgba(198,165,92,0.45)] bg-[rgba(18,15,13,0.85)] p-1 backdrop-blur-md shadow-lg"
      >
        {PERSPECTIVES.map((p) => {
          const isSelected = p.id === activeTab;
          return (
            <button
              key={p.id}
              role="tab"
              aria-selected={isSelected}
              aria-controls={`perspective-panel-${p.id}`}
              aria-label={`View perspective: ${p.label}`}
              type="button"
              onClick={() => setActiveTab(p.id)}
              className={`rounded-full px-3 py-1 text-[10px] font-bold uppercase tracking-[0.18em] transition-all duration-200 ${
                isSelected
                  ? "bg-[linear-gradient(180deg,#c8a96e_0%,#a8894e_100%)] text-[#1a140d] shadow-sm font-extrabold"
                  : "text-white/80 hover:text-white"
              }`}
            >
              {p.label}
            </button>
          );
        })}
      </div>

      {/* Docked Luxury Editorial Plaque */}
      <div className="absolute inset-x-0 bottom-0 z-30 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(18,15,13,0.88)] p-4 sm:p-5 backdrop-blur-md shadow-2xl">
        <p className="text-[10px] font-bold uppercase tracking-[0.22em] text-[var(--champagne)]">
          {active.eyebrow}
        </p>
        <p className="mt-1 font-serif text-base text-white sm:text-lg leading-snug">
          {active.title}
        </p>
      </div>
    </div>
  );
}
