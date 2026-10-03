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

existing_ids = {p.get('postId') or p.get('id') for p in master_queue}

added = 0
for pp in penix_posts:
    pid = f"penix-{pp['id']:02d}"
    if pid not in existing_ids:
        master_queue.append({
            'campaign': 'penix',
            'id': pid,
            'type': pp.get('type', 'image'),
            'dueAt': pp['dueAt'],
            'slot': pp['slot'],
            'postId': pp.get('postId', ''),
            'status': pp.get('status', 'staged'),
            'assetFile': pp['assetFile'],
            'assetUrl': pp['assetUrl'],
            'cta': pp.get('cta', '')
        })
        existing_ids.add(pid)
        added += 1

print(f"Added {added} Michael Penix Jr. posts to master queue. Total items in master queue: {len(master_queue)}")

with open('scripts/master-campaign-queue.json', 'w', encoding='utf-8') as f:
    json.dump(master_queue, f, indent=2, ensure_ascii=False)

with open('scripts/scheduled-master-report.json', 'w', encoding='utf-8') as f:
    json.dump({
        'totalScheduled': len(master_queue),
        'pending': sum(1 for p in master_queue if p.get('status') in ['staged', 'pending', 'failed']),
        'posts': master_queue
    }, f, indent=2, ensure_ascii=False)
