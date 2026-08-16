import { PageShell } from "@/components/PageShell";
import { ServicePage } from "@/components/ServicePage";
import { createMetadata, servicePages } from "@/content/site";

export const metadata = createMetadata(
  "Athlete & Performance Coaching",
  "Athlete mindset, performance psychology, preparation, resilience, teamwork, and goal-setting.",
  "/athlete-coaching",
);

export default function AthleteCoachingPage() {
  return (
    <PageShell>
      <ServicePage page={servicePages["athlete-coaching"]} />
    </PageShell>
  );
}
