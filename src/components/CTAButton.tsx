import Link from "next/link";
import { ArrowUpRight } from "lucide-react";

type CTAButtonProps = {
  href: string;
  children: React.ReactNode;
  variant?: "primary" | "secondary" | "dark";
  className?: string;
};

export function CTAButton({
  href,
  children,
  variant = "primary",
  className = "",
}: CTAButtonProps) {
  const styles = {
    primary:
      "border-transparent bg-[var(--champagne)] text-[var(--ink)] shadow-[0_14px_34px_rgba(155,118,46,0.22)] hover:bg-[#d8b96e]",
    secondary:
      "border-[rgba(155,118,46,0.45)] bg-white/35 text-[var(--ink)] hover:bg-[rgba(198,165,92,0.12)]",
    dark: "border-transparent bg-[var(--ink)] text-[var(--ivory)] shadow-[0_14px_34px_rgba(23,20,18,0.18)] hover:bg-[var(--charcoal)]",
  };

  return (
    <Link
      href={href}
      className={`inline-flex min-h-12 w-full items-center justify-center gap-2 border px-5 py-3 text-center text-sm font-bold uppercase leading-5 transition sm:w-auto ${styles[variant]} ${className}`}
    >
      {children}
      <ArrowUpRight size={17} aria-hidden="true" />
    </Link>
  );
}
