import { BlogCard } from "@/components/BlogCard";
import { PageShell } from "@/components/PageShell";
import { createMetadata, posts } from "@/content/site";

export const metadata = createMetadata(
  "Blog",
  "Insights from Lornette Daye on resilience, leadership, performance, and purpose.",
  "/blog",
);

export default function BlogPage() {
  return (
    <PageShell>
      <main className="bg-white px-3 py-8 sm:px-4 sm:py-10 lg:px-6">
        <div className="mx-auto max-w-[1140px]">
          <h1 className="font-serif text-[34px] font-normal leading-none text-black sm:text-[40px]">
            All Posts
          </h1>
          <div className="mt-16 grid gap-10 sm:mt-20">
            {posts.map((post) => (
              <BlogCard key={post.slug} post={post} />
            ))}
          </div>
        </div>
      </main>
    </PageShell>
  );
}
