import Link from "next/link";

import type { Post } from "@/content/site";
import { ImageFrame } from "./ImageFrame";

export function BlogCard({ post }: { post: Post }) {
  return (
    <article className="border border-[var(--line)] bg-white">
      <ImageFrame image={post.image} ratio="aspect-[16/10]" framed={false} />
      <div className="p-6">
        <p className="text-xs font-bold uppercase text-[var(--gold-dark)]">
          {post.category}
        </p>
        <h3 className="mt-3 font-serif text-2xl leading-tight text-[var(--ink)]">
          <Link href={`/blog/${post.slug}`}>{post.title}</Link>
        </h3>
        <p className="mt-4 text-sm leading-7 text-[#675d50]">{post.excerpt}</p>
        <Link
          href={`/blog/${post.slug}`}
          className="mt-5 inline-flex text-sm font-bold uppercase text-[var(--gold-dark)]"
        >
          Read Article
        </Link>
      </div>
    </article>
  );
}
