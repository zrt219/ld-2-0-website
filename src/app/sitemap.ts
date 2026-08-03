import type { MetadataRoute } from "next";

import { posts, requiredRoutes, siteUrl } from "@/content/site";

export default function sitemap(): MetadataRoute.Sitemap {
  const routes = Array.from(new Set([
    ...requiredRoutes,
    ...posts.map((post) => `/blog/${post.slug}`),
  ]));

  return routes.map((route) => ({
    url: `${siteUrl}${route === "/" ? "" : route}`,
    lastModified: new Date("2026-05-17"),
    changeFrequency: "monthly",
    priority: route === "/" ? 1 : 0.7,
  }));
}
