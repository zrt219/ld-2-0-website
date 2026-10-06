"use client";

import { motion, useReducedMotion } from "framer-motion";
import { type ReactNode } from "react";

interface MotionFadeInProps {
  children: ReactNode;
  delay?: number;
  duration?: number;
  yOffset?: number;
  className?: string;
  viewportMargin?: string;
  id?: string;
}

export function MotionFadeIn({
  children,
  delay = 0,
  duration = 0.55,
  yOffset = 24,
  className = "",
  viewportMargin = "-30px",
  id,
}: MotionFadeInProps) {
  const reduce = useReducedMotion();

  if (reduce) {
    return <div id={id} className={className}>{children}</div>;
  }

  return (
    <motion.div
      id={id}
      initial={{ opacity: 0, y: yOffset }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: viewportMargin }}
      transition={{ duration, delay, ease: [0.22, 1, 0.36, 1] }}
      className={className}
    >
      {children}
    </motion.div>
  );
}
