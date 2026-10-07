"use client";

import { useState } from "react";
import Image from "next/image";
import Link from "next/link";
import { useRouter } from "next/navigation";
import { useFoundationsStore, ADMIN_ATHLETE } from "@/lib/foundations/store";
import {
  TrackId,
  getTrackConfig,
} from "@/lib/foundations/track-registry";
import {
  verifyAdminCodeAction,
  createGuestPreviewSessionAction,
} from "@/app/foundations/login/actions";
import {
  ArrowRight,
  CheckCircle2,
  ChevronRight,
  Globe,
  KeyRound,
  ShieldCheck,
  Smartphone,
  Sparkles,
} from "lucide-react";

interface PathwaySelectOption {
  id: TrackId;
  title: string;
  category: string;
  discipline: string;
  description: string;
  cardImage: string;
  imageAlt: string;
  objectPosition: string;
}

const PATHWAY_OPTIONS: PathwaySelectOption[] = [
  {
    id: "golf",
    title: "Golf",
    category: "ATHLETE PATHWAY",
    discipline: "Championship Golf",
    description: "Mental performance, composure, and repeatable execution for competitive golfers.",
    cardImage: "/foundations/select-stock/golf.jpg",
    imageAlt: "Diverse competitive golfers on fairway at golden hour sunset",
    objectPosition: "center 25%",
  },
  {
    id: "hockey",
    title: "Hockey",
    category: "TEAM PATHWAY",
    discipline: "High-Performance Hockey",
    description: "Shift recovery, high-speed poise, pressure regulation, and champion team culture.",
    cardImage: "/foundations/select-stock/hockey.jpg",
    imageAlt: "Diverse elite hockey players at rink bench in dramatic arena light",
    objectPosition: "center 20%",
  },
  {
    id: "corporate",
    title: "Corporate",
    category: "ORGANIZATIONAL PATHWAY",
    discipline: "Executive Leadership",
    description: "Executive composure, people-centred trust, and boardroom clarity under high-stakes pressure.",
    cardImage: "/foundations/select-stock/corporate.jpg",
    imageAlt: "Diverse executive leadership team in high-level corporate boardroom",
    objectPosition: "center 20%",
  },
  {
    id: "europe",
    title: "Europe",
    category: "EUROPEAN PARTNERSHIPS",
    discipline: "Continental Academy Systems",
    description: "Transatlantic academy pathways, multi-nation partnerships, and European sports federations.",
    cardImage: "/foundations/select-stock/europe.jpg",
    imageAlt: "Diverse athletes and sports leaders on panoramic alpine academy terrace",
    objectPosition: "center 20%",
  },
];

export default function FoundationsSelectPage() {
  const router = useRouter();
  const {
    state,
    setActiveTrack,
    setActiveRegion,
    setActiveAthleteId,
  } = useFoundationsStore();

  const [selectedTrack, setSelectedTrack] = useState<TrackId>(
    (state.activeTrack as TrackId) || "golf"
  );
  const [accessCode, setAccessCode] = useState("");
  const [authError, setAuthError] = useState<string | null>(null);
  const [authSuccess, setAuthSuccess] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isGuestLoading, setIsGuestLoading] = useState(false);

  const activeConfig = getTrackConfig(selectedTrack);
  const activeOption = PATHWAY_OPTIONS.find((t) => t.id === selectedTrack) || PATHWAY_OPTIONS[0];

  const handleSelectTrack = (trackId: TrackId) => {
    setSelectedTrack(trackId);
    setActiveTrack(trackId);
    if (trackId === "europe") {
      setActiveRegion("europe");
    } else {
      setActiveRegion("north_america");
    }
  };

  const handleEnterWithCode = async (e: React.FormEvent) => {
    e.preventDefault();
    setAuthError(null);
    setAuthSuccess(null);
    setIsSubmitting(true);

    const codeToVerify = accessCode.trim().toUpperCase() || "COACH2026";
    const res = await verifyAdminCodeAction(codeToVerify);

    if (!res.success) {
      setAuthError(res.message);
      setIsSubmitting(false);
      return;
    }

    setActiveTrack(selectedTrack);
    if (selectedTrack === "europe") {
      setActiveRegion("europe");
    }
    setActiveAthleteId(ADMIN_ATHLETE.id);
    setAuthSuccess(`Access verified. Launching your ${activeConfig.label} workspace...`);

    setTimeout(() => {
      router.push("/foundations/dashboard");
    }, 400);
  };

  const handleGuestPreview = async (trackIdOverride?: TrackId) => {
    const targetTrack = trackIdOverride || selectedTrack;
    setIsGuestLoading(true);
    setAuthError(null);

    await createGuestPreviewSessionAction();

    setActiveTrack(targetTrack);
    if (targetTrack === "europe") {
      setActiveRegion("europe");
    } else {
      setActiveRegion("north_america");
    }

    window.location.assign("/foundations/dashboard");
  };

  return (
    <main className="min-h-screen bg-[#faf7f0] text-[var(--ink)] flex flex-col justify-between selection:bg-[#f0cf7a] selection:text-[#171412]">
      {/* Top Header */}
      <header className="border-b border-[#dfd1b4] bg-[#fbf8f0]/95 backdrop-blur-md sticky top-0 z-30">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
          <Link href="/foundations" className="flex items-center gap-3 group">
            <div className="relative h-11 w-14 shrink-0">
              <Image
                src="/monogramlogo.png"
                alt="Lornette Daye Official Logo"
                fill
                sizes="56px"
                className="object-contain"
                priority
                unoptimized
              />
            </div>
            <div>
              <p className="font-serif text-lg font-bold text-[var(--ink)] leading-tight group-hover:text-[var(--gold-dark)] transition-colors">
                Lornette’s Foundations
              </p>
              <p className="text-[10px] font-bold uppercase tracking-[0.22em] text-[var(--gold-dark)]">
                Universal Performance Gateway
              </p>
            </div>
          </Link>

          <div className="flex items-center gap-3">
            <Link
              href="/foundations/login"
              className="text-xs font-semibold text-[#5c5246] hover:text-[var(--ink)] px-3.5 py-2 rounded-[3px] hover:bg-[#faf4e6] transition-colors border border-[#dfd1b4]"
            >
              Sign In via Email
            </Link>
          </div>
        </div>
      </header>

      {/* Main Selection Body */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 sm:py-14 flex-1 w-full space-y-12">
        {/* Intro Headline */}
        <div className="text-center max-w-3xl mx-auto space-y-3.5">
          <div className="inline-flex items-center gap-2 rounded-full border border-[#d9c69e] bg-[#faf4e6] px-4 py-1 text-[11px] font-bold uppercase tracking-[0.22em] text-[var(--gold-dark)]">
            <Sparkles size={12} />
            <span>Select Your Performance Pathway</span>
          </div>
          <h1 className="font-serif text-3xl sm:text-4xl lg:text-5xl font-semibold tracking-tight text-[var(--ink)] leading-[1.12]">
            Choose Your Performance Pathway
          </h1>
          <p className="font-sans text-sm sm:text-base text-[#5c5246] leading-relaxed">
            Every pathway provides a focused private workspace powered by Lornette Daye’s 10 Athletic Foundations. Select your athletic or corporate discipline below.
          </p>
        </div>

        {/* ========================================================= */}
        {/* 4 EDITORIAL PATHWAY CARDS WITH DOCKED LUXURY PLAQUES       */}
        {/* ========================================================= */}
        <section aria-label="Performance Tracks" className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6 sm:gap-7">
          {PATHWAY_OPTIONS.map((trk) => {
            const isSelected = trk.id === selectedTrack;
            return (
              <div
                key={trk.id}
                onClick={() => handleSelectTrack(trk.id)}
                className={`group relative flex flex-col justify-end rounded-[4px] overflow-hidden border transition-all duration-300 cursor-pointer aspect-[10/16] sm:aspect-[10/15] shadow-[0_12px_32px_rgba(30,24,15,0.08)] ${
                  isSelected
                    ? "border-[var(--gold-dark)] ring-2 ring-[var(--gold-dark)]/50 shadow-[0_20px_45px_rgba(198,165,92,0.3)] -translate-y-1.5"
                    : "border-[#dfd1b4] hover:border-[var(--gold-dark)] hover:shadow-[0_20px_45px_rgba(198,165,92,0.22)] hover:-translate-y-1"
                }`}
              >
                {/* Full Photographic Asset */}
                <Image
                  src={trk.cardImage}
                  alt={trk.imageAlt}
                  fill
                  sizes="(max-width: 640px) 100vw, (max-width: 1024px) 50vw, 25vw"
                  quality={95}
                  priority
                  className="object-cover transition-transform duration-700 ease-out group-hover:scale-105 pointer-events-none"
                  style={{ objectPosition: trk.objectPosition }}
                />

                {/* Cinematic Scrims */}
                <div className="pointer-events-none absolute inset-0 bg-gradient-to-t from-black/95 via-black/40 to-black/10" />
                <div className="pointer-events-none absolute inset-0 ring-1 ring-inset ring-white/10 group-hover:ring-[rgba(223,195,133,0.35)] transition-all duration-300" />

                {/* Glowing Aura when Selected */}
                {isSelected && (
                  <div className="pointer-events-none absolute -inset-px rounded-[4px] bg-[radial-gradient(ellipse_at_bottom,rgba(223,195,133,0.25)_0%,transparent_70%)]" />
                )}

                {/* Docked Luxury Editorial Plaque at Bottom (Flush Invariant) */}
                <div className="relative z-10 border-t border-[rgba(198,165,92,0.4)] bg-[rgba(18,15,13,0.88)] p-5 backdrop-blur-md shadow-2xl space-y-2">
                  <div className="flex items-center justify-between gap-2">
                    <p className="text-[10px] font-extrabold uppercase tracking-[0.24em] text-[var(--champagne)]">
                      {trk.category}
                    </p>
                    {isSelected ? (
                      <span className="inline-flex items-center gap-1 rounded-full bg-[#1e3a29] border border-[#a7f3d0]/40 px-2 py-0.5 text-[9px] font-bold text-white shadow-xs">
                        <CheckCircle2 size={10} /> Active
                      </span>
                    ) : (
                      <span className="text-[9px] font-bold uppercase tracking-wider text-[#a09485] group-hover:text-white transition-colors">
                        Click to Select
                      </span>
                    )}
                  </div>

                  <h3 className="font-serif text-2xl font-bold text-white leading-tight">
                    {trk.title}
                  </h3>

                  <p className="text-xs text-[#cfc5b4] leading-relaxed line-clamp-2">
                    {trk.description}
                  </p>

                  <div className="pt-2.5 border-t border-white/10 flex items-center justify-between">
                    <span
                      className={`text-[10.5px] font-bold uppercase tracking-[0.14em] ${
                        isSelected ? "text-[#dfc385]" : "text-[#b0a291] group-hover:text-white"
                      }`}
                    >
                      {isSelected ? "Currently Chosen" : "Select Pathway →"}
                    </span>

                    <button
                      type="button"
                      onClick={(e) => {
                        e.stopPropagation();
                        handleGuestPreview(trk.id);
                      }}
                      className="relative z-20 inline-flex items-center gap-1 rounded-[3px] bg-white/10 hover:bg-white/20 px-2.5 py-1 text-[10px] font-bold uppercase tracking-wider text-white transition-colors border border-white/20 cursor-pointer"
                      title={`Preview ${trk.title} as guest`}
                    >
                      <Smartphone size={10} />
                      <span>Preview</span>
                    </button>
                  </div>
                </div>
              </div>
            );
          })}
        </section>

        {/* ========================================================= */}
        {/* INTEGRATED WARM IVORY WORKSPACE UNLOCK PANEL              */}
        {/* ========================================================= */}
        <section
          aria-label="Unlock Workspace"
          className="rounded-xl border border-[#dfd1b4] bg-white p-6 sm:p-8 shadow-[0_12px_40px_rgba(30,24,15,0.06)] max-w-4xl mx-auto space-y-6 text-[var(--ink)]"
        >
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-[#dfd1b4] pb-5">
            <div>
              <p className="text-[11px] font-bold uppercase tracking-[0.22em] text-[var(--gold-dark)]">
                Selected Performance Pathway
              </p>
              <h2 className="font-serif text-2xl font-bold text-[var(--ink)] mt-0.5">
                {activeConfig.label} Workspace Ready
              </h2>
              <p className="text-xs text-[#5c5246] mt-1">
                {activeConfig.heroTagline}
              </p>
            </div>

            {selectedTrack === "europe" && (
              <div className="inline-flex items-center gap-1.5 rounded-full bg-[#f0f9ff] border border-[#0284c7]/40 px-3.5 py-1 text-xs font-bold text-[#0369a1] self-start sm:self-center">
                <Globe size={13} />
                <span>EU GDPR Sovereign Track</span>
              </div>
            )}
          </div>

          {/* Entrance Form */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 items-stretch">
            {/* Left: Code Verification */}
            <form onSubmit={handleEnterWithCode} className="space-y-3.5 flex flex-col justify-between">
              <div className="space-y-2">
                <label htmlFor="access_code" className="block text-xs font-bold uppercase tracking-wider text-[#3d362e]">
                  Member or Admin Access Code
                </label>
                <div className="relative">
                  <KeyRound size={16} className="absolute left-3.5 top-1/2 -translate-y-1/2 text-[var(--gold-dark)]" />
                  <input
                    id="access_code"
                    type="text"
                    value={accessCode}
                    onChange={(e) => setAccessCode(e.target.value)}
                    placeholder="e.g. COACH2026 or cohort code"
                    className="w-full rounded-[4px] border border-[#dfd1b4] bg-[#faf7f0] pl-10 pr-4 py-2.5 text-sm text-[var(--ink)] placeholder:text-[#9c8e7d] focus:border-[var(--gold-dark)] focus:ring-1 focus:ring-[var(--gold-dark)] outline-none transition-all uppercase font-medium"
                  />
                </div>
                <div className="flex items-center justify-between text-[11px] text-[#786c5e]">
                  <span>Member or Coach verification</span>
                  <button
                    type="button"
                    onClick={() => setAccessCode("COACH2026")}
                    className="text-[var(--gold-dark)] font-semibold hover:underline cursor-pointer"
                  >
                    Quick-fill COACH2026
                  </button>
                </div>
              </div>

              {authError && (
                <div className="rounded-[4px] bg-[#fef2f2] border border-[#f87171]/40 p-2.5 text-xs text-[#b91c1c] font-medium">
                  {authError}
                </div>
              )}

              {authSuccess && (
                <div className="rounded-[4px] bg-[#ecfdf5] border border-[#34d399]/40 p-2.5 text-xs text-[#047857] font-medium">
                  {authSuccess}
                </div>
              )}

              <button
                type="submit"
                disabled={isSubmitting}
                className="w-full inline-flex min-h-12 items-center justify-center gap-2 rounded-[3px] bg-[#c7a75e] hover:bg-[#d8b76c] px-6 py-3 text-xs font-bold uppercase tracking-[0.16em] text-[#171412] shadow-md transition-all cursor-pointer disabled:opacity-50"
              >
                <span>{isSubmitting ? "Verifying..." : `Enter ${activeConfig.label} Dashboard`}</span>
                <ArrowRight size={15} />
              </button>
            </form>

            {/* Right: Universal Guest Mobile Preview for Any Track */}
            <div className="rounded-xl border border-[#dfd1b4] bg-[#faf7f0] p-5 space-y-3.5 flex flex-col justify-between">
              <div>
                <div className="flex items-center gap-2 text-[var(--gold-dark)]">
                  <Smartphone size={18} />
                  <span className="text-xs font-bold uppercase tracking-wider">
                    Instant Guest Preview
                  </span>
                </div>
                <h3 className="font-serif text-lg font-semibold text-[var(--ink)] mt-1">
                  Preview {activeConfig.label} Without Login
                </h3>
                <p className="text-xs text-[#5c5246] leading-relaxed mt-1">
                  Instant guest access across all devices. Experience the full {activeConfig.label} workspace, routine cadence protocols, and 10 Foundations modules.
                </p>
              </div>

              <div className="pt-2">
                <button
                  type="button"
                  onClick={() => handleGuestPreview()}
                  disabled={isGuestLoading}
                  className="w-full inline-flex min-h-11 items-center justify-center gap-2 rounded-[3px] border border-[#dfd1b4] bg-white hover:bg-[#f6ede0] px-4 py-2.5 text-xs font-bold uppercase tracking-wider text-[var(--ink)] transition-colors cursor-pointer disabled:opacity-50 shadow-xs"
                >
                  <span>{isGuestLoading ? "Opening Preview..." : `Launch Guest Preview (${activeConfig.label})`}</span>
                  <ChevronRight size={14} />
                </button>
              </div>
            </div>
          </div>
        </section>
      </div>

      {/* Footer */}
      <footer className="border-t border-[#dfd1b4] bg-[#f5eedf] py-6 text-center text-xs text-[#786c5e]">
        <p>© 2026 Lornette Daye. All rights reserved. · Better People · Better Players.</p>
      </footer>
    </main>
  );
}
