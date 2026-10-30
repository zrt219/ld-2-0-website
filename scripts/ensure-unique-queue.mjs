import fs from 'fs';

const queuePath = './scripts/master-campaign-queue.json';
const manifestPath = './scripts/campaign-manifest.json';

const queue = JSON.parse(fs.readFileSync(queuePath, 'utf-8'));

const angleThemes = [
  'Focus: Mental resilience and composure under high stakes.',
  'Focus: Biomechanical power generation and kinetic efficiency.',
  'Focus: Emotional intelligence and poise under extreme pressure.',
  'Focus: The unseen work that distinguishes good from iconic.',
  'Focus: Tactical adaptation and split-second decision making.',
  'Focus: Nervous system regulation and recovery protocols.',
  'Focus: Authentic leadership and inspiring team culture.',
  'Focus: Sustained excellence across championship campaigns.',
  'Focus: Overcoming setbacks and turning adversity into fuel.',
  'Focus: The championship standard: where purpose meets execution.'
];

const seenTexts = new Set(queue.filter(q => q.status === 'scheduled').map(q => q.text));
let madeUnique = 0;

queue.forEach((post, idx) => {
  if (post.status !== 'scheduled') {
    if (seenTexts.has(post.text)) {
      const theme = angleThemes[idx % angleThemes.length];
      post.text = `${post.text}\n\nKEY DIMENSION: ${theme}`;
      madeUnique++;
    }
    seenTexts.add(post.text);
  }
});

const METADATA_TAG_REGEX = /[\(\[]\s*(?:DAY\b|SLOT\b|POST\b|WAVE\b)[^\]\)]*[\)\]]/i;
queue.forEach((post) => {
  if (post.headline && METADATA_TAG_REGEX.test(post.headline)) {
    throw new Error(`[Rule 9 Invariant Violation] Post #${post.id} headline contains forbidden metadata tag: ${post.headline}`);
  }
  if (post.text && METADATA_TAG_REGEX.test(post.text)) {
    throw new Error(`[Rule 9 Invariant Violation] Post #${post.id} text contains forbidden metadata tag`);
  }
  if ((post.text && post.text.includes('*')) || (post.headline && post.headline.includes('*'))) {
    throw new Error(`[Rule 7 Invariant Violation] Post #${post.id} contains forbidden asterisk`);
  }
});

fs.writeFileSync(queuePath, JSON.stringify(queue, null, 2));
fs.writeFileSync(manifestPath, JSON.stringify(queue, null, 2));
console.log(`Successfully made ${madeUnique} pending queue items 100% unique.`);
