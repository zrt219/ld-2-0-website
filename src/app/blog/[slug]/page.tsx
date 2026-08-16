import { notFound } from "next/navigation";

import { ImageFrame } from "@/components/ImageFrame";
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
      <main className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
        <article className="mx-auto grid max-w-5xl gap-10 lg:grid-cols-[0.8fr_1.2fr] lg:items-start">
          <ImageFrame image={post.image} ratio="aspect-[4/5]" priority />
          <div>
            <p className="text-sm font-bold uppercase text-[var(--gold-dark)]">
              {post.category}
            </p>
            <h1 className="mt-5 font-serif text-4xl leading-tight text-balance text-[var(--ink)] sm:text-6xl">
              {post.title}
            </h1>
            <p className="mt-6 text-lg leading-8 text-[#675d50]">
              {post.excerpt}
            </p>
            <div className="mt-8 border-t border-[var(--line)] pt-6 text-base leading-8 text-[#675d50]">
              <p>
                This article page is ready for final approved copy. The current
                summary is intentionally restrained so the site does not invent
                claims, outcomes, or source details.
              </p>
            </div>
          </div>
        </article>
      </main>
    </PageShell>
  );
}
