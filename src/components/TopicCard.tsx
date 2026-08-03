import { ArrowUpRight } from "lucide-react";
import Link from "next/link";

type TopicCardProps = {
  title: string;
  body: string;
  href: string;
};

export function TopicCard({ title, body, href }: TopicCardProps) {
  return (
    <article className="group flex min-h-64 flex-col border border-[var(--line)] bg-white/[0.82] p-6 shadow-[0_18px_60px_rgba(23,20,18,0.06)] transition hover:-translate-y-1 hover:border-[var(--champagne)] hover:bg-white hover:shadow-[0_24px_70px_rgba(23,20,18,0.1)]">
      <h3 className="font-serif text-2xl text-[var(--ink)]">{title}</h3>
      <p className="mt-4 text-sm leading-7 text-[#675d50]">{body}</p>
      <Link
        href={href}
        className="mt-auto inline-flex items-center gap-2 pt-6 text-sm font-bold uppercase text-[var(--gold-dark)]"
      >
        Learn More
        <ArrowUpRight size={16} aria-hidden="true" />
      </Link>
    </article>
  );
}
