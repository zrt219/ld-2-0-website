import { PageShell } from "@/components/PageShell";
import { ServicePage } from "@/components/ServicePage";
import { createMetadata, servicePages } from "@/content/site";

export const metadata = createMetadata(
  "Mentorship & Youth Development",
  "Mentorship and youth development programs with Lornette Daye.",
  "/mentorship",
);

export default function MentorshipPage() {
  return (
    <PageShell>
      <ServicePage page={servicePages.mentorship} />
    </PageShell>
  );
}
