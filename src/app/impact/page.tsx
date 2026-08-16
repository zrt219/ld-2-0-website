import Image from "next/image";

import { CTAButton } from "@/components/CTAButton";
import { ImageFrame } from "@/components/ImageFrame";
import { PageShell } from "@/components/PageShell";
import { SectionHeader } from "@/components/SectionHeader";
import { TestimonialCard } from "@/components/TestimonialCard";
import { additionalImages, createMetadata, images, testimonials } from "@/content/site";

export const metadata = createMetadata(
  "Impact / Testimonials",
  "Testimonials and impact materials for Lornette Daye.",
  "/impact",
);

export default function ImpactPage() {
  return (
    <PageShell>
      <main>
        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto grid max-w-7xl gap-10 lg:grid-cols-[0.9fr_1.1fr] lg:items-center">
            <SectionHeader
              eyebrow="Impact / Testimonials"
              title="Real stories. Clear context."
              body="Testimonials and brand materials are presented with direct attribution where available and without unsupported proof or invented outcomes."
            />
            <ImageFrame image={images.heroPortrait} priority ratio="aspect-[16/10]" />
          </div>
        </section>
        <section className="px-4 pb-16 sm:px-6 lg:px-8 lg:pb-24">
          <div className="mx-auto max-w-7xl">
            <div className="grid gap-6 lg:grid-cols-2">
              {testimonials.map((testimonial) => (
                <TestimonialCard key={testimonial.name} {...testimonial} className="h-full" />
              ))}
            </div>
            <div className="mt-12 grid gap-8 lg:grid-cols-2">
              <ImageFrame image={additionalImages.testimonialComposite} ratio="aspect-[4/3]" />
              <ImageFrame image={additionalImages.testimonialYouth} ratio="aspect-[4/3]" />
            </div>
            <div className="mt-12 border border-[var(--line)] bg-white p-6">
              <p className="text-sm font-bold uppercase text-[var(--gold-dark)]">
                Media & Organization Reference Collage
              </p>
              <p className="mt-2 text-sm text-[#675d50]">
                Presented as one brand-provided collage while individual feature claims and logo permissions are confirmed.
              </p>
              <Image
                src={images.featuredOn.src}
                alt={images.featuredOn.alt}
                unoptimized
                className="mt-6 h-auto w-full"
              />
            </div>
            <div className="mt-10">
              <CTAButton href="/book">Bring Lornette to Your Event</CTAButton>
            </div>
          </div>
        </section>
      </main>
    </PageShell>
  );
}
