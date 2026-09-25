# -*- coding: utf-8 -*-
import os
import sys
import json
import urllib.request
import urllib.error
import ssl
import time

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)

TOKEN = os.environ.get('BUFFER_ACCESS_TOKEN', 'mLbjEsRdn5FKtGOskFoGzK-gW2CGTl8dfAK8klDVEPC')
CHANNEL_ID = '6a39d30c5ab6d2f1065f5301'  # Lornette Daye LinkedIn

CDN_BASE = 'https://lornettedaye.com/campaigns/curacao'

posts_data = [
    {
        "id": 1,
        "type": "image",
        "slot": "Thursday (10:30 AM MDT)",
        "dueAt": "2026-10-01T16:30:00.000Z",
        "assetFile": "curacao-01.png",
        "assetUrl": f"{CDN_BASE}/curacao-01.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": (
            "CURAÇAO FANS: WHAT DID THAT SECOND HALF FEEL LIKE?! 🇨🇼🌊\n\n"
            "Costa Rica: 3. Curaçao: 0. Halftime.\n\n"
            "Then the second half whistle blew:\n"
            "• Kenji Gorré cuts the deficit.\n"
            "• Tahith Chong levels the psychological momentum.\n"
            "• Kenji Gorré strikes AGAIN.\n"
            "• Jordi Paulina finishes the masterpiece in the 88th minute.\n"
            "Final score: Costa Rica 3, Curaçao 4.\n\n"
            "In four decades coaching Olympic athletes, I have learned that the scoreboard tells you where you are, "
            "but it can never dictate where you are going. Curaçao could have accepted damage limitation on the road. "
            "Instead, they decided to change the story entirely.\n\n"
            "To everyone watching in Kòrsou, the Netherlands, and across the global Curaçao diaspora: "
            "Where were you when that fourth goal went in?\n\n"
            "👉 Discover how to build unshakeable belief when the odds are stacked against you. "
            "Explore *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#TheBlueWave #Curaçao #DushiKòrsou #TeamCuraçao #CuraçaoFootball #CaribbeanPride #SmallIslandBigDreams #CONCACAF #ConcacafNationsLeague #FootballComeback #HistoricComeback #PerformanceUnderPressure #FinishStrong #LornetteDaye"
        )
    },
    {
        "id": 2,
        "type": "image",
        "slot": "Friday (10:30 AM MDT)",
        "dueAt": "2026-10-02T16:30:00.000Z",
        "assetFile": "curacao-02.png",
        "assetUrl": f"{CDN_BASE}/curacao-02.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "THE BLUE WAVE DID NOT BREAK. IT GREW BIGGER. 🌊🇨🇼\n\n"
            "Costa Rica: 3. Curaçao: 0. Halftime.\n\n"
            "A lot of teams would have retreated into a defensive shell just to avoid embarrassment. "
            "Curaçao came out of the tunnel with one singular thought: win this match.\n\n"
            "Four unanswered goals away from home against a regional giant. "
            "This is what sports is truly about. It is not merely the goals; it is the response. "
            "What happens inside a squad when the first 45 minutes go completely wrong, yet they find enough internal poise "
            "to write a completely different ending?\n\n"
            "Executives & Leaders: When your quarterly kickoff goes off the rails, does your organization panic, or execute your second-half turnaround?\n\n"
            "👉 Train your leadership team to command high-pressure arenas with Olympic calm. "
            "Book Coach Lornette Daye for executive summits: lornettedaye.com/speaking\n\n"
            "#TheBlueWave #Curaçao #TeamCuraçao #CuraçaoFootball #CaribbeanPride #SmallIslandBigDreams #CONCACAF #FootballComeback #HistoricComeback #ExecutiveLeadership #ResilienceUnderPressure #CoachLornette #LornetteDaye"
        )
    },
    {
        "id": 3,
        "type": "image",
        "slot": "Saturday (11:30 AM MDT)",
        "dueAt": "2026-10-03T17:30:00.000Z",
        "assetFile": "curacao-03.png",
        "assetUrl": f"{CDN_BASE}/curacao-03.png",
        "cta": "Survival Skills for Athletes (lornettedaye.com/books)",
        "text": (
            "IF YOU TURNED THE MATCH OFF AT 3-0, YOU MISSED THE LESSON. 😳🇨🇼\n\n"
            "Be completely honest: who predicted Curaçao was coming back from that?\n\n"
            "Three goals down in San José. One half remaining. Hostile crowd. "
            "Yet at the final whistle, the scoreboard flashed COSTA RICA 3, CURAÇAO 4.\n\n"
            "That is why you never judge an athlete or team purely by their low points. "
            "The real test of high performance is discovering how competitors respond when failure seems guaranteed. "
            "Curaçao did not just score four goals. They refused to let 45 minutes of adversity define their standard.\n\n"
            "Athletes: How quickly do you reset your emotional focus when the first half gets away from you?\n\n"
            "👉 Master the tools of emotional regulation, focus, and resilience under extreme pressure. "
            "Read *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#TheBlueWave #Curaçao #TeamCuraçao #SurvivalSkillsForAthletes #MentalToughness #ResetRoutine #CONCACAF #ConcacafNationsLeague #FootballComeback #NeverCountThemOut #LornetteDaye"
        )
    },
    {
        "id": 4,
        "type": "video",
        "slot": "Sunday (11:30 AM MDT)",
        "dueAt": "2026-10-04T17:30:00.000Z",
        "assetFile": "curacao.mp4",
        "assetUrl": f"{CDN_BASE}/curacao.mp4",
        "cta": "Keynotes & Book Catalog (lornettedaye.com)",
        "text": (
            "WATCH THE COMEBACK: THE BLUE WAVE IN FULL FLIGHT. 🎥🇨🇼⚽️\n\n"
            "Four goals in forty-five minutes. Press play and witness momentum shift in real time.\n\n"
            "Look at the transition speed. Look at the belief radiating across every blue jersey. "
            "When Kenji Gorré struck first, you could feel Costa Rica's certainty begin to crack. "
            "By the time Jordi Paulina buried the winner in the 88th minute, history was sealed.\n\n"
            "This video clip is proof that momentum is not magic. It is created when disciplined athletes execute simple tasks "
            "repeatedly with relentless conviction until the opposition breaks.\n\n"
            "Curaçao supporters around the world: What was your exact reaction when the final whistle sounded?\n\n"
            "👉 Experience more stories, frameworks, and masterclasses on peak performance: lornettedaye.com\n\n"
            "#TheBlueWave #Curaçao #TeamCuraçao #CuracaoFootball #CONCACAF #ConcacafNationsLeague #HighlightReel #FootballComeback #EpicTurnaround #CaribbeanAthletes #LornetteDaye #BetterPeopleBetterPlayers"
        )
    },
    {
        "id": 5,
        "type": "image",
        "slot": "Monday (03:15 PM MDT)",
        "dueAt": "2026-10-05T21:15:00.000Z",
        "assetFile": "curacao-04.png",
        "assetUrl": f"{CDN_BASE}/curacao-04.png",
        "cta": "Executive Speaking (lornettedaye.com/speaking)",
        "text": (
            "SMALL ISLAND. MASSIVE AMBITION. 🇨🇼🏝️\n\n"
            "The size of a country never limits the magnitude of its vision.\n\n"
            "With roughly 160,000 residents, Curaçao has repeatedly proven to the international sports world "
            "that talent, cohesion, and cultural courage punch far above geopolitical weight classes. "
            "From Little League World Series championships to historic CONCACAF away victories, Kòrsou represents "
            "the ultimate underdog standard: fearless, unified, and technically brilliant.\n\n"
            "In enterprise leadership, market cap does not guarantee victory. Nimble, cohesive, purpose-driven teams "
            "consistently outmaneuver entrenched industry incumbents when conviction is high.\n\n"
            "Leaders: Is your team playing like a fearful incumbent or an inspired challenger?\n\n"
            "👉 Inspire your organization to punch above its weight with Olympic-level purpose. "
            "Inquire for executive summits: lornettedaye.com/speaking\n\n"
            "#SmallIslandBigDreams #TheBlueWave #Curaçao #DushiKòrsou #CaribbeanPride #UnderdogMentality #PunchAboveYourWeight #ExecutiveLeadership #OlympicCoach #LornetteDaye"
        )
    },
    {
        "id": 6,
        "type": "image",
        "slot": "Tuesday (07:00 AM MDT)",
        "dueAt": "2026-10-06T13:00:00.000Z",
        "assetFile": "curacao-05.png",
        "assetUrl": f"{CDN_BASE}/curacao-05.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": (
            "KENJI GORRÉ: THE ART OF THE BRACE UNDER PRESSURE. ⚽️⚡️\n\n"
            "When your nation needs an answer, leaders deliver.\n\n"
            "Trailing 3-0 on the road, someone has to step forward and plant the flag. "
            "Kenji Gorré did not just score; he dismantled Costa Rica's back line twice with ruthless clinical composure. "
            "His brace transformed what looked like a rout into an electric tactical contest.\n\n"
            "In high-stakes athletics, composure in front of goal is not taught on chalkboards. "
            "It is forged through thousands of repetitions in silence, allowing the athlete's heart rate to stay low "
            "while execution remains lethal.\n\n"
            "Where in your life or career do you need to step forward and deliver your own second-half breakthrough?\n\n"
            "👉 Discover how to finish every chapter of life with purpose and authority. "
            "Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#KenjiGorré #TheBlueWave #CuraçaoFootball #Brace #ClinicalFinishing #PoiseUnderPressure #FinishStrong #TeamCuraçao #CONCACAF #LornetteDaye"
        )
    },
    {
        "id": 7,
        "type": "image",
        "slot": "Wednesday (07:00 AM MDT)",
        "dueAt": "2026-10-07T13:00:00.000Z",
        "assetFile": "curacao-06.png",
        "assetUrl": f"{CDN_BASE}/curacao-06.png",
        "cta": "Survival Skills for Athletes (lornettedaye.com/books)",
        "text": (
            "TAHITH CHONG: SHIFTING THE GRAVITY OF THE MATCH. 🌪️💙\n\n"
            "World-class quality turning hope into undeniable reality.\n\n"
            "When Tahith Chong equalized, the entire psychological equilibrium of the stadium shattered. "
            "You could see the disbelief in the eyes of Costa Rica's veteran defenders. "
            "That is the power of top-tier professional experience: staying patient, reading defensive gaps, "
            "and striking at the exact moment the opponent feels comfortable.\n\n"
            "Individual brilliance matters, but its highest purpose is elevating the collective belief of the entire squad. "
            "When Chong scored, every Curaçaoan on the pitch knew the match belonged to them.\n\n"
            "Athletes: How does your individual excellence raise the collective confidence of your teammates?\n\n"
            "👉 Strengthen your tactical decision-making, mental discipline, and leadership on the field. "
            "Explore *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#TahithChong #TheBlueWave #CuraçaoFootball #MomentumShift #TeamSynergy #SurvivalSkillsForAthletes #CONCACAF #NationsLeague #LornetteDaye"
        )
    },
    {
        "id": 8,
        "type": "video",
        "slot": "Thursday (07:00 AM MDT)",
        "dueAt": "2026-10-08T13:00:00.000Z",
        "assetFile": "curacao.mp4",
        "assetUrl": f"{CDN_BASE}/curacao.mp4",
        "cta": "Keynotes & Executive Summits (lornettedaye.com/speaking)",
        "text": (
            "JORDI PAULINA: THE 88TH-MINUTE WINNER IN 4K. 🎥🇨🇼🔥\n\n"
            "Watch history unfold in the closing moments.\n\n"
            "Eighty-seventh minute: 3-3. Most teams on the road settle for an honorable draw. "
            "Not Curaçao. Dick Advocaat sent Jordi Paulina onto the pitch with instructions to attack the box. "
            "One clinical touch, one decisive strike, and the ball hits the back of the net for 3-4.\n\n"
            "That moment demonstrates what I call championship greed: the refusal to settle for a safe compromise "
            "when your preparation has earned you the right to claim the entire prize.\n\n"
            "Leaders: When the market presents a rare window of opportunity, do you settle for safety, or seize the win?\n\n"
            "👉 Bring the mindset of decisive execution to your organization. "
            "Book Coach Lornette Daye for your corporate keynote: lornettedaye.com/speaking\n\n"
            "#JordiPaulina #TheBlueWave #WinningGoal #88thMinute #CuraçaoFootball #DecisiveAction #ExecutiveMindset #SportsLeadership #CONCACAF #LornetteDaye"
        )
    },
    {
        "id": 9,
        "type": "image",
        "slot": "Friday (07:00 AM MDT)",
        "dueAt": "2026-10-09T13:00:00.000Z",
        "assetFile": "curacao-07.png",
        "assetUrl": f"{CDN_BASE}/curacao-07.png",
        "cta": "Executive Coaching (lornettedaye.com/speaking)",
        "text": (
            "DICK ADVOCAAT: TACTICAL ADJUSTMENTS AT THE BREAK. 📋🧠\n\n"
            "What was said in the locker room when all seemed lost?\n\n"
            "At 3-0 down, emotional coaches yell. Great coaches diagnose. "
            "Dick Advocaat did not panic; he adjusted pressing triggers, altered substitution timing, and gave his players "
            "clear, actionable tactical instructions rather than vague emotional hype. "
            "The result was one of the most remarkable tactical turnarounds in modern international football.\n\n"
            "Leadership in a crisis is not about volume. It is about clarity. "
            "When your team is under fire, they do not need panic; they need an architect who can point them toward the solution.\n\n"
            "How do you communicate with your team when unexpected setbacks hit your operational plan?\n\n"
            "👉 Master executive poise, crisis leadership, and strategic agility with Coach Lornette Daye: lornettedaye.com/speaking\n\n"
            "#DickAdvocaat #TheBlueWave #TacticalMastery #CrisisLeadership #LockerRoomTalk #ExecutiveCoaching #StrategicAgility #LornetteDaye #Speaker"
        )
    },
    {
        "id": 10,
        "type": "image",
        "slot": "Saturday (02:00 PM MDT)",
        "dueAt": "2026-10-10T20:00:00.000Z",
        "assetFile": "curacao-08.png",
        "assetUrl": f"{CDN_BASE}/curacao-08.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": (
            "BAN KÒRSOU: DIASPORA PRIDE FROM WILLEMSTAD TO AMSTERDAM. 🇨🇼✈️\n\n"
            "United under one blue flag across continents.\n\n"
            "The beauty of Team Curaçao is how it bridges oceans. "
            "Athletes raised in the Caribbean and those developed in European academies wearing the same crest, "
            "singing the same anthem, and fighting for the pride of their ancestors. "
            "When that final whistle blew in San José, celebrations erupted across Willemstad, Rotterdam, Amsterdam, and North America.\n\n"
            "When a sports team represents a cultural heartbeat, they play with an emotional reservoir that money can never buy. "
            "That is the power of authentic cultural identity.\n\n"
            "Ban Kòrsou! 🌊💙\n\n"
            "👉 Discover the principles that turn shared heritage into unstoppable performance. "
            "Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#BanKòrsou #DushiKòrsou #TheBlueWave #CuraçaoDiaspora #CaribbeanPride #CulturalIdentity #FinishStrong #TeamCuraçao #LornetteDaye"
        )
    },
    {
        "id": 11,
        "type": "image",
        "slot": "Sunday (02:00 PM MDT)",
        "dueAt": "2026-10-11T20:00:00.000Z",
        "assetFile": "curacao-09.png",
        "assetUrl": f"{CDN_BASE}/curacao-09.png",
        "cta": "Survival Skills for Athletes (lornettedaye.com/books)",
        "text": (
            "YOUR PREVIOUS SHOT CANNOT HIT YOUR NEXT SHOT. 🎯🌊\n\n"
            "The timeless Olympic principle that decided the match.\n\n"
            "At halftime in San José, Costa Rica owned the statistics. They had the lead. They had the momentum. "
            "If Curaçao had allowed the errors of the first half to occupy their thoughts, the second half would have been a disaster. "
            "Instead, they operated on the signature principle I teach every athlete: your previous shot cannot hit your next shot.\n\n"
            "You cannot change the past 45 minutes. You can only master the possession directly in front of you. "
            "One tackle. One cross. One finish. That is how comebacks are constructed.\n\n"
            "What past mistake in your career do you need to release today so you can focus on your next execution?\n\n"
            "👉 Equip yourself with foundational mental models for elite athletic focus. "
            "Explore *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#BetterPeopleBetterPlayers #TheBlueWave #MentalResilience #FocusUnderPressure #SurvivalSkillsForAthletes #OlympicMindset #CoachLornette #LornetteDaye"
        )
    },
    {
        "id": 12,
        "type": "video",
        "slot": "Monday (02:00 PM MDT)",
        "dueAt": "2026-10-12T20:00:00.000Z",
        "assetFile": "curacao.mp4",
        "assetUrl": f"{CDN_BASE}/curacao.mp4",
        "cta": "Official Website & Books (lornettedaye.com)",
        "text": (
            "RELIVE THE MOMENTUM: FROM 3-0 TO 3-4 IN FULL MOTION. 🎥🇨🇼⚽️\n\n"
            "The match that proved why we fall in love with international football.\n\n"
            "Watch the defensive pressure intensify. Watch the spacing in the final third. "
            "This video compilation captures the heart of Curaçaoan football: technical flair combined with grit, "
            "passion, and brotherhood under the Caribbean blue flag.\n\n"
            "When the odds said impossible, Team Curaçao chose belief. "
            "May this historic comeback remind you this week that no deficit in life or business is insurmountable "
            "when your team stays unified and committed to finishing strong.\n\n"
            "To the people of Kòrsou: Keep shining on the world stage. The Blue Wave rolls on!\n\n"
            "👉 Explore books, executive coaching, and leadership masterclasses: lornettedaye.com\n\n"
            "#TheBlueWave #Curaçao #TeamCuraçao #FootballComeback #HistoricComeback #CaribbeanFootball #HighlightVideo #NeverGiveUp #FinishStrong #LornetteDaye"
        )
    },
    {
        "id": 13,
        "type": "image",
        "slot": "Tuesday (06:45 AM MDT)",
        "dueAt": "2026-10-13T12:45:00.000Z",
        "assetFile": "curacao-10.png",
        "assetUrl": f"{CDN_BASE}/curacao-10.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": (
            "REFUSING DAMAGE LIMITATION: THE CHAMPION MINDSET. 🛡️🔥\n\n"
            "Average teams play to avoid humiliation. Champions play to rewrite destiny.\n\n"
            "When adversity strikes, human psychology naturally defaults to fear: protect what remains, minimize the loss, "
            "and survive to play another day. But settling for damage limitation guarantees defeat. "
            "Curaçao chose the champion route: they took calculated risks, committed numbers forward, and turned Costa Rica's comfort into panic.\n\n"
            "If you want to achieve extraordinary breakthroughs in business or sport, you cannot play with defensive timidity. "
            "You must stay aggressive on your strategic goals.\n\n"
            "Where in your life are you currently settling for damage limitation instead of playing to win?\n\n"
            "👉 Step into fearless execution and finish what you started with authority. "
            "Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#ChampionMindset #RefuseDefeat #TheBlueWave #CuraçaoFootball #FearlessLeadership #FinishStrong #OlympicStandards #LornetteDaye"
        )
    },
    {
        "id": 14,
        "type": "image",
        "slot": "Wednesday (06:45 AM MDT)",
        "dueAt": "2026-10-14T12:45:00.000Z",
        "assetFile": "curacao-11.png",
        "assetUrl": f"{CDN_BASE}/curacao-11.png",
        "cta": "Keynotes & Summits (lornettedaye.com/speaking)",
        "text": (
            "NOS TA KÒRSOU: RESILIENCE IS IN OUR DNA. 🇨🇼💎\n\n"
            "When national pride runs deeper than the scoreboard, miracles become repeatable.\n\n"
            "Look at the joy in this photograph. That is not just celebration of three points in a table. "
            "It is the affirmation of an island's identity. For generations, Caribbean nations have navigated economic, "
            "geographic, and logistical hurdles through profound cultural resilience. "
            "When that heritage translates onto the football pitch, it creates a team that simply refuses to stay down.\n\n"
            "True strength is not never falling. It is the communal certainty that you will rise again every single time.\n\n"
            "Nos ta Kòrsou! 🌊💙\n\n"
            "👉 Cultivate unbreakable resilience and purpose across your leadership team. "
            "Book Coach Lornette Daye for your corporate keynote: lornettedaye.com/speaking\n\n"
            "#NosTaKòrsou #TheBlueWave #Curaçao #CaribbeanResilience #DushiKòrsou #SmallIslandBigDreams #OlympicMindset #LornetteDaye #KeynoteSpeaker"
        )
    },
    {
        "id": 15,
        "type": "video",
        "slot": "Thursday (06:45 AM MDT)",
        "dueAt": "2026-10-15T12:45:00.000Z",
        "assetFile": "curacao.mp4",
        "assetUrl": f"{CDN_BASE}/curacao.mp4",
        "cta": "Official Leadership Catalog (lornettedaye.com)",
        "text": (
            "THE BLUE WAVE ROLLS ON: CELEBRATING HISTORY WITH PURPOSE. 🌊🇨🇼🏆\n\n"
            "Closing the chapter on an unforgettable night in Costa Rica.\n\n"
            "From Gorré's double to Chong's brilliance and Paulina's ice-cold finish, "
            "the 3-4 victory will be replayed in living rooms, sports bars, and training pitches across Curaçao for decades. "
            "It showed the world that when heart meets tactical discipline, the impossible becomes inevitable.\n\n"
            "As we celebrate Team Curaçao, remember that the greatest victories in life are not the ones where you led from the start. "
            "They are the ones where you were down 3-0, refused to give up, and fought your way back to finish strong.\n\n"
            "Ban Kòrsou! 🇨🇼🌊\n\n"
            "👉 Explore Coach Lornette Daye's official books, keynotes, and executive coaching programs: lornettedaye.com\n\n"
            "#TheBlueWave #Curaçao #TeamCuraçao #HistoricComeback #BanKòrsou #DushiKòrsou #CONCACAF #CaribbeanPride #FinishStrong #BetterPeopleBetterPlayers #CoachLornette #LornetteDaye"
        )
    }
]

def schedule_post(post):
    query = '''
    mutation CreatePost($input: CreatePostInput!) {
        createPost(input: $input) {
            __typename
            ... on PostActionSuccess {
                post {
                    id
                    status
                    dueAt
                }
            }
            ... on LimitReachedError {
                message
            }
            ... on InvalidInputError {
                message
            }
            ... on UnexpectedError {
                message
            }
            ... on UnauthorizedError {
                message
            }
        }
    }
    '''

    asset_payload = []
    if post.get("type") == "video":
        asset_payload.append({
            "video": {
                "url": post["assetUrl"]
            }
        })
    else:
        asset_payload.append({
            "image": {
                "url": post["assetUrl"]
            }
        })

    variables = {
        "input": {
            "channelId": CHANNEL_ID,
            "text": post["text"],
            "schedulingType": "automatic",
            "mode": "customScheduled",
            "dueAt": post["dueAt"],
            "saveToDraft": False,
            "needsApproval": False,
            "assets": asset_payload
        }
    }

    data = json.dumps({"query": query, "variables": variables}).encode('utf-8')
    req = urllib.request.Request(
        'https://api.buffer.com',
        data=data,
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {TOKEN}',
            'User-Agent': 'Mozilla/5.0'
        }
    )

    ctx = ssl._create_unverified_context()
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
            return json.loads(resp.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        retry_after = e.headers.get('Retry-After')
        return {
            "error": str(e),
            "status_code": e.code,
            "retry_after": int(retry_after) if retry_after and retry_after.isdigit() else 60
        }
    except Exception as e:
        return {"error": str(e)}

def main():
    print("=" * 80)
    print("CAMPAIGN: CURAÇAO NATIONAL FOOTBALL TEAM COMEBACK (15 POSTS)")
    print(f"Target Channel: {CHANNEL_ID} (Lornette Daye LinkedIn)")
    print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)

    report_path = os.path.join(os.path.dirname(__file__), "curacao-scheduled-report.json")
    results = {}
    if os.path.exists(report_path):
        try:
            with open(report_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    if item.get("status") in ["scheduled", "success"] and item.get("postId"):
                        results[item["id"]] = item
        except Exception as e:
            print(f"Note: Could not parse existing report: {e}")

    for idx, post in enumerate(posts_data, 1):
        p_id = post["id"]
        p_type = post.get("type", "image").upper()

        if p_id in results and results[p_id].get("postId"):
            print(f"[{idx}/15] [{p_type}] Post #{p_id} already scheduled (Buffer ID: {results[p_id]['postId']}). Skipping.")
            continue

        while True:
            print(f"\n[{idx}/15] [{p_type}] Scheduling: #{p_id} ({post['slot']}) - {post['dueAt']}...")
            print(f"  Asset: {post['assetUrl']}")
            res = schedule_post(post)

            if res.get("status_code") == 429 or "429" in str(res.get("error", "")):
                wait_sec = res.get("retry_after", 60)
                print(f"  [RATE LIMIT] HTTP 429 encountered. Waiting {wait_sec + 5}s...")
                time.sleep(wait_sec + 5)
                continue

            create_post_data = res.get("data", {}).get("createPost", {})
            typename = create_post_data.get("__typename")
            post_obj = create_post_data.get("post")

            if typename == "PostActionSuccess" and post_obj and post_obj.get("id"):
                b_id = post_obj["id"]
                st = post_obj.get("status")
                due = post_obj.get("dueAt")
                print(f"  >>> SUCCESS: Post ID {b_id} scheduled for {due} (status: {st})")
                results[p_id] = {
                    "id": p_id,
                    "type": post["type"],
                    "slot": post["slot"],
                    "dueAt": due,
                    "postId": b_id,
                    "status": st,
                    "assetFile": post["assetFile"],
                    "assetUrl": post["assetUrl"],
                    "cta": post["cta"]
                }
                break
            else:
                err_msg = create_post_data.get("message") or res.get("errors") or res.get("error") or str(res)
                print(f"  >>> ERROR: {err_msg}")
                results[p_id] = {
                    "id": p_id,
                    "type": post["type"],
                    "slot": post["slot"],
                    "dueAt": post["dueAt"],
                    "assetFile": post["assetFile"],
                    "error": err_msg,
                    "status": "failed"
                }
                break

        time.sleep(1.5)

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(list(results.values()), f, indent=2)

    print("\n" + "=" * 80)
    print(f"Execution complete. Report written to {report_path}")
    success_count = sum(1 for r in results.values() if r.get("status") in ["scheduled", "success"])
    print(f"Summary: {success_count}/15 posts scheduled successfully.")
    print("=" * 80)

if __name__ == "__main__":
    main()
