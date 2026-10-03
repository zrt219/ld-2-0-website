# -*- coding: utf-8 -*-
import json
import os

with open('scripts/master-campaign-queue.json', 'r', encoding='utf-8') as f:
    master_queue = json.load(f)

report_file = 'scripts/oilers-scheduled-report.json'
if os.path.exists(report_file):
    with open(report_file, 'r', encoding='utf-8') as f:
        oilers_posts = json.load(f)
else:
    import importlib.util
    spec = importlib.util.spec_from_file_location("mod", "scripts/schedule-oilers-campaign.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    oilers_posts = mod.posts_data

queue_map = {p.get('id'): p for p in master_queue if p.get('id')}

added = 0
updated = 0
for op in oilers_posts:
    oid = f"oilers-{op['id']:02d}"
    pid = op.get('postId', '')
    status = op.get('status', 'scheduled' if pid else 'staged')
    if oid in queue_map:
        queue_map[oid]['postId'] = pid
        queue_map[oid]['bufferPostId'] = pid
        queue_map[oid]['status'] = status
        queue_map[oid]['dueAt'] = op['dueAt']
        queue_map[oid]['slot'] = op['slot']
        queue_map[oid]['assetFile'] = op['assetFile']
        queue_map[oid]['assetUrl'] = op['assetUrl']
        queue_map[oid]['cta'] = op.get('cta', '')
        updated += 1
    else:
        entry = {
            'campaign': 'oilers',
            'id': oid,
            'type': op.get('type', 'image'),
            'dueAt': op['dueAt'],
            'slot': op['slot'],
            'postId': pid,
            'bufferPostId': pid,
            'status': status,
            'assetFile': op['assetFile'],
            'assetUrl': op['assetUrl'],
            'cta': op.get('cta', '')
        }
        master_queue.append(entry)
        queue_map[oid] = entry
        added += 1

print(f"Edmonton Oilers sync: {updated} updated, {added} added. Total items in master queue: {len(master_queue)}")

with open('scripts/master-campaign-queue.json', 'w', encoding='utf-8') as f:
    json.dump(master_queue, f, indent=2, ensure_ascii=False)

with open('scripts/scheduled-master-report.json', 'w', encoding='utf-8') as f:
    json.dump({
        'totalScheduled': len(master_queue),
        'pending': sum(1 for p in master_queue if p.get('status') in ['staged', 'pending', 'failed']),
        'posts': master_queue
    }, f, indent=2, ensure_ascii=False)
