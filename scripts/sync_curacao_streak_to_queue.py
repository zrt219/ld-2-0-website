# -*- coding: utf-8 -*-
import json
import os

with open('scripts/master-campaign-queue.json', 'r', encoding='utf-8') as f:
    master_queue = json.load(f)

report_file = 'scripts/curacao-streak-scheduled-report.json'
if os.path.exists(report_file):
    with open(report_file, 'r', encoding='utf-8') as f:
        streak_posts = json.load(f)
else:
    import importlib.util
    spec = importlib.util.spec_from_file_location("mod", "scripts/schedule-curacao-streak.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    streak_posts = mod.posts_data

queue_map = {p.get('id'): p for p in master_queue if p.get('id')}

added = 0
updated = 0
for cp in streak_posts:
    cid = f"curacao-strk-{cp['id']:02d}"
    pid = cp.get('postId', '')
    status = cp.get('status', 'scheduled' if pid else 'staged')
    if cid in queue_map:
        queue_map[cid]['postId'] = pid
        queue_map[cid]['bufferPostId'] = pid
        queue_map[cid]['status'] = status
        queue_map[cid]['dueAt'] = cp['dueAt']
        queue_map[cid]['slot'] = cp['slot']
        queue_map[cid]['assetFile'] = cp['assetFile']
        queue_map[cid]['assetUrl'] = cp['assetUrl']
        queue_map[cid]['cta'] = cp.get('cta', '')
        updated += 1
    else:
        entry = {
            'campaign': 'curacao-streak',
            'id': cid,
            'type': cp.get('type', 'image'),
            'dueAt': cp['dueAt'],
            'slot': cp['slot'],
            'postId': pid,
            'bufferPostId': pid,
            'status': status,
            'assetFile': cp['assetFile'],
            'assetUrl': cp['assetUrl'],
            'cta': cp.get('cta', '')
        }
        master_queue.append(entry)
        queue_map[cid] = entry
        added += 1

print(f"Curaçao streak sync: {updated} updated, {added} added. Total items in master queue: {len(master_queue)}")

total_scheduled = sum(1 for p in master_queue if p.get('status') in ['scheduled', 'success'] and (p.get('postId') or p.get('bufferPostId')))
pending = len(master_queue) - total_scheduled

with open('scripts/master-campaign-queue.json', 'w', encoding='utf-8') as f:
    json.dump(master_queue, f, indent=2, ensure_ascii=False)

with open('scripts/scheduled-master-report.json', 'w', encoding='utf-8') as f:
    json.dump({
        'totalScheduled': total_scheduled,
        'pending': pending,
        'posts': master_queue
    }, f, indent=2, ensure_ascii=False)
