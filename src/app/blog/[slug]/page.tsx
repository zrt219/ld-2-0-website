import Image from "next/image";
import { notFound } from "next/navigation";

import { PageShell } from "@/components/PageShell";
import { createMetadata, posts, siteCopy, siteUrl } from "@/content/site";

type BlogPostPageProps = {
  params: Promise<{
    slug: string;
  }>;
};

export function generateStaticParams() {
  return posts.map((post) => ({ slug: post.slug }));
}

export async function generateMetadata({ params }: BlogPostPageProps) {
  const { slug } = await params;
  const post = posts.find((item) => item.slug === slug);

  if (!post) {
    return {};
  }

  return createMetadata(post.title, post.excerpt, `/blog/${post.slug}`);
}

export default async function BlogPostPage({ params }: BlogPostPageProps) {
  const { slug } = await params;
  const post = posts.find((item) => item.slug === slug);

  if (!post) {
    notFound();
  }

  const articleJsonLd = {
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    headline: post.title,
    description: post.excerpt,
    datePublished: post.date,
    dateModified: post.date,
    mainEntityOfPage: {
      "@type": "WebPage",
      "@id": `${siteUrl}/blog/${post.slug}`,
    },
    author: {
      "@type": "Person",
      name: post.author || siteCopy.brandName,
      url: siteUrl,
    },
    publisher: {
      "@type": "Person",
      name: siteCopy.brandName,
      url: siteUrl,
    },
  };

  return (
    <PageShell>
      <main className="bg-white px-6 py-8 sm:py-10">
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(articleJsonLd) }}
        />
        <article className="mx-auto max-w-[740px] text-[14px] leading-[1.65] text-black">
          <h1 className="max-w-[660px] font-serif text-[30px] font-normal leading-[1.25] text-black sm:text-[34px]">
            {post.title}
          </h1>
          <div className="mt-6 space-y-4">
            {post.body.intro.map((paragraph) => (
              <p key={paragraph}>{paragraph}</p>
            ))}
          </div>

          <figure className="mt-8">
            <div
              className={`relative overflow-hidden bg-[#f5f2ec] ${
                post.image.aspect ?? "aspect-[2.05/1]"
              }`}
            >
              <Image
                src={post.image.src}
                alt={post.image.alt}
                fill
                priority
                sizes="(max-width: 820px) 92vw, 740px"
                className={post.image.crop ?? "object-cover object-center"}
              />
            </div>
            {post.image.caption ? (
              <figcaption className="mt-3 text-center text-[11px] leading-none text-black">
                {post.image.caption}
              </figcaption>
            ) : null}
          </figure>

          <div className="mt-12">
            {post.body.sections.map((section) => (
              <section key={section.heading} className="mt-12 first:mt-0">
                <h2 className="font-serif text-[23px] font-normal leading-tight text-black sm:text-[25px]">
                  {section.heading}
                </h2>
                <div className="mt-5 space-y-5">
                  {section.paragraphs.map((paragraph) => (
                    <p key={paragraph}>{paragraph}</p>
                  ))}
                  {section.bullets ? (
                    <ul className="space-y-5 pl-5">
                      {section.bullets.map((bullet) => (
                        <li key={bullet.label} className="list-disc">
                          <span className="font-bold">{bullet.label}</span>
                          <span className="block">{bullet.text}</span>
                        </li>
                      ))}
                    </ul>
                  ) : null}
                </div>
              </section>
            ))}
          </div>

          {post.body.conclusion ? (
            <div className="mt-8 space-y-4">
              {post.body.conclusion.map((paragraph) => (
                <p key={paragraph}>{paragraph}</p>
              ))}
            </div>
          ) : null}

          {/* End-of-Blog Actions & CTA */}
          <div className="mt-14 space-y-12">
            {/* Purchase CTA if available */}
            {post.amazonUrl || post.purchaseUrl ? (
              <div className="border border-[rgba(198,165,92,0.5)] bg-[#faf6ee] p-6 sm:p-8">
                <p className="text-xs font-bold uppercase tracking-[0.24em] text-[var(--gold-dark)]">
                  Published Guide & Book
                </p>
                <h3 className="mt-2 font-serif text-2xl text-[var(--ink)] sm:text-3xl">
                  Get Your Copy of {post.title.split(":")[0]}
                </h3>
                <p className="mt-2 text-sm leading-6 text-[#675d50]">
                  Deepen your growth with actionable blueprints, daily reflection prompts, and enduring wisdom.
                </p>
                <div className="mt-6 flex flex-col gap-3 sm:flex-row sm:items-center">
                  {post.amazonUrl ? (
                    <a
                      href={post.amazonUrl}
                      target="_blank"
                      rel="noreferrer"
                      className="inline-flex min-h-12 items-center justify-center rounded-sm bg-[#ff9900] px-6 py-3 text-center text-sm font-bold uppercase tracking-wider text-black shadow-md transition hover:bg-[#e68a00] focus:outline-none focus:ring-2 focus:ring-[#ff9900]"
                    >
                      Order on Amazon
                    </a>
                  ) : null}
                  {post.purchaseUrl ? (
                    <a
                      href={post.purchaseUrl}
                      target="_blank"
                      rel="noreferrer"
                      className="inline-flex min-h-12 items-center justify-center bg-[var(--ink)] px-6 py-3 text-center text-sm font-bold uppercase tracking-wider text-[var(--ivory)] shadow-md transition hover:bg-[var(--charcoal)]"
                    >
                      Buy Digital Edition
                    </a>
                  ) : null}
                </div>
              </div>
            ) : null}

            {/* Related Posts to Keep Reader Engaged */}
            <div className="border-t border-[var(--line)] pt-10">
              <p className="text-xs font-bold uppercase tracking-[0.24em] text-[var(--gold-dark)]">
                Keep Reading & Exploring
              </p>
              <h3 className="mt-2 font-serif text-2xl text-[var(--ink)] sm:text-3xl">
                More Reflections from Lornette
              </h3>
              <div className="mt-6 grid gap-6 sm:grid-cols-2">
                {posts
                  .filter((p) => p.slug !== post.slug)
                  .slice(0, 2)
                  .map((relatedPost) => (
                    <a
                      key={relatedPost.slug}
                      href={`/blog/${relatedPost.slug}`}
                      className="group flex flex-col overflow-hidden border border-[var(--line)] bg-[#faf7f2] p-5 transition hover:-translate-y-1 hover:border-[var(--champagne)] hover:shadow-md"
                    >
                      <span className="text-[11px] font-bold uppercase tracking-wider text-[var(--gold-dark)]">
                        {relatedPost.category}
                      </span>
                      <h4 className="mt-2 font-serif text-lg leading-snug text-[var(--ink)] group-hover:text-[var(--gold-dark)]">
                        {relatedPost.title}
                      </h4>
                      <p className="mt-2 line-clamp-2 text-xs leading-5 text-[#675d50]">
                        {relatedPost.excerpt}
                      </p>
                      <span className="mt-4 inline-flex items-center text-xs font-bold uppercase tracking-wider text-[var(--ink)] group-hover:underline">
                        Read reflection →
                      </span>
                    </a>
                  ))}
              </div>
            </div>

            {/* Site Engagement Banner */}
            <div className="border border-[rgba(198,165,92,0.42)] bg-[var(--ink)] p-8 text-[var(--ivory)] shadow-xl">
              <p className="text-xs font-bold uppercase tracking-[0.28em] text-[var(--champagne)]">
                Bring the Message to Your Room & Life
              </p>
              <h3 className="mt-3 font-serif text-3xl leading-tight text-white">
                Transformational Keynotes, Elite Coaching & Workshops
              </h3>
              <p className="mt-4 max-w-xl text-sm leading-7 text-[#d8cdbb]">
                Bring Lornette Daye to your next conference, athletic program, corporate retreat, or community event to empower your team with unshakeable resilience.
              </p>
              <div className="mt-6 flex flex-wrap gap-3">
                <a
                  href="/book"
                  className="inline-flex min-h-11 items-center justify-center bg-[var(--gold-dark)] px-5 py-2.5 text-xs font-bold uppercase tracking-wider text-[var(--ink)] shadow-md transition hover:bg-[var(--champagne)]"
                >
                  Book Lornette Daye
                </a>
                <a
                  href="/athlete-coaching"
                  className="inline-flex min-h-11 items-center justify-center border border-white/30 bg-white/10 px-5 py-2.5 text-xs font-bold uppercase tracking-wider text-white transition hover:bg-white/20"
                >
                  Athlete Coaching
                </a>
                <a
                  href="/books"
                  className="inline-flex min-h-11 items-center justify-center border border-white/30 bg-white/10 px-5 py-2.5 text-xs font-bold uppercase tracking-wider text-white transition hover:bg-white/20"
                >
                  Explore All Books
                </a>
                <a
                  href="/speaker-kit"
                  className="inline-flex min-h-11 items-center justify-center border border-white/30 bg-white/10 px-5 py-2.5 text-xs font-bold uppercase tracking-wider text-white transition hover:bg-white/20"
                >
                  Speaker Kit
                </a>
              </div>
            </div>
          </div>
        </article>
      </main>
    </PageShell>
  );
}
