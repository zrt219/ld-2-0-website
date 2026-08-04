import Image from "next/image";
import { notFound } from "next/navigation";

import { PageShell } from "@/components/PageShell";
import { createMetadata, posts } from "@/content/site";

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

  return (
    <PageShell>
      <main className="bg-white px-6 py-8 sm:py-10">
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

          {/* Action CTAs */}
          <div className="mt-12 border border-[rgba(198,165,92,0.4)] bg-[var(--ivory)] p-6 sm:p-8">
            <h3 className="font-serif text-2xl text-[var(--ink)] sm:text-3xl">
              Take the Next Step in Your Journey
            </h3>
            <p className="mt-2 text-sm leading-6 text-[#675d50]">
              Elevate your performance, mindset, and legacy with Lornette Daye&apos;s published guides, keynotes, and elite coaching.
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
              <a
                href="/book"
                className="inline-flex min-h-12 items-center justify-center border border-[var(--ink)] bg-transparent px-6 py-3 text-center text-sm font-bold uppercase tracking-wider text-[var(--ink)] transition hover:bg-[var(--ink)] hover:text-[var(--ivory)]"
              >
                Book Lornette for Coaching & Speaking
              </a>
            </div>
          </div>
        </article>
      </main>
    </PageShell>
  );
}
