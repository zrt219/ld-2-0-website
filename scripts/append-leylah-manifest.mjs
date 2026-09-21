import fs from 'fs';
import path from 'path';
import { leylahCaptions } from './schedule-leylah-campaign.mjs';

const manifestPath = path.join(process.cwd(), 'scripts', 'campaign-manifest.json');
let manifest = [];
if (fs.existsSync(manifestPath)) {
  manifest = JSON.parse(fs.readFileSync(manifestPath, 'utf-8'));
}

console.log(`Current posts in master manifest: ${manifest.length}`);

const timeSlots = [
  { label: '9:00 AM MDT', utcOffset: 15, hour: 9, minute: 0 },
  { label: '1:00 PM MDT', utcOffset: 19, hour: 13, minute: 0 },
  { label: '6:30 PM MDT', utcOffset: 0.5, hour: 18, minute: 30 },
];

let idCounter = manifest.length > 0 ? Math.max(...manifest.map(m => m.id)) : 0;
let postCount = 0;

for (let day = 1; day <= 30; day++) {
  timeSlots.forEach((slot, slotIdx) => {
    const captionObj = leylahCaptions[postCount % leylahCaptions.length];
    const imgFile = 'leylah-' + String(captionObj.imageIndex).padStart(2, '0') + '.png';
    const fullImageUrl = 'https://lornettedaye.com/campaigns/leylah/' + imgFile;
    
    let dueYear = 2026;
    let dueMonth = 8; // September
    let dueDay = day;
    let dueHour = slot.utcOffset;
    let dueMinute = 0;
    
    if (slotIdx === 2) {
      dueDay += 1;
      dueHour = 0;
      dueMinute = 30;
    }
    
    const targetDate = new Date(Date.UTC(dueYear, dueMonth, dueDay, dueHour, dueMinute, 0, 0));
    idCounter++;
    postCount++;
    
    manifest.push({
      id: idCounter,
      campaign: 'leylah-fernandez-september',
      day: day,
      timeMDT: slot.label,
      dueAt: targetDate.toISOString(),
      imageIndex: captionObj.imageIndex,
      imageFile: imgFile,
      imageUrl: fullImageUrl,
      headline: captionObj.headline,
      text: captionObj.text,
      status: 'pending',
      bufferPostId: null,
    });
  });
}

fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2));
console.log(`🎉 Successfully saved 90 Leylah posts for September! Total posts in master manifest: ${manifest.length}`);
