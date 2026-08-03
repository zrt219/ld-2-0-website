import Image from "next/image";
import Link from "next/link";
import { ArrowUpRight, MoreVertical } from "lucide-react";

import type { Post } from "@/content/site";

type BlogCardVariant = "list" | "featured" | "compact";
type HeadingLevel = "h2" | "h3";

export function BlogCard({
  post,
  variant = "list",
  headingLevel = "h2",
}: {
  post: Post;
  variant?: BlogCardVariant;
  headingLevel?: HeadingLevel;
}) {
  const titleId = `blog-card-${post.slug}`;
  const Heading = headingLevel;

  if (variant !== "list") {
    const featured = variant === "featured";

    return (
      <article className="h-full border border-[rgba(198,165,92,0.36)] bg-[var(--ivory)] shadow-[0_24px_80px_rgba(23,20,18,0.08)]">
        <Link
          href={`/blog/${post.slug}`}
          aria-labelledby={titleId}
          className="group flex h-full flex-col bg-[var(--ivory)] transition duration-300 hover:-translate-y-1 hover:border-[var(--champagne)] focus:outline-none focus:ring-4 focus:ring-[rgba(198,165,92,0.25)]"
        >
          <div
            className={`relative overflow-hidden bg-[#efe6d6] ${
              featured ? "aspect-[16/10]" : "aspect-[4/3]"
            }`}
          >
            <Image
              src={post.image.src}
              alt={post.image.alt}
              fill
              sizes={featured ? "(max-width: 1024px) 94vw, 58vw" : "(max-width: 1024px) 45vw, 30vw"}
              className={`object-cover transition duration-700 group-hover:scale-[1.04] ${post.image.crop ?? "object-center"}`}
            />
          </div>
          <div className={`flex flex-1 flex-col ${featured ? "p-7 lg:p-8" : "p-6"}`}>
            <p className="text-[0.68rem] font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)]">
              {post.category} <span aria-hidden="true">/</span> {post.readTime}
            </p>
            <Heading
              id={titleId}
              className={`mt-4 font-serif font-normal leading-tight text-[var(--ink)] transition group-hover:text-[var(--gold-dark)] ${
                featured ? "text-3xl sm:text-4xl lg:text-[2.65rem]" : "text-2xl sm:text-[1.7rem]"
              }`}
            >
              {post.title}
            </Heading>
            <p
              className={`mt-4 text-[0.95rem] leading-7 text-[#62594d] ${
                featured ? "line-clamp-3 max-w-2xl" : "line-clamp-2"
              }`}
            >
              {post.excerpt}
            </p>
            <span className="mt-6 inline-flex items-center gap-2 text-xs font-bold uppercase tracking-[0.18em] text-[var(--gold-dark)]">
              Read the reflection
              <ArrowUpRight size={15} aria-hidden="true" className="transition group-hover:translate-x-0.5 group-hover:-translate-y-0.5" />
            </span>
          </div>
        </Link>
      </article>
    );
  }

  return (
    <article className="border border-[#ededed] bg-white">
      <Link
        href={`/blog/${post.slug}`}
        aria-labelledby={titleId}
        className="group grid bg-white transition focus:outline-none focus:ring-4 focus:ring-[rgba(198,165,92,0.25)] md:grid-cols-[0.96fr_1fr]"
      >
        <div className="relative aspect-[1.55/1] overflow-hidden bg-[#f5f2ec] md:aspect-auto md:min-h-[315px]">
          <Image
            src={post.image.src}
            alt={post.image.alt}
            fill
            sizes="(max-width: 768px) 94vw, 48vw"
            className={`object-cover transition duration-500 group-hover:scale-[1.02] ${post.image.crop ?? "object-center"}`}
          />
        </div>
        <div className="flex min-h-[315px] flex-col px-8 py-7 lg:px-10">
          <div className="flex items-start justify-between gap-4">
            <div className="flex items-center gap-3">
              <span className="relative h-8 w-8 overflow-hidden rounded-full bg-[#f8efd8] ring-1 ring-[#ead8ad]">
                <Image
                  src="/generated/blog-golden-eagle-avatar.png"
                  alt="Minimal golden eagle profile avatar."
                  fill
                  sizes="32px"
                  className="object-contain p-0.5"
                />
              </span>
              <div className="text-[12px] leading-tight text-black">
                <p>{post.author}</p>
                <p className="mt-1">{post.readTime}</p>
              </div>
            </div>
            <MoreVertical size={19} aria-hidden="true" className="mt-1 text-black" />
          </div>
          <Heading
            id={titleId}
            className="mt-6 font-serif text-[28px] font-normal leading-[1.18] text-black sm:text-[32px]"
          >
            {post.title}
          </Heading>
          <p className="mt-5 line-clamp-4 max-w-[470px] text-[15px] leading-7 text-black">
            {post.excerpt}
          </p>
        </div>
      </Link>
    </article>
  );
}
