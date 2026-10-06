"use client";

import { ChevronDown } from "lucide-react";
import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";

const faqs = [
  {
    q: "How far in advance should we book?",
    a: "Share your timing as early as possible. Preferred and alternate dates help Lornette's team respond with a clear next step.",
  },
  {
    q: "What formats are available?",
    a: "Keynotes, workshops, panels, virtual or hybrid sessions, retreats, school programs, and coaching-focused sessions can be scoped through the inquiry form.",
  },
  {
    q: "Can we request a custom topic?",
    a: "Yes. Share the audience, event goals, and the outcome you want the room to leave with.",
  },
  {
    q: "What happens if email delivery is not configured?",
    a: "The site prepares a mailto fallback with the inquiry details so the request is never silently lost.",
  },
];

export interface FAQItem {
  q?: string;
  question?: string;
  a?: string;
  answer?: string;
}

interface FAQAccordionProps {
  items?: FAQItem[];
  variant?: "default" | "boxed";
}

export function FAQAccordion({ items = faqs, variant = "default" }: FAQAccordionProps) {
  const [open, setOpen] = useState<number | null>(0);

  const normalizedItems = items.map((item) => ({
    q: item.q || item.question || "",
    a: item.a || item.answer || "",
  }));

  if (variant === "boxed") {
    return (
      <div className="space-y-4">
        {normalizedItems.map((faq, index) => {
          const isOpen = open === index;
          return (
            <div
              key={faq.q}
              className={`rounded-sm border bg-white p-5 sm:p-6 shadow-sm transition-colors duration-200 ${
                isOpen ? "border-[var(--champagne)]" : "border-[rgba(198,165,92,0.35)]"
              }`}
            >
              <button
                id={`faq-trigger-${index}`}
                type="button"
                onClick={() => setOpen(isOpen ? null : index)}
                className="flex w-full items-center justify-between text-left font-serif text-base sm:text-lg font-medium text-[var(--ink)] hover:text-[var(--gold-dark)] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)] select-none cursor-pointer"
                aria-expanded={isOpen}
                aria-controls={`faq-panel-${index}`}
              >
                <span>{faq.q}</span>
                <motion.div
                  animate={{ rotate: isOpen ? 180 : 0 }}
                  transition={{ duration: 0.25, ease: "easeInOut" }}
                  className="shrink-0 ml-4"
                >
                  <ChevronDown
                    size={18}
                    aria-hidden="true"
                    className="text-[var(--gold-dark)]"
                  />
                </motion.div>
              </button>
              <AnimatePresence initial={false}>
                {isOpen && (
                  <motion.div
                    id={`faq-panel-${index}`}
                    role="region"
                    aria-labelledby={`faq-trigger-${index}`}
                    initial={{ opacity: 0, height: 0 }}
                    animate={{ opacity: 1, height: "auto" }}
                    exit={{ opacity: 0, height: 0 }}
                    transition={{ duration: 0.3, ease: [0.22, 1, 0.36, 1] }}
                    className="overflow-hidden"
                  >
                    <p className="mt-4 text-sm leading-7 text-[#554a3e] border-t border-[var(--line)] pt-4">
                      {faq.a}
                    </p>
                  </motion.div>
                )}
              </AnimatePresence>
            </div>
          );
        })}
      </div>
    );
  }

  return (
    <div className="divide-y divide-[var(--line)] border-y border-[var(--line)]">
      {normalizedItems.map((faq, index) => {
        const isOpen = open === index;
        return (
          <div key={faq.q} className="overflow-hidden">
            <button
              id={`faq-trigger-${index}`}
              type="button"
              onClick={() => setOpen(isOpen ? null : index)}
              className="flex w-full items-center justify-between gap-4 py-5 text-left font-semibold cursor-pointer group"
              aria-expanded={isOpen}
              aria-controls={`faq-panel-${index}`}
            >
              <span className="transition-colors group-hover:text-[var(--gold-dark)]">{faq.q}</span>
              <motion.div
                animate={{ rotate: isOpen ? 180 : 0 }}
                transition={{ duration: 0.25, ease: "easeInOut" }}
                className="shrink-0"
              >
                <ChevronDown
                  size={18}
                  aria-hidden="true"
                  className="text-[var(--gold-dark)]"
                />
              </motion.div>
            </button>
            <AnimatePresence initial={false}>
              {isOpen && (
                <motion.div
                  id={`faq-panel-${index}`}
                  role="region"
                  aria-labelledby={`faq-trigger-${index}`}
                  initial={{ opacity: 0, height: 0 }}
                  animate={{ opacity: 1, height: "auto" }}
                  exit={{ opacity: 0, height: 0 }}
                  transition={{ duration: 0.3, ease: [0.22, 1, 0.36, 1] }}
                  className="overflow-hidden"
                >
                  <p className="pb-5 text-sm leading-7 text-[#675d50]">
                    {faq.a}
                  </p>
                </motion.div>
              )}
            </AnimatePresence>
          </div>
        );
      })}
    </div>
  );
}

