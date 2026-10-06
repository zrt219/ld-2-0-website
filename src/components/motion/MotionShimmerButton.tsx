"use client";

import Link from "next/link";
import { ArrowUpRight } from "lucide-react";
import { motion, useReducedMotion } from "framer-motion";
import { type ReactNode } from "react";

interface MotionShimmerButtonProps {
  href: string;
  children: ReactNode;
  variant?: "primary" | "secondary" | "dark";
  size?: "default" | "large" | "tall";
  showIcon?: boolean;
  className?: string;
  enableShimmer?: boolean;
}

export function MotionShimmerButton({
  href,
  children,
  variant = "primary",
  size = "default",
  showIcon = true,
  className = "",
  enableShimmer = true,
}: MotionShimmerButtonProps) {
  const reduce = useReducedMotion();

  const styles = {
    primary:
      "border-transparent bg-[linear-gradient(135deg,var(--champagne)_0%,#d8b96e_100%)] text-[var(--ink)] shadow-[0_14px_34px_rgba(155,118,46,0.22)] hover:shadow-[0_22px_44px_rgba(155,118,46,0.32)]",
    secondary:
      "border-[rgba(155,118,46,0.45)] bg-white/35 text-[var(--ink)] hover:bg-[rgba(198,165,92,0.12)] hover:border-[rgba(155,118,46,0.7)]",
    dark: "border-transparent bg-[var(--ink)] text-[var(--ivory)] shadow-[0_14px_34px_rgba(23,20,18,0.18)] hover:bg-[var(--charcoal)]",
  };

  const sizes = {
    default: "min-h-12 px-5 py-3 text-sm leading-5",
    large: "min-h-14 px-7 py-4 text-base leading-6",
    tall: "min-h-16 px-8 py-5 text-base leading-7",
  };

  if (reduce) {
    return (
      <Link
        href={href}
        className={`inline-flex w-full items-center justify-center gap-2 border text-center font-bold uppercase transition-colors sm:w-auto ${sizes[size]} ${styles[variant]} ${className}`}
      >
        {children}
        {showIcon ? <ArrowUpRight size={size === "default" ? 17 : 19} aria-hidden="true" /> : null}
      </Link>
    );
  }

  return (
    <motion.div
      whileHover={{ scale: 1.025, y: -2 }}
      whileTap={{ scale: 0.98 }}
      transition={{ duration: 0.25, ease: [0.22, 1, 0.36, 1] }}
      className="inline-block w-full sm:w-auto"
    >
      <Link
        href={href}
        className={`relative overflow-hidden inline-flex w-full items-center justify-center gap-2 border text-center font-bold uppercase focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)] sm:w-auto ${sizes[size]} ${styles[variant]} ${className}`}
      >
        {enableShimmer && variant === "primary" && (
          <motion.span
            className="pointer-events-none absolute inset-0 -skew-x-12 bg-gradient-to-r from-transparent via-white/40 to-transparent"
            initial={{ x: "-150%" }}
            animate={{ x: "250%" }}
            transition={{
              repeat: Infinity,
              repeatDelay: 4.2,
              duration: 1.4,
              ease: "easeInOut",
            }}
            aria-hidden="true"
          />
        )}
        <span className="relative z-10">{children}</span>
        {showIcon ? (
          <ArrowUpRight
            size={size === "default" ? 17 : 19}
            aria-hidden="true"
            className="relative z-10 transition-transform duration-300 group-hover:translate-x-0.5 group-hover:-translate-y-0.5"
          />
        ) : null}
      </Link>
    </motion.div>
  );
}
