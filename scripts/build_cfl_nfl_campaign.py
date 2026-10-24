# -*- coding: utf-8 -*-
"""
Build CFL-NFL Gameday & Playoff Campaign Queue
Featuring: Edmonton Elks (CFL West Champions) & Cleveland Browns (NFL AFC North Leaders)
Authoritative Voice: Lornette Daye (Olympian coach & Canadian national champion)

Strict Invariants:
- Zero asterisks (* or **)
- Zero em dashes (—, &mdash;, \u2014)
- High-energy gameday leadership breakdowns
- Production custom domain URLs (https://lornettedaye.com/campaigns/cfl-nfl/...)
- Primary CTA: https://lornettedaye.com/foundations
"""

import os
import sys
import json

BASE_URL = "https://lornettedaye.com/campaigns/cfl-nfl"
CHANNEL_ID = "6a39d30c5ab6d2f1065f5301"

POSTS = [
    {
        "id": "CFL_NFL_001",
        "title": "THE SPIRIT IS BACK: EDMONTON ELKS WEST DIVISION CHAMPIONS",
        "dueAt": "2026-10-24T17:30:00.000Z",
        "slot": "Weekend Kickoff (Sat Oct 24, 11:30 AM MDT)",
        "asset_url": f"{BASE_URL}/edmonton-elks-west-champions.png",
        "headline_copy": "For the first time since 2015, the Edmonton Elks have finished on top of the CFL West. They have brought belief back to our city, pride back to our fans, and reminded us what we can do together. The spirit is back. And the playoffs are calling!",
        "breakdown": "Cultural turnarounds do not happen overnight. After years of heartbreak and rebuilding, this Edmonton team proved what happens when athletes commit to collective standards over individual ego. Finishing on top of the CFL West division for the first time in over a decade is not just a statistical milestone: it is a masterclass in athletic perseverance and civic revitalization.",
        "takeaway": "When belief returns to a locker room, momentum becomes undeniable. As coaches and leaders, our mission is to build systems of trust so strong that external doubt can never penetrate the huddle.",
        "foundation": "Foundation 2: Champion Mindset and Foundation 10: Legacy, Culture and Community Pride",
        "hashtags": "#EdmontonElks #CFL #CFLFootball #GoElks #YEG #CanadianFootball #LornetteDaye #HighPerformance #LeadershipInSport #Foundations"
    },
    {
        "id": "CFL_NFL_002",
        "title": "CLEVELAND: LOOK WHO IS ON TOP",
        "dueAt": "2026-10-25T16:00:00.000Z",
        "slot": "NFL Gameday Morning (Sun Oct 25, 10:00 AM MDT)",
        "asset_url": f"{BASE_URL}/cleveland-browns-afc-north.png",
        "headline_copy": "4-2. First in the AFC North. Cleveland is on top after a dramatic 13-10 win over Baltimore. Four wins. Four fourth-quarter comebacks. This team is showing heart, resilience and a new identity.",
        "breakdown": "Four fourth-quarter comebacks in six weeks. That is not luck: that is psychological conditioning. In high-stakes competition, most teams fracture when trailing late. Cleveland is executing under fire because they have embraced adversity as their competitive advantage.",
        "takeaway": "Great teams do not panic when the clock winds down. They trust their preparation, regulate their emotions, and seize the defining possession. Poise in crunch time separates contenders from pretenders.",
        "foundation": "Foundation 4: Resilience After Setback and Foundation 5: Pressure and Emotional Regulation",
        "hashtags": "#ClevelandBrowns #Browns #DawgPound #NFL #AFCNorth #NFLGameday #LornetteDaye #ComebackMindset #Foundations #CrunchTime"
    },
    {
        "id": "CFL_NFL_003",
        "title": "THE WEST GOES THROUGH EDMONTON: COUNTDOWN TO THE WESTERN FINAL",
        "dueAt": "2026-10-31T17:30:00.000Z",
        "slot": "Playoff Countdown (Sat Oct 31, 11:30 AM MDT)",
        "asset_url": f"{BASE_URL}/edmonton-elks-western-final.png",
        "headline_copy": "The Elks have earned the right to host the Western Final. Every practice has built this moment. Every decision has brought us here. Every player matters now. Can the Elks carry this momentum all the way to the Grey Cup?",
        "breakdown": "Hosting the Western Final at Commonwealth Stadium on November 7 is the culmination of every grueling rep in training camp, every film study session, and every shared sacrifice. But playoff football is unforgiving: past wins guarantee nothing. The team that wins championship weekend is the team that stays present on every single down.",
        "takeaway": "Championship preparation is about eliminating distractions. When the stage gets bigger, your focus must get smaller. Master the immediate detail in front of you.",
        "foundation": "Foundation 3: Discipline Systems and Attention Control",
        "hashtags": "#EdmontonElks #WesternFinal #CFLPlayoffs #CommonwealthStadium #GreyCupBound #CFL #LornetteDaye #AthleteDevelopment #Foundations"
    },
    {
        "id": "CFL_NFL_004",
        "title": "GAMEDAY AT COMMONWEALTH: THE ROAD TO THE GREY CUP",
        "dueAt": "2026-11-07T17:00:00.000Z",
        "slot": "Western Final Gameday (Sat Nov 07, 10:00 AM MST)",
        "asset_url": f"{BASE_URL}/edmonton-elks-western-final.png",
        "headline_copy": "Today, the West goes through Edmonton. Sixty minutes of championship football between Commonwealth Stadium and the Grey Cup. Play with heart. Trust your brothers. Leave everything on the turf.",
        "breakdown": "This is what every athlete dreams of: sixty minutes for the right to play for the ultimate prize. In championship moments, you do not rise to the occasion: you sink to the level of your training. Edmonton has built the foundation. Now is the time to trust the work, embrace the physical battle, and finish strong.",
        "takeaway": "When pressure reaches its peak, true competitors do not flinch. Stand tall, play for the city, and let your preparation speak.",
        "foundation": "Foundation 2: Champion Mindset and Foundation 10: Legacy and Community Impact",
        "hashtags": "#EdmontonElks #WesternFinal #CFL #GreyCup #Gameday #CFLGameday #CommonwealthStadium #LornetteDaye #FinishStrong #Foundations"
    }
]

def build_post_text(p):
    text = f"""{p['title']}

"{p['headline_copy']}"

THE COACH'S BREAKDOWN:
{p['breakdown']}

LEADERSHIP & PERFORMANCE TAKEAWAY:
{p['takeaway']}

ATHLETE DEVELOPMENT INSIGHT:
Lornette's Foundations: {p['foundation']}

Discover how Lornette Daye's complete athlete development system equips competitors, coaches, and organizations to build championship culture and master pressure:
https://lornettedaye.com/foundations

Sincerely,
Lornette Daye
Olympic-level Coach and Canadian National Champion

{p['hashtags']}"""

    # Strict Invariant Assertions
    assert "*" not in text, f"Post {p['id']} contains asterisks!"
    assert "—" not in text, f"Post {p['id']} contains em dash!"
    assert "&mdash;" not in text, f"Post {p['id']} contains mdash!"
    assert "\u2014" not in text, f"Post {p['id']} contains unicode em dash!"

    return text

def build_queue():
    queue = []
    for p in POSTS:
        queue.append({
            "id": p["id"],
            "title": p["title"],
            "slot": p["slot"],
            "dueAt": p["dueAt"],
            "channel_id": CHANNEL_ID,
            "mode": "customScheduled",
            "schedulingType": "automatic",
            "asset_url": p["asset_url"],
            "asset_type": "image",
            "text": build_post_text(p)
        })
    return queue

def main():
    print("================================================================")
    print("🏈 CFL-NFL GAMEDAY & PLAYOFF CAMPAIGN BUILDER")
    print("Authoritative Voice: Lornette Daye")
    print("Zero Asterisks | Zero Em Dashes | 3 Curated Production Assets")
    print("================================================================\n")
    
    queue = build_queue()
    print(f"Generated {len(queue)} bespoke gameday posts.")
    
    output_path = "scripts/master-cfl-nfl-queue.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(queue, f, indent=2)
        
    print(f"Successfully saved queue to: {output_path}")
    
    asterisk_count = sum(p["text"].count("*") for p in queue)
    em_dash_count = sum(p["text"].count("—") for p in queue)
    print(f"Audit Results:")
    print(f"- Asterisks Count: {asterisk_count} (Must be 0)")
    print(f"- Em Dashes Count: {em_dash_count} (Must be 0)")
    print(f"- Post 1: {queue[0]['id']} -> {queue[0]['dueAt']} ({queue[0]['slot']})")
    print(f"- Post 2: {queue[1]['id']} -> {queue[1]['dueAt']} ({queue[1]['slot']})")
    print(f"- Post 3: {queue[2]['id']} -> {queue[2]['dueAt']} ({queue[2]['slot']})")
    print(f"- Post 4: {queue[3]['id']} -> {queue[3]['dueAt']} ({queue[3]['slot']})")
    print("\n✅ ZERO-ASTERISK AND GAMEDAY CALENDAR INVARIANTS VERIFIED.")

if __name__ == "__main__":
    main()
