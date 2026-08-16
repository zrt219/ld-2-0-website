export type HomeProofSectionProps = {
  title?: string;
  body?: string;
  timelineItems?: readonly HomeProofTimelineItem[];
  className?: string;
};

type HomeProofTimelineItem = {
  years: string;
  title: string;
  detail: string;
  context?: string;
  stat?: {
    value: string;
    label: string;
  };
};

const defaultTimelineItems: readonly HomeProofTimelineItem[] = [
  {
    years: "1979-1981",
    title: "Junior High City Champion",
    detail: "City champion in the 100-metre and 200-metre sprints.",
    context: "Early sprint dominance",
  },
  {
    years: "1981-1984",
    title: "High School Champion Years",
    detail:
      "City champion in the 100-metre and 200-metre sprints, with back-to-back high school volleyball championships in 1983 and 1984.",
    context: "Track and volleyball",
  },
  {
    years: "1983",
    title: "National Record Standard",
    detail:
      "Youth Canadian Nationals 100-metre gold medalist. Her 11.7-second mark stood for 28 years, until 2011.",
    context: "Royal Canadian Legion Youth Nationals",
    stat: {
      value: "11.7s",
      label: "Record stood 28 years",
    },
  },
  {
    years: "1983-1987",
    title: "Summer Games Double Gold",
    detail:
      "Gold medalist in both the 100-metre and 200-metre sprints at the Western Canada Summer Games and the Canada Summer Games.",
    context: "Western Canada and Canada Summer Games",
  },
  {
    years: "1986-1987",
    title: "Team Canada Abroad",
    detail:
      "Represented the Canadian national team in Eastern Europe in 1986 and Western Europe in 1987.",
    context: "International competition",
  },
];

export function HomeProofSection({
  title = "Years of Proof.",
  body = "From provincial and national titles to records broken and defended, she knows what long-term success looks like.",
  timelineItems = defaultTimelineItems,
  className = "",
}: HomeProofSectionProps) {
  return (
    <section className={`bg-white px-4 pb-16 sm:px-6 lg:px-8 lg:pb-24 ${className}`}>
      <div className="mx-auto max-w-7xl">
        <div className="relative overflow-hidden border border-[rgba(198,165,92,0.38)] bg-[linear-gradient(140deg,rgba(255,255,255,0.98)_0%,rgba(250,247,240,0.96)_52%,rgba(232,221,203,0.78)_100%)] p-6 shadow-[0_20px_80px_rgba(23,20,18,0.08)] sm:p-8 lg:p-10">
          <div className="pointer-events-none absolute inset-x-0 top-0 h-px bg-gradient-to-r from-transparent via-[rgba(198,165,92,0.5)] to-transparent" />
          <div className="pointer-events-none absolute -right-24 top-0 h-52 w-52 rounded-full bg-[radial-gradient(circle,rgba(198,165,92,0.18),transparent_68%)]" />

          <div className="relative">
            <div className="min-w-0">
              <h2 className="font-serif text-4xl leading-tight text-balance text-[var(--ink)] sm:text-5xl">
                {title}
              </h2>

              <p className="mt-6 max-w-3xl text-lg leading-8 text-[#5f5548] sm:text-xl sm:leading-9">
                {body}
              </p>

              <ol className="mt-10 border-y border-[rgba(198,165,92,0.32)]">
                {timelineItems.map((item) => (
                  <li
                    key={`${item.years}-${item.title}`}
                    className="grid gap-4 border-t border-[rgba(198,165,92,0.22)] py-6 first:border-t-0 md:grid-cols-[12rem_minmax(0,1fr)] md:gap-8 lg:grid-cols-[14rem_minmax(0,1fr)]"
                  >
                    <div className="md:border-r md:border-[rgba(198,165,92,0.3)] md:pr-8">
                      <p className="font-serif text-4xl leading-none text-[var(--ink)] sm:text-5xl">
                        {item.years}
                      </p>
                    </div>
                    <div className="grid gap-5 lg:grid-cols-[minmax(0,1fr)_auto] lg:items-start">
                      <div>
                        {item.context ? (
                          <p className="text-[11px] font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)]">
                            {item.context}
                          </p>
                        ) : null}
                        <h3 className="mt-2 font-serif text-2xl leading-tight text-[var(--ink)] sm:text-3xl">
                          {item.title}
                        </h3>
                        <p className="mt-3 max-w-3xl text-base leading-8 text-[#5f5548]">
                          {item.detail}
                        </p>
                      </div>

                      {item.stat ? (
                        <div className="border border-[rgba(198,165,92,0.38)] bg-[var(--ink)] px-5 py-4 text-[var(--ivory)] shadow-[0_18px_60px_rgba(23,20,18,0.12)] lg:min-w-44">
                          <p className="font-serif text-5xl leading-none text-[var(--champagne)]">
                            {item.stat.value}
                          </p>
                          <p className="mt-2 text-xs font-bold uppercase leading-5 tracking-[0.18em] text-[rgba(250,247,240,0.78)]">
                            {item.stat.label}
                          </p>
                        </div>
                      ) : null}
                    </div>
                  </li>
                ))}
              </ol>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}
