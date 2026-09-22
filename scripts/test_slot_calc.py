# -*- coding: utf-8 -*-
import os
import re
import json
from datetime import datetime, timedelta

# Load existing booked slots
existing_due = set()
for rpt in ['scripts/rescheduled-master-report.json', 'scripts/henry-scheduled-report.json']:
    if os.path.exists(rpt):
        with open(rpt, 'r', encoding='utf-8') as f:
            for item in json.load(f):
                if item.get('dueAt'):
                    existing_due.add(item['dueAt'])

print(f"Loaded {len(existing_due)} existing booked slots.")

candidate_times = ['14:30:00.000Z', '17:00:00.000Z', '19:15:00.000Z', '21:45:00.000Z', '23:45:00.000Z']
curr = datetime(2026, 10, 6)
all_slots = []
while len(all_slots) < 82:
    day_str = curr.strftime('%Y-%m-%d')
    for t in candidate_times:
        slot_iso = f'{day_str}T{t}'
        if slot_iso not in existing_due:
            all_slots.append(slot_iso)
            if len(all_slots) == 82:
                break
    curr += timedelta(days=1)

print(f"Generated 82 slots: from {all_slots[0]} to {all_slots[-1]}")

def get_slot_name(iso_str):
    dt = datetime.strptime(iso_str, '%Y-%m-%dT%H:%M:%S.%fZ')
    # MDT is UTC-6
    mdt_dt = dt - timedelta(hours=6)
    day_name = mdt_dt.strftime('%A')
    time_str = mdt_dt.strftime('%I:%M %p')
    return f"{day_name} ({time_str} MDT)"

print("Sample slots:")
for i in [0, 23, 24, 34, 35, 44, 45, 64, 65, 67, 68, 81]:
    print(f"Slot #{i+1}: {all_slots[i]} -> {get_slot_name(all_slots[i])}")
