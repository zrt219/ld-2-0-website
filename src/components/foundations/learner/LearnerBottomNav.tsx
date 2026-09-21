"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { Compass, LayoutDashboard, PlayCircle, RotateCcw, UserCheck } from "lucide-react";

const mobileTabs = [
  { label: "Dashboard", href: "/foundations/dashboard", icon: LayoutDashboard, exact: true },
  { label: "Lessons", href: "/foundations/lessons", icon: PlayCircle },
  { label: "Tools", href: "/foundations/quick-tools", icon: RotateCcw },
  { label: "My Plan", href: "/foundations/plan", icon: Compass },
  { label: "Account", href: "/foundations/account", icon: UserCheck },
];

export function LearnerBottomNav() {
  const pathname = usePathname();

  const isActive = (href: string, exact?: boolean) => {
    if (exact) {
      return pathname === href;
    }
    return pathname === href || pathname.startsWith(`${href}/`);
  };

  return (
    <nav
      aria-label="Mobile quick tabs"
      className="fixed inset-x-0 bottom-0 z-30 flex h-16 items-center justify-around border-t border-[#e8ded0] bg-[#fcfaf4]/95 px-2 backdrop-blur-md lg:hidden shadow-[0_-4px_16px_rgba(30,24,15,0.05)]"
    >
      {mobileTabs.map((tab) => {
        const Icon = tab.icon;
        const active = isActive(tab.href, tab.exact);
        return (
          <Link
            key={tab.href}
            href={tab.href}
            aria-current={active ? "page" : undefined}
            className={`flex min-h-12 flex-1 flex-col items-center justify-center gap-1 rounded-sm text-[10.5px] font-bold uppercase tracking-wider transition-colors ${
              active
                ? "text-[#1e3a29]"
                : "text-[#6e6355] hover:text-[var(--ink)]"
            }`}
          >
            <Icon
              size={18}
              aria-hidden="true"
              className={active ? "text-[#1e3a29]" : "text-[#7a6f62]"}
            />
            <span>{tab.label}</span>
          </Link>
        );
      })}
    </nav>
  );
}
