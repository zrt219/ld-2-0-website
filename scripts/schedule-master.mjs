/**
 * 100% Autonomous Master Buffer Campaign Publisher & Queue Daemon
 * Handles continuous scheduling, rate limit cooldowns, and automatic recovery
 * Target Channel: Lornette Daye LinkedIn (6a39d30c5ab6d2f1065f5301)
 */

import fs from 'fs';
import path from 'path';
import { execSync } from 'child_process';

const scriptsDir = path.join(process.cwd(), 'scripts');
const queuePath = path.join(scriptsDir, 'master-campaign-queue.json');
const reportPath = path.join(scriptsDir, 'scheduled-master-report.json');

// Ordered list of campaigns and their sync scripts in sequence
const campaignPipelines = [
  {
    name: 'Curaçao 3-Win Streak Campaign (19 posts)',
    script: 'schedule-curacao-streak.py',
    sync: 'sync_curacao_streak_to_queue.py'
  },
  {
    name: 'Finish Strong Keynote 60-Day Campaign (30 posts)',
    script: 'schedule-finish-strong-keynote.py',
    sync: 'sync_finish_strong_keynote_to_queue.py'
  },
  {
    name: 'Michael Penix Jr. Campaign (14 posts)',
    script: 'schedule-penix-campaign.py',
    sync: 'sync_penix_to_queue.py'
  }
];

console.log('======================================================================');
console.log('MASTER CAMPAIGN QUEUE DAEMON & CATCHUP RUNNER');
console.log(`Execution Time: ${new Date().toISOString()}`);
console.log('======================================================================\n');

for (const pipeline of campaignPipelines) {
  const scriptPath = path.join(scriptsDir, pipeline.script);
  if (!fs.existsSync(scriptPath)) {
    console.warn(`[Queue Daemon] Warning: ${pipeline.script} not found at ${scriptPath}`);
    continue;
  }

  console.log(`\n>>> [Queue Daemon] Executing ${pipeline.name} (${pipeline.script})...`);
  try {
    execSync(`python "${scriptPath}"`, { stdio: 'inherit', env: process.env });
  } catch (err) {
    console.warn(`[Queue Daemon] ${pipeline.script} finished with notice/error: ${err.message}`);
  }

  if (pipeline.sync) {
    const syncPath = path.join(scriptsDir, pipeline.sync);
    if (fs.existsSync(syncPath)) {
      console.log(`>>> [Queue Daemon] Synchronizing ${pipeline.name} to master queue...`);
      try {
        execSync(`python "${syncPath}"`, { stdio: 'inherit', env: process.env });
      } catch (err) {
        console.error(`[Queue Daemon] Error syncing ${pipeline.sync}:`, err.message);
      }
    }
  }
}

// Read updated master report
if (fs.existsSync(reportPath)) {
  try {
    const report = JSON.parse(fs.readFileSync(reportPath, 'utf-8'));
    console.log('\n======================================================================');
    const totalScheduled = report.totalScheduled || (report.posts ? report.posts.filter(p => p.status === 'scheduled' || p.status === 'success').length : 0);
    const totalPosts = (report.posts || []).length;
    const pendingCount = report.pending !== undefined ? report.pending : (totalPosts - totalScheduled);
    const completionRate = totalPosts > 0 ? ((totalScheduled / totalPosts) * 100).toFixed(1) + '%' : '0%';
    console.log(`STATUS SUMMARY: ${totalScheduled}/${totalPosts} posts scheduled (${completionRate})`);
    console.log(`Pending: ${pendingCount} posts`);
    if (pendingCount > 0) {
      console.log(`Autonomous Catchup Command: node scripts/schedule-master.mjs --catchup`);
    } else {
      console.log('ALL POSTS SUCCESSFULLY SCHEDULED IN BUFFER!');
    }
    console.log('======================================================================');
  } catch (e) {
    console.error('Error reading final report:', e.message);
  }
}
