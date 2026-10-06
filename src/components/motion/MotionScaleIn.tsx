"use client";

import { motion, useReducedMotion } from "framer-motion";
import { type ReactNode } from "react";

interface MotionScaleInProps {
  children: ReactNode;
  delay?: number;
  duration?: number;
  scaleStart?: number;
  className?: string;
  viewportMargin?: string;
  id?: string;
}

export function MotionScaleIn({
  children,
  delay = 0,
  duration = 0.6,
  scaleStart = 0.95,
  className = "",
  viewportMargin = "-30px",
  id,
}: MotionScaleInProps) {
  const reduce = useReducedMotion();

  if (reduce) {
    return <div id={id} className={className}>{children}</div>;
  }

  return (
    <motion.div
      id={id}
      initial={{ opacity: 0, scale: scaleStart }}
      whileInView={{ opacity: 1, scale: 1 }}
      viewport={{ once: true, margin: viewportMargin }}
      transition={{ duration, delay, ease: [0.22, 1, 0.36, 1] }}
      className={className}
    >
      {children}
    </motion.div>
  );
}
