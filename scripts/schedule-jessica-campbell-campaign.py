import os
import sys
import json
import urllib.request
import ssl
import time

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

TOKEN = os.environ.get('BUFFER_ACCESS_TOKEN', 'mLbjEsRdn5FKtGOskFoGzK-gW2CGTl8dfAK8klDVEPC')
CHANNEL_ID = '6a39d30c5ab6d2f1065f5301'  # Lornette Daye LinkedIn

CDN_BASE = 'https://lornettedaye.com/campaigns/jessica-campbell'

HASHTAGS = "#JessicaCampbell #SeattleKraken #NHL #WomenInSports #WomenInLeadership #Trailblazer #LeadDifferently #LornetteDaye #HighPerformance #BreakingBarriers #CoachingExcellence #HockeyCanada #OlympicCoach #ExecutiveMentorship #FinishStrong"

posts_data = [
    # =========================================================================
    # WEEK 1: SHATTERING CEILINGS & ESTABLISHING COMPETENCE (Sep 14 - Sep 20, 2026)
    # =========================================================================
    # DAY 1: Monday, Sep 14, 2026
    {
        "id": 1,
        "theme_arc": "Making NHL History",
        "slot": "Monday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-14T14:30:00.000Z",
        "displayTime": "Monday, Sep 14, 2026 - 8:30 AM MDT",
        "assetFile": "jessica-campbell-making-history-01.png",
        "assetUrl": f"{CDN_BASE}/jessica-campbell-making-history-01.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""MAKING NHL HISTORY: THE FIRST WOMAN BEHIND AN NHL BENCH. 🏒⚡👑

Jessica Campbell stepping behind the bench for the Seattle Kraken isn't just an unforgettable sports milestone—it is a masterclass in breaking barriers through unassailable competence.

In over 40 years of coaching Olympic athletes and advising high-performance leaders, I have seen barriers fall only when talent, tactical obsession, and mental fortitude collide.

Jessica did not arrive in the National Hockey League as a publicity statement. She arrived as one of the most respected skating and skill mechanics coaches in professional hockey—commanding the respect of NHL veterans across North America and Europe.

When you lead differently, you redefine what is possible for everyone watching.

Female Leaders & Executives: Are you waiting for permission to step behind your industry's bench, or are you preparing so thoroughly that your presence cannot be denied?

👉 Empower your corporate summit, athletic conference, or university leadership with an unforgettable keynote from Olympic Coach Lornette Daye on Breaking Barriers & Leading Differently: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 2,
        "theme_arc": "Saskatchewan Roots to the NHL",
        "slot": "Monday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-14T23:00:00.000Z",
        "displayTime": "Monday, Sep 14, 2026 - 5:00 PM MDT",
        "assetFile": "jessica-campbell-canadian-trailblazer-02.png",
        "assetUrl": f"{CDN_BASE}/jessica-campbell-canadian-trailblazer-02.png",
        "cta": "Survival Skills for Women (lornettedaye.com/books)",
        "text": f"""CANADIAN. COACH. TRAILBLAZER. FROM SASKATCHEWAN TO THE NHL. 🇨🇦❄️🏒

Rocanville, Saskatchewan has a population of around 1,000 people. Today, one of its daughters stands on the global stage as a pioneer in men's professional sport.

Trailblazing is rarely glamorous in its early chapters. It means sub-zero early mornings, endless highway miles, facing rooms where nobody looks like you, and having to prove your right to exist in the conversation every single day.

As a fellow Canadian woman who spent decades navigating the intense pressures of elite Olympic athletics, I recognize that look in Jessica's eyes:

It is the quiet, unbreakable resolve of a woman who knows her purpose is bigger than the doubt around her.

Monday Evening Reflection: What dream have you kept alive through seasons of isolation and resistance?

👉 Build your inner foundation of resilience, courage, and purpose. Read *Survival Skills for Women* by Lornette Daye ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },

    # DAY 2: Tuesday, Sep 15, 2026
    {
        "id": 3,
        "theme_arc": "Lead From The Bench",
        "slot": "Tuesday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-15T14:30:00.000Z",
        "displayTime": "Tuesday, Sep 15, 2026 - 8:30 AM MDT",
        "assetFile": "jessica-campbell-lead-from-bench-03.png",
        "assetUrl": f"{CDN_BASE}/jessica-campbell-lead-from-bench-03.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""LEAD FROM THE BENCH: COACHING CHANGES THE GAME. 📋⛸️🎯

Look at how Jessica Campbell commands the whiteboard. No hesitation. Clear technical communication. Laser focus on the execution detail.

In high-stakes sports—just like in Fortune 500 boardrooms—respect is not demanded through title or volume; it is commanded through precision. When players realize that your instruction will shave a tenth of a second off their transition or create a half-inch of separation in the offensive zone, all skepticism evaporates.

Competence creates belonging. Process creates progress.

How is your leadership team translating complex strategy into decisive execution under live fire?

👉 Book Lornette Daye for your executive retreat or sports administration seminar on High-Performance Coaching & Bench Leadership: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 4,
        "theme_arc": "The First Is Never Small",
        "slot": "Tuesday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-15T23:00:00.000Z",
        "displayTime": "Tuesday, Sep 15, 2026 - 5:00 PM MDT",
        "assetFile": "jessica-campbell-first-never-small-04.png",
        "assetUrl": f"{CDN_BASE}/jessica-campbell-first-never-small-04.png",
        "cta": "Survival Skills for Women (lornettedaye.com/books)",
        "text": f"""THE FIRST IS NEVER SMALL. 🌟🎙️⚓

When you are the first to walk through a historic doorway, you carry more than your clipboard—you carry the hopes and aspirations of millions of women who were told that certain rooms were closed to them.

Press conferences, media spotlights, and endless commentary can easily distract an ordinary coach. But Jessica carries herself with radiant poise, reminding us that being first is not about self-glorification—it is about keeping the door wedged open so the second, third, and fiftieth woman can sprint through after you.

More than hockey. More than a job. A more inclusive tomorrow.

Who is a trailblazing woman in your network who broke ground so others could rise? Tag them below!

👉 For women ready to step into leadership with confidence and grace. Order *Survival Skills for Women* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },

    # DAY 3: Wednesday, Sep 16, 2026
    {
        "id": 5,
        "theme_arc": "Work Before Recognition",
        "slot": "Wednesday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-16T14:30:00.000Z",
        "displayTime": "Wednesday, Sep 16, 2026 - 8:30 AM MDT",
        "assetFile": "jessica-campbell-prepared-moment-05.png",
        "assetUrl": f"{CDN_BASE}/jessica-campbell-prepared-moment-05.png",
        "cta": "Survival Skills for Athletes (lornettedaye.com/books)",
        "text": f"""PREPARED FOR THE MOMENT: WORK BEFORE RECOGNITION. 🏒📝⏳

The headlines celebrate the announcement. But history was won during the unseen reps.

Before the Seattle Kraken bench, there were years captaining Cornell, skating for Team Canada, coaching men in Germany's DEL, running power-skating development camps for NHL stars like Mat Barzal, and grinding behind the bench in Coachella Valley.

True authority is not granted by hiring committees. It is forged in the sweat, research, and technical mastery you cultivate when nobody is watching.

Discipline today creates brighter tomorrows.

Are you doing the unglamorous homework required to seize your breakthrough when your name is called?

👉 Master the mental discipline and daily habits of elite athletes. Read *Survival Skills for Athletes* by Lornette Daye ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 6,
        "theme_arc": "She Belongs Here",
        "slot": "Wednesday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-16T23:00:00.000Z",
        "displayTime": "Wednesday, Sep 16, 2026 - 5:00 PM MDT",
        "assetFile": "jessica-campbell-she-belongs-here-06.png",
        "assetUrl": f"{CDN_BASE}/jessica-campbell-she-belongs-here-06.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""SHE BELONGS HERE. LEADERSHIP HAS NO BOUNDARY. 🏔️🧢💪

Look at the command in her posture. Directing players, engaging the bench, demanding higher standards.

For decades, women in sports were told to stay in administrative roles or women's divisions. But hockey IQ, tactical vision, and emotional leadership do not carry a gender tag.

When women enter executive boardrooms, collegiate athletic director suites, or NHL benches, the conversation must shift permanently from 'Can she handle it?' to 'Watch how she elevates the entire room.'

She belongs here. And so do you.

Leaders: How is your organization creating pathways that judge talent purely on impact rather than tradition?

👉 Book Lornette Daye for your corporate keynote on Transforming Organizational Culture & Empowering Female Leadership: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 7: Thursday, Sep 17, 2026
    {
        "id": 7,
        "theme_arc": "The Mind Behind The Bench",
        "slot": "Thursday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-17T14:30:00.000Z",
        "displayTime": "Thursday, Sep 17, 2026 - 8:30 AM MDT",
        "assetFile": "jessica-campbell-mind-behind-bench-07.png",
        "assetUrl": f"{CDN_BASE}/jessica-campbell-mind-behind-bench-07.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""THE MIND BEHIND THE BENCH: VISION. DETAIL. LEADERSHIP. 🧠🏒🔍

NHL hockey moves at 30 miles per hour on razor-sharp steel. You don't have five minutes to deliberate a play—you have half a second.

Jessica Campbell's superpower is cognitive speed and tactical empathy. She breaks down complex edge-work and offensive-zone rotations into actionable, digestible cues that NHL athletes can execute instantly under immense physical pressure.

Detail better together. People, process, progress.

In your business or athletic program, does your leadership communicate with clarity or confusion during high-speed crisis moments?

👉 Bring Lornette Daye to train your leadership teams on High-Speed Cognitive Decision Making & Tactical Command: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 8,
        "theme_arc": "Quiet Confidence, Real Power",
        "slot": "Thursday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-17T23:00:00.000Z",
        "displayTime": "Thursday, Sep 17, 2026 - 5:00 PM MDT",
        "assetFile": "jessica-campbell-quiet-confidence-08.png",
        "assetUrl": f"{CDN_BASE}/jessica-campbell-quiet-confidence-08.png",
        "cta": "Survival Skills for Women (lornettedaye.com/books)",
        "text": f"""QUIET CONFIDENCE. REAL POWER. A NEW CHAPTER IN HOCKEY LEADERSHIP. 👑✨

Notice her smile alongside her steely focus. That is the signature of quiet confidence.

Weak leadership relies on intimidation, yelling, and posturing. True authority is calm. It is warm, composed, and utterly resolute. When you possess real mastery, you don't need to shout to be heard; your presence commands attention before you even speak.

To every woman navigating high-pressure corporate culture or competitive sports: Never let anyone convince you that kindness and composure are weaknesses. They are your greatest competitive advantages.

Lead differently. Inspire. Belong.

👉 Discover practical tools to lead with authenticity, resilience, and unshakeable inner power. Order *Survival Skills for Women* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },

    # DAY 5: Friday, Sep 18, 2026
    {
        "id": 9,
        "theme_arc": "Coaching Is Impact",
        "slot": "Friday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-18T14:30:00.000Z",
        "displayTime": "Friday, Sep 18, 2026 - 8:30 AM MDT",
        "assetFile": "jessica-campbell-coaching-is-impact-09.png",
        "assetUrl": f"{CDN_BASE}/jessica-campbell-coaching-is-impact-09.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""COACHING IS IMPACT: BEYOND THE MILESTONE. 🎯🤝💡

Better players. Brighter people.

At the highest level of professional sports, coaching is not about dictating drills. It is about understanding human psychology, unlocking individual potential, and getting elite performers to subordinate ego for the greater mission of the team.

Jessica Campbell's impact reaches far beyond the NHL standings. Every time she steps onto that ice, she models what the future of sports coaching looks like: holistic, high-standard, and deeply human-centric.

Friday Challenge: How are you investing in the human beings behind the job titles on your team?

👉 Schedule Olympic Coach Lornette Daye for your corporate keynote or athletic department symposium on Transformational Coaching: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 10,
        "theme_arc": "A Bench, A Barrier, A Breakthrough",
        "slot": "Friday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-18T23:00:00.000Z",
        "displayTime": "Friday, Sep 18, 2026 - 5:00 PM MDT",
        "assetFile": "jessica-campbell-barrier-breakthrough-10.png",
        "assetUrl": f"{CDN_BASE}/jessica-campbell-barrier-breakthrough-10.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": f"""A BENCH. A BARRIER. A BREAKTHROUGH. HISTORY OPENED. SHE WALKED THROUGH. 🚪💥🏒

The glass did not shatter by accident. It cracked under the relentless pressure of consistency, preparation, and courage.

For generations, women looked at NHL benches and saw an impenetrable wall. Today, Jessica Campbell stands on the other side of that wall, proving that when history finally opens a crack in the door, you must be ready to walk through with your head held high and your skates laced tight.

Barriers only hold until someone bold enough refuses to turn back.

What is the barrier standing between you and your breakthrough chapter right now?

👉 Fuel your courage to rise, fight through resistance, and achieve your highest goals. Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },

    # DAY 6: Saturday, Sep 19, 2026 (Weekend Showcase)
    {
        "id": 11,
        "theme_arc": "What Young Girls See",
        "slot": "Saturday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-19T14:30:00.000Z",
        "displayTime": "Saturday, Sep 19, 2026 - 8:30 AM MDT",
        "assetFile": "jessica-campbell-making-history-01.png",
        "assetUrl": f"{CDN_BASE}/jessica-campbell-making-history-01.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""SATURDAY MORNING RINKS: WHAT YOUNG GIRLS SEE TODAY. 👧🏒✨

Across Canada and the United States this Saturday morning, thousands of young girls are taping their sticks, tying their skates, and heading onto the ice.

For the first time in hockey history, when those girls watch NHL highlights tonight, they won't just see women in the stands or reporting from the concourse. They will see Jessica Campbell standing behind the bench in an NHL jacket, running the power play, and directing the world's best hockey players.

Representation is not a buzzword. It is the visual proof that your dreams are valid.

You cannot be what you cannot see—until someone is brave enough to be first.

👉 Inspire the next generation of female leaders and athletes. Book Lornette Daye for your school, athletic league, or corporate youth empowerment keynote: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 12,
        "theme_arc": "Canadian Pioneers",
        "slot": "Saturday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-19T23:00:00.000Z",
        "displayTime": "Saturday, Sep 19, 2026 - 5:00 PM MDT",
        "assetFile": "jessica-campbell-canadian-trailblazer-02.png",
        "assetUrl": f"{CDN_BASE}/jessica-campbell-canadian-trailblazer-02.png",
        "cta": "Survival Skills for Women (lornettedaye.com/books)",
        "text": f"""FROM ONE CANADIAN PIONEER TO ANOTHER: THE PRICE OF PAVING ROADS. 🍁🛤️

Paving roads is lonely, exhausting, and rarely appreciated until years later.

When I was competing and coaching on the international Olympic stage, there were few women in senior athletic leadership. You had to have thick skin, an iron stomach, and an unshakable commitment to excellence.

Watching Jessica Campbell carry the Canadian maple leaf into the NHL coaching fraternity fills my heart with immense pride. She is writing a playbook that will outlive all of us.

To every woman doing the hard, thankless work of paving a new road in her field: Keep swinging your hammer. You are building something historic.

👉 Rebuild your stamina and anchor your purpose when life demands everything from you. Order *Survival Skills for Women* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },

    # DAY 7: Sunday, Sep 20, 2026 (Reflection & Reset)
    {
        "id": 13,
        "theme_arc": "Command Without Shouting",
        "slot": "Sunday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-20T14:30:00.000Z",
        "displayTime": "Sunday, Sep 20, 2026 - 8:30 AM MDT",
        "assetFile": "jessica-campbell-lead-from-bench-03.png",
        "assetUrl": f"{CDN_BASE}/jessica-campbell-lead-from-bench-03.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""SUNDAY LEADERSHIP REFLECTION: COMMANDING RESPECT WITHOUT RAISING YOUR VOICE. 🤫⚡

There is a tired myth in sports and corporate executive culture that leadership requires shouting, pounding desks, and dominating the room through intimidation.

Watch Jessica Campbell behind that Seattle Kraken bench. Her authority is anchored in emotional composure, deep tactical knowledge, and mutual respect.

When an NHL veteran with 800 games of experience leans in closely to hear what she has to say, it isn't because she yelled at him. It's because he knows her insight will help him win.

Real power is quiet. Real authority is competent.

How are you cultivating quiet, unshakable authority in your leadership circles?

👉 Transform your organization's leadership culture. Book Lornette Daye for executive team workshops and keynote addresses: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 14,
        "theme_arc": "Standing Alone in the Arena",
        "slot": "Sunday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-20T23:00:00.000Z",
        "displayTime": "Sunday, Sep 20, 2026 - 5:00 PM MDT",
        "assetFile": "jessica-campbell-first-never-small-04.png",
        "assetUrl": f"{CDN_BASE}/jessica-campbell-first-never-small-04.png",
        "cta": "Survival Skills for Women (lornettedaye.com/books)",
        "text": f"""WEEK 1 IN REVIEW: THE COURAGE TO STAND ALONE IN THE ARENA. 🏟️✨🛡️

As we wrap up Week 1 of our Jessica Campbell tribute, let us sit with the sheer courage it takes to step onto an NHL rink as the only woman on the bench.

Every eye on you. Every decision scrutinized. Critics waiting for one mistake.

And yet, she smiles. She coaches. She stands tall.

If life or your career has called you into an arena where you feel alone and outnumbered: Do not retreat. Stand your ground. Your preparation brought you here, and your resilience will carry you through.

A brighter tomorrow always wins.

👉 Equip yourself or the women in your circle with tools for unshakeable confidence. Get *Survival Skills for Women* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },

    # =========================================================================
    # WEEK 2: HIGH-PERFORMANCE CULTURE & SUSTAINED LEGACY (Sep 21 - Sep 27, 2026)
    # =========================================================================
    # DAY 8: Monday, Sep 21, 2026
    {
        "id": 15,
        "theme_arc": "Competence as the Equalizer",
        "slot": "Monday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-21T14:30:00.000Z",
        "displayTime": "Monday, Sep 21, 2026 - 8:30 AM MDT",
        "assetFile": "jessica-campbell-prepared-moment-05.png",
        "assetUrl": f"{CDN_BASE}/jessica-campbell-prepared-moment-05.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""WEEK 2 KICKOFF: WHY COMPETENCE IS THE ULTIMATE EQUALIZER. 📈🏒👑

Skepticism only survives where competence is absent.

When Jessica Campbell entered the Coachella Valley AHL locker room and subsequently the Seattle Kraken bench, any initial doubt evaporated within minutes of the first skating session. Why? Because her technical breakdown of edge mechanics and power skating was superior to anything those players had encountered.

In any male-dominated industry—whether technology, finance, or sports—competence is the great equalizer. When you bring elite skill to the table, prejudices have no ground left to stand on.

Lead with competence. Let your work dismantle the skeptics.

👉 Inspire your company to build a culture where performance and merit reign supreme. Book Olympic Coach Lornette Daye for your corporate keynote: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 16,
        "theme_arc": "Redefining the Room",
        "slot": "Monday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-21T23:00:00.000Z",
        "displayTime": "Monday, Sep 21, 2026 - 5:00 PM MDT",
        "assetFile": "jessica-campbell-she-belongs-here-06.png",
        "assetUrl": f"{CDN_BASE}/jessica-campbell-she-belongs-here-06.png",
        "cta": "Survival Skills for Women (lornettedaye.com/books)",
        "text": f"""REDEFINING THE ROOM: WHEN LEADERSHIP STOPS ASKING PERMISSION. 🚪💫

For generations, women were conditioned to wait for someone to invite them into the room.

Jessica Campbell did not wait for an invitation. She coached, studied, earned credentials, took high-risk positions in European men's leagues, and built a reputation that made her impossible to ignore.

When you walk into a room where you are the first or the only: Do not shrink. Do not apologize for taking up space. Do not alter your authentic self to fit someone else's narrow tradition.

You belong in every room your preparation brought you to.

Monday Night Truth: What room are you ready to redefine this week?

👉 Step into your power, resilience, and purpose. Read *Survival Skills for Women* by Lornette Daye ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },

    # DAY 9: Tuesday, Sep 22, 2026
    {
        "id": 17,
        "theme_arc": "Precision in the Details",
        "slot": "Tuesday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-22T14:30:00.000Z",
        "displayTime": "Tuesday, Sep 22, 2026 - 8:30 AM MDT",
        "assetFile": "jessica-campbell-mind-behind-bench-07.png",
        "assetUrl": f"{CDN_BASE}/jessica-campbell-mind-behind-bench-07.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""PRECISION IN THE DETAILS: HOW ELITE COACHES EARN TRUST. 🔍🎯🏒

In professional sports, veteran athletes have seen it all. They can spot a coach who is faking knowledge from 50 feet away.

Jessica Campbell earned immediate buy-in from multi-million-dollar NHL players because of her obsessive attention to micro-details: hip angle on crossovers, weight distribution on zone entries, and release timing on one-timers.

Trust is not built with grand speeches. Trust is built in the micro-adjustments that make your people demonstrably better.

How are you proving to your team that you care about the details of their success?

👉 Elevate your leadership precision and team performance. Book Lornette Daye for your keynote conference or athletic seminar: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 18,
        "theme_arc": "Composure Under Pressure",
        "slot": "Tuesday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-22T23:00:00.000Z",
        "displayTime": "Tuesday, Sep 22, 2026 - 5:00 PM MDT",
        "assetFile": "jessica-campbell-quiet-confidence-08.png",
        "assetUrl": f"{CDN_BASE}/jessica-campbell-quiet-confidence-08.png",
        "cta": "Survival Skills for Athletes (lornettedaye.com/books)",
        "text": f"""THE POWER OF COMPOSURE IN HOSTILE ENVIRONMENTS. ❄️🧊⚡

When you coach in visiting NHL arenas, 18,000 hostile fans want nothing more than to see you fail. Cameras zoom in on your every expression. Pundits analyze every line change.

How do you survive that kind of pressure cooker?

You cultivate an internal fortress. You lock your focus entirely on what you can control—your communication, your strategy, and your emotional stability.

When the bench gets chaotic, the coach must be the thermostat, not the thermometer. Set the temperature; don't reflect the panic.

How do you maintain your center when the environment around you is in turmoil?

👉 Learn the mental resilience protocols of Olympic champions. Read *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },

    # DAY 10: Wednesday, Sep 23, 2026
    {
        "id": 19,
        "theme_arc": "Mentorship in Motion",
        "slot": "Wednesday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-23T14:30:00.000Z",
        "displayTime": "Wednesday, Sep 23, 2026 - 8:30 AM MDT",
        "assetFile": "jessica-campbell-coaching-is-impact-09.png",
        "assetUrl": f"{CDN_BASE}/jessica-campbell-coaching-is-impact-09.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""MENTORSHIP IN MOTION: BUILDING A BRIDGE FOR THE NEXT GENERATION. 🌉🤝💡

Behind every trailblazer stands someone who had the courage to advocate for them. In Jessica Campbell's journey, Dan Bylsma saw her brilliance and brought her onto his staff in Coachella Valley and then Seattle.

And in front of every trailblazer walks the responsibility to pull the next generation forward.

Mentorship is not a passive coffee meeting; it is putting your organizational capital on the line to open doors for deserving, high-caliber talent that traditional systems overlook.

Who are you championing in your organization today who has the skill but lacks the platform?

👉 Build an intentional culture of transformative mentorship and inclusion. Book Lornette Daye for your corporate summit: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 20,
        "theme_arc": "Turning Barriers into Stepping Stones",
        "slot": "Wednesday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-23T23:00:00.000Z",
        "displayTime": "Wednesday, Sep 23, 2026 - 5:00 PM MDT",
        "assetFile": "jessica-campbell-barrier-breakthrough-10.png",
        "assetUrl": f"{CDN_BASE}/jessica-campbell-barrier-breakthrough-10.png",
        "cta": "Survival Skills for Women (lornettedaye.com/books)",
        "text": f"""TURNING BARRIERS INTO STEPPING STONES. 🧱🧗‍♀️✨

A barrier is only a wall if you choose to stop walking. If you keep moving forward, that barrier becomes a stepping stone that elevates your perspective above the crowd.

Jessica Campbell encountered barriers at every stage of her hockey journey: when women's playing opportunities were limited, when men's pro coaching roles were considered off-limits, and when skeptics questioned whether men would listen to a woman.

She turned every single barrier into proof of her endurance.

To every woman facing a closed door tonight: That door is not your destination. It is the resistance training that is forging your resilience.

Keep going. Brighter tomorrows are waiting.

👉 Reclaim your strength and discover purpose through hardship. Order *Survival Skills for Women* by Lornette Daye ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },

    # DAY 11: Thursday, Sep 24, 2026
    {
        "id": 21,
        "theme_arc": "The Multiplier Effect",
        "slot": "Thursday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-24T14:30:00.000Z",
        "displayTime": "Thursday, Sep 24, 2026 - 8:30 AM MDT",
        "assetFile": "jessica-campbell-making-history-01.png",
        "assetUrl": f"{CDN_BASE}/jessica-campbell-making-history-01.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""THE MULTIPLIER EFFECT: WHEN ONE WOMAN ADVANCES, AN ECOSYSTEM SHIFTS. 🌍⚡👑

When Jessica Campbell was hired by the Seattle Kraken, the headline was about one woman.

But the ripple effect touched every level of hockey: youth leagues saw spikes in female registration, NCAA programs saw increased coaching interest, and NHL general managers were forced to reconsider how they source coaching talent.

That is the multiplier effect of trailblazing leadership. Your breakthrough is never just about you—it creates economic, cultural, and psychological opportunities for people you may never meet.

What standard are you setting today that will multiply impact for those who follow you?

👉 Book Olympic Coach Lornette Daye for your corporate keynote on Exponential Leadership & Systemic Change: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 22,
        "theme_arc": "Canadian Tenacity & Grit",
        "slot": "Thursday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-24T23:00:00.000Z",
        "displayTime": "Thursday, Sep 24, 2026 - 5:00 PM MDT",
        "assetFile": "jessica-campbell-canadian-trailblazer-02.png",
        "assetUrl": f"{CDN_BASE}/jessica-campbell-canadian-trailblazer-02.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": f"""CANADIAN TENACITY: THE GRIT REQUIRED TO REDRAW SPORTS HISTORY. 🇨🇦🏒🏔️

There is a distinct resilience born on Canadian prairie ice. When the wind chill is -35 and the outdoor rinks freeze over, you don't complain about the cold—you skate harder to stay warm.

That prairie work ethic is what carries Jessica Campbell behind an NHL bench, and it is the same spirit that fueled my four decades of Olympic athletics.

You cannot fake grit. You cannot buy resilience with venture capital. It must be forged through repeated encounters with difficulty and the refusal to quit.

Where in your life do you need to tap into your deepest grit right now?

👉 Discover the Olympic blueprint for rising again after crushing setbacks. Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },

    # DAY 12: Friday, Sep 25, 2026
    {
        "id": 23,
        "theme_arc": "Earning Locker Room Respect",
        "slot": "Friday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-25T14:30:00.000Z",
        "displayTime": "Friday, Sep 25, 2026 - 8:30 AM MDT",
        "assetFile": "jessica-campbell-lead-from-bench-03.png",
        "assetUrl": f"{CDN_BASE}/jessica-campbell-lead-from-bench-03.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""EARNING LOCKER ROOM RESPECT: THE DAILY RIGOR OF HIGH PERFORMANCE. 🤝🏒🛡️

A professional sports locker room is one of the most demanding social environments on Earth. It has no tolerance for pretense or superficial slogans.

Jessica Campbell didn't win over Kraken players by talking about history. She won them over by showing up first, having video breakdowns queued up before they walked off the ice, and providing individual feedback that made them sharper competitors.

Respect in high-performance organizations is currency earned in pennies and spent in dollars. You earn it through daily rigor.

How are you earning the respect of your colleagues and direct reports today?

👉 Connect with Lornette Daye for executive team culture workshops and keynote presentations: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 24,
        "theme_arc": "Owning Your Space",
        "slot": "Friday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-25T23:00:00.000Z",
        "displayTime": "Friday, Sep 25, 2026 - 5:00 PM MDT",
        "assetFile": "jessica-campbell-first-never-small-04.png",
        "assetUrl": f"{CDN_BASE}/jessica-campbell-first-never-small-04.png",
        "cta": "Survival Skills for Women (lornettedaye.com/books)",
        "text": f"""OWNING YOUR SPACE WITHOUT ASKING FOR PERMISSION. 🎙️👑✨

When you step up to the podium or into the executive boardroom, do not look around to see if everyone approves of your presence.

Look straight ahead, speak your truth with clarity, and own your space.

Jessica Campbell's journey reminds women everywhere that humility does not mean making yourself small. You can be deeply humble before God and the craft while standing completely upright in your authority.

Friday Evening Reminder: You were created with unique brilliance, purpose, and capability. Do not shrink to make small minds comfortable.

A brighter tomorrow always wins.

👉 Empower your journey with timeless wisdom, courage, and hope. Order *Survival Skills for Women* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },

    # DAY 13: Saturday, Sep 26, 2026
    {
        "id": 25,
        "theme_arc": "Demanding More of Yourself",
        "slot": "Saturday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-26T14:30:00.000Z",
        "displayTime": "Saturday, Sep 26, 2026 - 8:30 AM MDT",
        "assetFile": "jessica-campbell-prepared-moment-05.png",
        "assetUrl": f"{CDN_BASE}/jessica-campbell-prepared-moment-05.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""SATURDAY GAME MINDSET: DEMANDING MORE OF YOURSELF THAN ANYONE ELSE CAN ASK. 🏒🔥

When you coach at the pinnacle of sports, the scrutiny is endless. But the real pressure never comes from outside critics—it comes from your own commitment to the standard.

Jessica Campbell works with the intensity of someone who knows that every single detail on the ice matters. When a coach holds herself to that standard, the players have no choice but to elevate their game to match it.

Culture is contagious. High standards are infectious.

What standard are you bringing to your craft today?

👉 Elevate your corporate or sports conference with a keynote on High-Standard Leadership from Olympic Coach Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 26,
        "theme_arc": "Normalizing Greatness",
        "slot": "Saturday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-26T23:00:00.000Z",
        "displayTime": "Saturday, Sep 26, 2026 - 5:00 PM MDT",
        "assetFile": "jessica-campbell-she-belongs-here-06.png",
        "assetUrl": f"{CDN_BASE}/jessica-campbell-she-belongs-here-06.png",
        "cta": "Survival Skills for Women (lornettedaye.com/books)",
        "text": f"""NORMALIZING GREATNESS: MOVING BEYOND 'FIRST WOMAN' TO 'ELITE COACH'. 🏒🌟💡

The milestone was historic. But the ultimate goal of trailblazing is to make what was once extraordinary feel completely normal.

The day is coming soon when a woman on an NHL, NBA, or NFL sideline will draw zero headlines—not because it isn't impressive, but because competence has completely eliminated surprise.

Jessica Campbell is doing the heavy lifting right now so that the next generation of female coaches can simply be judged as elite hockey minds.

That is the true definition of legacy.

👉 Learn how to navigate transition, build resilience, and leave an enduring legacy. Read *Survival Skills for Women* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },

    # DAY 14: Sunday, Sep 27, 2026 (Grand Finale)
    {
        "id": 27,
        "theme_arc": "The Enduring Standard",
        "slot": "Sunday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-27T14:30:00.000Z",
        "displayTime": "Sunday, Sep 27, 2026 - 8:30 AM MDT",
        "assetFile": "jessica-campbell-mind-behind-bench-07.png",
        "assetUrl": f"{CDN_BASE}/jessica-campbell-mind-behind-bench-07.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""THE ENDURING STANDARD: LESSONS FROM 4 DECADES OF OLYMPIC COACHING. 🏅⛸️📜

As we draw toward the conclusion of our Jessica Campbell tribute series, I reflect on my 40+ years in elite international athletics:

Fads come and go. Marketing slogans fade. Headlines rotate daily.

What endures through decades of high-stakes pressure is substance: the relentless pursuit of mastery, unconditional care for the people you lead, and the humility to keep learning every day.

Jessica Campbell embodies those timeless values. She leads differently—and that is why she is changing the game forever.

👉 Bring Lornette Daye's four decades of championship wisdom to your organization's next major event: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 28,
        "theme_arc": "The Legacy of Trailblazers",
        "slot": "Sunday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-27T23:00:00.000Z",
        "displayTime": "Sunday, Sep 27, 2026 - 5:00 PM MDT",
        "assetFile": "jessica-campbell-barrier-breakthrough-10.png",
        "assetUrl": f"{CDN_BASE}/jessica-campbell-barrier-breakthrough-10.png",
        "cta": "Speaking & Complete Catalog (lornettedaye.com/speaking)",
        "text": f"""GRAND FINALE: THE LEGACY OF TRAILBLAZERS — KEEP GOING UNTIL THE BARRIER BREAKS. 🏔️🚪✨🏒

A bench. A barrier. A breakthrough.

Jessica Campbell stepped onto the ice in Seattle and proved what is possible when female competence meets opportunity and courage.

To every woman reading this who has ever felt overlooked, doubted, or told that your ambition was too big for your hometown: Look at Jessica. Look at what can happen when you refuse to surrender your dream.

Keep sharpening your edges. Keep studying the game. Keep standing tall.

Your breakthrough is closer than you think. Finish strong.

👉 Book Lornette Daye for Keynote Speaking: lornettedaye.com/speaking
👉 Explore the Official Digital Book Catalog (*Survival Skills for Women*, *Survival Skills for Athletes*, *Finish Strong*, $14.99 CAD each): lornettedaye.com/books

#JessicaCampbell #SeattleKraken #NHL #WomenInSports #WomenInLeadership #Trailblazer #LeadDifferently #LornetteDaye #HighPerformance #BreakingBarriers #CoachingExcellence #HockeyCanada #OlympicCoach #FinishStrong"""
    }
]

def check_media_head(url):
    ctx = ssl._create_unverified_context()
    req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            return resp.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:
        return str(e)

def buffer_request(query, variables):
    ctx = ssl._create_unverified_context()
    payload = json.dumps({"query": query, "variables": variables}).encode('utf-8')
    req = urllib.request.Request(
        "https://api.buffer.com",
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {TOKEN}",
            "User-Agent": "Mozilla/5.0"
        }
    )
    with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
        body = json.loads(resp.read().decode('utf-8'))
        if "errors" in body:
            print(f"   ❌ GraphQL Errors: {body['errors']}")
        return body.get("data", {})

mutation = """
mutation CreatePost($input: CreatePostInput!) {
    createPost(input: $input) {
        __typename
        ... on PostActionSuccess {
            post {
                id
                dueAt
                status
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

def main():
    print("==================================================================")
    print("🏒 LORNETTE DAYE - 2-WEEK JESSICA CAMPBELL NHL CAMPAIGN SCHEDULER")
    print(f"Target Channel: {CHANNEL_ID} (LinkedIn)")
    print(f"Total Posts to Schedule: {len(posts_data)}")
    print("==================================================================\n")

    # 1. Pre-flight CDN Media Probe
    print("🔍 [Pre-Flight Invariant] Probing Media Assets on lornettedaye.com...")
    all_media_urls = list(set([p["assetUrl"] for p in posts_data]))
    all_ok = True
    for url in sorted(all_media_urls):
        status = check_media_head(url)
        if status == 200:
            print(f"   ✅ [200 OK] {url}")
        else:
            print(f"   ❌ [{status}] {url}")
            all_ok = False

    if not all_ok:
        print("\n❌ HARD INVARIANT VIOLATION: Some media assets returned non-200. Halting Buffer scheduling.")
        sys.exit(1)

    print("\n✅ All production visual assets verified 200 OK! Proceeding to Buffer scheduling...\n")

    results = []

    for i, p in enumerate(posts_data, start=1):
        print(f"[{i}/{len(posts_data)}] Scheduling: {p['slot']} - {p['theme_arc']}")
        print(f"   Due At: {p['dueAt']} ({p['displayTime']})")
        print(f"   Asset:  {p['assetFile']}")
        print(f"   CTA:    {p['cta']}")

        asset_payload = [{"image": {"url": p["assetUrl"]}}]

        input_data = {
            "channelId": CHANNEL_ID,
            "text": p["text"],
            "mode": "customScheduled",
            "dueAt": p["dueAt"],
            "schedulingType": "automatic",
            "needsApproval": False,
            "saveToDraft": False,
            "assets": asset_payload
        }

        try:
            data = buffer_request(mutation, {"input": input_data})
            create_post = data.get("createPost", {})
            typename = create_post.get("__typename")

            if typename == "PostActionSuccess" and "post" in create_post:
                post_obj = create_post["post"]
                print(f"   ✅ Success! Buffer Post ID: {post_obj['id']} | Due: {post_obj['dueAt']}\n")
                p["bufferPostId"] = post_obj["id"]
                p["status"] = "scheduled"
                p["scheduledAt"] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
                results.append(p)
            elif typename == "LimitReachedError":
                msg = create_post.get("message", "Rate limit reached")
                print(f"   ⚠️ Limit reached: {msg}\n")
                p["status"] = "limit_reached"
                p["error"] = msg
                results.append(p)
            else:
                print(f"   ⚠️ Failed response: {json.dumps(create_post, indent=2)}\n")
                p["status"] = "failed"
                p["error"] = create_post
                results.append(p)
        except Exception as e:
            print(f"   ❌ Exception: {e}\n")
            p["status"] = "error"
            p["error"] = str(e)
            results.append(p)

        time.sleep(1.0)

    report_path = os.path.join(os.path.dirname(__file__), "jessica-campbell-scheduled-report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("------------------------------------------------------")
    print(f"🎉 Jessica Campbell Campaign Report saved to {report_path}")
    successful = sum(1 for r in results if r.get("status") == "scheduled")
    print(f"Summary: {successful}/{len(posts_data)} posts scheduled in Buffer Scheduled Queue.")
    print("------------------------------------------------------")

if __name__ == "__main__":
    main()
