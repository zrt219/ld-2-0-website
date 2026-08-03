import { PageShell } from "@/components/PageShell";
import { ServicePage } from "@/components/ServicePage";
import { createMetadata, servicePages } from "@/content/site";

export const metadata = createMetadata(
  "Diversity & Inclusion",
  "Inclusion in action workshops focused on belonging, collaboration, and performance.",
  "/inclusion",
);

export default function InclusionPage() {
  return (
    <PageShell>
      <ServicePage page={servicePages.inclusion} />
    </PageShell>
  );
}
