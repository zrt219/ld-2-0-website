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
            <div className="relative aspect-[2.05/1] overflow-hidden bg-[#f5f2ec]">
              <Image
                src={post.image.src}
                alt={post.image.alt}
                fill
                priority
                sizes="(max-width: 820px) 92vw, 740px"
                className={`object-cover ${post.image.crop ?? "object-center"}`}
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
        </article>
      </main>
    </PageShell>
  );
}
