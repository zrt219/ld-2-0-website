import Image from "next/image";
import {
  ArrowRight,
  BookOpenCheck,
  CheckCircle2,
  CreditCard,
  Download,
  FileText,
  LockKeyhole,
  Sparkles,
} from "lucide-react";

import { CTAButton } from "@/components/CTAButton";
import { PageShell } from "@/components/PageShell";
import { bookListings, createMetadata, siteCopy } from "@/content/site";

export const metadata = createMetadata(
  "Books & PDF Downloads",
  "Purchase Lornette Daye books and digital PDF guides through secure Stripe checkout.",
  "/books",
);

const buyingSteps = [
  {
    title: "Choose a Guide",
    body: "Select the PDF resource that fits your season, audience, or growth focus.",
    icon: BookOpenCheck,
  },
  {
    title: "Checkout With Stripe",
    body: "Each book uses a secure Stripe-hosted checkout page for one-time purchase.",
    icon: CreditCard,
  },
  {
    title: "Receive the PDF",
    body: "PDF delivery should be finalized in the Stripe fulfillment workflow before launch promotion.",
    icon: Download,
  },
];

const heroTrustMarkers = [
  { label: "Secure Checkout", icon: LockKeyhole },
  { label: "PDF Editions", icon: FileText },
  { label: "Purpose-Led Tools", icon: Sparkles },
];

const coverCropBySlug: Record<string, { objectFit?: "cover" | "contain"; objectPosition: string; transform: string }> = {
  "survival-skills-for-men": {
    objectFit: "cover",
    objectPosition: "50% 50%",
    transform: "scale(1.85)",
  },
  "road-to-the-olympics": {
    objectFit: "cover",
    objectPosition: "50% 50%",
    transform: "scale(1)",
  },
  "surviving-life": {
    objectFit: "cover",
    objectPosition: "50% 50%",
    transform: "scale(1.85)",
  },
};

function getCoverCrop(slug: string) {
  return coverCropBySlug[slug] ?? {
    objectFit: "cover",
    objectPosition: "50% 50%",
    transform: "scale(1)",
  };
}

const productJsonLd = {
  "@context": "https://schema.org",
  "@type": "ItemList",
  name: "Books by Lornette Daye",
  itemListElement: bookListings.map((book, index) => ({
    "@type": "ListItem",
    position: index + 1,
    item: {
      "@type": "Product",
      name: book.title,
      description: book.description,
      brand: siteCopy.brandName,
      offers: {
        "@type": "Offer",
        price: "14.99",
        priceCurrency: "CAD",
        availability: "https://schema.org/InStock",
        url: book.purchaseUrl,
      },
    },
  })),
};

export default function BooksPage() {
  return (
    <PageShell>
      <main className="bg-[var(--ivory)]">
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(productJsonLd) }}
        />

        <section className="relative overflow-hidden border-b border-[var(--line)] px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="absolute inset-y-0 right-0 hidden w-1/2 bg-[radial-gradient(circle_at_70%_35%,rgba(198,165,92,0.22),transparent_36%),linear-gradient(135deg,transparent,rgba(232,221,203,0.55))] lg:block" />
          <div className="absolute left-0 top-10 h-64 w-64 rounded-full bg-[rgba(198,165,92,0.11)] blur-3xl" />

          <div className="relative mx-auto grid max-w-7xl items-center gap-12 lg:grid-cols-[0.9fr_1.1fr]">
            <div>
              <p className="text-xs font-bold uppercase tracking-[0.32em] text-[var(--gold-dark)]">
                Books & Digital Guides
              </p>
              <h1 className="mt-5 max-w-4xl font-serif text-5xl leading-[0.95] text-[var(--ink)] sm:text-6xl lg:text-7xl">
                Practical Wisdom for Resilience, Purpose, and Renewal.
              </h1>
              <p className="mt-7 max-w-2xl text-lg leading-8 text-[var(--charcoal)]">
                Explore Lornette Daye&apos;s books for readers who want
                encouragement they can return to, reflect on, and apply in real
                life.
              </p>
              <div className="mt-8 flex flex-col gap-3 sm:flex-row">
                <CTAButton href="#book-listings">Shop PDF Books</CTAButton>
                <CTAButton href="/book" variant="secondary">
                  Invite Lornette to Speak
                </CTAButton>
              </div>
              <div className="mt-8 grid gap-3 text-sm font-semibold text-[#5d544a] sm:grid-cols-3">
                {heroTrustMarkers.map(({ label, icon: Icon }) => (
                  <div
                    key={label}
                    className="flex min-h-14 items-center gap-3 border border-[rgba(198,165,92,0.32)] bg-white/55 px-4"
                  >
                    <Icon size={19} className="text-[var(--gold-dark)]" aria-hidden="true" />
                    <span>{label}</span>
                  </div>
                ))}
              </div>
            </div>

            <div className="relative">
              <div className="grid gap-4 sm:grid-cols-3 lg:translate-y-4">
                {bookListings.map((book, index) => (
                  <div
                    key={book.slug}
                    className={`group relative overflow-hidden border border-[rgba(198,165,92,0.38)] bg-white shadow-[0_24px_70px_rgba(23,20,18,0.11)] ${
                      index === 1 ? "sm:-translate-y-8" : ""
                    }`}
                  >
                    <div className="relative aspect-[4/5]">
                      <Image
                        src={book.image.src}
                        alt={book.image.alt}
                        fill
                        sizes="(min-width: 1024px) 260px, 33vw"
                        className="object-cover transition duration-500 group-hover:brightness-105"
                        style={getCoverCrop(book.slug)}
                      />
                      <div className="absolute inset-0 bg-gradient-to-t from-[rgba(23,20,18,0.24)] to-transparent" />
                    </div>
                  </div>
                ))}
              </div>
              <div className="mx-auto mt-6 max-w-lg border border-[rgba(198,165,92,0.35)] bg-white/75 p-5 text-center text-sm leading-7 text-[#675d50] shadow-[0_18px_45px_rgba(23,20,18,0.08)] backdrop-blur">
                Secure Stripe checkout links are connected for all three PDF
                listings. Final digital fulfillment should be confirmed in
                Stripe before heavy promotion.
              </div>
            </div>
          </div>
        </section>

        <section id="book-listings" className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
          <div className="mx-auto max-w-7xl">
            <div className="max-w-3xl">
              <h2 className="font-serif text-4xl leading-tight text-[var(--ink)] sm:text-5xl">
                Digital resources designed to help readers rise.
              </h2>
              <p className="mt-5 text-base leading-8 text-[#675d50]">
                Each book offers practical encouragement for resilience, faith,
                purpose, leadership, and personal growth. Choose the resource
                that speaks to your season or the people you serve.
              </p>
            </div>

            <div className="mt-12 grid gap-7 lg:grid-cols-3">
              {bookListings.map((book) => (
                <article
                  key={book.slug}
                  className="group flex h-full flex-col overflow-hidden border border-[rgba(198,165,92,0.34)] bg-white shadow-[0_20px_55px_rgba(23,20,18,0.08)] transition duration-300 hover:-translate-y-1 hover:shadow-[0_28px_80px_rgba(23,20,18,0.13)]"
                >
                  <div className="relative aspect-[16/13] overflow-hidden bg-[#efe7d8]">
                    <Image
                      src={book.image.src}
                      alt={book.image.alt}
                      fill
                      sizes="(min-width: 1024px) 33vw, 100vw"
                      className="object-cover transition duration-500 group-hover:brightness-105"
                      style={getCoverCrop(book.slug)}
                    />
                    <div className="absolute inset-x-0 bottom-0 bg-gradient-to-t from-[rgba(23,20,18,0.72)] to-transparent p-5">
                      <span className="inline-flex border border-white/35 bg-white/15 px-3 py-1 text-xs font-bold uppercase tracking-[0.2em] text-white backdrop-blur">
                        {book.format}
                      </span>
                    </div>
                  </div>

                  <div className="flex flex-1 flex-col p-7">
                    <div className="flex items-start justify-between gap-4">
                      <div>
                        <h3 className="font-serif text-3xl leading-tight text-[var(--ink)]">
                          {book.title}
                        </h3>
                        <p className="mt-2 text-sm font-bold uppercase tracking-[0.18em] text-[var(--gold-dark)]">
                          {book.priceLabel}
                        </p>
                      </div>
                      <BookOpenCheck
                        className="mt-1 shrink-0 text-[var(--champagne)]"
                        size={30}
                        aria-hidden="true"
                      />
                    </div>

                    <p className="mt-4 text-base font-semibold leading-7 text-[var(--charcoal)]">
                      {book.subtitle}
                    </p>
                    <p className="mt-4 text-sm leading-7 text-[#675d50]">
                      {book.description}
                    </p>
                    <p className="mt-5 border-l-2 border-[var(--champagne)] pl-4 text-sm leading-7 text-[#675d50]">
                      <span className="font-bold text-[var(--ink)]">Best for: </span>
                      {book.audience}
                    </p>

                    <ul className="mt-6 grid gap-3">
                      {book.highlights.map((highlight) => (
                        <li key={highlight} className="flex items-start gap-3 text-sm text-[#5f564c]">
                          <CheckCircle2
                            className="mt-0.5 shrink-0 text-[var(--gold-dark)]"
                            size={17}
                            aria-hidden="true"
                          />
                          <span>{highlight}</span>
                        </li>
                      ))}
                    </ul>

                    <div className="mt-7 pt-2">
                      <a
                        href={book.purchaseUrl}
                        target="_blank"
                        rel="noreferrer"
                        aria-label={`Buy ${book.title} through Stripe`}
                        className="inline-flex min-h-12 w-full items-center justify-center gap-2 border border-transparent bg-[var(--ink)] px-5 py-3 text-center text-sm font-bold uppercase leading-5 text-[var(--ivory)] shadow-[0_14px_34px_rgba(23,20,18,0.18)] transition hover:bg-[var(--charcoal)] focus:outline-none focus:ring-2 focus:ring-[var(--gold-dark)] focus:ring-offset-2"
                      >
                        Buy
                        <ArrowRight size={17} aria-hidden="true" />
                      </a>
                    </div>
                  </div>
                </article>
              ))}
            </div>
          </div>
        </section>

        <section className="border-y border-[var(--line)] bg-white px-4 py-14 sm:px-6 lg:px-8">
          <div className="mx-auto grid max-w-7xl gap-6 lg:grid-cols-[0.75fr_1.25fr] lg:items-center">
            <div>
              <p className="text-xs font-bold uppercase tracking-[0.32em] text-[var(--gold-dark)]">
                How It Works
              </p>
              <h2 className="mt-4 font-serif text-4xl leading-tight text-[var(--ink)]">
                Simple purchase path for digital readers.
              </h2>
            </div>
            <div className="grid gap-4 md:grid-cols-3">
              {buyingSteps.map((step, index) => {
                const Icon = step.icon;
                return (
                  <div
                    key={step.title}
                    className="border border-[rgba(198,165,92,0.3)] bg-[var(--ivory)] p-6"
                  >
                    <div className="flex items-center gap-3">
                      <span className="flex h-10 w-10 items-center justify-center rounded-full bg-[var(--champagne)] text-sm font-black text-[var(--ink)]">
                        {index + 1}
                      </span>
                      <Icon size={21} className="text-[var(--gold-dark)]" aria-hidden="true" />
                    </div>
                    <h3 className="mt-5 font-serif text-2xl text-[var(--ink)]">
                      {step.title}
                    </h3>
                    <p className="mt-3 text-sm leading-7 text-[#675d50]">{step.body}</p>
                  </div>
                );
              })}
            </div>
          </div>
        </section>

        <section className="px-4 py-16 sm:px-6 lg:px-8 lg:py-20">
          <div className="mx-auto grid max-w-7xl gap-8 border border-[rgba(198,165,92,0.34)] bg-[linear-gradient(135deg,#ffffff,rgba(232,221,203,0.56))] p-7 shadow-[0_24px_70px_rgba(23,20,18,0.08)] lg:grid-cols-[1fr_auto] lg:items-center lg:p-10">
            <div>
              <p className="text-xs font-bold uppercase tracking-[0.32em] text-[var(--gold-dark)]">
                Bring the Message to the Room
              </p>
              <h2 className="mt-4 font-serif text-4xl leading-tight text-[var(--ink)] sm:text-5xl">
                Pair the books with a keynote, workshop, or mentoring session.
              </h2>
              <p className="mt-5 max-w-3xl text-base leading-8 text-[#675d50]">
                These PDF resources extend the same resilience, identity,
                purpose, and growth themes Lornette brings to stages,
                classrooms, churches, teams, and community spaces.
              </p>
            </div>
            <div className="flex flex-col gap-3 sm:flex-row lg:flex-col">
              <CTAButton href="/speaking">Explore Speaking</CTAButton>
              <CTAButton href="/book" variant="secondary">
                Book Lornette
              </CTAButton>
            </div>
          </div>
        </section>

      </main>
    </PageShell>
  );
}
