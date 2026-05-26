"use client";

import { ChevronDown } from "lucide-react";
import { useState } from "react";

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

export function FAQAccordion() {
  const [open, setOpen] = useState(0);

  return (
    <div className="divide-y divide-[var(--line)] border-y border-[var(--line)]">
      {faqs.map((faq, index) => (
        <div key={faq.q}>
          <button
            type="button"
            onClick={() => setOpen(open === index ? -1 : index)}
            className="flex w-full items-center justify-between gap-4 py-5 text-left font-semibold"
            aria-expanded={open === index}
          >
            {faq.q}
            <ChevronDown
              size={18}
              aria-hidden="true"
              className={`shrink-0 transition ${open === index ? "rotate-180" : ""}`}
            />
          </button>
          {open === index ? (
            <p className="pb-5 text-sm leading-7 text-[#675d50]">{faq.a}</p>
          ) : null}
        </div>
      ))}
    </div>
  );
}
