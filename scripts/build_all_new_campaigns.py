# -*- coding: utf-8 -*-
"""
Builder and generator for the 6 new campaigns:
1. vintage NFL (24 posts)
2. macclung (11 posts)
3. jazzy davidson (10 posts)
4. mendoza (20 posts)
5. nba (3 posts)
6. cricket (14 posts)
Total: 82 posts

Strict invariants enforced:
- Zero em dashes (assert no '\u2014' or '—' or '&mdash;')
- Canonical Lornette Daye voice and book catalog
- Production custom domain https://lornettedaye.com/campaigns/...
"""

import os
import json

# Define slot assignment generator
candidate_times = ['14:30:00.000Z', '17:00:00.000Z', '19:15:00.000Z', '21:45:00.000Z', '23:45:00.000Z']

# Load existing booked slots from both reports
existing_due = set()
for rpt in ['scripts/rescheduled-master-report.json', 'scripts/henry-scheduled-report.json']:
    if os.path.exists(rpt):
        with open(rpt, 'r', encoding='utf-8') as f:
            for item in json.load(f):
                if item.get('dueAt'):
                    existing_due.add(item['dueAt'])

print(f"Loaded {len(existing_due)} existing booked slots.")
