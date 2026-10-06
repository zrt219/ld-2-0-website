"use client";

import Image from "next/image";
import { motion, useReducedMotion } from "framer-motion";

/**
 * Renders the authentic LD monogram signature in gold with an organic glowing effect.
 * Uses a transparent PNG with no box or background.
 */
export function GlowMonogram({ className = "" }: { className?: string }) {
  const reduce = useReducedMotion();

  const restGlow =
    "drop-shadow(0 0 4px rgba(235,210,145,0.7)) drop-shadow(0 0 12px rgba(198,165,92,0.45))";
  const peakGlow =
    "drop-shadow(0 0 8px rgba(250,230,175,0.95)) drop-shadow(0 0 22px rgba(215,185,110,0.75))";
  const hoverGlow =
    "drop-shadow(0 0 10px rgba(255,240,195,1)) drop-shadow(0 0 28px rgba(235,200,120,0.9))";

  return (
    <motion.div
      className={`relative shrink-0 flex items-center justify-center ${className}`}
      initial={{ opacity: 0, filter: restGlow }}
      whileInView={{ opacity: 1 }}
      viewport={{ once: true }}
      animate={
        reduce
          ? { filter: restGlow }
          : { filter: [restGlow, peakGlow, restGlow] }
      }
      transition={
        reduce
          ? { duration: 0.4 }
          : {
              filter: {
                duration: 3.5,
                repeat: Infinity,
                ease: "easeInOut",
              },
              opacity: { duration: 0.6 },
            }
      }
      whileHover={{
        filter: hoverGlow,
        scale: 1.04,
        transition: { duration: 0.25 },
      }}
      role="img"
      aria-label="Lornette Daye LD monogram logo"
    >
      <Image
        src="/ld-monogram-gold-clean.png"
        alt="Lornette Daye LD Monogram"
        width={369}
        height={186}
        priority
        unoptimized
        className="h-full w-auto max-w-full object-contain select-none pointer-events-none"
      />
    </motion.div>
  );
}
