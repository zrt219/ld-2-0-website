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

def get_token():
    t = os.environ.get('BUFFER_ACCESS_TOKEN')
    if t:
        return t
    for env_name in ['.env.local', '.env']:
        p = os.path.join(os.path.dirname(__file__), '..', env_name)
        if os.path.exists(p):
            with open(p, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.startswith('BUFFER_ACCESS_TOKEN='):
                        val = line.strip().split('=', 1)[1].strip()
                        if val:
                            return val
    return 'uR7DeyYk4O9VcFHqPQOnWseUl7BONqA8RZ4CK_03Ci0'

TOKEN = get_token()
CHANNEL_ID = '6a39d30c5ab6d2f1065f5301'  # Lornette Daye LinkedIn

CDN_BASE = 'https://lornettedaye.com/campaigns/curacao-streak'

posts_data = [
    {
        "id": 1,
        "wave": "Wave 1: Fulfilling My Prediction",
        "slot": "Tonight: Friday 8:00 PM MDT (Oct 02, 2026)",
        "dueAt": "2026-10-03T02:00:00.000Z",
        "assetFile": "curacao-streak-01.png",
        "assetUrl": f"{CDN_BASE}/curacao-streak-01.png",
        "cta": "Book Lornette (lornettedaye.com/book) & Buy a Book (lornettedaye.com/books)",
        "text": (
            "AFTER THE WORLD CUP, I TOLD EVERYONE: JUST GIVE THEM TIME. THEY WILL GET BETTER. AND THEY DID: 3 WINS IN A ROW BACK-TO-BACK! 🇨🇼🌊\n\n"
            "When the final whistle blew at the 2026 World Cup, I heard the critics. "
            "I heard the doubters asking if Curaçao had reached its peak on the global stage.\n\n"
            "In my forty years coaching Olympic athletes, I have seen this exact crossroad a hundred times. "
            "When you step onto the world stage for the first time, you do not immediately conquer it. "
            "You absorb the lessons, you test your foundation, and you return home to build.\n\n"
            "I told everyone back then: do not judge this team by a single tournament. "
            "Give them time. Trust their preparation. They will get better.\n\n"
            "Tonight, three consecutive international victories later, Team Curaçao has answered. "
            "Three wins in a row back-to-back-to-back.\n\n"
            "Ban Kòrsou!\n\n"
            "Keep climbing. Finish strong.\n"
            "Lornette\n\n"
            "Bring this exact championship resilience and performance mindset to your leadership team. "
            "Book me for your next keynote or executive retreat: https://lornettedaye.com/book\n\n"
            "Read my official athlete guide, Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #SmallIslandBigDreams #CaribbeanPride #VamosCuraçao #IslandPride #CaribbeanToTheWorld #CONCACAF #ConcacafNationsLeague #WorldCup #WorldCup2026 #FIFAWorldCup #3WinsInARow #WinningStreak #FinishStrong #LornetteDaye #HighPerformance #SportsLeadership"
        )
    },
    {
        "id": 2,
        "wave": "Wave 1: Fulfilling My Prediction",
        "slot": "Day 1: Saturday 9:00 AM MDT (Oct 03, 2026)",
        "dueAt": "2026-10-03T15:00:00.000Z",
        "assetFile": "curacao-streak-02.png",
        "assetUrl": f"{CDN_BASE}/curacao-streak-02.png",
        "cta": "Buy a Book (lornettedaye.com/books) & Book Lornette (lornettedaye.com/book)",
        "text": (
            "WHEN YOU ARE DOWN, THE ONLY PLACE TO GO IS UP. 🇨🇼⚽\n\n"
            "Look at this visual. Look at the brotherhood in that huddle.\n\n"
            "After our World Cup campaign, people wondered how a nation of 160,000 citizens "
            "would respond once the global spotlight shifted. "
            "My answer was simple: just give them time to work. "
            "True champions are forged when nobody is cheering in the quiet months of preparation.\n\n"
            "Three consecutive victories in a row prove what happens when you refuse to let setbacks define you. "
            "Curaçao keeps climbing because their foundation is built on genuine resilience.\n\n"
            "To anyone in business, sport, or life feeling counted out: "
            "your current deficit is merely the setup for your comeback.\n\n"
            "With belief,\n"
            "Lornette\n\n"
            "Build elite mental endurance, focus, and recovery systems. "
            "Get my digital guidebook, Survival Skills for Athletes ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Inquire about keynote speaking and corporate workshops: https://lornettedaye.com/book\n\n"
            "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #SmallIslandBigDreams #CaribbeanPride #VamosCuraçao #IslandPride #CaribbeanToTheWorld #CONCACAF #ConcacafNationsLeague #WorldCup #WorldCup2026 #FIFAWorldCup #3WinsInARow #WinningStreak #FinishStrong #LornetteDaye #HighPerformance #SportsLeadership"
        )
    },
    {
        "id": 3,
        "wave": "Wave 1: Fulfilling My Prediction",
        "slot": "Day 1: Saturday 5:30 PM MDT (Oct 03, 2026)",
        "dueAt": "2026-10-03T23:30:00.000Z",
        "assetFile": "curacao-streak-03.png",
        "assetUrl": f"{CDN_BASE}/curacao-streak-03.png",
        "cta": "Book Lornette (lornettedaye.com/book) & Buy a Book (lornettedaye.com/books)",
        "text": (
            "BUILT THROUGH RESILIENCE: 3 WINS IN A ROW BACK-TO-BACK! 🌊🇨🇼\n\n"
            "Winning once can happen on adrenaline. "
            "Winning twice can be momentum. "
            "Winning three times in a row against international competition is culture.\n\n"
            "When I watched Team Curaçao leave the World Cup stage, I saw a group of men "
            "who tasted the highest level of sport and realized they belonged there. "
            "I reminded everyone who asked me: be patient. Give them time to internalize the standard. "
            "They will get better.\n\n"
            "Today, the results are undeniable. Three straight wins. "
            "A locker room that trusts each other under pressure.\n\n"
            "Ban Kòrsou!\n\n"
            "Stay focused,\n"
            "Lornette\n\n"
            "Bring Olympic team alignment and unshakeable poise to your organization. "
            "Book me for your executive summit or conference: https://lornettedaye.com/book\n\n"
            "Explore my complete digital book library ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #SmallIslandBigDreams #CaribbeanPride #VamosCuraçao #IslandPride #CaribbeanToTheWorld #CONCACAF #ConcacafNationsLeague #WorldCup #WorldCup2026 #FIFAWorldCup #3WinsInARow #WinningStreak #FinishStrong #LornetteDaye #HighPerformance #SportsLeadership"
        )
    },
    {
        "id": 4,
        "wave": "Wave 1: Fulfilling My Prediction",
        "slot": "Day 2: Sunday 9:00 AM MDT (Oct 04, 2026)",
        "dueAt": "2026-10-04T15:00:00.000Z",
        "assetFile": "curacao-streak-04.png",
        "assetUrl": f"{CDN_BASE}/curacao-streak-04.png",
        "cta": "Buy a Book (lornettedaye.com/books) & Book Lornette (lornettedaye.com/book)",
        "text": (
            "PATIENCE IN PLAYER DEVELOPMENT: THE RESULTS ARE HERE 🇨🇼⚡\n\n"
            "In modern sports, everyone wants instant gratification. "
            "People expect immediate dominance without honoring the development curve.\n\n"
            "After the World Cup, I told everyone: give them time. "
            "Athletic maturity requires reps against elite speed. It requires learning how to manage fatigue. "
            "It requires discovering how to play your best when the stadium is hostile.\n\n"
            "Team Curaçao took those lessons, put their heads down, and put together a 3-match winning streak "
            "that has the entire CONCACAF region paying attention.\n\n"
            "Never rush the foundation if you want the house to stand.\n\n"
            "Finish strong,\n"
            "Lornette\n\n"
            "Read my Olympic autobiography, Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Keynote bookings and high-performance leadership consulting: https://lornettedaye.com/book\n\n"
            "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #SmallIslandBigDreams #CaribbeanPride #VamosCuraçao #IslandPride #CaribbeanToTheWorld #CONCACAF #ConcacafNationsLeague #WorldCup #WorldCup2026 #FIFAWorldCup #3WinsInARow #WinningStreak #FinishStrong #LornetteDaye #HighPerformance #SportsLeadership"
        )
    },
    {
        "id": 5,
        "wave": "Wave 1: Fulfilling My Prediction",
        "slot": "Day 2: Sunday 5:30 PM MDT (Oct 04, 2026)",
        "dueAt": "2026-10-04T23:30:00.000Z",
        "assetFile": "curacao-streak-05.png",
        "assetUrl": f"{CDN_BASE}/curacao-streak-05.png",
        "cta": "Book Lornette (lornettedaye.com/book) & Buy a Book (lornettedaye.com/books)",
        "text": (
            "LOCKER ROOM BROTHERHOOD: UNITED IN ONE BLUE WAVE 🇨🇼🤝\n\n"
            "Look at the unity in this squad.\n\n"
            "When you watch Team Curaçao celebrate their third straight win, "
            "you are not looking at eleven individuals chasing personal glory. "
            "You are looking at a united family representing an entire island nation.\n\n"
            "This is what I saw coming after the World Cup: "
            "once this group realized what they could achieve together, no single opponent could intimidate them. "
            "I said give them time, and they gave us three consecutive masterclasses.\n\n"
            "Ban Kòrsou! Where did you celebrate win number three?\n\n"
            "With pride,\n"
            "Lornette\n\n"
            "Bring this exact culture of trust, communication, and unity to your executive team. "
            "Book Lornette for your keynote: https://lornettedaye.com/book\n\n"
            "Order Survival Skills for Athletes ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #SmallIslandBigDreams #CaribbeanPride #VamosCuraçao #IslandPride #CaribbeanToTheWorld #CONCACAF #ConcacafNationsLeague #WorldCup #WorldCup2026 #FIFAWorldCup #3WinsInARow #WinningStreak #FinishStrong #LornetteDaye #HighPerformance #SportsLeadership"
        )
    },
    {
        "id": 6,
        "wave": "Wave 1: Fulfilling My Prediction",
        "slot": "Day 3: Monday 9:00 AM MDT (Oct 05, 2026)",
        "dueAt": "2026-10-05T15:00:00.000Z",
        "assetFile": "curacao-streak-06.png",
        "assetUrl": f"{CDN_BASE}/curacao-streak-06.png",
        "cta": "Buy a Book (lornettedaye.com/books) & Book Lornette (lornettedaye.com/book)",
        "text": (
            "MONDAY MORNING STANDARD: WINNING IS A REPEATABLE DISCIPLINE 🇨🇼🔥\n\n"
            "Start your week with the championship posture of Team Curaçao.\n\n"
            "Three consecutive international wins back-to-back do not happen by chance. "
            "They happen when you respect the process, eliminate excuses, and execute your assignment.\n\n"
            "When critics questioned our post-World Cup trajectory, I stood firm: "
            "give them time, and they will prove their quality. "
            "Now the proof is on the scoreboard for the entire world to witness.\n\n"
            "Whatever mountain you are climbing this week: take it one possession at a time.\n\n"
            "Keep climbing,\n"
            "Lornette\n\n"
            "Equip your mind for high-pressure execution. "
            "Explore my full collection of digital books ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Inquire about corporate leadership retreats and speaking: https://lornettedaye.com/book\n\n"
            "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #SmallIslandBigDreams #CaribbeanPride #VamosCuraçao #IslandPride #CaribbeanToTheWorld #CONCACAF #ConcacafNationsLeague #WorldCup #WorldCup2026 #FIFAWorldCup #3WinsInARow #WinningStreak #FinishStrong #LornetteDaye #HighPerformance #SportsLeadership"
        )
    },
    {
        "id": 7,
        "wave": "Wave 1: Fulfilling My Prediction",
        "slot": "Day 3: Monday 6:00 PM MDT (Oct 05, 2026)",
        "dueAt": "2026-10-06T00:00:00.000Z",
        "assetFile": "curacao-streak-07.png",
        "assetUrl": f"{CDN_BASE}/curacao-streak-07.png",
        "cta": "Book Lornette (lornettedaye.com/book) & Buy a Book (lornettedaye.com/books)",
        "text": (
            "THE BLUE WAVE KEEPS SURGING: 3 STRAIGHT VICTORIES! 🌊🇨🇼\n\n"
            "Three wins in a row back-to-back-to-back.\n\n"
            "Remember where this streak started: trailing 3-0 in San José at halftime. "
            "A lesser team would have crumbled. A team without belief would have pointed fingers.\n\n"
            "Curaçao came back to win 4-3, and they have not stopped winning since. "
            "This is why I told everyone to be patient after the World Cup. "
            "When you build character through fire, the streak takes care of itself.\n\n"
            "Ban Kòrsou!\n\n"
            "Finish strong,\n"
            "Lornette\n\n"
            "Book Lornette Daye for your next keynote, conference, or high-performance workshop: https://lornettedaye.com/book\n\n"
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #SmallIslandBigDreams #CaribbeanPride #VamosCuraçao #IslandPride #CaribbeanToTheWorld #CONCACAF #ConcacafNationsLeague #WorldCup #WorldCup2026 #FIFAWorldCup #3WinsInARow #WinningStreak #FinishStrong #LornetteDaye #HighPerformance #SportsLeadership"
        )
    },
    {
        "id": 8,
        "wave": "Wave 2: What I Saw Change on the Pitch",
        "slot": "Day 4: Tuesday 11:00 AM MDT (Oct 06, 2026)",
        "dueAt": "2026-10-06T17:00:00.000Z",
        "assetFile": "curacao-streak-08.png",
        "assetUrl": f"{CDN_BASE}/curacao-streak-08.png",
        "cta": "Buy a Book (lornettedaye.com/books) & Book Lornette (lornettedaye.com/book)",
        "text": (
            "WORLD CUP AMBITIONS: A SMALL ISLAND ON THE GLOBAL STAGE 🇨🇼🌍\n\n"
            "What changed between the World Cup and this 3-game winning streak?\n\n"
            "I saw the tactical maturity click into place. "
            "When you play against the best in the world, the game slows down for you afterward. "
            "The passes become crisper. The defensive rotations become second nature.\n\n"
            "I told everyone to give them time because you cannot teach international speed on a whiteboard. "
            "You have to experience it, endure it, and grow into it. "
            "That is exactly what Team Curaçao did.\n\n"
            "Small island. Massive execution.\n\n"
            "With belief,\n"
            "Lornette\n\n"
            "Discover the mental habits behind repeatable athletic excellence. "
            "Read Survival Skills for Athletes ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Book Lornette for keynote presentations and executive coaching: https://lornettedaye.com/book\n\n"
            "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #SmallIslandBigDreams #CaribbeanPride #VamosCuraçao #IslandPride #CaribbeanToTheWorld #CONCACAF #ConcacafNationsLeague #WorldCup #WorldCup2026 #FIFAWorldCup #3WinsInARow #WinningStreak #FinishStrong #LornetteDaye #HighPerformance #SportsLeadership"
        )
    },
    {
        "id": 9,
        "wave": "Wave 2: What I Saw Change on the Pitch",
        "slot": "Day 4: Tuesday 7:00 PM MDT (Oct 06, 2026)",
        "dueAt": "2026-10-07T01:00:00.000Z",
        "assetFile": "curacao-streak-09.png",
        "assetUrl": f"{CDN_BASE}/curacao-streak-09.png",
        "cta": "Book Lornette (lornettedaye.com/book) & Buy a Book (lornettedaye.com/books)",
        "text": (
            "WHAT I SAW CHANGE: DICK ADVOCAAT'S TACTICAL MASTERCLASS 🇨🇼🧠\n\n"
            "Coaching at the highest level is not about dramatic speeches. "
            "It is about diagnosis, structural clarity, and calm under fire.\n\n"
            "What Dick Advocaat gave this squad post-World Cup was tactical discipline. "
            "He adjusted the midfield spacing, clarified recovery responsibilities, "
            "and trusted his leaders to execute.\n\n"
            "When I said give them time after the World Cup, I knew that a master tactician like Advocaat "
            "needed fixtures to let his principles sink in. "
            "Three wins later, the tactical identity of Curaçao is clear for all to see.\n\n"
            "Ban Kòrsou!\n\n"
            "Finish strong,\n"
            "Lornette\n\n"
            "Bring Olympic and international coaching principles to your corporate boardroom. "
            "Book Lornette Daye for your next event: https://lornettedaye.com/book\n\n"
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #SmallIslandBigDreams #CaribbeanPride #VamosCuraçao #IslandPride #CaribbeanToTheWorld #CONCACAF #ConcacafNationsLeague #WorldCup #WorldCup2026 #FIFAWorldCup #3WinsInARow #WinningStreak #FinishStrong #LornetteDaye #HighPerformance #SportsLeadership"
        )
    },
    {
        "id": 10,
        "wave": "Wave 2: What I Saw Change on the Pitch",
        "slot": "Day 5: Wednesday 11:00 AM MDT (Oct 07, 2026)",
        "dueAt": "2026-10-07T17:00:00.000Z",
        "assetFile": "curacao-streak-10.png",
        "assetUrl": f"{CDN_BASE}/curacao-streak-10.png",
        "cta": "Buy a Book (lornettedaye.com/books) & Book Lornette (lornettedaye.com/book)",
        "text": (
            "PLAYING YOUR BEST WHEN IT MATTERS MOST 🇨🇼🏆\n\n"
            "In four decades around elite athletes, I have noticed that good players perform when conditions are perfect. "
            "Great players perform when everything is on the line.\n\n"
            "Across these three consecutive wins, Team Curaçao has displayed cold-blooded poise in high-leverage moments. "
            "Whether defending a lead in stoppage time or converting clinical chances, their nerve held steady.\n\n"
            "This is the payoff of patience. This is why I urged everyone: give them time. "
            "Poise under pressure is an earned asset, and Curaçao has earned it.\n\n"
            "Keep climbing,\n"
            "Lornette\n\n"
            "Learn how to master your thoughts under supreme competitive pressure. "
            "Get Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Book Lornette for keynote speaking and high-performance retreats: https://lornettedaye.com/book\n\n"
            "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #SmallIslandBigDreams #CaribbeanPride #VamosCuraçao #IslandPride #CaribbeanToTheWorld #CONCACAF #ConcacafNationsLeague #WorldCup #WorldCup2026 #FIFAWorldCup #3WinsInARow #WinningStreak #FinishStrong #LornetteDaye #HighPerformance #SportsLeadership"
        )
    },
    {
        "id": 11,
        "wave": "Wave 2: What I Saw Change on the Pitch",
        "slot": "Day 5: Wednesday 7:00 PM MDT (Oct 07, 2026)",
        "dueAt": "2026-10-08T01:00:00.000Z",
        "assetFile": "curacao-streak-11.png",
        "assetUrl": f"{CDN_BASE}/curacao-streak-11.png",
        "cta": "Book Lornette (lornettedaye.com/book) & Buy a Book (lornettedaye.com/books)",
        "text": (
            "COMPOSURE IN THE HEAT OF INTERNATIONAL COMPETITION 🇨🇼⚡\n\n"
            "Look at the calm focus in this visual.\n\n"
            "When you play away from home against established regional powers, the environment is designed to rattle you. "
            "Hostile crowds, physical fouls, unpredictable momentum swings.\n\n"
            "What separates Team Curaçao today from six months ago is emotional regulation. "
            "They do not retaliate. They do not lose their shape. They let their football answer.\n\n"
            "I saw this evolution coming when I told everyone to give them time. "
            "Three wins in a row are the direct fruit of emotional discipline.\n\n"
            "Ban Kòrsou!\n\n"
            "Stay composed,\n"
            "Lornette\n\n"
            "Bring Olympic-caliber mental conditioning to your organization. "
            "Book Lornette for your next conference: https://lornettedaye.com/book\n\n"
            "Explore Survival Skills for Athletes ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #SmallIslandBigDreams #CaribbeanPride #VamosCuraçao #IslandPride #CaribbeanToTheWorld #CONCACAF #ConcacafNationsLeague #WorldCup #WorldCup2026 #FIFAWorldCup #3WinsInARow #WinningStreak #FinishStrong #LornetteDaye #HighPerformance #SportsLeadership"
        )
    },
    {
        "id": 12,
        "wave": "Wave 2: What I Saw Change on the Pitch",
        "slot": "Day 6: Thursday 11:00 AM MDT (Oct 08, 2026)",
        "dueAt": "2026-10-08T17:00:00.000Z",
        "assetFile": "curacao-streak-12.png",
        "assetUrl": f"{CDN_BASE}/curacao-streak-12.png",
        "cta": "Buy a Book (lornettedaye.com/books) & Book Lornette (lornettedaye.com/book)",
        "text": (
            "FROM UNDERDOGS TO FRONT-RUNNERS: THE PSYCHOLOGICAL SHIFT 🇨🇼🎯\n\n"
            "The hardest transition in sports is moving from a plucky underdog to a squad that expects to win.\n\n"
            "When you are an underdog, you play with house money. "
            "When you are on a 3-game winning streak, every opponent circles you on their calendar.\n\n"
            "Team Curaçao has welcomed that pressure. "
            "They carry the confidence of having proved themselves on the world stage, "
            "just as I predicted when I told everyone to give them time after the World Cup.\n\n"
            "Never apologize for growing into your power.\n\n"
            "Finish strong,\n"
            "Lornette\n\n"
            "Equip yourself with the tools to navigate high expectations and leadership pressure. "
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Inquire about executive coaching and keynote speaking: https://lornettedaye.com/book\n\n"
            "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #SmallIslandBigDreams #CaribbeanPride #VamosCuraçao #IslandPride #CaribbeanToTheWorld #CONCACAF #ConcacafNationsLeague #WorldCup #WorldCup2026 #FIFAWorldCup #3WinsInARow #WinningStreak #FinishStrong #LornetteDaye #HighPerformance #SportsLeadership"
        )
    },
    {
        "id": 13,
        "wave": "Wave 2: What I Saw Change on the Pitch",
        "slot": "Day 6: Thursday 7:00 PM MDT (Oct 08, 2026)",
        "dueAt": "2026-10-09T01:00:00.000Z",
        "assetFile": "curacao-streak-13.png",
        "assetUrl": f"{CDN_BASE}/curacao-streak-13.png",
        "cta": "Book Lornette (lornettedaye.com/book) & Buy a Book (lornettedaye.com/books)",
        "text": (
            "THE SCIENCE OF CONSISTENCY: 3 WINS BACK-TO-BACK-TO-BACK 🌊🇨🇼\n\n"
            "In elite performance, consistency is the ultimate currency.\n\n"
            "Anyone can have a hot afternoon. But stringing together three consecutive victories "
            "across travel, tactical adjustments, and varying opponents requires systems.\n\n"
            "I told everyone after the World Cup to give this team time, "
            "because building reliable routines takes patience. "
            "Now the routines are locked in, and the wins are following.\n\n"
            "Ban Kòrsou!\n\n"
            "With respect,\n"
            "Lornette\n\n"
            "Bring championship consistency to your executive team. "
            "Book Lornette Daye for your leadership keynote: https://lornettedaye.com/book\n\n"
            "Order Survival Skills for Athletes ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #SmallIslandBigDreams #CaribbeanPride #VamosCuraçao #IslandPride #CaribbeanToTheWorld #CONCACAF #ConcacafNationsLeague #WorldCup #WorldCup2026 #FIFAWorldCup #3WinsInARow #WinningStreak #FinishStrong #LornetteDaye #HighPerformance #SportsLeadership"
        )
    },
    {
        "id": 14,
        "wave": "Wave 3: What This Teaches Us About Leadership and Life",
        "slot": "Day 7: Friday 11:00 AM MDT (Oct 09, 2026)",
        "dueAt": "2026-10-09T17:00:00.000Z",
        "assetFile": "curacao-streak-14.png",
        "assetUrl": f"{CDN_BASE}/curacao-streak-14.png",
        "cta": "Buy a Book (lornettedaye.com/books) & Book Lornette (lornettedaye.com/book)",
        "text": (
            "DIASPORA ROAR: FROM WILLEMSTAD TO AMSTERDAM 🇨🇼🌍\n\n"
            "When Team Curaçao wins, you feel the celebration across oceans.\n\n"
            "From Punda and Otrobanda to Rotterdam, Amsterdam, Miami, and Toronto, "
            "our community stands taller. "
            "Sport has the rare power to bridge miles and remind us who we are.\n\n"
            "This 3-win streak is not just for the athletes on the pitch. "
            "It is for every parent, mentor, and supporter who kept the faith when I said: "
            "just give them time. They will get better. And they did.\n\n"
            "Nos ta Kòrsou!\n\n"
            "Proudly,\n"
            "Lornette\n\n"
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Keynote bookings and high-performance retreats: https://lornettedaye.com/book\n\n"
            "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #SmallIslandBigDreams #CaribbeanPride #VamosCuraçao #IslandPride #CaribbeanToTheWorld #CONCACAF #ConcacafNationsLeague #WorldCup #WorldCup2026 #FIFAWorldCup #3WinsInARow #WinningStreak #FinishStrong #LornetteDaye #HighPerformance #SportsLeadership"
        )
    },
    {
        "id": 15,
        "wave": "Wave 3: What This Teaches Us About Leadership and Life",
        "slot": "Day 7: Friday 7:00 PM MDT (Oct 09, 2026)",
        "dueAt": "2026-10-10T01:00:00.000Z",
        "assetFile": "curacao-streak-15.png",
        "assetUrl": f"{CDN_BASE}/curacao-streak-15.png",
        "cta": "Book Lornette (lornettedaye.com/book) & Buy a Book (lornettedaye.com/books)",
        "text": (
            "WEEKEND CELEBRATION: CARIBBEAN POWER ON DISPLAY 🇨🇼🌴\n\n"
            "Let this 3-game winning streak be a reminder to every Caribbean nation:\n\n"
            "Our potential is limitless. "
            "When we invest in development, protect our youth, and demand excellence, "
            "we can compete with anyone on this planet.\n\n"
            "I told the world to give Curaçao time after the World Cup because I know the heart of our athletes. "
            "Three consecutive wins later, the message is loud and clear.\n\n"
            "Ban Kòrsou! Celebrate this milestone with pride this weekend.\n\n"
            "With warmth,\n"
            "Lornette\n\n"
            "Book Lornette Daye for your corporate summit, university lecture, or athletic banquet: https://lornettedaye.com/book\n\n"
            "Explore all digital books ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #SmallIslandBigDreams #CaribbeanPride #VamosCuraçao #IslandPride #CaribbeanToTheWorld #CONCACAF #ConcacafNationsLeague #WorldCup #WorldCup2026 #FIFAWorldCup #3WinsInARow #WinningStreak #FinishStrong #LornetteDaye #HighPerformance #SportsLeadership"
        )
    },
    {
        "id": 16,
        "wave": "Wave 3: What This Teaches Us About Leadership and Life",
        "slot": "Day 8: Saturday 10:00 AM MDT (Oct 10, 2026)",
        "dueAt": "2026-10-10T16:00:00.000Z",
        "assetFile": "curacao-streak-16.png",
        "assetUrl": f"{CDN_BASE}/curacao-streak-16.png",
        "cta": "Buy a Book (lornettedaye.com/books) & Book Lornette (lornettedaye.com/book)",
        "text": (
            "GENERATIONAL INSPIRATION FOR THE YOUTH OF KÒRSOU 🇨🇼✨\n\n"
            "The greatest victory is not the three points on the table. "
            "It is the young boy or girl in Willemstad watching their heroes and saying: 'I can do that too.'\n\n"
            "When I said give them time after the World Cup, I was thinking about legacy. "
            "Patience teaches our next generation that greatness does not require magic; "
            "it requires showing up, working through disappointment, and trusting your preparation.\n\n"
            "Three wins in a row back-to-back have planted seeds that will bloom for decades.\n\n"
            "Finish strong,\n"
            "Lornette\n\n"
            "Equip your young athletes with championship mental habits. "
            "Order Survival Skills for Athletes ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Inquire about youth leadership mentorship and speaking: https://lornettedaye.com/book\n\n"
            "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #SmallIslandBigDreams #CaribbeanPride #VamosCuraçao #IslandPride #CaribbeanToTheWorld #CONCACAF #ConcacafNationsLeague #WorldCup #WorldCup2026 #FIFAWorldCup #3WinsInARow #WinningStreak #FinishStrong #LornetteDaye #HighPerformance #SportsLeadership"
        )
    },
    {
        "id": 17,
        "wave": "Wave 3: What This Teaches Us About Leadership and Life",
        "slot": "Day 8: Saturday 5:00 PM MDT (Oct 10, 2026)",
        "dueAt": "2026-10-10T23:00:00.000Z",
        "assetFile": "curacao-streak-17.png",
        "assetUrl": f"{CDN_BASE}/curacao-streak-17.png",
        "cta": "Book Lornette (lornettedaye.com/book) & Buy a Book (lornettedaye.com/books)",
        "text": (
            "BETTER PEOPLE · BETTER PLAYERS: AUTHENTIC TEAM CULTURE 🇨🇼🤝\n\n"
            "You cannot build a winning streak on broken relationships.\n\n"
            "In four decades coaching Olympic athletes, this has remained my non-negotiable rule: "
            "better people make better players. "
            "When Team Curaçao faced adversity after the World Cup, they did not fracture. "
            "They grew closer. They protected each other. They held each other accountable.\n\n"
            "That is why they won three straight matches. Culture always reveals itself under pressure.\n\n"
            "Ban Kòrsou!\n\n"
            "With belief,\n"
            "Lornette\n\n"
            "Bring this transformative culture framework to your executive team. "
            "Book Lornette Daye for your leadership keynote: https://lornettedaye.com/book\n\n"
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #SmallIslandBigDreams #CaribbeanPride #VamosCuraçao #IslandPride #CaribbeanToTheWorld #CONCACAF #ConcacafNationsLeague #WorldCup #WorldCup2026 #FIFAWorldCup #3WinsInARow #WinningStreak #FinishStrong #LornetteDaye #HighPerformance #SportsLeadership"
        )
    },
    {
        "id": 18,
        "wave": "Wave 3: What This Teaches Us About Leadership and Life",
        "slot": "Day 9: Sunday 10:00 AM MDT (Oct 11, 2026)",
        "dueAt": "2026-10-11T16:00:00.000Z",
        "assetFile": "curacao-streak-18.png",
        "assetUrl": f"{CDN_BASE}/curacao-streak-18.png",
        "cta": "Buy a Book (lornettedaye.com/books) & Book Lornette (lornettedaye.com/book)",
        "text": (
            "SUNDAY LEGACY REFLECTION: PRIDE THAT CROSSES OCEANS 🇨🇼⚓\n\n"
            "Reflecting this Sunday morning on what this 3-win streak means.\n\n"
            "It means that when you are faithful in the small details, the breakthrough will come. "
            "It means that when you give people time to grow, they surprise everyone who doubted them.\n\n"
            "I said it after the World Cup, and I say it again today: "
            "Team Curaçao is showing the entire sporting world what authentic resilience looks like in motion.\n\n"
            "Hold your heads high. The Blue Wave is rolling forward.\n\n"
            "Keep climbing,\n"
            "Lornette\n\n"
            "Build lasting resilience in your personal and professional journey. "
            "Explore my digital book catalog ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Inquire about executive coaching and keynote speaking: https://lornettedaye.com/book\n\n"
            "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #SmallIslandBigDreams #CaribbeanPride #VamosCuraçao #IslandPride #CaribbeanToTheWorld #CONCACAF #ConcacafNationsLeague #WorldCup #WorldCup2026 #FIFAWorldCup #3WinsInARow #WinningStreak #FinishStrong #LornetteDaye #HighPerformance #SportsLeadership"
        )
    },
    {
        "id": 19,
        "wave": "Wave 3: What This Teaches Us About Leadership and Life",
        "slot": "Day 9: Sunday 5:00 PM MDT (Oct 11, 2026)",
        "dueAt": "2026-10-11T23:00:00.000Z",
        "assetFile": "curacao-streak-19.png",
        "assetUrl": f"{CDN_BASE}/curacao-streak-19.png",
        "cta": "Book Lornette (lornettedaye.com/book) & Buy a Book (lornettedaye.com/books)",
        "text": (
            "GRAND FINALE: BAN KÒRSOU! FINISH STRONG! 🇨🇼🏆\n\n"
            "To every player, coach, and supporter of Team Curaçao:\n\n"
            "Thank you for proving that patience, courage, and discipline always triumph in the end. "
            "Three wins in a row back-to-back-to-back.\n\n"
            "I told everyone to give you time after the World Cup, and you delivered a masterclass. "
            "Remember this feeling as you prepare for the next chapter. "
            "Your previous victory cannot win your next fixture. Stay humble. Stay hungry. Finish strong.\n\n"
            "Ban Kòrsou! Nos ta Kòrsou forever.\n\n"
            "With immense pride,\n"
            "Lornette\n\n"
            "Bring Olympic-caliber leadership and championship focus to your organization. "
            "Book Lornette Daye for your next keynote or retreat: https://lornettedaye.com/book\n\n"
            "Explore my complete digital book library ($14.99 CAD each): https://lornettedaye.com/books\n\n"
            "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #SmallIslandBigDreams #CaribbeanPride #VamosCuraçao #IslandPride #CaribbeanToTheWorld #CONCACAF #ConcacafNationsLeague #WorldCup #WorldCup2026 #FIFAWorldCup #3WinsInARow #WinningStreak #FinishStrong #LornetteDaye #HighPerformance #SportsLeadership"
        )
    }
]

def check_for_em_dashes():
    errors = []
    for p in posts_data:
        t = p["text"]
        if "—" in t or "&mdash;" in t or "\u2014" in t:
            errors.append(f"Post {p['id']} contains an em dash!")
    if errors:
        for err in errors:
            print("ERROR:", err)
        sys.exit(1)
    print("EM DASH CHECK: PASS (Zero em dashes found across all 19 streak posts).")

def check_first_person_and_signature():
    errors = []
    for p in posts_data:
        t = p["text"]
        if "Coach Lornette\n" in t or "Coach Lornette " in t:
            errors.append(f"Post {p['id']} signed with 'Coach Lornette' instead of 'Lornette'!")
        if "Lornette\n" not in t:
            errors.append(f"Post {p['id']} missing signature 'Lornette'!")
    if errors:
        for err in errors:
            print("SIGNATURE ERROR:", err)
        sys.exit(1)
    print("SIGNATURE CHECK: PASS (All posts strictly signed as 'Lornette').")

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

    variables = {
        "input": {
            "channelId": CHANNEL_ID,
            "text": post["text"],
            "schedulingType": "automatic",
            "mode": "customScheduled",
            "dueAt": post["dueAt"],
            "saveToDraft": False,
            "needsApproval": False,
            "assets": [
                {
                    "image": {
                        "url": post["assetUrl"]
                    }
                }
            ]
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
    print("=" * 75)
    print("STARTING CURAÇAO 3-WIN STREAK CAMPAIGN (19 POSTS - WRITTEN BY LORNETTE)")
    print("=" * 75)

    check_for_em_dashes()
    check_first_person_and_signature()

    report_path = os.path.join(os.path.dirname(__file__), "curacao-streak-scheduled-report.json")
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

        if p_id in results and results[p_id].get("postId"):
            print(f"[{idx}/19] Post #{p_id} already scheduled (Buffer ID: {results[p_id]['postId']}). Skipping.")
            continue

        while True:
            print(f"\n[{idx}/19] Scheduling Post #{p_id} ({post['slot']}) - Due: {post['dueAt']}...")
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
                    "wave": post["wave"],
                    "type": "image",
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
                    "wave": post["wave"],
                    "type": "image",
                    "slot": post["slot"],
                    "dueAt": post["dueAt"],
                    "assetFile": post["assetFile"],
                    "error": err_msg,
                    "status": "failed"
                }
                break

        time.sleep(2)

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(list(results.values()), f, indent=2, ensure_ascii=False)

    print("\n" + "=" * 75)
    print(f"Execution complete. Report written to {report_path}")
    success_count = sum(1 for r in results.values() if r.get("status") in ["scheduled", "success"])
    print(f"Summary: {success_count}/19 posts scheduled successfully.")

if __name__ == "__main__":
    main()
