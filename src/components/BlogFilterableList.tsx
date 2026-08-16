"use client";

import { useMemo, useState } from "react";
import { ArrowUpDown, Filter } from "lucide-react";

import { BlogCard } from "@/components/BlogCard";
import type { Post } from "@/content/site";

type SortOption = "newest" | "oldest" | "title" | "readTime";

type CategoryFilter = {
  id: string;
  label: string;
  matches: (category: string) => boolean;
};

const categoryFilters: CategoryFilter[] = [
  { id: "all", label: "All Posts", matches: () => true },
  {
    id: "athlete",
    label: "Athlete & Performance",
    matches: (cat) =>
      cat.includes("Athlete") || cat.includes("Performance") || cat.includes("Keynotes & Mindset"),
  },
  {
    id: "resilience",
    label: "Resilience & Mindset",
    matches: (cat) =>
      cat.includes("Resilience") || cat.includes("Mindset") || cat.includes("Transformational"),
  },
  {
    id: "spiritual",
    label: "Spiritual & Personal Growth",
    matches: (cat) =>
      cat.includes("Spiritual") || cat.includes("Personal") || cat.includes("Faith"),
  },
  {
    id: "leadership",
    label: "Leadership & Purpose",
    matches: (cat) =>
      cat.includes("Leadership") || cat.includes("Purpose") || cat.includes("Men's"),
  },
  {
    id: "youth",
    label: "Youth & Students",
    matches: (cat) =>
      cat.includes("Youth") || cat.includes("Student") || cat.includes("Coaching"),
  },
];

export function BlogFilterableList({ initialPosts }: { initialPosts: Post[] }) {
  const [selectedFilter, setSelectedFilter] = useState<string>("all");
  const [sortBy, setSortBy] = useState<SortOption>("newest");

  const filteredAndSortedPosts = useMemo(() => {
    const activeFilterObj = categoryFilters.find((f) => f.id === selectedFilter);
    const filtered = initialPosts.filter((post) =>
      activeFilterObj ? activeFilterObj.matches(post.category) : true,
    );

    return [...filtered].sort((a, b) => {
      if (sortBy === "newest") {
        return new Date(b.date).getTime() - new Date(a.date).getTime();
      }
      if (sortBy === "oldest") {
        return new Date(a.date).getTime() - new Date(b.date).getTime();
      }
      if (sortBy === "title") {
        return a.title.localeCompare(b.title);
      }
      if (sortBy === "readTime") {
        const timeA = parseInt(a.readTime) || 0;
        const timeB = parseInt(b.readTime) || 0;
        return timeA - timeB;
      }
      return 0;
    });
  }, [initialPosts, selectedFilter, sortBy]);

  return (
    <div className="mt-8 space-y-8 sm:mt-10">
      {/* Controls Bar: Category Filters & Sort Select */}
      <div className="flex flex-col gap-6 border-b border-[var(--line)] pb-6 lg:flex-row lg:items-center lg:justify-between">
        {/* Category Filter Pills */}
        <div className="flex flex-wrap items-center gap-2" role="tablist" aria-label="Blog post category filters">
          <span className="mr-2 hidden items-center gap-1.5 text-xs font-bold uppercase tracking-[0.2em] text-[#675d50] sm:inline-flex">
            <Filter size={14} aria-hidden="true" />
            Filter:
          </span>
          {categoryFilters.map((filter) => {
            const isSelected = selectedFilter === filter.id;
            return (
              <button
                key={filter.id}
                type="button"
                role="tab"
                aria-selected={isSelected}
                onClick={() => setSelectedFilter(filter.id)}
                className={`min-h-10 rounded-full px-4 py-2 text-xs font-bold transition focus:outline-none focus:ring-2 focus:ring-[var(--gold-dark)] ${
                  isSelected
                    ? "bg-[var(--ink)] text-[var(--ivory)] shadow-md"
                    : "border border-[var(--line)] bg-[var(--ivory)] text-[#574e43] hover:border-[var(--champagne)] hover:bg-white"
                }`}
              >
                {filter.label}
              </button>
            );
          })}
        </div>

        {/* Sort Controls */}
        <div className="flex items-center gap-3 self-end lg:self-auto">
          <label htmlFor="blog-sort" className="flex items-center gap-1.5 text-xs font-bold uppercase tracking-[0.18em] text-[#675d50]">
            <ArrowUpDown size={14} aria-hidden="true" />
            Sort By:
          </label>
          <select
            id="blog-sort"
            value={sortBy}
            onChange={(e) => setSortBy(e.target.value as SortOption)}
            className="min-h-10 rounded-lg border border-[var(--line)] bg-white px-3 py-2 text-xs font-semibold text-[var(--ink)] shadow-sm transition focus:border-[var(--gold-dark)] focus:outline-none focus:ring-1 focus:ring-[var(--gold-dark)]"
          >
            <option value="newest">Newest First</option>
            <option value="oldest">Oldest First</option>
            <option value="title">Title (A-Z)</option>
            <option value="readTime">Read Time</option>
          </select>
        </div>
      </div>

      {/* Results Count & List */}
      <div>
        <p className="mb-6 text-xs font-semibold uppercase tracking-wider text-[#827566]">
          Showing {filteredAndSortedPosts.length} {filteredAndSortedPosts.length === 1 ? "reflection" : "reflections"}
        </p>

        {filteredAndSortedPosts.length > 0 ? (
          <div className="grid gap-10">
            {filteredAndSortedPosts.map((post) => (
              <BlogCard key={post.slug} post={post} />
            ))}
          </div>
        ) : (
          <div className="my-16 text-center">
            <p className="font-serif text-2xl text-[var(--ink)]">No posts found in this category.</p>
            <button
              type="button"
              onClick={() => setSelectedFilter("all")}
              className="mt-4 inline-flex items-center text-xs font-bold uppercase tracking-[0.2em] text-[var(--gold-dark)] underline hover:text-[var(--ink)]"
            >
              Reset Filters
            </button>
          </div>
        )}
      </div>
    </div>
  );
}
