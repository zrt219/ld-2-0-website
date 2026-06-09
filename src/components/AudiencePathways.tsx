"use client";

import Link from "next/link";
import { ArrowUpRight, CheckCircle2 } from "lucide-react";
import { useState } from "react";

type PathwayTopic = {
  title: string;
  body: string;
  href: string;
};

export type AudiencePathway = {
  audience: string;
  title: string;
  description: string;
  primaryHref: string;
  topics: PathwayTopic[];
  proofPoints: string[];
};

type AudiencePathwaysProps = {
  pathways: AudiencePathway[];
};

export function AudiencePathways({ pathways }: AudiencePathwaysProps) {
  const [activeIndex, setActiveIndex] = useState(0);
  const activePathway = pathways[activeIndex] ?? pathways[0];

  function focusTab(index: number) {
    const tab = document.getElementById(`audience-pathway-tab-${index}`);
    tab?.focus();
  }

  function onTabKeyDown(event: React.KeyboardEvent<HTMLButtonElement>, index: number) {
    const lastIndex = pathways.length - 1;
    let nextIndex = index;

    if (event.key === "ArrowRight" || event.key === "ArrowDown") {
      nextIndex = index === lastIndex ? 0 : index + 1;
    } else if (event.key === "ArrowLeft" || event.key === "ArrowUp") {
      nextIndex = index === 0 ? lastIndex : index - 1;
    } else if (event.key === "Home") {
      nextIndex = 0;
    } else if (event.key === "End") {
      nextIndex = lastIndex;
    } else {
      return;
    }

    event.preventDefault();
    setActiveIndex(nextIndex);
    focusTab(nextIndex);
  }

  if (!activePathway) {
    return null;
  }

  return (
    <section className="bg-[var(--sand)] px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
      <div className="mx-auto max-w-7xl">
        <div className="grid gap-10 lg:grid-cols-[0.78fr_1.22fr] lg:items-start">
          <div className="max-w-2xl">
            <p className="text-sm font-bold uppercase text-[var(--gold-dark)]">
              Find the Right Message
            </p>
            <h2 className="mt-4 font-serif text-4xl leading-tight text-balance text-[var(--ink)] sm:text-5xl">
              Choose talks that meet your audience where they are.
            </h2>
            <p className="mt-5 text-base leading-8 text-[#675d50] sm:text-lg">
              Select your audience to see the themes, credentials, and next steps
              that match your event.
            </p>
          </div>

          <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3" role="tablist" aria-label="Audience pathway options">
            {pathways.map((pathway, index) => {
              const selected = index === activeIndex;

              return (
                <button
                  id={`audience-pathway-tab-${index}`}
                  key={pathway.audience}
                  type="button"
                  role="tab"
                  aria-selected={selected}
                  aria-controls="audience-pathway-panel"
                  tabIndex={selected ? 0 : -1}
                  onClick={() => setActiveIndex(index)}
                  onKeyDown={(event) => onTabKeyDown(event, index)}
                  className={`min-h-24 border px-4 py-4 text-left transition focus:outline-none focus:ring-4 focus:ring-[rgba(198,165,92,0.24)] ${
                    selected
                      ? "border-[var(--champagne)] bg-[var(--ink)] text-[var(--ivory)] shadow-[0_22px_70px_rgba(23,20,18,0.16)]"
                      : "border-[rgba(198,165,92,0.36)] bg-white/80 text-[var(--ink)] hover:border-[var(--champagne)] hover:bg-white"
                  }`}
                >
                  <span
                    className={`block text-[0.68rem] font-bold uppercase tracking-[0.2em] ${
                      selected ? "text-[var(--champagne)]" : "text-[var(--gold-dark)]"
                    }`}
                  >
                    Audience {String(index + 1).padStart(2, "0")}
                  </span>
                  <span className="mt-3 block font-serif text-xl leading-tight">
                    {pathway.audience}
                  </span>
                </button>
              );
            })}
          </div>
        </div>

        <div
          id="audience-pathway-panel"
          role="tabpanel"
          aria-labelledby={`audience-pathway-tab-${activeIndex}`}
          tabIndex={0}
          className="mt-10 grid overflow-hidden border border-[rgba(198,165,92,0.42)] bg-white shadow-[0_24px_90px_rgba(23,20,18,0.08)] lg:grid-cols-[0.9fr_1.1fr]"
        >
          <div className="bg-[var(--ink)] p-7 text-[var(--ivory)] sm:p-9 lg:p-10">
            <p className="text-xs font-bold uppercase tracking-[0.2em] text-[var(--champagne)]">
              Audience Focus
            </p>
            <h3 className="mt-4 font-serif text-4xl leading-tight text-white">
              {activePathway.title}
            </h3>
            <p className="mt-5 text-base leading-8 text-[#d8cdbb]">
              {activePathway.description}
            </p>

            <div className="mt-8 grid gap-3">
              {activePathway.proofPoints.map((point) => (
                <div key={point} className="flex gap-3 border-t border-white/10 pt-3 text-sm font-semibold leading-6 text-[#efe5d4]">
                  <CheckCircle2 className="mt-0.5 h-5 w-5 shrink-0 text-[var(--champagne)]" aria-hidden="true" />
                  <span>{point}</span>
                </div>
              ))}
            </div>

            <div className="mt-9 flex flex-col gap-3 sm:flex-row">
              <Link
                href="/book"
                className="inline-flex min-h-12 items-center justify-center gap-2 border border-transparent bg-[var(--champagne)] px-5 py-3 text-center text-sm font-bold uppercase leading-5 text-[var(--ink)] shadow-[0_14px_34px_rgba(155,118,46,0.22)] transition hover:bg-[#d8b96e]"
              >
                Inquire About Availability
                <ArrowUpRight size={17} aria-hidden="true" />
              </Link>
              <Link
                href="/speaker-kit"
                className="inline-flex min-h-12 items-center justify-center gap-2 border border-white/20 px-5 py-3 text-center text-sm font-bold uppercase leading-5 text-[var(--ivory)] transition hover:border-[var(--champagne)] hover:text-[var(--champagne)]"
              >
                Speaker Kit
                <ArrowUpRight size={17} aria-hidden="true" />
              </Link>
            </div>
          </div>

          <div className="p-6 sm:p-8 lg:p-10">
            <div className="flex flex-col gap-4 border-b border-[var(--line)] pb-6 sm:flex-row sm:items-end sm:justify-between">
              <div>
                <p className="text-xs font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)]">
                  Talks That Fit
                </p>
                <p className="mt-2 text-sm leading-7 text-[#675d50]">
                  When a topic feels right, share your event details and Lornette&apos;s
                  team can shape the next step.
                </p>
              </div>
              <Link
                href={activePathway.primaryHref}
                className="inline-flex items-center gap-2 text-sm font-bold uppercase text-[var(--gold-dark)]"
              >
                Explore This Audience
                <ArrowUpRight size={16} aria-hidden="true" />
              </Link>
            </div>

            <div className="mt-6 grid gap-4">
              {activePathway.topics.map((topic, index) => (
                <Link
                  key={`${activePathway.audience}-${topic.title}`}
                  href={topic.href}
                  className="group grid gap-4 border border-[var(--line)] bg-[var(--ivory)] p-5 transition hover:border-[var(--champagne)] hover:bg-white sm:grid-cols-[3.5rem_1fr_auto] sm:items-start"
                >
                  <span className="font-serif text-4xl leading-none text-[rgba(155,118,46,0.42)]">
                    {index + 1}
                  </span>
                  <span>
                    <span className="block font-serif text-2xl leading-tight text-[var(--ink)]">
                      {topic.title}
                    </span>
                    <span className="mt-2 block text-sm leading-7 text-[#675d50]">
                      {topic.body}
                    </span>
                  </span>
                  <span className="hidden h-10 w-10 items-center justify-center border border-[rgba(155,118,46,0.3)] text-[var(--gold-dark)] transition group-hover:bg-[var(--champagne)] group-hover:text-[var(--ink)] sm:inline-flex">
                    <ArrowUpRight size={16} aria-hidden="true" />
                  </span>
                </Link>
              ))}
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
