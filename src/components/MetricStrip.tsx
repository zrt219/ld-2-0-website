"use client";

import { motion, useReducedMotion } from "framer-motion";
import { metrics } from "@/content/site";

export function MetricStrip() {
  const reduce = useReducedMotion();

  return (
    <section className="bg-[var(--ink)] text-[var(--ivory)] overflow-hidden">
      <div className="mx-auto grid max-w-7xl gap-px px-4 sm:px-6 md:grid-cols-4 lg:px-8">
        {metrics.map((metric, idx) => (
          <motion.div
            key={metric.label}
            initial={reduce ? { opacity: 1 } : { opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true, margin: "-30px" }}
            transition={{ duration: 0.5, delay: idx * 0.1, ease: [0.22, 1, 0.36, 1] }}
            whileHover={{ y: -3, transition: { duration: 0.2 } }}
            className="border-x border-white/10 py-8 text-center transition-colors group hover:bg-white/[0.03]"
          >
            <p className="font-serif text-5xl text-[var(--champagne)] group-hover:text-white transition-colors duration-300">
              {metric.value}
            </p>
            <p className="mt-3 text-sm font-semibold uppercase tracking-wider text-[#d8cdbb]">
              {metric.label}
            </p>
          </motion.div>
        ))}
      </div>
    </section>
  );
}

