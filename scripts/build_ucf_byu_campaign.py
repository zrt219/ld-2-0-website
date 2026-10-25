import json
import os
from datetime import datetime, timezone

BASE_MEDIA_URL = "https://lornettedaye.com/campaigns/ucf-byu"

posts_data = [
    {
        "id": 1,
        "date_str": "2026-10-24T18:45:00-06:00", # 6:45 PM MDT tonight
        "asset": "ucf_byu_upset_plate_01.png",
        "isVideo": False,
        "title": "HISTORIC UPSET: UCF SHOCKS NO. 2 BYU 39-31 IN DOUBLE OVERTIME",
        "caption": """HISTORIC UPSET: UCF SHOCKS NO. 2 BYU 39-31 IN DOUBLE OVERTIME.

In one of the most electric, fearless finishes of the entire college football season, the UCF Knights have brought down the undefeated No. 2-ranked BYU Cougars in Orlando.

Final score: UCF 39, No. 2 BYU 31 in double overtime.

This is not just another win on the schedule. This is the first victory over a top-5 team in UCF program history.

When you step onto the field against the second-ranked team in the nation, every spectator expects you to hesitate. But in elite sport, rankings do not make tackles, and reputations do not execute third-down conversions.

As an Olympic-level coach and former national champion, I always remind athletes that an upset is never an accident. It is the predictable outcome of a team that refused to be intimidated by someone else's ranking, maintained total composure through high-stress referee reviews, and executed when the game hung on a single play.

Congratulations to the UCF Knights, their coaching staff, and the roaring fans who stormed the field in Orlando.

Where were you when UCF pulled off the shock of the season?

Explore how elite athletes and high-performing leaders build composure and execution under extreme pressure:
https://lornettedaye.com/foundations

#UCF #UCFKnights #ChargeOn #Big12 #BYU #CollegeFootball #CFBUpset #HistoricWin #BetterPeopleBetterPlayers #LornettesFoundations #ChampionMindset"""
    },
    {
        "id": 2,
        "date_str": "2026-10-24T20:00:00-06:00", # 8:00 PM MDT tonight
        "asset": "ucf_byu_touchdown_2ot.mp4",
        "isVideo": True,
        "title": "ONE PLAY. ONE TOUCHDOWN: KEYONE JENKINS TO GRAYSON BROUSSEAU IN 2OT",
        "caption": """ONE PLAY. ONE TOUCHDOWN. DOUBLE OVERTIME EXECUTION.

Watch the focus in this sequence.

Second overtime. The physical exhaustion is absolute. Legs are heavy, breath is shallow, and the entire stadium is holding its collective breath.

Quarterback Keyone Jenkins takes the snap, stands tall in the pocket, and delivers a surgical 2-yard strike to tight end Grayson Brousseau in the end zone.

In high-performance athletics, the red zone in overtime is where technique either breaks down or solidifies legacy. Most athletes rush their reads when the clock is tight and the stakes are immense. Great athletes slow their heart rate, trust their muscle memory, and deliver with calm precision.

Repetition in empty practice facilities creates calm in sold-out stadiums.

What was your immediate reaction when Jenkins found Brousseau for this score?

Discover how we train competitors in emotional regulation and fourth-quarter execution:
https://lornettedaye.com/foundations

#UCF #ChargeOn #KeyoneJenkins #DoubleOvertime #Touchdown #ClutchPerformance #CollegeFootball #LornettesFoundations #BetterPeopleBetterPlayers #ExecutionUnderPressure"""
    },
    {
        "id": 3,
        "date_str": "2026-10-24T21:30:00-06:00", # 9:30 PM MDT tonight
        "asset": "ucf_byu_magical_2pt_conversion.mp4",
        "isVideo": True,
        "title": "THE MAGICAL 2-POINT CONVERSION: CALCULATED AGGRESSION UNDER PRESSURE",
        "caption": """THE MAGICAL 2-POINT CONVERSION: CALCULATED AGGRESSION UNDER PRESSURE.

Leading 37-31 in double overtime, UCF faced a critical tactical decision. Kick the extra point for a seven-point lead, or go for two to make it a full eight-point cushion.

They did not play not to lose. They attacked to win.

Watch Keyone Jenkins escape pressure, maintain downfield vision, and thread a magnificent conversion pass to seize complete control of the contest at 39-31.

In my four decades coaching Olympic athletes, the biggest difference between competitors who almost win and champions who finish the job is courage in pivotal moments. When you have momentum, you do not pull back. You press the advantage.

Fortune favors the team that stays on the offensive when fear would suggest caution.

How brilliant was the play-call and execution on this crucial conversion?

Learn how we train teams and executive leaders to make courageous, high-stakes decisions:
https://lornettedaye.com/foundations

#UCFKnights #ChargeOn #TwoPointConversion #CalculatedRisk #BoldLeadership #Big12Football #LornettesFoundations #BetterPeopleBetterPlayers #ChampionMindset"""
    },
    {
        "id": 4,
        "date_str": "2026-10-25T08:30:00-06:00", # 8:30 AM MDT Sunday
        "asset": "ucf_byu_goal_line_stand_win.mp4",
        "isVideo": True,
        "title": "THE 4TH-AND-GOAL STAND: DEFENSE SEALS THE FIELD STORMING",
        "caption": """THE 4TH-AND-GOAL STAND: WHEN DEFENSE SEALS IMMORTALITY.

Turn the sound up and witness Orlando erupt.

BYU drove all the way down to the UCF 4-yard line in second overtime. Fourth down. The entire game, the undefeated season for BYU, and the biggest upset in UCF history came down to four yards.

The UCF secondary played disciplined, lock-down coverage. Bear Bachmeier's fourth-down pass fell incomplete on the turf, and instantly, thousands of roaring students and fans stormed the field.

Defense wins championships because defense is built entirely on desire, communication, and refusing to yield an inch of ground. When your offense gives you an eight-point lead, the defense has to anchor the result.

That defensive stand will be talked about in Orlando for the next thirty years.

Rate the intensity of this goal-line stand from 1 to 10!

Learn how to build resilient team defense and unbreakable culture under pressure:
https://lornettedaye.com/foundations

#UCF #FieldStorming #GoalLineStand #DefenseWins #CollegeFootballUpset #ChargeOn #LornettesFoundations #BetterPeopleBetterPlayers #ResilienceAfterSetback"""
    },
    {
        "id": 5,
        "date_str": "2026-10-25T12:00:00-06:00", # 12:00 PM MDT Sunday
        "asset": "ucf_byu_capitalize_penalty.mp4",
        "isVideo": True,
        "title": "POISE AMID CHAOS: CAPITALIZING ON OPPONENT MISTAKES",
        "caption": """POISE AMID CHAOS: HOW TO CAPITALIZE ON OPPONENT MISTAKES.

Watch how UCF responded when the game seemed on the verge of slipping away.

Late in the fourth quarter, an initial sack and fumble call threatened to end the contest. But UCF did not panic. The coaching staff and players remained composed while officials reviewed the play, successfully overturning it to an incomplete pass. Then, when BYU was flagged for an unsportsmanlike conduct penalty, UCF immediately seized the momentum.

In elite sport, chaos is guaranteed. Referees make controversial calls. Reviews take minutes. Opponents lose their discipline.

The team that regulates its emotions and immediately shifts into attack mode will always punish the opponent's lapse in composure.

Emotional poise is a competitive superpower. When everyone around you is losing their heads, your calm becomes your weapon.

How important is emotional discipline when officiating drama strikes in a close game?

Discover our Olympic frameworks for emotional regulation and poise:
https://lornettedaye.com/foundations

#UCFKnights #ChargeOn #EmotionalRegulation #DisciplineSystems #GameManagement #CollegeFootball #LornettesFoundations #BetterPeopleBetterPlayers #FocusUnderPressure"""
    },
    {
        "id": 6,
        "date_str": "2026-10-25T15:30:00-06:00", # 3:30 PM MDT Sunday
        "asset": "ucf_byu_upset_plate_02.png",
        "isVideo": False,
        "title": "CULTURE OVER RANKING: WHY PREPARATION CONQUERS PERCEPTION",
        "caption": """CULTURE OVER RANKING: WHY PREPARATION CONQUERS PERCEPTION.

Look closely at this image: BYU 31, UCF 39 in double overtime.

Entering this weekend, BYU was sitting at No. 2 in the country with an unblemished record and national title aspirations. On paper, the national media gave them every statistical edge.

But games are not played on spreadsheets. They are played on grass by young men whose belief in one another can outshine any national poll.

In my 40-plus years of coaching, I have watched underdogs dismantle heavy favorites time and again. The secret is always cultural cohesion:
- Believing your preparation is superior regardless of the opponent's jersey.
- Embracing physical contact without backing down.
- Treating overtime not as a burden, but as an opportunity to prove your conditioning.

Rankings are opinions. Execution is a fact.

What lesson from UCF's historic win can you apply to the battles in your own career this week?

Train your mind for elite competition with "Survival Skills for Athletes" ($14.99 CAD):
https://lornettedaye.com/books

#UCF #BYU #DavidVsGoliath #CultureWins #CollegeFootball #PreparationExcellence #LornettesFoundations #BetterPeopleBetterPlayers #ChampionMindset"""
    },
    {
        "id": 7,
        "date_str": "2026-10-25T18:30:00-06:00", # 6:30 PM MDT Sunday
        "asset": "ucf_byu_upset_plate_03.png",
        "isVideo": False,
        "title": "THE AFTERMATH: CARRYING THE STANDARD FORWARD",
        "caption": """THE AFTERMATH: CARRYING THE STANDARD FORWARD.

The field has been cleared. The goalposts survived the night. The celebration in Orlando will echo for months.

Now comes the ultimate test of athletic maturity: What do you do on Monday morning?

When you knock off the No. 2 team in the nation, the entire country begins looking at you differently. You are no longer the hunter lurking in the shadows; you are the team everyone wants to measure themselves against.

In high-performance leadership, we teach that winning an upset requires courage, but sustaining that standard requires systems. True competitors do not celebrate themselves into complacency. They review the film, fix the missed assignments, and demand even more from their Tuesday conditioning drills.

Enjoy the glory of double overtime. And then get back to work.

Knight Nation: What is the ceiling for this UCF team for the remainder of this season?

Learn more about building sustainable high-performance cultures that outlast the moment:
https://lornettedaye.com/foundations

#UCFKnights #ChargeOn #TheStandard #KeepMovingForward #Big12Football #HighPerformanceCulture #BetterPeopleBetterPlayers #LornettesFoundations #LegacyAndImpact"""
    }
]

# Assertions
for p in posts_data:
    assert "*" not in p["caption"], f"Asterisk in caption id {p['id']}"
    assert "*" not in p["title"], f"Asterisk in title id {p['id']}"
    assert "—" not in p["caption"], f"Em-dash in caption id {p['id']}"
    assert "—" not in p["title"], f"Em-dash in title id {p['id']}"
    local_path = os.path.join(r"c:\Users\Zhane\Documents\New project\LD 2.0 WEBSITE\public\campaigns\ucf-byu", p["asset"])
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
        "isVideo": p["isVideo"],
        "local_file": p["asset"]
    })

out_path = r"c:\Users\Zhane\Documents\New project\LD 2.0 WEBSITE\scripts\master-ucf-byu-queue.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(queue, f, indent=2, ensure_ascii=False)

print(f"Successfully generated {len(queue)} campaign posts in {out_path}!")
for q in queue:
    print(f"Post {q['id']} | {'VIDEO' if q['isVideo'] else 'IMAGE'} | {q['dueAt']} | {q['assetUrl']}")
