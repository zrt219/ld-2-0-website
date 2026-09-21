"use client";

import { useState, useRef, useEffect, ReactNode } from "react";
import Image from "next/image";
import { LearnerSidebar } from "./LearnerSidebar";
import { LearnerHeader } from "./LearnerHeader";
import { LearnerBottomNav } from "./LearnerBottomNav";
import { X, WifiOff, RefreshCw, CheckCircle2 } from "lucide-react";
import { useFoundationsStore } from "@/lib/foundations/store";
import {
  getPendingOutboxSyncs,
  flushOutboxSync,
  SYNC_STATUS_EVENT,
  type SyncStatusDetail,
} from "@/lib/foundations/offline-store";

type LearnerShellProps = {
  children: ReactNode;
};

export function LearnerShell({ children }: LearnerShellProps) {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const drawerRef = useRef<HTMLDivElement>(null);
  const triggerRef = useRef<HTMLElement | null>(null);

  const { initData, state } = useFoundationsStore();
  const [syncStatus, setSyncStatus] = useState<SyncStatusDetail>({
    isOnline: typeof navigator !== "undefined" ? navigator.onLine : true,
    pendingCount: 0,
    isSyncing: false,
    lastSyncedAt: null,
  });
  const [toastMessage, setToastMessage] = useState<string | null>(null);

  useEffect(() => {
    initData();
  }, [initData]);

  useEffect(() => {
    getPendingOutboxSyncs().then((items) => {
      setSyncStatus((prev) => ({ ...prev, pendingCount: items.length }));
    });

    const handleSyncStatus = (e: Event) => {
      const customEvent = e as CustomEvent<SyncStatusDetail>;
      if (customEvent.detail) {
        setSyncStatus((prev) => ({ ...prev, ...customEvent.detail }));
      }
    };

    const handleOnline = async () => {
      setSyncStatus((prev) => ({ ...prev, isOnline: true }));
      const pending = await getPendingOutboxSyncs();
      if (pending.length > 0) {
        setToastMessage(`Reconnected to network. Syncing ${pending.length} offline reflection${pending.length > 1 ? "s" : ""}...`);
        const res = await flushOutboxSync();
        if (res.synced > 0) {
          setToastMessage(`Synced ${res.synced} reflection${res.synced > 1 ? "s" : ""} to your cloud account.`);
          setTimeout(() => setToastMessage(null), 4000);
        }
      } else {
        setToastMessage("Network connection restored.");
        setTimeout(() => setToastMessage(null), 3000);
      }
    };

    const handleOffline = () => {
      setSyncStatus((prev) => ({ ...prev, isOnline: false }));
      setToastMessage("Working offline. Unsaved notes and reflections are securely cached on this device.");
      setTimeout(() => setToastMessage(null), 5000);
    };

    window.addEventListener(SYNC_STATUS_EVENT, handleSyncStatus as EventListener);
    window.addEventListener("online", handleOnline);
    window.addEventListener("offline", handleOffline);

    return () => {
      window.removeEventListener(SYNC_STATUS_EVENT, handleSyncStatus as EventListener);
      window.removeEventListener("online", handleOnline);
      window.removeEventListener("offline", handleOffline);
    };
  }, []);

  // Focus trap & Escape key dismiss for mobile drawer
  useEffect(() => {
    if (!mobileMenuOpen) return;
    triggerRef.current = document.activeElement as HTMLElement;

    // Move initial focus to drawer close button or first focusable
    const focusables = drawerRef.current?.querySelectorAll<HTMLElement>(
      'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
    );
    focusables?.[0]?.focus();

    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === "Escape") {
        setMobileMenuOpen(false);
      } else if (e.key === "Tab" && drawerRef.current) {
        const items = drawerRef.current.querySelectorAll<HTMLElement>(
          'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
        );
        if (!items.length) return;
        const first = items[0];
        const last = items[items.length - 1];

        if (e.shiftKey && document.activeElement === first) {
          e.preventDefault();
          last.focus();
        } else if (!e.shiftKey && document.activeElement === last) {
          e.preventDefault();
          first.focus();
        }
      }
    };

    window.addEventListener("keydown", handleKeyDown);
    return () => {
      window.removeEventListener("keydown", handleKeyDown);
      triggerRef.current?.focus();
    };
  }, [mobileMenuOpen]);

  if (state.isLoading) {
    return <div className="min-h-screen bg-[#faf7f2] flex items-center justify-center font-serif text-[#1e1b18]">Loading...</div>;
  }

  return (
    <div className="min-h-screen bg-[#faf7f2] text-[#2c2620] font-sans antialiased flex flex-col selection:bg-[#dfc187]/40 selection:text-[#1e1b18]">
      {/* Skip to Content Link */}
      <a
        href="#learner-main-content"
        className="sr-only focus:not-sr-only focus:fixed focus:left-4 focus:top-4 focus:z-[100] focus:bg-[#1e1b18] focus:px-4 focus:py-3 focus:text-xs focus:font-bold focus:uppercase focus:text-[#fbf9f4] focus:outline focus:outline-2 focus:outline-[#c8a86b] focus:shadow-xl rounded-xs"
      >
        Skip to portal content
      </a>

      {/* Top Header */}
      <LearnerHeader onOpenMobileMenu={() => setMobileMenuOpen(true)} />

      <div className="flex flex-1 relative">
        {/* Desktop Sidebar */}
        <div className="hidden lg:block w-[275px] shrink-0 border-r border-[#ebdcc9] bg-[#fbf9f4]">
          <div className="sticky top-16 sm:top-20 h-[calc(100vh-4rem)] sm:h-[calc(100vh-5rem)] overflow-y-auto no-scrollbar">
            <LearnerSidebar />
          </div>
        </div>

        {/* Mobile Slide-out Drawer */}
        {mobileMenuOpen && (
          <div
            className="fixed inset-0 z-50 lg:hidden flex"
            role="dialog"
            aria-modal="true"
            aria-label="Portal Navigation Drawer"
          >
            {/* Backdrop */}
            <div
              className="fixed inset-0 bg-black/50 backdrop-blur-xs transition-opacity"
              onClick={() => setMobileMenuOpen(false)}
              aria-hidden="true"
            />

            {/* Drawer Content */}
            <div
              ref={drawerRef}
              className="relative z-10 flex w-full max-w-[280px] flex-col bg-[#fbf9f4] shadow-2xl border-r border-[#ebdcc9]"
            >
              <div className="flex items-center justify-between border-b border-[#ebdcc9] px-5 py-4">
                <div className="flex items-center gap-2.5">
                  <div className="relative h-8 w-11 shrink-0 overflow-hidden rounded-sm">
                    <Image
                      src="/monogramlogo.png"
                      alt="Lornette Daye LD Monogram Logo"
                      fill
                      sizes="44px"
                      className="object-contain"
                      unoptimized
                    />
                  </div>
                  <span className="font-serif text-sm font-bold tracking-tight text-[#1e1b18]">
                    My Performance Edge
                  </span>
                </div>
                <button
                  type="button"
                  onClick={() => setMobileMenuOpen(false)}
                  aria-label="Close menu"
                  className="flex h-9 w-9 items-center justify-center rounded-sm text-[#5c5144] hover:bg-[#f2e8dc] focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-[var(--gold-dark)]"
                >
                  <X size={18} aria-hidden="true" />
                </button>
              </div>

              <div className="flex-1 overflow-y-auto no-scrollbar">
                <LearnerSidebar onNavClick={() => setMobileMenuOpen(false)} />
              </div>
            </div>
          </div>
        )}

        {/* Main Content Area */}
        <main
          id="learner-main-content"
          tabIndex={-1}
          className="flex-1 min-w-0 pb-20 lg:pb-12 focus:outline-none"
        >
          {children}
        </main>
      </div>

      {/* Offline / Cloud Sync Subtle Notification Toast */}
      {toastMessage && (
        <aside
          aria-label="Network and synchronization notifications"
          role="status"
          aria-live="polite"
          className="fixed bottom-20 sm:bottom-6 right-4 sm:right-6 z-40 flex items-center gap-3 rounded-lg border border-[#ebdcc9] bg-[#fbf9f4]/95 px-3 py-2.5 sm:px-4 sm:py-3 shadow-lg backdrop-blur-md text-xs text-[#1e1b18] animate-in fade-in slide-in-from-bottom-2 duration-200"
        >
          {syncStatus.isSyncing ? (
            <RefreshCw size={15} className="text-[#b89456] animate-spin shrink-0" aria-hidden="true" />
          ) : syncStatus.isOnline ? (
            <CheckCircle2 size={15} className="text-[#1e3a29] shrink-0" aria-hidden="true" />
          ) : (
            <WifiOff size={15} className="text-[#8e7e6e] shrink-0" aria-hidden="true" />
          )}
          <span className="font-medium">{toastMessage}</span>
          <button
            type="button"
            onClick={() => setToastMessage(null)}
            aria-label="Dismiss message"
            className="ml-1 text-[#8e7e6e] hover:text-[#1e1b18]"
          >
            <X size={14} aria-hidden="true" />
          </button>
        </aside>
      )}

      {/* Mobile Bottom Navigation Bar */}
      <LearnerBottomNav />
    </div>
  );
}
