import { Quote } from "lucide-react";

type TestimonialCardProps = {
  category?: string;
  quote: string;
  name: string;
  context: string;
};

export function TestimonialCard({
  category,
  quote,
  name,
  context,
}: TestimonialCardProps) {
  return (
    <figure className="flex min-h-[344px] flex-col border border-white bg-white p-6 shadow-[0_18px_70px_rgba(23,20,18,0.04)]">
      <div className="flex min-h-6 items-start justify-between gap-4">
        <Quote className="shrink-0 text-[var(--champagne)]" size={26} aria-hidden="true" />
        {category ? (
          <p className="border border-[#e5d5b8] px-4 py-2 text-[0.62rem] font-bold uppercase leading-none tracking-[0.2em] text-[var(--gold-dark)]">
            {category}
          </p>
        ) : null}
      </div>
      <blockquote className="mt-8 text-[0.94rem] leading-8 text-[var(--ink)]">
        &quot;{quote}&quot;
      </blockquote>
      <figcaption className="mt-auto border-t border-[var(--line)] pt-4">
        <p className="font-serif text-2xl text-[var(--ink)]">{name}</p>
        <p className="mt-1 text-[0.65rem] font-semibold uppercase leading-4 text-[#7d7164]">
          {context}
        </p>
      </figcaption>
    </figure>
  );
}
