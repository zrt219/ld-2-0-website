import { BlogCard } from "@/components/BlogCard";
import { PageShell } from "@/components/PageShell";
import { SectionHeader } from "@/components/SectionHeader";
import { createMetadata, posts } from "@/content/site";

export const metadata = createMetadata(
  "Blog",
  "Insights from Lornette Daye on resilience, leadership, performance, and purpose.",
  "/blog",
);

export default function BlogPage() {
  return (
    <PageShell>
      <main className="px-4 py-16 sm:px-6 lg:px-8 lg:py-24">
        <div className="mx-auto max-w-7xl">
          <SectionHeader
            eyebrow="Blog"
            title="Insights for resilience, leadership, and performance."
            body="Short reflections and article concepts aligned with the supplied Lornette Daye brand materials."
          />
          <div className="mt-10 grid gap-6 md:grid-cols-3">
            {posts.map((post) => (
              <BlogCard key={post.slug} post={post} />
            ))}
          </div>
        </div>
      </main>
    </PageShell>
  );
}
