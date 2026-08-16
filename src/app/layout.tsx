import type { Metadata } from "next";
import { Inter, Playfair_Display } from "next/font/google";
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

export const metadata: Metadata = {
  metadataBase: new URL(siteUrl),
  title: {
    default: siteCopy.seoTitle,
    template: `%s | ${siteCopy.brandName}`,
  },
  description: siteCopy.seoDescription,
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
        url: "/images/lornette-executive-portrait.jpg",
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
    images: ["/images/lornette-executive-portrait.jpg"],
  },
  icons: {
    icon: "/favicon.ico",
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
  const personJsonLd = {
    "@context": "https://schema.org",
    "@type": "Person",
    name: siteCopy.brandName,
    url: siteUrl,
    jobTitle: siteCopy.verifiedClaims,
    sameAs: siteCopy.socialLinks
      .map((link) => link.href)
      .filter((href) => href.startsWith("http")),
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
        {children}
      </body>
    </html>
  );
}
