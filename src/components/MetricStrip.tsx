import { metrics } from "@/content/site";

export function MetricStrip() {
  return (
    <section className="bg-[var(--ink)] text-[var(--ivory)]">
      <div className="mx-auto grid max-w-7xl gap-px px-4 sm:px-6 md:grid-cols-4 lg:px-8">
        {metrics.map((metric) => (
          <div
            key={metric.label}
            className="border-x border-white/10 py-8 text-center"
          >
            <p className="font-serif text-5xl text-[var(--champagne)]">
              {metric.value}
            </p>
            <p className="mt-3 text-sm font-semibold uppercase text-[#d8cdbb]">
              {metric.label}
            </p>
          </div>
        ))}
      </div>
    </section>
  );
}
