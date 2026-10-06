import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  images: {
    unoptimized: true,
    qualities: [75, 95],
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
      {
        source: "/foundations/golf/program",
        destination: "/foundations/golf#program",
        permanent: false,
      },
      {
        source: "/foundations/golf/club-partnership",
        destination: "/foundations/golf#club-partnership",
        permanent: false,
      },
      {
        source: "/foundations/golf/keynote",
        destination: "/foundations/golf#keynote",
        permanent: false,
      },
      {
        source: "/foundations/golf/workshop",
        destination: "/foundations/golf#workshop",
        permanent: false,
      },
      {
        source: "/foundations/golf/register",
        destination: "/book",
        permanent: false,
      },
      {
        source: "/register",
        destination: "/book",
        permanent: false,
      },
      {
        source: "/foundations/register",
        destination: "/book",
        permanent: false,
      },
      {
        source: "/corporate",
        destination: "/foundations/corporate",
        permanent: false,
      },
      {
        source: "/hockey",
        destination: "/foundations/hockey",
        permanent: false,
      },
    ];
  },
};

export default nextConfig;
