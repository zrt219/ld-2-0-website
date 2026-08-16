import { ArrowUpRight } from "lucide-react";
import Link from "next/link";

type TopicCardProps = {
  title: string;
  body: string;
  href: string;
};

export function TopicCard({ title, body, href }: TopicCardProps) {
  return (
    <article className="group flex min-h-64 flex-col border border-[var(--line)] bg-white/[0.82] p-6 shadow-[0_18px_60px_rgba(23,20,18,0.06)] transition-all duration-500 ease-out hover:-translate-y-1.5 hover:border-[rgba(198,165,92,0.6)] hover:bg-white hover:shadow-[0_32px_80px_rgba(198,165,92,0.12)]">
      <h3 className="font-serif text-2xl text-[var(--ink)]">{title}</h3>
      <p className="mt-4 text-sm leading-7 text-[#675d50]">{body}</p>
      <Link
        href={href}
        className="mt-auto inline-flex items-center gap-2 pt-6 text-sm font-bold uppercase text-[var(--gold-dark)] transition-transform duration-300 group-hover:translate-x-1"
      >
        Learn More
        <ArrowUpRight size={16} aria-hidden="true" />
      </Link>
    </article>
  );
}
