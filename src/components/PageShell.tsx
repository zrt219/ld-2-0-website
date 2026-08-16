import { Footer } from "./Footer";
import { Header } from "./Header";
import { MobileStickyCTA } from "./MobileStickyCTA";

export function PageShell({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen pb-16 md:pb-0">
      <Header />
      {children}
      <Footer />
      <MobileStickyCTA />
    </div>
  );
}
