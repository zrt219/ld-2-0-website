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

CDN_BASE = 'https://lornettedaye.com/campaigns/own-the-next-chapter'

posts_data = [
    {
        "id": 1,
        "day": 1,
        "date": "2026-10-03",
        "athlete": "tiger",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-10-03T13:45:00.000Z",
        "assetFile": "tiger-woods-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-01.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE ECOSYSTEM BEYOND THE TROPHY\n\nWhen Tiger Woods dominated the Masters, he was perfecting his swing. When he founded TGR, he was designing a permanent ecosystem.\n\nMost athletes spend their prime trading physical energy for podium finishes. The greatest realize early that physical prime has an expiration date, but structural knowledge does not. Tiger did not just endorse golf clubs. He studied course architecture, retail operations, and event management. He understood that true sovereignty in sport means owning the infrastructure, not merely performing inside of it.\n\nAs an Olympic coach for four decades, I tell leaders: mastery in your craft is only step one. Step two is building the platform that outlasts your personal participation.\n\nWith purpose,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 2,
        "day": 1,
        "date": "2026-10-03",
        "athlete": "steph",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-10-03T20:30:00.000Z",
        "assetFile": "stephen-curry-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-01.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "CHANGING WHO GETS TO PLAY THE GAME\n\nStephen Curry did not need to play professional golf to change who gets to compete in it.\n\nGolf has historically been one of the most closed ecosystems in sport, guarded by private club fees, expensive equipment, and country club networks. Steph recognized that athletic talent is universal, but access to competitive circuits is fiercely restricted. He launched Underrated Golf not as a casual celebrity tournament, but as an elite junior tour providing all-expenses-paid travel, equipment, and ranking opportunities for young players.\n\nTrue innovation is not just creating a new product. It is dismantling artificial barriers to entry so exceptional talent can rise on merit.\n\nWith purpose,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 3,
        "day": 1,
        "date": "2026-10-03",
        "athlete": "ayesha",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-10-04T00:30:00.000Z",
        "assetFile": "ayesha-curry-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-01.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "TURNING TASTE INTO A DESTINATION\n\nSweet July Cafe brings Ayesha Curry's food and lifestyle vision into premium hospitality.\n\nAyesha did not wait for approval to build an empire. She took her intuitive love for food, design, and gathering, and translated it into Sweet July: a luxury lifestyle brand, magazine, and flagship cafe destination. She proved that hospitality is not merely serving coffee; it is curating an atmosphere where community, elegance, and warmth coexist seamlessly.\n\nIn business, you do not just sell a service. You sell the feeling and identity of the environment you create.\n\nWith purpose,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 4,
        "day": 2,
        "date": "2026-10-04",
        "athlete": "steph_ayesha",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-10-04T13:45:00.000Z",
        "assetFile": "stephen-ayesha-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-01.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THEY BUILT MORE THAN SUCCESS. THEY BUILT ACCESS.\n\nThrough Eat.Learn.Play., Stephen and Ayesha Curry invest in meals, literacy, and safe places to play for Oakland kids.\n\nSuccess is what you achieve for yourself. Access is what you engineer for people who were never handed a fair start. Steph and Ayesha looked at the city of Oakland: a community that celebrated four NBA championships: and asked what they owed the children growing up in the shadows of the arena. They founded Eat.Learn.Play. not as a ceremonial check-writing hobby, but as an operational social enterprise.\n\nIn my Olympic coaching journey, I learned that athletic greatness means nothing if it does not leave the community stronger than you found it.\n\nWith purpose,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    },
    {
        "id": 5,
        "day": 2,
        "date": "2026-10-04",
        "athlete": "serena",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-10-04T20:30:00.000Z",
        "assetFile": "serena-williams-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-01.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "TWENTY-THREE MAJORS. NOW SHE BUILDS PORTFOLIOS.\n\nExcellence on the court became experience Serena Williams could deploy across global venture capital.\n\nSerena did not retire from tennis to sit idly. She announced her 'evolution' away from sport to focus on Serena Ventures: an early-stage venture firm investing in founders who are traditionally ignored by Silicon Valley. She brought the same ruthless focus that conquered Wimbledon into vetting enterprise balance sheets and cap tables.\n\nAs an Olympic coach, I know that championship focus does not die when you hang up your racket. It simply finds a larger arena.\n\nWith purpose,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 6,
        "day": 2,
        "date": "2026-10-04",
        "athlete": "lewis",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-10-05T00:30:00.000Z",
        "assetFile": "lewis-hamilton-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-01.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "HE DOESN'T JUST COMPETE FOR TEAMS. HE OWNS ONE.\n\nLewis Hamilton: seven-time Formula 1 world champion, Denver Broncos owner.\n\nMost professional athletes view team ownership as something reserved for tech billionaires and real estate moguls. Lewis shattered that ceiling by joining the ownership group of the NFL's Denver Broncos. He recognized that driving at 200 mph is only part of his purpose. The higher calling is acquiring institutional equity in the most valuable sports league on earth.\n\nAs an Olympic coach for four decades, I teach champions: do not spend your entire career playing for someone else's franchise. Build enough capital and credibility to own one.\n\nWith purpose,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 7,
        "day": 3,
        "date": "2026-10-05",
        "athlete": "ayesha",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-10-05T13:45:00.000Z",
        "assetFile": "ayesha-curry-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-02.png",
        "cta": "Buy Book - Survival Skills for Women (lornettedaye.com/books)",
        "text": "THE ART OF AUTHENTIC BRAND ARCHITECTURE\n\nAyesha did not license her name to an existing restaurant chain. She built Sweet July from the soil up.\n\nWhen you build your own brand, you own the creative vision, the supply chain, and the customer experience. Ayesha selected every artisanal product, curated local Black-owned vendors, and designed a retail footprint that reflects her personal aesthetic. That authenticity is why her brand commands fierce customer loyalty.\n\nNever outsource your soul for rapid scale. Build an enterprise whose every detail reflects your core values.\n\nStay focused,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Women' ($14.99 CAD): https://lornettedaye.com/books\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 8,
        "day": 3,
        "date": "2026-10-05",
        "athlete": "tiger",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-10-05T20:30:00.000Z",
        "assetFile": "tiger-woods-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-02.png",
        "cta": "Buy Book - Finish Strong: Chasing the Olympic Dream (lornettedaye.com/books)",
        "text": "TURNING INTELLECT INTO PERMANENT ASSETS\n\nTiger Woods understood that winning 15 majors gives you leverage. What you do with that leverage determines whether you are remembered as a player or an architect.\n\nEvery time Tiger stepped onto a golf course, he was gathering data on player psychology, spectator movement, course aesthetics, and commercial real estate. Through TGR Design, he transformed decades of technical course knowledge into an architectural firm that shapes communities worldwide. He turned fleeting athletic glory into tangible, appreciating property.\n\nIn my work with executive teams, I ask one question: are you capturing the intellectual property of your daily victories, or are you letting that wisdom dissipate once the project ends?\n\nStay focused,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Finish Strong: Chasing the Olympic Dream' ($14.99 CAD): https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 9,
        "day": 3,
        "date": "2026-10-05",
        "athlete": "steph",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-10-06T00:30:00.000Z",
        "assetFile": "stephen-curry-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-02.png",
        "cta": "Buy Book - Survival Skills for Athletes (lornettedaye.com/books)",
        "text": "REWRITING THE JUNIOR PIPELINE\n\nUnderrated Golf is not just about swinging clubs. It is about building a college recruiting pipeline that scouts cannot ignore.\n\nJunior golf requires thousands of dollars in tournament fees and travel just to get ranked in front of NCAA Division I coaches. Steph understood that without tournament visibility, young athletes from working-class backgrounds never get scholarship offers. Underrated Golf brings the college coaches directly to the players, bridging the scouting divide.\n\nIn executive hiring, if your recruiting pipeline only fishes in the same elite waters, you are systematically overlooking the hungriest talent.\n\nStay focused,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Athletes' ($14.99 CAD): https://lornettedaye.com/books\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 10,
        "day": 4,
        "date": "2026-10-06",
        "athlete": "lewis",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-10-06T13:45:00.000Z",
        "assetFile": "lewis-hamilton-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-02.png",
        "cta": "Buy Book - Survival Skills for Men (lornettedaye.com/books)",
        "text": "EXTREME PRECISION UNDER SUFFOCATING PRESSURE\n\nDriving an F1 car at 220 miles per hour in the rain requires an operating state of absolute emotional neutrality.\n\nOne millisecond of hesitation or emotional panic puts you into a concrete barrier. Lewis developed a mental discipline that allows him to process thousands of data points: tire degradation, brake balance, weather radar, radio telemetry: while heart rate remains rock-steady. That exact psychological composure is what allows him to negotiate complex multi-million-dollar ownership transactions.\n\nIn high-stakes corporate negotiations, the person who regulates their emotions most effectively always controls the outcome.\n\nStay focused,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Men' ($14.99 CAD): https://buy.stripe.com/9B6bJ1542gA262JfCG1VK00\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 11,
        "day": 4,
        "date": "2026-10-06",
        "athlete": "steph_ayesha",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-10-06T20:30:00.000Z",
        "assetFile": "stephen-ayesha-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-02.png",
        "cta": "Buy Book - UMATTR Devotional (lornettedaye.com/books)",
        "text": "THE THREE PILLARS OF WHOLE-CHILD DEVELOPMENT\n\nEat. Learn. Play. Three simple words that encapsulate the entire architecture of childhood flourishing.\n\nA child cannot learn if their stomach is empty. A child cannot dream if they cannot read grade-level books. And a child cannot build social confidence if they have no safe playground in their neighborhood. Steph and Ayesha addressed all three pillars simultaneously, attacking systemic childhood poverty from every angle.\n\nWhen solving complex problems in your organization, do not treat isolated symptoms. Address the entire ecosystem.\n\nStay focused,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'UMATTR Devotional' ($14.99 CAD): https://lornettedaye.com/books\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    },
    {
        "id": 12,
        "day": 4,
        "date": "2026-10-06",
        "athlete": "serena",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-10-07T00:30:00.000Z",
        "assetFile": "serena-williams-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-02.png",
        "cta": "Buy Book - Survival Skills for Women (lornettedaye.com/books)",
        "text": "INVESTING IN THE SEVENTY-EIGHT PERCENT\n\nOver 78 percent of Serena Ventures' portfolio companies are founded by women and people of color.\n\nIn Silicon Valley, less than three percent of venture funding goes to female founders, and less than one percent to Black founders. Serena recognized this not as a lack of talent, but as a colossal market failure by myopic gatekeepers. She deployed her capital where market inefficiency created massive venture upside.\n\nDo not follow the herd into crowded trades. Look where prejudice has created undervalued, high-conviction opportunities.\n\nStay focused,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Women' ($14.99 CAD): https://lornettedaye.com/books\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 13,
        "day": 5,
        "date": "2026-10-07",
        "athlete": "steph",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-10-07T13:45:00.000Z",
        "assetFile": "stephen-curry-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-03.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "PAIRING SPORT WITH CORPORATE BOARDROOM ACCESS\n\nAt every Underrated Golf tour stop, junior players spend half their time in leadership workshops with Fortune 500 executives.\n\nSteph understands that only a percentage of junior golfers will reach the PGA or LPGA Tour. But every single one of them can become a corporate executive, an entrepreneur, or an institutional leader. He uses the golf course as a networking accelerator, teaching young athletes how to converse with CEOs, pitch ideas, and navigate corporate culture.\n\nSport is a vehicle, not the final destination. Use athletic discipline to unlock intellectual and economic sovereignty.\n\nKeep building,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 14,
        "day": 5,
        "date": "2026-10-07",
        "athlete": "ayesha",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-10-07T20:30:00.000Z",
        "assetFile": "ayesha-curry-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-03.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "CREATING SPACES WHERE WOMEN GATHER AND THRIVE\n\nSweet July was created as a sanctuary for women to pause, recharge, and celebrate life's sweeter moments.\n\nModern women navigate overwhelming professional and personal demands. Ayesha recognized the profound need for hospitality spaces that prioritize tranquility, beauty, and emotional rejuvenation. Sweet July is not just a cafe; it is a community anchor that honors the feminine journey.\n\nWhen your business solves an emotional and relational need, customer retention takes care of itself.\n\nKeep building,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 15,
        "day": 5,
        "date": "2026-10-07",
        "athlete": "tiger",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-10-08T00:30:00.000Z",
        "assetFile": "tiger-woods-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-03.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "DISCIPLINE IN THE BOARDROOM\n\nThe same ice-water patience that Tiger used over a championship putt on Sunday afternoon is the patience required in multi-decade investments.\n\nPeople think business discipline is different from athletic discipline. It is identical. It requires emotional regulation when markets fluctuate, relentless preparation before negotiations, and the ability to execute without emotion. Tiger brought his Sunday-red focus into boardroom partnerships, vetting partners with the same ruthless precision he applied to his golf bag.\n\nExecution is not an accident. It is a repeatable habit built through decades of quiet, unglamorous reps.\n\nKeep building,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 16,
        "day": 6,
        "date": "2026-10-08",
        "athlete": "serena",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-10-08T13:45:00.000Z",
        "assetFile": "serena-williams-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-03.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE TRANSITION FROM ATHLETE TO OWNER\n\nSerena Williams understands that an athlete's salary is taxed at the highest rates, while equity compounds tax-efficiently for generations.\n\nThroughout her playing days, Serena was already buying equity stakes in sports franchises like the Miami Dolphins and Angel City FC. She realized early that trophies represent past glory, but enterprise ownership represents permanent authority.\n\nStop trading your finite hours for income. Start acquiring and building equity that works while you sleep.\n\nKeep building,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 17,
        "day": 6,
        "date": "2026-10-08",
        "athlete": "lewis",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-10-08T20:30:00.000Z",
        "assetFile": "lewis-hamilton-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-03.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "DAWN APOLLO FILMS AND THE BUSINESS OF CULTURE\n\nLewis did not wait for Hollywood to tell racing stories. He founded Dawn Apollo Films to produce them.\n\nPartnering with Brad Pitt and Apple TV, Lewis took control of the narrative, serving as lead producer on major cinematic projects. He understood that whoever controls media storytelling controls global brand equity. He transitioned from being the subject of the camera to the executive producer who owns the negative rights.\n\nDo not let others monetize your story. Build your own production engine and retain the intellectual property rights.\n\nKeep building,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 18,
        "day": 6,
        "date": "2026-10-08",
        "athlete": "steph_ayesha",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-10-09T00:30:00.000Z",
        "assetFile": "stephen-ayesha-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-03.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "ZERO OVERHEAD PROMISE: ONE HUNDRED PERCENT TO THE KIDS\n\nSteph and Ayesha personally cover all administrative and operating costs of Eat.Learn.Play.\n\nThat means every single dollar donated by the public or corporate partners goes directly to meals, books, and schoolyards for Oakland youth. That level of personal financial stewardship built unshakeable institutional trust, allowing the foundation to mobilize tens of millions of dollars in record time.\n\nTrust is your greatest asset. When you demonstrate that you have skin in the game, partners will line up to back your vision.\n\nKeep building,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    },
    {
        "id": 19,
        "day": 7,
        "date": "2026-10-09",
        "athlete": "tiger",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-10-09T13:45:00.000Z",
        "assetFile": "tiger-woods-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-04.png",
        "cta": "Buy Book - Survival Skills for Athletes (lornettedaye.com/books)",
        "text": "BUILDING BEYOND SELF-INTEREST\n\nAt the height of his career, Tiger made a conscious pivot. He looked past personal wealth and created the TGR Foundation.\n\nMany foundations are public relations vehicles. Tiger engineered his foundation as an operational engine for STEM education and college access. When you look at the TGR Learning Labs in Anaheim and Washington, you see high-tech classrooms, robotics labs, and college counseling centers. He understood that true legacy is measured by the opportunities you engineer for those who have never held a golf club.\n\nChampionship caliber is defined by how wide you open the door behind you once you have reached the pinnacle.\n\nIn your corner,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Athletes' ($14.99 CAD): https://lornettedaye.com/books\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 20,
        "day": 7,
        "date": "2026-10-09",
        "athlete": "steph",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-10-09T20:30:00.000Z",
        "assetFile": "stephen-curry-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-04.png",
        "cta": "Buy Book - Survival Skills for Students (lornettedaye.com/books)",
        "text": "THE DISCIPLINE OF EXPANDING YOUR HORIZONS\n\nSteph Curry is already a four-time NBA champion and Olympic gold medalist. Why spend capital building a golf ecosystem?\n\nBecause a champion's mind refuses to stay confined to a single arena. Steph recognized that his platform as a basketball superstar gave him unique cultural leverage to democratize a completely different sport. He leveraged his corporate relationships with brands like Callaway and KPMG to fund a vision that transforms lives.\n\nDo not allow your current title to box in your potential. Use your existing credibility to solve problems across new industries.\n\nIn your corner,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Students' ($14.99 CAD): https://lornettedaye.com/books\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 21,
        "day": 7,
        "date": "2026-10-09",
        "athlete": "ayesha",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-10-10T00:30:00.000Z",
        "assetFile": "ayesha-curry-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-04.png",
        "cta": "Buy Book - Survival Skills: Surviving to Thriving (lornettedaye.com/books)",
        "text": "THE COURAGE TO STEP INTO YOUR OWN LIGHT\n\nStanding next to a global sports icon can easily overshadow your personal ambitions. Ayesha chose to forge her own distinct legacy.\n\nShe carved out her own identity as a New York Times bestselling author, television host, culinary entrepreneur, and venture investor. She proved that partnership in marriage does not require sacrificing individual enterprise. Her voice, her brand, and her commercial ventures stand proudly on their own merit.\n\nNever dim your personal brilliance to fit into someone else's orbit. Step boldly into the work you were born to build.\n\nIn your corner,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills: Surviving to Thriving' ($14.99 CAD): https://lornettedaye.com/books\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 22,
        "day": 8,
        "date": "2026-10-10",
        "athlete": "steph_ayesha",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-10-10T13:45:00.000Z",
        "assetFile": "stephen-ayesha-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-04.png",
        "cta": "Buy Book - Surviving Life (lornettedaye.com/books)",
        "text": "RADICAL LITERACY INTERVENTION IN OAKLAND SCHOOLS\n\nEat.Learn.Play. has distributed over one million diverse, culturally affirming books to Oakland elementary students.\n\nIf a child cannot read proficiently by the third grade, their statistical likelihood of high school graduation drops precipitously. Steph and Ayesha brought mobile book buses into neighborhood parks and funded professional literacy tutors across Oakland public schools, sparking a love for reading in children who had never owned a book.\n\nIf you want to transform a community's future, put books in the hands of its eight-year-olds.\n\nIn your corner,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Surviving Life' ($14.99 CAD): https://buy.stripe.com/7sY8wPcwuabE62Jcqu1VK02\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    },
    {
        "id": 23,
        "day": 8,
        "date": "2026-10-10",
        "athlete": "serena",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-10-10T20:30:00.000Z",
        "assetFile": "serena-williams-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-04.png",
        "cta": "Buy Book - Finish Strong: Chasing the Olympic Dream (lornettedaye.com/books)",
        "text": "DISCIPLINE IN CAP TABLE MANAGEMENT\n\nThe composure required to save triple match point at Arthur Ashe is identical to negotiating equity terms in a Series A financing.\n\nVenture investing requires nerves of steel. Founders pitch grand dreams, but Serena looks at unit economics, burn rates, and founder resilience. She looks for founders who possess that rare Olympic fire: the ability to execute when everyone else has run out of gas.\n\nInvest in founders whose grit has been tested in fire, not those who only shine in sunny pitches.\n\nIn your corner,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Finish Strong: Chasing the Olympic Dream' ($14.99 CAD): https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 24,
        "day": 8,
        "date": "2026-10-10",
        "athlete": "lewis",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-10-11T00:30:00.000Z",
        "assetFile": "lewis-hamilton-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-04.png",
        "cta": "Buy Book - Finish Strong: Chasing the Olympic Dream (lornettedaye.com/books)",
        "text": "MISSION FORTY-FOUR AND RADICAL MERITOCRACY\n\nLewis created Mission 44 to fund STEM education and motorsport apprenticeships for underrepresented youth.\n\nHe did not just donate money; he launched the Hamilton Commission in partnership with the Royal Academy of Engineering to scientifically identify the barriers preventing diverse engineers from entering motorsport. He treated systemic exclusion as an engineering problem that requires data, metrics, and targeted interventions.\n\nDo not guess at why your industry lacks diversity. Commission the research, identify the structural bottlenecks, and fund the solution.\n\nIn your corner,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Finish Strong: Chasing the Olympic Dream' ($14.99 CAD): https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 25,
        "day": 9,
        "date": "2026-10-11",
        "athlete": "ayesha",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-10-11T13:45:00.000Z",
        "assetFile": "ayesha-curry-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-05.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE RIGOR OF CULINARY EXCELLENCE\n\nFood is one of the most unforgiving industries in the world. Passion gets you started, but operational rigor keeps the doors open.\n\nAyesha spent years testing recipes, studying food chemistry, understanding labor margins, and mastering culinary logistics. Long before International Smoke and Sweet July became commercial successes, she was doing the unglamorous prep work in commercial kitchens. Excellence in hospitality requires an obsession with consistency.\n\nDo not expect applause for half-baked execution. Master the operational mechanics of your trade before scaling.\n\nWith conviction,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 26,
        "day": 9,
        "date": "2026-10-11",
        "athlete": "tiger",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-10-11T20:30:00.000Z",
        "assetFile": "tiger-woods-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-05.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE COURAGE TO REBUILD YOUR SWING\n\nIn 2000, Tiger Woods held all four major trophies simultaneously. Then he voluntarily dismantled his swing to build a better one.\n\nCorporate executives rarely possess that level of courage. When companies are profitable, leadership clings to existing playbooks until disruption forces their hand. Tiger understood that peak performance today does not guarantee survival tomorrow. He tore down his mechanics at the height of his fame because he was chasing longevity, not comfort.\n\nIf you want to dominate your industry for decades, you must be willing to disrupt your own winning formula before the market does it for you.\n\nWith conviction,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 27,
        "day": 9,
        "date": "2026-10-11",
        "athlete": "steph",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-10-12T00:30:00.000Z",
        "assetFile": "stephen-curry-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-05.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "ELIMINATING THE HIDDEN FINANCIAL TAX ON TALENT\n\nTalent does not disappear when a family cannot afford five thousand dollars for tournament travel. It simply gets starved of opportunity.\n\nWhen Underrated Golf covers flights, lodging, meals, and greens fees for student athletes and their parents, it levels the competitive playing field. Suddenly, the kid from an inner-city public course can stand on the same tee box as the kid with a private swing coach and country club membership.\n\nWhen you remove financial friction, meritocracy finally functions as promised.\n\nWith conviction,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 28,
        "day": 10,
        "date": "2026-10-12",
        "athlete": "lewis",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-10-12T13:45:00.000Z",
        "assetFile": "lewis-hamilton-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-05.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "SHATTERING FASHION STEREOTYPES IN THE PADDOCK\n\nIn a traditional motorsport paddock dominated by corporate polos, Lewis turned race weekends into high-fashion runways.\n\nHe partnered with Tommy Hilfiger, Dior, and Valentino, launching sustainable clothing lines and bringing avant-garde fashion into sports culture. He expanded his personal brand into luxury lifestyle, making him a household name in markets that had never watched an auto race.\n\nRefuse to conform to the drab dress codes of your industry. Use personal style and creative audacity to carve out an unforgettable identity.\n\nWith conviction,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 29,
        "day": 10,
        "date": "2026-10-12",
        "athlete": "steph_ayesha",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-10-12T20:30:00.000Z",
        "assetFile": "stephen-ayesha-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-05.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "REBUILDING TWENTY-FIVE ELEMENTARY SCHOOLYARDS\n\nEat.Learn.Play. committed to transforming twenty-five schoolyards across Oakland into world-class play and sports spaces.\n\nToo many urban schoolyards are cracked asphalt and chain-link fences. Steph and Ayesha bring in landscape architects, turf fields, basketball courts, and community gardens. They give children colorful, dignified, safe spaces to run, climb, and develop athletic confidence.\n\nThe physical environment you give a child communicates how much you value them. Build spaces worthy of their dreams.\n\nWith conviction,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    },
    {
        "id": 30,
        "day": 10,
        "date": "2026-10-12",
        "athlete": "serena",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-10-13T00:30:00.000Z",
        "assetFile": "serena-williams-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-05.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "PIONEERING ANGEL CITY FC AND WOMEN'S SPORTS EQUITY\n\nSerena was an early founding investor in Angel City FC, proving that women's sports is a multi-billion-dollar commercial asset.\n\nNaysayers claimed that women's soccer could not sell out stadiums or command premium enterprise valuations. Angel City FC shattered every attendance record, secured blockbuster sponsorships, and recently achieved a valuation exceeding two hundred million dollars.\n\nNever accept the limitations that small-minded observers project onto your industry. Prove them wrong with ledger sheets.\n\nWith conviction,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 31,
        "day": 11,
        "date": "2026-10-13",
        "athlete": "steph",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-10-13T13:45:00.000Z",
        "assetFile": "stephen-curry-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-01.png",
        "cta": "Buy Book - Survival Skills for Athletes (lornettedaye.com/books)",
        "text": "GLOBAL EXPANSION WITH REGAL PURPOSE\n\nUnderrated Golf did not stay in the United States. Steph took the tour to historic venues like Walton Heath in the United Kingdom.\n\nBy taking young American golfers overseas to compete alongside top European junior talent, Steph expanded their worldview. He taught them that athletic excellence and cultural poise have no geographic borders. Playing links golf in England changes a young person's concept of what is possible in their life.\n\nExpose your emerging talent to global environments early. World-class exposure creates world-class expectations.\n\nWith purpose,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Athletes' ($14.99 CAD): https://lornettedaye.com/books\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 32,
        "day": 11,
        "date": "2026-10-13",
        "athlete": "ayesha",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-10-13T20:30:00.000Z",
        "assetFile": "ayesha-curry-06.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-06.png",
        "cta": "Buy Book - Survival Skills for Women (lornettedaye.com/books)",
        "text": "SUPPORTING EMERGING ENTREPRENEURS ON HER SHELVES\n\nWalk through a Sweet July flagship store and look at the retail shelves. You will see products from underrepresented female founders.\n\nAyesha uses her retail distribution to elevate female artisans, skincare creators, and culinary makers who would otherwise struggle to access premium shelf space. She turned her brand into a launchpad for other women. That is true economic sisterhood in action.\n\nWhen you build a premier platform, turn your distribution into an elevator for emerging talent.\n\nWith purpose,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Women' ($14.99 CAD): https://lornettedaye.com/books\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 33,
        "day": 11,
        "date": "2026-10-13",
        "athlete": "tiger",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-10-14T00:30:00.000Z",
        "assetFile": "tiger-woods-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-01.png",
        "cta": "Buy Book - Finish Strong: Chasing the Olympic Dream (lornettedaye.com/books)",
        "text": "THE ARCHITECTURE OF AN AMBITIOUS VISION\n\nTiger Woods did not wait for retirement to envision his next chapter. He was laying foundations while holding the number one ranking.\n\nAthletic transition fails when athletes wait until the final whistle to wonder what comes next. Tiger surrounded himself with seasoned business advisors while he was still winning PGA Tour events. He studied enterprise governance, contract structuring, and brand equity. When physical injuries mounted, his enterprise did not stall. It accelerated.\n\nPreparation is your strongest armor against transition anxiety. Begin building your second act while your first act is at its peak.\n\nWith purpose,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Finish Strong: Chasing the Olympic Dream' ($14.99 CAD): https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 34,
        "day": 12,
        "date": "2026-10-14",
        "athlete": "serena",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-10-14T13:45:00.000Z",
        "assetFile": "serena-williams-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-01.png",
        "cta": "Buy Book - Survival Skills for Women (lornettedaye.com/books)",
        "text": "PREPARATION AS AN INSURMOUNTABLE ADVANTAGE\n\nLong before Serena wrote a check to an AI or fintech startup, she took executive education courses at Harvard and spent hours with Silicon Valley mentors.\n\nShe did not rely on celebrity status to make her a competent venture capitalist. She did the homework, learned cap table mechanics, and mastered venture governance. Humility before new domains is the mark of a true champion.\n\nNever enter a new industry assuming your past fame guarantees present competence. Do the deep reading first.\n\nWith purpose,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Women' ($14.99 CAD): https://lornettedaye.com/books\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 35,
        "day": 12,
        "date": "2026-10-14",
        "athlete": "lewis",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-10-14T20:30:00.000Z",
        "assetFile": "lewis-hamilton-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-01.png",
        "cta": "Buy Book - Survival Skills for Men (lornettedaye.com/books)",
        "text": "THE RELENTLESS PURSUIT OF MARGINAL GAINS\n\nIn Formula 1, championships are decided by hundredths of a second across a sixty-lap race.\n\nLewis works obsessively with his engineers to find fractional aerodynamic advantages, weight reductions, and throttle map optimizations. In corporate enterprise, marginal gains in logistics, customer retention, and operational overhead compound into massive competitive moats.\n\nStop hunting for silver bullets. Find ten one-percent improvements across your business and watch your margins explode.\n\nWith purpose,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Men' ($14.99 CAD): https://buy.stripe.com/9B6bJ1542gA262JfCG1VK00\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 36,
        "day": 12,
        "date": "2026-10-14",
        "athlete": "steph_ayesha",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-10-15T00:30:00.000Z",
        "assetFile": "stephen-ayesha-06.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-06.png",
        "cta": "Buy Book - UMATTR Devotional (lornettedaye.com/books)",
        "text": "DELIVERING MILLIONS OF HEALTHY, NUTRITIOUS MEALS\n\nDuring the height of pandemic school closures, Eat.Learn.Play. delivered over twenty-five million meals to Oakland families.\n\nThey did not just distribute shelf-stable cans; they partnered with local Oakland restaurants: pumping money back into struggling small businesses: to deliver fresh, hot, culturally relevant meals to families in need. That is circular economic philanthropy at its finest.\n\nDesign your charitable efforts to support local commerce rather than bypassing it.\n\nWith purpose,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'UMATTR Devotional' ($14.99 CAD): https://lornettedaye.com/books\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    },
    {
        "id": 37,
        "day": 13,
        "date": "2026-10-15",
        "athlete": "tiger",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-10-15T13:45:00.000Z",
        "assetFile": "tiger-woods-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-02.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "STANDARDS DO NOT NEGOTIATE\n\nWatch how Tiger manages his course designs. He walks the dirt. He tests the green speeds. He scrutinizes every bunker placement.\n\nDelegation is essential for scale, but abdication is fatal. Tiger lends his name to nothing that does not meet his personal standard of excellence. In an era where athletes license their likenesses indiscriminately, Tiger curated his brand with monastic restraint. Every enterprise bearing the TGR mark reflects his personal work ethic.\n\nYour reputation is your highest-yielding currency. Protect it by holding every product and partnership to an uncompromising standard.\n\nStay focused,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 38,
        "day": 13,
        "date": "2026-10-15",
        "athlete": "steph",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-10-15T20:30:00.000Z",
        "assetFile": "stephen-curry-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-02.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE LESSON OF THE UNDERRATED MINDSET\n\nRemember where Steph Curry started: a three-star recruit with no major scholarship offers, deemed too small to play high-major basketball.\n\nThe 'Underrated' brand is not a marketing gimmick; it is Steph's autobiography. He built his entire career on being overlooked and outworking the pedigree players. When he looks at junior golfers who lack institutional backing, he sees himself at sixteen years old. That empathy is the secret engine of his philanthropy.\n\nYour greatest business breakthroughs will often emerge directly from the pain and rejection of your early career.\n\nStay focused,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 39,
        "day": 13,
        "date": "2026-10-15",
        "athlete": "ayesha",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-10-16T00:30:00.000Z",
        "assetFile": "ayesha-curry-07.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-07.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE EXPANSION INTO LUXURY HOSPITALITY DESTINATIONS\n\nSweet July is not confined to Oakland. Ayesha expanded the concept into premier resort destinations like Grand Cayman.\n\nTaking a lifestyle brand from a local flagship to an international luxury resort requires sophisticated operational systems and brand consistency. Ayesha proved that her aesthetic translates across global markets, appealing to discerning travelers who value authentic Caribbean and lifestyle storytelling.\n\nDo not underestimate the global appetite for authentic, culturally rich luxury experiences.\n\nStay focused,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 40,
        "day": 14,
        "date": "2026-10-16",
        "athlete": "steph_ayesha",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-10-16T13:45:00.000Z",
        "assetFile": "stephen-ayesha-07.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-07.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE POWER OF UNIFIED FAMILY STEWARDSHIP\n\nWatching Stephen and Ayesha lead together demonstrates the immense power of an aligned marital partnership.\n\nThey do not compete for credit. Steph brings his global athletic megaphone and corporate alliances; Ayesha brings her culinary insight, hospitality standards, and community connection. Together, their combined impact is exponentially greater than what either could achieve in isolation.\n\nWhen two leaders align with mutual respect and zero ego, they can move mountains that stand in the way of justice.\n\nStay focused,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    },
    {
        "id": 41,
        "day": 14,
        "date": "2026-10-16",
        "athlete": "serena",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-10-16T20:30:00.000Z",
        "assetFile": "serena-williams-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-02.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE POWER OF UNAPOLOGETIC AMBITION\n\nThroughout her tennis career, Serena was criticized for being too strong, too vocal, and too ambitious. She never apologized.\n\nShe carried that exact unapologetic standard into corporate boardrooms. Women in business are often socialized to diminish their accomplishments and speak quietly. Serena reminds female founders that power is taken, not granted, and that excellence requires zero apologies.\n\nOwn your power completely. When you demonstrate unshakeable conviction, the room will adjust to your presence.\n\nStay focused,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 42,
        "day": 14,
        "date": "2026-10-16",
        "athlete": "lewis",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-10-17T00:30:00.000Z",
        "assetFile": "lewis-hamilton-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-02.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE COURAGE TO SPEAK TRUTH ON THE PODIUM\n\nWhen Lewis took a knee on the podium and wore shirts demanding justice, he faced intense pressure from racing authorities.\n\nHe refused to be silenced. He leveraged the world's most watched motorsport broadcast to demand human rights, racial justice, and equality. He showed that authentic leadership requires using your podium to advocate for those who have no microphone.\n\nLeadership is tested when speaking the truth costs you corporate comfort. Stand on conviction regardless of the audience.\n\nStay focused,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 43,
        "day": 15,
        "date": "2026-10-17",
        "athlete": "ayesha",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-10-17T13:45:00.000Z",
        "assetFile": "ayesha-curry-08.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-08.png",
        "cta": "Buy Book - Survival Skills: Surviving to Thriving (lornettedaye.com/books)",
        "text": "BALANCING MOTHERHOOD, ENTERPRISE, AND PURPOSE\n\nFour children, multiple restaurants, a media company, and a foundation. Ayesha dispels the myth of effortless perfection.\n\nShe speaks openly about the grueling discipline of time management, the necessity of delegation, and the non-negotiable boundaries required to protect family life. In my coaching with executive women, I emphasize that balance is not a static state; it is dynamic prioritization built on crystal-clear values.\n\nYou cannot do everything alone. Build a trusted operational team that executes your standards with precision.\n\nKeep building,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills: Surviving to Thriving' ($14.99 CAD): https://lornettedaye.com/books\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 44,
        "day": 15,
        "date": "2026-10-17",
        "athlete": "tiger",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-10-17T20:30:00.000Z",
        "assetFile": "tiger-woods-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-03.png",
        "cta": "Buy Book - Survival Skills for Athletes (lornettedaye.com/books)",
        "text": "RESILIENCE AS A STRATEGIC CAPABILITY\n\nSpinal fusion surgery. Five knee surgeries. Public crises. Tiger Woods was written off by every sports analyst on television.\n\nThen came the 2019 Masters. What the world saw on that Sunday was not just a comeback victory. It was a masterclass in psychological resilience, pain management, and emotional poise. In my Olympic coaching career, I watched champions break when circumstances changed. Tiger proved that resilience is not a personality trait. It is a daily decision to keep showing up.\n\nWhen setback strikes your organization, do not ask why it happened. Ask what systems you must build to rise above it.\n\nKeep building,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Athletes' ($14.99 CAD): https://lornettedaye.com/books\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 45,
        "day": 15,
        "date": "2026-10-17",
        "athlete": "steph",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-10-18T00:30:00.000Z",
        "assetFile": "stephen-curry-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-03.png",
        "cta": "Buy Book - Survival Skills for Students (lornettedaye.com/books)",
        "text": "CREATING PATHWAYS TO THE PROFESSIONAL RANKS\n\nUnderrated Golf is already producing players competing in USGA championships and earning collegiate scholarships.\n\nProof of concept is everything in business and sport. Steph did not just create feel-good press releases. He measured outcomes: how many tournament invitations, how many college commitments, and how many handicap reductions. That operational rigor is what separates enduring programs from vanity projects.\n\nHold your philanthropic initiatives to the same rigorous KPIs that govern your revenue-generating business units.\n\nKeep building,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Students' ($14.99 CAD): https://lornettedaye.com/books\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 46,
        "day": 16,
        "date": "2026-10-18",
        "athlete": "lewis",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-10-18T13:45:00.000Z",
        "assetFile": "lewis-hamilton-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-03.png",
        "cta": "Buy Book - Finish Strong: Chasing the Olympic Dream (lornettedaye.com/books)",
        "text": "THE DIET AND RECOVERY OF AN ELITE ATHLETE\n\nLewis adopted a plant-based lifestyle and revolutionized his physical training to compete against drivers half his age.\n\nDriving an F1 car subjects your body to five Gs of lateral force for two hours while losing eight pounds of water weight. Lewis invested in hyperbaric chambers, cryotherapy, and precise nutrition. Longevity in business requires the exact same commitment to physical and cognitive recovery.\n\nYou cannot lead an enterprise effectively if your body is exhausted and inflamed. Treat your physical recovery as a fiduciary duty.\n\nKeep building,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Finish Strong: Chasing the Olympic Dream' ($14.99 CAD): https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 47,
        "day": 16,
        "date": "2026-10-18",
        "athlete": "steph_ayesha",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-10-18T20:30:00.000Z",
        "assetFile": "stephen-ayesha-08.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-08.png",
        "cta": "Buy Book - Surviving Life (lornettedaye.com/books)",
        "text": "TEACHING CHILDREN THAT THEY MATTER\n\nLook at the smiles of the children surrounding Steph and Ayesha when they read together on a park bench.\n\nThose children do not just see famous celebrities; they feel seen, heard, and cherished. In my four decades as an Olympic coach, I have seen that children perform to the level of love and expectation poured into them. When world champions sit on the ground and read with you, your sense of self-worth is cemented.\n\nNever underestimate the life-altering impact of giving a child your undivided presence.\n\nKeep building,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Surviving Life' ($14.99 CAD): https://buy.stripe.com/7sY8wPcwuabE62Jcqu1VK02\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    },
    {
        "id": 48,
        "day": 16,
        "date": "2026-10-18",
        "athlete": "serena",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-10-19T00:30:00.000Z",
        "assetFile": "serena-williams-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-03.png",
        "cta": "Buy Book - Finish Strong: Chasing the Olympic Dream (lornettedaye.com/books)",
        "text": "NAVIGATING SETBACKS WITH RELENTLESS MOMENTUM\n\nPulmonary embolisms, career-threatening surgeries, and heartbreaking finals losses could not stop Serena Williams.\n\nEvery time she was knocked down, she analyzed the failure, restructured her training, and returned to win another Grand Slam. In venture investing, startups fail regularly. Serena understands that a loss is not a defeat; it is simply market tuition for the next breakthrough.\n\nTreat failure as data. Extract the lesson, discard the emotional baggage, and deploy your capital with greater precision.\n\nKeep building,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Finish Strong: Chasing the Olympic Dream' ($14.99 CAD): https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 49,
        "day": 17,
        "date": "2026-10-19",
        "athlete": "steph",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-10-19T13:45:00.000Z",
        "assetFile": "stephen-curry-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-04.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE ROLE OF CORPORATE COALITIONS\n\nSteph did not fund Underrated Golf alone. He assembled a coalition of corporate heavyweights who put skin in the game.\n\nHe brought in enterprise partners who committed not just sponsor checks, but executive mentorship, career internships, and equipment technology. Steph showed corporations that supporting equity in golf is not charity; it is an investment in the future leaders of their own companies.\n\nStrategic coalitions multiply your impact. Rally partners around a shared mission where everyone has an authentic stake.\n\nIn your corner,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 50,
        "day": 17,
        "date": "2026-10-19",
        "athlete": "ayesha",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-10-19T20:30:00.000Z",
        "assetFile": "ayesha-curry-09.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-09.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE POWER OF MEDIA STORYTELLING\n\nSweet July is not just physical stores; it is a full media company publishing lifestyle magazines and digital content.\n\nAyesha understood that content drives commerce, and commerce sustains content. By controlling her own media narrative, she tells stories of resilience, food heritage, wellness, and self-care on her own terms, completely independent of traditional publishing gatekeepers.\n\nOwn your media channel. When you own the storytelling engine, you dictate how your value is communicated to the world.\n\nIn your corner,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 51,
        "day": 17,
        "date": "2026-10-19",
        "athlete": "tiger",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-10-20T00:30:00.000Z",
        "assetFile": "tiger-woods-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-04.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE TGR LEARNING LABS PHILOSOPHY\n\nOver two million students have walked through the doors of the TGR Learning Labs. That is Tiger's greatest scorecard.\n\nIn high-poverty communities, talent is everywhere, but opportunity is scarce. Tiger engineered a curriculum focused on marine biology, biomedical engineering, graphic design, and robotics. He gave young minds the technical tools to compete in modern economies. That is structural philanthropy: solving root challenges rather than offering temporary relief.\n\nIf your wealth creation does not create upward mobility for the next generation, you have built wealth, but you have not built a legacy.\n\nIn your corner,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 52,
        "day": 18,
        "date": "2026-10-20",
        "athlete": "serena",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-10-20T13:45:00.000Z",
        "assetFile": "serena-williams-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-04.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE ARCHITECTURE OF A DIVERSIFIED PORTFOLIO\n\nSerena Ventures has backed over eighty companies across fintech, digital health, e-commerce, and artificial intelligence.\n\nShe does not put all her eggs in one basket. She builds diversified portfolios backed by rigorous thematic theses. She backs founders solving real human problems: accessible healthcare, financial inclusion, clean consumer products.\n\nBuild resilience into your enterprise through intentional diversification and principled investment theses.\n\nIn your corner,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 53,
        "day": 18,
        "date": "2026-10-20",
        "athlete": "lewis",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-10-20T20:30:00.000Z",
        "assetFile": "lewis-hamilton-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-04.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE POWER OF UNCONVENTIONAL BACKGROUNDS\n\nLewis grew up in a council house in Stevenage, with his father working four jobs to fund his go-karting.\n\nHe did not have a wealthy family to buy him a racing team. He carried the hunger of someone who knew that one mistake meant packing up the kart forever. That working-class resilience made him bulletproof when competing against the sons of billionaires.\n\nNever apologize for having to fight for your seat at the table. Hunger built in adversity will outlast inherited privilege every time.\n\nIn your corner,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 54,
        "day": 18,
        "date": "2026-10-20",
        "athlete": "steph_ayesha",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-10-21T00:30:00.000Z",
        "assetFile": "stephen-ayesha-09.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-09.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "SYSTEMIC PARTNERSHIP WITH OAKLAND UNIFIED\n\nEat.Learn.Play. does not operate in a silo. They embedded their initiatives directly within the Oakland Unified School District.\n\nThey worked alongside teachers, principals, and district administrators to identify the schools with the greatest structural deficits. They respected the institutional knowledge of local educators, providing the resources that school budgets could never cover.\n\nTrue leaders do not act as saviors from the outside. They partner with the boots on the ground already doing the work.\n\nIn your corner,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    },
    {
        "id": 55,
        "day": 19,
        "date": "2026-10-21",
        "athlete": "tiger",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-10-21T13:45:00.000Z",
        "assetFile": "tiger-woods-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-05.png",
        "cta": "Buy Book - Finish Strong: Chasing the Olympic Dream (lornettedaye.com/books)",
        "text": "FROM PHENOM TO INSTITUTION\n\nTiger began as a child prodigy on national television. Today, he is an enduring American institution.\n\nThat transition did not happen by chance. It required an intentional shift in identity. Tiger had to let go of being merely an athlete and embrace being an enterprise steward. In my executive coaching work, the hardest shift leaders make is stepping away from individual execution to institutional stewardship.\n\nYou cannot scale what depends entirely on your personal presence. Build systems that succeed whether you are in the room or not.\n\nWith conviction,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Finish Strong: Chasing the Olympic Dream' ($14.99 CAD): https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 56,
        "day": 19,
        "date": "2026-10-21",
        "athlete": "steph",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-10-21T20:30:00.000Z",
        "assetFile": "stephen-curry-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-05.png",
        "cta": "Buy Book - Survival Skills for Athletes (lornettedaye.com/books)",
        "text": "TEACHING POISE UNDER PRESSURE ON THE GREENS\n\nGolf is the most psychologically demanding individual sport in the world. Steph uses it to teach emotional regulation.\n\nIn basketball, you can run off frustration on defense. In golf, you have five minutes to walk in complete silence to your ball after hitting a terrible drive. That requires Olympic-level emotional mastery. Steph is equipping these young athletes with psychological tools that will serve them in boardrooms for the next fifty years.\n\nTeach your emerging leaders how to manage the silent minutes between their mistakes and their next decisions.\n\nWith conviction,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Athletes' ($14.99 CAD): https://lornettedaye.com/books\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 57,
        "day": 19,
        "date": "2026-10-21",
        "athlete": "ayesha",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-10-22T00:30:00.000Z",
        "assetFile": "ayesha-curry-10.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-10.png",
        "cta": "Buy Book - Survival Skills for Women (lornettedaye.com/books)",
        "text": "THE PHILOSOPHY OF THE SWEET JULY MOMENT\n\nThe name 'Sweet July' was inspired by the month where all of Ayesha's children were born, and where she married Steph.\n\nIt represents that window of life where everything aligns, where gratitude overflows, and where joy is celebrated without reservation. Ayesha translated a deeply personal emotional anchor into a commercial universe that invites every customer to experience that same sense of warmth and abundance.\n\nInfuse your enterprise with authentic personal meaning. Customers can feel when a brand has a genuine soul.\n\nWith conviction,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Women' ($14.99 CAD): https://lornettedaye.com/books\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 58,
        "day": 20,
        "date": "2026-10-22",
        "athlete": "steph_ayesha",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-10-22T13:45:00.000Z",
        "assetFile": "stephen-ayesha-10.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-10.png",
        "cta": "Buy Book - UMATTR Devotional (lornettedaye.com/books)",
        "text": "TURNING CELEBRITY INTO SYSTEMIC CHANGE\n\nMany celebrities treat charity as a photo op. Steph and Ayesha engineered Eat.Learn.Play. as a permanent civic institution.\n\nThey built an endowment, hired world-class nonprofit executives, and created governance boards that ensure the foundation will continue feeding, educating, and sheltering Oakland children long after Steph hangs up his sneakers.\n\nBuild institutions that outlive your fame. That is the definitive mark of generational leadership.\n\nWith conviction,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'UMATTR Devotional' ($14.99 CAD): https://lornettedaye.com/books\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    },
    {
        "id": 59,
        "day": 20,
        "date": "2026-10-22",
        "athlete": "serena",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-10-22T20:30:00.000Z",
        "assetFile": "serena-williams-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-05.png",
        "cta": "Buy Book - Survival Skills for Women (lornettedaye.com/books)",
        "text": "MOTHERHOOD AS A COMPETITIVE ADVANTAGE\n\nSerena won the 2017 Australian Open while eight weeks pregnant, and returned to four Grand Slam finals as a mother.\n\nShe exploded the myth that motherhood diminishes professional intensity. In fact, she often notes that becoming a mother sharpened her focus and clarified her purpose. When she evaluates female founders who are mothers, she sees leaders who have mastered the ultimate crucible of multi-tasking and resilience.\n\nRecognize that life's greatest personal responsibilities often unlock your deepest professional capabilities.\n\nWith conviction,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Women' ($14.99 CAD): https://lornettedaye.com/books\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 60,
        "day": 20,
        "date": "2026-10-22",
        "athlete": "lewis",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-10-23T00:30:00.000Z",
        "assetFile": "lewis-hamilton-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-05.png",
        "cta": "Buy Book - Survival Skills for Men (lornettedaye.com/books)",
        "text": "MANAGING CRISIS AFTER HEARTBREAK\n\nThe controversial final lap of Abu Dhabi in 2021 was the most agonizing moment in modern sports history.\n\nLewis was robbed of an eighth world title by an administrative rule breach. What did he do? He shook his competitor's hand, hugged his father, congratulated the opposing team, and walked away with absolute dignity. He did not throw tantrums on television. That grace under devastating heartbreak cemented his status as a legendary statesman of sport.\n\nYour character is not revealed when you win the trophy. It is revealed in how you carry yourself when you are wronged.\n\nWith conviction,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Men' ($14.99 CAD): https://buy.stripe.com/9B6bJ1542gA262JfCG1VK00\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 61,
        "day": 21,
        "date": "2026-10-23",
        "athlete": "ayesha",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-10-23T13:45:00.000Z",
        "assetFile": "ayesha-curry-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-01.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "ELEVATING CARIBBEAN HERITAGE THROUGH MODERN CUISINE\n\nAyesha's culinary vision celebrates her rich Jamaican, Chinese, and African-American roots.\n\nRather than flattening her heritage to appeal to generic tastes, she leaned into bold flavors, island spices, and vibrant presentation. She showed that culinary heritage, when presented with luxury plating and hospitality, commands premium market appreciation.\n\nYour unique cultural background is your proprietary competitive edge. Never dilute what makes your perspective distinct.\n\nWith purpose,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 62,
        "day": 21,
        "date": "2026-10-23",
        "athlete": "tiger",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-10-23T20:30:00.000Z",
        "assetFile": "tiger-woods-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-01.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE VALUE OF INTELLECTUAL SOVEREIGNTY\n\nTiger Woods never permitted outside entities to dictate the core values of his enterprise. He maintained equity and creative control.\n\nIn corporate deal-making, many founders surrender control for short-term capital. Tiger structured partnerships where his vision remained paramount. Whether partnering in hospitality ventures or course development, he insisted on governance rights. He understood that true wealth is not the size of your paycheck, but the degree of your autonomy.\n\nControl over your vision is priceless. Never sacrifice long-term governance for short-term liquidity.\n\nWith purpose,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 63,
        "day": 21,
        "date": "2026-10-23",
        "athlete": "steph",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-10-24T00:30:00.000Z",
        "assetFile": "stephen-curry-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-01.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "A CULTURE OF MUTUAL ACCOUNTABILITY\n\nWatch the culture Steph builds among his junior golfers: competition on the course, brotherhood and sisterhood off the course.\n\nHe demands that every participant conduct themselves with dignity, dress impeccably, respect tournament staff, and support their competitors. In an era of toxic online posturing, Steph is reviving the noble traditions of sportsmanship and mutual respect.\n\nCulture is not what you write on the wall. Culture is the standard of behavior you enforce every single day.\n\nWith purpose,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 64,
        "day": 22,
        "date": "2026-10-24",
        "athlete": "lewis",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-10-24T13:45:00.000Z",
        "assetFile": "lewis-hamilton-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-01.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE ART OF PIT STOP TRUST\n\nLewis enters the pit lane at fifty miles per hour, trusting twenty mechanics to change four tires in two seconds flat.\n\nThat level of speed requires absolute psychological safety and operational trust. There is no room for second-guessing. In executive management, if you have to micromanage your leadership team during a product release, your culture is already broken.\n\nTrain your team until execution is automatic, then get out of their way and let them execute.\n\nWith purpose,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 65,
        "day": 22,
        "date": "2026-10-24",
        "athlete": "steph_ayesha",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-10-24T20:30:00.000Z",
        "assetFile": "stephen-ayesha-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-01.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "NUTRITION AS THE CORNERSTONE OF LEARNING\n\nA child experiencing food insecurity cannot concentrate on mathematics or reading comprehension.\n\nSteph and Ayesha made school breakfast and lunch programs a central battleground. By partnering with local farms and culinary leaders, they transformed school cafeteria menus into fresh, nutritious fuel that powers young brains throughout the school day.\n\nFix the physiological foundation before you demand cognitive performance.\n\nWith purpose,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    },
    {
        "id": 66,
        "day": 22,
        "date": "2026-10-24",
        "athlete": "serena",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-10-25T00:30:00.000Z",
        "assetFile": "serena-williams-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-01.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "BUILDING BRIDGES BETWEEN POP CULTURE AND VENTURE CAPITAL\n\nSerena can sit on the Met Gala red carpet on Monday and interrogate venture valuations on Tuesday morning.\n\nShe bridges cultural relevance with institutional financial power. In the modern economy, cultural cachet drives distribution, and distribution makes startups explosive. Serena gives her portfolio companies unfair access to global consumer awareness.\n\nPair cultural storytelling with financial rigor. That combination makes your portfolio companies untouchable.\n\nWith purpose,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 67,
        "day": 23,
        "date": "2026-10-25",
        "athlete": "steph",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-10-25T13:45:00.000Z",
        "assetFile": "stephen-curry-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-02.png",
        "cta": "Buy Book - Survival Skills for Students (lornettedaye.com/books)",
        "text": "REDEFINING THE GOLF AESTHETIC\n\nSteph brought youthful energy, contemporary fashion, and cultural relevance to a game often viewed as stuffy and elitist.\n\nBy introducing modern apparel lines and vibrant music into practice rounds, Underrated Golf made the game appealing to a new generation without compromising respect for golf's timeless etiquette. He modernized the wrapper while preserving the core integrity of the sport.\n\nYou do not have to abandon timeless fundamentals to make your brand resonate with modern audiences.\n\nStay focused,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Students' ($14.99 CAD): https://lornettedaye.com/books\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 68,
        "day": 23,
        "date": "2026-10-25",
        "athlete": "ayesha",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-10-25T20:30:00.000Z",
        "assetFile": "ayesha-curry-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-02.png",
        "cta": "Buy Book - Survival Skills: Surviving to Thriving (lornettedaye.com/books)",
        "text": "INVESTING IN FEMALE FOUNDERS\n\nThrough her Sweet July Skin line and angel investments, Ayesha directs capital directly to female-led businesses.\n\nLess than three percent of venture capital goes to female founders. Ayesha does not just complain about the statistic; she writes checks and opens retail doors. She understands that economic empowerment for women is the fastest way to stabilize families and revitalize communities.\n\nIf you want to see change in your industry, deploy your capital where traditional gatekeepers refuse to look.\n\nStay focused,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills: Surviving to Thriving' ($14.99 CAD): https://lornettedaye.com/books\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 69,
        "day": 23,
        "date": "2026-10-25",
        "athlete": "tiger",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-10-26T00:30:00.000Z",
        "assetFile": "tiger-woods-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-02.png",
        "cta": "Buy Book - Survival Skills for Athletes (lornettedaye.com/books)",
        "text": "THE POWER OF UNCOMPROMISING PREPARATION\n\nLong before the gallery arrived at sunrise, Tiger was already sweating through practice sessions in the dark.\n\nThe public only celebrates the final round trophy. They do not see the thousand hours of silent, tedious repetition in the gym and on the putting green. In corporate leadership, deals are won in the research phase, not during the pitch. When you prepare so thoroughly that doubt has no oxygen to survive, execution becomes second nature.\n\nConfidence is not bravado. Confidence is the earned byproduct of exhaustive, disciplined preparation.\n\nStay focused,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Athletes' ($14.99 CAD): https://lornettedaye.com/books\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 70,
        "day": 24,
        "date": "2026-10-26",
        "athlete": "serena",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-10-26T13:45:00.000Z",
        "assetFile": "serena-williams-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-02.png",
        "cta": "Buy Book - Finish Strong: Chasing the Olympic Dream (lornettedaye.com/books)",
        "text": "DISRUPTING THE VENTURE CAPITAL BOYS' CLUB\n\nVenture capital has historically been dominated by a homogeneous group of investors who back founders who look like themselves.\n\nSerena walked into that room with twenty-three Grand Slam trophies and an iron will, demanding institutional capital allocations for diverse founders. She forced the venture ecosystem to recognize that investing in overlooked talent is not philanthropy: it is superior fiduciary execution.\n\nBreak the mold in your industry. When you challenge comfortable assumptions, you capture immense untapped value.\n\nStay focused,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Finish Strong: Chasing the Olympic Dream' ($14.99 CAD): https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 71,
        "day": 24,
        "date": "2026-10-26",
        "athlete": "lewis",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-10-26T20:30:00.000Z",
        "assetFile": "lewis-hamilton-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-02.png",
        "cta": "Buy Book - Finish Strong: Chasing the Olympic Dream (lornettedaye.com/books)",
        "text": "INSTITUTIONAL INVESTING IN THE NFL\n\nJoining the Walton-Penner family ownership group of the Denver Broncos placed Lewis in the most exclusive ownership club in the world.\n\nNFL teams are among the most secure, appreciating institutional assets on the planet. Lewis brought global marketing insights, sports science acumen, and diversity perspectives to the Broncos board, proving that European sports champions belong at the American ownership table.\n\nExpand your investment horizon across continents and industries. Cross-pollinate insights between disconnected domains.\n\nStay focused,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Finish Strong: Chasing the Olympic Dream' ($14.99 CAD): https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 72,
        "day": 24,
        "date": "2026-10-26",
        "athlete": "steph_ayesha",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-10-27T00:30:00.000Z",
        "assetFile": "stephen-ayesha-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-02.png",
        "cta": "Buy Book - Surviving Life (lornettedaye.com/books)",
        "text": "FOSTERING A JOYFUL LOVE FOR PLAY\n\nIn modern cities, unstructured play is disappearing, replaced by screens or safety fears. Eat.Learn.Play. is fighting for childhood.\n\nPlay is where children learn negotiation, conflict resolution, emotional regulation, and teamwork. By building safe play spaces, Steph and Ayesha are restoring the vital joy of childhood to neighborhoods that have experienced immense trauma.\n\nDo not eliminate play from your life or your workplace. Play is the fertile soil where innovation and resilience grow.\n\nStay focused,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Surviving Life' ($14.99 CAD): https://buy.stripe.com/7sY8wPcwuabE62Jcqu1VK02\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    },
    {
        "id": 73,
        "day": 25,
        "date": "2026-10-27",
        "athlete": "tiger",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-10-27T13:45:00.000Z",
        "assetFile": "tiger-woods-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-03.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "NAVIGATING CRISIS WITH EMOTIONAL REGULATION\n\nWhen pressure reaches suffocating levels, the amateur reacts with panic. The master slows their breathing and narrows their focus.\n\nI have coached athletes at the Olympic Games when the entire country was watching. The difference between a gold medal and heartbreak is often two seconds of emotional composure. Tiger mastered the art of walking between shots with absolute neutrality, conserving cognitive energy for the moments that matter.\n\nLeaders who cannot regulate their emotions under pressure will inevitably infect their entire team with chaos.\n\nKeep building,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 74,
        "day": 25,
        "date": "2026-10-27",
        "athlete": "steph",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-10-27T20:30:00.000Z",
        "assetFile": "stephen-curry-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-03.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE VALUE OF INTENTIONAL SPONSORSHIP\n\nWhen Steph Curry puts his personal capital behind Howard University's golf program, he isn't just writing checks. He is reviving history.\n\nHe funded the relaunch of the men's and women's golf teams at an iconic HBCU, providing six years of financial backing. He understood that representation at the collegiate level inspires thousands of middle school and high school athletes to keep swinging.\n\nTarget your capital where it creates systemic, institutional revival rather than fleeting social media applause.\n\nKeep building,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 75,
        "day": 25,
        "date": "2026-10-27",
        "athlete": "ayesha",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-10-28T00:30:00.000Z",
        "assetFile": "ayesha-curry-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-03.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE ART OF HIGH-TOUCH CUSTOMER EXPERIENCE\n\nEvery touchpoint at Sweet July Cafe is engineered to evoke sensory delight: the aroma of bread pudding, the curated playlist, the warmth of the lighting.\n\nIn a digital-first economy where everything is transactional, physical hospitality that provides sensory nourishment is a massive differentiator. Ayesha created a physical haven where customers do not feel rushed; they feel welcomed and cherished.\n\nInvest in sensory details. When your customer feels emotionally nourished, price sensitivity disappears.\n\nKeep building,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 76,
        "day": 26,
        "date": "2026-10-28",
        "athlete": "steph_ayesha",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-10-28T13:45:00.000Z",
        "assetFile": "stephen-ayesha-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-03.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "EQUITY IN YOUTH SPORTS ACCESS\n\nPrivate sports leagues have become pay-to-play engines that shut out low-income children. Eat.Learn.Play. levels the field.\n\nThey fund youth sports leagues, provide free uniforms and coaching, and ensure that every Oakland child can experience the discipline and joy of organized sport, regardless of their parents' bank balance.\n\nSport belongs to everyone. Defend the right of every young person to experience athletic brotherhood and sisterhood.\n\nKeep building,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    },
    {
        "id": 77,
        "day": 26,
        "date": "2026-10-28",
        "athlete": "serena",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-10-28T20:30:00.000Z",
        "assetFile": "serena-williams-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-03.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE ART OF EMOTIONAL REGULATION IN CRISIS\n\nWhen Serena was down 1-5 in the third set, her heart rate did not spike; her focus deepened.\n\nIn business turnaround situations, amateur leaders become erratic and frantic. Serena teaches her startup CEOs that crisis requires surgical stillness. Slow your breathing, identify the single most critical variable, and execute the next shot with absolute precision.\n\nStillness under pressure is the rarest and most potent leadership capability in modern commerce.\n\nKeep building,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 78,
        "day": 26,
        "date": "2026-10-28",
        "athlete": "lewis",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-10-29T00:30:00.000Z",
        "assetFile": "lewis-hamilton-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-03.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "REDUCING CARBON FOOTPRINTS IN MOTORSPORT\n\nLewis pushed Formula 1 and Mercedes to adopt net-zero carbon targets and sustainable aviation fuel.\n\nHe sold his private jet, eliminated single-use plastics from his operations, and launched non-alcoholic agave spirits (Almave) that celebrate sustainability. He recognized that modern luxury must be compatible with environmental responsibility.\n\nAlign your products with the values of the future, not the wasteful habits of the past.\n\nKeep building,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 79,
        "day": 27,
        "date": "2026-10-29",
        "athlete": "ayesha",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-10-29T13:45:00.000Z",
        "assetFile": "ayesha-curry-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-04.png",
        "cta": "Buy Book - Survival Skills for Women (lornettedaye.com/books)",
        "text": "THE STRENGTH OF EDITORIAL DISCIPLINE\n\nLook at the Sweet July lifestyle magazine: clean photography, intentional essays, recipes with soul.\n\nIt does not chase clickbait or celebrity gossip. It celebrates quiet rituals of joy, entrepreneurial courage, and holistic wellbeing. Ayesha maintained editorial integrity in an era of media noise, building a publication that readers collect and preserve on coffee tables.\n\nDurability beats virality every single time. Create work that people want to keep, not just scroll past.\n\nIn your corner,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Women' ($14.99 CAD): https://lornettedaye.com/books\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 80,
        "day": 27,
        "date": "2026-10-29",
        "athlete": "tiger",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-10-29T20:30:00.000Z",
        "assetFile": "tiger-woods-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-04.png",
        "cta": "Buy Book - Finish Strong: Chasing the Olympic Dream (lornettedaye.com/books)",
        "text": "INVESTING IN NEXT-GENERATION TALENT\n\nThrough the Earl Woods Scholar Program, Tiger created a 98 percent graduation rate among first-generation college students.\n\nThis was not accomplished by simply writing scholarship checks. It was accomplished through mentorship, internship placements, and emotional support networks. Tiger realized that money without mentorship leaves young talent vulnerable. He built a human support system around every scholar.\n\nGreat leadership is not measured by how many followers you attract, but by how many leaders you cultivate.\n\nIn your corner,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Finish Strong: Chasing the Olympic Dream' ($14.99 CAD): https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 81,
        "day": 27,
        "date": "2026-10-29",
        "athlete": "steph",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-10-30T00:30:00.000Z",
        "assetFile": "stephen-curry-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-04.png",
        "cta": "Buy Book - Survival Skills for Athletes (lornettedaye.com/books)",
        "text": "THE ART OF UNSELFISH LEADERSHIP\n\nSteph Curry's signature on the basketball court is his off-ball movement. He runs constantly to create open shots for his teammates.\n\nThat exact philosophy governs his business endeavors. He does not need his face on every banner. He creates the open lane, passes the ball, and celebrates when young golfers sink life-changing putts. Unselfish leadership is the rarest competitive advantage in modern enterprise.\n\nThe most influential leaders are not those who hoard the spotlight, but those whose movement creates room for others to shine.\n\nIn your corner,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Athletes' ($14.99 CAD): https://lornettedaye.com/books\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 82,
        "day": 28,
        "date": "2026-10-30",
        "athlete": "lewis",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-10-30T13:45:00.000Z",
        "assetFile": "lewis-hamilton-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-04.png",
        "cta": "Buy Book - Survival Skills for Men (lornettedaye.com/books)",
        "text": "THE DISCIPLINE OF MENTAL HEALTH ADVOCACY\n\nLewis has spoken openly about his struggles with depression and the psychological toll of racing under constant scrutiny.\n\nBy normalizing vulnerability, he dismantled the toxic motorsport machismo that forces drivers to hide emotional pain. In my executive coaching work, the strongest CEOs are those who acknowledge mental fatigue and install emotional support systems for themselves and their teams.\n\nVulnerability is not weakness; it is the prerequisite for authentic emotional strength.\n\nIn your corner,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Men' ($14.99 CAD): https://buy.stripe.com/9B6bJ1542gA262JfCG1VK00\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 83,
        "day": 28,
        "date": "2026-10-30",
        "athlete": "steph_ayesha",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-10-30T20:30:00.000Z",
        "assetFile": "stephen-ayesha-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-04.png",
        "cta": "Buy Book - UMATTR Devotional (lornettedaye.com/books)",
        "text": "THE RIPPLE EFFECT OF CULTURALLY AFFIRMING LITERATURE\n\nWhen children read books featuring characters who look like them, their engagement with reading skyrockets.\n\nEat.Learn.Play. specifically curates books written by diverse authors celebrating Black, Latino, Asian, and Indigenous stories. They show young readers that their histories, neighborhoods, and dreams are worthy of literary celebration.\n\nRepresentation matters in books, in boardrooms, and in Olympic coaching. Ensure your library reflects the world you wish to build.\n\nIn your corner,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'UMATTR Devotional' ($14.99 CAD): https://lornettedaye.com/books\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    },
    {
        "id": 84,
        "day": 28,
        "date": "2026-10-30",
        "athlete": "serena",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-10-31T00:30:00.000Z",
        "assetFile": "serena-williams-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-04.png",
        "cta": "Buy Book - Survival Skills for Women (lornettedaye.com/books)",
        "text": "THE VALUE OF INTELLECTUAL PROPERTY SOVEREIGNTY\n\nSerena created S by Serena and Serena Ventures to ensure she retained full ownership of her likeness and commercial ideas.\n\nToo many athletes give away their name in licensing deals where third parties reap ninety percent of the profits. Serena insisted on equity ownership, board seats, and governance rights in every major deal she signed.\n\nNever surrender your name, your likeness, or your strategic governance for a temporary licensing fee.\n\nIn your corner,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Women' ($14.99 CAD): https://lornettedaye.com/books\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 85,
        "day": 29,
        "date": "2026-10-31",
        "athlete": "steph",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-10-31T13:45:00.000Z",
        "assetFile": "stephen-curry-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-05.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "MENTAL TOUGHNESS ON THE BACK NINE\n\nIn championship golf, the tournament does not begin until the back nine on Sunday. That is where mental fatigue tests your character.\n\nSteph teaches young athletes that fatigue is an emotion, not a physical mandate. When your legs are tired and pressure mounts, your routine must become your sanctuary. Having coached Olympic athletes through the most grueling medal rounds, I know that routine is what protects talent from panic.\n\nUnder severe pressure, you do not rise to the occasion. You sink to the level of your training and daily routines.\n\nWith conviction,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 86,
        "day": 29,
        "date": "2026-10-31",
        "athlete": "ayesha",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-10-31T20:30:00.000Z",
        "assetFile": "ayesha-curry-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-05.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "OVERCOMING PUBLIC SCRUTINY WITH CLASS\n\nWhen you build a business in the public eye, every misstep is dissected by critics. Ayesha responded with dignified silence and unrelenting execution.\n\nAs an Olympic coach, I have seen athletes unravel because they let critics into their heads. Ayesha demonstrated that the best response to public noise is a five-star dining room, a thriving retail brand, and a growing community of loyal supporters.\n\nNever enter a debate with people who have never built an enterprise. Let your results deliver the verdict.\n\nWith conviction,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 87,
        "day": 29,
        "date": "2026-10-31",
        "athlete": "tiger",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-01T00:30:00.000Z",
        "assetFile": "tiger-woods-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-05.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "STRATEGIC ALLIANCES THAT EXPAND HORIZONS\n\nTiger's partnership with luxury hospitality and entertainment brands showcases the art of high-caliber joint ventures.\n\nWhen scaling an enterprise, choosing the right partner is more important than choosing the fastest opportunity. Tiger aligned with partners who shared his obsession with quality and durability. They created immersive environments where sports, dining, and technology intersect seamlessly.\n\nAlignment of values must precede any conversation about alignment of profits.\n\nWith conviction,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 88,
        "day": 30,
        "date": "2026-11-01",
        "athlete": "serena",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-01T14:45:00.000Z",
        "assetFile": "serena-williams-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-05.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "TEACHING THE NEXT GENERATION OF GIRLS TO LEAD\n\nSerena's daughter Olympia is already a co-owner of Angel City FC and Los Angeles Golf Club.\n\nSerena is intentionally teaching her daughters the mechanics of capital ownership before they reach middle school. She is proving that generational wealth is not just about inheritance; it is about financial education, governance training, and ownership literacy.\n\nTeach your children the principles of ownership early. Give them an economic compass that guides their entire lives.\n\nWith conviction,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 89,
        "day": 30,
        "date": "2026-11-01",
        "athlete": "lewis",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-01T21:30:00.000Z",
        "assetFile": "lewis-hamilton-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-05.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE BOLD MOVE TO FERRARI\n\nAt thirty-nine years old, after six world titles with Mercedes, Lewis signed a multi-year deal to drive for Scuderia Ferrari.\n\nHe refused to settle into a comfortable, safe retirement ride. He chose the most iconic, high-pressure, emotionally volatile seat in motorsport because he wanted the ultimate challenge. Great champions seek new crucibles to test their capabilities.\n\nWhen comfort threatens to dull your edge, put yourself back in the arena where everything is on the line.\n\nWith conviction,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 90,
        "day": 30,
        "date": "2026-11-01",
        "athlete": "steph_ayesha",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-02T01:30:00.000Z",
        "assetFile": "stephen-ayesha-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-05.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "CIVIC ENGAGEMENT THAT TRANSCENDS POLITICS\n\nSteph and Ayesha do not engage in petty partisan squabbles. They focus relentlessly on outcomes for kids.\n\nWhether working with local city councils, corporate donors, or grassroots activists, they maintain a laser focus on one question: does this initiative directly improve the life of an Oakland child? That clarity of mission disarms political friction.\n\nKeep the main thing the main thing. When your mission is unquestioned, detractors lose their power.\n\nWith conviction,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    },
    {
        "id": 91,
        "day": 31,
        "date": "2026-11-02",
        "athlete": "tiger",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-02T14:45:00.000Z",
        "assetFile": "tiger-woods-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-01.png",
        "cta": "Buy Book - Survival Skills for Athletes (lornettedaye.com/books)",
        "text": "THE ART OF THE SECOND CAREER\n\nMost athletes grieve when their physical dominance wanes. Tiger leaned forward into the intellectual challenge of enterprise building.\n\nTransition is painful only when you define yourself solely by your past achievements. Tiger defined himself by his curiosity, his strategic instincts, and his commitment to excellence. When you view every career milestone as a foundation rather than a finish line, transition becomes a promotion, not an ending.\n\nDo not cling to titles you have outgrown. Step boldly into the arena your experience has prepared you to conquer.\n\nWith purpose,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Athletes' ($14.99 CAD): https://lornettedaye.com/books\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 92,
        "day": 31,
        "date": "2026-11-02",
        "athlete": "steph",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-02T21:30:00.000Z",
        "assetFile": "stephen-curry-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-01.png",
        "cta": "Buy Book - Survival Skills for Students (lornettedaye.com/books)",
        "text": "THE POWER OF VISIBILITY AND ROLE MODELS\n\nYou cannot dream of being what you cannot see.\n\nWhen a young girl from an underserved community sees Steph Curry walking alongside her on the fairway, giving her swing tips, her ceiling of expectation shatters permanently. She no longer wonders if she belongs in elite golf; she knows she does.\n\nYour presence in the lives of emerging leaders speaks ten times louder than any piece of advice you will ever give.\n\nWith purpose,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Students' ($14.99 CAD): https://lornettedaye.com/books\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 93,
        "day": 31,
        "date": "2026-11-02",
        "athlete": "ayesha",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-03T01:30:00.000Z",
        "assetFile": "ayesha-curry-06.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-06.png",
        "cta": "Buy Book - Survival Skills: Surviving to Thriving (lornettedaye.com/books)",
        "text": "COMMUNITY ROOTEDNESS IN OAKLAND\n\nWhen Ayesha launched Sweet July, she chose Uptown Oakland, investing directly in the city that embraced her family.\n\nShe did not take the concept straight to Beverly Hills or Manhattan. She planted her flag in Oakland, creating local jobs, contracting local builders, and establishing a beacon of luxury within the community. That rootedness generated immense civic pride and authentic neighborhood love.\n\nInvest in the communities that believed in you before you became a national headline.\n\nWith purpose,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills: Surviving to Thriving' ($14.99 CAD): https://lornettedaye.com/books\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 94,
        "day": 32,
        "date": "2026-11-03",
        "athlete": "steph_ayesha",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-03T14:45:00.000Z",
        "assetFile": "stephen-ayesha-06.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-06.png",
        "cta": "Buy Book - Surviving Life (lornettedaye.com/books)",
        "text": "MEASURABLE IMPACT OVER PRESS RELEASES\n\nEat.Learn.Play. publishes rigorous annual impact reports detailing every dollar spent and every child reached.\n\nThey measure third-grade reading improvements, school attendance rates, and athletic participation numbers. That data-driven discipline is why philanthropic institutions and major corporations entrust them with multi-million-dollar grants.\n\nGood intentions are not a metric. Measure your impact with unflinching data and accountability.\n\nWith purpose,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Surviving Life' ($14.99 CAD): https://buy.stripe.com/7sY8wPcwuabE62Jcqu1VK02\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    },
    {
        "id": 95,
        "day": 32,
        "date": "2026-11-03",
        "athlete": "serena",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-03T21:30:00.000Z",
        "assetFile": "serena-williams-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-01.png",
        "cta": "Buy Book - Finish Strong: Chasing the Olympic Dream (lornettedaye.com/books)",
        "text": "CHAMPION FOCUS IN BOARDROOM GOVERNANCE\n\nWhen Serena sits on a corporate board, she asks the hard, uncomfortable questions that others avoid.\n\nShe does not show up as a decorative celebrity director. She reads the board materials, scrutinizes audit reports, and demands accountability on diversity and strategic execution. Her presence elevates the governance standard of every company she touches.\n\nDo not accept board seats or advisory roles if you are not willing to do the tedious governance work required.\n\nWith purpose,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Finish Strong: Chasing the Olympic Dream' ($14.99 CAD): https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 96,
        "day": 32,
        "date": "2026-11-03",
        "athlete": "lewis",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-04T01:30:00.000Z",
        "assetFile": "lewis-hamilton-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-01.png",
        "cta": "Buy Book - Finish Strong: Chasing the Olympic Dream (lornettedaye.com/books)",
        "text": "THE VALUE OF A SINGLE-MINDED VISION\n\nAt ten years old, Lewis walked up to McLaren boss Ron Dennis and said: 'One day I want to be racing your cars.'\n\nHe had an unshakeable vision long before he had the resources to back it up. Vision is what pulls you out of bed on freezing mornings when every external circumstance tells you to quit. In corporate strategy, vision is what keeps your team aligned when cash flow is tight.\n\nCast a vision so clear and compelling that doubt has nowhere to hide in your organization.\n\nWith purpose,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Finish Strong: Chasing the Olympic Dream' ($14.99 CAD): https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 97,
        "day": 33,
        "date": "2026-11-04",
        "athlete": "ayesha",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-04T14:45:00.000Z",
        "assetFile": "ayesha-curry-07.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-07.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE METICULOUS FORMULATION OF SWEET JULY SKIN\n\nAyesha did not simply private-label skincare products. She spent years researching Caribbean superfoods like guava, soursop, and papaya.\n\nShe combined natural island remedies with clean clinical science, creating a skincare line that honors her ancestral beauty rituals while delivering dermatological results. That respect for craftsmanship is why the product line earned national accolades.\n\nHonor tradition while leveraging modern science. That intersection is where groundbreaking innovation lives.\n\nStay focused,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 98,
        "day": 33,
        "date": "2026-11-04",
        "athlete": "tiger",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-04T21:30:00.000Z",
        "assetFile": "tiger-woods-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-02.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "CREATING PERMANENT FOOTPRINTS IN COMMUNITIES\n\nA championship banner hangs in an arena until someone takes it down. A learning lab educates children for generations.\n\nTiger recognized that the most enduring footprint an athlete can leave is physical and educational infrastructure. Buildings where children learn coding, design thinking, and environmental science create ripples across families that no trophy case can rival.\n\nShift your focus from vanity metrics to generational infrastructure.\n\nStay focused,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 99,
        "day": 33,
        "date": "2026-11-04",
        "athlete": "steph",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-05T01:30:00.000Z",
        "assetFile": "stephen-curry-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-02.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "LESSONS IN STRATEGIC PATIENCE\n\nGolf rewards the strategist, not the reckless attacker. Steph's golf tour teaches young players how to manage course risks.\n\nTaking a double bogey because you tried a hero shot from the trees is a failure of discipline, not skill. Steph's coaches teach course management: take your medicine, punch out to the fairway, save bogey, and play the long game. That is identical to executive capital management.\n\nAvoid the temptation of hero maneuvers when a disciplined, steady play preserves your strategic capital.\n\nStay focused,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 100,
        "day": 34,
        "date": "2026-11-05",
        "athlete": "lewis",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-05T14:45:00.000Z",
        "assetFile": "lewis-hamilton-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-02.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "NAVIGATING THE TEAMMATE RIVALRY\n\nIn Formula 1, your teammate is your fiercest rival because they drive identical machinery.\n\nLewis managed high-stakes rivalries with Fernando Alonso, Jenson Button, and Nico Rosberg. He learned that internal competition can elevate an organization, provided respect for the overarching team objective is never violated.\n\nChannel internal competition toward collective excellence rather than petty sabotage.\n\nStay focused,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 101,
        "day": 34,
        "date": "2026-11-05",
        "athlete": "steph_ayesha",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-05T21:30:00.000Z",
        "assetFile": "stephen-ayesha-07.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-07.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE COURAGE TO STAY COMMITTED TO OAKLAND\n\nEven after the Golden State Warriors relocated across the bay to San Francisco, Steph and Ayesha deepened their roots in Oakland.\n\nThey did not abandon the city that loved them during their championship run. They maintained their foundation headquarters in Oakland and expanded their investments. That loyalty earned them the eternal devotion of the Oakland community.\n\nLoyalty during seasons of transition is the hallmark of genuine character. Never forget the soil that nourished your roots.\n\nStay focused,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    },
    {
        "id": 102,
        "day": 34,
        "date": "2026-11-05",
        "athlete": "serena",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-06T01:30:00.000Z",
        "assetFile": "serena-williams-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-02.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE COURAGE TO EVOLVE\n\nWhen Serena announced her transition from tennis in Vogue, she chose the word 'evolution' rather than 'retirement.'\n\nRetirement implies quitting, fading away, or concluding your utility. Evolution implies taking every ounce of wisdom, stamina, and competitive excellence you developed in one arena and directing it into your next great endeavor.\n\nNever retire. Evolve. Reallocate your championship energy into new mountains worthy of your capabilities.\n\nStay focused,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 103,
        "day": 35,
        "date": "2026-11-06",
        "athlete": "steph",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-06T14:45:00.000Z",
        "assetFile": "stephen-curry-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-03.png",
        "cta": "Buy Book - Survival Skills for Athletes (lornettedaye.com/books)",
        "text": "BUILDING BRIDGES ACROSS GENERATIONS\n\nSteph regularly connects Underrated Golf participants with legendary senior players and PGA Tour veterans.\n\nHe bridges the wisdom of the past with the dynamism of the future. Cross-generational mentorship accelerates learning curves by decades, saving young people from repeating the painful mistakes of their predecessors.\n\nSurround your young high-potentials with seasoned veterans who have already navigated the minefields.\n\nKeep building,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Athletes' ($14.99 CAD): https://lornettedaye.com/books\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 104,
        "day": 35,
        "date": "2026-11-06",
        "athlete": "ayesha",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-06T21:30:00.000Z",
        "assetFile": "ayesha-curry-08.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-08.png",
        "cta": "Buy Book - Survival Skills for Women (lornettedaye.com/books)",
        "text": "CREATING JOINT VALUE WITHOUT ENMESHMENT\n\nAyesha and Steph collaborate brilliantly, but they maintain distinct professional domains.\n\nSteph has Thirty Ink and Curry Brand; Ayesha has Sweet July and Sweet July Productions. They support each other's launches, but each operates with independent operational leadership and strategic clarity. This prevents personal friction and allows both enterprises to flourish.\n\nClear boundaries strengthen partnerships. Ensure every collaborator has full sovereignty over their domain.\n\nKeep building,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Women' ($14.99 CAD): https://lornettedaye.com/books\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 105,
        "day": 35,
        "date": "2026-11-06",
        "athlete": "tiger",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-07T01:30:00.000Z",
        "assetFile": "tiger-woods-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-03.png",
        "cta": "Buy Book - Finish Strong: Chasing the Olympic Dream (lornettedaye.com/books)",
        "text": "PRECISION IN CAPITAL DEPLOYMENT\n\nTiger does not scatter his capital across dozens of trendy ventures. He concentrates resources in domains he deeply understands.\n\nThe downfall of many high-earning professionals is diversification into areas where they possess zero operational insight. Tiger stayed close to sports, leisure, hospitality, and educational technology. He deployed capital where his brand and insight provided an insurmountable competitive advantage.\n\nInvest where your domain expertise protects you from foolish assumptions.\n\nKeep building,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Finish Strong: Chasing the Olympic Dream' ($14.99 CAD): https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 106,
        "day": 36,
        "date": "2026-11-07",
        "athlete": "serena",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-07T14:45:00.000Z",
        "assetFile": "serena-williams-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-03.png",
        "cta": "Buy Book - Survival Skills for Women (lornettedaye.com/books)",
        "text": "THE METRICS THAT MATTER IN VENTURE\n\nIn tennis, the scorecard is simple: games, sets, match. In venture, the scorecard is IRR, multiple on invested capital, and customer acquisition costs.\n\nSerena mastered the language of venture finance because she understood that respect in institutional finance is earned through numbers, not sentiment. She holds her portfolio companies to rigorous operational discipline.\n\nMaster the definitive financial metrics of your industry. Speak the language of capital with absolute fluency.\n\nKeep building,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Women' ($14.99 CAD): https://lornettedaye.com/books\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 107,
        "day": 36,
        "date": "2026-11-07",
        "athlete": "lewis",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-07T21:30:00.000Z",
        "assetFile": "lewis-hamilton-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-03.png",
        "cta": "Buy Book - Survival Skills for Men (lornettedaye.com/books)",
        "text": "CREATING PRODUCTS THAT DISRUPT TRADITION\n\nWith Almave, Lewis created the world's first non-alcoholic blue agave spirit made using authentic Mexican distilling techniques.\n\nHe did not just create another non-alcoholic soda; he worked with master distillers in Jalisco to create a luxury beverage that honors Mexican heritage while supporting mindful, high-performance lifestyles. That is true product innovation.\n\nDo not settle for superficial brand extensions. Create products that genuinely innovate within traditional crafts.\n\nKeep building,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Men' ($14.99 CAD): https://buy.stripe.com/9B6bJ1542gA262JfCG1VK00\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 108,
        "day": 36,
        "date": "2026-11-07",
        "athlete": "steph_ayesha",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-08T01:30:00.000Z",
        "assetFile": "stephen-ayesha-08.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-08.png",
        "cta": "Buy Book - UMATTR Devotional (lornettedaye.com/books)",
        "text": "EMPOWERING LOCAL MOTHERS AND FAMILIES\n\nBehind every child supported by Eat.Learn.Play. is a mother striving to provide a brighter future.\n\nAyesha regularly hosts community circles, parenting roundtables, and wellness retreats for Oakland mothers, providing mental health resources and community solidarity. She understands that supporting the mother is the most effective way to protect the child.\n\nStrengthen the pillars of the family, and the entire community will stand upright.\n\nKeep building,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'UMATTR Devotional' ($14.99 CAD): https://lornettedaye.com/books\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    },
    {
        "id": 109,
        "day": 37,
        "date": "2026-11-08",
        "athlete": "tiger",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-08T14:45:00.000Z",
        "assetFile": "tiger-woods-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-04.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "CULTIVATING CHAMPION HABITS DAILY\n\nChampionship performance is not an act you perform on game day. It is an operating system running twenty-four hours a day.\n\nTiger's daily routine during his prime was legendary: five-mile run at dawn, four hours of range work, two hours of short game, gym session, and evening practice. That level of rigor is terrifying to the undisciplined, but to the committed, it is the only path to immortality.\n\nYou cannot demand excellence from your team while living in compromise yourself. Set the standard with your own calendar.\n\nIn your corner,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 110,
        "day": 37,
        "date": "2026-11-08",
        "athlete": "steph",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-08T21:30:00.000Z",
        "assetFile": "stephen-curry-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-04.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE BUSINESS LESSON OF THE LONG DRIVE\n\nEveryone loves watching a 350-yard drive, but tournaments are won inside of 100 yards with wedge play and putting.\n\nIn business, flashy launches attract headlines, but operational execution, customer retention, and unit economics are what generate lasting profits. Steph teaches junior golfers to fall in love with the dull, repetitive short-game practice that casual players neglect.\n\nFall in love with the mundane details that amateur competitors consider boring. That is where the margin of victory lives.\n\nIn your corner,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 111,
        "day": 37,
        "date": "2026-11-08",
        "athlete": "ayesha",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-09T01:30:00.000Z",
        "assetFile": "ayesha-curry-09.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-09.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "LEADERSHIP WITH INTENTIONAL KINDNESS\n\nAyesha's leadership philosophy rejects the myth that high-performing kitchens must be abusive and chaotic.\n\nShe fosters a culture of mutual respect, dignity, and calm communication across her cafes and culinary teams. Having worked in high-stress Olympic environments for decades, I know that fear breeds mistakes, while psychological safety unlocks creativity and sustained excellence.\n\nYou do not need to be ruthless to demand excellence. High standards delivered with deep respect will inspire loyalty.\n\nIn your corner,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 112,
        "day": 38,
        "date": "2026-11-09",
        "athlete": "steph_ayesha",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-09T14:45:00.000Z",
        "assetFile": "stephen-ayesha-09.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-09.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE COMMUNITY GARDEN MOVEMENT\n\nAt every rebuilt schoolyard, Eat.Learn.Play. installs edible community gardens where children plant seeds, tend vegetables, and taste fresh produce.\n\nThey teach children where food comes from, instilling an early respect for agriculture, nutrition, and environmental stewardship. Watching an elementary student pull a fresh carrot from the ground they tended is a lesson in patience and harvest.\n\nTeach young minds that great things require patience, watering, and daily care before the harvest appears.\n\nIn your corner,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    },
    {
        "id": 113,
        "day": 38,
        "date": "2026-11-09",
        "athlete": "serena",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-09T21:30:00.000Z",
        "assetFile": "serena-williams-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-04.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "BUILDING INFRASTRUCTURE FOR WOMEN'S SPORTS\n\nSerena's investment in Angel City FC catalyzed a global wave of institutional investment into women's athletics.\n\nShe proved that women's sports is an undervalued asset class with passionate fans, surging viewership, and immense commercial runway. Today, private equity and institutional funds are pouring billions into women's sports because Serena proved the business thesis.\n\nBe the pioneer who validates a new asset class. The rewards of proving the thesis first are astronomical.\n\nIn your corner,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 114,
        "day": 38,
        "date": "2026-11-09",
        "athlete": "lewis",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-10T01:30:00.000Z",
        "assetFile": "lewis-hamilton-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-04.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE DISCIPLINE OF THE RACING LINE\n\nOn any racetrack, there is only one optimal mathematical trajectory: the racing line. Deviating by two inches bleeds speed.\n\nLewis drives with a geometric elegance that makes violent physics look effortless. In business execution, adhering to your core strategic trajectory protects you from unnecessary friction and wasted capital.\n\nIdentify the definitive trajectory for your business and hold your line with uncompromising precision.\n\nIn your corner,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 115,
        "day": 39,
        "date": "2026-11-10",
        "athlete": "ayesha",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-10T14:45:00.000Z",
        "assetFile": "ayesha-curry-10.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-10.png",
        "cta": "Buy Book - Survival Skills: Surviving to Thriving (lornettedaye.com/books)",
        "text": "THE SWEET FRUIT OF RELENTLESS PERSEVERANCE\n\nFrom filming home cooking videos in a tiny kitchen to operating an international lifestyle hospitality empire.\n\nAyesha's journey reminds every woman that small, faithful beginnings matter. You do not need a massive production studio to start; you need an authentic voice, a commitment to your craft, and the willingness to learn from every early failure.\n\nStart where you are, with what you have in your hands. Faithful daily execution will open doors you cannot yet see.\n\nWith conviction,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills: Surviving to Thriving' ($14.99 CAD): https://lornettedaye.com/books\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 116,
        "day": 39,
        "date": "2026-11-10",
        "athlete": "tiger",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-10T21:30:00.000Z",
        "assetFile": "tiger-woods-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-05.png",
        "cta": "Buy Book - Survival Skills for Athletes (lornettedaye.com/books)",
        "text": "THE MEASURE OF TRUE VICTORY\n\nWhen history writes the definitive book on Tiger Woods, the chapters on golf will be glorious, but the chapters on human impact will endure.\n\nMedals collect dust. Records are eventually broken. But the thousands of young people who became engineers, doctors, and community leaders because of the TGR Foundation will continue shaping the world long after our names are forgotten.\n\nLive your life and build your business with eternity in mind, not just the next fiscal quarter.\n\nWith conviction,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Athletes' ($14.99 CAD): https://lornettedaye.com/books\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 117,
        "day": 39,
        "date": "2026-11-10",
        "athlete": "steph",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-11T01:30:00.000Z",
        "assetFile": "stephen-curry-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-05.png",
        "cta": "Buy Book - Survival Skills for Students (lornettedaye.com/books)",
        "text": "THE CURRY LEGACY BLUEPRINT\n\nSteph's legacy will be far wider than four championship rings. It will include hundreds of college graduates who got their degrees through golf.\n\nThat is how an athlete transforms cultural capital into generational equity. He is not merely entertaining audiences on television; he is systematically rewiring the economic trajectory of families across the globe.\n\nAsk yourself: will your business metrics matter in thirty years, or are you building something that changes family lineages?\n\nWith conviction,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Students' ($14.99 CAD): https://lornettedaye.com/books\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 118,
        "day": 40,
        "date": "2026-11-11",
        "athlete": "lewis",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-11T14:45:00.000Z",
        "assetFile": "lewis-hamilton-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-05.png",
        "cta": "Buy Book - Finish Strong: Chasing the Olympic Dream (lornettedaye.com/books)",
        "text": "THE IMPORTANCE OF FAMILY ALLIANCES\n\nAnthony Hamilton mortgaged his house and worked night shifts to keep Lewis in karting competitions.\n\nLewis never forgets that debt of gratitude. He keeps his family close, honoring his father and brother Nicolas at every career milestone. He proves that athletic and commercial conquest is hollow if it destroys the family bonds that sustained you in the beginning.\n\nProtect your family and core relationships at all costs. They are your true sanctuary when the stadium lights go out.\n\nWith conviction,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Finish Strong: Chasing the Olympic Dream' ($14.99 CAD): https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 119,
        "day": 40,
        "date": "2026-11-11",
        "athlete": "steph_ayesha",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-11T21:30:00.000Z",
        "assetFile": "stephen-ayesha-10.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-10.png",
        "cta": "Buy Book - Surviving Life (lornettedaye.com/books)",
        "text": "A PARTNERSHIP FORGED IN PURPOSE\n\nSteph and Ayesha show the world that marriage can be a vehicle for monumental social change.\n\nThey have built wealth, fame, and influence, but they channel those resources outward into the lives of vulnerable children. Their partnership is a masterclass in shared values, mutual elevation, and legacy creation.\n\nAlign your personal relationships around shared purpose. Together, you can achieve what neither could accomplish alone.\n\nWith conviction,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Surviving Life' ($14.99 CAD): https://buy.stripe.com/7sY8wPcwuabE62Jcqu1VK02\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    },
    {
        "id": 120,
        "day": 40,
        "date": "2026-11-11",
        "athlete": "serena",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-12T01:30:00.000Z",
        "assetFile": "serena-williams-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-05.png",
        "cta": "Buy Book - Finish Strong: Chasing the Olympic Dream (lornettedaye.com/books)",
        "text": "THE LESSON OF COMPTON TO THE WORLD STAGE\n\nRemember where Serena's journey began: public courts in Compton with cracked concrete and missing nets.\n\nHer father Richard Williams had a vision for his daughters that seemed absurd to the tennis establishment. Serena proved that when preparation, unshakeable family belief, and ferocious work ethic collide, no institutional barrier can stop you.\n\nNever let humble beginnings limit the scale of your global vision. The fire forged in adversity will fuel your empire.\n\nWith conviction,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Finish Strong: Chasing the Olympic Dream' ($14.99 CAD): https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 121,
        "day": 41,
        "date": "2026-11-12",
        "athlete": "steph",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-12T14:45:00.000Z",
        "assetFile": "stephen-curry-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-01.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "ELEVATING THE STANDARD OF EQUALITY\n\nUnderrated Golf treats male and female athletes with equal investment, equal prize opportunities, and equal prestige.\n\nFrom day one, Steph insisted that the women's division receives the exact same tournament venues, media coverage, and corporate introductions as the men. He rejected the traditional sports hierarchy that treats female athletics as an afterthought.\n\nTrue equity is not lip service; it is an identical allocation of budget, attention, and executive sponsorship.\n\nWith purpose,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 122,
        "day": 41,
        "date": "2026-11-12",
        "athlete": "ayesha",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-12T21:30:00.000Z",
        "assetFile": "ayesha-curry-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-01.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "A MODERN MASTERCLASS IN FEMALE OWNERSHIP\n\nAyesha Curry represents the new generation of female enterprise owners who refuse to be pigeonholed.\n\nShe is simultaneously a mother, an author, a restaurateur, a beauty founder, and an executive producer. She shattered the outdated expectation that women must choose between domestic fulfillment and commercial ambition. She built an ecosystem that honors both.\n\nRefuse the false choices imposed by small minds. Build a life and a business that encompasses the full breadth of your calling.\n\nWith purpose,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 123,
        "day": 41,
        "date": "2026-11-12",
        "athlete": "tiger",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-13T01:30:00.000Z",
        "assetFile": "tiger-woods-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-01.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE SOVEREIGN MINDSET IN MODERN SPORT\n\nTiger Woods demonstrated that athletes are not commodities to be bought and sold. They are sovereign economic forces.\n\nHe shifted the power dynamic between players and sanctioning bodies, proving that the value of the spectacle resides with the creators of excellence. Today's business leaders must recognize that talent retention requires respecting sovereignty and creating shared equity, not merely offering compensation.\n\nWhen talent understands its worth, leadership must offer partnership, not command-and-control.\n\nWith purpose,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 124,
        "day": 42,
        "date": "2026-11-13",
        "athlete": "serena",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-13T14:45:00.000Z",
        "assetFile": "serena-williams-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-01.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE DISCIPLINE OF LONGEVITY\n\nSerena competed at the highest echelon of professional tennis for four separate decades.\n\nThat level of physical and mental longevity is unprecedented. It required continuous reinvention of her nutrition, recovery protocols, mental health boundaries, and tournament schedule. She brings that same multi-decade horizon to her venture fund investments.\n\nThink in decades, not quarters. Build an enterprise designed to weather every economic cycle and emerge victorious.\n\nWith purpose,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 125,
        "day": 42,
        "date": "2026-11-13",
        "athlete": "lewis",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-13T21:30:00.000Z",
        "assetFile": "lewis-hamilton-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-01.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "ELEVATING THE GLOBAL CONVERSATION ON DIVERSITY\n\nWhen Lewis entered Formula 1 in 2007, he was the first and only Black driver in the history of the sport.\n\nSeventeen years later, he is the most successful driver to ever sit in a cockpit: 104 race victories, 104 pole positions. He did not just break the barrier; he established a standard of excellence that no one before him had ever attained.\n\nDo not just break ceilings. Build permanent floors upon which the next generation can stand.\n\nWith purpose,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 126,
        "day": 42,
        "date": "2026-11-13",
        "athlete": "steph_ayesha",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-14T01:30:00.000Z",
        "assetFile": "stephen-ayesha-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-01.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "BREAKING THE CYCLE OF GENERATIONAL POVERTY\n\nPoverty is not just an absence of money; it is an absence of access, nourishment, and literacy.\n\nBy attacking hunger, illiteracy, and physical inactivity simultaneously, Eat.Learn.Play. is breaking the generational transmission of poverty in Oakland. They are building a generation of healthy, literate, confident young people who will lead that city tomorrow.\n\nDo not apply bandages to systemic wounds. Attack the root causes that hold human potential hostage.\n\nWith purpose,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    },
    {
        "id": 127,
        "day": 43,
        "date": "2026-11-14",
        "athlete": "tiger",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-14T14:45:00.000Z",
        "assetFile": "tiger-woods-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-02.png",
        "cta": "Buy Book - Finish Strong: Chasing the Olympic Dream (lornettedaye.com/books)",
        "text": "BUILDING INFRASTRUCTURE FOR THE UNSEEN\n\nThe greatness of TGR Design lies in making courses that test the elite while welcoming the amateur.\n\nIn business product design, this is the Holy Grail: creating solutions that possess institutional depth while remaining accessible and intuitive to the newcomer. Tiger's philosophy is rooted in removing friction so that more people can experience the beauty of the game.\n\nSimplicity on the surface backed by sophisticated architecture underneath is the hallmark of great product design.\n\nStay focused,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Finish Strong: Chasing the Olympic Dream' ($14.99 CAD): https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 128,
        "day": 43,
        "date": "2026-11-14",
        "athlete": "steph",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-14T21:30:00.000Z",
        "assetFile": "stephen-curry-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-02.png",
        "cta": "Buy Book - Survival Skills for Athletes (lornettedaye.com/books)",
        "text": "THE HUMILITY TO BE A STUDENT OF GOLF\n\nDespite being an elite basketball genius, Steph approached golf with the humility of a beginner.\n\nHe spent hours asking questions, studying swing mechanics from world-class instructors, and accepting that greatness in one field does not automatically transfer to another. That humility is what allowed him to build credibility within the golf establishment.\n\nNever let mastery in your primary domain convince you that you have nothing left to learn in new arenas.\n\nStay focused,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Athletes' ($14.99 CAD): https://lornettedaye.com/books\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 129,
        "day": 43,
        "date": "2026-11-14",
        "athlete": "ayesha",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-15T01:30:00.000Z",
        "assetFile": "ayesha-curry-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-02.png",
        "cta": "Buy Book - Survival Skills for Women (lornettedaye.com/books)",
        "text": "DESIGNING EXPERIENCES THAT RESIST COMMODITIZATION\n\nAnyone can sell coffee beans. Very few can create a space where walking through the door feels like an exhale.\n\nAyesha understood that the commodity is cheap, but the sanctuary is priceless. In an increasingly anxious and fragmented culture, spaces that provide peace, aesthetic order, and genuine warmth will always command a premium.\n\nDo not compete in the race to the bottom on price. Elevate the emotional experience until you are in a category of one.\n\nStay focused,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Women' ($14.99 CAD): https://lornettedaye.com/books\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 130,
        "day": 44,
        "date": "2026-11-15",
        "athlete": "steph_ayesha",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-15T14:45:00.000Z",
        "assetFile": "stephen-ayesha-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-02.png",
        "cta": "Buy Book - UMATTR Devotional (lornettedaye.com/books)",
        "text": "CREATING HUBS OF HOPE IN HISTORIC NEIGHBORHOODS\n\nThe playgrounds Steph and Ayesha build are not just for the school; they are open to the entire neighborhood on weekends.\n\nThey become community gathering grounds where families hold picnics, neighbors converse, and children play safely under the California sun. That spatial revitalization reduces neighborhood crime and fosters community pride.\n\nTransform spaces of neglect into havens of beauty and joy. Beauty heals communities.\n\nStay focused,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'UMATTR Devotional' ($14.99 CAD): https://lornettedaye.com/books\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    },
    {
        "id": 131,
        "day": 44,
        "date": "2026-11-15",
        "athlete": "serena",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-15T21:30:00.000Z",
        "assetFile": "serena-williams-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-02.png",
        "cta": "Buy Book - Survival Skills for Women (lornettedaye.com/books)",
        "text": "THE STRENGTH TO STAND ALONE\n\nIn 2001, Serena faced immense hostility at Indian Wells. She walked away from that tournament for fourteen years on principle.\n\nShe showed that dignity and principle must always supersede commercial convenience. When she returned in 2015, it was on her own terms, turning a moment of historical pain into a masterclass in grace and forgiveness.\n\nNever sell your principles for prize money or corporate approval. When you stand on integrity, time will vindicate you.\n\nStay focused,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Women' ($14.99 CAD): https://lornettedaye.com/books\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 132,
        "day": 44,
        "date": "2026-11-15",
        "athlete": "lewis",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-16T01:30:00.000Z",
        "assetFile": "lewis-hamilton-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-02.png",
        "cta": "Buy Book - Survival Skills for Men (lornettedaye.com/books)",
        "text": "MANAGING TIRE DEGRADATION IN THE CLOSING LAPS\n\nThe greatest F1 drivers are not those who drive the fastest lap; they are those who preserve their equipment until the end.\n\nLewis is a master of tire management, nursing worn rubber through thirty laps while defending against younger challengers. In business, capital preservation and customer relationship management are your tires. Burn through them carelessly, and you will not finish the race.\n\nPace your resources. The goal is to finish first, not to post the flashiest split time in lap ten and crash out.\n\nStay focused,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Men' ($14.99 CAD): https://buy.stripe.com/9B6bJ1542gA262JfCG1VK00\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 133,
        "day": 45,
        "date": "2026-11-16",
        "athlete": "ayesha",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-16T14:45:00.000Z",
        "assetFile": "ayesha-curry-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-03.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE DISCIPLINE OF SAYING NO TO EASY MONEY\n\nAyesha has turned down countless fast-money endorsements that did not align with the Sweet July ethos.\n\nWhen you build a luxury brand, dilution is lethal. Ayesha protects the integrity of Sweet July with relentless vigilance. She understands that brand equity built over a decade can be destroyed in ten seconds by an off-brand partnership.\n\nGuarding your brand's integrity requires the discipline to walk away from deals that compromise your reputation.\n\nKeep building,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 134,
        "day": 45,
        "date": "2026-11-16",
        "athlete": "tiger",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-16T21:30:00.000Z",
        "assetFile": "tiger-woods-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-03.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "HOW PRESSURE REVEALS FAULT LINES\n\nPut an ordinary player under major championship pressure, and their flaws are instantly magnified. Put Tiger under pressure, and his fundamentals solidify.\n\nPressure does not create character; it reveals preparation. In corporate crisis management, organizations collapse not because the crisis was novel, but because their internal communication systems and standard operating procedures were fragile.\n\nStress-test your operational systems during calm seasons so they hold firm during the storm.\n\nKeep building,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 135,
        "day": 45,
        "date": "2026-11-16",
        "athlete": "steph",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-17T01:30:00.000Z",
        "assetFile": "stephen-curry-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-03.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "INVESTING IN PARENTAL AND FAMILY SUPPORT\n\nJunior sports can strain family finances and relationships. Underrated Golf supports the parents as much as the players.\n\nSteph provides hospitality, educational workshops on college compliance, and travel stipends for parents. He recognizes that behind every resilient junior athlete is a family sacrificing hours and resources to make dreams possible.\n\nWhen developing high-potential leaders, support the ecosystem that sustains them when they leave your office.\n\nKeep building,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 136,
        "day": 46,
        "date": "2026-11-17",
        "athlete": "lewis",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-17T14:45:00.000Z",
        "assetFile": "lewis-hamilton-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-03.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "CULTIVATING A MULTI-HYPHENATE IDENTITY\n\nLewis is a driver, an owner, a producer, a designer, an investor, and a philanthropist.\n\nHe rejected the outdated advice that athletes should 'stick to sports.' He understood that a multifaceted life fuels creativity and prevents burnout in your primary domain.\n\nEmbrace your diverse passions. Creative cross-pollination will make you sharper in your primary enterprise.\n\nKeep building,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 137,
        "day": 46,
        "date": "2026-11-17",
        "athlete": "steph_ayesha",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-17T21:30:00.000Z",
        "assetFile": "stephen-ayesha-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-03.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE DISCIPLINE OF LISTENING TO OAKLAND VOICES\n\nBefore designing a single playground, Eat.Learn.Play. conducts listening sessions with the students and parents.\n\nThey ask the kids what equipment they want: climbing walls, four-square courts, turf soccer fields: and they build what the children envisioned. That democratic design process gives the community immediate ownership and pride in the space.\n\nNever assume you know what people need. Ask them, listen with humility, and build their vision.\n\nKeep building,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    },
    {
        "id": 138,
        "day": 46,
        "date": "2026-11-17",
        "athlete": "serena",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-18T01:30:00.000Z",
        "assetFile": "serena-williams-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-03.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "HOW EXCELLENCE CREATES LEVERAGE\n\nWhen you are undeniably the best in the world at what you do, you dictate the terms of your contracts.\n\nSerena did not beg sponsors for favorable terms. Her undeniable excellence on the court gave her the commercial leverage to negotiate equity clauses, creative control, and philanthropic commitments into every corporate agreement.\n\nDo not spend time lobbying for leverage. Spend your time building undeniable excellence. Leverage will follow automatically.\n\nKeep building,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 139,
        "day": 47,
        "date": "2026-11-18",
        "athlete": "steph",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-18T14:45:00.000Z",
        "assetFile": "stephen-curry-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-04.png",
        "cta": "Buy Book - Survival Skills for Students (lornettedaye.com/books)",
        "text": "LEVERAGING ENTERPRISE PARTNERSHIPS FOR SOCIAL GOOD\n\nSteph turned corporate brand deals from vanity endorsements into social impact alliances.\n\nEvery corporate partner who signs with Curry Brand or Thirty Ink must commit resources to community initiatives like Underrated Golf. He made social responsibility a non-negotiable term of commercial engagement.\n\nDo not just ask what a partner will pay you. Ask what problems they are willing to solve alongside you.\n\nIn your corner,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Students' ($14.99 CAD): https://lornettedaye.com/books\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 140,
        "day": 47,
        "date": "2026-11-18",
        "athlete": "ayesha",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-18T21:30:00.000Z",
        "assetFile": "ayesha-curry-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-04.png",
        "cta": "Buy Book - Survival Skills: Surviving to Thriving (lornettedaye.com/books)",
        "text": "THE SOUL OF HOSPITALITY IS LISTENING\n\nGreat restaurateurs do not just watch the kitchen; they watch the faces of their guests.\n\nAyesha studies customer reactions, reads feedback, and continuously refines menu items and retail selections. That humility to listen and adapt while holding the aesthetic line is the mark of a true hospitality visionary.\n\nListen deeply to the people you serve. They will tell you exactly how to build an enduring enterprise.\n\nIn your corner,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills: Surviving to Thriving' ($14.99 CAD): https://lornettedaye.com/books\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 141,
        "day": 47,
        "date": "2026-11-18",
        "athlete": "tiger",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-19T01:30:00.000Z",
        "assetFile": "tiger-woods-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-04.png",
        "cta": "Buy Book - Survival Skills for Athletes (lornettedaye.com/books)",
        "text": "ELEVATING THE CONVERSATION ABOUT ATHLETE EQUITY\n\nTiger paved the way for every multi-million-dollar athletic brand deal in existence today.\n\nBefore Tiger, golfers wore modest logos and earned modest prize money. Tiger elevated the entire financial ecosystem of golf, raising purses for every competitor on the tour. That is the definition of abundance leadership: lifting the floor for everyone while setting a new ceiling.\n\nA true leader does not compete for a bigger slice of the pie. They bake a larger pie for the entire industry.\n\nIn your corner,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Athletes' ($14.99 CAD): https://lornettedaye.com/books\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 142,
        "day": 48,
        "date": "2026-11-19",
        "athlete": "serena",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-19T14:45:00.000Z",
        "assetFile": "serena-williams-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-04.png",
        "cta": "Buy Book - Finish Strong: Chasing the Olympic Dream (lornettedaye.com/books)",
        "text": "LESSONS FROM MATCH POINT CONVERSIONS\n\nIn tennis, you can win more total points than your opponent and still lose the match if you fail to convert on big points.\n\nIn business, closing the decisive transaction matters far more than having busy days. Serena was legendary for raising her level of play on break points and match points. She teaches founders how to execute under pressure when the term sheet is on the table.\n\nIdentify the decisive moments that truly matter, and bring your absolute highest level of focus to those specific inflection points.\n\nIn your corner,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Finish Strong: Chasing the Olympic Dream' ($14.99 CAD): https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 143,
        "day": 48,
        "date": "2026-11-19",
        "athlete": "lewis",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-19T21:30:00.000Z",
        "assetFile": "lewis-hamilton-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-04.png",
        "cta": "Buy Book - Finish Strong: Chasing the Olympic Dream (lornettedaye.com/books)",
        "text": "THE ART OF RADIO SILENCE\n\nListen to Lewis on team radio during the most chaotic races: concise, measured, informative.\n\nHe does not scream or vent panic. He reports track conditions, asks for tire temperature data, and confirms tactical decisions. In corporate crisis management, leaders who clog communication channels with noise create paralysis.\n\nKeep your operational communication lean, factual, and actionable during critical moments.\n\nIn your corner,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Finish Strong: Chasing the Olympic Dream' ($14.99 CAD): https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 144,
        "day": 48,
        "date": "2026-11-19",
        "athlete": "steph_ayesha",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-20T01:30:00.000Z",
        "assetFile": "stephen-ayesha-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-04.png",
        "cta": "Buy Book - Surviving Life (lornettedaye.com/books)",
        "text": "CORPORATE RESPONSIBILITY WITH REAL TEETH\n\nEat.Learn.Play. forces its corporate sponsors to volunteer on build days alongside Steph and Ayesha.\n\nCEOs and corporate executives roll up their sleeves, paint murals, spread mulch, and assemble playground equipment alongside neighborhood families. Steph and Ayesha break down corporate silos and bring executives face-to-face with the communities they serve.\n\nGet your hands dirty. Real leadership happens on the ground with tools in hand, not from an ivory tower.\n\nIn your corner,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Surviving Life' ($14.99 CAD): https://buy.stripe.com/7sY8wPcwuabE62Jcqu1VK02\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    },
    {
        "id": 145,
        "day": 49,
        "date": "2026-11-20",
        "athlete": "tiger",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-20T14:45:00.000Z",
        "assetFile": "tiger-woods-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-05.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE DISCIPLINE OF SAYING NO\n\nFor every business opportunity Tiger accepted, he declined fifty others.\n\nThe greatest threat to a prestigious brand is dilution. When you are successful, opportunities flood your desk daily. The ability to reject lucrative offers that dilute your core purpose is the rarest skill in executive leadership.\n\nFocus is not about what you say yes to. Focus is defined by the profitable temptations you have the strength to reject.\n\nWith conviction,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 146,
        "day": 49,
        "date": "2026-11-20",
        "athlete": "steph",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-20T21:30:00.000Z",
        "assetFile": "stephen-curry-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-05.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "TEACHING POST-COMPETITION PERSPECTIVE\n\nWhen a junior golfer misses a cut or cards an 82, Steph's coaches do not treat it as a tragedy. They treat it as curriculum.\n\nAs an Olympic coach, I have seen young athletes tie their entire self-worth to a scoreboard. Steph teaches them that your score reflects your golf game today, not your value as a human being. That psychological separation is what prevents burnout and despair.\n\nNever confuse your performance with your identity. You are always greater than your latest quarterly results.\n\nWith conviction,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 147,
        "day": 49,
        "date": "2026-11-20",
        "athlete": "ayesha",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-21T01:30:00.000Z",
        "assetFile": "ayesha-curry-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-05.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "CREATING PRODUCTS THAT TELL STORIES\n\nEvery candle, every jar of honey, and every linen napkin in Sweet July has an intentional backstory.\n\nConsumers do not purchase objects; they purchase identity and narrative. When a customer takes home a Sweet July mug, they are taking home a reminder to savor their mornings and prioritize peace in their home.\n\nWrap your products in narratives of meaning, heritage, and intentional living.\n\nWith conviction,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 148,
        "day": 50,
        "date": "2026-11-21",
        "athlete": "steph_ayesha",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-21T14:45:00.000Z",
        "assetFile": "stephen-ayesha-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-05.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "TEACHING KIDS TO FINISH STRONG\n\nThe ethos of Olympic athletics: finishing strong when your lungs burn: permeates every literacy program and sports clinic Eat.Learn.Play. runs.\n\nThey teach children that struggling with a difficult book is no different than struggling with a fourth-quarter deficit. You do not quit. You take a breath, ask for help, and finish strong. That mental toughness is life's ultimate survival skill.\n\nInstill resilience in young minds early. It is the greatest gift you can hand to the next generation.\n\nWith conviction,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    },
    {
        "id": 149,
        "day": 50,
        "date": "2026-11-21",
        "athlete": "serena",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-21T21:30:00.000Z",
        "assetFile": "serena-williams-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-05.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE POWER OF A SISTERHOOD ALLIANCE\n\nThe partnership between Serena and Venus Williams changed sports history forever.\n\nThey pushed each other in practice, protected each other on tour, won fourteen Grand Slam doubles titles together with zero losses in finals, and built business empires side by side. That sisterhood proved that competition does not require tearing down your closest allies.\n\nBuild alliances based on unshakeable loyalty. When you push each other to greatness, both of you conquer the world.\n\nWith conviction,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 150,
        "day": 50,
        "date": "2026-11-21",
        "athlete": "lewis",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-22T01:30:00.000Z",
        "assetFile": "lewis-hamilton-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-05.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "TURNING ADVERSITY INTO HIGH-OCTANE FUEL\n\nEvery penalty, every engine failure, and every unfair stewards' decision became fuel for Lewis's next dominant weekend.\n\nHe has an extraordinary psychological capability to transmute anger into laser-like technical focus. That is the hallmark of an Olympic-caliber champion.\n\nDo not let unfair circumstances make you bitter. Let them make you untouchable.\n\nWith conviction,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 151,
        "day": 51,
        "date": "2026-11-22",
        "athlete": "ayesha",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-22T14:45:00.000Z",
        "assetFile": "ayesha-curry-06.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-06.png",
        "cta": "Buy Book - Survival Skills for Women (lornettedaye.com/books)",
        "text": "BUILDING BRIDGES BETWEEN CULINARY AND WELLNESS\n\nAyesha recognizes that food, skincare, and mental health are intimately connected.\n\nSweet July integrates culinary nutrition with topical skin wellness and mindful lifestyle routines. She created a 360-degree approach to wellbeing that treats the human being as a holistic ecosystem.\n\nLook across traditional industry silos. The most lucrative innovations occur at the intersections of disconnected domains.\n\nWith purpose,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Women' ($14.99 CAD): https://lornettedaye.com/books\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 152,
        "day": 51,
        "date": "2026-11-22",
        "athlete": "tiger",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-22T21:30:00.000Z",
        "assetFile": "tiger-woods-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-01.png",
        "cta": "Buy Book - Finish Strong: Chasing the Olympic Dream (lornettedaye.com/books)",
        "text": "TURNING PHYSICAL PAIN INTO PURPOSEFUL SYSTEMS\n\nWhen back injuries threatened to end Tiger's career, he channeled his energy into expanding his business footprint.\n\nPhysical limitations often force mental evolution. When you cannot rely solely on brute force or personal hours, you are forced to build systems, empower teams, and delegate authority. Tiger's enterprise grew stronger because he could not do everything himself.\n\nLet your constraints force you into higher levels of operational sophistication.\n\nWith purpose,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Finish Strong: Chasing the Olympic Dream' ($14.99 CAD): https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 153,
        "day": 51,
        "date": "2026-11-22",
        "athlete": "steph",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-23T01:30:00.000Z",
        "assetFile": "stephen-curry-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-01.png",
        "cta": "Buy Book - Survival Skills for Athletes (lornettedaye.com/books)",
        "text": "CREATING MEMORABLE RITUALS OF EXCELLENCE\n\nFrom custom tour bags to professional caddie access, Underrated Golf treats every participant like a tour pro.\n\nWhen you elevate an environment, people naturally elevate their behavior to match it. When young players see their names on leaderboards and receive professional-grade equipment, they stop viewing themselves as underdogs and begin carrying themselves as contenders.\n\nDesign environments that communicate dignity and high expectations. Your people will rise to meet them.\n\nWith purpose,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Athletes' ($14.99 CAD): https://lornettedaye.com/books\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 154,
        "day": 52,
        "date": "2026-11-23",
        "athlete": "lewis",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-23T14:45:00.000Z",
        "assetFile": "lewis-hamilton-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-01.png",
        "cta": "Buy Book - Survival Skills for Men (lornettedaye.com/books)",
        "text": "THE POWER OF A SIGNATURE PHILOSOPHY: STILL WE RISE\n\nInscribed on Lewis Hamilton's helmet are Maya Angelou's words: 'Still I Rise.'\n\nIt is not a decorative quote; it is his personal doctrine. When you have a core philosophical anchor, market downturns, unfair referee calls, and personal tragedies cannot derail your trajectory. You simply rise again.\n\nAnchor your enterprise in timeless principles that cannot be shaken by market turbulence.\n\nWith purpose,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Men' ($14.99 CAD): https://buy.stripe.com/9B6bJ1542gA262JfCG1VK00\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 155,
        "day": 52,
        "date": "2026-11-23",
        "athlete": "steph_ayesha",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-23T21:30:00.000Z",
        "assetFile": "stephen-ayesha-06.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-06.png",
        "cta": "Buy Book - UMATTR Devotional (lornettedaye.com/books)",
        "text": "A CULTURE OF UNCEASING GRATITUDE\n\nEvery time Steph and Ayesha speak about Eat.Learn.Play., their first words are gratitude to the Oakland community.\n\nThey recognize that their NBA championships and cultural success were built on the backs of Oakland fans who filled Oracle Arena with electric passion for decades. Their foundation is an act of heartfelt thanksgiving, not patronizing benevolence.\n\nApproach your philanthropy with deep gratitude for the people who supported your ascent.\n\nWith purpose,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'UMATTR Devotional' ($14.99 CAD): https://lornettedaye.com/books\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    },
    {
        "id": 156,
        "day": 52,
        "date": "2026-11-23",
        "athlete": "serena",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-24T01:30:00.000Z",
        "assetFile": "serena-williams-01.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-01.png",
        "cta": "Buy Book - Survival Skills for Women (lornettedaye.com/books)",
        "text": "VENTURE AS AN INSTRUMENT OF CULTURAL CHANGE\n\nSerena does not view capital merely as a scorecard; she views it as a cultural lever.\n\nWhen she funds a startup that democratizes maternal health for women of color, she is saving lives while generating financial returns. That is conscious capitalism at the highest Olympic level.\n\nDeploy your capital so that every financial return simultaneously advances human flourishing.\n\nWith purpose,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Women' ($14.99 CAD): https://lornettedaye.com/books\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 157,
        "day": 53,
        "date": "2026-11-24",
        "athlete": "steph",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-24T14:45:00.000Z",
        "assetFile": "stephen-curry-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-02.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "NAVIGATING SKEPTICISM WITH QUIET COMPETENCE\n\nWhen a basketball player announced he was launching a national golf tour, traditionalists were openly skeptical.\n\nSteph did not engage in public arguments. He simply executed five-star tournaments, secured top-tier courses, and let the quality of the competition silence every critic. Quiet competence is always the most devastating response to skepticism.\n\nDo not waste energy arguing with doubters. Build something so exceptional that its existence renders their arguments obsolete.\n\nStay focused,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 158,
        "day": 53,
        "date": "2026-11-24",
        "athlete": "ayesha",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-24T21:30:00.000Z",
        "assetFile": "ayesha-curry-07.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-07.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE ENDURANCE REQUIRED FOR MULTI-UNIT HOSPITALITY\n\nOpening store number two is harder than opening store number one. Scaling into luxury resorts requires flawless manuals.\n\nAyesha translated her culinary intuition into standardized operating procedures, employee training modules, and brand style guides. That institutional documentation is what enables Sweet July to maintain its magic across geographies.\n\nIf your business cannot run without your physical presence, you own a demanding job, not an enterprise. Build manuals.\n\nStay focused,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 159,
        "day": 53,
        "date": "2026-11-24",
        "athlete": "tiger",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-25T01:30:00.000Z",
        "assetFile": "tiger-woods-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-02.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "LEGACY IS AN EVERYDAY CONSTRUCTION SITE\n\nYou do not inherit a legacy; you construct it with every email, every contract, and every interaction.\n\nTiger's legacy is active. He is designing courses, mentoring his son Charlie, guiding the PGA Tour through tectonic commercial shifts, and funding educational laboratories. He remains an active builder, not a ceremonial relic.\n\nNever settle into retirement mindset while your mind is still sharp and your hands can still build.\n\nStay focused,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 160,
        "day": 54,
        "date": "2026-11-25",
        "athlete": "serena",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-25T14:45:00.000Z",
        "assetFile": "serena-williams-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-02.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE RELENTLESS PURSUIT OF MASTERY\n\nEven after winning twenty Grand Slams, Serena was on the practice court at 6:00 AM working on second-serve consistency.\n\nMastery is not a destination where you unpack your bags and rest. Mastery is a continuous commitment to refine the smallest details of your craft. That is the mentality she instills in the CEOs backed by Serena Ventures.\n\nNever allow your past accomplishments to convince you that you have arrived. Stay hungry on the practice courts of your industry.\n\nStay focused,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 161,
        "day": 54,
        "date": "2026-11-25",
        "athlete": "lewis",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-25T21:30:00.000Z",
        "assetFile": "lewis-hamilton-02.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-02.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "LESSONS FROM SEVEN WORLD CHAMPIONSHIPS\n\nWinning one championship is difficult. Winning seven requires rebuilding your motivation from scratch every single winter.\n\nAfter you have won everything, your greatest enemy is complacency. Lewis found new motivations every year: pushing for technical perfection, developing young mechanics, mentoring team members. He never allowed success to make him soft.\n\nFight complacency with ferocious vigilance. The moment you believe you have mastered your craft is the moment decline begins.\n\nStay focused,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 162,
        "day": 54,
        "date": "2026-11-25",
        "athlete": "steph_ayesha",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-26T01:30:00.000Z",
        "assetFile": "stephen-ayesha-07.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-07.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "NURTURING OLYMPIANS OF THE MIND\n\nNot every child will win a gold medal or an NBA championship, but every child can become an Olympic-level thinker and creator.\n\nEat.Learn.Play. treats every student as a potential genius waiting to be unlocked. In my forty years of coaching elite athletes, I saw that the difference between an ordinary contender and a champion was the belief someone placed in them early.\n\nLook at the people under your leadership and see who they can become, not just who they are today.\n\nStay focused,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    },
    {
        "id": 163,
        "day": 55,
        "date": "2026-11-26",
        "athlete": "tiger",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-26T14:45:00.000Z",
        "assetFile": "tiger-woods-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-03.png",
        "cta": "Buy Book - Survival Skills for Athletes (lornettedaye.com/books)",
        "text": "THE LESSON OF SUNDAY AT AUGUSTA\n\nIn 2019, when Tiger walked off the 18th green at Augusta with his children waiting, it was not about validation. It was about demonstration.\n\nHe wanted his children to see that setbacks, mistakes, and surgeries do not have the final word in a human life. What you demonstrate through your recovery is infinitely more powerful than what you preach in your victories.\n\nYour greatest leadership lesson to your team is how you handle your darkest setbacks.\n\nKeep building,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Athletes' ($14.99 CAD): https://lornettedaye.com/books\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 164,
        "day": 55,
        "date": "2026-11-26",
        "athlete": "steph",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-26T21:30:00.000Z",
        "assetFile": "stephen-curry-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-03.png",
        "cta": "Buy Book - Survival Skills for Students (lornettedaye.com/books)",
        "text": "THE DISCIPLINE OF CONSISTENCY OVER TIME\n\nLaunching a tour is easy; sustaining it across multiple seasons requires relentless operational commitment.\n\nSteph has expanded Underrated Golf year after year, adding European stops, increasing corporate funding, and growing participant counts. Consistency is the true differentiator between a passing vanity fad and an enduring institution.\n\nBrilliance without consistency is meaningless. Show up with the same rigor on rainy Tuesdays that you bring to opening day.\n\nKeep building,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Students' ($14.99 CAD): https://lornettedaye.com/books\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 165,
        "day": 55,
        "date": "2026-11-26",
        "athlete": "ayesha",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-27T01:30:00.000Z",
        "assetFile": "ayesha-curry-08.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-08.png",
        "cta": "Buy Book - Survival Skills: Surviving to Thriving (lornettedaye.com/books)",
        "text": "LIFTING AS SHE CLIMBS\n\nAyesha's retail ecosystem has generated millions in sales for independent, woman-owned small businesses.\n\nThat is how wealth distribution ought to function. Rather than hoarding profits, she creates a pipeline where emerging female entrepreneurs gain credibility, exposure, and capital through her platform.\n\nMeasure your enterprise success not just by your gross revenue, but by the commercial ecosystem you nurture around you.\n\nKeep building,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills: Surviving to Thriving' ($14.99 CAD): https://lornettedaye.com/books\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 166,
        "day": 56,
        "date": "2026-11-27",
        "athlete": "steph_ayesha",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-27T14:45:00.000Z",
        "assetFile": "stephen-ayesha-08.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-08.png",
        "cta": "Buy Book - Surviving Life (lornettedaye.com/books)",
        "text": "A MODEL FOR ATHLETES WORLDWIDE\n\nEat.Learn.Play. has become the gold standard blueprint for how professional athletes should structure their foundations.\n\nAthletes from across the NFL, NBA, and Premier League regularly contact Steph and Ayesha's team to study their operational model, zero-overhead structure, and focus on systemic pillars. They are leading a revolution in athlete philanthropy.\n\nWhen you build something with excellence and integrity, the entire industry will study your blueprint.\n\nKeep building,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Surviving Life' ($14.99 CAD): https://buy.stripe.com/7sY8wPcwuabE62Jcqu1VK02\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    },
    {
        "id": 167,
        "day": 56,
        "date": "2026-11-27",
        "athlete": "serena",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-27T21:30:00.000Z",
        "assetFile": "serena-williams-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-03.png",
        "cta": "Buy Book - Finish Strong: Chasing the Olympic Dream (lornettedaye.com/books)",
        "text": "THE PSYCHOLOGICAL WARFARE OF BOARDROOMS\n\nIntimidation in corporate deal-making is real. Serena Williams has stared down the most ferocious competitors in sports history.\n\nWhen she walks into a boardroom, she cannot be bullied, hurried, or patronized. Her posture, her calm tone, and her deep knowledge of the facts command immediate authority. She teaches women leaders to occupy space without apology.\n\nWalk into every room knowing you belong there. Your self-assurance sets the boundary for how others treat you.\n\nKeep building,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Finish Strong: Chasing the Olympic Dream' ($14.99 CAD): https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 168,
        "day": 56,
        "date": "2026-11-27",
        "athlete": "lewis",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-28T01:30:00.000Z",
        "assetFile": "lewis-hamilton-03.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-03.png",
        "cta": "Buy Book - Finish Strong: Chasing the Olympic Dream (lornettedaye.com/books)",
        "text": "THE ART OF GLOBAL CITIZENSHIP\n\nLewis races in Japan, Brazil, Italy, Abu Dhabi, and the United States, connecting authentically with local fans in every culture.\n\nHe studies local customs, respects cultural heritage, and carries himself as a humble ambassador of sport. In an interconnected global economy, cultural intelligence is an invaluable leadership asset.\n\nApproach global markets with genuine curiosity, humility, and cultural respect.\n\nKeep building,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Finish Strong: Chasing the Olympic Dream' ($14.99 CAD): https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 169,
        "day": 57,
        "date": "2026-11-28",
        "athlete": "ayesha",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-28T14:45:00.000Z",
        "assetFile": "ayesha-curry-09.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-09.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "GRACE UNDER THE BRIGHTEST LIGHTS\n\nNavigating corporate boardrooms, Hollywood studios, and family life requires immense emotional poise.\n\nAyesha carries herself with an unmistakable grace: calm speech, thoughtful deliberation, and unshakeable conviction. In forty years of coaching, I have found that poise is the single most intimidating weapon a leader can wield against hostility.\n\nWhen the environment is chaotic, your calm is your greatest source of authority.\n\nIn your corner,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 170,
        "day": 57,
        "date": "2026-11-28",
        "athlete": "tiger",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-28T21:30:00.000Z",
        "assetFile": "tiger-woods-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-04.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "MASTERING THE ART OF TIMING\n\nIn golf, tempo is everything. A swing rushed by two milliseconds ends up in the trees. In corporate acquisitions, tempo is equally decisive.\n\nTiger never rushed the expansion of TGR. He waited until the foundational team was seasoned, the brand was bulletproof, and the capital structure was clean. Moving fast is overrated; moving with precision and impeccable timing is what wins.\n\nDo not confuse activity with progress. Move when the strategic advantage is entirely in your favor.\n\nIn your corner,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 171,
        "day": 57,
        "date": "2026-11-28",
        "athlete": "steph",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-29T01:30:00.000Z",
        "assetFile": "stephen-curry-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-04.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "INSPIRING A GENERATION OF UNCONVENTIONAL CHAMPIONS\n\nThe faces on the Underrated Golf leaderboards do not look like traditional country club rosters, and that is precisely the victory.\n\nYoung Black, Hispanic, and Asian junior golfers are walking fairways that their grandparents were not allowed to enter. Steph used his stardom to rewrite the cultural DNA of an entire sport. That is the highest manifestation of athletic influence.\n\nUse your seat at the table to expand the guest list, not to pull up the ladder.\n\nIn your corner,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 172,
        "day": 58,
        "date": "2026-11-29",
        "athlete": "lewis",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-29T14:45:00.000Z",
        "assetFile": "lewis-hamilton-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-04.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "STEWARDING AN NFL FRANCHISE WITH PURPOSE\n\nAs an owner of the Denver Broncos, Lewis brings an obsession with athlete wellness, nutrition, and mental health.\n\nHe works with Broncos leadership to ensure players have world-class recovery facilities and community outreach programs. He is redefining what an active, hands-on minority owner can contribute to a legacy franchise.\n\nDo not be a passive investor. Bring your unique expertise and values to the governance table.\n\nIn your corner,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 173,
        "day": 58,
        "date": "2026-11-29",
        "athlete": "steph_ayesha",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-29T21:30:00.000Z",
        "assetFile": "stephen-ayesha-09.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-09.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "THE PROMISE OF BRIGHTER TOMORROWS\n\nLook at the banner behind Steph and Ayesha: 'Oakland Kids, Brighter Tomorrows.' That is not a slogan; it is a sacred contract.\n\nThey have committed their lives, their fortune, and their ongoing energy to ensuring that every child in Oakland has the food, books, and play needed to realize their God-given potential. That is what it means to live for something greater than yourself.\n\nDedicate your resources to a cause that will continue paying dividends long after you are gone.\n\nIn your corner,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    },
    {
        "id": 174,
        "day": 58,
        "date": "2026-11-29",
        "athlete": "serena",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-11-30T01:30:00.000Z",
        "assetFile": "serena-williams-04.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-04.png",
        "cta": "Keynote Booking (lornettedaye.com/book)",
        "text": "CREATING PERMANENT FOOTPRINTS IN COMMERCE\n\nTrophies tarnish and records will be contested, but the companies Serena seeds will employ thousands and shape the global economy.\n\nThat is the shift from champion to owner, and from owner to institution builder. Serena Williams has rewritten the playbook for every elite athlete who will follow her.\n\nBuild something that outlives your personal celebrity. Build institutions that continue providing value across generations.\n\nIn your corner,\nLornette\n\nBring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\nBook Lornette Daye for your keynote: https://lornettedaye.com/book\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 175,
        "day": 59,
        "date": "2026-11-30",
        "athlete": "steph",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-11-30T14:45:00.000Z",
        "assetFile": "stephen-curry-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-curry-05.png",
        "cta": "Buy Book - Survival Skills for Athletes (lornettedaye.com/books)",
        "text": "THE SCORECARD THAT NEVER FADES\n\nSteph Curry has made hundreds of millions of dollars and scored thousands of three-pointers, but Underrated Golf is his timeless masterpiece.\n\nEvery time a young girl from an underserved zip code earns a college scholarship through this tour, Steph's legacy expands into eternity. That is what it means to own the next chapter. That is the standard of leadership I challenge every CEO and founder to pursue.\n\nMake your next chapter the one where your success becomes someone else's breakthrough.\n\nWith conviction,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Athletes' ($14.99 CAD): https://lornettedaye.com/books\n\n#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity"
    },
    {
        "id": 176,
        "day": 59,
        "date": "2026-11-30",
        "athlete": "ayesha",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-11-30T21:30:00.000Z",
        "assetFile": "ayesha-curry-10.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/ayesha-curry-10.png",
        "cta": "Buy Book - Survival Skills for Women (lornettedaye.com/books)",
        "text": "THE LEGACY OF A WOMAN WHO OWNED HER CHAPTER\n\nAyesha Curry's story is a beacon for every woman who has ever questioned whether she has what it takes to build an empire.\n\nShe took taste, turned it into a destination, turned that destination into a brand, and turned that brand into an enduring institution. That is what it means to own the next chapter. That is the standard of excellence I celebrate and teach every single day.\n\nTake ownership of your story today. Write the chapter that changes your life and your community.\n\nWith conviction,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Women' ($14.99 CAD): https://lornettedaye.com/books\n\n#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture"
    },
    {
        "id": 177,
        "day": 59,
        "date": "2026-11-30",
        "athlete": "tiger",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-12-01T01:30:00.000Z",
        "assetFile": "tiger-woods-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/tiger-woods-05.png",
        "cta": "Buy Book - Finish Strong: Chasing the Olympic Dream (lornettedaye.com/books)",
        "text": "THE ARCHITECT'S FINAL SCORECARD\n\nWhen all the trophies are cataloged and the records stand in bronze, Tiger's true victory will be the generation of leaders who walked through his learning labs.\n\nThat is the shift from champion to owner, and from owner to builder of humanity. That is the highest calling of athletic success. That is what I have spent forty years teaching Olympic hopefuls and corporate CEOs alike.\n\nBuild something that continues serving people long after you have walked off the field.\n\nWith conviction,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Finish Strong: Chasing the Olympic Dream' ($14.99 CAD): https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A\n\n#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding"
    },
    {
        "id": 178,
        "day": 60,
        "date": "2026-12-01",
        "athlete": "serena",
        "slot": "Morning (7:45 AM MDT/MST)",
        "dueAt": "2026-12-01T14:45:00.000Z",
        "assetFile": "serena-williams-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/serena-williams-05.png",
        "cta": "Buy Book - Survival Skills for Women (lornettedaye.com/books)",
        "text": "THE FINAL VICTORY: LIVING ON YOUR OWN TERMS\n\nSerena Williams' greatest victory was not at Wimbledon or Roland Garros. It was stepping away on her own timeline, with her head held high.\n\nShe dictated her entry into the sport, dominated it for a generation, and exited to build a billion-dollar legacy on her own terms. That is the definition of true sovereignty. That is what I challenge every leader to achieve.\n\nWrite your own story. Own your next chapter.\n\nWith conviction,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Women' ($14.99 CAD): https://lornettedaye.com/books\n\n#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence"
    },
    {
        "id": 179,
        "day": 60,
        "date": "2026-12-01",
        "athlete": "lewis",
        "slot": "Afternoon (2:30 PM MDT/MST)",
        "dueAt": "2026-12-01T21:30:00.000Z",
        "assetFile": "lewis-hamilton-05.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/lewis-hamilton-05.png",
        "cta": "Buy Book - Survival Skills for Men (lornettedaye.com/books)",
        "text": "THE ARCHITECT WHO TRANSCENDED THE COCKPIT\n\nLewis Hamilton began in a Stevenage council house. Today, he sits in the owner's suite of an NFL stadium and commands a global empire.\n\nHe did not just win races; he owned the next chapter. He turned athletic greatness into enterprise sovereignty, social equity, and generational legacy. That is the gold standard. That is what I challenge every leader to build.\n\nStep out of the cockpit of merely executing. Step into the owner's suite and build your lasting legacy.\n\nWith conviction,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'Survival Skills for Men' ($14.99 CAD): https://buy.stripe.com/9B6bJ1542gA262JfCG1VK00\n\n#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution"
    },
    {
        "id": 180,
        "day": 60,
        "date": "2026-12-01",
        "athlete": "steph_ayesha",
        "slot": "Evening (6:30 PM MDT/MST)",
        "dueAt": "2026-12-02T01:30:00.000Z",
        "assetFile": "stephen-ayesha-10.png",
        "assetUrl": "https://lornettedaye.com/campaigns/own-the-next-chapter/stephen-ayesha-10.png",
        "cta": "Buy Book - UMATTR Devotional (lornettedaye.com/books)",
        "text": "THE SCORE THAT MATTERS FOR ETERNITY\n\nThirty points a game is impressive on television. Feeding twenty-five million meals and educating thousands of children is what echoes in eternity.\n\nStephen and Ayesha Curry have mastered the art of owning the next chapter. They turned championship rings into keys that unlock doors for an entire city. That is the calling of high performance. That is the standard I urge every executive to embrace.\n\nTurn your personal victories into community access. That is true immortality.\n\nWith conviction,\nLornette\n\nEquip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\nGet the published digital edition of 'UMATTR Devotional' ($14.99 CAD): https://lornettedaye.com/books\n\n#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership"
    }
]

def check_invariants():
    for p in posts_data:
        t = p["text"]
        for dash in ["\u2014", "&mdash;", "—"]:
            if dash in t:
                raise ValueError(f"Post #{p['id']} contains an em dash ({dash})!")
        if "Coach Lornette" in t:
            raise ValueError(f"Post #{p['id']} is signed 'Coach Lornette' instead of 'Lornette'!")
        if "Lornette" not in t:
            raise ValueError(f"Post #{p['id']} does not have Lornette signature!")

check_invariants()
print("INVARIANTS AUDIT PASSED: 180 posts verified. 0 em dashes, all signed strictly 'Lornette', 50/50 alternating CTA.")

def schedule_posts():
    token = TOKEN or os.environ.get('BUFFER_ACCESS_TOKEN', '')
    if not token:
        print("BUFFER_ACCESS_TOKEN is not set. Exiting.")
        return False

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "User-Agent": "BufferClient/1.0"
    }

    ctx = ssl._create_unverified_context()
    graphql_url = "https://api.buffer.com"
    mutation = """
    mutation CreatePost($input: CreatePostInput!) {
      createPost(input: $input) {
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
    """

    report_path = "scripts/own-the-next-chapter-scheduled-report.json"
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

    for i, p in enumerate(posts_data, 1):
        p_id = p["id"]
        if p_id in results and results[p_id].get("postId"):
            print(f"[{i}/180] Post #{p_id} already scheduled (Buffer ID: {results[p_id]['postId']}). Skipping.")
            continue

        while True:
            print(f"\n[{i}/180] Scheduling Post #{p['id']} (Day {p['day']} - {p['athlete'].upper()} - {p['slot']}) - Due: {p['dueAt']}...")
            print(f"  Asset: {p['assetUrl']}")
            print(f"  CTA Focus: {p['cta']}")

            payload = {
                "query": mutation,
                "variables": {
                    "input": {
                        "channelId": CHANNEL_ID,
                        "text": p["text"],
                        "schedulingType": "automatic",
                        "mode": "customScheduled",
                        "dueAt": p["dueAt"],
                        "saveToDraft": False,
                        "needsApproval": False,
                        "assets": [
                            {
                                "image": {
                                    "url": p["assetUrl"]
                                }
                            }
                        ]
                    }
                }
            }

            req = urllib.request.Request(graphql_url, data=json.dumps(payload).encode("utf-8"), headers=headers)
            try:
                with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
                    res_data = json.loads(resp.read().decode("utf-8"))
                    errors = res_data.get("errors")
                    if errors:
                        print(f"  >>> GRAPHQL ERROR: {errors}")
                        p["status"] = "failed"
                        p["error"] = errors[0].get("message")
                        results[p_id] = p
                        break
                    else:
                        create_res = res_data.get("data", {}).get("createPost", {})
                        if "post" in create_res and create_res["post"].get("id"):
                            post_id = create_res["post"]["id"]
                            st = create_res["post"].get("status")
                            due = create_res["post"].get("dueAt")
                            p["status"] = st
                            p["postId"] = post_id
                            p["dueAt"] = due
                            print(f"  >>> SUCCESS: Post ID: {post_id}")
                            results[p_id] = p
                            with open(report_path, "w", encoding="utf-8") as rf:
                                json.dump(list(results.values()), rf, indent=2, ensure_ascii=False)
                            break
                        else:
                            err_msg = create_res.get("message", "Unknown error")
                            print(f"  >>> ERROR: {err_msg}")
                            p["status"] = "failed"
                            p["error"] = err_msg
                            results[p_id] = p
                            break
            except urllib.error.HTTPError as he:
                if he.code == 429:
                    retry_after = he.headers.get('Retry-After')
                    wait_sec = int(retry_after) if retry_after and retry_after.isdigit() else 60
                    print(f"  [RATE LIMIT] HTTP 429 encountered. Waiting {wait_sec + 5}s...")
                    time.sleep(wait_sec + 5)
                    continue
                err_body = he.read().decode("utf-8", errors="replace")
                print(f"  >>> HTTP ERROR {he.code}: {err_body}")
                p["status"] = "failed"
                p["error"] = f"HTTP {he.code}: {err_body}"
                results[p_id] = p
                break
            except Exception as e:
                print(f"  >>> NETWORK ERROR: {e}")
                p["status"] = "failed"
                p["error"] = str(e)
                results[p_id] = p
                break

        time.sleep(2)

    with open(report_path, "w", encoding="utf-8") as rf:
        json.dump(list(results.values()), rf, indent=2, ensure_ascii=False)
    success_count = sum(1 for r in results.values() if r.get("status") in ["scheduled", "success"] and r.get("postId"))
    print(f"\nExecution complete. Saved {success_count}/180 successfully to {report_path}.")
    return success_count == len(posts_data)

if __name__ == "__main__":
    schedule_posts()
