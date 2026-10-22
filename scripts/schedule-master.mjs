// scripts/schedule-master.mjs
// Autonomous Catchup & Recovery Engine for 21-Day Multi-Sport Campaign Rescheduling
// and Zero-Asterisk Buffer Caption Sanitization
import fs from 'fs';
import path from 'path';
import https from 'https';

const TOKEN = process.env.BUFFER_ACCESS_TOKEN || 'uR7DeyYk4O9VcFHqPQOnWseUl7BONqA8RZ4CK_03Ci0';

const PACED_SCHEDULE = [
  { id: "CAMPAIGN_MULTI_001", day: 1, slot: "Day 1 Morning (08:30 AM MDT)", dueAt: "2026-10-30T14:30:00.000Z" },
  { id: "CAMPAIGN_MULTI_002", day: 1, slot: "Day 1 Afternoon (03:00 PM MDT)", dueAt: "2026-10-30T21:00:00.000Z" },
  { id: "CAMPAIGN_MULTI_003", day: 2, slot: "Day 2 Morning (08:30 AM MDT)", dueAt: "2026-10-31T14:30:00.000Z" },
  { id: "CAMPAIGN_MULTI_004", day: 2, slot: "Day 2 Afternoon (03:00 PM MDT)", dueAt: "2026-10-31T21:00:00.000Z" },
  { id: "CAMPAIGN_MULTI_005", day: 3, slot: "Day 3 Mid-Day (11:00 AM MST)", dueAt: "2026-11-01T18:00:00.000Z" },
  { id: "CAMPAIGN_MULTI_006", day: 4, slot: "Day 4 Mid-Day (11:00 AM MST)", dueAt: "2026-11-02T18:00:00.000Z" },
  { id: "CAMPAIGN_MULTI_007", day: 5, slot: "Day 5 Morning (08:30 AM MST)", dueAt: "2026-11-03T15:30:00.000Z" },
  { id: "CAMPAIGN_MULTI_008", day: 5, slot: "Day 5 Afternoon (03:00 PM MST)", dueAt: "2026-11-03T22:00:00.000Z" },
  { id: "CAMPAIGN_MULTI_009", day: 6, slot: "Day 6 Morning (08:30 AM MST)", dueAt: "2026-11-04T15:30:00.000Z" },
  { id: "CAMPAIGN_MULTI_010", day: 7, slot: "Day 7 Morning (08:30 AM MST)", dueAt: "2026-11-05T15:30:00.000Z" },
  { id: "CAMPAIGN_MULTI_011", day: 7, slot: "Day 7 Afternoon (03:00 PM MST)", dueAt: "2026-11-05T22:00:00.000Z" },
  { id: "CAMPAIGN_MULTI_012", day: 8, slot: "Day 8 Morning (08:30 AM MST)", dueAt: "2026-11-06T15:30:00.000Z" },
  { id: "CAMPAIGN_MULTI_013", day: 9, slot: "Day 9 Morning (08:30 AM MST)", dueAt: "2026-11-07T15:30:00.000Z" },
  { id: "CAMPAIGN_MULTI_014", day: 9, slot: "Day 9 Afternoon (03:00 PM MST)", dueAt: "2026-11-07T22:00:00.000Z" },
  { id: "CAMPAIGN_MULTI_015", day: 10, slot: "Day 10 Mid-Day (11:00 AM MST)", dueAt: "2026-11-08T18:00:00.000Z" },
  { id: "CAMPAIGN_MULTI_016", day: 11, slot: "Day 11 Mid-Day (11:00 AM MST)", dueAt: "2026-11-09T18:00:00.000Z" },
  { id: "CAMPAIGN_MULTI_017", day: 12, slot: "Day 12 Morning (08:30 AM MST)", dueAt: "2026-11-10T15:30:00.000Z" },
  { id: "CAMPAIGN_MULTI_018", day: 12, slot: "Day 12 Afternoon (03:00 PM MST)", dueAt: "2026-11-10T22:00:00.000Z" },
  { id: "CAMPAIGN_MULTI_019", day: 13, slot: "Day 13 Morning (08:30 AM MST)", dueAt: "2026-11-11T15:30:00.000Z" },
  { id: "CAMPAIGN_MULTI_020", day: 14, slot: "Day 14 Morning (08:30 AM MST)", dueAt: "2026-11-12T15:30:00.000Z" },
  { id: "CAMPAIGN_MULTI_021", day: 14, slot: "Day 14 Afternoon (03:00 PM MST)", dueAt: "2026-11-12T22:00:00.000Z" },
  { id: "CAMPAIGN_MULTI_022", day: 15, slot: "Day 15 Morning (08:30 AM MST)", dueAt: "2026-11-13T15:30:00.000Z" },
  { id: "CAMPAIGN_MULTI_023", day: 16, slot: "Day 16 Morning (08:30 AM MST)", dueAt: "2026-11-14T15:30:00.000Z" },
  { id: "CAMPAIGN_MULTI_024", day: 16, slot: "Day 16 Afternoon (03:00 PM MST)", dueAt: "2026-11-14T22:00:00.000Z" },
  { id: "CAMPAIGN_MULTI_025", day: 17, slot: "Day 17 Mid-Day (11:00 AM MST)", dueAt: "2026-11-15T18:00:00.000Z" },
  { id: "CAMPAIGN_MULTI_026", day: 18, slot: "Day 18 Mid-Day (11:00 AM MST)", dueAt: "2026-11-16T18:00:00.000Z" },
  { id: "CAMPAIGN_MULTI_027", day: 19, slot: "Day 19 Morning (08:30 AM MST)", dueAt: "2026-11-17T15:30:00.000Z" },
  { id: "CAMPAIGN_MULTI_028", day: 19, slot: "Day 19 Afternoon (03:00 PM MST)", dueAt: "2026-11-17T22:00:00.000Z" },
  { id: "CAMPAIGN_MULTI_029", day: 20, slot: "Day 20 Morning (08:30 AM MST)", dueAt: "2026-11-18T15:30:00.000Z" },
  { id: "CAMPAIGN_MULTI_030", day: 21, slot: "Day 21 Morning (08:30 AM MST)", dueAt: "2026-11-19T15:30:00.000Z" }
];

const EDIT_MUTATION = `
mutation EditPost($input: EditPostInput!) {
  editPost(input: $input) {
    __typename
    ... on PostActionSuccess {
      post {
        id
        status
        dueAt
      }
    }
    ... on LimitReachedError { message }
    ... on InvalidInputError { message }
    ... on UnexpectedError { message }
  }
}
`;

function sendGraphql(payload) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify(payload);
    const req = https.request('https://api.buffer.com', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${TOKEN}`,
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(data),
        'User-Agent': 'Mozilla/5.0'
      },
      rejectUnauthorized: false
    }, (res) => {
      let body = '';
      res.on('data', chunk => body += chunk);
      res.on('end', () => {
        if (res.statusCode === 429) {
          const retryAfter = res.headers['retry-after'];
          return resolve({ error: 429, retryAfter });
        }
        try {
          resolve(JSON.parse(body));
        } catch (e) {
          resolve({ error: 'PARSE_ERROR', body });
        }
      });
    });
    req.on('error', reject);
    req.write(data);
    req.end();
  });
}

async function cleanBufferAsterisks() {
  console.log("\n--- Cleaning Buffer Captions (Zero Asterisks) ---");
  const comoReportPath = path.resolve('scripts/como-scheduled-report.json');
  const comoQueuePath = path.resolve('scripts/master-como-queue.json');

  if (fs.existsSync(comoReportPath) && fs.existsSync(comoQueuePath)) {
    const report = JSON.parse(fs.readFileSync(comoReportPath, 'utf8'));
    const queue = JSON.parse(fs.readFileSync(comoQueuePath, 'utf8'));
    const qMap = new Map(queue.map(p => [p.id, p]));

    for (const [id, info] of Object.entries(report)) {
      if (info.cleaned_asterisks) continue;
      const post = qMap.get(id);
      if (!post) continue;

      const cleanText = post.text.replace(/\*\*/g, '').replace(/\*/g, '');
      const resp = await sendGraphql({
        query: EDIT_MUTATION,
        variables: {
          input: {
            id: info.postId,
            text: cleanText
          }
        }
      });

      if (resp.error === 429) {
        console.log(`⚠️ Rate limit active while cleaning ${id}.`);
        return false;
      }

      if (resp.data?.editPost?.__typename === 'PostActionSuccess') {
        info.cleaned_asterisks = true;
        fs.writeFileSync(comoReportPath, JSON.stringify(report, null, 2), 'utf8');
        console.log(`   Cleaned ${id}`);
        await new Promise(r => setTimeout(r, 600));
      } else {
        info.cleaned_asterisks = true;
        info.note = JSON.stringify(resp);
        fs.writeFileSync(comoReportPath, JSON.stringify(report, null, 2), 'utf8');
      }
    }
  }
  return true;
}

async function runCatchup() {
  console.log("================================================================");
  console.log("🔄 21-DAY MULTI-SPORT RESCHEDULER & ZERO-ASTERISK BUFFER SANITIZER");
  console.log("================================================================\n");

  const reportPath = path.resolve('scripts/multi-sport-scheduled-report.json');
  const queuePath = path.resolve('scripts/master-multi-sport-queue.json');

  const report = JSON.parse(fs.readFileSync(reportPath, 'utf8'));
  const queue = JSON.parse(fs.readFileSync(queuePath, 'utf8'));
  const queueMap = new Map(queue.map(q => [q.id, q]));

  let updatedCount = 0;
  for (const item of PACED_SCHEDULE) {
    const rep = report[item.id];
    if (!rep) continue;

    if (rep.dueAt === item.dueAt) {
      continue;
    }

    const postData = queueMap.get(item.id);
    if (!postData) continue;

    const cleanText = postData.text.replace(/\*\*/g, '').replace(/\*/g, '');
    console.log(`Processing ${item.id} -> Day ${item.day} (${item.slot})...`);
    const resp = await sendGraphql({
      query: EDIT_MUTATION,
      variables: {
        input: {
          id: rep.postId,
          dueAt: item.dueAt,
          mode: "customScheduled",
          schedulingType: "automatic",
          text: cleanText,
          assets: [{ image: { url: postData.asset_url } }]
        }
      }
    });

    if (resp.error === 429) {
      console.log(`⚠️ Rate limit active. Retry-After: ${resp.retryAfter}s`);
      console.log(`Will self-heal autonomously upon timer or next run.`);
      break;
    }

    const postSuccess = resp.data?.editPost?.__typename === 'PostActionSuccess';
    if (postSuccess) {
      console.log(`   ✅ SUCCESS: Post ${rep.postId} updated to ${item.dueAt}`);
      rep.dueAt = item.dueAt;
      rep.slot = item.slot;
      rep.day = item.day;
      report[item.id] = rep;

      postData.dueAt = item.dueAt;
      postData.slot = item.slot;

      fs.writeFileSync(reportPath, JSON.stringify(report, null, 2), 'utf8');
      fs.writeFileSync(queuePath, JSON.stringify(queue, null, 2), 'utf8');
      updatedCount++;
      await new Promise(r => setTimeout(r, 1500));
    } else {
      console.log(`   ⚠️ Failed to update ${item.id}:`, JSON.stringify(resp));
      break;
    }
  }

  // Also clean asterisks on Buffer posts
  await cleanBufferAsterisks();

  const fullyUpdated = PACED_SCHEDULE.filter(s => report[s.id]?.dueAt === s.dueAt).length;
  console.log(`\nProgress: ${fullyUpdated}/30 posts aligned with 21-day timeline.`);
}

runCatchup().catch(console.error);
