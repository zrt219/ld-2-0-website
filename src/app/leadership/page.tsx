import { PageShell } from "@/components/PageShell";
import { ServicePage } from "@/components/ServicePage";
import { createMetadata, servicePages } from "@/content/site";

export const metadata = createMetadata(
  "Resilient Leadership",
  "Workshops that help leaders communicate clearly, build trust, and stay steady under pressure.",
  "/leadership",
);

export default function LeadershipPage() {
  return (
    <PageShell>
      <ServicePage page={servicePages.leadership} />
    </PageShell>
  );
}
