import { BlogFilterableList } from "@/components/BlogFilterableList";
import { PageShell } from "@/components/PageShell";
import { createMetadata, posts } from "@/content/site";

export const metadata = createMetadata(
  "Blog & Reflections",
  "Insights from Lornette Daye on resilience, leadership, performance, and purpose.",
  "/blog",
);

export default function BlogPage() {
  const sortedPosts = [...posts].sort(
    (a, b) => new Date(b.date).getTime() - new Date(a.date).getTime(),
  );

  return (
    <PageShell>
      <main className="bg-white px-3 py-8 sm:px-4 sm:py-10 lg:px-6">
        <div className="mx-auto max-w-[1140px]">
          <div className="border-b border-[var(--line)] pb-6">
            <p className="text-xs font-bold uppercase tracking-[0.24em] text-[var(--gold-dark)]">
              Reflections & Blueprints
            </p>
            <h1 className="mt-3 font-serif text-[34px] font-normal leading-none text-black sm:text-[44px]">
              All Reflections & Articles
            </h1>
            <p className="mt-3 max-w-2xl text-base leading-7 text-[#675d50]">
              Explore Lornette Daye&apos;s latest writings on athletic focus, resilience, spiritual growth, leadership, and personal transformation.
            </p>
          </div>
          <BlogFilterableList initialPosts={sortedPosts} />
        </div>
      </main>
    </PageShell>
  );
}
