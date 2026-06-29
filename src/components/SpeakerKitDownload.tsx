import { ArrowRight, Download } from "lucide-react";

type SpeakerKitDownloadProps = {
  title: string;
  href: string;
};

export function SpeakerKitDownload({ title, href }: SpeakerKitDownloadProps) {
  const isExternal = href.startsWith("http://") || href.startsWith("https://");
  const Icon = isExternal ? ArrowRight : Download;

  return (
    <a
      href={href}
      download={isExternal ? undefined : true}
      rel={isExternal ? "noreferrer" : undefined}
      className="flex min-h-24 items-center justify-between gap-4 border border-[var(--line)] bg-white p-5 transition hover:border-[var(--champagne)]"
    >
      <span className="block font-serif text-2xl text-[var(--ink)]">{title}</span>
      <Icon className="text-[var(--gold-dark)]" size={22} aria-hidden="true" />
    </a>
  );
}
