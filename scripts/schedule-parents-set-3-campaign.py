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

CDN_BASE = 'https://lornettedaye.com/campaigns/parents-set-3'

HASHTAGS = "#MarcusFreeman #NotreDame #FightingIrish #CollegeFootball #NCAA #SportsLeadership #CoachingExcellence #RepresentationMatters #AthleticDirector #ExecutiveLeadership #OlympicMindset #LornetteDaye #DisciplineBuildsFreedom"

posts_data = [
    {
        "id": 1,
        "slot": "Monday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-14T14:30:00.000Z",
        "assetFile": "parents-3-1.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": "WHEN CARLOS LOOKED UP, HOME WAS THERE. 🇪🇸🎾❤️\n\nLook at Carlos Alcaraz's eyes in this moment. The Wimbledon crowd of 15,000 is on its feet, royalty is in the front row, and the international cameras are tracking his every breath.\n\nWhere does Carlos point? Straight to the corner where his father Carlos Sr. and his mother Virginia Garfia are standing.\n\nIn 40+ years coaching Olympic athletes, I have seen child prodigies crumble when they enter the brutal meat-grinder of professional sport. The ones who thrive for a decade aren't the ones with the flashiest forehands—they are the ones whose homes remain an unshakeable emotional anchor.\n\nParents & Coaches: What does your young athlete see in your eyes when the match is on the line? Judgment, or unconditional belief?\n\n👉 Book Lornette Daye for keynotes and workshops on raising resilient champions with healthy family foundations: lornettedaye.com/speaking\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 2,
        "slot": "Monday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-14T19:00:00.000Z",
        "assetFile": "parents-3-1.png",
        "cta": "Survival Skills for Men Book (lornettedaye.com/books)",
        "text": "ROOTS STILL MATTER: WHY CARLOS SR. KEPT HIM IN EL PALMAR. 🏡🇪🇸\n\nWhen Carlos Alcaraz was 15, agents offered millions in guarantees to move him to glamorous private academies abroad.\n\nCarlos Sr. said NO.\n\nHe kept Carlos in El Palmar, Murcia. He kept him around his brothers, his childhood club, and his hometown friends. Carlos Sr. knew that if you rip a tree's roots out of the soil before the trunk is thick, the first winter storm will snap it in half.\n\nFathers and mentors: Protecting your son's roots is the most important leadership responsibility you have.\n\n👉 Strengthen your emotional resilience and purposeful leadership. Read *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 3,
        "slot": "Monday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-15T00:00:00.000Z",
        "assetFile": "parents-3-1.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": "PRESENCE MATTERS. FAMILY MATTERS. 🕊️✨\n\nLook at Virginia Garfia's face in the stands. She isn't shouting tactical advice. She isn't checking ATP ranking points on her phone.\n\nShe is simply present. Her presence communicates to Carlos: \"You are my son. Win or lose, dinner is on the table, and you are loved.\"\n\nThat unconditional security is why Carlos plays five-set finals with joy rather than terror.\n\nAthletic Directors & Academy Heads: Are you creating high-performance environments that partner with parents, or isolate athletes from them?\n\n👉 Keynote Lornette Daye for your sports leadership summit on holistic student-athlete development: lornettedaye.com/speaking\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 4,
        "slot": "Tuesday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-15T14:30:00.000Z",
        "assetFile": "parents-3-2.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": "COCO NEVER RAN THIS JOURNEY ALONE. 🇺🇸✨🎾\n\nLook at the grit and beauty of this visual.\n\nBefore Coco Gauff was holding the US Open trophy in front of 24,000 roaring fans at Arthur Ashe Stadium, there were thousands of forgotten hours:\n- Packing rolling luggage in hotel lobbies at 5:00 AM.\n- Driving 300 miles to rain-delayed junior tournaments in Florida.\n- Sacrificing two full-time corporate and teaching careers so Corey and Candi could invest in their daughter.\n\nBehind every explosive, self-assured young champion is a family that chose sacrifice over comfort.\n\nCoaches & Parents: What is the unseen sacrifice you are making today that nobody on social media will ever see?\n\n👉 Empower your organization with Lornette Daye's keynote on family leadership and youth sports excellence: lornettedaye.com/speaking\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 5,
        "slot": "Tuesday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-15T19:00:00.000Z",
        "assetFile": "parents-3-2.png",
        "cta": "Survival Skills for Women Book (lornettedaye.com/books)",
        "text": "THE MOTHER BEHIND THE FIRE: CANDI GAUFF'S GRACE. 🌸👑\n\nCandi Gauff was an NCAA Division I heptathlete at Florida State. She understands athletic pain, track intervals, and physical exhaustion.\n\nYet her role in Coco's journey was never about being a drill sergeant. Candi was Coco's homeschool teacher, her travel companion, and her emotional anchor. When Coco cried after brutal losses at 14, Candi held her and whispered truth into her spirit.\n\nWomen leaders and mothers: Carrying the vision for your family requires you to possess deep, quiet emotional reserves.\n\n👉 Restore your clarity, protect your inner peace, and thrive through every season of transition. Read *Survival Skills for Women* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 6,
        "slot": "Tuesday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-16T00:00:00.000Z",
        "assetFile": "parents-3-2.png",
        "cta": "Surviving Life Book (lornettedaye.com/books)",
        "text": "STRUCTURE. SACRIFICE. LOVE: THE THREE PILLARS OF GAUFF FAMILY CULTURE. 🏛️❤️\n\nNotice that Corey and Candi Gauff didn't just give Coco tennis drills. They gave her:\n1. Structure: Strict bedtimes, daily reading, and academic rigor.\n2. Sacrifice: Moving into grandparents' home to fund tournament travel.\n3. Unconditional Love: Never allowing tennis to define her worth as a young Black woman.\n\nWhen the structure is solid, the athlete can soar without fear of falling apart.\n\nParents: What are the non-negotiable pillars of your household?\n\n👉 Rebuild hope, find strength, and embrace purpose through life's hardest chapters. Read *Surviving Life* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 7,
        "slot": "Wednesday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-16T14:30:00.000Z",
        "assetFile": "parents-3-3.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": "A FATHER IN THE CORNER CHANGES EVERYTHING. 🇺🇸🎾🤝\n\nLook at this image of Ben Shelton and Bryan Shelton.\n\nBryan was an ATP top-55 touring pro and a legendary NCAA national championship coach. He knows every technical angle of the serve and return. But look at his eyes: he isn't staring at Ben like a technician evaluating equipment. He is looking at his son with the pride of a father who helped shape the man.\n\n\"Some fathers coach the game,\" the saying goes. \"Great fathers shape the man.\"\n\nWhen an athlete knows his father loves him unconditionally—not just when he serves 149 mph—he plays with total freedom.\n\nCollegiate Coaches & Athletic Directors: How are you supporting coaches who also coach their own children?\n\n👉 Keynote Lornette Daye for your athletic department on coaching boundaries and family resilience: lornettedaye.com/speaking\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 8,
        "slot": "Wednesday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-16T19:00:00.000Z",
        "assetFile": "parents-3-3.png",
        "cta": "Survival Skills for Men Book (lornettedaye.com/books)",
        "text": "MORE THAN A MATCH: BRYAN SHELTON'S TENURE SACRIFICE. 🐊🎾\n\nLet's remember the magnitude of what Bryan Shelton did:\n\nHe had lifetime job security at the University of Florida. He was a revered, championship-winning head coach with a salary, pension, and comfortable campus life.\n\nWhen Ben turned pro, Bryan walked away from all of it. Why? Because he knew Ben would need a trusted, grounded guide through the predatory, lonely world of the ATP tour.\n\nFathers and mentors: What comforts are you willing to sacrifice so that the young men following you have a faithful guide?\n\n👉 Lead with purpose, emotional balance, and generational fortitude. Read *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 9,
        "slot": "Wednesday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-17T00:00:00.000Z",
        "assetFile": "parents-3-3.png",
        "cta": "Survival Skills for Athletes Book (lornettedaye.com/books)",
        "text": "TRUST IN THE HEAT OF BATTLE: BEN & BRYAN SHELTON. 🎯⚡\n\nWhen you are down break point in the 4th set in front of 20,000 screaming fans, you cannot fake trust.\n\nBen Shelton trusts Bryan because Bryan has never lied to him, never hyped him for clicks, and never abandoned him when his forehand was spraying wide. That multi-decade trust allows Ben to look into the box and find instant calm.\n\nAthletes: Do you have people in your corner who tell you the truth, or just people who flatter you?\n\n👉 Build the mental poise, coachability, and inner focus of elite performers. Read *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 10,
        "slot": "Thursday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-17T14:30:00.000Z",
        "assetFile": "parents-3-4.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": "SOME DREAMS ARE CARRIED BY MOTHERS. 🇯🇵🗽🌸\n\nLook at Tamaki Osaka holding her daughter Naomi after winning the US Open.\n\nBefore Naomi held that silver trophy, Tamaki carried this dream through the darkest nights:\n- Working 16-hour shifts in New York so Leonard could coach the girls in public parks.\n- Balancing bills with zero guarantee of a return on investment.\n- Enduring cultural alienation and racism without ever passing bitterness to her daughters.\n\nBehind every champion is someone who kept showing up when nobody was watching.\n\nMothers & Mentors: Your quiet persistence is the greatest foundation your children will ever receive.\n\n👉 Bring Lornette Daye to your conference or symposium to honor and teach the power of family resilience: lornettedaye.com/speaking\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 11,
        "slot": "Thursday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-17T19:00:00.000Z",
        "assetFile": "parents-3-4.png",
        "cta": "Survival Skills for Women Book (lornettedaye.com/books)",
        "text": "WORK TODAY. A BRIGHTER TOMORROW. 🕊️✍️\n\nNotice the inset in this artwork: Tamaki Osaka holding young Naomi's hand with an oversized tennis bag slung over the shoulder.\n\nTamaki never played tennis. She didn't know how to hit a topspin backhand. But she understood work ethic, honor, and sacrifice. She gave her daughters the gift of seeing a woman work tirelessly for the people she loved.\n\nWomen leaders and mothers: The quiet labor you do today is planting seeds for a harvest your children will reap tomorrow.\n\n👉 Protect your peace, restore your strength, and discover meaning in heavy seasons. Read *Survival Skills for Women* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 12,
        "slot": "Thursday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-18T00:00:00.000Z",
        "assetFile": "parents-3-4.png",
        "cta": "Surviving Life Book (lornettedaye.com/books)",
        "text": "STRONGER TOGETHER: A MOTHER'S EMBRACE AS MENTAL HAVEN. 🌸🤍\n\nWhen Naomi Osaka spoke publicly about her battles with depression and social anxiety, the world debated her courage.\n\nDo you know what Tamaki did? She didn't read the commentary. She held Naomi close and reminded her: \"You are my little girl. Tennis is what you do, but your spirit is who you are.\"\n\nIn Olympic sport, the ultimate luxury is a mother's embrace where an athlete is completely safe from scrutiny.\n\nParents: Is your home a stage for performance, or a haven for healing?\n\n👉 Rebuild hope, confidence, and peace after seasons of pressure. Read *Surviving Life* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 13,
        "slot": "Friday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-18T14:30:00.000Z",
        "assetFile": "parents-3-5.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": "THE FIRST RUNWAY WAS THE BACKYARD. 🇸🇪🏡🚀\n\nArmand \"Mondo\" Duplantis is the undisputed king of pole vault. He has broken the World Record over 10 times, clearing 6.30m+ with effortless elegance.\n\nWhere did this superhuman ability come from?\n\nIt didn't come from a $50 million national training center. It came from the grass and plywood in his parents' backyard in Lafayette, Louisiana. His father, Greg Duplantis (a 5.80m Olympian vaulter himself), built a runway and pit when Mondo was four years old.\n\nMondo learned to vault while his mother Helena cooked dinner and his brothers played baseball. It was pure joy.\n\nCoaches & Parents: When you build the environment, greatness becomes an inevitable byproduct.\n\n👉 Book Lornette Daye for your sports leadership seminar on unlocking athletic genius through environment design: lornettedaye.com/speaking\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 14,
        "slot": "Friday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-18T19:00:00.000Z",
        "assetFile": "parents-3-5.png",
        "cta": "Survival Skills for Athletes Book (lornettedaye.com/books)",
        "text": "SAME FOUNDATION. HIGHER HORIZONS. 🧗‍♂️✨\n\nLook at Greg Duplantis's smile in this artwork as Mondo points to the sky.\n\nGreg never lived vicariously through Mondo. Because Greg was an Olympian himself, he had already walked that mountain. He didn't need Mondo to validate his ego. That emotional maturity allowed Greg to coach Mondo with total patience.\n\nAthletes: Are you competing to fulfill your parents' unlived dreams, or because you love the pursuit of excellence?\n\n👉 Cultivate intrinsic motivation and elite mental discipline. Read *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 15,
        "slot": "Friday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-19T00:00:00.000Z",
        "assetFile": "parents-3-5.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": "THE FLIGHT STARTED AT HOME: GREG DUPLANTIS'S MASTERCLASS. 🇸🇪🤝\n\nIn 40+ years coaching Olympic athletes, the saddest phenomenon I witness is parental burnout: talented kids who hate their sport by age 16 because their parents turned practice into a prison sentence.\n\nGreg and Helena Duplantis did the exact opposite. They protected Mondo's passion. When he wanted to jump, they watched. When he wanted to stop, they let him go fish.\n\nThe result? Mondo is still vaulting with the joy of a four-year-old boy in a Louisiana backyard.\n\nSports Leaders & Parents: Are you protecting the fire in your athlete's soul?\n\n👉 Build enduring legacy and finish your race with joy. Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 16,
        "slot": "Saturday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-19T14:30:00.000Z",
        "assetFile": "parents-3-1.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": "THE SPANISH LESSON: WINNING WITH HUMILITY. 🇪🇸🎾\n\nWatch Carlos Alcaraz after he wins a 5-hour slugfest. He hugs his opponent at the net. He thanks the ball crew. He signs every autograph.\n\nWhy? Because his mother Virginia made him understand that tennis is a privilege, not a pass to be arrogant.\n\nIn collegiate athletics and youth academies, character is the ultimate force multiplier. An athlete with humility is coachable, adaptable, and emotionally resilient.\n\nCoaches: Are you cultivating athletes who are feared for their talent, or respected for their character?\n\n👉 Keynote Lornette Daye for your sports leadership summit on character-driven athletic development: lornettedaye.com/speaking\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 17,
        "slot": "Saturday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-19T19:00:00.000Z",
        "assetFile": "parents-3-1.png",
        "cta": "Survival Skills for Men Book (lornettedaye.com/books)",
        "text": "THE FATHER WHO STEPPED INTO THE BACKGROUND. 🤝🇪🇸\n\nCarlos Alcaraz Sr. was a top junior player in Spain whose pro career ended early because his family couldn't afford travel costs.\n\nYet when Carlos Jr. showed world-class potential, Carlos Sr. never forced his unfulfilled dreams onto his son. When Juan Carlos Ferrero took over as head coach, Carlos Sr. stepped back and became purely a father.\n\nParental ego subordination is the greatest gift an athletic father can give.\n\nFathers: Can you step back from managing and simply love?\n\n👉 Clarify your purpose, master pressure, and lead your family with wisdom. Read *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 18,
        "slot": "Saturday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-20T00:00:00.000Z",
        "assetFile": "parents-3-1.png",
        "cta": "Surviving Life Book (lornettedaye.com/books)",
        "text": "HOME IS WHERE YOU DON'T HAVE TO PERFORM. 🏠🌿\n\nWhen Carlos Alcaraz returns home to El Palmar, nobody treats him like World No. 1. He cleans his room, sits with his brothers, and eats his mother's food.\n\nEvery elite performer needs a space where they don't have to perform. If your home is just another arena of evaluation, emotional burnout is inevitable.\n\nParents: Is your dinner table a sanctuary or an interrogation room?\n\n👉 Ground your identity in purpose and rebuild steady hope. Read *Surviving Life* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 19,
        "slot": "Sunday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-20T14:30:00.000Z",
        "assetFile": "parents-3-2.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": "EARLY MORNINGS. BIGGER DREAMS. 🌅🎾\n\nLook at the young Coco Gauff in this artwork with her luggage, heading to an early flight.\n\nMost people only see the US Open victory speech. They don't see the alarm clocks at 4:30 AM, the cold practice courts in Delray Beach, or the parents who gave up their own weekends for a decade.\n\nIn my 40+ years coaching Olympic athletes, champions are built in the dark when nobody is watching.\n\nAthletic Directors & School Leaders: How are you instilling the daily habits of excellence in your young athletes?\n\n👉 Book Lornette Daye for keynotes on the daily disciplines of championship cultures: lornettedaye.com/speaking\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 20,
        "slot": "Sunday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-20T19:00:00.000Z",
        "assetFile": "parents-3-2.png",
        "cta": "Survival Skills for Women Book (lornettedaye.com/books)",
        "text": "BELIEF WHEN THE WORLD DOUBTS: CANDI GAUFF'S UNSHAKEABLE FAITH. 🌸🙏\n\nWhen Coco Gauff was 12 years old, scouts questioned whether her forehand mechanics could survive on the WTA tour.\n\nCandi Gauff didn't listen to the critics. She knew that mechanics can be rebuilt, but a young woman's inner fire and self-worth cannot be bought.\n\nMothers: The belief you pour into your daughter's heart is stronger than any critic's evaluation.\n\n👉 Rebuild your foundation, thrive with meaning, and cultivate unshakeable peace. Read *Survival Skills for Women* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 21,
        "slot": "Sunday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-21T00:00:00.000Z",
        "assetFile": "parents-3-2.png",
        "cta": "Survival Skills for Athletes Book (lornettedaye.com/books)",
        "text": "GRATITUDE AS A COMPETITIVE ADVANTAGE. 🎾❤️\n\nWhen Coco Gauff won the US Open, her first words at the microphone were thanking her parents, her grandparents, and the people who believed in her when she was a nobody.\n\nAn entitled athlete is fragile; the moment adversity strikes, they blame everyone around them. A grateful athlete is indestructible because they realize they stand on the shoulders of giants.\n\nAthletes: When was the last time you thanked the people who paid for your training?\n\n👉 Train the inner maturity and mental resilience of champions. Read *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 22,
        "slot": "Monday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-21T14:30:00.000Z",
        "assetFile": "parents-3-3.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": "COLLEGE TENNIS AS THE FORGE: BRYAN SHELTON'S ROADMAP. 🐊🇺🇸\n\nWhy did Bryan Shelton make Ben stay in college tennis at Florida instead of turning pro at 16?\n\nBecause college athletics teaches you what junior tennis never can: brotherhood, locker room accountability, and performing for a team bigger than yourself.\n\nWhen Ben arrived on the ATP tour, he didn't wilt under pressure because he had already played in hostile SEC college environments.\n\nCoaches & Athletic Directors: Are you promoting college sports as the premier developmental bridge to professional life?\n\n👉 Keynote Lornette Daye for your collegiate athletic conference or coaching retreat: lornettedaye.com/speaking\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 23,
        "slot": "Monday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-21T19:00:00.000Z",
        "assetFile": "parents-3-3.png",
        "cta": "Survival Skills for Men Book (lornettedaye.com/books)",
        "text": "THE TOUGH LOVE OF A FATHER WHO KNOWS THE SUMMIT. 🏔️🎾\n\nWhen Ben Shelton misses a short volley, Bryan Shelton doesn't sugarcoat the feedback. But he delivers it with love, not contempt.\n\nA boy needs truth delivered by a man who loves him. Without truth, there is no technical mastery. Without love, there is rebellion.\n\nFathers and mentors: Mastering the balance of high standards and deep affection is the mark of elite leadership.\n\n👉 Strengthen your emotional fortitude, clarify your vision, and lead your family. Read *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 24,
        "slot": "Monday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-22T00:00:00.000Z",
        "assetFile": "parents-3-3.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": "THE 149 MPH SERVE WAS BUILT IN EMPTY GYMS. ⚡🏟️\n\nThe world sees Ben Shelton's electric smile and thunderbolt left-handed serve on ESPN.\n\nThey don't see Bryan Shelton feeding thousands of tennis balls out of a rusted hopper in the hot Gainesville humidity while other teenagers were at the mall.\n\nExcellence is paid in advance, in unglamorous installments.\n\nCompetitors: Are you willing to pay the price in private for the victory in public?\n\n👉 Unleash your champion mindset and finish strong. Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 25,
        "slot": "Tuesday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-22T14:30:00.000Z",
        "assetFile": "parents-3-4.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": "THE UNSUNG CURRENCY OF SPORT: SLEEP SACRIFICED. 🇯🇵🗽\n\nWhen Naomi Osaka won the US Open, commentators talked about prize money and endorsement deals.\n\nNobody talked about the 15 years Tamaki Osaka worked night shifts so Leonard could teach Naomi and Mari tennis on cracked public courts with second-hand balls.\n\nTamaki paid for Naomi's tennis dream with her own physical sleep.\n\nAthletic Directors & Sports Executives: How often do we remember to honor the parents whose labor made the spectacle possible?\n\n👉 Book Lornette Daye for keynotes on the human heart behind high-performance sport: lornettedaye.com/speaking\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 26,
        "slot": "Tuesday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-22T19:00:00.000Z",
        "assetFile": "parents-3-4.png",
        "cta": "Survival Skills for Women Book (lornettedaye.com/books)",
        "text": "BIGGER GIRLS. BRIGHTER TOMORROWS: TAMAKI'S VISION. 🌸✨\n\nLook at Tamaki Osaka's eyes in this artwork. She carried a vision for her daughters that transcended two cultures, two continents, and every racial barrier in international tennis.\n\nShe taught Naomi that she wasn't just playing for herself; she was playing to show young girls of color across Japan, Haiti, and America that they belonged on the highest stage.\n\nWomen leaders: When your vision is rooted in service to others, exhaustion cannot stop you.\n\n👉 Renew your inner strength, protect your boundaries, and thrive with purpose. Read *Survival Skills for Women* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 27,
        "slot": "Tuesday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-23T00:00:00.000Z",
        "assetFile": "parents-3-4.png",
        "cta": "Surviving Life Book (lornettedaye.com/books)",
        "text": "WHEN ANXIETY VISITS: A MOTHER'S UNCONDITIONAL LOVE. 🕊️🤍\n\nIn modern elite sport, mental health is finally being recognized as the foundation of all physical performance.\n\nWhen Naomi Osaka took her stand on mental wellness, Tamaki Osaka stood beside her like a lioness. She didn't care about sponsors or headlines; she cared about her daughter's soul.\n\nParents: Your athlete will forget 90% of their victories, but they will never forget whether you stood by them when they were broken.\n\n👉 Find strength and renewal through life's deepest trials. Read *Surviving Life* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 28,
        "slot": "Wednesday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-23T14:30:00.000Z",
        "assetFile": "parents-3-5.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": "HIGHER TOGETHER: THE DUPLANTIS FAMILY BLUEPRINT. 🇸🇪🚀\n\nArmand Duplantis has rewritten track and field history. At 24, he is already the greatest pole vaulter who has ever lived.\n\nWho coaches his takeoff mechanics? His father Greg.\nWho coordinates his strength, nutrition, and recovery? His mother Helena.\nWho cheers him on at every meet? His brothers.\n\nMondo is the tip of the spear; his family is the shaft that gives the spear its momentum.\n\nAthletic Directors & Coaches: Are your programs building family partnerships that amplify athletic performance?\n\n👉 Keynote Lornette Daye for your sports leadership seminar on unlocking generational athletic potential: lornettedaye.com/speaking\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 29,
        "slot": "Wednesday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-23T19:00:00.000Z",
        "assetFile": "parents-3-5.png",
        "cta": "Survival Skills for Athletes Book (lornettedaye.com/books)",
        "text": "PLAY OVER PRESSURE: WHY MONDO STILL SMILES. 🧗‍♂️✨\n\nWatch Mondo Duplantis on the runway before breaking another World Record. He doesn't look like a condemned man going to the gallows. He looks like a boy on a playground.\n\nWhy? Because his father Greg never turned the pole vault into an obligation. He turned it into an adventure.\n\nWhen you love what you do, the nervous system stays relaxed and reaction times stay sharp.\n\nAthletes: Are you vaulting out of fear of failure, or the joy of flight?\n\n👉 Train the inner poise, mental freedom, and champion discipline of elite competitors. Read *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 30,
        "slot": "Wednesday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-24T00:00:00.000Z",
        "assetFile": "parents-3-5.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": "THE BACKYARD RUNWAY: BIG DREAMS BEGIN IN SIMPLE SPACES. 🏡🌟\n\nThink about that backyard in Lafayette, Louisiana.\n\nNo corporate logos. No VIP lounges. Just a dad with a tape measure, a young boy with a fiberglass stick, and an endless summer afternoon.\n\nYou don't need million-dollar facilities to raise a champion. You need dedication, consistency, and a parent who believes before the world sees anything.\n\nTo every parent creating practice spaces in the backyard or garage: Keep building.\n\n👉 Finish your race with endurance, purpose, and legacy. Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 31,
        "slot": "Thursday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-24T14:30:00.000Z",
        "assetFile": "parents-3-1.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": "THE QUIET DISCIPLINE OF PATIENCE. 🇪🇸🎾⏳\n\nIn modern sports, when a teenager exhibits extraordinary talent, everyone scrambles to cash in immediately. Endorsement contracts, international travel, early pro status.\n\nCarlos Alcaraz's parents refused to play that game.\n\nCarlos Sr. and Virginia Garfia understood that rushing an athlete's development is the quickest route to physical injury and emotional devastation. They protected his childhood. They let him play soccer with his brothers in El Palmar. They allowed his body and mind to mature on nature's clock.\n\nAs an Olympian coach who has guided elite performers across 40+ years: You cannot microwave championship maturity.\n\nAthletic Directors & Youth Coaches: Are you building athletes for a single high-school trophy, or equipping them for lifetime mastery?\n\n👉 Book Lornette Daye for your sports leadership summit or coaching clinic on long-term athlete development: lornettedaye.com/speaking\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 32,
        "slot": "Thursday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-24T19:00:00.000Z",
        "assetFile": "parents-3-1.png",
        "cta": "Survival Skills for Men Book (lornettedaye.com/books)",
        "text": "WHAT A SON SEES IN HIS FATHER'S EYES. 🇪🇸🤝\n\nWatch Carlos Alcaraz walk off court after a heartbreaking loss. The first person he looks for is his father, Carlos Sr.\n\nAnd what does he find? Not disappointment. Not anger over missed break points. He finds quiet, grounded strength.\n\nWhen a father can handle his son's defeat without flinching, the son learns that defeat is not a death sentence—it is simply data. He learns that his worth as a man is not tied to a tennis scoreboard.\n\nMen and fathers: Your reaction to your children's setbacks will either build their resilience or feed their anxiety.\n\n👉 Clarify your purpose, manage pressure, and lead your family with steady wisdom. Read *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 33,
        "slot": "Thursday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-25T00:00:00.000Z",
        "assetFile": "parents-3-1.png",
        "cta": "Surviving Life Book (lornettedaye.com/books)",
        "text": "KEEPING THE CHAMPION HUMAN. 🏡🌿🇪🇸\n\nAt 21 years old, Carlos Alcaraz has won Wimbledon, Roland Garros, and the US Open. He is courted by luxury brands and global dignitaries.\n\nYet when he returns home to Murcia, Virginia Garfia still reminds him to make his bed and wash his plate.\n\nWhy is this essential? Because when the stadium lights turn off, every athlete must return to ordinary humanity. If your identity exists solely inside the ropes of the court, retirement or injury will destroy you.\n\nParents: Give your children the greatest gift of all—the freedom to be ordinary at home, so they can be extraordinary in the world.\n\n👉 Rebuild hope, discover purpose, and stay anchored through every storm. Read *Surviving Life* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 34,
        "slot": "Friday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-25T14:30:00.000Z",
        "assetFile": "parents-3-2.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": "COREY & CANDI GAUFF: THE PARTNERSHIP BEHIND THE PHENOM. 🇺🇸👑🎾\n\nHigh-performance parenting is an endurance team sport.\n\nLook at Corey and Candi Gauff. Corey brought the collegiate basketball tenacity, the tactical discipline, and the willingness to drive the van across five states. Candi brought the Division I heptathlete grit, the emotional intuition, and the academic structure of homeschooling.\n\nThey didn't compete with each other. They complemented each other.\n\nWhen parents form a united, drama-free leadership front, the athlete feels completely safe to take risks, fail forward, and play fearlessly.\n\nAthletic Directors & School Leaders: How are you educating sports parents to work in harmony with coaching staffs?\n\n👉 Keynote Lornette Daye for your sports leadership seminar or parent education forum: lornettedaye.com/speaking\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 35,
        "slot": "Friday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-25T19:00:00.000Z",
        "assetFile": "parents-3-2.png",
        "cta": "Survival Skills for Women Book (lornettedaye.com/books)",
        "text": "CANDI GAUFF'S UNSHAKEABLE MATERNAL ANCHOR. 🌸✨\n\nWhen Coco Gauff broke down in tears on international television during difficult tournament stretches, who walked down from the stands?\n\nHer mother, Candi.\n\nShe didn't hand Coco a racket or lecture her on backhand angles. She wrapped her arms around her daughter and reminded her of who she is away from the spotlight.\n\nIn my 40+ years in Olympic athletics, women often carry the emotional weight of an entire family's dreams. Doing so requires immense inner resilience, boundaries, and quiet faith.\n\nWomen leaders and mothers: Are you pouring from an empty cup, or replenishing your own spirit?\n\n👉 Rebuild your confidence, find meaning in heavy seasons, and protect your inner peace. Read *Survival Skills for Women* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 36,
        "slot": "Friday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-26T00:00:00.000Z",
        "assetFile": "parents-3-2.png",
        "cta": "Survival Skills for Athletes Book (lornettedaye.com/books)",
        "text": "NAVIGATING EXPECTATIONS WITH A CHAMPION MINDSET. 🎯⚡🎾\n\nAt 15, Coco Gauff beat Venus Williams at Wimbledon. Overnight, the sports media crowned her the savior of American tennis.\n\nA lesser athlete—or a less grounded family—would have buckled under that suffocating weight.\n\nHow did Coco survive the hype machine? By anchoring herself in daily work, not external praise. Corey and Candi taught her: \"Compliments are like perfume: sniff them, but never swallow them.\"\n\nYoung athletes: When the world starts hyping your talent, will your foundation hold?\n\n👉 Build mental poise, focus under pressure, and elite discipline on and off the court. Read *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 37,
        "slot": "Saturday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-26T14:30:00.000Z",
        "assetFile": "parents-3-3.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": "THE ART OF COACHING YOUR OWN CHILD. 🇺🇸🎾🤝\n\nCoaching your own son or daughter is one of the most hazardous undertakings in all of sports.\n\nToo often, it destroys the parent-child relationship. The car ride home becomes a battlefield. Every dinner becomes a critique session.\n\nLook at Bryan Shelton and Ben Shelton. Bryan mastered the art of role clarity:\n- On the court, he is Coach Shelton—demanding, precise, and uncompromising.\n- At home, he is Dad—supportive, caring, and safe.\n\nBen respects Bryan because Bryan never blurred those lines or used love as leverage.\n\nCollegiate Coaches & Parents: How are you managing boundaries so that athletics strengthens your family instead of fracturing it?\n\n👉 Keynote Lornette Daye for your sports organization on coaching boundaries and generational leadership: lornettedaye.com/speaking\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 38,
        "slot": "Saturday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-26T19:00:00.000Z",
        "assetFile": "parents-3-3.png",
        "cta": "Survival Skills for Men Book (lornettedaye.com/books)",
        "text": "FATHERHOOD UNDER PRESSURE: BRYAN SHELTON'S EXAMPLE. 🐊🇺🇸\n\nNotice Bryan Shelton's demeanor in the coaching box during a 5th-set tiebreak at the US Open.\n\nHe isn't jumping out of his seat. He isn't screaming at the umpire. He sits with folded arms, eyes focused, radiating total calm.\n\nWhy? Because an anxious coach creates an anxious player. A calm coach allows the athlete's natural instincts to fire without interference.\n\nMen: In your home, business, or athletic arena, your emotional regulation is the ceiling of your team's performance.\n\n👉 Strengthen your emotional fortitude, master high-pressure environments, and lead with purpose. Read *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 39,
        "slot": "Saturday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-27T00:00:00.000Z",
        "assetFile": "parents-3-3.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": "RISING AGAIN AFTER SETBACKS: THE SHELTON DNA. ⚡🎾🏆\n\nIn elite tennis, you can play magnificent tennis for four hours and still lose by two points.\n\nWhen Ben Shelton suffers a tough defeat, you don't see him sulking or blaming external factors. Within 48 hours, he is back on the practice court with Bryan, analyzing forehand depths and return positioning.\n\nThat resilience was forged in Florida clay and SEC tournament wars.\n\nIn 40+ years in Olympic sport, I tell every champion: Setbacks are not roadblocks; they are the curriculum.\n\nCompetitors & Leaders: How quickly do you reset after life breaks your serve?\n\n👉 Cultivate the elite athlete mindset and learn to rise after every defeat. Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 40,
        "slot": "Sunday Morning Finale (8:30 AM MDT)",
        "dueAt": "2026-09-27T14:30:00.000Z",
        "assetFile": "parents-3-6.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": "BEHIND GREAT CHAMPIONS, SOMEONE KEPT SHOWING UP. 🌟👑🏆\n\nLook at this master ensemble of five world-class champions and the families who built them:\n- Carlos Alcaraz & his parents Carlos Sr. and Virginia Garfia.\n- Coco Gauff & Corey and Candi Gauff.\n- Ben Shelton & Bryan Shelton.\n- Naomi Osaka & Tamaki Osaka.\n- Armand \"Mondo\" Duplantis & Greg Duplantis.\n\nFive different sports paths. Five different nations. One undeniable universal truth:\n\nNo champion ever arrived at the podium alone.\n\nBehind every Grand Slam trophy, every World Record clearance, and every roaring stadium moment are parents who woke up at 4:30 AM, drove thousands of miles, sacrificed their personal comforts, and believed in their children long before the world knew their names.\n\nSports Leaders, Athletic Directors & Educators: Are you honoring and supporting the families behind your athletes?\n\n👉 Book Lornette Daye for your sports gala, university conference, or corporate keynote: lornettedaye.com/speaking\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 41,
        "slot": "Sunday Mid-day Finale (1:00 PM MDT)",
        "dueAt": "2026-09-27T19:00:00.000Z",
        "assetFile": "parents-3-6.png",
        "cta": "Surviving Life Book (lornettedaye.com/books)",
        "text": "THE ANATOMY OF SACRIFICE: WHAT THE CAMERAS NEVER CAPTURE. 🕊️✨\n\nWhen you look at this visual of world champions and their parents, remember what isn't shown:\n- The second mortgages taken to pay for coaching.\n- The 16-hour shifts worked by mothers like Tamaki Osaka.\n- The careers stepped away from by fathers like Bryan Shelton.\n- The thousands of weekends sacrificed by Corey and Candi Gauff.\n- The backyard runways hammered together with bare hands by Greg Duplantis.\n\nSacrifice is not glorious in the moment. It is exhausting, lonely, and filled with doubt.\n\nYet love makes sacrifice worthwhile. When a family is anchored in purpose, hardship does not break them—it binds them together.\n\nTo every parent grinding in obscurity today for your child's future: Your sacrifice is seen.\n\n👉 Rebuild hope, find strength, and embrace purpose through life's deepest trials. Read *Surviving Life* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 42,
        "slot": "Sunday Evening Grand Campaign Finale (6:00 PM MDT)",
        "dueAt": "2026-09-28T00:00:00.000Z",
        "assetFile": "parents-3-6.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": "THE GREATEST TROPHY IS THE RELATIONSHIP. 🏆❤️🌟\n\nAs our 14-day campaign honoring sports parents comes to a close, consider this reflection from 40+ years in Olympic athletics:\n\nGold medals will eventually tarnish in glass cases.\nWorld records will eventually be broken by the next generation.\nApplause fades the moment you walk out of the arena.\n\nWhat remains?\n\nThe father who held your hand.\nThe mother who dried your tears.\nThe family that loved you when you had zero ranking points.\n\nThe ultimate victory of athletic competition is not the trophy you hold up—it is the character you build and the bonds that endure a lifetime.\n\nTo every parent, coach, and athlete striving for excellence: Protect your foundation, honor your roots, and finish strong.\n\n👉 Build enduring legacy and champion discipline in every stage of life. Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    }
]

for p in posts_data:
    p["assetUrl"] = f"{CDN_BASE}/{p['assetFile']}"

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
            body = json.loads(resp.read().decode('utf-8'))
            return body
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
    print("Starting Buffer queue scheduling for Parents Set 3 Campaign (42 posts)...")
    print(f"Total Posts to Schedule: {len(posts_data)}")
    print(f"Channel: {CHANNEL_ID}")
    print(f"Token: {TOKEN[:6]}...{TOKEN[-4:]}")
    print("-" * 60)

    report_path = os.path.join(os.path.dirname(__file__), "parents-set-3-scheduled-report.json")
    results = {}
    if os.path.exists(report_path):
        try:
            with open(report_path, "r", encoding="utf-8") as f:
                existing_report = json.load(f)
                for item in existing_report.get("results", []):
                    if item.get("success") and item.get("bufferPostId"):
                        results[item["id"]] = item
        except Exception as e:
            print(f"Note: Could not parse existing report: {e}")

    print(f"Loaded {len(results)} previously scheduled posts from report.")

    daily_limit_hit = False

    for idx, post in enumerate(posts_data, 1):
        post_id_num = post["id"]
        if post_id_num in results and results[post_id_num].get("success"):
            print(f"[{idx}/42] Post #{post_id_num} already scheduled (Buffer ID: {results[post_id_num]['bufferPostId']}). Skipping.")
            continue

        while True:
            print(f"[{idx}/42] Scheduling: Post #{post['id']} ({post['slot']}) - {post['dueAt']}...")
            resp = schedule_post(post)

            # Check for 429 rate limit
            if resp.get("status_code") == 429 or "429" in str(resp.get("error", "")):
                wait_sec = resp.get("retry_after", 60)
                if wait_sec > 900:
                    print(f"   [DAILY 24H LIMIT] Buffer 24-hour daily limit reached. Reset in {wait_sec}s.")
                    print(f"   [AUTONOMOUS PERSISTENCE] Persisting queue state to report for background timer catchup.")
                    daily_limit_hit = True
                    break
                print(f"   [RATE LIMIT] HTTP 429 encountered. Buffer cooldown: sleeping {wait_sec + 5} seconds...")
                time.sleep(wait_sec + 5)
                print(f"   [RESUMING] Retrying Post #{post['id']} now...")
                continue

            create_post_data = resp.get("data", {}).get("createPost", {})
            typename = create_post_data.get("__typename")
            post_obj = create_post_data.get("post")

            if typename == "PostActionSuccess" and post_obj and post_obj.get("id"):
                b_id = post_obj["id"]
                status = post_obj.get("status")
                due_at = post_obj.get("dueAt")
                print(f"   --> SUCCESS! Post ID: {b_id} | Status: {status} | Due: {due_at}")
                results[post_id_num] = {
                    "id": post["id"],
                    "slot": post["slot"],
                    "dueAt": post["dueAt"],
                    "bufferPostId": b_id,
                    "status": status,
                    "assetUrl": post["assetUrl"],
                    "cta": post["cta"],
                    "success": True
                }
                break
            else:
                err_msg = create_post_data.get("message") or resp.get("errors") or resp.get("error") or str(resp)
                print(f"   --> FAILED: {err_msg}")
                results[post_id_num] = {
                    "id": post["id"],
                    "slot": post["slot"],
                    "dueAt": post["dueAt"],
                    "error": str(err_msg),
                    "success": False
                }
                break

        # Save checkpoint after each post
        ordered_results = [results[p["id"]] for p in posts_data if p["id"] in results]
        successful_count = sum(1 for r in ordered_results if r.get("success"))
        with open(report_path, "w", encoding="utf-8") as f:
            json.dump({
                "campaign": "Behind Great Champions, Someone Kept Showing Up (Parents Set 3)",
                "total_posts": len(posts_data),
                "successful_posts": successful_count,
                "daily_limit_hit": daily_limit_hit,
                "channelId": CHANNEL_ID,
                "scheduled_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                "results": ordered_results
            }, f, indent=2)

        if daily_limit_hit:
            print("   [AUTONOMOUS HANDOFF] Stopping execution loop for background timer catchup.")
            break

        time.sleep(1.0)

    ordered_results = [results[p["id"]] for p in posts_data if p["id"] in results]
    successful_count = sum(1 for r in ordered_results if r.get("success"))
    print("-" * 60)
    print(f"Parents Set 3 Campaign Scheduling Complete: {successful_count}/42 posts placed into Buffer Scheduled Queue.")
    print(f"Report updated at {report_path}")

if __name__ == "__main__":
    main()
