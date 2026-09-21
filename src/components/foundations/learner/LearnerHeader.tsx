"use client";

import { useState } from "react";
import Image from "next/image";
import Link from "next/link";
import { Bell, ChevronDown, Menu, RotateCcw, X } from "lucide-react";
import { useFoundationsStore } from "@/lib/foundations/store";

type LearnerHeaderProps = {
  onOpenMobileMenu: () => void;
};

export function LearnerHeader({ onOpenMobileMenu }: LearnerHeaderProps) {
  const [showResetCard, setShowResetCard] = useState(false);
  const { activeAthlete } = useFoundationsStore();
  const nameParts = activeAthlete.golferName.split(" ");
  const monogram = nameParts.map((n: string) => n[0]).join("").toUpperCase().slice(0, 2);
  const firstName = nameParts[0] || "Golfer";
  return (
    <header className="sticky top-0 z-30 flex min-h-16 sm:min-h-20 h-auto py-2 w-full items-center justify-between border-b border-[#ebdcc9] bg-[#fbf9f5] px-4 lg:px-6 shadow-xs relative overflow-hidden">
      {/* Master Panoramic Sunrise Golf Lake Background */}
      <div className="absolute inset-0 pointer-events-none overflow-hidden">
        <Image
          src="/foundations/learner/banner-header-sunrise-lake.jpg"
          alt=""
          role="presentation"
          fill
          priority
          quality={95}
          sizes="100vw"
          className="object-cover object-center"
        />
        {/* Luxury subtle dual gradient overlay for 100% typographic legibility */}
        <div className="absolute inset-0 bg-gradient-to-r from-[#fbf9f5]/98 via-[#fbf9f5]/88 to-[#fbf9f5]/98 lg:from-[#fbf9f5]/95 lg:via-[#fbf9f5]/70 lg:to-[#fbf9f5]/95 backdrop-blur-[1px]" />
      </div>

      {/* Left Branding & Monogram */}
      <div className="relative z-10 flex items-center gap-2 sm:gap-4 min-w-0 flex-1">
        <button
          type="button"
          onClick={onOpenMobileMenu}
          aria-label="Open portal navigation drawer"
          className="flex h-10 w-10 shrink-0 items-center justify-center rounded-lg border border-[#ebdcc9]/70 bg-[#fbf9f5]/90 text-[#42372c] hover:bg-[#f2e8dc] hover:text-[#1e1b18] lg:hidden focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)]"
        >
          <Menu size={20} aria-hidden="true" />
        </button>

        <Link
          href="/foundations/dashboard"
          className="flex items-center gap-2 sm:gap-3 group min-w-0 rounded-xl px-2 sm:px-2.5 py-1 sm:py-1.5 bg-[#fbf9f5]/90 sm:bg-transparent backdrop-blur-xs sm:backdrop-blur-none border border-[#ebdcc9]/70 sm:border-transparent focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)]"
        >
          {/* Official Monogram Logo */}
          <div className="relative flex h-9 sm:h-11 w-12 sm:w-14 items-center justify-center rounded-sm overflow-hidden shrink-0">
            <Image
              src="/monogramlogo.png"
              alt="Lornette Daye Official Logo"
              fill
              sizes="(max-width: 640px) 48px, 56px"
              className="object-contain"
              priority
              unoptimized
            />
          </div>

          <div className="min-w-0">
            <div className="flex items-center gap-1.5">
              <div className="font-serif text-[14.5px] sm:text-base lg:text-lg font-bold tracking-tight text-[#141210] leading-tight drop-shadow-[0_1px_1px_rgba(255,255,255,0.9)]">
                Lornette’s Foundation Golf
              </div>
            </div>
            <p className="text-[9.5px] sm:text-[10px] font-bold uppercase tracking-[0.16em] sm:tracking-[0.22em] text-[#332b23] drop-shadow-[0_1px_1px_rgba(255,255,255,0.9)]">
              Powered by the Performance Edge Framework
            </p>
          </div>
        </Link>
      </div>

      {/* Center / Right: Greeting & Principle Stack (Matches user mockup) */}
      <div className="relative z-10 flex items-center gap-3 sm:gap-6 shrink-0">
        {/* Morning Greeting with Gold Accent Underline */}
        <div className="hidden lg:flex flex-col items-start leading-tight">
          <span className="font-sans text-[11px] text-[#786b5c] font-medium">
            Good morning,
          </span>
          <span className="font-serif text-sm sm:text-[15px] font-semibold text-[#1e1b18] tracking-tight">
            Playing Your Best When It Matters.
          </span>
          <div className="mt-1 h-[1.5px] w-12 bg-[#c8a86b]" />
        </div>

        {/* 5-Second Mistake Reset Quick Card Button & Modal */}
        <button
          type="button"
          onClick={() => setShowResetCard(true)}
          aria-label="Open 5-Second Mistake Reset Quick Card"
          className="inline-flex items-center gap-1.5 rounded-full border border-[#c8a86b]/60 bg-[#1e3a29] px-2.5 sm:px-3 py-1 text-[11px] sm:text-xs font-bold uppercase tracking-wider text-white hover:bg-[#274d36] transition-colors focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)] shadow-xs"
        >
          <RotateCcw size={13} className="text-[#dfc385]" aria-hidden="true" />
          <span className="hidden sm:inline">5-Sec</span> Reset Card
        </button>

        {/* Notification Bell */}
        <button
          type="button"
          aria-label="Notifications"
          className="relative flex h-9 w-9 items-center justify-center rounded-full text-[#6b5d4d] hover:bg-[#f2e8dc] hover:text-[#1e1b18] transition-colors focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)]"
        >
          <Bell size={18} aria-hidden="true" />
          <span className="absolute top-2 right-2 h-2 w-2 rounded-full bg-[#c8a86b] ring-2 ring-[#fbf9f5]" />
        </button>

        {/* User Profile Pill */}
        <Link
          href="/foundations/account"
          className="flex items-center gap-2.5 rounded-full py-1 px-1.5 sm:px-2.5 text-xs text-[#3d3429] hover:bg-[#f2e8dc]/80 transition-colors focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)]"
        >
          <div className="flex h-8 w-8 items-center justify-center rounded-full bg-[#1e3a29] text-white font-serif font-bold text-xs shadow-xs">
            {monogram}
          </div>
          <div className="hidden sm:block text-left leading-tight">
            <span className="text-[10px] text-[#827464] block">Welcome,</span>
            <span className="font-semibold text-[#1e1b18]">{firstName}</span>
          </div>
          <ChevronDown size={14} className="text-[#827464] hidden sm:block" aria-hidden="true" />
        </Link>

        {/* Principle Stack from Reference Mockup */}
        <div className="hidden xl:flex flex-col text-[8.5px] font-bold uppercase tracking-[0.24em] text-[#6b5d4d] leading-[1.35] border-l border-[#ebdcc9] pl-4 select-none">
          <span>Discipline</span>
          <span>Composure</span>
          <span>Execution</span>
        </div>
      </div>

      {/* 5-Second Mistake Reset Quick Card Modal */}
      {showResetCard && (
        <div
          role="dialog"
          aria-modal="true"
          aria-labelledby="reset-modal-title"
          className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-xs"
        >
          <div className="relative w-full max-w-md rounded-2xl bg-[#faf7f2] border border-[#d9c69e] p-6 shadow-2xl text-[#1e1b18]">
            <div className="flex items-center justify-between border-b border-[#ebdcc9] pb-3 mb-4">
              <div className="flex items-center gap-2">
                <div className="flex h-8 w-8 items-center justify-center rounded-full bg-[#1e3a29] text-[#dfc385]">
                  <RotateCcw size={16} />
                </div>
                <div>
                  <h3 id="reset-modal-title" className="font-serif text-lg font-bold text-[#1e1b18]">
                    5-Second Mistake Reset
                  </h3>
                  <p className="text-[10px] font-bold uppercase tracking-wider text-[#8a6828]">
                    Tool PE-GOLF-03 Quick Reference
                  </p>
                </div>
              </div>
              <button
                type="button"
                onClick={() => setShowResetCard(false)}
                aria-label="Close 5-Second Reset Card"
                className="flex h-8 w-8 items-center justify-center rounded-full text-[#6b5d4d] hover:bg-[#ebdcc9] transition-colors focus-visible:outline focus-visible:outline-2 focus-visible:outline-[#8a6828]"
              >
                <X size={18} />
              </button>
            </div>

            <p className="font-serif italic text-sm text-[#594b3d] mb-4 text-center">
              &ldquo;Your previous shot cannot hit your next shot.&rdquo;
            </p>

            <div className="space-y-2 mb-5 text-xs">
              <div className="flex gap-3 p-2.5 rounded-lg bg-white border border-[#ebdcc9]">
                <span className="flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-[#dfc385]/30 text-[#8a6828] font-bold text-[10px]">1</span>
                <div>
                  <span className="font-bold text-[#1e1b18] block uppercase tracking-wider text-[10.5px]">1. Acknowledge</span>
                  <span className="text-[#665a4c]">Notice what happened without self-criticism or emotion.</span>
                </div>
              </div>

              <div className="flex gap-3 p-2.5 rounded-lg bg-white border border-[#ebdcc9]">
                <span className="flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-[#dfc385]/30 text-[#8a6828] font-bold text-[10px]">2</span>
                <div>
                  <span className="font-bold text-[#1e1b18] block uppercase tracking-wider text-[10.5px]">2. Evaluate</span>
                  <span className="text-[#665a4c]">Identify the objective fact (wind, contact, commitment, or tempo).</span>
                </div>
              </div>

              <div className="flex gap-3 p-2.5 rounded-lg bg-white border border-[#ebdcc9]">
                <span className="flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-[#dfc385]/30 text-[#8a6828] font-bold text-[10px]">3</span>
                <div>
                  <span className="font-bold text-[#1e1b18] block uppercase tracking-wider text-[10.5px]">3. Release</span>
                  <span className="text-[#665a4c]">Take a slow physiological double breath and unhook the shot.</span>
                </div>
              </div>

              <div className="flex gap-3 p-2.5 rounded-lg bg-white border border-[#ebdcc9]">
                <span className="flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-[#dfc385]/30 text-[#8a6828] font-bold text-[10px]">4</span>
                <div>
                  <span className="font-bold text-[#1e1b18] block uppercase tracking-wider text-[10.5px]">4. Reset</span>
                  <span className="text-[#665a4c]">Execute a physical trigger: unvelcro glove, ground clubhead, settle stance.</span>
                </div>
              </div>

              <div className="flex gap-3 p-2.5 rounded-lg bg-white border border-[#ebdcc9]">
                <span className="flex h-5 w-5 shrink-0 items-center justify-center rounded-full bg-[#dfc385]/30 text-[#8a6828] font-bold text-[10px]">5</span>
                <div>
                  <span className="font-bold text-[#1e1b18] block uppercase tracking-wider text-[10.5px]">5. Recommit</span>
                  <span className="text-[#665a4c]">Step into the next shot with full focus and absolute confidence.</span>
                </div>
              </div>
            </div>

            <div className="flex justify-end">
              <button
                type="button"
                onClick={() => setShowResetCard(false)}
                className="w-full rounded-lg bg-[#1e3a29] py-2.5 text-xs font-bold uppercase tracking-wider text-white hover:bg-[#274d36] transition-colors focus-visible:outline focus-visible:outline-2 focus-visible:outline-[#8a6828]"
              >
                Done / Return to Play
              </button>
            </div>
          </div>
        </div>
      )}
    </header>
  );
}
