"use client";

import { Search, SlidersHorizontal } from "lucide-react";
import { useMemo, useState } from "react";

import { mediaItems } from "@/content/site";
import { VideoCard } from "./VideoCard";

const categories = [
  "All Videos",
  "Keynotes",
  "Interviews",
  "Short Insights",
  "Podcasts",
];

export function MediaGrid() {
  const [category, setCategory] = useState("All Videos");
  const [query, setQuery] = useState("");
  const [sort, setSort] = useState("Featured");

  const filtered = useMemo(() => {
    const result = mediaItems.filter((item) => {
      const matchesCategory = category === "All Videos" || item.category === category;
      const matchesSearch = `${item.title} ${item.summary}`
        .toLowerCase()
        .includes(query.toLowerCase());
      return matchesCategory && matchesSearch;
    });
    return sort === "A-Z" ? [...result].sort((a, b) => a.title.localeCompare(b.title)) : result;
  }, [category, query, sort]);

  return (
    <div>
      <div className="grid gap-5 border border-[var(--line)] bg-white/85 p-4 shadow-[0_16px_60px_rgba(23,20,18,0.06)] lg:grid-cols-[1fr_auto] lg:items-center">
        <div className="flex gap-2 overflow-x-auto pb-1">
          {categories.map((item) => (
            <button
              key={item}
              type="button"
              aria-pressed={category === item}
              onClick={() => setCategory(item)}
              className={`min-h-11 shrink-0 border px-4 text-xs font-bold uppercase tracking-[0.14em] transition ${
                category === item
                  ? "border-[var(--champagne)] bg-[var(--ink)] text-[var(--ivory)]"
                  : "border-[var(--line)] bg-white text-[var(--ink)] hover:border-[var(--champagne)]"
              }`}
            >
              {item}
            </button>
          ))}
        </div>
        <div className="grid gap-3 sm:grid-cols-[minmax(15rem,1fr)_auto]">
          <label className="relative block">
            <span className="sr-only">Search videos</span>
            <Search
              size={17}
              aria-hidden="true"
              className="absolute left-3 top-1/2 -translate-y-1/2 text-[#7d7164]"
            />
            <input
              value={query}
              onChange={(event) => setQuery(event.target.value)}
              placeholder="Search videos"
              className="min-h-11 w-full border border-[var(--line)] bg-white pl-10 pr-3 text-sm"
            />
          </label>
          <label className="relative block">
            <span className="sr-only">Sort videos</span>
            <SlidersHorizontal
              size={17}
              aria-hidden="true"
              className="absolute left-3 top-1/2 -translate-y-1/2 text-[#7d7164]"
            />
            <select
              id="media-sort"
              value={sort}
              onChange={(event) => setSort(event.target.value)}
              className="min-h-11 w-full border border-[var(--line)] bg-white pl-10 pr-8 text-sm"
            >
              <option>Featured</option>
              <option>A-Z</option>
            </select>
          </label>
        </div>
      </div>

      <div className="mt-8 grid gap-7 md:grid-cols-2" aria-live="polite" aria-atomic="false">
        {filtered.map((item) => (
          <VideoCard
            key={item.title}
            title={item.title}
            summary={item.summary}
            image={item.image}
            videoSrc={item.videoSrc}
            duration={item.duration}
          />
        ))}
      </div>
      {filtered.length === 0 ? (
        <div className="mt-8 border border-[var(--line)] bg-white p-8 text-center">
          <p className="font-serif text-3xl text-[var(--ink)]">No media matched that search.</p>
          <p className="mt-2 text-sm text-[#675d50]">
            Try another topic or choose All Videos.
          </p>
        </div>
      ) : null}
    </div>
  );
}
