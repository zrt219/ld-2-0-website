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
        "slot": "Day 1: Saturday 12:30 PM MDT (Sep 26, 2026)",
        "dueAt": "2026-09-26T18:30:00.000Z",
        "assetFile": "curacao-ad-01.png",
        "assetUrl": f"{CDN_BASE}/curacao-ad-01.png",
        "cta": "Finish Strong: Chasing the Olympic Dream ($14.99 CAD) & Speaking",
        "text": (
            "IF YOU TURNED IT OFF AT 3-0, YOU MISSED HISTORY. 🇨🇼🌊\n\n"
            "Costa Rica 3, Curaçao 0 at the interval.\n"
            "Down three goals on the road in San José against a regional titan. "
            "Human nature says minimize damage and ride out the second half. "
            "Olympic-caliber culture says step onto the pitch and alter your reality.\n\n"
            "Four unanswered goals later, Team Curaçao proved that your past 45 minutes "
            "never dictate what you are capable of achieving in the next 45.\n\n"
            "In forty years coaching Olympic contenders, this is the exact principle that separates "
            "champions from participants: belief is an active discipline.\n\n"
            "Ban Kòrsou!\n\n"
            "Discover the mindset that turns steep deficits into historic milestones. "
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Keynote bookings and high-performance leadership consulting: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #SmallIslandBigDreams #CaribbeanPride #VamosCuraçao #FinishStrong #LornetteDaye"
        )
    },
    {
        "id": 2,
        "slot": "Day 1: Saturday 7:15 PM MDT (Sep 26, 2026)",
        "dueAt": "2026-09-27T01:15:00.000Z",
        "assetFile": "curacao-ad-02.png",
        "assetUrl": f"{CDN_BASE}/curacao-ad-02.png",
        "cta": "Survival Skills for Athletes ($14.99 CAD) & Speaking",
        "text": (
            "THE BLUE WAVE DID NOT BREAK. IT GREW BIGGER. 🌊🇨🇼\n\n"
            "Away win in Costa Rica: from 3-0 down to full-time winners.\n\n"
            "When pressure intensifies, ordinary teams scramble and panic. "
            "Championship teams lean into their identity and execute with sharper focus. "
            "Team Curaçao did not let the scoreboard break their posture. "
            "They adjusted their pressing triggers, dominated the middle third, and took control of the match.\n\n"
            "This is what high-performance poise looks like under intense international pressure.\n\n"
            "To every athlete, entrepreneur, and leader facing a steep deficit: "
            "let this match remind you that pressure is only a question of who keeps their composure.\n\n"
            "Master focus, emotional regulation, and competitive consistency. "
            "Explore Survival Skills for Athletes ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Bring Olympic-caliber mental conditioning to your organization: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueAndProud #CuraçaoRising #BanKòrsou #CuraçaoFootball #CaribbeanSports #IslandFootball #SmallIslandBigDreams #CaribbeanExcellence #LornetteDaye"
        )
    },
    {
        "id": 3,
        "slot": "Day 2: Sunday 12:30 PM MDT (Sep 27, 2026)",
        "dueAt": "2026-09-27T18:30:00.000Z",
        "assetFile": "curacao-ad-03.png",
        "assetUrl": f"{CDN_BASE}/curacao-ad-03.png",
        "cta": "Executive Keynote Speaking & Books",
        "text": (
            "SUNDAY MORNING BLUEPRINT: REFUSING TO ACCEPT LIMITATIONS 🇨🇼⚡\n\n"
            "A nation of 160,000 citizens going toe-to-toe with global football heritage and walking away victorious.\n\n"
            "Geographic size has never determined athletic capability. "
            "Resources never dictate heart. "
            "When preparation meets unshakeable collective belief, barriers dissolve.\n\n"
            "Every player wearing the blue kit in San José represented decades of diaspora ambition, "
            "family sacrifice, and cultural pride.\n\n"
            "Nos ta Kòrsou! Where were you when that winning goal hit the back of the net?\n\n"
            "Bring Olympic resilience and elite team alignment to your leadership summit. "
            "Explore keynote speaking with Coach Lornette Daye: https://lornettedaye.com/speaking\n\n"
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "#Curaçao #Curacao #Korsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #CaribbeanPower #CaribbeanToTheWorld #SmallIslandBigDreams #LornetteDaye"
        )
    },
    {
        "id": 4,
        "slot": "Day 2: Sunday 7:15 PM MDT (Sep 27, 2026)",
        "dueAt": "2026-09-28T01:15:00.000Z",
        "assetFile": "curacao-ad-04.png",
        "assetUrl": f"{CDN_BASE}/curacao-ad-04.png",
        "cta": "Finish Strong: Chasing the Olympic Dream ($14.99 CAD) & Speaking",
        "text": (
            "THE ARCHITECTURE OF AN IMPOSSIBLE COMEBACK 🇨🇼🎯\n\n"
            "How do you score four unanswered goals against Costa Rica on their home soil?\n\n"
            "1. You refuse emotional surrender at the half.\n"
            "2. You clarify tactical execution instead of complaining about the past.\n"
            "3. You celebrate every small breakthrough as momentum builds.\n"
            "4. You finish ruthlessly when the opportunity presents itself.\n\n"
            "In elite sport and business alike, greatness is never accidental. "
            "It is structured, intentional, and anchored in deep self-worth.\n\n"
            "Equip your mindset with four decades of Olympic wisdom. "
            "Order Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Executive coaching and performance retreats: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueAndProud #CuraçaoRising #VamosCuraçao #CuraçaoFootball #CaribbeanPride #IslandPride #SmallIslandBigDreams #CaribbeanAthletes #LornetteDaye"
        )
    },
    {
        "id": 5,
        "slot": "Day 3: Monday 12:30 PM MDT (Sep 28, 2026)",
        "dueAt": "2026-09-28T18:30:00.000Z",
        "assetFile": "curacao-ad-05.png",
        "assetUrl": f"{CDN_BASE}/curacao-ad-05.png",
        "cta": "Survival Skills for Athletes ($14.99 CAD) & Speaking",
        "text": (
            "MONDAY DRIVE: YOUR PAST DEFICIT CANNOT PREVENT YOUR FUTURE TRIUMPH 🌊🇨🇼\n\n"
            "Enter your work week with the exact mentality Team Curaçao brought out of the tunnel at halftime.\n\n"
            "Down 3-0. No excuses. No hesitation. Pure execution.\n\n"
            "Whatever challenges, targets, or setbacks you are confronting today: "
            "remember that champions do not wait for ideal conditions. They create momentum by taking immediate action.\n\n"
            "Ban Kòrsou! What goal are you conquering this week?\n\n"
            "Build unwavering mental discipline on and off the field. "
            "Read Survival Skills for Athletes ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Keynotes for high-stakes leadership teams: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #CaribbeanExcellence #SmallIslandBigDreams #IslandFootball #LornetteDaye"
        )
    },
    {
        "id": 6,
        "slot": "Day 3: Monday 7:15 PM MDT (Sep 28, 2026)",
        "dueAt": "2026-09-29T01:15:00.000Z",
        "assetFile": "curacao-ad-06.png",
        "assetUrl": f"{CDN_BASE}/curacao-ad-06.png",
        "cta": "Olympic Mindset Consulting & Books",
        "text": (
            "KENJI GORRÉ: THE ANATOMY OF A SECOND HALF BRACE 🇨🇼⚽\n\n"
            "When your team needs an offensive spark under heavy pressure, "
            "you do not hope for magic. You demand the ball and execute.\n\n"
            "Kenji Gorré stepped up when it mattered most, slicing the Costa Rican defense "
            "and scoring twice to level the psychological balance of the entire nation.\n\n"
            "True leaders take personal accountability in critical moments.\n\n"
            "Tag an athlete or colleague who always steps up when the game is on the line!\n\n"
            "Learn how Olympic athletes train their mind for high-stakes moments. "
            "Explore Coach Lornette Daye's digital books ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Corporate workshops and keynotes: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueAndProud #CuraçaoRising #BanKòrsou #CuraçaoFootball #CaribbeanPride #CaribbeanToTheWorld #SmallIslandBigDreams #CaribbeanPower #LornetteDaye"
        )
    },
    {
        "id": 7,
        "slot": "Day 4: Tuesday 12:30 PM MDT (Sep 29, 2026)",
        "dueAt": "2026-09-29T18:30:00.000Z",
        "assetFile": "curacao-ad-07.png",
        "assetUrl": f"{CDN_BASE}/curacao-ad-07.png",
        "cta": "Finish Strong: Chasing the Olympic Dream ($14.99 CAD) & Speaking",
        "text": (
            "TAHITH CHONG: SHIFTING THE GRAVITY OF THE MATCH 🇨🇼✨\n\n"
            "World-class vision, spatial awareness, and pristine technical execution.\n\n"
            "Tahith Chong showed why composure is the ultimate weapon in hostile environments. "
            "He controlled the tempo, unlocked passing lanes, and delivered the breakthrough "
            "that convinced everyone in San José that Curaçao was taking all three points.\n\n"
            "When you possess clarity of purpose, hostile noise becomes background static.\n\n"
            "Ban Kòrsou! Share your favorite Chong play in the comments below!\n\n"
            "Build elite mental clarity and poise under tournament pressure. "
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Book Lornette Daye for your next conference: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #Curacao #Korsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #SmallIslandBigDreams #CaribbeanPride #VamosCuraçao #IslandPride #CaribbeanToTheWorld #LornetteDaye"
        )
    },
    {
        "id": 8,
        "slot": "Day 4: Tuesday 7:15 PM MDT (Sep 29, 2026)",
        "dueAt": "2026-09-30T01:15:00.000Z",
        "assetFile": "curacao-ad-08.png",
        "assetUrl": f"{CDN_BASE}/curacao-ad-08.png",
        "cta": "Survival Skills for Athletes ($14.99 CAD) & Speaking",
        "text": (
            "JORDI PAULINA: THE 88TH MINUTE WINNER 🇨🇼🔥\n\n"
            "88 minutes played. Legs burning. Lungs gasping for air. The score tied 3-3.\n\n"
            "A comfortable draw away against Costa Rica would have earned praise across the region. "
            "But Jordi Paulina and Team Curaçao did not travel to Central America for a moral victory. "
            "They came for the win.\n\n"
            "Paulina's clinical finish in the 88th minute sealed one of the greatest comebacks "
            "in international football history.\n\n"
            "Refuse good enough when greatness is within reach.\n\n"
            "Develop championship grit and late-game finishing focus. "
            "Read Survival Skills for Athletes ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Keynote speaking inquiries: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueAndProud #CuraçaoRising #BanKòrsou #CuraçaoFootball #CaribbeanSports #IslandFootball #SmallIslandBigDreams #CaribbeanExcellence #LornetteDaye"
        )
    },
    {
        "id": 9,
        "slot": "Day 5: Wednesday 12:30 PM MDT (Sep 30, 2026)",
        "dueAt": "2026-09-30T18:30:00.000Z",
        "assetFile": "curacao-ad-09.png",
        "assetUrl": f"{CDN_BASE}/curacao-ad-09.png",
        "cta": "Executive Keynote Speaking & Books",
        "text": (
            "DICK ADVOCAAT: TACTICAL LEADERSHIP IN TIMES OF CRISIS 🇨🇼🧠\n\n"
            "When your squad trails 0-3 on hostile territory at halftime, leadership reveals its true nature.\n\n"
            "Panic coaches scream and assign blame. "
            "Master tacticians provide clarity, structural corrections, and unshakable belief.\n\n"
            "Dick Advocaat and his technical staff diagnosed the flaws, reorganized the pressing lines, "
            "and unleashed the Blue Wave in the second half.\n\n"
            "Crisis management is never about emotional volume. It is about strategic composure.\n\n"
            "Bring Olympic and international coaching principles to your executive team. "
            "Explore keynote speaking with Coach Lornette Daye: https://lornettedaye.com/speaking\n\n"
            "Read Coach Lornette's digital guides ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "#Curaçao #Curacao #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #CaribbeanPower #CaribbeanToTheWorld #SmallIslandBigDreams #LornetteDaye"
        )
    },
    {
        "id": 10,
        "slot": "Day 5: Wednesday 7:15 PM MDT (Sep 30, 2026)",
        "dueAt": "2026-10-01T01:15:00.000Z",
        "assetFile": "curacao-ad-10.png",
        "assetUrl": f"{CDN_BASE}/curacao-ad-10.png",
        "cta": "Finish Strong: Chasing the Olympic Dream ($14.99 CAD) & Speaking",
        "text": (
            "DIASPORA PRIDE FROM WILLEMSTAD TO AMSTERDAM 🇨🇼🌍\n\n"
            "When the final whistle blew in San José, the celebration rippled across continents.\n\n"
            "From Punda and Otrobanda to Rotterdam, Amsterdam, Miami, and Toronto, "
            "Curaçaoans stood as one unified community.\n\n"
            "Sport connects heritage, pride, and family like nothing else on earth. "
            "This victory belongs to every person who carries the blue and yellow flag in their heart.\n\n"
            "Drop your flag in the comments if you stand with Team Curaçao!\n\n"
            "Ban Kòrsou!\n\n"
            "Turn family, community, and heritage into your greatest performance fuel. "
            "Discover Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Executive leadership retreats with Coach Lornette Daye: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueAndProud #CuraçaoRising #VamosCuraçao #CuraçaoFootball #CaribbeanPride #IslandPride #SmallIslandBigDreams #CaribbeanAthletes #LornetteDaye"
        )
    },
    {
        "id": 11,
        "slot": "Day 6: Thursday 12:30 PM MDT (Oct 01, 2026)",
        "dueAt": "2026-10-01T18:30:00.000Z",
        "assetFile": "curacao-ad-11.png",
        "assetUrl": f"{CDN_BASE}/curacao-ad-11.png",
        "cta": "Survival Skills for Athletes ($14.99 CAD) & Speaking",
        "text": (
            "WELCOME TO OCTOBER: RIDE THE BLUE WAVE ALL MONTH LONG 🇨🇼🌊\n\n"
            "A new month brings fresh opportunities, bigger targets, and new challenges to conquer.\n\n"
            "Take the spirit of Team Curaçao into every room you enter this month: "
            "no matter where you find yourself on the scoreboard, refuse to accept defeat.\n\n"
            "Four goals. Zero excuses. Historic triumph.\n\n"
            "Ban Kòrsou! What milestone are you finishing strong this month?\n\n"
            "Build elite mental endurance, discipline systems, and focus. "
            "Explore Survival Skills for Athletes ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Book Coach Lornette Daye for your October leadership event: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #CaribbeanExcellence #SmallIslandBigDreams #IslandFootball #LornetteDaye"
        )
    },
    {
        "id": 12,
        "slot": "Day 6: Thursday 7:15 PM MDT (Oct 01, 2026)",
        "dueAt": "2026-10-02T01:15:00.000Z",
        "assetFile": "curacao-ad-12.png",
        "assetUrl": f"{CDN_BASE}/curacao-ad-12.png",
        "cta": "Olympic Mindset Consulting & Books",
        "text": (
            "MORE STORIES BEHIND SPORT: PERFORMANCE. RESILIENCE. PURPOSE. 🇨🇼🏆\n\n"
            "At LornetteDaye.com, we go far beyond match highlights and box scores.\n\n"
            "We examine the psychological, cultural, and spiritual foundations "
            "that allow athletes to perform at their best when pressure is at its peak.\n\n"
            "Team Curaçao's 4-3 comeback in Costa Rica is living proof that preparation, "
            "emotional poise, and brotherhood create outcomes that statistics can never predict.\n\n"
            "Explore deep-dive analysis, leadership wisdom, and championship guides: https://lornettedaye.com\n\n"
            "Executive coaching and keynote speaking inquiries: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueAndProud #CuraçaoRising #BanKòrsou #CuraçaoFootball #CaribbeanSports #IslandFootball #SmallIslandBigDreams #CaribbeanExcellence #LornetteDaye"
        )
    },
    {
        "id": 13,
        "slot": "Day 7: Friday 12:30 PM MDT (Oct 02, 2026)",
        "dueAt": "2026-10-02T18:30:00.000Z",
        "assetFile": "curacao-ad-13.png",
        "assetUrl": f"{CDN_BASE}/curacao-ad-13.png",
        "cta": "Finish Strong: Chasing the Olympic Dream ($14.99 CAD) & Speaking",
        "text": (
            "FRIDAY LUNCH REFLECTION: BETTER PEOPLE MAKE BETTER PLAYERS 🇨🇼🤝\n\n"
            "In four decades of elite Olympic coaching, one core truth stands above all others: "
            "you cannot build a championship squad with fragmented character.\n\n"
            "When Team Curaçao went down 3-0, they did not turn against each other. "
            "They doubled down on mutual trust, covered for one another's runs, and communicated with respect.\n\n"
            "Culture beats talent when talent refuses to unite.\n\n"
            "Ban Kòrsou! Tag a teammate who always elevates the culture around them!\n\n"
            "Learn the character principles that build lasting championship teams. "
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Bring Lornette Daye to your athletic program or corporate keynote: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #Curacao #Korsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #SmallIslandBigDreams #CaribbeanPride #VamosCuraçao #IslandPride #CaribbeanToTheWorld #LornetteDaye"
        )
    },
    {
        "id": 14,
        "slot": "Day 7: Friday 7:15 PM MDT (Oct 02, 2026)",
        "dueAt": "2026-10-03T01:15:00.000Z",
        "assetFile": "curacao-ad-14.png",
        "assetUrl": f"{CDN_BASE}/curacao-ad-14.png",
        "cta": "Survival Skills for Athletes ($14.99 CAD) & Speaking",
        "text": (
            "WEEKEND ENERGY: CELEBRATING CARIBBEAN SOLIDARITY 🇨🇼🌴\n\n"
            "When Curaçao makes international headlines, the entire Caribbean region celebrates.\n\n"
            "It reminds the world that greatness is not restricted by geography or population. "
            "Our islands are home to extraordinary brilliance, determination, and competitive fire.\n\n"
            "To all our supporters across the Caribbean and the global diaspora: "
            "hold your heads high this weekend. The Blue Wave is rolling forward.\n\n"
            "Ban Kòrsou!\n\n"
            "Develop the mental focus and resilience required to win at the highest level. "
            "Read Survival Skills for Athletes ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "High-performance executive coaching: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueAndProud #CuraçaoRising #BanKòrsou #CuraçaoFootball #CaribbeanPride #CaribbeanToTheWorld #SmallIslandBigDreams #CaribbeanPower #LornetteDaye"
        )
    },
    {
        "id": 15,
        "slot": "Day 8: Saturday 12:30 PM MDT (Oct 03, 2026)",
        "dueAt": "2026-10-03T18:30:00.000Z",
        "assetFile": "curacao-ad-15.png",
        "assetUrl": f"{CDN_BASE}/curacao-ad-15.png",
        "cta": "Executive Keynote Speaking & Books",
        "text": (
            "SATURDAY FILM STUDY: HOW MOMENTUM REVERSES IN SECONDS 🇨🇼⚡\n\n"
            "Momentum is the most powerful psychological force in competitive sport.\n\n"
            "Costa Rica held complete control for 45 minutes. "
            "One goal from Kenji Gorré introduced doubt into their minds. "
            "A second goal from Tahith Chong shattered their certainty. "
            "By the time the third and fourth goals arrived, the psychological advantage had shifted entirely to Curaçao.\n\n"
            "Never underestimate what a single bold move can do to reverse the momentum of your life or business.\n\n"
            "Ban Kòrsou!\n\n"
            "Learn how to master psychological momentum in high-stakes environments. "
            "Explore keynote speaking with Coach Lornette Daye: https://lornettedaye.com/speaking\n\n"
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "#Curaçao #Curacao #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #CaribbeanPower #CaribbeanToTheWorld #SmallIslandBigDreams #LornetteDaye"
        )
    },
    {
        "id": 16,
        "slot": "Day 8: Saturday 7:15 PM MDT (Oct 03, 2026)",
        "dueAt": "2026-10-04T01:15:00.000Z",
        "assetFile": "curacao-ad-16.png",
        "assetUrl": f"{CDN_BASE}/curacao-ad-16.png",
        "cta": "Finish Strong: Chasing the Olympic Dream ($14.99 CAD) & Speaking",
        "text": (
            "SATURDAY NIGHT ROAR: WHEN BELIEF BECOMES CONTAGIOUS 🇨🇼🔥\n\n"
            "Look at the expression on the players' faces in this visual.\n\n"
            "That is not relief; that is total competitive conviction. "
            "When one player refuses to quit, it gives permission to ten others to dig deeper. "
            "When eleven players refuse to quit, it inspires an entire island nation.\n\n"
            "Be the spark in your family, team, or company that refuses to accept defeat.\n\n"
            "Ban Kòrsou! Dushi Kòrsou forever.\n\n"
            "Turn your biggest obstacles into career-defining springboards. "
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Executive leadership coaching with Coach Lornette Daye: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueAndProud #CuraçaoRising #VamosCuraçao #CuraçaoFootball #CaribbeanPride #IslandPride #SmallIslandBigDreams #CaribbeanAthletes #LornetteDaye"
        )
    },
    {
        "id": 17,
        "slot": "Day 9: Sunday 12:30 PM MDT (Oct 04, 2026)",
        "dueAt": "2026-10-04T18:30:00.000Z",
        "assetFile": "curacao-ad-17.png",
        "assetUrl": f"{CDN_BASE}/curacao-ad-17.png",
        "cta": "Survival Skills for Athletes ($14.99 CAD) & Speaking",
        "text": (
            "SUNDAY WISDOM: PREPARATION IS YOUR GREATEST ANCHOR 🇨🇼⚓\n\n"
            "You do not rise to the occasion under pressure; you sink to the level of your preparation.\n\n"
            "The reason Team Curaçao was able to press Costa Rica for 45 minutes in the second half "
            "and outlast them physically was the weeks of quiet, unseen conditioning that came before.\n\n"
            "When fatigue set in, their conditioning carried them across the finish line.\n\n"
            "Trust your preparation. Respect your daily habits. Finish strong.\n\n"
            "Master elite training discipline and physical recovery. "
            "Explore Survival Skills for Athletes ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Athletic mindset and leadership keynotes: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #Curacao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #CaribbeanExcellence #SmallIslandBigDreams #IslandFootball #LornetteDaye"
        )
    },
    {
        "id": 18,
        "slot": "Day 9: Sunday 7:15 PM MDT (Oct 04, 2026)",
        "dueAt": "2026-10-05T01:15:00.000Z",
        "assetFile": "curacao-ad-18.png",
        "assetUrl": f"{CDN_BASE}/curacao-ad-18.png",
        "cta": "Olympic Mindset Consulting & Books",
        "text": (
            "SUNDAY EVENING REFLECTION: REWRITING THE RECORD BOOKS 🇨🇼📖\n\n"
            "History is not written by observers. It is written by the people who stay in the fight.\n\n"
            "Every young girl and boy across Kòrsou will look at this match and know "
            "that their dreams are valid. They will know that a 3-0 deficit is never the end of the story.\n\n"
            "That is the power of sports: it creates blueprints for generational confidence.\n\n"
            "Ban Kòrsou! Share this message with a young athlete who needs inspiration today!\n\n"
            "Anchor your self-worth in lasting purpose and Olympic excellence. "
            "Explore Coach Lornette Daye's full library ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Bring Lornette Daye to your next corporate summit: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueAndProud #CuraçaoRising #BanKòrsou #CuraçaoFootball #CaribbeanSports #IslandFootball #SmallIslandBigDreams #CaribbeanExcellence #LornetteDaye"
        )
    },
    {
        "id": 19,
        "slot": "Day 10: Monday 12:30 PM MDT (Oct 05, 2026)",
        "dueAt": "2026-10-05T18:30:00.000Z",
        "assetFile": "curacao-ad-19.png",
        "assetUrl": f"{CDN_BASE}/curacao-ad-19.png",
        "cta": "Finish Strong: Chasing the Olympic Dream ($14.99 CAD) & Speaking",
        "text": (
            "10-DAY CELEBRATION FINALE: NOS TA KÒRSOU 🇨🇼🏆\n\n"
            "Ten days of celebrating one of the most heroic chapters in Caribbean sports lore.\n\n"
            "From Costa Rica 3, Curaçao 0 at halftime to a breathtaking 3-4 victory at full time. "
            "Four unanswered goals away from home against a regional powerhouse.\n\n"
            "Never forget who you are. Never forget what your people are capable of when united.\n\n"
            "Ban Kòrsou! Dushi Kòrsou forever.\n\n"
            "Build Olympic-level resilience and purpose into your daily life. "
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books\n\n"
            "Keynote bookings and executive coaching: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #Curacao #Korsou #TeamCuraçao #TheBlueWave #BlueWave #BanKòrsou #CuraçaoFootball #CaribbeanFootball #SmallIslandBigDreams #CaribbeanPride #VamosCuraçao #IslandPride #CaribbeanToTheWorld #LornetteDaye"
        )
    },
    {
        "id": 20,
        "slot": "Day 10: Monday 7:15 PM MDT (Oct 05, 2026)",
        "dueAt": "2026-10-06T01:15:00.000Z",
        "assetFile": "curacao-ad-20.png",
        "assetUrl": f"{CDN_BASE}/curacao-ad-20.png",
        "cta": "Full Championship Library ($14.99 CAD) & Speaking",
        "text": (
            "THE LEGACY CONTINUES: BETTER PEOPLE · BETTER PLAYERS 🇨🇼🌟\n\n"
            "As we wrap this historic campaign, let the lesson of Team Curaçao guide your every move:\n\n"
            "Your previous score cannot dictate your next possession. "
            "Your past mistakes cannot limit your future excellence.\n\n"
            "Keep pushing. Keep executing. Keep believing.\n\n"
            "To Coach Dick Advocaat, every player, and every supporter across the globe: "
            "thank you for showing the world what it means to finish strong.\n\n"
            "Ban Kòrsou!\n\n"
            "Explore Coach Lornette Daye's complete digital book catalog ($14.99 CAD each): https://lornettedaye.com/books\n\n"
            "Executive coaching and Olympic keynote presentations: https://lornettedaye.com/speaking\n\n"
            "#Curaçao #DushiKòrsou #TeamCuraçao #TheBlueWave #BlueAndProud #CuraçaoRising #BanKòrsou #CuraçaoFootball #CaribbeanSports #IslandFootball #SmallIslandBigDreams #CaribbeanExcellence #FinishStrong #LornetteDaye"
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
    print("EM DASH CHECK: PASS (Zero em dashes found across all 20 ad posts).")

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
    print("STARTING CURAÇAO 20-IMAGE AD CAMPAIGN SCHEDULING (10 DAYS, 2 DROPS/DAY)")
    print("=" * 75)

    check_for_em_dashes()

    report_path = os.path.join(os.path.dirname(__file__), "curacao-ads-scheduled-report.json")
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
            print(f"[{idx}/20] Post #{p_id} already scheduled (Buffer ID: {results[p_id]['postId']}). Skipping.")
            continue

        while True:
            print(f"\n[{idx}/20] Scheduling Post #{p_id} ({post['slot']}) - Due: {post['dueAt']}...")
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
    print(f"Summary: {success_count}/20 posts scheduled successfully.")

if __name__ == "__main__":
    main()
