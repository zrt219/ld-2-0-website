# -*- coding: utf-8 -*-
import json

posts = [
    {"id": 1, "postId": "6ab201236ed20e9354f72532", "dueAt": "2026-10-24T19:15:00.000Z", "slot": "Saturday (01:15 PM MDT)", "status": "scheduled", "assetUrl": "https://lornettedaye.com/campaigns/tyrese-gibson/tyrese-gibson-01.png"},
    {"id": 2, "postId": "6ab201259609314f621766f7", "dueAt": "2026-10-24T21:45:00.000Z", "slot": "Saturday (03:45 PM MDT)", "status": "scheduled", "assetUrl": "https://lornettedaye.com/campaigns/tyrese-gibson/tyrese-gibson-02.png"},
    {"id": 3, "postId": "6ab20127e2882add8db28d3b", "dueAt": "2026-10-24T23:45:00.000Z", "slot": "Saturday (05:45 PM MDT)", "status": "scheduled", "assetUrl": "https://lornettedaye.com/campaigns/tyrese-gibson/tyrese-gibson-03.png"},
    {"id": 4, "postId": "6ab20128ffe5c8afb12a7e68", "dueAt": "2026-10-25T14:30:00.000Z", "slot": "Sunday (08:30 AM MDT)", "status": "scheduled", "assetUrl": "https://lornettedaye.com/campaigns/tyrese-gibson/tyrese-gibson-04.png"},
    {"id": 5, "postId": "6ab2012affe5c8afb12a7eb9", "dueAt": "2026-10-25T17:00:00.000Z", "slot": "Sunday (11:00 AM MDT)", "status": "scheduled", "assetUrl": "https://lornettedaye.com/campaigns/tyrese-gibson/tyrese-gibson-05.png"},
    {"id": 6, "postId": "6ab2012b377d336018c7fd2d", "dueAt": "2026-10-25T19:15:00.000Z", "slot": "Sunday (01:15 PM MDT)", "status": "scheduled", "assetUrl": "https://lornettedaye.com/campaigns/tyrese-gibson/tyrese-gibson-06.png"},
    {"id": 7, "postId": "6ab2012d377d336018c7fd76", "dueAt": "2026-10-25T21:45:00.000Z", "slot": "Sunday (03:45 PM MDT)", "status": "scheduled", "assetUrl": "https://lornettedaye.com/campaigns/tyrese-gibson/tyrese-gibson-07.png"},
    {"id": 8, "postId": "6ab2012f74424003bca80cbc", "dueAt": "2026-10-25T23:45:00.000Z", "slot": "Sunday (05:45 PM MDT)", "status": "scheduled", "assetUrl": "https://lornettedaye.com/campaigns/tyrese-gibson/tyrese-gibson-08.png"},
    {"id": 9, "postId": "6ab20131ffe5c8afb12a7f77", "dueAt": "2026-10-26T14:30:00.000Z", "slot": "Monday (08:30 AM MDT)", "status": "scheduled", "assetUrl": "https://lornettedaye.com/campaigns/tyrese-gibson/tyrese-gibson-09.png"},
    {"id": 10, "postId": "6ab20132e2882add8db28e35", "dueAt": "2026-10-26T17:00:00.000Z", "slot": "Monday (11:00 AM MDT)", "status": "scheduled", "assetUrl": "https://lornettedaye.com/campaigns/tyrese-gibson/tyrese-gibson-10.png"}
]

with open('scripts/tyrese-gibson-scheduled-report.json', 'w', encoding='utf-8') as f:
    json.dump(posts, f, indent=2)

print('Successfully persisted scripts/tyrese-gibson-scheduled-report.json (10 posts).')
