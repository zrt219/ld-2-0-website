"use client";

import { motion, useScroll, useSpring, useReducedMotion } from "framer-motion";

interface ScrollProgressBarProps {
  className?: string;
  topOffset?: string;
}

/**
 * Luxury hairline scroll indicator for high-intent editorial and foundations pages.
 * Smoothly tracks reading progress using spring physics while respecting reduced-motion preferences.
 */
export function ScrollProgressBar({
  className = "",
  topOffset = "top-0",
}: ScrollProgressBarProps) {
  const { scrollYProgress } = useScroll();
  const scaleX = useSpring(scrollYProgress, {
    stiffness: 140,
    damping: 30,
    restDelta: 0.001,
  });
  const reduce = useReducedMotion();

  if (reduce) {
    return null;
  }

  return (
    <div
      className={`fixed ${topOffset} left-0 right-0 z-[60] h-[2.5px] pointer-events-none ${className}`}
      aria-hidden="true"
    >
      <motion.div
        style={{ scaleX }}
        className="h-full w-full origin-left bg-gradient-to-r from-[var(--champagne)] via-[#e2c785] to-[var(--gold-dark)] shadow-[0_1px_8px_rgba(198,165,92,0.45)]"
      />
    </div>
  );
}
