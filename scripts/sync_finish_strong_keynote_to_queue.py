# -*- coding: utf-8 -*-
import json
import os

with open('scripts/master-campaign-queue.json', 'r', encoding='utf-8') as f:
    master_queue = json.load(f)

report_file = 'scripts/finish-strong-keynote-scheduled-report.json'
if os.path.exists(report_file):
    with open(report_file, 'r', encoding='utf-8') as f:
        keynote_posts = json.load(f)
else:
    import importlib.util
    spec = importlib.util.spec_from_file_location("mod", "scripts/schedule-finish-strong-keynote.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    keynote_posts = mod.posts_data

queue_map = {p.get('id'): p for p in master_queue if p.get('id')}

added = 0
updated = 0
for kp in keynote_posts:
    kid = f"fs-keynote-{kp['id']:02d}"
    pid = kp.get('postId', '')
    status = kp.get('status', 'scheduled' if pid else 'staged')
    if kid in queue_map:
        queue_map[kid]['postId'] = pid
        queue_map[kid]['bufferPostId'] = pid
        queue_map[kid]['status'] = status
        queue_map[kid]['dueAt'] = kp['dueAt']
        queue_map[kid]['slot'] = kp['slot']
        queue_map[kid]['assetFile'] = kp['assetFile']
        queue_map[kid]['assetUrl'] = kp['assetUrl']
        queue_map[kid]['cta'] = kp.get('cta', '')
        updated += 1
    else:
        entry = {
            'campaign': 'finish-strong-keynote',
            'id': kid,
            'type': kp.get('type', 'image'),
            'dueAt': kp['dueAt'],
            'slot': kp['slot'],
            'postId': pid,
            'bufferPostId': pid,
            'status': status,
            'assetFile': kp['assetFile'],
            'assetUrl': kp['assetUrl'],
            'cta': kp.get('cta', '')
        }
        master_queue.append(entry)
        queue_map[kid] = entry
        added += 1

print(f"Finish Strong Keynote sync: {updated} updated, {added} added. Total items in master queue: {len(master_queue)}")

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
