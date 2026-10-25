import json
import os
from datetime import datetime, timezone

BASE_MEDIA_URL = "https://lornettedaye.com/campaigns/oilers"

posts_data = [
    {
        "id": 1,
        "date_str": "2026-10-24T20:15:00-06:00", # Tonight Sat Oct 24 @ 8:15 PM MDT
        "asset": "rnh-shootout-winner.mp4",
        "title": "THE SHOOTOUT WINNER: RYAN NUGENT-HOPKINS CALLS GAME",
        "caption": """THE SHOOTOUT WINNER: RYAN NUGENT-HOPKINS CALLS GAME.

Watch the patience on this shootout attempt.

October 22 at Rogers Place. A 6-5 double-overtime thriller against Carolina comes down to individual skill on open ice.

Ryan Nugent-Hopkins steps onto the ice for his very first game of the season after missing nine straight games with injury. The building is roaring. Every eye in Alberta is glued to his stick.

He glides in, reads the goaltender's stance, shifts his weight, and buries the only successful shootout goal of the entire night while Devon Levi completely shuts the door at the other end.

In over four decades coaching Olympic athletes, I tell my champions that calm under pressure is not born in the moment. It is the predictable outcome of mental preparation. When you have done the invisible work during rehab, your pulse stays steady when the game is on your stick.

Fan Question: Where were you when Nuge scored this shootout winner? Drop your memory below.

Discover how elite athletes train mental stillness and clutch execution under pressure:
https://lornettedaye.com/foundations

#EdmontonOilers #Oilers #LetsGoOilers #OilCountry #RyanNugentHopkins #DevonLevi #NHL #ClutchPerformance #LornettesFoundations #BetterPeopleBetterPlayers #ChampionMindset"""
    },
    {
        "id": 2,
        "date_str": "2026-10-25T11:00:00-06:00", # Sun Oct 25 @ 11:00 AM MDT
        "asset": "rnh-shootout-winner.mp4",
        "title": "THE COMEBACK: RETURNING FROM INJURY STRAIGHT INTO THE FIRE",
        "caption": """THE COMEBACK: RETURNING FROM INJURY STRAIGHT INTO THE FIRE.

Imagine missing nine consecutive games, rehabbing away from the spotlight, and having your very first game back be a 6-5 emotional rollercoaster against a relentless Carolina squad.

Most athletes ask for sheltered minutes in their return. They want low-leverage shifts to get their legs back.

Ryan Nugent-Hopkins did not ask for ease. He competed through sixty minutes of high-tempo hockey, absorbed five minutes of sudden-death overtime, and then took the deciding shot in the shootout.

In high-performance sports, returning from setback is never purely physical. It is an exercise in mental trust. You must trust that your conditioning is solid and that your timing will answer the call.

Nuge demonstrated why he has been the quiet cornerstone of this franchise for over a decade: unwavering professionalism and total accountability.

Fan Question: What does Ryan Nugent-Hopkins mean to Oil Country and the culture of this locker room?

Read "Survival Skills for Athletes" ($14.99 CAD) for strategies on returning stronger after injury:
https://lornettedaye.com/books

#EdmontonOilers #OilersNation #RyanNugentHopkins #TheComeback #ResilienceAfterSetback #OilCountry #NHL #LornettesFoundations #BetterPeopleBetterPlayers #AthleteDevelopment"""
    },
    {
        "id": 3,
        "date_str": "2026-10-26T12:15:00-06:00", # Mon Oct 26 @ 12:15 PM MDT
        "asset": "rnh-shootout-winner.mp4",
        "title": "PRESSURE MOMENT: THE PSYCHOLOGY OF THE DECIDING ATTEMPT",
        "caption": """PRESSURE MOMENT: THE PSYCHOLOGY OF THE DECIDING ATTEMPT.

The NHL shootout is one of the most psychologically unforgiving environments in professional sport.

There are no teammates to pass to. There is no flow or momentum to lean on. Just you, the puck, twenty-five meters of ice, and a goaltender whose entire job is to read your eyes.

Notice what Nugent-Hopkins does not do: he does not rush. He maintains optical calm, delays his commitment until the goaltender bites, and finishes with surgical precision.

In our Performance Edge coaching framework, we emphasize that your previous shot cannot hit your next shot. When an athlete decouples their self-worth from previous missed chances, anxiety disappears. They become completely absorbed in the execution of the next movement.

Pair that with Devon Levi standing tall in goal, and you get two points in the standings.

Fan Question: When the game is on the line in a deciding shootout, who is the one player in hockey history you would send over the boards?

Explore our frameworks for performing under extreme organizational pressure:
https://lornettedaye.com/foundations

#LetsGoOilers #EdmontonOilers #Shootout #HighPressureExecution #PerformanceEdge #EmotionalPoise #NHL #DevonLevi #LornettesFoundations #BetterPeopleBetterPlayers"""
    },
    {
        "id": 4,
        "date_str": "2026-10-28T11:00:00-06:00", # Wed Oct 28 @ 11:00 AM MDT
        "asset": "rnh-shootout-winner.mp4",
        "title": "THE COMPLETE PERFORMANCE: McDAVID, DRAISAITL, NUGE, AND LEVI",
        "caption": """THE COMPLETE PERFORMANCE: McDAVID, DRAISAITL, NUGE, AND LEVI.

Look at the extraordinary scoreline from October 22:
- Edmonton Oilers 6, Carolina Hurricanes 5 (Shootout)
- Connor McDavid: 5 Points
- Leon Draisaitl: 5 Points
- Ryan Nugent-Hopkins: The Game-Deciding Shootout Winner
- Devon Levi: Shutting the Door in the Skills Competition

When superstar talent produces ten combined points, that is world-class offensive firepower. But championship rosters cannot rely on brilliance alone. They need defensive grit when Carolina pushes back, and they need secondary leaders to step forward in the clutch.

In my work mentoring athletic directors and corporate executives, true team excellence happens when every member understands their distinct assignment. McDavid and Draisaitl broke the game open; Nugent-Hopkins and Levi sealed the victory.

Fan Question: With McDavid and Draisaitl posting five-point nights, Nuge scoring the winner, and Levi holding the line, who gets your Player-of-the-Game vote?

Learn how we help elite organizations build shared accountability and role clarity:
https://lornettedaye.com/foundations

#EdmontonOilers #ConnorMcDavid #LeonDraisaitl #RyanNugentHopkins #DevonLevi #TeamExcellence #OilCountry #NHL #LornettesFoundations #BetterPeopleBetterPlayers"""
    },
    {
        "id": 5,
        "date_str": "2026-10-30T17:45:00-06:00", # Fri Oct 30 @ 5:45 PM MDT
        "asset": "rnh-shootout-winner.mp4",
        "title": "OIL COUNTRY REMEMBERS: WHERE DOES THIS RANK AMONG ICONIC FINISHES?",
        "caption": """OIL COUNTRY REMEMBERS: WHERE DOES THIS RANK AMONG ICONIC FINISHES?

Certain regular season games feel like April playoff hockey.

When Carolina pushed Edmonton to the limit in a 6-5 barnburner, Rogers Place stood on its feet for every single second of extra time. And when Ryan Nugent-Hopkins celebrated his game-winner with Devon Levi, the entire city shared that emotional release.

Sports provide communities with moments of shared connection, identity, and collective pride. That energy is why athletic culture matters far beyond the rink.

When young athletes watch a veteran like Nugent-Hopkins handle adversity, rehab quietly, and deliver when called upon, they learn what authentic athletic character looks like.

Better people make better players.

Fan Question: Where does this 6-5 shootout victory rank among your favourite Edmonton Oilers regular season finishes in recent years?

Explore Lornette Daye's Complete Athlete Development System:
https://lornettedaye.com/foundations

#EdmontonOilers #OilCountry #RogersPlace #LetsGoOilers #OilersHockey #CommunityPride #BetterPeopleBetterPlayers #LornettesFoundations #LegacyAndImpact #ChampionStandards"""
    }
]

# Assertions
for p in posts_data:
    assert "*" not in p["caption"], f"Asterisk in caption id {p['id']}"
    assert "*" not in p["title"], f"Asterisk in title id {p['id']}"
    assert "—" not in p["caption"], f"Em-dash in caption id {p['id']}"
    assert "—" not in p["title"], f"Em-dash in title id {p['id']}"
    local_path = os.path.join(r"c:\Users\Zhane\Documents\New project\LD 2.0 WEBSITE\public\campaigns\oilers", p["asset"])
    assert os.path.isfile(local_path), f"Asset missing: {local_path}"

queue = []
for p in posts_data:
    dt = datetime.fromisoformat(p["date_str"])
    due_at = dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")
    queue.append({
        "id": p["id"],
        "date": dt.strftime("%Y-%m-%d"),
        "dueAt": due_at,
        "title": p["title"],
        "caption": p["caption"],
        "assetUrl": f"{BASE_MEDIA_URL}/{p['asset']}",
        "isVideo": True,
        "local_file": p["asset"]
    })

out_path = r"c:\Users\Zhane\Documents\New project\LD 2.0 WEBSITE\scripts\master-oilers-shootout-queue.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(queue, f, indent=2, ensure_ascii=False)

print(f"Successfully generated {len(queue)} campaign posts in {out_path}!")
for q in queue:
    print(f"Post {q['id']} | {q['dueAt']} | {q['assetUrl']}")
