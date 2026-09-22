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

CDN_BASE = 'https://lornettedaye.com/campaigns/juju-business'

posts_data = [
    # -------------------------------------------------------------
    # BATCH 1: JUJU WATKINS - BUSINESS & NIL EQUITY (POSTS 1 to 10)
    # -------------------------------------------------------------
    {
        "id": 1,
        "slot": "Tuesday Afternoon (2:45 PM MDT)",
        "dueAt": "2026-10-06T20:45:00.000Z",
        "assetFile": "juju-business-01.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": (
            "DON'T JUST SIGN DEALS. BUILD EQUITY. 💼🏀\n\n"
            "The new era of athlete empowerment: JuJu Watkins and business ownership.\n\n"
            "For generations, student-athletes generated billions for collegiate athletic departments "
            "while being barred from earning a single dollar. Today, the NIL landscape has opened the floodgates, "
            "but many young athletes are still operating under outdated paradigms: taking short-term brand cash "
            "rather than building lasting financial sovereignty.\n\n"
            "JuJu Watkins is changing the game by demanding equity, board representation, and strategic alignment. "
            "She proves that an athlete can command the court while architecting a modern corporate portfolio.\n\n"
            "Leaders & Athletes: Are you settling for fee-for-service compensation, or building assets that appreciate over time?\n\n"
            "👉 Learn how to transition from athletic performance to enduring generational impact. "
            "Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#JuJuWatkins #NILEquity #AthleteEntrepreneur #GenerationalWealth #WomensBasketball #BusinessLeadership #SportsBusiness #FinishStrong #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/juju-business-01.png"
    },
    {
        "id": 2,
        "slot": "Thursday Afternoon (2:45 PM MDT)",
        "dueAt": "2026-10-08T20:45:00.000Z",
        "assetFile": "juju-business-02.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "THE ATHLETE BALANCE SHEET: CONVERTING INFLUENCE INTO ENTERPRISE. 📊✨\n\n"
            "Social media followers do not pay mortgages; equity portfolios do.\n\n"
            "Influence without enterprise is fleeting. When the cameras turn to the next recruiting class, "
            "what remains of your athletic brand? JuJu Watkins demonstrates that true business acumen is about "
            "converting cultural relevance into verifiable enterprise value: intellectual property, equity stakes, "
            "and long-term commercial infrastructure.\n\n"
            "In four decades mentoring elite athletes, the ones who thrive post-career are those who treat their name "
            "not merely as a trademark, but as a venture studio. That mindset starts on day one.\n\n"
            "Executives: Is your brand converting surface attention into measurable enterprise equity?\n\n"
            "👉 Bring Olympic-caliber discipline and strategic alignment to your executive leadership team. "
            "Inquire for keynote engagements: lornettedaye.com/speaking\n\n"
            "#AthleteEnterprise #BrandValuation #JuJuWatkins #SportsVenture #ExecutiveLeadership #HighPerformance #OlympicCoach #LornetteDaye #KeynoteSpeaker"
        ),
        "assetUrl": f"{CDN_BASE}/juju-business-02.png"
    },
    {
        "id": 3,
        "slot": "Saturday Afternoon (2:45 PM MDT)",
        "dueAt": "2026-10-10T20:45:00.000Z",
        "assetFile": "juju-business-03.png",
        "cta": "Survival Skills for Athletes (lornettedaye.com/books)",
        "text": (
            "CONTRACT SOVEREIGNTY IN MODERN SPORTS. 📜⚖️\n\n"
            "Saying no to bad terms is the ultimate power move.\n\n"
            "In the excitement of collegiate NIL offers, it is easy to sign away licensing rights, image usage, "
            "and exclusivity clauses for quick upfront bonuses. The athletes who establish generational empires "
            "are the ones who know how to protect their legal and creative autonomy.\n\n"
            "JuJu Watkins' strategic discipline at USC proves that selectivity creates premium positioning. "
            "When you hold a high standard for brand partnerships, corporations don't just sponsor you; they partner with you as an equal.\n\n"
            "Athletes: Are your contracts serving your future, or restricting your freedom?\n\n"
            "👉 Equip yourself with the focus, discernment, and principles needed to excel on and off the court. "
            "Explore *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#ContractSovereignty #NILStrategy #JuJuWatkins #SportsBusiness #SurvivalSkillsForAthletes #BrandProtection #EliteAthletes #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/juju-business-03.png"
    },
    {
        "id": 4,
        "slot": "Monday Afternoon (2:45 PM MDT)",
        "dueAt": "2026-10-12T20:45:00.000Z",
        "assetFile": "juju-business-04.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "BOARDROOM LEADERSHIP BEFORE GRADUATION. 🏢🔥\n\n"
            "Commanding the room with preparation and poise.\n\n"
            "Walk into any Fortune 500 boardroom and the dynamic is unmistakable. "
            "Most people wait decades to earn a seat at the decision-making table. "
            "JuJu Watkins is redefining that timeline: sitting across from senior executives, analyzing cap sheets, "
            "and negotiating terms with the same calm poise she displays at the free throw line with two seconds on the clock.\n\n"
            "Poise under pressure is a universal currency. When you master it on the court, it translates effortlessly into corporate authority.\n\n"
            "Leaders: How are you preparing the young innovators in your organization to command the boardroom?\n\n"
            "👉 Inspire your leadership pipeline to lead with courage and poise. "
            "Book Coach Lornette Daye for your corporate convention: lornettedaye.com/speaking\n\n"
            "#BoardroomLeadership #JuJuWatkins #YoungExecutives #ExecutivePoise #WomenInLeadership #OlympicMindset #CorporateStrategy #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/juju-business-04.png"
    },
    {
        "id": 5,
        "slot": "Wednesday Afternoon (2:45 PM MDT)",
        "dueAt": "2026-10-14T20:45:00.000Z",
        "assetFile": "juju-business-05.png",
        "cta": "Survival Skills for Women (lornettedaye.com/books)",
        "text": (
            "BRAND PRESERVATION: PROTECTING YOUR CORE IDENTITY. 🛡️💎\n\n"
            "Authenticity cannot be bought; it must be protected.\n\n"
            "As an athlete's profile explodes, sponsors will ask you to compromise your voice, promote products "
            "that contradict your values, or soften your personality to appease algorithms. "
            "JuJu Watkins represents unapologetic authenticity: proud of her roots, anchored in her community, "
            "and clear about what she stands for.\n\n"
            "Your brand is not what you tell people; it is the values you refuse to compromise when money is on the table.\n\n"
            "Women in Business & Leadership: What non-negotiable core value keeps your professional journey grounded?\n\n"
            "👉 Build unshakeable confidence, identity, and resilience through every chapter of life. "
            "Explore *Survival Skills for Women* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#BrandPreservation #AuthenticLeadership #JuJuWatkins #SurvivalSkillsForWomen #CoreValues #WomenInBusiness #IdentityBeyondSport #CoachLornette"
        ),
        "assetUrl": f"{CDN_BASE}/juju-business-05.png"
    },
    {
        "id": 6,
        "slot": "Friday Afternoon (2:45 PM MDT)",
        "dueAt": "2026-10-16T20:45:00.000Z",
        "assetFile": "juju-business-06.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": (
            "THE COLLEGIATE CEO: BALANCING COURTHOUSE WITH BOARDROOM. ⏱️📚\n\n"
            "Mastering the art of ruthless time management.\n\n"
            "Consider the daily schedule: 6:00 AM film review, morning lectures, two-hour team practice, "
            "weight training, sports medicine rehab, brand strategy calls, and evening academic study. "
            "This is not just student life; it is running an executive enterprise while competing at the highest NCAA level.\n\n"
            "JuJu Watkins proves that discipline is not about having more time; it is about having crystal clarity on your priorities. "
            "When your goals are clear, distractions lose their power.\n\n"
            "How do you organize your calendar to ensure your primary objectives get your highest energy?\n\n"
            "👉 Master elite time discipline and purposeful focus. "
            "Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#CollegiateCEO #JuJuWatkins #TimeManagement #ExecutiveDiscipline #FocusWins #FinishStrong #OlympicStandards #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/juju-business-06.png"
    },
    {
        "id": 7,
        "slot": "Sunday Afternoon (2:45 PM MDT)",
        "dueAt": "2026-10-18T20:45:00.000Z",
        "assetFile": "juju-business-07.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "WEALTH LITERACY FOR THE NEXT GENERATION OF WOMEN SPORTS LEADERS. 💰🏛️\n\n"
            "Breaking financial cycles and establishing generational foundations.\n\n"
            "Historically, women athletes received a fraction of commercial opportunities. "
            "Today, leaders like JuJu Watkins are proving that women's sports is not a charity; it is a blue-chip investment asset class. "
            "By mastering tax efficiency, venture investments, and trusts, modern female athletes are setting a new standard "
            "for generational wealth literacy that will impact communities for decades.\n\n"
            "True empowerment happens when financial knowledge is paired with athletic excellence.\n\n"
            "What financial lesson do you wish you had learned at the start of your professional journey?\n\n"
            "👉 Empower your workforce with high-performance financial and leadership frameworks. "
            "Book Coach Lornette Daye: lornettedaye.com/speaking\n\n"
            "#WealthLiteracy #JuJuWatkins #WomensSportsRevenue #GenerationalWealth #FinancialEmpowerment #OlympicCoach #LornetteDaye #Leadership"
        ),
        "assetUrl": f"{CDN_BASE}/juju-business-07.png"
    },
    {
        "id": 8,
        "slot": "Tuesday Afternoon (2:45 PM MDT)",
        "dueAt": "2026-10-20T20:45:00.000Z",
        "assetFile": "juju-business-08.png",
        "cta": "Survival Skills for Athletes (lornettedaye.com/books)",
        "text": (
            "LONG-TERM CAP TABLES OVER SHORT-TERM CHECKS. 📈💡\n\n"
            "The investor mentality separates operators from icons.\n\n"
            "When brands approach an elite athlete, the standard instinct is to quote an endorsement fee. "
            "The visionary athlete asks: 'What percentage of equity am I earning in exchange for driving customer acquisition?'\n\n"
            "JuJu Watkins' strategic positioning aligns with the top echelon of athlete investors: LeBron James, Serena Williams, and Kevin Durant. "
            "She understands that endorsement checks run out, but equity distributions compound forever.\n\n"
            "Athletes & Founders: Are you thinking in quarters or thinking in generations?\n\n"
            "👉 Build a champion mindset that outlasts the final buzzer. "
            "Explore *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#CapTables #InvestorMindset #JuJuWatkins #EquityOverEndorsements #SportsVenture #SurvivalSkillsForAthletes #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/juju-business-08.png"
    },
    {
        "id": 9,
        "slot": "Thursday Afternoon (2:45 PM MDT)",
        "dueAt": "2026-10-22T20:45:00.000Z",
        "assetFile": "juju-business-09.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "THE INNER CIRCLE: MENTORSHIP AND EXECUTIVE COUNSEL. 🤝🛡️\n\n"
            "No champion reaches the summit alone.\n\n"
            "Behind every elite athlete who makes seamless business decisions is a fortress of trusted counsel: "
            "attorneys who scrutinize every clause, mentors who have walked the path before, and family members who keep their feet on the ground.\n\n"
            "JuJu Watkins surrounds herself with seasoned advisors who care more about her long-term well-being than quick commissions. "
            "When your circle protects your integrity, your career has no ceiling.\n\n"
            "Leaders: Who is in your confidential advisory circle challenging your blind spots?\n\n"
            "👉 Strengthen executive alignment and mentorship cultures across your organization. "
            "Inquire with Coach Lornette Daye: lornettedaye.com/speaking\n\n"
            "#MentorshipMatters #InnerCircle #JuJuWatkins #AdvisoryBoard #ExecutiveCounsel #HighPerformance #LornetteDaye #Speaker"
        ),
        "assetUrl": f"{CDN_BASE}/juju-business-09.png"
    },
    {
        "id": 10,
        "slot": "Saturday Afternoon (2:45 PM MDT)",
        "dueAt": "2026-10-24T20:45:00.000Z",
        "assetFile": "juju-business-10.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": (
            "THE BLUEPRINT FOR WOMEN ATHLETE ENTREPRENEURS. 👑⚡️\n\n"
            "Creating pathways for millions who will follow.\n\n"
            "What JuJu Watkins is executing in Los Angeles is more than individual business success; "
            "it is a scalable playbook for young women athletes nationwide. It proves that you can be fierce on the floor, "
            "brilliant in negotiations, and grounded in community service all at the same time.\n\n"
            "When one door opens for an athlete who honors the opportunity, she holds that door open for a thousand others. "
            "That is the true definition of leadership.\n\n"
            "How are you using your platform to pave the way for those rising behind you?\n\n"
            "👉 Embrace your purpose, build your legacy, and finish strong. "
            "Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#WomensSports #AthleteEntrepreneurs #JuJuWatkins #FinishStrong #LegacyBuilding #PaveTheWay #OlympicLeadership #CoachLornette #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/juju-business-10.png"
    },

    # -------------------------------------------------------------
    # BATCH 2: NAOMI OSAKA - FOUNDER, OWNER & TRAILBLAZER (POSTS 11 to 20)
    # -------------------------------------------------------------
    {
        "id": 11,
        "slot": "Monday Afternoon (2:45 PM MDT)",
        "dueAt": "2026-10-26T20:45:00.000Z",
        "assetFile": "juju-business-11.png",
        "cta": "Survival Skills for Women (lornettedaye.com/books)",
        "text": (
            "THE TROPHIES WERE NEVER THE WHOLE PLAN: NAOMI OSAKA'S OWNERSHIP REVOLUTION. 🎾🏆\n\n"
            "Four Grand Slam titles. Multi-company founder. Team owner. Trailblazer.\n\n"
            "When Naomi Osaka captured global headlines on the tennis court, the world tried to define her by match points and trophy presentations. "
            "Yet Naomi recognized early that an athletic career is merely the launchpad, not the destination. "
            "She expanded beyond the court to build a global business empire centered on ownership, creative agency, and social purpose.\n\n"
            "In four decades coaching Olympic athletes, the most transformative figures are those who understand that sport provides a platform, "
            "but purpose dictates legacy. Naomi Osaka did not just play the game. She rewrote the rules of athlete sovereignty.\n\n"
            "Leaders: Are you defining yourself solely by your current title, or building an enduring ecosystem?\n\n"
            "👉 Rebuild confidence, discover deep purpose, and thrive through every season. "
            "Explore *Survival Skills for Women* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#NaomiOsaka #FounderOwnerStoryteller #AthleteOwnership #WomenInSports #Kinlo #HanaKuma #SportsBusiness #SurvivalSkillsForWomen #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/juju-business-11.png"
    },
    {
        "id": 12,
        "slot": "Wednesday Afternoon (2:45 PM MDT)",
        "dueAt": "2026-10-28T20:45:00.000Z",
        "assetFile": "juju-business-12.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "KINLÒ: PURPOSEFUL ENTREPRENEURSHIP FOR UNDERSERVED COMMUNITIES. ☀️🧴\n\n"
            "Naomi Osaka identified an urgent healthcare void and built the solution.\n\n"
            "Many celebrity brands slap a famous name onto generic products. Naomi Osaka took a radically different approach with KINLÒ: "
            "she created specialized skincare formulated specifically to protect melanated skin from sun damage and skin cancer risks, "
            "addressing a public health gap that major conglomerates had overlooked for decades.\n\n"
            "This is what purposeful entrepreneurship looks like. It is not just about profit margins; it is about leveraging your platform "
            "to solve authentic problems for the people you care about most.\n\n"
            "Executives: Is your organization solving real community needs or just manufacturing noise?\n\n"
            "👉 Train your corporate leadership to lead with authentic social conviction and Olympic focus. "
            "Inquire for executive keynotes: lornettedaye.com/speaking\n\n"
            "#Kinlo #NaomiOsaka #PurposeDrivenBusiness #SkincareForAll #SocialEntrepreneurship #WomenFounders #ExecutiveLeadership #CoachLornette #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/juju-business-12.png"
    },
    {
        "id": 13,
        "slot": "Friday Afternoon (2:45 PM MDT)",
        "dueAt": "2026-10-30T20:45:00.000Z",
        "assetFile": "juju-business-13.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": (
            "HANA KUMA: OWNING THE NARRATIVE AND TELLING UNFILTERED STORIES. 🎬🌍\n\n"
            "Naomi Osaka is transforming global media production from the creator chair.\n\n"
            "For years, athletes allowed external media conglomerates to frame their stories, dictate their public image, "
            "and control the rights to their life journeys. With Hana Kuma, Naomi Osaka built a premier media production company "
            "dedicated to culturally distinct stories that cross global borders and amplify multicultural voices.\n\n"
            "When you own the production company, you own the narrative. You decide how triumph is celebrated, "
            "how struggle is shared, and how the next generation sees themselves reflected on screen.\n\n"
            "What narrative about your life or organization needs to be reclaimed and told on your terms?\n\n"
            "👉 Master the courage to author your own story and finish strong. "
            "Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#HanaKuma #NaomiOsaka #MediaProduction #OwnYourStory #MulticulturalVoices #GlobalStorytelling #FinishStrong #OlympicWisdom #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/juju-business-13.png"
    },
    {
        "id": 14,
        "slot": "Sunday Afternoon (2:45 PM MDT)",
        "dueAt": "2026-11-01T21:45:00.000Z",
        "assetFile": "juju-business-14.png",
        "cta": "Survival Skills for Athletes (lornettedaye.com/books)",
        "text": (
            "FROM ATHLETE TO FRANCHISE OWNER: NORTH CAROLINA COURAGE. ⚽️🏛️\n\n"
            "Naomi Osaka taking equity ownership in women's professional soccer.\n\n"
            "Stepping into team ownership with the NWSL's North Carolina Courage was a defining statement: "
            "female athletes must not merely be employees on the field; they must be owners at the cap table. "
            "By investing directly in women's sports franchises, Naomi demonstrated that the ultimate power "
            "in athletics is shaping the infrastructure that supports female competitors.\n\n"
            "Her investment signals to Wall Street and global venture capital that women's sports is one of the highest-growth "
            "entertainment assets in the world.\n\n"
            "Athletes: How are you investing in the sport and community that provided your initial foundation?\n\n"
            "👉 Develop long-range vision and champion mindset that lasts a lifetime. "
            "Explore *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#NCCourage #NWSL #NaomiOsaka #SportsOwnership #WomensSportsInvestment #FranchiseOwner #SurvivalSkillsForAthletes #LornetteDaye #EquityInSports"
        ),
        "assetUrl": f"{CDN_BASE}/juju-business-14.png"
    },
    {
        "id": 15,
        "slot": "Monday Afternoon (2:45 PM MDT)",
        "dueAt": "2026-11-02T21:45:00.000Z",
        "assetFile": "juju-business-15.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "POISE UNDER SCRUTINY: PROTECTING MENTAL BOUNDARIES WHILE SCALING. 🧠🛡️\n\n"
            "Naomi Osaka's courage to prioritize mental health changed global sports forever.\n\n"
            "When Naomi stepped back from press conferences at Roland Garros to safeguard her mental health, "
            "critics claimed it would destroy her commercial brand. Instead, it galvanized millions worldwide. "
            "It showed that true strength is not tolerating burnout; true strength is having the courage to establish "
            "healthy psychological boundaries in high-stakes environments.\n\n"
            "In four decades coaching Olympic competitors, the athletes who sustain excellence over twenty years "
            "are those who treat mental recovery with the same seriousness as physical conditioning.\n\n"
            "Leaders: Does your company culture celebrate unsustainable burnout, or cultivate resilient stamina?\n\n"
            "👉 Build cultures of sustainable high performance and emotional poise under pressure. "
            "Book Coach Lornette Daye for your executive team: lornettedaye.com/speaking\n\n"
            "#MentalHealthInSports #NaomiOsaka #ExecutiveWellbeing #HealthyBoundaries #OlympicMindset #SustainableExcellence #LornetteDaye #KeynoteSpeaker"
        ),
        "assetUrl": f"{CDN_BASE}/juju-business-15.png"
    },
    {
        "id": 16,
        "slot": "Tuesday Afternoon (2:45 PM MDT)",
        "dueAt": "2026-11-03T21:45:00.000Z",
        "assetFile": "juju-business-16.png",
        "cta": "Survival Skills for Women (lornettedaye.com/books)",
        "text": (
            "THE MULTI-HYPHENATE LEADER: CHAMPION, FOUNDER, INVESTOR, MOTHER. 🌟👶\n\n"
            "Naomi Osaka proves you do not have to surrender who you are to achieve greatness.\n\n"
            "Society often tries to restrict women to one single identity: you can be a world-class competitor, "
            "or a dedicated entrepreneur, or a loving mother. Naomi Osaka rejects those false dichotomies completely. "
            "Returning to elite Grand Slam tennis after becoming a mother while managing multiple enterprises "
            "is a masterclass in modern multidimensional leadership.\n\n"
            "When you align your life with your authentic values, each role enriches the others rather than draining them.\n\n"
            "Women in Leadership: How do you honor the multiple dimensions of your purpose without apologizing?\n\n"
            "👉 Find strength, balance, and resilience through every transition in life. "
            "Explore *Survival Skills for Women* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#MultidimensionalLeadership #NaomiOsaka #WomenWhoLead #WorkingMothers #SurvivalSkillsForWomen #GrandSlamChampion #LornetteDaye #Balance"
        ),
        "assetUrl": f"{CDN_BASE}/juju-business-16.png"
    },
    {
        "id": 17,
        "slot": "Wednesday Afternoon (2:45 PM MDT)",
        "dueAt": "2026-11-04T21:45:00.000Z",
        "assetFile": "juju-business-17.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": (
            "GLOBAL CULTURE AND BRAND SOVEREIGNTY ACROSS CONTINENTS. 🌏🗼\n\n"
            "Bridging Tokyo, North America, and the Caribbean with effortless elegance.\n\n"
            "Naomi Osaka's heritage encompasses Japanese, Haitian, and American roots. "
            "Rather than flattening her identity to fit conventional corporate boxes, she has celebrated every facet of her culture. "
            "From lighting the Olympic cauldron in Tokyo to collaborating with global luxury fashion houses, "
            "she commands international markets with quiet dignity and unmistakable authority.\n\n"
            "Cultural authenticity is not a marketing strategy; it is a superpower that resonates across languages and continents.\n\n"
            "How does your organization honor and leverage diverse cultural perspectives to lead globally?\n\n"
            "👉 Build universal resilience and lead with cultural confidence. "
            "Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#GlobalCulture #NaomiOsaka #CulturalAuthenticity #BrandSovereignty #TokyoOlympics #FinishStrong #InternationalLeadership #CoachLornette #LornetteDaye"
        ),
        "assetUrl": f"{CDN_BASE}/juju-business-17.png"
    },
    {
        "id": 18,
        "slot": "Thursday Afternoon (2:45 PM MDT)",
        "dueAt": "2026-11-05T21:45:00.000Z",
        "assetFile": "juju-business-18.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": (
            "CHAMPIONING EQUITY: REDEFINING HOW WOMEN ATHLETES NEGOTIATE. 💼📈\n\n"
            "Moving from passive endorsement recipient to equity co-creator.\n\n"
            "When Naomi Osaka partner with brands, she demands equity participation, product development input, "
            "and dedicated philanthropic initiatives. She has demonstrated that women athletes can command the highest "
            "commercial compensation in sports history while maintaining absolute creative control.\n\n"
            "Her negotiations have permanently raised the ceiling for every female athlete who will ever sit down "
            "across from a sponsor, agent, or venture capital partner.\n\n"
            "Leaders: Are you creating equitable partnership models that share long-term value creation?\n\n"
            "👉 Elevate your organization's negotiation, diversity, and executive performance. "
            "Book Coach Lornette Daye for your next conference: lornettedaye.com/speaking\n\n"
            "#ChampioningEquity #NaomiOsaka #NegotiationPower #AthleteEquity #WomensSportsBusiness #ExecutiveKeynote #LornetteDaye #LeadershipSummit"
        ),
        "assetUrl": f"{CDN_BASE}/juju-business-18.png"
    },
    {
        "id": 19,
        "slot": "Friday Afternoon (2:45 PM MDT)",
        "dueAt": "2026-11-06T21:45:00.000Z",
        "assetFile": "juju-business-19.png",
        "cta": "Survival Skills for Women (lornettedaye.com/books)",
        "text": (
            "THE COURAGE TO SET BOUNDARIES AND BUILD AN AUTHENTIC LEGACY. 🛡️✨\n\n"
            "Saying no to outside pressure allows you to say yes to your true purpose.\n\n"
            "The world will always have demands on your time, your emotional energy, and your talent. "
            "Naomi Osaka taught a masterclass to the global sports community: you cannot pour from an empty cup. "
            "Setting firm boundaries does not mean you lack competitive drive; it means you have the self-awareness "
            "to protect the flame that fuels your greatness.\n\n"
            "When you protect your inner peace, your creative and entrepreneurial output reaches heights that compromise could never achieve.\n\n"
            "Where do you need to establish healthier boundaries in your professional or personal life today?\n\n"
            "👉 Strengthen your inner foundation and reclaim your peace. "
            "Explore *Survival Skills for Women* ($14.99 CAD): lornettedaye.com/books\n\n"
            "#HealthyBoundaries #NaomiOsaka #InnerPeace #SelfAwarenessInLeadership #SurvivalSkillsForWomen #OlympicWisdom #LornetteDaye #Empowerment"
        ),
        "assetUrl": f"{CDN_BASE}/juju-business-19.png"
    },
    {
        "id": 20,
        "slot": "Saturday Afternoon (2:45 PM MDT)",
        "dueAt": "2026-11-07T21:45:00.000Z",
        "assetFile": "juju-business-20.png",
        "cta": "Finish Strong Book & Executive Coaching (lornettedaye.com)",
        "text": (
            "THE NEW ERA OF SPORTS LEADERSHIP: FOUNDER. OWNER. STORYTELLER. LEADER. 👑🔥\n\n"
            "Naomi Osaka and JuJu Watkins represent the future of sports governance.\n\n"
            "We are witnessing a seismic shift. Athletes are no longer content being passive participants in sports entertainment; "
            "they are the founders, the majority owners, the creative directors, and the visionaries shaping the next century of athletic culture.\n\n"
            "From Naomi Osaka's boardrooms and grand slam courts to JuJu Watkins' collegiate CEO blueprint at USC, "
            "these women remind us that excellence is not defined by external permission. It is claimed through relentless preparation, "
            "unshakeable character, and the courage to build something that outlives your playing days.\n\n"
            "Stand tall in your arena. Lead with vision. And always finish strong.\n\n"
            "👉 Discover how to build enduring leadership and finish strong in every endeavor. "
            "Explore Lornette Daye's official catalog and leadership keynotes: lornettedaye.com\n\n"
            "#NewEraOfSports #NaomiOsaka #JuJuWatkins #WomenInSports #FounderOwnerStoryteller #SportsOwnership #FinishStrong #OlympicStandards #LornetteDaye #ExecutiveCoaching"
        ),
        "assetUrl": f"{CDN_BASE}/juju-business-20.png"
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
    print("=" * 70)
    print("CAMPAIGN 6: JUJU BUSINESS & NAOMI OSAKA - NIL EQUITY & VENTURE OWNERSHIP (20 POSTS)")
    print(f"Target Channel: {CHANNEL_ID} (Lornette Daye LinkedIn)")
    print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    report_path = os.path.join(os.path.dirname(__file__), "juju-business-scheduled-report.json")
    results = {}
    if os.path.exists(report_path):
        try:
            with open(report_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    for item in data:
                        if item.get("status") in ["scheduled", "success"] and item.get("postId"):
                            results[item["id"]] = item
                elif isinstance(data, dict):
                    for item in data.get("results", []):
                        if item.get("status") in ["scheduled", "success"] and item.get("postId"):
                            results[item["id"]] = item
        except Exception as e:
            print(f"Note: Could not parse existing report: {e}")

    for idx, post in enumerate(posts_data, 1):
        p_id = post["id"]
        feature_tag = "NAOMI OSAKA" if p_id >= 11 else "JUJU WATKINS"

        if p_id in results and results[p_id].get("postId"):
            print(f"[{idx}/{len(posts_data)}] ({feature_tag}) Post #{p_id} already scheduled (Buffer ID: {results[p_id]['postId']}). Skipping.")
            continue

        while True:
            print(f"\n[{idx}/{len(posts_data)}] ({feature_tag}) Scheduling: Post #{p_id} ({post['slot']}) - {post['dueAt']}...")
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
                    "feature": feature_tag,
                    "slot": post["slot"],
                    "dueAt": due,
                    "postId": b_id,
                    "status": st,
                    "assetUrl": post["assetUrl"],
                    "cta": post["cta"]
                }
                break
            else:
                err_msg = create_post_data.get("message") or res.get("errors") or res.get("error") or str(res)
                print(f"  >>> ERROR: {err_msg}")
                results[p_id] = {
                    "id": p_id,
                    "feature": feature_tag,
                    "slot": post["slot"],
                    "assetUrl": post["assetUrl"],
                    "error": err_msg,
                    "status": "failed"
                }
                break

        time.sleep(1.5)

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(list(results.values()), f, indent=2)

    print("\n" + "=" * 70)
    print(f"Execution complete. Report written to {report_path}")
    success_count = sum(1 for r in results.values() if r.get("status") in ["scheduled", "success"])
    print(f"Summary: {success_count}/20 posts scheduled successfully.")
    print("=" * 70)

if __name__ == "__main__":
    main()
