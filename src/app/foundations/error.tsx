"use client";

import { useEffect } from "react";
import Link from "next/link";
import Image from "next/image";
import { ArrowLeft, RotateCcw, ShieldAlert } from "lucide-react";

export default function FoundationsError({
  error,
  reset,
}: {
  error: Error & { digest?: string };
  reset: () => void;
}) {
  useEffect(() => {
    // Log unexpected errors securely
    console.error("Foundations Portal Error Boundary caught:", error);
  }, [error]);

  return (
    <div className="min-h-screen bg-[#120f0d] text-white flex flex-col justify-between selection:bg-[#c6a55c]/30 selection:text-white">
      {/* Header with Monogram */}
      <header className="border-b border-[rgba(198,165,92,0.2)] bg-[#120f0d]/90 backdrop-blur-md px-6 py-4 flex items-center justify-between">
        <Link href="/foundations/dashboard" className="flex items-center gap-3 group">
          <div className="relative h-10 w-12 shrink-0">
            <Image
              src="/monogramlogo.png"
              alt="Lornette Daye"
              fill
              className="object-contain"
              unoptimized
            />
          </div>
          <div className="flex flex-col">
            <span className="font-serif text-lg tracking-wide text-white group-hover:text-[var(--champagne)] transition-colors">
              Lornette Daye
            </span>
            <span className="text-[10px] tracking-[0.22em] text-[#c6a55c] uppercase">
              Athlete &amp; Coach Portal
            </span>
          </div>
        </Link>
        <div className="text-xs text-neutral-400 font-mono">
          Status: Handled
        </div>
      </header>

      {/* Main Error Card */}
      <main className="flex-1 flex items-center justify-center p-6">
        <div className="max-w-md w-full bg-[#1c1714] border border-[rgba(198,165,92,0.3)] rounded-2xl p-8 sm:p-10 shadow-2xl text-center relative overflow-hidden">
          {/* Subtle background glow */}
          <div className="absolute -top-24 left-1/2 -translate-x-1/2 w-48 h-48 bg-[#c6a55c]/10 rounded-full blur-3xl pointer-events-none" />

          <div className="w-14 h-14 mx-auto mb-6 rounded-full bg-[rgba(198,165,92,0.12)] border border-[rgba(198,165,92,0.35)] flex items-center justify-center text-[#c6a55c]">
            <ShieldAlert className="w-7 h-7" />
          </div>

          <p className="text-[11px] font-bold uppercase tracking-[0.22em] text-[var(--champagne,#c6a55c)] mb-2">
            System Notice
          </p>
          <h1 className="font-serif text-2xl sm:text-3xl text-white mb-3">
            Temporary Interruption
          </h1>
          <p className="text-sm text-neutral-300 leading-relaxed mb-8">
            An unexpected error occurred while loading this section. Your progress and reflections remain securely stored.
          </p>

          <div className="flex flex-col sm:flex-row items-center justify-center gap-3">
            <button
              onClick={() => reset()}
              className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-5 py-3 rounded-lg bg-[#c6a55c] hover:bg-[#b5944d] text-black font-semibold text-xs tracking-wider uppercase transition-all shadow-lg shadow-[#c6a55c]/10"
            >
              <RotateCcw className="w-3.5 h-3.5" />
              Try Again
            </button>
            <Link
              href="/foundations/dashboard"
              className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-5 py-3 rounded-lg border border-[rgba(198,165,92,0.35)] hover:border-[#c6a55c] bg-transparent text-neutral-200 hover:text-white text-xs tracking-wider uppercase transition-all"
            >
              <ArrowLeft className="w-3.5 h-3.5" />
              Return to Dashboard
            </Link>
          </div>

          {error.digest && (
            <p className="mt-6 text-[10px] font-mono text-neutral-500">
              Reference Code: {error.digest}
            </p>
          )}
        </div>
      </main>

      {/* Footer */}
      <footer className="border-t border-[rgba(198,165,92,0.15)] py-4 text-center text-xs text-neutral-500">
        &copy; {new Date().getFullYear()} Lornette Daye. Better People · Better Players.
      </footer>
    </div>
  );
}
