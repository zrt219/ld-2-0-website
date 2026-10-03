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

existing_ids = {p.get('postId') or p.get('id') for p in master_queue}

added = 0
for kp in keynote_posts:
    kid = f"fs-keynote-{kp['id']:02d}"
    if kid not in existing_ids:
        master_queue.append({
            'campaign': 'finish-strong-keynote',
            'id': kid,
            'type': kp.get('type', 'image'),
            'dueAt': kp['dueAt'],
            'slot': kp['slot'],
            'postId': kp.get('postId', ''),
            'status': kp.get('status', 'staged'),
            'assetFile': kp['assetFile'],
            'assetUrl': kp['assetUrl'],
            'cta': kp.get('cta', '')
        })
        existing_ids.add(kid)
        added += 1

print(f"Added {added} Finish Strong Keynote posts to master queue. Total items in master queue: {len(master_queue)}")

with open('scripts/master-campaign-queue.json', 'w', encoding='utf-8') as f:
    json.dump(master_queue, f, indent=2, ensure_ascii=False)

with open('scripts/scheduled-master-report.json', 'w', encoding='utf-8') as f:
    json.dump({
        'totalScheduled': len(master_queue),
        'pending': sum(1 for p in master_queue if p.get('status') in ['staged', 'pending', 'failed']),
        'posts': master_queue
    }, f, indent=2, ensure_ascii=False)
