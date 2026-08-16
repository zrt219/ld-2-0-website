import type { Metadata } from "next";
import "./globals.css";

import { siteCopy, siteUrl } from "@/content/site";

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
  },
  twitter: {
    card: "summary_large_image",
    title: siteCopy.seoTitle,
    description: siteCopy.seoDescription,
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
      className="h-full antialiased"
    >
      <body className="min-h-full">
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(personJsonLd) }}
        />
        {children}
      </body>
    </html>
  );
}
