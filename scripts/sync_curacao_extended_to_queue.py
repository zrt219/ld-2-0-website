# -*- coding: utf-8 -*-
import json

with open('scripts/master-campaign-queue.json', 'r', encoding='utf-8') as f:
    master_queue = json.load(f)

with open('scripts/curacao-extended-scheduled-report.json', 'r', encoding='utf-8') as f:
    curacao_ext_posts = json.load(f)

existing_ids = {p.get('postId') or p.get('bufferPostId') for p in master_queue}

added = 0
for cp in curacao_ext_posts:
    pid = cp.get('postId')
    if pid and pid not in existing_ids:
        master_queue.append({
            'campaign': 'curacao-extended',
            'id': f"curacao-ext-{cp['id']:02d}",
            'type': cp.get('type', 'video'),
            'dueAt': cp['dueAt'],
            'slot': cp['slot'],
            'postId': pid,
            'status': cp['status'],
            'assetFile': cp['assetFile'],
            'assetUrl': cp['assetUrl'],
            'cta': cp.get('cta', '')
        })
        existing_ids.add(pid)
        added += 1

print(f"Added {added} Curaçao extended posts to master queue. Total items: {len(master_queue)}")

with open('scripts/master-campaign-queue.json', 'w', encoding='utf-8') as f:
    json.dump(master_queue, f, indent=2, ensure_ascii=False)

with open('scripts/scheduled-master-report.json', 'w', encoding='utf-8') as f:
    json.dump({
        'totalScheduled': len(master_queue),
        'pending': 0,
        'posts': master_queue
    }, f, indent=2, ensure_ascii=False)
