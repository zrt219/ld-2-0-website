# -*- coding: utf-8 -*-
"""
Master Sequential Orchestrator for all 10 Lornette Daye LinkedIn Campaigns:
1. Vintage NFL (24 posts)
2. Mac McClung (11 posts)
3. Jazzy Davidson (10 posts)
4. Mendoza (20 posts)
5. NBA (3 posts)
6. Cricket (14 posts)
7. Sitaya Fagan (10 posts)
8. Tyrese Gibson (12 posts)
9. Yaroslava Mahuchikh (8 posts)
10. Saquon Barkley (10 posts)
Total: 122 Posts
"""

import os
import sys
import subprocess
import time
import json

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)

scripts = [
    ("Campaign 1: Vintage NFL", "schedule-vintage-nfl-campaign.py", "vintage-nfl-scheduled-report.json", 24),
    ("Campaign 2: Mac McClung", "schedule-macclung-campaign.py", "macclung-scheduled-report.json", 11),
    ("Campaign 3: Jazzy Davidson", "schedule-jazzy-davidson-campaign.py", "jazzy-davidson-scheduled-report.json", 10),
    ("Campaign 4: Mendoza", "schedule-mendoza-campaign.py", "mendoza-scheduled-report.json", 20),
    ("Campaign 5: NBA", "schedule-nba-campaign.py", "nba-scheduled-report.json", 3),
    ("Campaign 6: Cricket", "schedule-cricket-campaign.py", "cricket-scheduled-report.json", 14),
    ("Campaign 7: Sitaya Fagan", "schedule-sitaya-fagan-campaign.py", "sitaya-fagan-scheduled-report.json", 10),
    ("Campaign 8: Tyrese Gibson", "schedule-tyrese-gibson-campaign.py", "tyrese-gibson-scheduled-report.json", 12),
    ("Campaign 9: Yaroslava Mahuchikh", "schedule-yaroslava-mahuchikh-campaign.py", "yaroslava-mahuchikh-scheduled-report.json", 8),
    ("Campaign 10: Saquon Barkley", "schedule-saquon-barkley-campaign.py", "saquon-barkley-scheduled-report.json", 10)
]

print("=" * 80)
print("STARTING MASTER EXECUTION OF ALL 10 CAMPAIGNS (122 POSTS)")
print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 80)

total_scheduled = 0
total_target = sum(s[3] for s in scripts)

for title, script_file, report_file, count in scripts:
    print(f"\n>>> LAUNCHING {title} ({count} posts)...")
    script_path = os.path.join("scripts", script_file)
    
    # Run the script
    ret = subprocess.run([sys.executable, script_path], capture_output=False)
    
    # Check report
    rpt_path = os.path.join("scripts", report_file)
    if os.path.exists(rpt_path):
        try:
            with open(rpt_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                items = data if isinstance(data, list) else data.get("results", [])
                sched = sum(1 for x in items if x.get("status") in ["scheduled", "success"] and x.get("postId"))
                total_scheduled += sched
                print(f">>> {title} COMPLETE: {sched}/{count} posts scheduled in Buffer.")
        except Exception as e:
            print(f">>> Error reading report {rpt_path}: {e}")
    else:
        print(f">>> Warning: Report {rpt_path} not found.")

    time.sleep(2)

print("\n" + "=" * 80)
print("MASTER EXECUTION COMPLETE!")
print(f"Overall Progress: {total_scheduled}/{total_target} posts scheduled successfully.")
print("=" * 80)
