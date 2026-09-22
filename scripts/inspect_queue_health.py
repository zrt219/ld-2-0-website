import json
from collections import defaultdict

with open('scripts/master-campaign-queue.json', 'r', encoding='utf-8') as f:
    queue = json.load(f)

by_due = defaultdict(list)
camp_ranges = defaultdict(list)
camp_status = defaultdict(lambda: {'scheduled': 0, 'pending': 0, 'failed': 0})

for item in queue:
    by_due[item['dueAt']].append(f"{item['campaign']}#{item['postId']} ({item['status']})")
    camp_ranges[item['campaign']].append(item['dueAt'])
    camp_status[item['campaign']][item['status']] += 1

print("--- CAMPAIGN SUMMARY & DATE RANGES ---")
for camp, dues in camp_ranges.items():
    st = camp_status[camp]
    print(f"{camp:20s}: {len(dues):2d} posts | sched={st['scheduled']:2d}, pend={st['pending']:2d} | {min(dues)} to {max(dues)}")

print("\n--- COLLISIONS (SAME TIMESTAMP FOR MULTIPLE POSTS) ---")
coll_count = 0
for due in sorted(by_due.keys()):
    if len(by_due[due]) > 1:
        coll_count += 1
        print(f"{due}: {by_due[due]}")

print(f"\nTotal collisions: {coll_count}")
