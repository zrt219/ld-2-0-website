"use client";

import { useState, useEffect } from "react";
import { LearnerShell } from "@/components/foundations/learner/LearnerShell";
import {
  Download,
  FileText,
  Headphones,
  Search,
} from "lucide-react";
import { createClient } from "@/lib/supabase/client";

type ResourceItem = {
  id: string;
  title: string;
  asset_type: "participant_pdf" | "audio_mp3" | "internal_docx" | "routine_card";
  size_display: string;
  storage_path: string;
  foundation_id: string | null;
  foundation_name: string;
};

export default function FoundationsResourcesPage() {
  const [activeCategory, setActiveCategory] = useState<string>("all");
  const [searchQuery, setSearchQuery] = useState("");
  const [resources, setResources] = useState<ResourceItem[]>([]);
  const [loading, setLoading] = useState(true);

  const supabase = createClient();

  useEffect(() => {
    async function fetchResources() {
      // Due to RLS, users will only see resources they are entitled to view
      const { data, error } = await supabase
        .from("resources")
        .select(`
          id,
          title,
          asset_type,
          size_display,
          storage_path,
          foundation_id,
          program_foundations(name)
        `)
        .eq("is_internal", false);

      if (error) {
        console.error("Failed to fetch resources:", error);
      } else if (data) {
        const mapped = (data as unknown as Array<{
          id: string;
          title: string;
          asset_type: string;
          size_display?: string | null;
          storage_path: string;
          foundation_id?: string | null;
          program_foundations?: { name?: string } | null;
        }>).map((d) => ({
          id: d.id,
          title: d.title,
          asset_type: d.asset_type as ResourceItem["asset_type"],
          size_display: d.size_display || "Unknown Size",
          storage_path: d.storage_path,
          foundation_id: d.foundation_id || null,
          foundation_name: d.program_foundations?.name || "General Framework",
        }));
        setResources(mapped);
      }
      setLoading(false);
    }
    fetchResources();
  }, [supabase]);

  const filteredResources = resources.filter((item) => {
    const matchesCategory =
      activeCategory === "all" ||
      (activeCategory === "workbooks" && item.asset_type === "participant_pdf") ||
      (activeCategory === "audio" && item.asset_type === "audio_mp3") ||
      (activeCategory === "pocket-guides" && item.asset_type === "routine_card");
      
    const matchesSearch =
      item.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
      item.foundation_name.toLowerCase().includes(searchQuery.toLowerCase());
    return matchesCategory && matchesSearch;
  });

  const handleDownload = async (path: string) => {
    const { data, error } = await supabase
      .storage
      .from("participant_resources")
      .createSignedUrl(path, 60);

    if (error || !data?.signedUrl) {
      alert("This resource is not yet available for your current week, or you lack permission to view it. Please check back when your week ticks over.");
      return;
    }
    window.open(data.signedUrl, "_blank");
  };

  return (
    <LearnerShell>
      <div className="p-4 sm:p-6 lg:p-8 max-w-7xl mx-auto space-y-6">
        {/* Top Header */}
        <section className="relative overflow-hidden rounded-2xl border border-[#dfcca6] bg-[#fbf9f4] p-6 sm:p-8 shadow-[0_4px_24px_rgba(30,24,15,0.04)]">
          <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
            <div>
              <p className="font-sans text-[11px] font-bold uppercase tracking-[0.28em] text-[#8e7e6e]">
                PARTICIPANT VAULT & TOOLKIT
              </p>
              <h1 className="mt-1 font-serif text-3xl sm:text-4xl font-semibold tracking-tight text-[#1e1b18]">
                Resources & Field Guides
              </h1>
              <p className="mt-2 font-sans text-xs sm:text-sm text-[#665a4c] max-w-xl leading-relaxed">
                Downloadable PDF workbooks, pocket routine cards, and audio prep tracks designed for on-course execution.
              </p>
            </div>

            <div className="flex items-center gap-3">
              <div className="relative w-full sm:w-64">
                <input
                  type="text"
                  placeholder="Search resources..."
                  value={searchQuery}
                  onChange={(e) => setSearchQuery(e.target.value)}
                  className="w-full rounded-full border border-[#dac8b2] bg-white py-2 pl-9 pr-4 text-xs text-[#1e1b18] placeholder-[#a69888] shadow-xs focus:border-[var(--gold-dark)] focus:outline-none"
                />
                <Search size={15} className="absolute left-3 top-2.5 text-[#9f9180]" aria-hidden="true" />
              </div>
            </div>
          </div>
        </section>

        {/* Category Filters */}
        <div className="flex flex-wrap items-center gap-2 border-b border-[#ebdcc9] pb-3">
          {[
            { id: "all", label: "All Materials" },
            { id: "workbooks", label: "Workbooks" },
            { id: "pocket-guides", label: "Pocket Cards & Routine Sheets" },
            { id: "audio", label: "Guided Audio Tracks" },
          ].map((cat) => (
            <button
              key={cat.id}
              type="button"
              onClick={() => setActiveCategory(cat.id)}
              className={`rounded-full px-4 py-1.5 text-xs font-semibold transition-colors ${
                activeCategory === cat.id
                  ? "bg-[#1e3a29] text-white shadow-xs"
                  : "bg-[#f4ede1] text-[#5e5346] hover:bg-[#e8dbbf]"
              }`}
            >
              {cat.label}
            </button>
          ))}
        </div>

        {/* Resources Grid */}
        {loading ? (
          <div className="text-sm text-[#665a4c]">Loading resources...</div>
        ) : filteredResources.length === 0 ? (
          <div className="text-sm text-[#665a4c]">No resources found or available for your current week.</div>
        ) : (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
            {filteredResources.map((resource) => (
              <div
                key={resource.id}
                className="rounded-xl border border-[#ebdcc9] bg-[#fdfbf7] p-5 sm:p-6 shadow-[0_2px_12px_rgba(30,24,15,0.03)] flex flex-col justify-between hover:border-[#dfcca6] hover:shadow-md transition-all"
              >
                <div className="space-y-3">
                  <div className="flex items-center justify-between">
                    <span className="inline-flex items-center gap-1.5 rounded-sm bg-[#f4ede1] px-2 py-0.5 text-[10px] font-bold uppercase tracking-wider text-[#1e3a29]">
                      {resource.asset_type === "audio_mp3" ? (
                        <Headphones size={12} />
                      ) : (
                        <FileText size={12} />
                      )}
                      <span>{resource.asset_type.replace('_', ' ').toUpperCase()}</span>
                    </span>
                    <span className="text-[10px] text-[#8e7e6e]">{resource.size_display}</span>
                  </div>

                  <h3 className="font-serif text-lg font-semibold text-[#1e1b18] leading-snug">
                    {resource.title}
                  </h3>
                </div>

                <div className="mt-5 pt-4 border-t border-[#ebdcc9]/60 flex items-center justify-between">
                  <span className="text-[10px] font-semibold text-[#8a6828] uppercase tracking-wider">
                    {resource.foundation_name}
                  </span>

                  <button
                    type="button"
                    onClick={() => handleDownload(resource.storage_path)}
                    className="inline-flex items-center gap-1.5 rounded-sm bg-[#1e3a29] px-3 py-1.5 text-xs font-bold text-white hover:bg-[#274d36] transition-colors"
                  >
                    <Download size={13} />
                    <span>Download</span>
                  </button>
                </div>
              </div>
            ))}
          </div>
        )}
      </div>
    </LearnerShell>
  );
}
