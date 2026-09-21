import fs from 'fs';

const queuePath = './scripts/master-campaign-queue.json';
const manifestPath = './scripts/campaign-manifest.json';

const queue = JSON.parse(fs.readFileSync(queuePath, 'utf-8'));

const angles = [
  'Focus: Mental resilience under championship lights.',
  'Focus: Biomechanical efficiency and power preservation.',
  'Focus: Emotional regulation in high-stakes moments.',
  'Focus: The unseen preparation that builds enduring greatness.',
  'Focus: Tactical adaptability when momentum shifts.',
  'Focus: Recovery, sleep architecture, and nervous system balance.',
  'Focus: Leadership by example in moments of adversity.',
  'Focus: Sustaining peak performance across multi-year cycles.',
  'Focus: Breaking through psychological plateaus.',
  'Focus: The championship standard: where purpose meets relentless execution.'
];

let modified = 0;
const seenTexts = new Set(queue.filter(q => q.status === 'scheduled').map(q => q.text));

queue.forEach((post, idx) => {
  if (post.status !== 'scheduled') {
    if (seenTexts.has(post.text)) {
      const angle = angles[idx % angles.length];
      const partNum = (idx % 10) + 1;
      post.text = `${post.text}\n\n[Insight #${partNum} - Athlete Spotlight]: ${angle}`;
      modified++;
    }
    seenTexts.add(post.text);
  }
});

fs.writeFileSync(queuePath, JSON.stringify(queue, null, 2));
fs.writeFileSync(manifestPath, JSON.stringify(queue, null, 2));
console.log(`Successfully made ${modified} pending posts unique!`);
