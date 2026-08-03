import Link from "next/link";
import { CalendarCheck, Play } from "lucide-react";

export function MobileStickyCTA() {
  return (
    <nav
      aria-label="Mobile quick actions"
      className="fixed inset-x-0 bottom-0 z-40 grid grid-cols-2 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(23,20,18,0.94)] p-2 text-sm font-bold uppercase text-[var(--ivory)] shadow-2xl backdrop-blur md:hidden"
    >
      <Link
        href="/media"
        className="flex min-h-12 items-center justify-center gap-2 border border-white/15"
      >
        <Play size={16} aria-hidden="true" />
        Watch Reel
      </Link>
      <Link
        href="/book"
        className="flex min-h-12 items-center justify-center gap-2 bg-[var(--champagne)] text-[var(--ink)]"
      >
        <CalendarCheck size={16} aria-hidden="true" />
        Book Lornette
      </Link>
    </nav>
  );
}
