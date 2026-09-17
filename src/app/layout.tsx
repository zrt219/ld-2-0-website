import type { Metadata, Viewport } from "next";
import { Inter, Playfair_Display } from "next/font/google";
import { preconnect } from "react-dom";
import { Analytics } from "@vercel/analytics/next";
import "./globals.css";

import { siteCopy, siteUrl } from "@/content/site";

const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
  display: "swap",
});

const playfair = Playfair_Display({
  subsets: ["latin"],
  variable: "--font-playfair",
  display: "swap",
});

export const viewport: Viewport = {
  themeColor: "#faf7f0",
  colorScheme: "light",
  width: "device-width",
  initialScale: 1,
};

export const metadata: Metadata = {
  metadataBase: new URL(siteUrl),
  title: {
    default: siteCopy.seoTitle,
    template: `%s | ${siteCopy.brandName}`,
  },
  description: siteCopy.seoDescription,
  manifest: "/manifest.webmanifest",
  appleWebApp: {
    capable: true,
    statusBarStyle: "default",
    title: siteCopy.brandName,
  },
  alternates: {
    canonical: "/",
  },
  openGraph: {
    title: siteCopy.seoTitle,
    description: siteCopy.seoDescription,
    url: "/",
    siteName: siteCopy.brandName,
    type: "website",
    images: [
      {
        url: "/generated/lornette-executive-portrait.jpg",
        width: 1200,
        height: 630,
        alt: `${siteCopy.brandName} - Keynote Speaker, Executive Coach, Author`,
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: siteCopy.seoTitle,
    description: siteCopy.seoDescription,
    images: ["/generated/lornette-executive-portrait.jpg"],
  },
  icons: {
    icon: [
      { url: "/icon", sizes: "32x32", type: "image/png" },
      { url: "/favicon.ico", sizes: "any" },
    ],
    apple: [
      { url: "/apple-icon", sizes: "180x180", type: "image/png" },
    ],
  },
  robots: {
    index: true,
    follow: true,
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  preconnect("https://www.youtube.com");
  preconnect("https://youtu.be");

  const personJsonLd = {
    "@context": "https://schema.org",
    "@type": "Person",
    name: siteCopy.brandName,
    url: siteUrl,
    image: `${siteUrl}/generated/lornette-executive-portrait.jpg`,
    jobTitle: "Professional Keynote Speaker & Executive Coach",
    description: siteCopy.seoDescription,
    sameAs: siteCopy.socialLinks
      .map((link) => link.href)
      .filter((href) => href.startsWith("http")),
    knowsAbout: [
      "Resilient Leadership",
      "Diversity, Equity & Inclusion",
      "Executive & Athlete Performance Coaching",
      "Youth Development & Mentorship",
    ],
  };

  const webSiteJsonLd = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    name: `${siteCopy.brandName} - Keynote Speaker, Coach, Leader`,
    url: siteUrl,
  };

  return (
    <html
      lang="en"
      data-scroll-behavior="smooth"
      className={`h-full antialiased ${inter.variable} ${playfair.variable}`}
    >
      <body className="min-h-full font-sans">
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(personJsonLd) }}
        />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(webSiteJsonLd) }}
        />
        {children}
        <Analytics />
      </body>
    </html>
  );
}
