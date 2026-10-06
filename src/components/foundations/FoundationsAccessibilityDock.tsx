"use client";

import { useState, useEffect, useCallback, useRef } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  ChevronUp,
  SlidersHorizontal,
  X,
  RotateCcw,
  Type,
  Contrast,
  AlignJustify,
  Eye,
  Check,
} from "lucide-react";

type TextSizeOption = "normal" | "large" | "xlarge";

interface A11yPrefs {
  textSize: TextSizeOption;
  highContrast: boolean;
  relaxedSpacing: boolean;
  readingRuler: boolean;
}

const DEFAULT_PREFS: A11yPrefs = {
  textSize: "normal",
  highContrast: false,
  relaxedSpacing: false,
  readingRuler: false,
};

const STORAGE_KEY = "ld_foundations_a11y_prefs";

export function FoundationsAccessibilityDock() {
  const [mounted, setMounted] = useState(false);
  const [isScrolled, setIsScrolled] = useState(false);
  const [isOpen, setIsOpen] = useState(false);
  const [prefs, setPrefs] = useState<A11yPrefs>(DEFAULT_PREFS);
  const [rulerY, setRulerY] = useState(300);
  const drawerRef = useRef<HTMLDivElement>(null);

  // Apply DOM attributes based on active preferences
  const applyPrefsToDom = useCallback((p: A11yPrefs) => {
    if (typeof document === "undefined") return;
    const root = document.documentElement;

    if (p.textSize === "normal") {
      root.removeAttribute("data-a11y-text");
    } else {
      root.setAttribute("data-a11y-text", p.textSize);
    }

    if (p.highContrast) {
      root.setAttribute("data-a11y-contrast", "high");
    } else {
      root.removeAttribute("data-a11y-contrast");
    }

    if (p.relaxedSpacing) {
      root.setAttribute("data-a11y-spacing", "relaxed");
    } else {
      root.removeAttribute("data-a11y-spacing");
    }
  }, []);

  // Hydrate preferences from localStorage and register scroll listener
  useEffect(() => {
    setMounted(true);
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      if (stored) {
        const parsed: A11yPrefs = JSON.parse(stored);
        setPrefs(parsed);
        applyPrefsToDom(parsed);
      }
    } catch {
      // Fallback gracefully if storage is restricted
    }

    const handleScroll = () => {
      setIsScrolled(window.scrollY > 280);
    };

    window.addEventListener("scroll", handleScroll, { passive: true });
    handleScroll();

    return () => {
      window.removeEventListener("scroll", handleScroll);
      // Clean up DOM attributes when leaving page
      if (typeof document !== "undefined") {
        const root = document.documentElement;
        root.removeAttribute("data-a11y-text");
        root.removeAttribute("data-a11y-contrast");
        root.removeAttribute("data-a11y-spacing");
      }
    };
  }, [applyPrefsToDom]);

  // Track reading ruler position
  useEffect(() => {
    if (!prefs.readingRuler) return;

    const handlePointerMove = (e: PointerEvent) => {
      setRulerY(e.clientY);
    };

    window.addEventListener("pointermove", handlePointerMove, { passive: true });
    return () => window.removeEventListener("pointermove", handlePointerMove);
  }, [prefs.readingRuler]);

  // Close drawer on click outside or escape key
  useEffect(() => {
    if (!isOpen) return;

    const handleClickOutside = (e: MouseEvent) => {
      if (drawerRef.current && !drawerRef.current.contains(e.target as Node)) {
        setIsOpen(false);
      }
    };

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        setIsOpen(false);
      }
    };

    document.addEventListener("mousedown", handleClickOutside);
    document.addEventListener("keydown", handleKeyDown);
    return () => {
      document.removeEventListener("mousedown", handleClickOutside);
      document.removeEventListener("keydown", handleKeyDown);
    };
  }, [isOpen]);

  const updatePreference = <K extends keyof A11yPrefs>(key: K, value: A11yPrefs[K]) => {
    const updated: A11yPrefs = { ...prefs, [key]: value };
    setPrefs(updated);
    applyPrefsToDom(updated);
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(updated));
    } catch {
      // Ignore storage errors
    }
  };

  const resetDefaults = () => {
    setPrefs(DEFAULT_PREFS);
    applyPrefsToDom(DEFAULT_PREFS);
    try {
      localStorage.removeItem(STORAGE_KEY);
    } catch {
      // Ignore storage errors
    }
  };

  const scrollToTop = () => {
    window.scrollTo({
      top: 0,
      behavior: "smooth",
    });
  };

  const hasActivePrefs =
    prefs.textSize !== "normal" ||
    prefs.highContrast ||
    prefs.relaxedSpacing ||
    prefs.readingRuler;

  if (!mounted) return null;

  return (
    <>
      {/* Reading Ruler Guide */}
      {prefs.readingRuler && (
        <div
          aria-hidden="true"
          className="pointer-events-none fixed inset-x-0 z-[9999] transition-[top] duration-75 ease-out"
          style={{
            top: `${Math.max(0, rulerY - 24)}px`,
            height: "48px",
            background:
              "linear-gradient(180deg, rgba(199,167,94,0.03) 0%, rgba(199,167,94,0.2) 50%, rgba(199,167,94,0.03) 100%)",
            borderTop: "2px solid rgba(199,167,94,0.5)",
            borderBottom: "2px solid rgba(199,167,94,0.5)",
            boxShadow: "0 0 24px rgba(199,167,94,0.2)",
          }}
        />
      )}

      {/* Floating Luxury Dock */}
      <div
        ref={drawerRef}
        className="fixed bottom-5 right-5 sm:bottom-7 sm:right-7 z-40 flex flex-col items-end gap-2.5"
      >
        {/* Expandable Luxury Accessibility Popover */}
        <AnimatePresence>
          {isOpen && (
            <motion.div
              id="accessibility-drawer"
              role="dialog"
              aria-modal="false"
              aria-label="Accessibility and display settings"
              initial={{ opacity: 0, y: 12, scale: 0.94 }}
              animate={{ opacity: 1, y: 0, scale: 1 }}
              exit={{ opacity: 0, y: 10, scale: 0.94 }}
              transition={{ duration: 0.2, ease: "easeOut" }}
              className="w-[300px] sm:w-[330px] rounded-[2px] border border-[rgba(198,165,92,0.4)] bg-[#171412]/95 p-4 sm:p-5 text-[#faf7f0] shadow-2xl backdrop-blur-xl"
            >
              {/* Header */}
              <div className="flex items-start justify-between border-b border-[rgba(198,165,92,0.25)] pb-3">
                <div>
                  <p className="text-[10px] font-bold uppercase tracking-[0.24em] text-[var(--champagne)]">
                    Accessibility &amp; View
                  </p>
                  <p className="font-serif text-base font-semibold text-white">
                    Display Preferences
                  </p>
                </div>
                <button
                  type="button"
                  onClick={() => setIsOpen(false)}
                  aria-label="Close accessibility options"
                  className="rounded p-1 text-[#b7a891] hover:bg-white/10 hover:text-white transition-colors"
                >
                  <X size={16} aria-hidden="true" />
                </button>
              </div>

              {/* Toggles Container */}
              <div className="mt-3.5 space-y-4">
                {/* 1. Text Sizing */}
                <div>
                  <div className="mb-2 flex items-center justify-between">
                    <span className="flex items-center gap-1.5 text-xs font-semibold uppercase tracking-[0.12em] text-[#e8ddcb]">
                      <Type size={14} className="text-[var(--champagne)]" aria-hidden="true" />
                      Text Scaling
                    </span>
                    <span className="text-[11px] text-[#b7a891]">
                      {prefs.textSize === "normal"
                        ? "100%"
                        : prefs.textSize === "large"
                        ? "112%"
                        : "125%"}
                    </span>
                  </div>
                  <div className="grid grid-cols-3 gap-1 rounded-[1px] bg-white/5 p-1 border border-white/10">
                    {(
                      [
                        { id: "normal", label: "Default", sizeLabel: "A" },
                        { id: "large", label: "Large", sizeLabel: "A+" },
                        { id: "xlarge", label: "XL", sizeLabel: "A++" },
                      ] as const
                    ).map((opt) => (
                      <button
                        key={opt.id}
                        type="button"
                        onClick={() => updatePreference("textSize", opt.id)}
                        className={`flex flex-col items-center justify-center py-1.5 rounded-[1px] text-xs transition-all ${
                          prefs.textSize === opt.id
                            ? "bg-[#c7a75e] font-bold text-[#171412] shadow-sm"
                            : "text-[#d8cdb8] hover:bg-white/10 hover:text-white"
                        }`}
                      >
                        <span className="font-bold">{opt.sizeLabel}</span>
                        <span className="text-[9px] uppercase tracking-wider">{opt.label}</span>
                      </button>
                    ))}
                  </div>
                </div>

                {/* 2. High Contrast Mode */}
                <div className="flex items-center justify-between pt-1">
                  <div className="pr-2">
                    <span className="flex items-center gap-1.5 text-xs font-semibold uppercase tracking-[0.12em] text-[#e8ddcb]">
                      <Contrast size={14} className="text-[var(--champagne)]" aria-hidden="true" />
                      High Contrast
                    </span>
                    <p className="mt-0.5 text-[11px] leading-tight text-[#b7a891]">
                      Darkens text and clarifies borders
                    </p>
                  </div>
                  <button
                    type="button"
                    role="switch"
                    aria-checked={prefs.highContrast}
                    aria-label="Toggle high contrast mode"
                    onClick={() => updatePreference("highContrast", !prefs.highContrast)}
                    className={`relative inline-flex h-6 w-11 shrink-0 cursor-pointer rounded-full border border-[rgba(198,165,92,0.5)] transition-colors duration-200 ease-in-out ${
                      prefs.highContrast ? "bg-[#c7a75e]" : "bg-black/50"
                    }`}
                  >
                    <span
                      className={`pointer-events-none inline-block h-5 w-5 transform rounded-full bg-white shadow-md transition duration-200 ease-in-out ${
                        prefs.highContrast ? "translate-x-5 bg-[#171412]" : "translate-x-0.5"
                      }`}
                    />
                  </button>
                </div>

                {/* 3. Relaxed Line Spacing */}
                <div className="flex items-center justify-between pt-1">
                  <div className="pr-2">
                    <span className="flex items-center gap-1.5 text-xs font-semibold uppercase tracking-[0.12em] text-[#e8ddcb]">
                      <AlignJustify size={14} className="text-[var(--champagne)]" aria-hidden="true" />
                      Relaxed Spacing
                    </span>
                    <p className="mt-0.5 text-[11px] leading-tight text-[#b7a891]">
                      Expands paragraph height for reading
                    </p>
                  </div>
                  <button
                    type="button"
                    role="switch"
                    aria-checked={prefs.relaxedSpacing}
                    aria-label="Toggle relaxed line spacing"
                    onClick={() => updatePreference("relaxedSpacing", !prefs.relaxedSpacing)}
                    className={`relative inline-flex h-6 w-11 shrink-0 cursor-pointer rounded-full border border-[rgba(198,165,92,0.5)] transition-colors duration-200 ease-in-out ${
                      prefs.relaxedSpacing ? "bg-[#c7a75e]" : "bg-black/50"
                    }`}
                  >
                    <span
                      className={`pointer-events-none inline-block h-5 w-5 transform rounded-full bg-white shadow-md transition duration-200 ease-in-out ${
                        prefs.relaxedSpacing ? "translate-x-5 bg-[#171412]" : "translate-x-0.5"
                      }`}
                    />
                  </button>
                </div>

                {/* 4. Reading Ruler Guide */}
                <div className="flex items-center justify-between pt-1">
                  <div className="pr-2">
                    <span className="flex items-center gap-1.5 text-xs font-semibold uppercase tracking-[0.12em] text-[#e8ddcb]">
                      <Eye size={14} className="text-[var(--champagne)]" aria-hidden="true" />
                      Reading Ruler
                    </span>
                    <p className="mt-0.5 text-[11px] leading-tight text-[#b7a891]">
                      Subtle pointer band to track active line
                    </p>
                  </div>
                  <button
                    type="button"
                    role="switch"
                    aria-checked={prefs.readingRuler}
                    aria-label="Toggle reading ruler focus band"
                    onClick={() => updatePreference("readingRuler", !prefs.readingRuler)}
                    className={`relative inline-flex h-6 w-11 shrink-0 cursor-pointer rounded-full border border-[rgba(198,165,92,0.5)] transition-colors duration-200 ease-in-out ${
                      prefs.readingRuler ? "bg-[#c7a75e]" : "bg-black/50"
                    }`}
                  >
                    <span
                      className={`pointer-events-none inline-block h-5 w-5 transform rounded-full bg-white shadow-md transition duration-200 ease-in-out ${
                        prefs.readingRuler ? "translate-x-5 bg-[#171412]" : "translate-x-0.5"
                      }`}
                    />
                  </button>
                </div>
              </div>

              {/* Reset to Defaults Footer */}
              <div className="mt-4 flex items-center justify-between border-t border-[rgba(198,165,92,0.25)] pt-3">
                <button
                  type="button"
                  onClick={resetDefaults}
                  disabled={!hasActivePrefs}
                  className={`inline-flex items-center gap-1.5 text-[11px] font-semibold uppercase tracking-[0.14em] transition-colors ${
                    hasActivePrefs
                      ? "text-[#dfc385] hover:text-white cursor-pointer"
                      : "text-[#6c6155] cursor-not-allowed"
                  }`}
                >
                  <RotateCcw size={12} aria-hidden="true" />
                  <span>Reset All</span>
                </button>
                {hasActivePrefs && (
                  <span className="inline-flex items-center gap-1 text-[10px] font-bold uppercase tracking-wider text-[#dfc385]">
                    <Check size={11} aria-hidden="true" />
                    Customized
                  </span>
                )}
              </div>
            </motion.div>
          )}
        </AnimatePresence>

        {/* Floating Quick Action Buttons */}
        <div className="flex items-center gap-2">
          {/* Accessibility Settings Toggle Button */}
          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            type="button"
            onClick={() => setIsOpen((prev) => !prev)}
            aria-expanded={isOpen}
            aria-controls="accessibility-drawer"
            aria-label="Open accessibility display preferences"
            className="group relative flex h-11 w-11 sm:h-12 sm:w-12 items-center justify-center rounded-[2px] border border-[rgba(198,165,92,0.45)] bg-[#171412]/92 text-[#dfc385] shadow-xl backdrop-blur-md transition-colors hover:border-[#dfc385] hover:bg-[#25201a] hover:text-white cursor-pointer"
          >
            <SlidersHorizontal size={18} aria-hidden="true" className="transition-transform group-hover:rotate-45" />
            {/* Active Preferences Indicator Dot */}
            {hasActivePrefs && (
              <span
                className="absolute top-1.5 right-1.5 h-2 w-2 rounded-full bg-[#dfc385] ring-2 ring-[#171412]"
                aria-label="Custom settings active"
              />
            )}
          </motion.button>

          {/* Smooth Scroll to Top Button */}
          <AnimatePresence>
            {isScrolled && (
              <motion.button
                initial={{ opacity: 0, y: 10, scale: 0.85 }}
                animate={{ opacity: 1, y: 0, scale: 1 }}
                exit={{ opacity: 0, y: 10, scale: 0.85 }}
                whileHover={{ scale: 1.05, y: -2 }}
                whileTap={{ scale: 0.95 }}
                type="button"
                onClick={scrollToTop}
                aria-label="Scroll to top of page"
                className="group flex h-11 w-11 sm:h-12 sm:w-12 items-center justify-center rounded-[2px] border border-[rgba(198,165,92,0.5)] bg-[#c7a75e] text-[#171412] shadow-xl transition-all hover:bg-[#d8b76c] hover:shadow-[0_6px_24px_rgba(199,167,94,0.4)] cursor-pointer"
              >
                <ChevronUp
                  size={20}
                  aria-hidden="true"
                  className="transition-transform duration-200 group-hover:-translate-y-0.5"
                />
              </motion.button>
            )}
          </AnimatePresence>
        </div>
      </div>
    </>
  );
}
