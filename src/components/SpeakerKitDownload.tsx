import { Download } from "lucide-react";

type SpeakerKitDownloadProps = {
  title: string;
  href: string;
};

export function SpeakerKitDownload({ title, href }: SpeakerKitDownloadProps) {
  return (
    <a
      href={href}
      download
      className="flex min-h-24 items-center justify-between gap-4 border border-[var(--line)] bg-white p-5 transition hover:border-[var(--champagne)]"
    >
      <span>
        <span className="block font-serif text-2xl text-[var(--ink)]">{title}</span>
        <span className="mt-1 block text-xs font-bold uppercase text-[#7d7164]">
          Planning file
        </span>
      </span>
      <Download className="text-[var(--gold-dark)]" size={22} aria-hidden="true" />
    </a>
  );
}
