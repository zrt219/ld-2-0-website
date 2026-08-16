import { Quote } from "lucide-react";

type TestimonialCardProps = {
  quote: string;
  name: string;
  context: string;
  category?: string;
  className?: string;
};

export function TestimonialCard({
  quote,
  name,
  context,
  category,
  className = "",
}: TestimonialCardProps) {
  return (
    <figure className={`border border-[rgba(198,165,92,0.4)] bg-white p-6 shadow-[0_18px_70px_rgba(23,20,18,0.07)] ${className}`}>
      <div className="flex items-start justify-between gap-4">
        <Quote className="text-[var(--champagne)]" size={28} aria-hidden="true" />
        {category ? (
          <span className="border border-[rgba(198,165,92,0.34)] px-3 py-1 text-[0.64rem] font-bold uppercase tracking-[0.16em] text-[var(--gold-dark)]">
            {category}
          </span>
        ) : null}
      </div>
      <blockquote className="mt-5 text-base leading-8 text-[var(--charcoal)]">
        &quot;{quote}&quot;
      </blockquote>
      <figcaption className="mt-6 border-t border-[var(--line)] pt-4">
        <p className="font-serif text-2xl text-[var(--ink)]">{name}</p>
        <p className="mt-1 text-xs font-semibold uppercase text-[#7d7164]">
          {context}
        </p>
      </figcaption>
    </figure>
  );
}
