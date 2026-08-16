import Link from "next/link";
import { ArrowUpRight } from "lucide-react";

type CTAButtonProps = {
  href: string;
  children: React.ReactNode;
  variant?: "primary" | "secondary" | "dark";
  size?: "default" | "large" | "tall";
  showIcon?: boolean;
  className?: string;
};

export function CTAButton({
  href,
  children,
  variant = "primary",
  size = "default",
  showIcon = true,
  className = "",
}: CTAButtonProps) {
  const styles = {
    primary:
      "border-transparent bg-[linear-gradient(135deg,var(--champagne)_0%,#d8b96e_100%)] text-[var(--ink)] shadow-[0_14px_34px_rgba(155,118,46,0.22)] hover:shadow-[0_20px_40px_rgba(155,118,46,0.3)]",
    secondary:
      "border-[rgba(155,118,46,0.45)] bg-white/35 text-[var(--ink)] hover:bg-[rgba(198,165,92,0.12)] hover:border-[rgba(155,118,46,0.7)]",
    dark: "border-transparent bg-[var(--ink)] text-[var(--ivory)] shadow-[0_14px_34px_rgba(23,20,18,0.18)] hover:bg-[var(--charcoal)]",
  };
  const sizes = {
    default: "min-h-12 px-5 py-3 text-sm leading-5",
    large: "min-h-14 px-7 py-4 text-base leading-6",
    tall: "min-h-16 px-8 py-5 text-base leading-7",
  };

  return (
    <Link
      href={href}
      className={`inline-flex w-full items-center justify-center gap-2 border text-center font-bold uppercase transition-all duration-400 ease-out hover:-translate-y-1 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)] active:translate-y-0 sm:w-auto ${sizes[size]} ${styles[variant]} ${className}`}
    >
      {children}
      {showIcon ? <ArrowUpRight size={size === "default" ? 17 : 19} aria-hidden="true" /> : null}
    </Link>
  );
}
