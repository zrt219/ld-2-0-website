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
        "slot": "Day 1 Morning (8:30 AM MDT)",
        "dueAt": "2026-09-16T14:30:00.000Z",
        "assetFile": "parents-3-1.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": "WHEN CARLOS LOOKED UP, HOME WAS THERE. 🇪🇸🎾❤️\n\n\"Every time I look into my player box during a five-set final,\" Carlos Alcaraz shared after lifting the Wimbledon trophy, \"I see my father and mother. Knowing they love me whether I win or lose is the reason I can smile on court.\"\n\nLook at Carlos Alcaraz's eyes in this moment. The Wimbledon crowd of 15,000 is roaring, royalty sits in the front row, and the global cameras capture his raw power. Yet his immediate instinct is to point straight to his parents, Carlos Sr. and Virginia Garfia.\n\nWhen an athlete knows their home is an unshakeable haven, fear of failure evaporates. They don't play to earn love—they play from an overflow of security.\n\nCoaches & Athletic Directors: What do your student-athletes see in their family's eyes when the match is on the line?\n\n👉 Book Lornette Daye for keynotes and workshops on raising resilient champions with healthy family foundations: lornettedaye.com/speaking\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 2,
        "slot": "Day 1 Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-16T19:00:00.000Z",
        "assetFile": "parents-3-1.png",
        "cta": "Survival Skills for Men Book (lornettedaye.com/books)",
        "text": "ROOTS IN EL PALMAR: THE UNTOLD QUIET LABOR OF CARLOS SR. 🏡🇪🇸\n\nWhen Carlos Alcaraz was 15, international agents waved million-dollar checks to relocate him to glamorous overseas tennis academies.\n\nHis father, Carlos Alcaraz Sr., gave a firm, definitive answer: NO.\n\nCarlos Sr. was a top junior player in Spain whose own pro career was cut short by financial hardship. He knew the tennis academy circuit can become a mercenary meat-grinder. Instead of chasing instant glamour, Carlos Sr. kept his boy in El Palmar, Murcia—sleeping in his childhood bed, eating home-cooked meals, and staying grounded with his brothers.\n\nPaternal leadership isn't about pushing your son into the limelight; it is about protecting his roots until the trunk is thick enough to survive the storm.\n\nFathers and mentors: Are you guarding the roots of the young men in your care?\n\n👉 Strengthen your emotional resilience and purposeful leadership. Read *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 3,
        "slot": "Day 1 Evening (6:00 PM MDT)",
        "dueAt": "2026-09-17T00:00:00.000Z",
        "assetFile": "parents-3-1.png",
        "cta": "Survival Skills for Athletes Book (lornettedaye.com/books)",
        "text": "THE DANGER OF EARLY PRO HYPE: LORNETTE'S COACHING TAKEAWAY. ⚖️🎾\n\nIn my 40+ years coaching Olympic athletes, the most common tragedy I witness is \"the microwaved prodigy\": child phenoms who are celebrated at 14, signed to multi-million dollar sponsorships at 16, and emotionally bankrupt by 20.\n\nWhy did Carlos Alcaraz survive the hype?\n\nBecause his parents never allowed tennis results to dictate the mood of the household. When Carlos came home from winning national titles, Virginia still had him sweep the floor and do his homework.\n\nWhen an athlete's personal identity is decoupled from their match score, they develop immense competitive poise under pressure.\n\nSports Parents: Does your dinner table atmosphere change based on whether your child won or lost? Share your thoughts below! 👇\n\n👉 Build focus, mental discipline, and the champion mindset on and off the court. Read *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 4,
        "slot": "Day 2 Morning (8:30 AM MDT)",
        "dueAt": "2026-09-17T14:30:00.000Z",
        "assetFile": "parents-3-2.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": "COCO'S TRIBUTE: \"THEY GAVE UP THEIR ENTIRE LIVES FOR THIS.\" 🇺🇸👑🎾\n\n\"To my mom and dad,\" Coco Gauff said through tears with the US Open trophy in her hands, \"you gave up your entire lives for this dream. You believed in me when I didn't even believe in myself.\"\n\nLook at this visual of Coco walking through airport terminals with rolling luggage as a young girl, her parents Corey and Candi walking alongside her.\n\nBefore the Arthur Ashe Stadium spotlight, there were 5:00 AM drives in rainstorms, public courts in Delray Beach, and two parents who never wavered in their devotion.\n\nBehind every explosive, self-assured champion is a family that chose sacrificial presence over comfort.\n\nAthletic Directors & School Leaders: How are you instilling gratitude and family appreciation in your elite athletic programs?\n\n👉 Empower your sports department with Lornette Daye's keynotes on championship culture and family partnership: lornettedaye.com/speaking\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 5,
        "slot": "Day 2 Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-17T19:00:00.000Z",
        "assetFile": "parents-3-2.png",
        "cta": "Survival Skills for Women Book (lornettedaye.com/books)",
        "text": "THE MOTHER'S QUIET SANCTUARY: CANDI GAUFF'S UNSHAKEABLE POISE. 🌸👑\n\nCandi Gauff was a collegiate Division I heptathlete at Florida State. She knew the physical agony of competitive athletics.\n\nYet when she stepped into Coco's corner, she didn't act like a harsh drill instructor. Candi became Coco's homeschool educator, travel organizer, and emotional sanctuary.\n\nWhen 15-year-old Coco broke down under the suffocating weight of media scrutiny, Candi was the woman who held her hand in hotel rooms and reminded her: \"Tennis is what you do, Coco. It is not who you are.\"\n\nWomen leaders and mothers: Carrying a vision for your family requires profound inner emotional reserves and steadfast grace.\n\n👉 Restore your peace, rebuild inner strength, and thrive through seasons of high pressure. Read *Survival Skills for Women* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 6,
        "slot": "Day 2 Evening (6:00 PM MDT)",
        "dueAt": "2026-09-18T00:00:00.000Z",
        "assetFile": "parents-3-2.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": "SEPARATING WORTH FROM RANKING: LORNETTE'S COACHING TAKEAWAY. 🏛️✨\n\nWhen Corey and Candi Gauff raised Coco, they adhered to a non-negotiable principle:\n\n\"Compliments are like perfume: sniff them, but never swallow them.\"\n\nIn 40+ years guiding elite performers, young athletes who define their worth by ranking points are extraordinarily fragile. One bad season breaks their spirit. But athletes who know their worth is unconditional compete with ferocious freedom.\n\nCoaches & Parents: How do you teach your children to navigate praise and criticism without losing their core identity?\n\n👉 Build enduring legacy and champion mental toughness through life's trials. Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 7,
        "slot": "Day 3 Morning (8:30 AM MDT)",
        "dueAt": "2026-09-18T14:30:00.000Z",
        "assetFile": "parents-3-3.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": "BEN ON BRYAN: \"HE NEVER MADE ME FEEL LIKE HIS LOVE WAS CONDITIONAL.\" 🇺🇸🎾🤝\n\n\"My dad was an ATP pro and an NCAA champion coach,\" Ben Shelton stated. \"He could have pressured me into tennis from day one. But he let me play quarterback, soccer, baseball. When I finally chose tennis, he told me: 'I love you as my son whether you play this sport or not.'\"\n\nLook at Bryan Shelton's eyes in this artwork. He isn't staring at Ben like a technician appraising an investment. He looks at him with the pride of a father who shaped a man of character.\n\n\"Some fathers coach the game; great fathers shape the man.\"\n\nWhen a young man knows his father's approval isn't on the line with every forehand, he steps onto the court with unstoppable confidence.\n\nCollegiate Coaches & Athletic Leaders: How are you supporting coaches navigating high-stakes parent-athlete dynamics?\n\n👉 Keynote Lornette Daye for your sports leadership retreat on coaching boundaries and family resilience: lornettedaye.com/speaking\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 8,
        "slot": "Day 3 Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-18T19:00:00.000Z",
        "assetFile": "parents-3-3.png",
        "cta": "Survival Skills for Men Book (lornettedaye.com/books)",
        "text": "WALKING AWAY FROM TENURE: BRYAN SHELTON'S CAREER SACRIFICE. 🐊🎾\n\nLet us never forget the magnitude of Bryan Shelton's personal sacrifice:\n\nHe held lifetime job security as head coach at the University of Florida, having led the Gators to their first NCAA national championship. He had a top-tier salary, institutional prestige, and a guaranteed pension.\n\nYet when Ben made the leap to the professional circuit, Bryan stepped down from his university post. Why?\n\nBecause Bryan knew the pro tour is a lonely, predatory environment. He chose to pack his own bags, sit on cramped economy flights, and navigate the grind alongside his son.\n\nFathers and male leaders: What comforts are you willing to relinquish so the next generation has a faithful guide?\n\n👉 Lead with purpose, master pressure, and build generational fortitude. Read *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 9,
        "slot": "Day 3 Evening (6:00 PM MDT)",
        "dueAt": "2026-09-19T00:00:00.000Z",
        "assetFile": "parents-3-3.png",
        "cta": "Survival Skills for Athletes Book (lornettedaye.com/books)",
        "text": "THE 24-HOUR CAR RIDE RULE: LORNETTE'S COACHING TAKEAWAY. 🚗⏳\n\nThe most dangerous 30 minutes in youth sports is the car ride home after a loss.\n\nToo many parents turn the back seat into an interrogation chamber. They dissect every missed shot, analyze every error, and suffocate the athlete's passion before they even reach the front door.\n\nBryan Shelton established a master rule: No tennis talk in the car for 24 hours after a match. Let the emotions settle. First, get dinner. Be father and son first.\n\nAthletes & Parents: How does your family handle the immediate aftermath of a brutal loss?\n\n👉 Learn elite emotional composure and champion habits for competitive sport. Read *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 10,
        "slot": "Day 4 Morning (8:30 AM MDT)",
        "dueAt": "2026-09-19T14:30:00.000Z",
        "assetFile": "parents-3-4.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": "NAOMI ON TAMAKI: \"MY MOM SLEPT ON FLOORS SO WE COULD PLAY.\" 🇯🇵🗽🌸\n\n\"My mother is the strongest person I know,\" Naomi Osaka reflected after winning the US Open. \"When we were kids in Long Island, she worked overnight shifts and slept on the floor just so my sister and I could have tennis balls and court time.\"\n\nLook at Tamaki Osaka holding young Naomi's hand with that oversized tennis bag in this artwork.\n\nBefore the world watched Naomi lift Grand Slam trophies and light the Olympic cauldron in Tokyo, Tamaki carried this dream in silence:\n- Working 16-hour shifts without complaint.\n- Enduring cross-cultural alienation and economic insecurity.\n- Never letting bitterness or exhaustion poison her daughters' hearts.\n\nBehind every powerful champion is a parent whose quiet labor laid the cornerstone.\n\nAthletic Directors & Sports Executives: How often do we honor the mothers whose labor makes the spectacle possible?\n\n👉 Book Lornette Daye for keynotes on the human heart behind high-performance sport: lornettedaye.com/speaking\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 11,
        "slot": "Day 4 Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-19T19:00:00.000Z",
        "assetFile": "parents-3-4.png",
        "cta": "Survival Skills for Women Book (lornettedaye.com/books)",
        "text": "16-HOUR NIGHT SHIFTS IN SILENCE: TAMAKI OSAKA'S UNTOLD LABOR. 🕊️✍️\n\nTamaki Osaka never played competitive tennis. She did not know how to teach a kick serve or hit a slice backhand.\n\nHer contribution was far more profound: absolute, sacrificial labor.\n\nWhile Leonard coached the girls on public park courts, Tamaki worked double shifts to pay rent and purchase equipment. She gave her daughters the greatest gift a mother can offer: the living example of a woman who refuses to quit when circumstances are stacked against her.\n\nWomen leaders and mothers: The silent labor you perform today is laying the foundation for a future your children will inherit.\n\n👉 Protect your peace, restore your spirit, and thrive through life's hardest chapters. Read *Survival Skills for Women* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 12,
        "slot": "Day 4 Evening (6:00 PM MDT)",
        "dueAt": "2026-09-20T00:00:00.000Z",
        "assetFile": "parents-3-4.png",
        "cta": "Surviving Life Book (lornettedaye.com/books)",
        "text": "ANXIETY & SAFE HAVENS AT HOME: LORNETTE'S COACHING TAKEAWAY. 🌸🤍\n\nWhen Naomi Osaka courageously spoke out about her battles with depression and social anxiety, the sports world erupted in debate.\n\nDo you know what Tamaki Osaka did?\n\nShe did not read the opinion columns. She opened her arms, held her daughter close, and gave her a safe haven where she was completely shielded from public scrutiny.\n\nIn Olympic sports, an athlete who has a true safe haven at home can endure any storm in the arena. If home is just another stage for performance, emotional breakdown is guaranteed.\n\nParents: Is your home a stage of evaluation, or a sanctuary of unconditional healing?\n\n👉 Rebuild hope, find strength, and discover peace through life's deepest trials. Read *Surviving Life* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 13,
        "slot": "Day 5 Morning (8:30 AM MDT)",
        "dueAt": "2026-09-20T14:30:00.000Z",
        "assetFile": "parents-3-5.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": "MONDO ON GREG: \"HE NEVER FORCED ME TO JUMP. HE JUST MADE IT FUN.\" 🇸🇪🏡🚀\n\n\"The reason I still love pole vaulting at 24,\" Armand 'Mondo' Duplantis explained, \"is that my dad never turned it into a job. He built a pit in our backyard, and we treated it like a game of tag. I jump because it makes me happy.\"\n\nLook at Greg Duplantis smiling with pride as Mondo points to the sky in this artwork.\n\nMondo has broken the World Record more than 10 times, clearing 6.30m+ with effortless grace. But that superhuman aerial mastery didn't originate in a multi-million dollar national training institute. It was forged on grass and plywood behind their house in Lafayette, Louisiana.\n\nWhen parents build an environment of joyful exploration, athletic genius emerges naturally.\n\nCoaches & Sports Leaders: Are you cultivating joy in your training environments, or suffocating passion with rigid pressure?\n\n👉 Book Lornette Daye for your sports leadership seminar on unlocking athletic potential through environment design: lornettedaye.com/speaking\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 14,
        "slot": "Day 5 Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-20T19:00:00.000Z",
        "assetFile": "parents-3-5.png",
        "cta": "Survival Skills for Men Book (lornettedaye.com/books)",
        "text": "GREG DUPLANTIS: THE ART OF PATERNAL EGO SUBORDINATION. 🧗‍♂️✨\n\nGreg Duplantis was an elite pole vaulter himself, clearing 5.80m and competing at the highest international level.\n\nMany athletic fathers who competed at elite levels project their unresolved ambitions onto their sons. They demand perfection to stroke their own egos.\n\nGreg did the exact opposite. Because he had already climbed that mountain, he had nothing to prove. When Mondo wanted to vault until sundown, Greg held the standards. When Mondo wanted to go fishing or play baseball, Greg put the poles away.\n\nParental ego subordination is the greatest gift an athletic father can give.\n\nFathers: Can you step back from managing your child's outcome and simply nurture their spirit?\n\n👉 Master pressure, clarify your mission, and lead your family with wisdom. Read *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 15,
        "slot": "Day 5 Evening (6:00 PM MDT)",
        "dueAt": "2026-09-21T00:00:00.000Z",
        "assetFile": "parents-3-5.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": "PLAY OVER PRESSURE: LORNETTE'S COACHING TAKEAWAY. 🇸🇪🤝\n\nWatch Mondo Duplantis on the runway before an Olympic final. He doesn't look like a condemned man walking to the gallows. He is smiling, bobbing his head to music, and chatting with competitors.\n\nWhy? Because his father Greg and mother Helena protected his relationship with the sport.\n\nIn 40+ years in Olympic athletics, an athlete whose nervous system is relaxed reacts 15% faster than one paralyzed by fear. Playfulness is a massive competitive advantage.\n\nCoaches & Parents: How do you keep the spirit of play alive in high-stakes competition?\n\n👉 Finish your race with endurance, purpose, and lasting legacy. Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 16,
        "slot": "Day 6 Morning (8:30 AM MDT)",
        "dueAt": "2026-09-21T14:30:00.000Z",
        "assetFile": "parents-3-1.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": "CARLOS ON VIRGINIA: \"SHE KEEPS MY FEET ON THE GROUND.\" 🇪🇸🌿\n\n\"My mother doesn't care if I just beat Novak Djokovic in five sets,\" Carlos Alcaraz smiled in a post-match interview. \"When I get home to Murcia, she tells me: 'Clean your room and take out the trash.' That is the greatest blessing of my life.\"\n\nLook at the warmth between Carlos and Virginia Garfia in this artwork.\n\nIn elite sports, fame can distort an athlete's reality. The world tells them they are gods. But a mother's grounding presence reminds them they are human beings who need humility, kindness, and discipline.\n\nHumility isn't weakness; it is the cornerstone of coachability and long-term athletic dominance.\n\nAthletic Directors & Coaches: Are your programs developing athletes of character, or entitled superstars?\n\n👉 Keynote Lornette Daye for your sports leadership summit on building character-driven champions: lornettedaye.com/speaking\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 17,
        "slot": "Day 6 Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-21T19:00:00.000Z",
        "assetFile": "parents-3-1.png",
        "cta": "Survival Skills for Men Book (lornettedaye.com/books)",
        "text": "THE FATHER WHO STEPPED ASIDE: CARLOS SR.'S GREATEST LESSON. 🤝🇪🇸\n\nCarlos Alcaraz Sr. ran the tennis academy at Real Sociedad Club de Campo in El Palmar. He was Carlos's first coach and mentor.\n\nYet when Carlos turned 15 and showed generational talent, Carlos Sr. made a courageous leadership decision:\n\nHe stepped aside as head coach and handed the reins to former World No. 1 Juan Carlos Ferrero.\n\nCarlos Sr. understood that his role as father was infinitely more valuable than his role as tennis coach. By stepping back, he ensured his son would always have an objective coach on court and a loving father at home.\n\nMen: Knowing when to delegate authority for the benefit of those you lead is the mark of mature masculine leadership.\n\n👉 Lead with wisdom, emotional balance, and generational fortitude. Read *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 18,
        "slot": "Day 6 Evening (6:00 PM MDT)",
        "dueAt": "2026-09-22T00:00:00.000Z",
        "assetFile": "parents-3-1.png",
        "cta": "Surviving Life Book (lornettedaye.com/books)",
        "text": "THE COACH-PARENT HAND-OFF: LORNETTE'S COACHING TAKEAWAY. 🎾🏛️\n\nIn 40+ years in Olympic sport, one of the most toxic dynamics occurs when athletic parents refuse to relinquish technical control to professional coaches.\n\nThey stand behind the fence, contradicting the coach's tactical instructions and creating emotional chaos in the young athlete's mind.\n\nCarlos Alcaraz Sr. demonstrated the master standard: Trust the coach to handle the mechanics, and use your parental energy to protect the athlete's character.\n\nParents: Have you built a relationship of mutual trust with your child's coach?\n\n👉 Rebuild hope, find strength, and anchor your family through seasons of transition. Read *Surviving Life* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 19,
        "slot": "Day 7 Morning (8:30 AM MDT)",
        "dueAt": "2026-09-22T14:30:00.000Z",
        "assetFile": "parents-3-2.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": "COCO'S ARTHUR ASHE TRIBUTE: \"MY PARENTS NEVER LET ME QUIT.\" 🇺🇸🎾✨\n\nStanding before 24,000 roaring fans at Arthur Ashe Stadium after winning the US Open, Coco Gauff looked directly into the camera:\n\n\"To my dad who coached me on cracked public courts with second-hand balls, and my mom who homeschooled me on airplanes—thank you for never letting me quit when everyone doubted us.\"\n\nLook at the focus and grit in this visual. The glory of Arthur Ashe was built on thousands of forgotten hours on Florida public courts.\n\nGreat champions do not materialize by accident. They are molded through relentless family commitment.\n\nAthletic Directors & School Leaders: How are you recognizing and celebrating the families behind your standout athletes?\n\n👉 Bring Lornette Daye to your coaching conference or athletic banquet to inspire your community: lornettedaye.com/speaking\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 20,
        "slot": "Day 7 Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-22T19:00:00.000Z",
        "assetFile": "parents-3-2.png",
        "cta": "Survival Skills for Men Book (lornettedaye.com/books)",
        "text": "COREY GAUFF'S VAN TOURS: SACRIFICING CORPORATE SUCCESS. 🚐💨\n\nCorey Gauff had a thriving career in healthcare sales. He could have climbed the corporate ladder in comfort and security.\n\nInstead, he stepped away from corporate life, purchased a minivan, and spent years driving thousands of miles across the American South from one junior tournament to another.\n\nHe dealt with rain delays, flat tires, and budget hotel rooms, all while keeping Coco focused, motivated, and grounded.\n\nPaternal devotion isn't measured in bank account balances; it is measured in hours of faithful presence.\n\nFathers: What legacy are you leaving for your children through your presence?\n\n👉 Strengthen your resilience, clarify your purpose, and lead your household. Read *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 21,
        "slot": "Day 7 Evening (6:00 PM MDT)",
        "dueAt": "2026-09-23T00:00:00.000Z",
        "assetFile": "parents-3-2.png",
        "cta": "Survival Skills for Athletes Book (lornettedaye.com/books)",
        "text": "NAVIGATING PUBLIC SKEPTICISM: LORNETTE'S COACHING TAKEAWAY. 🛡️⚡\n\nWhen Coco Gauff was 13, skeptics claimed her forehand was too flawed to compete on the professional tour.\n\nMany young athletes let critics' opinions shatter their confidence. But Corey and Candi taught Coco to tune out external commentary:\n\n\"Focus on the work in front of you. Mechanics can be rebuilt, but your inner fire is your greatest weapon.\"\n\nAthletes: Are you allowing social media critics to dictate your self-worth?\n\n👉 Build unwavering focus, mental toughness, and champion poise under scrutiny. Read *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 22,
        "slot": "Day 8 Morning (8:30 AM MDT)",
        "dueAt": "2026-09-23T14:30:00.000Z",
        "assetFile": "parents-3-3.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": "BEN ON BRYAN: \"HE TAUGHT ME TO COMPETE LIKE A GENTLEMAN.\" 🐊🇺🇸\n\n\"My dad always told me: 'Hit the ball as hard as you want, but always look your opponent in the eye, shake their hand with respect, and thank the ball kids,'\" Ben Shelton stated after his breakout run at the US Open.\n\nLook at the bond between Ben and Bryan Shelton in this visual.\n\nBryan didn't just teach Ben how to launch a 149-mph left-handed serve. He taught him character, sportsmanship, and locker room accountability during their years together at the University of Florida.\n\nTrue champions are feared for their talent and respected for their character.\n\nCollegiate Coaches & Athletic Leaders: Are your programs instilling integrity and gentlemanly conduct in your young athletes?\n\n👉 Book Lornette Daye for your sports leadership seminar on holistic athlete development: lornettedaye.com/speaking\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 23,
        "slot": "Day 8 Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-23T19:00:00.000Z",
        "assetFile": "parents-3-3.png",
        "cta": "Survival Skills for Men Book (lornettedaye.com/books)",
        "text": "MANAGING FATHER VS. COACH BOUNDARIES: BRYAN SHELTON'S BLUEPRINT. 🎯🎾\n\nHow did Bryan Shelton coach his own son to an NCAA National Championship and an ATP top-15 world ranking without fracturing their relationship?\n\nBy mastering role boundaries:\n- When they walked onto the court, Bryan was Coach Shelton—demanding, analytical, and uncompromising.\n- The moment they walked off, he was Dad—caring, affectionate, and completely detached from the match statistics.\n\nBen never felt that Bryan's love was contingent upon winning tennis matches.\n\nFathers: Can you separate your expectations of performance from your unconditional love for your children?\n\n👉 Master high-pressure relationships, emotional regulation, and purposeful leadership. Read *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 24,
        "slot": "Day 8 Evening (6:00 PM MDT)",
        "dueAt": "2026-09-24T00:00:00.000Z",
        "assetFile": "parents-3-3.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": "RESILIENCE WHEN YOUR SERVE FAILS: LORNETTE'S COACHING TAKEAWAY. ⚡🎾🏆\n\nEven with a 149-mph serve, there are days on the pro tour when your primary weapon misfires.\n\nWhat separates good players from great champions is what they do when their A-game vanishes. Ben Shelton doesn't pester umpires or throw tantrums; he adapts, scrambles, and fights for every single point.\n\nResilience is not the absence of difficulty; it is the refusal to quit when your best weapons fail you.\n\nCompetitors: What do you do when your primary strategy falls apart in high-pressure competition?\n\n👉 Cultivate the elite athlete mindset and rise after setbacks. Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 25,
        "slot": "Day 9 Morning (8:30 AM MDT)",
        "dueAt": "2026-09-24T14:30:00.000Z",
        "assetFile": "parents-3-4.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": "NAOMI'S EMBRACE: \"SHE NEVER JUDGED ME FOR MY STRUGGLES.\" 🌸🤍\n\n\"When the whole world was debating whether I was strong enough to handle press conferences,\" Naomi Osaka shared, \"my mother Tamaki cooked me my favorite meal and held my hand. She never judged me. She just loved me.\"\n\nLook at the tenderness of Tamaki Osaka embracing Naomi in this artwork.\n\nIn modern elite sports, athletes are bombarded with judgment from millions of strangers on social media. What keeps them grounded is knowing that their mother's love is completely independent of public opinion.\n\nA mother's unconditional love is the ultimate mental health shield for high-performing young athletes.\n\nAthletic Directors & School Administrators: How are your athletic departments prioritizing mental wellness alongside physical training?\n\n👉 Book Lornette Daye for your sports conference on supporting athlete mental wellness through family systems: lornettedaye.com/speaking\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 26,
        "slot": "Day 9 Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-24T19:00:00.000Z",
        "assetFile": "parents-3-4.png",
        "cta": "Survival Skills for Women Book (lornettedaye.com/books)",
        "text": "CROSS-CULTURAL SACRIFICES: TAMAKI OSAKA'S SILENT COURAGE. 🇯🇵🗽\n\nThink about the courage it took for Tamaki Osaka:\n\nLeaving her homeland in Japan, moving across the world to the United States, raising two biracial daughters in a sport that had virtually zero Asian-Haitian representation, and working grueling night shifts to fund their tennis dream.\n\nTamaki didn't complain about systemic barriers. She focused on the controllable: her work ethic, her love for her family, and her unyielding belief in her daughters.\n\nWomen leaders: When you stand on a foundation of quiet resilience, cultural barriers cannot stop you.\n\n👉 Renew your inner fortitude, discover meaning in hard seasons, and protect your peace. Read *Survival Skills for Women* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 27,
        "slot": "Day 9 Evening (6:00 PM MDT)",
        "dueAt": "2026-09-25T00:00:00.000Z",
        "assetFile": "parents-3-4.png",
        "cta": "Surviving Life Book (lornettedaye.com/books)",
        "text": "SUPPORTING ATHLETES THROUGH MENTAL HEALTH: LORNETTE'S COACHING TAKEAWAY. 🕊️🌿\n\nIn 40+ years in Olympic sport, I have seen too many coaches treat young athletes like racehorses—valuable only while they are winning medals.\n\nWhen Naomi Osaka took a stand for her mental wellness, Tamaki stood beside her like an unmovable fortress. She proved that protecting an athlete's soul is far more important than protecting commercial endorsement deals.\n\nSports Leaders: If your athletes cannot talk to you about their mental struggles, you do not have a culture of excellence—you have a culture of fear.\n\nCoaches & Parents: How do you create an environment where young athletes feel safe admitting vulnerability?\n\n👉 Rebuild hope, find strength, and live with deep purpose. Read *Surviving Life* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 28,
        "slot": "Day 10 Morning (8:30 AM MDT)",
        "dueAt": "2026-09-25T14:30:00.000Z",
        "assetFile": "parents-3-5.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": "MONDO: \"MY PARENTS ARE THE BEST COACHING DUO IN THE WORLD.\" 🇸🇪🚀\n\n\"People ask me why I don't hire a famous European coaching team,\" Armand 'Mondo' Duplantis said after setting another World Record. \"Why would I? My dad Greg knows the mechanics of the pole vault better than anyone, and my mom Helena understands my nutrition and recovery. Together, they are unbeatable.\"\n\nLook at the sheer joy between Mondo and Greg in this artwork.\n\nMondo's success is a family triumph:\n- Father Greg (Olympian vaulter): Biomechanical mastery and takeoff dynamics.\n- Mother Helena (Heptathlete & volleyball player): Conditioning, recovery, and emotional balance.\n- Brothers: Life-long training partners and grounding brotherhood.\n\nFamily synergy in sports creates a competitive fortress that outside rivals cannot breach.\n\nAthletic Directors & Sports Executives: How are you creating environments that integrate families into student-athlete success?\n\n👉 Keynote Lornette Daye for your sports leadership symposium on unlocking generational athletic potential: lornettedaye.com/speaking\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 29,
        "slot": "Day 10 Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-25T19:00:00.000Z",
        "assetFile": "parents-3-5.png",
        "cta": "Survival Skills for Women Book (lornettedaye.com/books)",
        "text": "HELENA'S QUIET SCIENCE: THE MOTHER BEHIND MONDO'S PHYSICAL ENGINE. 🌸🏋️‍♀️\n\nWhile Greg Duplantis worked with Mondo on pole flexibility and approach speed, Helena Duplantis was the architect of Mondo's physical longevity.\n\nAs a former Swedish national heptathlete, Helena understood strength ratios, injury prevention, and nutritional periodization. She ensured that Mondo's joints, tendons, and muscles could withstand the immense G-forces of bending a 5.20m carbon fiber pole hundreds of times each season.\n\nMothers: Your practical wisdom and attention to daily wellness are often the invisible difference between an athlete's triumph and career-ending injury.\n\n👉 Protect your energy, cultivate daily balance, and lead your family with wisdom. Read *Survival Skills for Women* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 30,
        "slot": "Day 10 Evening (6:00 PM MDT)",
        "dueAt": "2026-09-26T00:00:00.000Z",
        "assetFile": "parents-3-5.png",
        "cta": "Survival Skills for Athletes Book (lornettedaye.com/books)",
        "text": "BIOMECHANICS MEETS PURE JOY: LORNETTE'S COACHING TAKEAWAY. 🧗‍♂️✨\n\nIn pole vaulting, technical precision is paramount. A mistake of two centimeters at takeoff can send a vaulter crashing into the box.\n\nYet Mondo Duplantis executes with absolute relaxation because Greg and Helena taught him that biomechanical discipline is the vehicle that unlocks creative joy.\n\nWhen technique is so ingrained that it becomes second nature, the conscious mind shuts off, and the athlete enters pure flow state.\n\nAthletes: Are you over-thinking your mechanics during competition, or allowing your training to flow?\n\n👉 Train the inner focus, mental composure, and champion discipline of elite performers. Read *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 31,
        "slot": "Day 11 Morning (8:30 AM MDT)",
        "dueAt": "2026-09-26T14:30:00.000Z",
        "assetFile": "parents-3-1.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": "WINNING WITH HUMILITY: CARLOS ALCARAZ'S SPANISH HERITAGE. 🇪🇸🎾\n\nWatch Carlos Alcaraz after winning an exhausting 5-hour Grand Slam battle.\n\nHe hugs his beaten opponent at the net. He acknowledges the chair umpire with respect. He applauds the line judges and ball kids. He signs autographs for young fans until the stadium security ushers him away.\n\nWhy? Because his parents, Carlos Sr. and Virginia Garfia, instilled in him that tennis is a privilege, not a pass to behave arrogantly.\n\nIn collegiate athletics and youth academies, character is the ultimate force multiplier. An athlete with humility remains coachable, adaptable, and emotionally resilient.\n\nCoaches & Athletic Leaders: Are you cultivating athletes who are feared for their talent, or respected for their character?\n\n👉 Keynote Lornette Daye for your sports conference on character-driven athletic development: lornettedaye.com/speaking\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 32,
        "slot": "Day 11 Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-26T19:00:00.000Z",
        "assetFile": "parents-3-1.png",
        "cta": "Survival Skills for Men Book (lornettedaye.com/books)",
        "text": "CARLOS SR.'S QUIET FORTITUDE: WALKING IN THE SHADOWS. 🤝🇪🇸\n\nMany fathers of sports prodigies make themselves the story. They give loud press interviews, wear ostentatious apparel, and demand camera time in the player box.\n\nCarlos Alcaraz Sr. does the exact opposite.\n\nHe sits quietly in the corner of the box, dressed in simple clothing, with arms folded and eyes focused on his son. He doesn't crave the spotlight. He has already won the only prize that matters to him: seeing his boy grow into a respectful, honorable young man.\n\nQuiet strength is always more powerful than noisy bravado.\n\nFathers: Can you lead from the background and let your son shine?\n\n👉 Clarify your purpose, manage pressure, and lead your family with steady fortitude. Read *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 33,
        "slot": "Day 11 Evening (6:00 PM MDT)",
        "dueAt": "2026-09-27T00:00:00.000Z",
        "assetFile": "parents-3-1.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": "THE LONG GAME IN HIGH PERFORMANCE: LORNETTE'S COACHING TAKEAWAY. ⏳🎾\n\nIn my 40+ years in Olympic athletics, the athletes who sustain a 15-year career at the summit are not the ones who sprinted out of the gates at 14.\n\nThey are the ones whose parents played the long game:\n- Prioritizing physical longevity over early junior ranking points.\n- Refusing to play injured just to chase prize money.\n- Ensuring their education and character developed in parallel with their sport.\n\nCarlos Alcaraz is built to dominate for a decade because his parents built his foundation with patient bricklaying, not quick shortcuts.\n\nSports Parents: Are you building your young athlete for a single tournament trophy, or for lifetime excellence?\n\n👉 Learn the endurance, purpose, and perseverance of Olympic champions. Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 34,
        "slot": "Day 12 Morning (8:30 AM MDT)",
        "dueAt": "2026-09-27T14:30:00.000Z",
        "assetFile": "parents-3-2.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": "BELIEF WHEN THE WORLD DOUBTED: CANDI GAUFF'S UNSHAKEABLE FAITH. 🌸🙏\n\nWhen Coco Gauff was 12 years old, scouts questioned whether her unconventional forehand could survive the brutal power of the WTA tour.\n\nCandi Gauff never allowed the critics' doubts to enter their household. She knew that technical mechanics can be retooled, but an athlete's inner fire and self-worth cannot be bought.\n\nThe unshakeable belief a mother pours into her daughter's heart is more powerful than any scout's evaluation.\n\nMothers & Mentors: The words of faith you speak over your children today will echo when they face their greatest trials.\n\n👉 Book Lornette Daye for keynotes on empowering women in sports and cultivating unshakeable inner resilience: lornettedaye.com/speaking\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 35,
        "slot": "Day 12 Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-27T19:00:00.000Z",
        "assetFile": "parents-3-2.png",
        "cta": "Survival Skills for Women Book (lornettedaye.com/books)",
        "text": "CANDI GAUFF'S EMOTIONAL RESERVE: POURING FROM A FULL CUP. 🕊️👑\n\nHow does a mother travel 40 weeks a year, manage homeschooling curricula, coordinate logistics, and stay emotionally grounded?\n\nBy cultivating her own spiritual and emotional reserves.\n\nCandi Gauff makes time for quiet reflection, prayer, and personal boundaries. She understands that if the mother collapses under stress, the entire family structure wobbles.\n\nWomen leaders and mothers: Are you burning out by neglecting your own wellness, or are you prioritizing your inner peace?\n\n👉 Rebuild your emotional foundation, protect your boundaries, and thrive with meaning. Read *Survival Skills for Women* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 36,
        "slot": "Day 12 Evening (6:00 PM MDT)",
        "dueAt": "2026-09-28T00:00:00.000Z",
        "assetFile": "parents-3-2.png",
        "cta": "Survival Skills for Athletes Book (lornettedaye.com/books)",
        "text": "GRATITUDE AS A COMPETITIVE ADVANTAGE: LORNETTE'S COACHING TAKEAWAY. 🎾❤️\n\nAn entitled athlete is a fragile athlete.\n\nThe moment adversity strikes—a bad line call, a sprained ankle, or a rain delay—the entitled athlete looks for someone to blame.\n\nA grateful athlete is indestructible. Because Coco Gauff recognizes the immense sacrifices Corey and Candi made, she views every match point as an opportunity to honor her family, not an unfair burden. Gratitude replaces anxiety with power.\n\nAthletes: When was the last time you expressed genuine gratitude to the people funding and driving your athletic pursuit?\n\n👉 Train the inner maturity, gratitude, and mental toughness of champions. Read *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 37,
        "slot": "Day 13 Morning (8:30 AM MDT)",
        "dueAt": "2026-09-28T14:30:00.000Z",
        "assetFile": "parents-3-3.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": "TRUST IN THE HEAT OF 5TH-SET TIEBREAKS: BEN & BRYAN SHELTON. 🎯⚡\n\nWhen you are down 4-5 in a fifth-set tiebreak on Arthur Ashe Stadium in front of 24,000 spectators, you cannot fake trust.\n\nBen Shelton looks into his player box and locks eyes with his father Bryan.\n\nThere is no panic. There are no frantic gestures. There is only mutual, unshakeable trust forged over two decades of honest communication, shared sweat, and mutual respect. That multi-decade foundation allows Ben to swing freely through the ball.\n\nAthletes: Do you have people in your corner who tell you the truth, or just people who flatter your ego?\n\n👉 Book Lornette Daye for your sports leadership seminar on building unbreakable trust between coaches and athletes: lornettedaye.com/speaking\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 38,
        "slot": "Day 13 Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-28T19:00:00.000Z",
        "assetFile": "parents-3-3.png",
        "cta": "Survival Skills for Men Book (lornettedaye.com/books)",
        "text": "TOUGH LOVE DELIVERED WITH GRACE: BRYAN SHELTON'S COACHING PHILOSOPHY. 🐊🇺🇸\n\nWhen Ben Shelton sprays three forehands into the stands, Bryan Shelton does not mince words.\n\nHis technical feedback is direct, demanding, and uncompromising. But he delivers it with love, never with sarcasm, contempt, or personal rejection.\n\nYoung men crave demanding standards delivered by men who genuinely love them. Without standards, there is no technical excellence. Without love, there is resentment.\n\nFathers and mentors: Mastering the balance between high standards and deep affection is the hallmark of elite masculine leadership.\n\n👉 Strengthen your emotional fortitude, lead with conviction, and master pressure. Read *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 39,
        "slot": "Day 13 Evening (6:00 PM MDT)",
        "dueAt": "2026-09-29T00:00:00.000Z",
        "assetFile": "parents-3-3.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": "RISING AGAIN AFTER DEFEAT: LORNETTE'S COACHING TAKEAWAY. ⚡🎾🏆\n\nIn professional tennis, even the world's best players lose matches nearly every single month.\n\nWhen Ben Shelton loses a match, you do not see him sulking on social media or pointing fingers at coaches. Within 48 hours, he is back on the practice court with Bryan, dissecting video footage and working on his return of serve.\n\nIn 40+ years in Olympic sport, I tell every competitor: Defeat is not your enemy; defeat is the curriculum.\n\nCompetitors & Leaders: How fast do you reset after life breaks your serve?\n\n👉 Cultivate the elite athlete mindset and learn to rise after every setback. Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 40,
        "slot": "Day 14 Morning Finale (8:30 AM MDT)",
        "dueAt": "2026-09-29T14:30:00.000Z",
        "assetFile": "parents-3-6.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": "BEHIND GREAT CHAMPIONS, SOMEONE KEPT SHOWING UP. 🌟👑🏆\n\nLook at this master visual of five world champions and the families who built them:\n- Carlos Alcaraz & Carlos Sr. and Virginia Garfia 🇪🇸\n- Coco Gauff & Corey and Candi Gauff 🇺🇸\n- Ben Shelton & Bryan Shelton 🐊\n- Naomi Osaka & Tamaki Osaka 🇯🇵\n- Armand 'Mondo' Duplantis & Greg and Helena Duplantis 🇸🇪\n\nFive different sports paths. Five different nations. One undeniable universal truth:\n\nNO CHAMPION EVER ARRIVED AT THE PODIUM ALONE.\n\nBehind every Grand Slam trophy, every World Record clearance, and every roaring stadium moment are parents who woke up at 4:30 AM, drove thousands of miles, sacrificed their personal comforts, and believed in their children long before the world knew their names.\n\nSports Leaders, Athletic Directors & Educators: Are you honoring and supporting the families behind your student-athletes?\n\n👉 Book Lornette Daye for your sports gala, university conference, or corporate keynote: lornettedaye.com/speaking\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 41,
        "slot": "Day 14 Mid-day Finale (1:00 PM MDT)",
        "dueAt": "2026-09-29T19:00:00.000Z",
        "assetFile": "parents-3-6.png",
        "cta": "Surviving Life Book (lornettedaye.com/books)",
        "text": "THE ANATOMY OF SACRIFICE: WHAT THE CAMERAS NEVER SHOW. 🕊️✨\n\nWhen you look at this magnificent artwork of champions and their parents, remember what isn't shown:\n- The second mortgages taken to finance coaching fees.\n- The 16-hour night shifts worked by mothers like Tamaki Osaka.\n- The comfortable careers walked away from by fathers like Bryan Shelton.\n- The thousands of weekends sacrificed by Corey and Candi Gauff.\n- The backyard runways built with bare hands by Greg Duplantis.\n\nSacrifice is rarely glamorous in the moment. It is exhausting, lonely, and filled with doubt.\n\nYet love makes sacrifice worthwhile. When a family is anchored in purpose, hardship does not break them—it binds them together forever.\n\nTo every parent grinding in obscurity today for your child's future: Your sacrifice is seen.\n\n👉 Rebuild hope, find strength, and embrace purpose through life's deepest trials. Read *Surviving Life* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
    },
    {
        "id": 42,
        "slot": "Day 14 Evening Grand Campaign Finale (6:00 PM MDT)",
        "dueAt": "2026-09-30T00:00:00.000Z",
        "assetFile": "parents-3-6.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": "THE GREATEST TROPHY IS THE RELATIONSHIP. 🏆❤️🌟\n\nAs our 14-day campaign honoring sports parents comes to a close, consider this reflection from 40+ years in Olympic athletics:\n\nGold medals will eventually tarnish in glass display cases.\nWorld records will eventually be eclipsed by the next generation.\nThe stadium applause fades the moment you walk out of the tunnel.\n\nWhat remains?\n\nThe father who held your hand when nobody believed.\nThe mother who dried your tears after heartbreaking defeats.\nThe family that loved you when you had zero ranking points.\n\nThe ultimate victory of athletic competition is not the trophy you hold in your hands—it is the character you build and the family bonds that endure a lifetime.\n\nTo every parent, coach, and athlete striving for excellence: Protect your foundation, honor your roots, and finish strong.\n\n👉 Build enduring legacy and champion discipline in every stage of life. Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n#BehindGreatChampions #SportsParents #ParentingChampions #CarlosAlcaraz #CocoGauff #BenShelton #NaomiOsaka #MondoDuplantis #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation #SomeoneKeptShowingUp"
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
    print("Starting Buffer queue scheduling for Parents Set 3 Campaign (4 posts)...")
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
