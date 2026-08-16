import { PageShell } from "@/components/PageShell";
import { ServicePage } from "@/components/ServicePage";
import { createMetadata, servicePages } from "@/content/site";

export const metadata = createMetadata(
  "Athlete & Performance Coaching",
  "Athlete coaching sessions on mindset, preparation, pressure, team standards, and confidence.",
  "/athlete-coaching",
);

export default function AthleteCoachingPage() {
  return (
    <PageShell>
      <ServicePage page={servicePages["athlete-coaching"]} />
    </PageShell>
  );
}
