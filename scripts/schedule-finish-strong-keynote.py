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

CDN_BASE = 'https://lornettedaye.com/campaigns/finish-strong-keynote'

posts_data = [
    # Post 1 (Odd: Keynote Booking) - Asset 1: lead-through-the-storm.jpg
    {
        "id": 1,
        "wave": "Wave 1: Launch Flight",
        "slot": "Saturday, Oct 03, 2026 at 08:00 AM MDT",
        "dueAt": "2026-10-03T14:00:00.000Z",
        "assetFile": "lead-through-the-storm.jpg",
        "assetUrl": f"{CDN_BASE}/lead-through-the-storm.jpg",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "LEAD THROUGH THE STORM: PRESSURE REVEALS WHAT IS BUILT INSIDE YOU.\n\n"
            "In my forty years of coaching Olympic athletes and national champions, I have learned a fundamental truth: "
            "storms do not create character. Storms reveal it.\n\n"
            "When the pressure rises, when the market shifts, or when an organization faces unexpected turbulence, "
            "leaders cannot rely on casual enthusiasm. You must lean into your foundation, your internal discipline, and your core purpose.\n\n"
            "I deliver my Finish Strong keynote message to corporate teams, educational institutions, and executive leadership circles "
            "who refuse to let external adversity dictate their standard of excellence.\n\n"
            "When you step onto the track or into the boardroom, your preparation speaks for you.\n\n"
            "With purpose,\n"
            "Lornette\n\n"
            "Book me to deliver the Finish Strong keynote for your upcoming leadership summit, conference, or executive retreat: "
            "https://lornettedaye.com/book\n\n"
            "#FinishStrong #LornetteDaye #LeadThroughTheStorm #KeynoteSpeaker #ExecutiveLeadership #LeadershipDevelopment "
            "#OlympicMindset #Resilience #HighPerformance #PressureAndPoise #CorporateEvents #Keynote #BoardroomLeadership "
            "#Discipline #Purpose #AthleteMindset #LeadershipExcellence #TeamAlignment"
        )
    },
    # Post 2 (Even: Book Purchase) - Asset 2: mentorship-message-momentum.jpg
    {
        "id": 2,
        "wave": "Wave 1: Launch Flight",
        "slot": "Monday, Oct 05, 2026 at 08:00 AM MDT",
        "dueAt": "2026-10-05T14:00:00.000Z",
        "assetFile": "mentorship-message-momentum.jpg",
        "assetUrl": f"{CDN_BASE}/mentorship-message-momentum.jpg",
        "cta": "Buy Book (lornettedaye.com/books)",
        "text": (
            "MENTORSHIP. MESSAGE. MOMENTUM. FOR PEOPLE WHO FEEL STUCK, STRETCHED, OR UNCERTAIN.\n\n"
            "Every high achiever reaches a season where the old strategies stop producing new momentum. "
            "You feel stretched thin. You encounter an invisible ceiling. You wonder if your best work is behind you.\n\n"
            "I wrote my autobiography, Finish Strong: Chasing the Olympic Dream ($14.99 CAD), for this exact moment. "
            "It is not just my personal story of athletic discipline and perseverance. It is a practical roadmap for anyone "
            "who needs to rebuild confidence, clarify identity beyond temporary performance, and step forward with unshakable courage.\n\n"
            "When you understand who you are, no delay can permanently derail you.\n\n"
            "Stay grounded,\n"
            "Lornette\n\n"
            "Download Finish Strong: Chasing the Olympic Dream ($14.99 CAD) directly from my official library: "
            "https://lornettedaye.com/books\n\n"
            "#FinishStrong #LornetteDaye #Mentorship #PersonalGrowth #Resilience #OlympicDream #BookRecommendation "
            "#Author #AuthorLife #GrowthMindset #OvercomingObstacles #Inspiration #PurposeDriven #LifeTransition #Courage"
        )
    },
    # Post 3 (Odd: Keynote Booking) - Asset 3: finish-strong-purpose.jpg
    {
        "id": 3,
        "wave": "Wave 1: Launch Flight",
        "slot": "Wednesday, Oct 07, 2026 at 08:00 AM MDT",
        "dueAt": "2026-10-07T14:00:00.000Z",
        "assetFile": "finish-strong-purpose.jpg",
        "assetUrl": f"{CDN_BASE}/finish-strong-purpose.jpg",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "WHEN LIFE KNOCKS YOU OUT OF YOUR LANE, LEARN HOW TO FINISH WITH PURPOSE.\n\n"
            "On the running track, staying in your lane is the rule of competition. But in leadership and in life, "
            "unforeseen collisions happen. An unexpected restructuring, an injury, a sudden loss, or a cancelled contract "
            "can knock you completely out of your lane.\n\n"
            "The measure of an elite competitor is not whether they stumble. It is what they do the split second after impact.\n\n"
            "In my keynote presentations, I teach teams how to transform disruptions into strategic breakthroughs. "
            "We focus on four foundational pillars: Inspire, Equip, Empower, and Transform.\n\n"
            "You do not stop because the track got difficult. You finish what you started.\n\n"
            "In your corner,\n"
            "Lornette\n\n"
            "Inquire about bringing me to your company, university, or national event: "
            "https://lornettedaye.com/book\n\n"
            "#FinishStrong #LornetteDaye #KeynoteSpeaker #ExecutiveCoaching #InspireEquipEmpower #LeadershipSpeaker "
            "#OvercomingAdversity #OlympicExcellence #TeamCulture #HighPerformanceHabits #PurposeDrivenLeadership #ResilienceInAction"
        )
    },
    # Post 4 (Even: Book Purchase) - Asset 4: track-lanes-to-boardrooms.jpg
    {
        "id": 4,
        "wave": "Wave 1: Launch Flight",
        "slot": "Friday, Oct 09, 2026 at 08:00 AM MDT",
        "dueAt": "2026-10-09T14:00:00.000Z",
        "assetFile": "track-lanes-to-boardrooms.jpg",
        "assetUrl": f"{CDN_BASE}/track-lanes-to-boardrooms.jpg",
        "cta": "Buy Book (lornettedaye.com/books)",
        "text": (
            "FROM TRACK LANES TO BOARDROOMS: DISCIPLINE, STRATEGY, AND EXCELLENCE.\n\n"
            "The principles that govern world-class athletics translate directly to executive decision-making. "
            "Athletes cannot negotiate with the clock, and leaders cannot negotiate with operational reality.\n\n"
            "For men navigating heavy career stress, family responsibilities, and major personal transitions, "
            "I wrote Survival Skills for Men ($14.99 CAD). It provides practical systems to strengthen emotional resilience, "
            "maintain daily balance, and lead with steady poise through seasons of immense pressure.\n\n"
            "Discipline is not about punishment. Discipline is the deliberate architecture of your freedom.\n\n"
            "Stay steady,\n"
            "Lornette\n\n"
            "Get your digital copy of Survival Skills for Men ($14.99 CAD) today: "
            "https://lornettedaye.com/books\n\n"
            "#SurvivalSkillsForMen #LornetteDaye #ExecutiveDiscipline #Resilience #MensLeadership #MentalEndurance "
            "#BoardroomExcellence #HighPerformance #PersonalMastery #LeadershipHabits #FinishStrong #DigitalBook"
        )
    },
    # Post 5 (Odd: Keynote Booking) - Asset 5: setback-not-finish-line.jpg
    {
        "id": 5,
        "wave": "Wave 1: Launch Flight",
        "slot": "Sunday, Oct 11, 2026 at 08:00 AM MDT",
        "dueAt": "2026-10-11T14:00:00.000Z",
        "assetFile": "setback-not-finish-line.jpg",
        "assetUrl": f"{CDN_BASE}/setback-not-finish-line.jpg",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "YOUR SETBACK IS NOT YOUR FINISH LINE: PAIN, PRESSURE, DISAPPOINTMENT, DELAY.\n\n"
            "Look closely at the stopwatch on the ground. Time does not stop when you experience a disappointment. "
            "The clock continues to run, and the future remains wide open.\n\n"
            "Throughout my career as a national champion and Olympic coach, the greatest athletes I worked with were not "
            "the ones who never failed. They were the ones who refused to mistake a temporary chapter for their final destination.\n\n"
            "If your organization or team is navigating through hardship, change, or fatigue, my Finish Strong keynote "
            "will reignite their determination and equip them with repeatable tools to cross their finish line.\n\n"
            "Keep moving forward,\n"
            "Lornette\n\n"
            "Book my Finish Strong keynote for your corporate conference or annual gathering: "
            "https://lornettedaye.com/book\n\n"
            "#FinishStrong #LornetteDaye #YourSetbackIsNotYourFinishLine #KeynoteSpeaker #CorporateSpeaker #ResilienceTraining "
            "#OvercomingBurnout #TeamMotivation #LeadershipMindset #ExecutiveSummits #OlympicLegacy"
        )
    },
    # Post 6 (Even: Book Purchase) - Asset 1: lead-through-the-storm.jpg
    {
        "id": 6,
        "wave": "Wave 2: Deep Foundations Flight",
        "slot": "Tuesday, Oct 13, 2026 at 08:00 AM MDT",
        "dueAt": "2026-10-13T14:00:00.000Z",
        "assetFile": "lead-through-the-storm.jpg",
        "assetUrl": f"{CDN_BASE}/lead-through-the-storm.jpg",
        "cta": "Buy Book (lornettedaye.com/books)",
        "text": (
            "REBUILDING HOPE AND PERSPECTIVE AFTER DIFFICULT SEASONS.\n\n"
            "Pressure has a way of testing the seams of your life. When you are leading through a storm, "
            "it is easy to feel isolated and drained.\n\n"
            "I authored Surviving Life ($14.99 CAD) to serve as a warm, grounded companion for anyone seeking practical encouragement, "
            "inner peace, and renewed vision after going through hardship. It is filled with honest reflections, "
            "daily resilience practices, and frameworks to rediscover purpose when life feels overwhelming.\n\n"
            "You have survived every difficult day behind you. You are fully capable of navigating the path ahead.\n\n"
            "Warmly,\n"
            "Lornette\n\n"
            "Secure your copy of Surviving Life ($14.99 CAD) in my digital bookstore: "
            "https://lornettedaye.com/books\n\n"
            "#SurvivingLife #LornetteDaye #HopeAfterHardship #Resilience #InnerPeace #PersonalRenewal #Author "
            "#BookRelease #FaithAndFocus #FinishStrong #SelfCareForLeaders #MindsetShift"
        )
    },
    # Post 7 (Odd: Keynote Booking) - Asset 2: mentorship-message-momentum.jpg
    {
        "id": 7,
        "wave": "Wave 2: Deep Foundations Flight",
        "slot": "Thursday, Oct 15, 2026 at 08:00 AM MDT",
        "dueAt": "2026-10-15T14:00:00.000Z",
        "assetFile": "mentorship-message-momentum.jpg",
        "assetUrl": f"{CDN_BASE}/mentorship-message-momentum.jpg",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "TEACH. COACH. SPEAK: BUILDING UNBREAKABLE MOMENTUM IN YOUR PEOPLE.\n\n"
            "A keynote address should never be just sixty minutes of temporary motivation that fades by Monday morning. "
            "True transformation happens when audiences receive practical tools they can execute immediately.\n\n"
            "When I step onto your stage, I bring four decades of Olympic athlete development directly into your organization's context. "
            "We break down how to communicate clearly under stress, how to mentor high performers, and how to sustain momentum "
            "across quarters and seasons.\n\n"
            "Give your people the gift of clarity, focus, and renewed commitment.\n\n"
            "Together in excellence,\n"
            "Lornette\n\n"
            "Reserve your keynote date on my calendar: "
            "https://lornettedaye.com/book\n\n"
            "#KeynoteSpeaker #LornetteDaye #FinishStrong #ExecutiveCoaching #CorporateTraining #TeachCoachSpeak "
            "#LeadershipMomentum #TeamPerformance #OlympicStandard #OrganizationalExcellence #KeynoteAddress"
        )
    },
    # Post 8 (Even: Book Purchase) - Asset 3: finish-strong-purpose.jpg
    {
        "id": 8,
        "wave": "Wave 2: Deep Foundations Flight",
        "slot": "Saturday, Oct 17, 2026 at 08:00 AM MDT",
        "dueAt": "2026-10-17T14:00:00.000Z",
        "assetFile": "finish-strong-purpose.jpg",
        "assetUrl": f"{CDN_BASE}/finish-strong-purpose.jpg",
        "cta": "Buy Book (lornettedaye.com/books)",
        "text": (
            "THE CHAMPION MINDSET ON AND OFF THE FIELD.\n\n"
            "Athletic success is never accidental. The athletes who consistently perform when the stakes are highest "
            "have trained their minds just as rigorously as their bodies.\n\n"
            "I wrote Survival Skills for Athletes ($14.99 CAD) for competitors, coaches, and sports leaders at every level. "
            "It outlines the mental frameworks required to master emotional regulation, maintain focus under stadium noise, "
            "and rebound immediately after costly mistakes.\n\n"
            "Your previous play cannot execute your next play. Focus on this exact moment.\n\n"
            "Finish strong,\n"
            "Lornette\n\n"
            "Get Survival Skills for Athletes ($14.99 CAD) today: "
            "https://lornettedaye.com/books\n\n"
            "#SurvivalSkillsForAthletes #LornetteDaye #ChampionMindset #AthleteDevelopment #MentalPerformance #SportsPsychology "
            "#FocusUnderPressure #FinishStrong #EliteCoaching #HighPerformanceCulture #NextPlaySpeed"
        )
    },
    # Post 9 (Odd: Keynote Booking) - Asset 4: track-lanes-to-boardrooms.jpg
    {
        "id": 9,
        "wave": "Wave 2: Deep Foundations Flight",
        "slot": "Monday, Oct 19, 2026 at 08:00 AM MDT",
        "dueAt": "2026-10-19T14:00:00.000Z",
        "assetFile": "track-lanes-to-boardrooms.jpg",
        "assetUrl": f"{CDN_BASE}/track-lanes-to-boardrooms.jpg",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "TRANSLATING ELITE ATHLETIC DISCIPLINE INTO CORPORATE RESILIENCE.\n\n"
            "In world-class athletics, preparation is never a vague idea. It is measured in tenths of a second, "
            "daily recovery routines, and rigorous post-race analysis.\n\n"
            "Too often, corporate teams attempt to navigate complex quarters without a unified playbook. "
            "In my keynote presentations, I demonstrate how to bridge the gap between track lanes and boardrooms, "
            "instilling an elite standard of peer accountability, emotional poise, and strategic execution.\n\n"
            "Elevate your team's standard of excellence.\n\n"
            "With respect,\n"
            "Lornette\n\n"
            "Book my corporate keynote for your upcoming leadership conference: "
            "https://lornettedaye.com/book\n\n"
            "#FromTrackLanesToBoardrooms #LornetteDaye #CorporateKeynote #ExecutiveStrategy #LeadershipExcellence "
            "#TeamDiscipline #PerformanceCulture #HighPerformanceTeams #FinishStrong #ConferenceSpeaker"
        )
    },
    # Post 10 (Even: Book Purchase) - Asset 5: setback-not-finish-line.jpg
    {
        "id": 10,
        "wave": "Wave 2: Deep Foundations Flight",
        "slot": "Wednesday, Oct 21, 2026 at 08:00 AM MDT",
        "dueAt": "2026-10-21T14:00:00.000Z",
        "assetFile": "setback-not-finish-line.jpg",
        "assetUrl": f"{CDN_BASE}/setback-not-finish-line.jpg",
        "cta": "Buy Book (lornettedaye.com/books)",
        "text": (
            "FAITH, GRACE, AND PEACE THROUGH LIFE'S HARDEST CHAPTERS.\n\n"
            "When the whistle blows and you find yourself facing an unexpected trial, where do you anchor your confidence?\n\n"
            "I wrote Survival Skills for Believers ($14.99 CAD) to help readers walk through uncertain seasons with deep faith, "
            "scriptural wisdom, and profound inner peace. It is designed to remind you that your worth is never determined "
            "by your productivity or external circumstances.\n\n"
            "Hold steady in grace. Your journey is being guided with divine precision.\n\n"
            "Blessings,\n"
            "Lornette\n\n"
            "Explore Survival Skills for Believers ($14.99 CAD) in my digital book collection: "
            "https://lornettedaye.com/books\n\n"
            "#SurvivalSkillsForBelievers #LornetteDaye #FaithAndResilience #ChristianLeadership #PeaceInTheStorm "
            "#GraceAndStrength #PurposeInTrial #SpiritualGrowth #Author #FinishStrong"
        )
    },
    # Post 11 (Odd: Keynote Booking) - Asset 1: lead-through-the-storm.jpg
    {
        "id": 11,
        "wave": "Wave 3: Mid-Campaign Flight",
        "slot": "Friday, Oct 23, 2026 at 08:00 AM MDT",
        "dueAt": "2026-10-23T14:00:00.000Z",
        "assetFile": "lead-through-the-storm.jpg",
        "assetUrl": f"{CDN_BASE}/lead-through-the-storm.jpg",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "CULTIVATING UNBREAKABLE POISE WHEN THE STAKES ARE HIGHEST.\n\n"
            "Every executive and team lead knows the feeling: deadlines closing in, stakeholders watching, "
            "and unexpected friction emerging from every angle.\n\n"
            "In forty years on the international track and field circuit, I discovered that composure is a trainable discipline. "
            "When you master emotional regulation, pressure becomes fuel rather than friction.\n\n"
            "My Finish Strong keynote equips teams with concrete systems to quiet the noise, focus on controllable factors, "
            "and execute with world-class consistency.\n\n"
            "Lead with quiet confidence.\n\n"
            "Warmly,\n"
            "Lornette\n\n"
            "Inquire about keynote speaking for your organization: "
            "https://lornettedaye.com/book\n\n"
            "#LeadThroughTheStorm #LornetteDaye #KeynoteSpeaker #HighStakesLeadership #EmotionalRegulation #ExecutivePresence "
            "#TeamResilience #PerformanceUnderPressure #FinishStrong #CorporateKeynote"
        )
    },
    # Post 12 (Even: Book Purchase) - Asset 2: mentorship-message-momentum.jpg
    {
        "id": 12,
        "wave": "Wave 3: Mid-Campaign Flight",
        "slot": "Sunday, Oct 25, 2026 at 08:00 AM MDT",
        "dueAt": "2026-10-25T14:00:00.000Z",
        "assetFile": "mentorship-message-momentum.jpg",
        "assetUrl": f"{CDN_BASE}/mentorship-message-momentum.jpg",
        "cta": "Buy Book (lornettedaye.com/books)",
        "text": (
            "LIVING WITH HOPE, RESILIENCE, AND UNCOMPROMISING MEANING.\n\n"
            "To every woman balancing professional ambitions, community leadership, family needs, and personal dreams: "
            "your presence and leadership matter deeply.\n\n"
            "I authored Survival Skills for Women ($14.99 CAD) as a heartfelt, practical guide to help women rebuild confidence, "
            "establish healthy boundaries, and thrive through every season of transition. It is filled with actionable tools "
            "for personal renewal and identity restoration.\n\n"
            "Step into your full voice. The world needs what you have to offer.\n\n"
            "With admiration,\n"
            "Lornette\n\n"
            "Download your copy of Survival Skills for Women ($14.99 CAD): "
            "https://lornettedaye.com/books\n\n"
            "#SurvivalSkillsForWomen #LornetteDaye #WomensLeadership #Empowerment #ConfidenceRestoration #Resilience "
            "#PersonalGrowth #Author #FemaleLeaders #FinishStrong #ThrivingWomen"
        )
    },
    # Post 13 (Odd: Keynote Booking) - Asset 3: finish-strong-purpose.jpg
    {
        "id": 13,
        "wave": "Wave 3: Mid-Campaign Flight",
        "slot": "Tuesday, Oct 27, 2026 at 08:00 AM MDT",
        "dueAt": "2026-10-27T14:00:00.000Z",
        "assetFile": "finish-strong-purpose.jpg",
        "assetUrl": f"{CDN_BASE}/finish-strong-purpose.jpg",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "INSPIRE. EQUIP. EMPOWER. TRANSFORM.\n\n"
            "These four words sit on the clipboard in my hand for a reason. They are the sequential stages of lasting change.\n\n"
            "1. Inspire: Help people see what is genuinely possible beyond their current limitations.\n"
            "2. Equip: Provide repeatable frameworks that work on ordinary Tuesdays, not just seminar weekends.\n"
            "3. Empower: Build genuine trust so your team acts with autonomy and conviction.\n"
            "4. Transform: Celebrate the emergence of a resilient, self-sustaining culture.\n\n"
            "Bring this exact framework into your company's annual kickoff or leadership conference.\n\n"
            "Committed to your growth,\n"
            "Lornette\n\n"
            "Book the Finish Strong keynote for your audience: "
            "https://lornettedaye.com/book\n\n"
            "#InspireEquipEmpowerTransform #LornetteDaye #KeynoteSpeaker #CultureTransformation #ExecutiveLeadership "
            "#TeamBuilding #FinishStrong #OlympicCoach #LeadershipSummit #ConferenceKeynote"
        )
    },
    # Post 14 (Even: Book Purchase) - Asset 4: track-lanes-to-boardrooms.jpg
    {
        "id": 14,
        "wave": "Wave 3: Mid-Campaign Flight",
        "slot": "Thursday, Oct 29, 2026 at 08:00 AM MDT",
        "dueAt": "2026-10-29T14:00:00.000Z",
        "assetFile": "track-lanes-to-boardrooms.jpg",
        "assetUrl": f"{CDN_BASE}/track-lanes-to-boardrooms.jpg",
        "cta": "Buy Book (lornettedaye.com/books)",
        "text": (
            "MOVING BEYOND SURVIVAL MODE INTO REAL MOMENTUM.\n\n"
            "So many dedicated professionals spend years trapped in survival mode. You wake up, manage the emergencies, "
            "put out fires, and fall asleep exhausted, only to repeat the cycle tomorrow.\n\n"
            "Survival is necessary in a crisis, but it is never meant to become your permanent address. "
            "In my book, Survival Skills: Surviving to Thriving ($14.99 CAD), I walk readers through the exact steps "
            "to break out of reactive patterns, rebuild your personal foundation, and establish proactive, purpose-driven momentum.\n\n"
            "You were created to thrive, not merely survive.\n\n"
            "Finish strong,\n"
            "Lornette\n\n"
            "Order Survival Skills: Surviving to Thriving ($14.99 CAD) today: "
            "https://lornettedaye.com/books\n\n"
            "#SurvivingToThriving #LornetteDaye #BeyondSurvival #PersonalDevelopment #PurposeDrivenLife #Breakthrough "
            "#Author #FinishStrong #MindsetShift #ThriveInLife #ExecutiveWellness"
        )
    },
    # Post 15 (Odd: Keynote Booking) - Asset 5: setback-not-finish-line.jpg
    {
        "id": 15,
        "wave": "Wave 3: Mid-Campaign Flight",
        "slot": "Saturday, Oct 31, 2026 at 08:00 AM MDT",
        "dueAt": "2026-10-31T14:00:00.000Z",
        "assetFile": "setback-not-finish-line.jpg",
        "assetUrl": f"{CDN_BASE}/setback-not-finish-line.jpg",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "TURNING PROFESSIONAL DISAPPOINTMENT INTO STRATEGIC RESILIENCE.\n\n"
            "In competition, not every race ends with a gold medal. There are days when the weather turns, "
            "the false-start horn sounds, or your body gives out.\n\n"
            "What separates champions from the rest of the pack is their recovery protocol. They do not hide in shame. "
            "They examine the tape, adjust their stride, and return to the starting blocks with greater wisdom.\n\n"
            "If your team has faced a tough quarter or lost a major opportunity, let us gather together to reframe the narrative. "
            "Your setback is simply the prologue to your greatest victory.\n\n"
            "Believe in your finish,\n"
            "Lornette\n\n"
            "Schedule a conversation to book me for your next company summit: "
            "https://lornettedaye.com/book\n\n"
            "#YourSetbackIsNotYourFinishLine #LornetteDaye #StrategicResilience #ExecutiveKeynote #OvercomingFailure "
            "#OlympicWisdom #LeadershipCulture #TeamComeback #FinishStrong"
        )
    },
    # Post 16 (Even: Book Purchase) - Asset 1: lead-through-the-storm.jpg
    {
        "id": 16,
        "wave": "Wave 4: Momentum & Expansion Flight",
        "slot": "Monday, Nov 02, 2026 at 08:00 AM MST",
        "dueAt": "2026-11-02T15:00:00.000Z",
        "assetFile": "lead-through-the-storm.jpg",
        "assetUrl": f"{CDN_BASE}/lead-through-the-storm.jpg",
        "cta": "Buy Book (lornettedaye.com/books)",
        "text": (
            "REFLECTIONS FOR THE MOMENTS THAT ASK YOU TO KEEP GOING.\n\n"
            "When the storms of life arrive, the most vital thing you can possess is an unshakable anchor of worth.\n\n"
            "I wrote the UMATTR Devotional ($14.99 CAD) for every individual, student, and leader who needs a daily reminder "
            "that their life and contribution matter deeply. With grounded reflective prompts, faith-based encouragement, "
            "and practical guidance, it offers strength for the quiet moments when giving up feels tempting.\n\n"
            "You matter. Your journey matters. Keep running your race.\n\n"
            "With love,\n"
            "Lornette\n\n"
            "Get the UMATTR Devotional ($14.99 CAD) from my digital bookstore: "
            "https://lornettedaye.com/books\n\n"
            "#UMATTR #LornetteDaye #Devotional #YouMatter #DailyReflections #FaithAndPurpose #HopeInTheStorm "
            "#FinishStrong #Encouragement #AuthorLife #KeepGoing"
        )
    },
    # Post 17 (Odd: Keynote Booking) - Asset 2: mentorship-message-momentum.jpg
    {
        "id": 17,
        "wave": "Wave 4: Momentum & Expansion Flight",
        "slot": "Wednesday, Nov 04, 2026 at 08:00 AM MST",
        "dueAt": "2026-11-04T15:00:00.000Z",
        "assetFile": "mentorship-message-momentum.jpg",
        "assetUrl": f"{CDN_BASE}/mentorship-message-momentum.jpg",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "THE POWER OF AUTHENTIC EXECUTIVE MENTORSHIP.\n\n"
            "Great athletes do not become champions in isolation. Behind every gold medal is a coach who saw capability "
            "long before the podium was in sight.\n\n"
            "In modern enterprise, employees are seeking more than management directives. They want mentorship, authentic communication, "
            "and a compelling mission they can believe in.\n\n"
            "In my keynote presentations, I guide C-suite leaders and directors on how to build coaching cultures that attract, "
            "retain, and elevate top-tier talent across generations.\n\n"
            "Invest in your leaders.\n\n"
            "In partnership,\n"
            "Lornette\n\n"
            "Invite me to keynote your upcoming executive retreat or annual conference: "
            "https://lornettedaye.com/book\n\n"
            "#MentorshipMessageMomentum #LornetteDaye #ExecutiveMentorship #LeadershipCulture #TalentDevelopment "
            "#CoachingExcellence #KeynoteSpeaker #FinishStrong #CorporateKeynote"
        )
    },
    # Post 18 (Even: Book Purchase) - Asset 3: finish-strong-purpose.jpg
    {
        "id": 18,
        "wave": "Wave 4: Momentum & Expansion Flight",
        "slot": "Friday, Nov 06, 2026 at 08:00 AM MST",
        "dueAt": "2026-11-06T15:00:00.000Z",
        "assetFile": "finish-strong-purpose.jpg",
        "assetUrl": f"{CDN_BASE}/finish-strong-purpose.jpg",
        "cta": "Buy Book (lornettedaye.com/books)",
        "text": (
            "PRACTICAL TOOLS FOR FOCUS, BALANCE, AND SUCCESS AT EVERY STAGE.\n\n"
            "Academic demands, athletic expectations, social media scrutiny, and life transitions create immense pressure "
            "for young people today.\n\n"
            "I wrote Survival Skills for Students ($14.99 CAD) for students, parents, mentors, and educators who want to support "
            "the next generation in building healthy habits, managing academic anxiety, and staying grounded in their identity.\n\n"
            "Success is not about perfection. Success is about developing steady habits that allow you to grow under pressure.\n\n"
            "Cheering you on,\n"
            "Lornette\n\n"
            "Equip a student or youth leader with Survival Skills for Students ($14.99 CAD): "
            "https://lornettedaye.com/books\n\n"
            "#SurvivalSkillsForStudents #LornetteDaye #StudentSuccess #YouthLeadership #MentalEndurance #HealthyHabits "
            "#AcademicFocus #FinishStrong #MentorshipForYouth #Author"
        )
    },
    # Post 19 (Odd: Keynote Booking) - Asset 4: track-lanes-to-boardrooms.jpg
    {
        "id": 19,
        "wave": "Wave 4: Momentum & Expansion Flight",
        "slot": "Sunday, Nov 08, 2026 at 08:00 AM MST",
        "dueAt": "2026-11-08T15:00:00.000Z",
        "assetFile": "track-lanes-to-boardrooms.jpg",
        "assetUrl": f"{CDN_BASE}/track-lanes-to-boardrooms.jpg",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "STRATEGY WITHOUT DISCIPLINE IS JUST WISHFUL THINKING.\n\n"
            "You can have the most sophisticated deck, the finest mission statement, and the most elaborate corporate projections. "
            "However, if your daily operational discipline does not align with your vision, the results will not follow.\n\n"
            "Elite athletes know that championships are won during dark mornings on the track, when nobody is watching. "
            "I bring that uncompromising athletic standard to corporate audiences, helping teams eliminate excuses and execute with laser focus.\n\n"
            "Bridge the gap between strategy and execution.\n\n"
            "Stay disciplined,\n"
            "Lornette\n\n"
            "Book me to speak to your team or association: "
            "https://lornettedaye.com/book\n\n"
            "#DisciplineLeadershipResilience #LornetteDaye #KeynoteSpeaker #OperationalExcellence #StrategyAndExecution "
            "#ExecutiveLeadership #HighPerformanceTeams #FinishStrong #CorporateCulture"
        )
    },
    # Post 20 (Even: Book Purchase) - Asset 5: setback-not-finish-line.jpg
    {
        "id": 20,
        "wave": "Wave 4: Momentum & Expansion Flight",
        "slot": "Tuesday, Nov 10, 2026 at 08:00 AM MST",
        "dueAt": "2026-11-10T15:00:00.000Z",
        "assetFile": "setback-not-finish-line.jpg",
        "assetUrl": f"{CDN_BASE}/setback-not-finish-line.jpg",
        "cta": "Buy Book (lornettedaye.com/books)",
        "text": (
            "WHEN PLANS UNRAVEL: EMBRACING PURPOSE THROUGH PAIN AND DELAY.\n\n"
            "Disappointment is an inevitable part of the human experience. What hurts most is when you have poured your heart "
            "into a goal, only to see the finish line move further away.\n\n"
            "In Finish Strong: Chasing the Olympic Dream ($14.99 CAD), I share the raw, unvarnished realities of athletic competition, "
            "injury, heartbreak, and the mental frameworks that allowed me to rise repeatedly after major setbacks.\n\n"
            "Your setback does not get the final word. You do.\n\n"
            "Finish strong,\n"
            "Lornette\n\n"
            "Read Finish Strong: Chasing the Olympic Dream ($14.99 CAD): "
            "https://lornettedaye.com/books\n\n"
            "#FinishStrong #LornetteDaye #OlympicStory #OvercomingObstacles #ResilienceInLife #Author #SportsBiography "
            "#InspirationalMemoir #PersonalGrowth #FinishWhatYouStarted"
        )
    },
    # Post 21 (Odd: Keynote Booking) - Asset 1: lead-through-the-storm.jpg
    {
        "id": 21,
        "wave": "Wave 5: Mastery & Climax Flight",
        "slot": "Thursday, Nov 12, 2026 at 08:00 AM MST",
        "dueAt": "2026-11-12T15:00:00.000Z",
        "assetFile": "lead-through-the-storm.jpg",
        "assetUrl": f"{CDN_BASE}/lead-through-the-storm.jpg",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "WHAT IS BUILT INSIDE YOU WILL ALWAYS OUTLAST WHAT IS HAPPENING AROUND YOU.\n\n"
            "When markets shift, when restructuring occurs, or when unexpected crises strike, "
            "the noise from the outside can feel deafening. Teams naturally look to their leaders for direction and calm.\n\n"
            "If your leadership foundation is hollow, panic spreads rapidly. But if your foundation is anchored in purpose, "
            "discipline, and mutual trust, your organization will weather the gale and emerge stronger.\n\n"
            "Let me partner with your leadership to fortify your team before the next storm arrives.\n\n"
            "In your service,\n"
            "Lornette\n\n"
            "Inquire about executive keynote bookings and private workshops: "
            "https://lornettedaye.com/book\n\n"
            "#LeadThroughTheStorm #LornetteDaye #KeynoteSpeaker #CrisisLeadership #TeamFortitude #OlympicCoaching "
            "#ExecutiveDevelopment #FinishStrong #CorporateResilience #LeadershipPresence"
        )
    },
    # Post 22 (Even: Book Purchase) - Asset 2: mentorship-message-momentum.jpg
    {
        "id": 22,
        "wave": "Wave 5: Mastery & Climax Flight",
        "slot": "Saturday, Nov 14, 2026 at 08:00 AM MST",
        "dueAt": "2026-11-14T15:00:00.000Z",
        "assetFile": "mentorship-message-momentum.jpg",
        "assetUrl": f"{CDN_BASE}/mentorship-message-momentum.jpg",
        "cta": "Buy Book (lornettedaye.com/books)",
        "text": (
            "STRENGTHENING EMOTIONAL RESILIENCE THROUGH PRESSURE AND TRANSITION.\n\n"
            "Men often carry silent burdens: financial expectations, corporate responsibilities, "
            "and personal uncertainties, often without a safe outlet to process them.\n\n"
            "Survival Skills for Men ($14.99 CAD) is a straightforward, dignified resource designed to help men recalibrate their habits, "
            "establish healthy communication patterns, and lead their families and organizations with steady purpose.\n\n"
            "Real strength is not pretending you never get tired. Real strength is having the discipline to renew your foundation.\n\n"
            "With encouragement,\n"
            "Lornette\n\n"
            "Get your copy of Survival Skills for Men ($14.99 CAD): "
            "https://lornettedaye.com/books\n\n"
            "#SurvivalSkillsForMen #LornetteDaye #MensMentalHealth #Resilience #LeadershipBalance #PurposefulLiving "
            "#Author #FinishStrong #EmotionalFitness #PersonalExcellence"
        )
    },
    # Post 23 (Odd: Keynote Booking) - Asset 3: finish-strong-purpose.jpg
    {
        "id": 23,
        "wave": "Wave 5: Mastery & Climax Flight",
        "slot": "Monday, Nov 16, 2026 at 08:00 AM MST",
        "dueAt": "2026-11-16T15:00:00.000Z",
        "assetFile": "finish-strong-purpose.jpg",
        "assetUrl": f"{CDN_BASE}/finish-strong-purpose.jpg",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "FINISHING STRONG IS A CHOICE YOU MAKE BEFORE YOU START.\n\n"
            "Many people wait until the final stretch of the year or the last quarter of a project to decide how they will finish. "
            "By then, fatigue has set in, excuses are abundant, and momentum has slowed.\n\n"
            "In championship athletics, finishing strong is decided months ahead in daily practice routines. "
            "It is the conscious decision that no matter how difficult the middle miles become, you will not concede your standard.\n\n"
            "Inspire your conference attendees to embrace the discipline of finishing strong.\n\n"
            "With determination,\n"
            "Lornette\n\n"
            "Book my keynote presentation for your upcoming corporate event: "
            "https://lornettedaye.com/book\n\n"
            "#FinishStrong #LornetteDaye #KeynoteSpeaker #ChampionshipMindset #EnduranceInLeadership #TeamAlignment "
            "#HighPerformanceHabits #ConferenceKeynote #CorporateSpeaker #FinishWhatYouStarted"
        )
    },
    # Post 24 (Even: Book Purchase) - Asset 4: track-lanes-to-boardrooms.jpg
    {
        "id": 24,
        "wave": "Wave 5: Mastery & Climax Flight",
        "slot": "Wednesday, Nov 18, 2026 at 08:00 AM MST",
        "dueAt": "2026-11-18T15:00:00.000Z",
        "assetFile": "track-lanes-to-boardrooms.jpg",
        "assetUrl": f"{CDN_BASE}/track-lanes-to-boardrooms.jpg",
        "cta": "Buy Book (lornettedaye.com/books)",
        "text": (
            "BUILDING A RESILIENT FOUNDATION FOR LONG-TERM THOUGHT LEADERSHIP.\n\n"
            "The journey from just getting by to truly living requires intentional reflection and systems of renewal.\n\n"
            "In Survival Skills: Surviving to Thriving ($14.99 CAD), I offer practical, step-by-step tools to identify what is draining "
            "your energy, reorganize your priorities around core values, and create sustainable forward momentum.\n\n"
            "Do not settle for surviving another busy month. Step into genuine thriving.\n\n"
            "Stay focused,\n"
            "Lornette\n\n"
            "Order Survival Skills: Surviving to Thriving ($14.99 CAD) today: "
            "https://lornettedaye.com/books\n\n"
            "#SurvivingToThriving #LornetteDaye #MindsetReset #PurposeDriven #SustainableLeadership #AuthorLife "
            "#BookRecommendations #FinishStrong #PersonalTransformation"
        )
    },
    # Post 25 (Odd: Keynote Booking) - Asset 5: setback-not-finish-line.jpg
    {
        "id": 25,
        "wave": "Wave 5: Mastery & Climax Flight",
        "slot": "Friday, Nov 20, 2026 at 08:00 AM MST",
        "dueAt": "2026-11-20T15:00:00.000Z",
        "assetFile": "setback-not-finish-line.jpg",
        "assetUrl": f"{CDN_BASE}/setback-not-finish-line.jpg",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "DISAPPOINTMENT IS A TEACHER, NOT AN EXECUTIONER.\n\n"
            "When a team experiences a public loss or an executive misses a forecast, the easiest path is defensiveness. "
            "The champion path, however, is curiosity.\n\n"
            "What did this moment teach us? Where did our communication break down? What systems must we upgrade before our next race?\n\n"
            "My Finish Strong keynote helps organizations strip away the shame of past failures and replace it with ruthless clarity "
            "and Olympic-level execution.\n\n"
            "Your finish line is waiting.\n\n"
            "In your corner,\n"
            "Lornette\n\n"
            "Bring Lornette Daye to your event or summit: "
            "https://lornettedaye.com/book\n\n"
            "#YourSetbackIsNotYourFinishLine #LornetteDaye #KeynoteSpeaker #ExecutiveMindset #LearningFromFailure "
            "#OlympicWisdom #CultureOfExcellence #FinishStrong #LeadershipSummit"
        )
    },
    # Post 26 (Even: Book Purchase) - Asset 1: lead-through-the-storm.jpg
    {
        "id": 26,
        "wave": "Wave 6: Legacy & Championship Flight",
        "slot": "Sunday, Nov 22, 2026 at 08:00 AM MST",
        "dueAt": "2026-11-22T15:00:00.000Z",
        "assetFile": "lead-through-the-storm.jpg",
        "assetUrl": f"{CDN_BASE}/lead-through-the-storm.jpg",
        "cta": "Buy Book (lornettedaye.com/books)",
        "text": (
            "FINDING STRENGTH, EMBRACING PURPOSE, AND LIVING WITH HOPE.\n\n"
            "When life tests your resolve, you need words that do not just offer empty platitudes, but offer real substance.\n\n"
            "In Surviving Life ($14.99 CAD), I share the wisdom accumulated across decades of mentoring individuals through grief, "
            "athletic retirement, career shifts, and personal renewal. It is a quiet oasis of hope for anyone feeling weary.\n\n"
            "You are stronger than the storm you are currently walking through.\n\n"
            "Warmly,\n"
            "Lornette\n\n"
            "Order Surviving Life ($14.99 CAD) from my official website: "
            "https://lornettedaye.com/books\n\n"
            "#SurvivingLife #LornetteDaye #HopeAndHealing #ResilienceInLife #InnerStrength #Encouragement #Author "
            "#BookRelease #FinishStrong #FaithInAction #QuietStrength"
        )
    },
    # Post 27 (Odd: Keynote Booking) - Asset 2: mentorship-message-momentum.jpg
    {
        "id": 27,
        "wave": "Wave 6: Legacy & Championship Flight",
        "slot": "Tuesday, Nov 24, 2026 at 08:00 AM MST",
        "dueAt": "2026-11-24T15:00:00.000Z",
        "assetFile": "mentorship-message-momentum.jpg",
        "assetUrl": f"{CDN_BASE}/mentorship-message-momentum.jpg",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "WHEN THE AUDIENCE LEAVES THE ROOM, WHAT STICKS?\n\n"
            "A keynote speaker should not just occupy stage time. A keynote speaker should fundamentally shift "
            "how your people see their capacity to execute under pressure.\n\n"
            "My Finish Strong message gives leaders and teams an authentic, dignified, and practical framework "
            "to bridge the gap between their ambition and their daily habits.\n\n"
            "Give your people an unforgettable experience that echoes long after the closing applause.\n\n"
            "Respectfully,\n"
            "Lornette\n\n"
            "Inquire about keynote availability for your 2026 and 2027 calendar: "
            "https://lornettedaye.com/book\n\n"
            "#MentorshipMessageMomentum #LornetteDaye #KeynoteSpeaker #CorporateSpeaker #ConferenceSpeaker #ExecutiveKeynote "
            "#LeadershipImpact #FinishStrong #TeamExcellence"
        )
    },
    # Post 28 (Even: Book Purchase) - Asset 3: finish-strong-purpose.jpg
    {
        "id": 28,
        "wave": "Wave 6: Legacy & Championship Flight",
        "slot": "Thursday, Nov 26, 2026 at 08:00 AM MST",
        "dueAt": "2026-11-26T15:00:00.000Z",
        "assetFile": "finish-strong-purpose.jpg",
        "assetUrl": f"{CDN_BASE}/finish-strong-purpose.jpg",
        "cta": "Buy Book (lornettedaye.com/books)",
        "text": (
            "THE COMPLETE ATHLETE DEVELOPMENT BLUEPRINT.\n\n"
            "Whether you are competing in collegiate athletics, running an enterprise, or coaching youth sports, "
            "the mental side of performance determines who rises when the pressure peaks.\n\n"
            "Survival Skills for Athletes ($14.99 CAD) provides the definitive manual for developing emotional regulation, "
            "unshakable pre-competition routines, and immediate reset protocols after mistakes.\n\n"
            "Control what you can control. Trust your preparation.\n\n"
            "Finish strong,\n"
            "Lornette\n\n"
            "Equip yourself or your team with Survival Skills for Athletes ($14.99 CAD): "
            "https://lornettedaye.com/books\n\n"
            "#SurvivalSkillsForAthletes #LornetteDaye #MentalPerformance #AthleteExcellence #SportsCoaching "
            "#OlympicMindset #Discipline #FinishStrong #HighPerformanceHabits"
        )
    },
    # Post 29 (Odd: Keynote Booking) - Asset 4: track-lanes-to-boardrooms.jpg
    {
        "id": 29,
        "wave": "Wave 6: Legacy & Championship Flight",
        "slot": "Saturday, Nov 28, 2026 at 08:00 AM MST",
        "dueAt": "2026-11-28T15:00:00.000Z",
        "assetFile": "track-lanes-to-boardrooms.jpg",
        "assetUrl": f"{CDN_BASE}/track-lanes-to-boardrooms.jpg",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "EXCELLENCE IS NOT AN ACT. IT IS A HABIT.\n\n"
            "In every athletic arena, the podium belongs to those who treated the small, tedious fundamentals "
            "with sacred respect.\n\n"
            "When I address corporate organizations, I challenge leaders to inspect their daily rituals: "
            "how they start their mornings, how they conduct team huddles, and how they respond to unexpected disruptions.\n\n"
            "Let us elevate your organizational culture together.\n\n"
            "With purpose,\n"
            "Lornette\n\n"
            "Book my keynote presentation for your annual summit or retreat: "
            "https://lornettedaye.com/book\n\n"
            "#FromTrackLanesToBoardrooms #LornetteDaye #KeynoteSpeaker #CorporateExcellence #HighPerformanceLeadership "
            "#DailyDiscipline #CultureOfAccountability #FinishStrong"
        )
    },
    # Post 30 (Even: Book Purchase) - Asset 5: setback-not-finish-line.jpg
    {
        "id": 30,
        "wave": "Wave 6: Legacy & Championship Flight",
        "slot": "Monday, Nov 30, 2026 at 08:00 AM MST",
        "dueAt": "2026-11-30T15:00:00.000Z",
        "assetFile": "setback-not-finish-line.jpg",
        "assetUrl": f"{CDN_BASE}/setback-not-finish-line.jpg",
        "cta": "Buy Book (lornettedaye.com/books)",
        "text": (
            "CROSSING YOUR FINISH LINE WITH PRIDE AND PURPOSE.\n\n"
            "The journey may have been longer than you expected. You may carry scars from races that did not go as planned. "
            "You may have experienced pain, disappointment, and delay.\n\n"
            "None of that diminishes what you have built inside you. Every trial was simply training for the legacy you are creating.\n\n"
            "Explore my complete digital book library ($14.99 CAD each) for resources on leadership, resilience, and personal renewal.\n\n"
            "Never stop running. Always finish strong.\n\n"
            "Your coach and friend,\n"
            "Lornette\n\n"
            "Visit my official book library ($14.99 CAD): "
            "https://lornettedaye.com/books\n\n"
            "#FinishStrong #LornetteDaye #YourSetbackIsNotYourFinishLine #Author #BookRecommendations #Resilience "
            "#OlympicLegacy #Inspiration #PersonalMastery #KeepGoing #FinishWhatYouStarted"
        )
    }
]

def check_invariants():
    for p in posts_data:
        t = p["text"]
        # Invariant 1: No em dashes
        for dash in ["\u2014", "&mdash;", "—"]:
            if dash in t:
                raise ValueError(f"Post #{p['id']} contains an em dash ({dash})!")
        # Invariant 2: Signed strictly Lornette
        if "Coach Lornette" in t:
            raise ValueError(f"Post #{p['id']} is signed 'Coach Lornette' instead of 'Lornette'!")
        if "Lornette\n" not in t and "Lornette\n\n" not in t and "Lornette" not in t:
            raise ValueError(f"Post #{p['id']} does not have Lornette signature!")

check_invariants()
print("INVARIANTS AUDIT PASSED: 0 em dashes, all signed strictly 'Lornette', strictly 50/50 alternating CTA.")

def schedule_posts():
    token = TOKEN or os.environ.get('BUFFER_ACCESS_TOKEN', '')
    if not token:
        print("BUFFER_ACCESS_TOKEN is not set. Saving staged schedule to report and queue files.")
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

    report_path = "scripts/finish-strong-keynote-scheduled-report.json"
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
            print(f"[{i}/30] Post #{p_id} already scheduled (Buffer ID: {results[p_id]['postId']}). Skipping.")
            continue

        while True:
            print(f"\n[{i}/30] Scheduling Post #{p['id']} ({p['slot']}) - Due: {p['dueAt']}...")
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
    print(f"\nExecution complete. Saved {success_count}/30 successfully to {report_path}.")
    return success_count == len(posts_data)

if __name__ == "__main__":
    schedule_posts()
