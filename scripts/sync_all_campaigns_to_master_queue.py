# -*- coding: utf-8 -*-
"""
Synchronizes scheduled campaign reports into scripts/master-campaign-queue.json
and performs a comprehensive health audit.
"""
import sys
import os
import json
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)

MASTER_QUEUE_FILE = "scripts/master-campaign-queue.json"

def sync_queue():
    if not os.path.exists(MASTER_QUEUE_FILE):
        print(f"Error: {MASTER_QUEUE_FILE} not found.")
        sys.exit(1)

    with open(MASTER_QUEUE_FILE, "r", encoding="utf-8") as f:
        master_queue = json.load(f)

    print(f"Initial master queue: {len(master_queue)} posts.")

    # Map existing posts by id / postId / timestamp
    existing_post_ids = {p.get("postId") for p in master_queue if p.get("postId")}
    existing_timestamps = {p.get("dueAt") for p in master_queue if p.get("dueAt")}

    reports_to_sync = [
        ("Business Athletes (60 Days)", "scripts/business-athletes-scheduled-report.json", "Business Athletes"),
        ("Own The Next Chapter (60 Days / 180 Posts)", "scripts/own-the-next-chapter-scheduled-report.json", "Own The Next Chapter"),
        ("Thierry Henry (40 Days / 120 Posts)", "scripts/thierry-henry-scheduled-report.json", "Thierry Henry"),
        ("Lewis Hamilton Comeback (5 Posts)", "scripts/lewis-comeback-scheduled-report.json", "Lewis Hamilton Comeback"),
    ]

    total_added = 0

    for rep_name, rep_path, camp_tag in reports_to_sync:
        if not os.path.exists(rep_path):
            print(f"[{rep_name}] Report not found at {rep_path}. Skipping.")
            continue

        with open(rep_path, "r", encoding="utf-8") as f:
            items = json.load(f)

        added_from_rep = 0
        for item in items:
            p_id = item.get("postId")
            due = item.get("dueAt")
            if not p_id:
                continue

            if p_id in existing_post_ids:
                continue

            entry = {
                "campaign": camp_tag,
                "title": item.get("title", f"{camp_tag} #{item.get('id')}"),
                "dueAt": due,
                "scheduledSlot": item.get("slot", ""),
                "mediaAsset": item.get("assetUrl", ""),
                "ctaFocus": item.get("cta", ""),
                "status": item.get("status", "scheduled"),
                "postId": p_id,
                "text": item.get("text", "")
            }
            master_queue.append(entry)
            existing_post_ids.add(p_id)
            added_from_rep += 1
            total_added += 1

        print(f"[{rep_name}] Synchronized {added_from_rep} new posts into master queue.")

    # Sort master queue chronologically
    master_queue.sort(key=lambda x: x.get("dueAt", ""))

    with open(MASTER_QUEUE_FILE, "w", encoding="utf-8") as f:
        json.dump(master_queue, f, indent=2, ensure_ascii=False)

    print(f"\nMaster queue updated: {len(master_queue)} total posts (+{total_added} added).")

    # Invariant and health audit
    print("\n--- MASTER QUEUE HEALTH AUDIT ---")
    timestamps = [p["dueAt"] for p in master_queue if p.get("dueAt")]
    ts_counts = Counter(timestamps)
    collisions = [ts for ts, count in ts_counts.items() if count > 1]

    if collisions:
        print(f"CRITICAL WARNING: Found {len(collisions)} timestamp collisions in master queue!")
        for c in collisions[:10]:
            print(f"  Collision at {c} ({ts_counts[c]} posts)")
    else:
        print("COLLISION AUDIT: EXACTLY 0 TIMESTAMP COLLISIONS ACROSS ENTIRE MASTER QUEUE!")

    em_dash_posts = []
    for idx, p in enumerate(master_queue, 1):
        t = p.get("text", "")
        for dash in ["\u2014", "&mdash;", "—"]:
            if dash in t:
                em_dash_posts.append((idx, p.get("postId"), dash))

    if em_dash_posts:
        print(f"CRITICAL WARNING: Found {len(em_dash_posts)} posts with em dashes!")
    else:
        print("PUNCTUATION AUDIT: EXACTLY 0 EM DASHES ACROSS ENTIRE MASTER QUEUE!")

    print(f"PORTFOLIO HORIZON: From {master_queue[0]['dueAt']} to {master_queue[-1]['dueAt']}")
    print("Health audit complete.\n")

if __name__ == "__main__":
    sync_queue()
