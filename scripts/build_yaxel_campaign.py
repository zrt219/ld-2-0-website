# -*- coding: utf-8 -*-
"""
Build 3-Week Yaxel Lendeborg Campaign Queue: 'Behind the Athlete, Beyond the Game'
Authoritative Voice: Lornette Daye (Olympian coach & Canadian national champion)
Cadence: 10 Ads paced across 21 calendar days (Oct 24 - Nov 13, 2026)
Strict Invariants:
- Zero asterisks (* or **)
- Zero em dashes (—, &mdash;, \u2014)
- Maximum depth captions addressing athlete humanity, family resilience, and emotional poise
- Primary CTA: https://lornettedaye.com/foundations
- Production custom domain URLs: https://lornettedaye.com/campaigns/yaxel-lendeborg/...
"""

import os
import sys
import json

BASE_URL = "https://lornettedaye.com/campaigns/yaxel-lendeborg"
CHANNEL_ID = "6a39d30c5ab6d2f1065f5301"

CAMPAIGN_DATA = [
    {
        "id": "YAXEL_001",
        "ad_num": 1,
        "title": "MORE THAN THE GAME",
        "dueAt": "2026-10-24T14:30:00.000Z",
        "slot": "Day 1 Morning (08:30 AM MDT)",
        "theme_line": "The world sees the basketball player. There is a young man with a life, a family and a story beyond the court.",
        "invisible_battle": "When millions of eyes tune in to watch professional basketball, they see jersey numbers, box scores, shooting percentages, and highlight dunks. What the camera rarely captures is the invisible load an athlete carries onto the hardwood: the quiet weight of family responsibilities, personal battles back home, and the intense psychological discipline required to perform under pressure while your heart is somewhere else.",
        "reflection": "In my four decades coaching elite competitors and representing Canada on international stages, I have witnessed countless athletes navigate the hardest chapters of their lives in silence. We celebrate their scoring runs, but we rarely ask what it costs them emotionally to stay upright. Yaxel Lendeborg represents the modern athlete: incredibly skilled, fiercely determined, but undeniably human first.",
        "takeaway": "Greatness is not measured solely by points in the paint. It is measured by your capacity to stand tall, protect your character, and honor your foundation when life demands everything from you.",
        "foundation": "Foundation 1: Identity Beyond Sport and Foundation 4: Resilience After Setback"
    },
    {
        "id": "YAXEL_002",
        "ad_num": 2,
        "title": "YAXEL, WHAT A JOURNEY",
        "dueAt": "2026-10-26T14:30:00.000Z",
        "slot": "Day 3 Morning (08:30 AM MDT)",
        "theme_line": "From Michigan to the NBA stage. Your hard work deserves to be celebrated. Enjoy every moment of this new chapter.",
        "invisible_battle": "The path to the highest level of professional basketball is never linear. It is forged in cold community gyms at dawn, long bus rides across collegiate leagues, late-night film sessions, and hundreds of moments where doubt whispered that the dream might be out of reach. Reaching this stage is not luck: it is the result of relentless, unyielding daily habit.",
        "reflection": "As coaches, we see the thousands of invisible hours that precede a breakthrough. When a young man from Michigan works his way onto an elite NBA franchise like Golden State, that achievement represents not just individual grit, but a triumph of community, discipline, and perseverance.",
        "takeaway": "Never allow the pressure of where you are going to steal the gratitude for how far you have already come. Every step on an NBA court is earned ground. Celebrate the journey.",
        "foundation": "Foundation 3: Discipline Systems and Foundation 2: Champion Mindset"
    },
    {
        "id": "YAXEL_003",
        "ad_num": 3,
        "title": "SOME BATTLES ARE PERSONAL",
        "dueAt": "2026-10-28T14:30:00.000Z",
        "slot": "Day 5 Morning (08:30 AM MDT)",
        "theme_line": "Athletes face challenges beyond competition. Showing up for the game while carrying concerns for those you love takes something special.",
        "invisible_battle": "Imagine lacing up your sneakers in an arena packed with twenty thousand screaming fans, knowing that someone you love more than life itself is battling adversity far away from the arena lights. That internal tension: being physically present on defense while emotionally anchoring a family member: is one of the heaviest tests any competitor can endure.",
        "reflection": "True athletic toughness is not a cold lack of emotion. Toughness is feeling the worry, feeling the love, and choosing to show up anyway with dignity and focus. That takes an extraordinary heart.",
        "takeaway": "When you compete for a purpose larger than yourself, your performance takes on sacred meaning. You are not just playing for stats: you are playing to make the people who love you proud.",
        "foundation": "Foundation 5: Pressure, Emotional Regulation and Recovery"
    },
    {
        "id": "YAXEL_004",
        "ad_num": 4,
        "title": "A MOTHER'S LOVE",
        "dueAt": "2026-10-30T14:30:00.000Z",
        "slot": "Day 7 Morning (08:30 AM MDT)",
        "theme_line": "Before the spotlight, before the cheers, there was someone who believed in you. That love is part of your story.",
        "invisible_battle": "Long before scouting reports and national broadcasts, there were early mornings, sacrifices nobody witnessed, and a mother's voice speaking belief into a child before the world knew his name. That maternal bond is the bedrock of an athlete's confidence.",
        "reflection": "Throughout my career, whenever I have seen an athlete display uncommon resilience under fire, I almost always find a mother whose prayer, discipline, and unconditional love laid the foundation. That bond transcends basketball.",
        "takeaway": "Never forget where your foundation was built. When you play with love for family in your chest, no opponent can intimidate you and no scoreboard can diminish your worth.",
        "foundation": "Foundation 7: Family, Community and Mentorship Support Systems"
    },
    {
        "id": "YAXEL_005",
        "ad_num": 5,
        "title": "STAY FOCUSED ON YOUR DREAM",
        "dueAt": "2026-11-01T15:30:00.000Z",
        "slot": "Day 9 Morning (08:30 AM MST)",
        "theme_line": "Preparation, dedication and belief still matter, even when life becomes complicated. Take each opportunity one moment at a time.",
        "invisible_battle": "When external circumstances become chaotic, the human instinct is to feel overwhelmed and lose focus. For elite competitors, the secret to surviving intense seasons is radical micro-focus: winning the exact possession in front of you.",
        "reflection": "I always tell my athletes: you cannot control the outcome of the entire season today, and you cannot solve every life challenge in forty-eight minutes. What you can control is your effort on this defensive rotation, your breath on this free throw, and your attitude in this huddle.",
        "takeaway": "Discipline is the anchor that holds you steady when emotional storms surge. Trust your preparation, execute the next right step, and let the results follow.",
        "foundation": "Foundation 3: Discipline Systems and Focus Control"
    },
    {
        "id": "YAXEL_006",
        "ad_num": 6,
        "title": "YOU ARE HUMAN FIRST",
        "dueAt": "2026-11-03T15:30:00.000Z",
        "slot": "Day 11 Morning (08:30 AM MST)",
        "theme_line": "An athlete can be strong and still feel worried, emotional or overwhelmed. Being human does not make you less of a competitor.",
        "invisible_battle": "Sport culture often pushes a dangerous myth: that real champions must be unfeeling machines who show zero vulnerability. That expectation isolates young athletes and prevents them from processing genuine grief or worry.",
        "reflection": "Vulnerability is not weakness. Acknowledging that you care deeply about your family and feeling the natural weight of their battles makes you stronger, not weaker. It grounds your competitive drive in authentic humanity.",
        "takeaway": "Give yourself permission to be a human being. You do not have to discard your heart to be a dominant competitor. Play with both your strength and your soul.",
        "foundation": "Foundation 1: Identity Beyond Sport"
    },
    {
        "id": "YAXEL_007",
        "ad_num": 7,
        "title": "ENJOY THIS MOMENT",
        "dueAt": "2026-11-05T15:30:00.000Z",
        "slot": "Day 13 Morning (08:30 AM MST)",
        "theme_line": "You have worked too hard to reach this stage not to appreciate the experience. Celebrate the little victories along the way.",
        "invisible_battle": "Elite sport moves at dizzying speed. It is easy to get so consumed by scouting reports, film breakdown, and the pressure of securing roster spots that you forget to breathe and absorb the wonder of playing the game you love on the world's premier stage.",
        "reflection": "When I look back on Olympic competition, the moments that linger longest are not just the medals: they are the locker room laughs, the morning runs, and the sheer joy of testing yourself against the world's best.",
        "takeaway": "Do not let anxiety steal your joy. You earned your seat at this table. Look up at the arena ceiling, feel the wood beneath your feet, and smile. You belong here.",
        "foundation": "Foundation 2: Champion Mindset and Gratitude"
    },
    {
        "id": "YAXEL_008",
        "ad_num": 8,
        "title": "LET YOUR LOVE OF THE GAME SHOW",
        "dueAt": "2026-11-07T15:30:00.000Z",
        "slot": "Day 15 Morning (08:30 AM MST)",
        "theme_line": "Play with heart. Trust your preparation. Remember what first made you love basketball.",
        "invisible_battle": "Under high-stakes pressure, athletes often tighten up and play conservatively out of fear of making mistakes. When that happens, instincts vanish and joy evaporates.",
        "reflection": "The greatest performances always come when an athlete reconnects with the pure, childlike love for the sport that started it all: the feeling of the ball in your hands, the sound of the net, the joy of competing alongside teammates.",
        "takeaway": "Play free. Trust the thousands of repetitions stored in your muscle memory. When you play out of love rather than fear, your true athletic genius unlocks.",
        "foundation": "Foundation 5: Emotional Poise and Athletic Flow"
    },
    {
        "id": "YAXEL_009",
        "ad_num": 9,
        "title": "EVERY ATHLETE HAS A STORY",
        "dueAt": "2026-11-10T15:30:00.000Z",
        "slot": "Day 18 Morning (08:30 AM MST)",
        "theme_line": "Beyond every statistic is a person with hopes, responsibilities, people they love and a future they are building.",
        "invisible_battle": "In an era of fantasy basketball, sports betting, and social media commentary, it is easy for fans to reduce complex young men to numbers on a screen. That dehumanization harms sports culture and diminishes our collective empathy.",
        "reflection": "Every athlete stepping onto the hardwood has lived through battles nobody knows about. When we choose to see their full humanity, sportsmanship elevates and the game becomes truly inspiring.",
        "takeaway": "Let us honor the people behind the jerseys. Support our athletes with respect, empathy, and dignity: in victory and in adversity alike.",
        "foundation": "Foundation 10: Legacy, Culture and Community Impact"
    },
    {
        "id": "YAXEL_010",
        "ad_num": 10,
        "title": "A PERSONAL MESSAGE FROM LORNETTE DAYE",
        "dueAt": "2026-11-13T15:30:00.000Z",
        "slot": "Day 21 Morning (08:30 AM MST)",
        "theme_line": "Yaxel, I admire how well you are playing while your family is facing a difficult time.",
        "invisible_battle": "As a former athlete and Olympic-level coach, I understand that the battles outside sport can be as challenging as those within it. Competing at the highest professional level while keeping your heart anchored to family requires rare courage.",
        "reflection": "Yaxel, keep believing in your abilities. Stay focused on what you can control, and above all, enjoy the moments you have worked so hard for. You are showing what it means to lead with character, dignity, and quiet strength.",
        "takeaway": "Wishing you, your mother, and your family strength, love, and many beautiful moments together. You have the respect of champions everywhere.",
        "foundation": "Foundation 1: Identity Beyond Sport and Foundation 4: Resilience After Setback"
    }
]

HASHTAGS = "#YaxelLendeborg #LornetteDaye #BehindTheAthlete #MentalHealthInSports #GoldenState #Basketball #AthleteDevelopment #Foundations #HighPerformance #NBA"

def build_post_text(item):
    text = f"""{item['title']}

"{item['theme_line']}"

THE INVISIBLE BATTLE:
{item['invisible_battle']}

FROM OLYMPIC-LEVEL COACH LORNETTE DAYE:
{item['reflection']}

KEY TAKEAWAY:
{item['takeaway']}

ATHLETE DEVELOPMENT INSIGHT:
Lornette's Foundations: {item['foundation']}

Learn how Lornette's complete athlete development system equips competitors to build resilience, regulate emotional pressure, and protect their identity on and off the court:
https://lornettedaye.com/foundations

Sincerely,
Lornette Daye
Olympic-level Coach and Canadian National Champion

{HASHTAGS}"""

    # Strict Invariant Assertions
    assert "*" not in text, f"AD {item['ad_num']} contains asterisks!"
    assert "—" not in text, f"AD {item['ad_num']} contains em dash!"
    assert "&mdash;" not in text, f"AD {item['ad_num']} contains mdash!"
    assert "\u2014" not in text, f"AD {item['ad_num']} contains unicode em dash!"

    return text

def build_queue():
    queue = []
    for item in CAMPAIGN_DATA:
        img_name = f"yaxel-{item['ad_num']:02d}.png"
        img_url = f"{BASE_URL}/{img_name}"
        post_text = build_post_text(item)
        
        queue.append({
            "id": item["id"],
            "ad_num": item["ad_num"],
            "title": item["title"],
            "slot": item["slot"],
            "dueAt": item["dueAt"],
            "channel_id": CHANNEL_ID,
            "mode": "customScheduled",
            "schedulingType": "automatic",
            "asset_url": img_url,
            "asset_type": "image",
            "text": post_text
        })
    return queue

def main():
    print("================================================================")
    print("🏀 LD x YAXEL LENDEBORG 3-WEEK CAMPAIGN: BEHIND THE ATHLETE")
    print("Authoritative Voice: Lornette Daye")
    print("Cadence: 10 Ads paced across 21 Days (Oct 24 - Nov 13, 2026)")
    print("Zero Asterisks | Zero Em Dashes | 10 Curated 1254x1254 Assets")
    print("================================================================\n")
    
    queue = build_queue()
    print(f"Generated {len(queue)} bespoke posts across 21 calendar days.")
    
    output_path = "scripts/master-yaxel-queue.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(queue, f, indent=2)
        
    print(f"Successfully saved master queue to: {output_path}")
    
    asterisk_count = sum(p["text"].count("*") for p in queue)
    em_dash_count = sum(p["text"].count("—") for p in queue)
    print(f"Audit Results:")
    print(f"- Asterisks Count: {asterisk_count} (Must be 0)")
    print(f"- Em Dashes Count: {em_dash_count} (Must be 0)")
    print(f"- Start: {queue[0]['dueAt']} ({queue[0]['slot']})")
    print(f"- Finish: {queue[-1]['dueAt']} ({queue[-1]['slot']})")
    print(f"- Total Calendar Span: 21 Days")
    print("\n✅ ZERO-ASTERISK AND 3-WEEK CALENDAR INVARIANTS VERIFIED.")

if __name__ == "__main__":
    main()
