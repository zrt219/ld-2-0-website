import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  images: {
    unoptimized: true,
  },
  experimental: {
    workerThreads: true,
  },
  turbopack: {
    root: process.cwd(),
  },
  async headers() {
    return [
      {
        source: "/:all*(svg|jpg|jpeg|png|webp|avif|ico|woff2)",
        headers: [
          {
            key: "Cache-Control",
            value: "public, max-age=31536000, immutable",
          },
        ],
      },
    ];
  },
  async redirects() {
    return [
      {
        source: "/goal",
        destination: "/foundations/plan",
        permanent: false,
      },
      {
        source: "/foundations/goal",
        destination: "/foundations/plan",
        permanent: false,
      },
      {
        source: "/grill-me",
        destination: "/foundations/grill-me",
        permanent: false,
      },
      {
        source: "/performance/admin",
        destination: "/foundations/admin",
        permanent: false,
      },
    ];
  },
};

export default nextConfig;
