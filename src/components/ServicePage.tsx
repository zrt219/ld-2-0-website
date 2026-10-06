"use client";

import { motion, useReducedMotion } from "framer-motion";
import { mediaItems, type ServicePage as ServicePageData } from "@/content/site";
import { CTAButton } from "./CTAButton";
import { HeroSplit } from "./HeroSplit";
import { SectionHeader } from "./SectionHeader";
import { SpeakerMediaBand } from "./SpeakerMediaBand";

export function ServicePage({ page }: { page: ServicePageData }) {
  const reduce = useReducedMotion();
  const mediaBandProps = page.mediaBand ?? {};

  return (
    <main>
      <HeroSplit
        eyebrow={page.eyebrow}
        title={page.title}
        body={page.description}
        image={page.heroImage}
        primaryLabel={page.cta}
        secondaryHref="/media"
        video={mediaItems[0]}
      />
      <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
        <div className="mx-auto max-w-7xl">
          <SectionHeader
            eyebrow="How Lornette Helps"
            title="Practical sessions shaped around the people in the room."
            body="Each keynote, workshop, or coaching experience connects Lornette's story with tools your audience can use under pressure, through change, and beyond the event."
          />
          <div className="mt-10 grid gap-4 md:grid-cols-5">
            {page.pillars.map((pillar, idx) => (
              <motion.div
                key={pillar}
                initial={reduce ? { opacity: 1 } : { opacity: 0, y: 18 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true, margin: "-30px" }}
                transition={{ duration: 0.45, delay: idx * 0.08, ease: [0.22, 1, 0.36, 1] }}
                whileHover={reduce ? undefined : { y: -4, transition: { duration: 0.2 } }}
                className="border border-[var(--line)] bg-white p-5 text-center font-serif text-xl text-[var(--ink)] shadow-[0_14px_55px_rgba(23,20,18,0.05)] hover:border-[rgba(198,165,92,0.6)] hover:shadow-md transition-all duration-300"
              >
                {pillar}
              </motion.div>
            ))}
          </div>
          <div className="mt-12 grid gap-6 lg:grid-cols-3">
            {page.sections.map((section, idx) => (
              <motion.article
                key={section.title}
                initial={reduce ? { opacity: 1 } : { opacity: 0, y: 22 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true, margin: "-30px" }}
                transition={{ duration: 0.55, delay: idx * 0.12, ease: [0.22, 1, 0.36, 1] }}
                whileHover={reduce ? undefined : { y: -5, transition: { duration: 0.25 } }}
                className="border border-[var(--line)] bg-white p-6 shadow-[0_18px_70px_rgba(23,20,18,0.06)] hover:border-[rgba(198,165,92,0.6)] hover:shadow-lg transition-all duration-300"
              >
                <h2 className="font-serif text-3xl text-[var(--ink)]">
                  {section.title}
                </h2>
                {section.body ? (
                  <p className="mt-4 text-sm leading-7 text-[#675d50]">
                    {section.body}
                  </p>
                ) : null}
                <ul className="mt-6 grid gap-3">
                  {section.items.map((item) => (
                    <li
                      key={item}
                      className="border-l-2 border-[var(--champagne)] pl-3 text-sm font-semibold text-[var(--charcoal)]"
                    >
                      {item}
                    </li>
                  ))}
                </ul>
              </motion.article>
            ))}
          </div>
          <div className="mt-12 border-y border-[rgba(198,165,92,0.5)] py-10">
            <div className="flex flex-col gap-5 lg:flex-row lg:items-center lg:justify-between">
              <p className="max-w-2xl font-serif text-3xl text-[var(--ink)]">
                Ready to shape the right experience for your audience?
              </p>
              <CTAButton href="/book">{page.cta}</CTAButton>
            </div>
          </div>
        </div>
      </section>
      <SpeakerMediaBand
        title="See Lornette's voice, presence, and message."
        body="Watch the reel, explore speaker materials, and start an inquiry when you are ready to talk through the right fit."
        {...mediaBandProps}
      />
    </main>
  );
}

