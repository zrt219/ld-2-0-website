type SectionHeaderProps = {
  eyebrow?: string;
  title: string;
  body?: string;
  align?: "left" | "center";
};

export function SectionHeader({
  eyebrow,
  title,
  body,
  align = "left",
}: SectionHeaderProps) {
  return (
    <div className={align === "center" ? "mx-auto max-w-3xl text-center" : "max-w-3xl"}>
      {eyebrow ? (
        <p className="text-sm font-bold uppercase text-[var(--gold-dark)]">
          {eyebrow}
        </p>
      ) : null}
      <h2 className="mt-4 font-serif text-4xl leading-tight text-balance text-[var(--ink)] sm:text-5xl">
        {title}
      </h2>
      {body ? (
        <p className="mt-5 text-base leading-8 text-[#675d50] sm:text-lg">{body}</p>
      ) : null}
    </div>
  );
}
