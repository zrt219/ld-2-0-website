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
};

export default nextConfig;
