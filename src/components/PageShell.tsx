import { Footer } from "./Footer";
import { Header } from "./Header";
import { MobileStickyCTA } from "./MobileStickyCTA";

export function PageShell({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen pb-16 md:pb-0">
      <a
        href="#main-content"
        className="sr-only focus:not-sr-only focus:fixed focus:left-4 focus:top-4 focus:z-[100] focus:bg-[var(--ink)] focus:px-4 focus:py-3 focus:text-sm focus:font-bold focus:uppercase focus:text-[var(--ivory)] focus:outline focus:outline-2 focus:outline-offset-2 focus:outline-[var(--champagne)]"
      >
        Skip to main content
      </a>
      <Header />
      <div id="main-content" tabIndex={-1}>
        {children}
      </div>
      <Footer />
      <MobileStickyCTA />
    </div>
  );
}
