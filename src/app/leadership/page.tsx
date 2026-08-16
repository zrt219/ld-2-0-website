import { PageShell } from "@/components/PageShell";
import { ServicePage } from "@/components/ServicePage";
import { createMetadata, servicePages } from "@/content/site";

export const metadata = createMetadata(
  "Leadership Development",
  "Leadership development workshops and outcomes with Lornette Daye.",
  "/leadership",
);

export default function LeadershipPage() {
  return (
    <PageShell>
      <ServicePage page={servicePages.leadership} />
    </PageShell>
  );
}
