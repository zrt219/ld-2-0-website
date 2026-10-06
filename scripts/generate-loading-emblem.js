const sharp = require('sharp');
const path = require('path');

async function main() {
  const inputPath = 'C:/Users/Zhane/.gemini/antigravity/brain/30de7d90-46c3-4285-b065-64a26e802a94/.user_uploaded/media_1791264973658.jpg';
  const size = 360;
  const radius = size / 2;
  const circleSvg = Buffer.from(
    `<svg width="${size}" height="${size}"><circle cx="${radius}" cy="${radius}" r="${radius}" fill="#fff" /></svg>`
  );

  // 1. Circular badge with marble & gold
  await sharp(inputPath)
    .resize(size, size)
    .composite([{ input: circleSvg, blend: 'dest-in' }])
    .png()
    .toFile('public/ld-loading-badge.png');
  console.log('Saved public/ld-loading-badge.png');

  // 2. High-res original square emblem
  await sharp(inputPath)
    .resize(512, 512)
    .webp({ quality: 92 })
    .toFile('public/ld-luxury-emblem.webp');
  console.log('Saved public/ld-luxury-emblem.webp');
}

main().catch(console.error);
