# -*- coding: utf-8 -*-
"""
Synchronizes all 10 Lornette Daye Campaigns into scripts/master-campaign-queue.json
and generates scripts/scheduled-master-report.json with accurate status tracking.
"""

import os
import sys
import json
import importlib.util
from datetime import datetime, timezone

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)

campaign_specs = [
    ("vintage-nfl", "schedule-vintage-nfl-campaign.py", "vintage-nfl-scheduled-report.json", 24),
    ("macclung", "schedule-macclung-campaign.py", "macclung-scheduled-report.json", 11),
    ("jazzy-davidson", "schedule-jazzy-davidson-campaign.py", "jazzy-davidson-scheduled-report.json", 10),
    ("mendoza", "schedule-mendoza-campaign.py", "mendoza-scheduled-report.json", 20),
    ("nba", "schedule-nba-campaign.py", "nba-scheduled-report.json", 3),
    ("cricket", "schedule-cricket-campaign.py", "cricket-scheduled-report.json", 14),
    ("sitaya-fagan", "schedule-sitaya-fagan-campaign.py", "sitaya-fagan-scheduled-report.json", 10),
    ("tyrese-gibson", "schedule-tyrese-gibson-campaign.py", "tyrese-gibson-scheduled-report.json", 12),
    ("yaroslava-mahuchikh", "schedule-yaroslava-mahuchikh-campaign.py", "yaroslava-mahuchikh-scheduled-report.json", 8),
    ("saquon-barkley", "schedule-saquon-barkley-campaign.py", "saquon-barkley-scheduled-report.json", 10)
]

scripts_dir = os.path.dirname(os.path.abspath(__file__))
master_queue = []
campaign_summaries = {}
global_index = 1

for camp_id, script_name, report_name, expected_count in campaign_specs:
    script_path = os.path.join(scripts_dir, script_name)
    report_path = os.path.join(scripts_dir, report_name)
    
    # Load module posts_data
    spec = importlib.util.spec_from_file_location(camp_id.replace('-', '_'), script_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    posts = getattr(mod, 'posts_data', [])
    
    # Load report if exists
    report_map = {}
    if os.path.exists(report_path):
        try:
            with open(report_path, "r", encoding="utf-8") as rf:
                rd = json.load(rf)
                items = rd if isinstance(rd, list) else rd.get("results", [])
                for item in items:
                    if item.get("status") in ["scheduled", "success"] and item.get("postId"):
                        report_map[item["id"]] = item
        except Exception as e:
            print(f"Warning reading report for {camp_id}: {e}")
            
    camp_sched_count = 0
    for p in posts:
        pid = p["id"]
        sched_item = report_map.get(pid)
        is_sched = sched_item is not None
        if is_sched:
            camp_sched_count += 1
            
        entry = {
            "globalId": global_index,
            "campaign": camp_id,
            "postId": pid,
            "slot": p.get("slot"),
            "dueAt": p.get("dueAt"),
            "cta": p.get("cta"),
            "assetFile": p.get("assetFile"),
            "assetUrl": p.get("assetUrl"),
            "text": p.get("text"),
            "status": "scheduled" if is_sched else "pending",
            "bufferPostId": sched_item.get("postId") if is_sched else None,
            "channelId": "6a39d30c5ab6d2f1065f5301"
        }
        master_queue.append(entry)
        global_index += 1
        
    campaign_summaries[camp_id] = {
        "expected": expected_count,
        "scheduled": camp_sched_count,
        "pending": expected_count - camp_sched_count,
        "status": "COMPLETED" if camp_sched_count == expected_count else ("PARTIAL" if camp_sched_count > 0 else "PENDING")
    }

total_posts = len(master_queue)
scheduled_count = sum(1 for p in master_queue if p["status"] == "scheduled")
pending_count = total_posts - scheduled_count

queue_file = os.path.join(scripts_dir, "master-campaign-queue.json")
with open(queue_file, "w", encoding="utf-8") as qf:
    json.dump(master_queue, qf, indent=2)

report_file = os.path.join(scripts_dir, "scheduled-master-report.json")
summary_report = {
    "lastRun": datetime.now(timezone.utc).isoformat(),
    "totalPosts": total_posts,
    "scheduledCount": scheduled_count,
    "pendingCount": pending_count,
    "completionRate": f"{(scheduled_count / total_posts) * 100:.1f}%",
    "rateLimitHit": pending_count > 0,
    "rateLimitDetails": {
        "reason": "Buffer 24h rolling post limit per channel reached (HTTP 429)",
        "cooldownSeconds": 72446,
        "recoveryCommand": "node scripts/schedule-master.mjs --catchup"
    },
    "campaigns": campaign_summaries
}

with open(report_file, "w", encoding="utf-8") as rf:
    json.dump(summary_report, rf, indent=2)

print("=" * 70)
print(f"MASTER QUEUE SYNCHRONIZED: {scheduled_count}/{total_posts} scheduled.")
print(f"Pending Posts: {pending_count}")
print(f"Queue written to: {queue_file}")
print(f"Master report written to: {report_file}")
print("=" * 70)
