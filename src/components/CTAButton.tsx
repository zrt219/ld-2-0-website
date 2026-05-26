import Link from "next/link";
import { ArrowUpRight } from "lucide-react";

type CTAButtonProps = {
  href: string;
  children: React.ReactNode;
  variant?: "primary" | "secondary" | "dark";
  size?: "default" | "large";
  className?: string;
};

export function CTAButton({
  href,
  children,
  variant = "primary",
  size = "default",
  className = "",
}: CTAButtonProps) {
  const styles = {
    primary:
      "border-transparent bg-[var(--champagne)] text-[var(--ink)] shadow-[0_14px_34px_rgba(155,118,46,0.22)] hover:bg-[#d8b96e]",
    secondary:
      "border-[rgba(155,118,46,0.45)] bg-white/35 text-[var(--ink)] hover:bg-[rgba(198,165,92,0.12)]",
    dark: "border-transparent bg-[var(--ink)] text-[var(--ivory)] shadow-[0_14px_34px_rgba(23,20,18,0.18)] hover:bg-[var(--charcoal)]",
  };
  const sizes = {
    default: "min-h-12 px-5 py-3 text-sm leading-5",
    large: "min-h-14 px-7 py-4 text-base leading-6",
  };

  return (
    <Link
      href={href}
      className={`inline-flex w-full items-center justify-center gap-2 border text-center font-bold uppercase transition sm:w-auto ${sizes[size]} ${styles[variant]} ${className}`}
    >
      {children}
      <ArrowUpRight size={size === "large" ? 19 : 17} aria-hidden="true" />
    </Link>
  );
}
