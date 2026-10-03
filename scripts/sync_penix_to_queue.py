# -*- coding: utf-8 -*-
import json
import os

with open('scripts/master-campaign-queue.json', 'r', encoding='utf-8') as f:
    master_queue = json.load(f)

report_file = 'scripts/penix-scheduled-report.json'
if os.path.exists(report_file):
    with open(report_file, 'r', encoding='utf-8') as f:
        penix_posts = json.load(f)
else:
    import importlib.util
    spec = importlib.util.spec_from_file_location("mod", "scripts/schedule-penix-campaign.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    penix_posts = mod.posts_data

queue_map = {p.get('id'): p for p in master_queue if p.get('id')}

added = 0
updated = 0
for pp in penix_posts:
    pid = f"penix-{pp['id']:02d}"
    b_pid = pp.get('postId', '')
    status = pp.get('status', 'scheduled' if b_pid else 'staged')
    if pid in queue_map:
        queue_map[pid]['postId'] = b_pid
        queue_map[pid]['bufferPostId'] = b_pid
        queue_map[pid]['status'] = status
        queue_map[pid]['dueAt'] = pp['dueAt']
        queue_map[pid]['slot'] = pp['slot']
        queue_map[pid]['assetFile'] = pp['assetFile']
        queue_map[pid]['assetUrl'] = pp['assetUrl']
        queue_map[pid]['cta'] = pp.get('cta', '')
        updated += 1
    else:
        entry = {
            'campaign': 'penix',
            'id': pid,
            'type': pp.get('type', 'image'),
            'dueAt': pp['dueAt'],
            'slot': pp['slot'],
            'postId': b_pid,
            'bufferPostId': b_pid,
            'status': status,
            'assetFile': pp['assetFile'],
            'assetUrl': pp['assetUrl'],
            'cta': pp.get('cta', '')
        }
        master_queue.append(entry)
        queue_map[pid] = entry
        added += 1

print(f"Michael Penix Jr. sync: {updated} updated, {added} added. Total items in master queue: {len(master_queue)}")

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
