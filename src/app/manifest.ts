import type { MetadataRoute } from "next";

import { siteCopy } from "@/content/site";

export default function manifest(): MetadataRoute.Manifest {
  return {
    name: `${siteCopy.brandName} | Keynote Speaker, Executive Coach & Author`,
    short_name: siteCopy.brandName,
    description: siteCopy.seoDescription,
    start_url: "/",
    display: "standalone",
    background_color: "#faf7f0",
    theme_color: "#faf7f0",
    icons: [
      {
        src: "/icon",
        sizes: "32x32",
        type: "image/png",
      },
      {
        src: "/apple-icon",
        sizes: "180x180",
        type: "image/png",
      },
      {
        src: "/favicon.ico",
        sizes: "any",
        type: "image/x-icon",
      },
    ],
  };
}
