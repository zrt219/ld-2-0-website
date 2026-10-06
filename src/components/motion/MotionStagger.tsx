"use client";

import { motion, useReducedMotion, type Variants } from "framer-motion";
import { type ReactNode } from "react";

interface MotionStaggerContainerProps {
  children: ReactNode;
  staggerDelay?: number;
  delayChildren?: number;
  className?: string;
  viewportMargin?: string;
  id?: string;
}

const containerVariants = (staggerDelay = 0.08, delayChildren = 0.05): Variants => ({
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: staggerDelay,
      delayChildren,
    },
  },
});

export const itemFadeUpVariants: Variants = {
  hidden: { opacity: 0, y: 22 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.5, ease: [0.22, 1, 0.36, 1] },
  },
};

export function MotionStaggerContainer({
  children,
  staggerDelay = 0.08,
  delayChildren = 0.05,
  className = "",
  viewportMargin = "-40px",
  id,
}: MotionStaggerContainerProps) {
  const reduce = useReducedMotion();

  if (reduce) {
    return <div id={id} className={className}>{children}</div>;
  }

  return (
    <motion.div
      id={id}
      variants={containerVariants(staggerDelay, delayChildren)}
      initial="hidden"
      whileInView="visible"
      viewport={{ once: true, margin: viewportMargin }}
      className={className}
    >
      {children}
    </motion.div>
  );
}

export function MotionStaggerItem({
  children,
  className = "",
  variants = itemFadeUpVariants,
  id,
}: {
  children: ReactNode;
  className?: string;
  variants?: Variants;
  id?: string;
}) {
  const reduce = useReducedMotion();

  if (reduce) {
    return <div id={id} className={className}>{children}</div>;
  }

  return (
    <motion.div id={id} variants={variants} className={className}>
      {children}
    </motion.div>
  );
}
