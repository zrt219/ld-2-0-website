import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const sourceDirs = ["src", "scripts"];
const appDir = path.join(root, "src", "app");
const publicDir = path.join(root, "public");
const failures = [];

function walk(dir, filter = () => true) {
  if (!fs.existsSync(dir)) {
    return [];
  }

  return fs.readdirSync(dir, { withFileTypes: true }).flatMap((entry) => {
    const fullPath = path.join(dir, entry.name);

    if (entry.isDirectory()) {
      return walk(fullPath, filter);
    }

    return filter(fullPath) ? [fullPath] : [];
  });
}

function routePathForPage(filePath) {
  const relative = path.relative(appDir, path.dirname(filePath));
  const segments = relative === "" ? [] : relative.split(path.sep);
  const route = `/${segments.join("/")}`.replace(/\\/g, "/");

  return route === "/page" ? "/" : route;
}

function normalizeInternalPath(href) {
  if (
    !href ||
    href.startsWith("#") ||
    href.startsWith("mailto:") ||
    href.startsWith("tel:") ||
    href.startsWith("http://") ||
    href.startsWith("https://") ||
    href.startsWith("//")
  ) {
    return null;
  }

  const withoutQuery = href.split("?")[0];
  const [pathname] = withoutQuery.split("#");
  return pathname || "/";
}

const appPages = new Set(
  walk(appDir, (filePath) => path.basename(filePath) === "page.tsx").map(routePathForPage),
);

const publicAssets = new Set(
  walk(publicDir).map((filePath) => `/${path.relative(publicDir, filePath).replace(/\\/g, "/")}`),
);

const sourceFiles = sourceDirs.flatMap((dir) =>
  walk(path.join(root, dir), (filePath) => /\.(tsx?|mjs)$/.test(filePath)),
);

const hrefPatterns = [
  /\bhref=["'`]([^"'`]+)["'`]/g,
  /\bhref:\s*["'`]([^"'`]+)["'`]/g,
  /\b(?:primaryHref|secondaryHref)=["'`]([^"'`]+)["'`]/g,
  /<CTAButton[^>]*\bhref=["'`]([^"'`]+)["'`]/g,
];

for (const filePath of sourceFiles) {
  const text = fs.readFileSync(filePath, "utf8");

  for (const pattern of hrefPatterns) {
    for (const match of text.matchAll(pattern)) {
      const href = match[1];
      const internalPath = normalizeInternalPath(href);

      if (!internalPath) {
        continue;
      }

      const isApiRoute = internalPath.startsWith("/api/");
      const isAppRoute = appPages.has(internalPath);
      const isPublicAsset = publicAssets.has(internalPath);

      if (!isApiRoute && !isAppRoute && !isPublicAsset) {
        failures.push({
          file: path.relative(root, filePath),
          href,
        });
      }
    }
  }
}

if (failures.length) {
  console.error("Dead internal links found:");
  for (const failure of failures) {
    console.error(`- ${failure.file}: ${failure.href}`);
  }
  process.exit(1);
}

console.log(`Checked ${sourceFiles.length} source files. No dead internal links found.`);
