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

CDN_BASE = 'https://lornettedaye.com/campaigns/colorado-buffs'

HASHTAGS = "#CUBuffs #ColoradoFootball #CoachPrime #JulianLewis #WeKeepReceipts #SkoBuffs #FolsomField #CollegeFootball #Big12 #LeadershipExcellence #ChampionMindset #LornetteDaye #AthleticDirector #KeynoteSpeaker #SportsLeadership"

posts_data = [
    # =========================================================================
    # WEEK 1: STATEMENT & IDENTITY BUILDING (Sep 14 - Sep 20, 2026)
    # =========================================================================
    # DAY 1: Monday, Sep 14, 2026
    {
        "id": 1,
        "theme_arc": "The Statement Game",
        "slot": "Monday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-14T14:30:00.000Z",
        "displayTime": "Monday, Sep 14, 2026 - 8:30 AM MDT",
        "assetFile": "colorado-buffs-statement-01.png",
        "assetUrl": f"{CDN_BASE}/colorado-buffs-statement-01.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""THE BUFFS DIDN'T JUST WIN, THEY MADE A STATEMENT. 🦬🏈🔥

Colorado 52 • Weber State 21. Five total touchdowns from Julian Lewis. Colorado sits at 2-0.

In over 40 years of mentoring elite Olympians and national championship contenders, I've learned that some wins merely settle a score, while other wins tell you what a team genuinely believes about itself.

When an offense executes with that level of surgical aggression, it isn't accidental. It represents months of disciplined preparation, shared accountability, and an uncompromising internal standard.

As an executive, athletic director, or head coach: Is your organization just trying to get through the week, or are you stepping into the arena to make a statement?

👉 Bring champion-level culture and high-stakes execution to your athletic program or leadership conference. Book Olympic Coach Lornette Daye for your keynote address: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 2,
        "theme_arc": "Belief Becoming Identity",
        "slot": "Monday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-14T23:00:00.000Z",
        "displayTime": "Monday, Sep 14, 2026 - 5:00 PM MDT",
        "assetFile": "colorado-buffs-identity-02.png",
        "assetUrl": f"{CDN_BASE}/colorado-buffs-identity-02.png",
        "cta": "Speaking & Books (lornettedaye.com/speaking)",
        "text": f"""COLORADO IS 2-0. SOME TEAMS SURVIVE. SOME TEAMS ANNOUNCE THEMSELVES. ⚡🏔️

578 total yards of offense. Complete command from the opening whistle to the final horn at Folsom Field.

You can feel the exact moment when belief stops being a slogan on a locker room wall and starts becoming a team's undeniable identity. When players look each other in the eyes and know—without hesitation—that their preparation will outlast anyone across the line of scrimmage.

Belief builds different. It alters how you walk, how you practice, and how you respond when the spotlight burns hottest.

Sports Leaders: What is the defining identity your athletes carry onto the field each Saturday?

👉 Equip your coaches, student-athletes, and executive teams with the psychological blueprint to turn belief into sustainable excellence. Book Lornette Daye for keynote speaking & leadership seminars: lornettedaye.com/speaking (Explore *Survival Skills for Athletes* at lornettedaye.com/books)

{HASHTAGS}"""
    },

    # DAY 2: Tuesday, Sep 15, 2026
    {
        "id": 3,
        "theme_arc": "Julian Lewis Composure",
        "slot": "Tuesday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-15T14:30:00.000Z",
        "displayTime": "Tuesday, Sep 15, 2026 - 8:30 AM MDT",
        "assetFile": "colorado-buffs-julian-ready-03.png",
        "assetUrl": f"{CDN_BASE}/colorado-buffs-julian-ready-03.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""JULIAN LEWIS LOOKED READY FOR THIS. 🎯🏈✨

17 of 23 passing. 366 yards through the air. 4 passing touchdowns, 5 total TDs. But more impressive than the stat line was the unshakeable calm in his eyes.

Sometimes a young athlete doesn't arrive quietly—he arrives prepared.

When you see a young quarterback command the pocket with that kind of emotional maturity, you aren't just witnessing raw arm talent; you're seeing thousands of unseen hours of film breakdown, footwork drills, and mental reps bearing fruit under live fire.

Preparation builds confidence. Confidence creates opportunity. Discipline today creates brighter tomorrows.

How are you preparing your young leaders to step into pressure without flinching?

👉 Transform your program's leadership pipeline. Book Lornette Daye for your university or corporate keynote: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 4,
        "theme_arc": "Folsom Field Voltage",
        "slot": "Tuesday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-15T23:00:00.000Z",
        "displayTime": "Tuesday, Sep 15, 2026 - 5:00 PM MDT",
        "assetFile": "colorado-buffs-folsom-belief-04.png",
        "assetUrl": f"{CDN_BASE}/colorado-buffs-folsom-belief-04.png",
        "cta": "Executive Culture & Keynotes (lornettedaye.com/speaking)",
        "text": f"""FOLSOM FELT THE BELIEF. 🏟️🏔️💛

42-14 at halftime. Colorado never let their foot off the gas.

When a team starts to truly believe in its system, the whole stadium knows it. Energy changes dramatically when players, coaches, and 50,000 screaming fans all feel the exact same heartbeat simultaneously.

That kind of collective voltage cannot be bought, manufactured with PR campaigns, or faked on social media. It is built in the dirt, forged through mutual sacrifice, and sustained through relentless brotherhood.

Culture is not what you preach; it is what your entire organization vibrates with under pressure.

👉 Want to build an electric, unified organizational culture that wins consistently? Connect with Lornette Daye for keynote speaking and culture transformation: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 3: Wednesday, Sep 16, 2026
    {
        "id": 5,
        "theme_arc": "52 Points & Imposing the Standard",
        "slot": "Wednesday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-16T14:30:00.000Z",
        "displayTime": "Wednesday, Sep 16, 2026 - 8:30 AM MDT",
        "assetFile": "colorado-buffs-52-points-05.png",
        "assetUrl": f"{CDN_BASE}/colorado-buffs-52-points-05.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""52 POINTS. ONE CLEAR MESSAGE. 💥📊

Colorado didn't just win on Saturday. Colorado imposed itself.

There are routine victories that fade from memory by Sunday morning, and then there are performances that permanently alter the temperature around an entire athletic program. Putting up 578 yards of offense is more than just executing a playbook—it is demanding that the world respect your standard.

In elite sport and executive business alike, you will never rise higher than the standards you enforce on your average days.

Are your teams setting the tempo, or are they waiting to see what the opposition will allow?

👉 Elevate your department to championship-tier execution. Book Lornette Daye for your next conference or university keynote: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 6,
        "theme_arc": "Growing Up Fast",
        "slot": "Wednesday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-16T23:00:00.000Z",
        "displayTime": "Wednesday, Sep 16, 2026 - 5:00 PM MDT",
        "assetFile": "colorado-buffs-growing-fast-06.png",
        "assetUrl": f"{CDN_BASE}/colorado-buffs-growing-fast-06.png",
        "cta": "Speaking & Student Literature (lornettedaye.com/speaking)",
        "text": f"""THIS LOOKS LIKE A TEAM GROWING UP FAST. 🚀🏈🌱

The confidence looked different. The execution did too. Explosive plays balanced by extraordinary poise across four quarters.

Rapid athletic development becomes visible the moment raw talent decides to play with pure conviction. When young players stop second-guessing their assignments and start trusting their training, speed unlocks.

In collegiate athletics, you don't have three years to wait for maturity to happen organically. Great coaching bridges the gap between raw potential and champion poise right now.

Coaches & Mentors: What environment are you providing to accelerate maturity in your young roster?

👉 Accelerate your athletes' mental maturity and life resilience. Keynote speaking: lornettedaye.com/speaking | Author of *Survival Skills for Students* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },

    # DAY 4: Thursday, Sep 17, 2026
    {
        "id": 7,
        "theme_arc": "Fast Start & Accountability",
        "slot": "Thursday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-17T14:30:00.000Z",
        "displayTime": "Thursday, Sep 17, 2026 - 8:30 AM MDT",
        "assetFile": "colorado-buffs-standard-07.png",
        "assetUrl": f"{CDN_BASE}/colorado-buffs-standard-07.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""THE STANDARD LOOKED DIFFERENT TODAY. ⏱️⚡

Fast start. Real command. Mature response. Three offensive plays from scrimmage was all it took for Colorado to go up 14-0.

Anyone can look good when everything is going their way in the fourth quarter. But what separates championship contenders is the intentionality of how they come out of the locker room in minute one.

Sometimes the scoreboard is impressive, but the standard behind it is what stays with you. Accountability isn't a lecture; it's a relentless daily habit.

Are your leaders prepared to strike first and establish their authority from the first snap?

👉 Bring Lornette Daye's 40+ years of high-performance wisdom to your organization. Book a keynote speaking session today: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 8,
        "theme_arc": "Turning Points Revealed",
        "slot": "Thursday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-17T23:00:00.000Z",
        "displayTime": "Thursday, Sep 17, 2026 - 5:00 PM MDT",
        "assetFile": "colorado-buffs-turning-point-08.png",
        "assetUrl": f"{CDN_BASE}/colorado-buffs-turning-point-08.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""SOMETIMES A WIN FEELS LIKE A TURNING POINT. 🔄🏔️🏆

Not because of the score alone—because of what it reveals under the surface.

Julian Lewis led the way, but the most profound story was how the entire sideline responded. The offensive line protecting their freshman signal-caller with ferocious brotherhood. The defense flying to the football. The special teams executing assignments with clinical discipline.

You watch closely enough through four decades of elite sport, and you can tell when an afternoon means far more than just one game on a calendar.

It marks the turning of a program's culture toward sustained excellence.

👉 Prepare your leadership team to recognize and seize your organization's turning points. Book Lornette Daye for your corporate summit or athletic convention: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 5: Friday, Sep 18, 2026
    {
        "id": 9,
        "theme_arc": "Talent Meets Conviction",
        "slot": "Friday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-18T14:30:00.000Z",
        "displayTime": "Friday, Sep 18, 2026 - 8:30 AM MDT",
        "assetFile": "colorado-buffs-conviction-09.png",
        "assetUrl": f"{CDN_BASE}/colorado-buffs-conviction-09.png",
        "cta": "Speaking & Literature (lornettedaye.com/speaking)",
        "text": f"""WHEN TALENT MEETS CONVICTION. 🧠💪🔥

That is when performances begin to carry weight.

Julian Lewis and the Colorado Buffaloes made the moment feel bigger on Saturday because they played with absolute, unshakeable conviction.

Skill opens the door. Talent gets you invited into the building. But conviction? Conviction is what changes the temperature of the room. It is the refusal to accept mediocrity even when you are already winning by four touchdowns.

Friday Question: In your life and career, are you relying purely on natural talent, or are you operating with ferocious conviction?

👉 Inspire your coaches, athletes, and executive teams to lead with champion conviction. Book Olympic Coach Lornette Daye for your keynote address: lornettedaye.com/speaking (Check out *Survival Skills for Athletes* at lornettedaye.com/books)

{HASHTAGS}"""
    },
    {
        "id": 10,
        "theme_arc": "The Future Arrived in Boulder",
        "slot": "Friday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-18T23:00:00.000Z",
        "displayTime": "Friday, Sep 18, 2026 - 5:00 PM MDT",
        "assetFile": "colorado-buffs-future-boulder-10.png",
        "assetUrl": f"{CDN_BASE}/colorado-buffs-future-boulder-10.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""THE FUTURE ARRIVED IN BOULDER. 🏔️✨🦬

Young leadership. Big response. A program vibrating with authentic, electric energy.

A 2-0 start and a quarterback performance that Folsom Field will remember for years to come. The future feels fundamentally different when it stops sounding like abstract potential on recruiting boards and starts looking like undeniable reality on game day.

When leadership provides young athletes with clear guardrails, high standards, and unwavering belief, the impossible becomes routine.

Tomorrow is game day across college football. Are your leaders ready to show what the future looks like?

👉 Book Lornette Daye for keynote speaking on cultivating next-generation champions and resilient leaders: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 6: Saturday, Sep 19, 2026 (Game Day)
    {
        "id": 11,
        "theme_arc": "Game Day Saturday Standard",
        "slot": "Saturday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-19T14:30:00.000Z",
        "displayTime": "Saturday, Sep 19, 2026 - 8:30 AM MDT",
        "assetFile": "colorado-buffs-statement-01.png",
        "assetUrl": f"{CDN_BASE}/colorado-buffs-statement-01.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""GAME DAY SATURDAY: THE STANDARD DOES NOT NEGOTIATE. 🏈⚔️💥

It's kickoff morning across college football. The pads are strapped, the stands are filling, and the noise is deafening.

Remember what the Buffs proved in their 52-21 statement: You don't win on Saturday afternoon. You win on Tuesday morning during pass-protection film study. You win on Thursday afternoon during red-zone walkthroughs when your legs are burning.

Saturday is simply the public receipt of your private discipline.

Go out there today and make your own statement—on the turf, in the boardroom, and in your community.

👉 Elevate your athletic conference or corporate convention with an unforgettable keynote from Olympic Coach Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 12,
        "theme_arc": "Saturday Post-Game Brotherhood",
        "slot": "Saturday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-19T23:00:00.000Z",
        "displayTime": "Saturday, Sep 19, 2026 - 5:00 PM MDT",
        "assetFile": "colorado-buffs-identity-02.png",
        "assetUrl": f"{CDN_BASE}/colorado-buffs-identity-02.png",
        "cta": "Speaking & Culture (lornettedaye.com/speaking)",
        "text": f"""WHEN THE LIGHTS DIM AND THE STADIUM EMPTIES. 🏟️🌙✨

When the fourth quarter clock hits 0:00, the scoreboard freezes. But the brotherhood built inside those four quarters lasts a lifetime.

Colorado's 2-0 start isn't just about offensive fireworks; it's about men buying into each other when the pressure is suffocating. When you see teammates celebrating another man's touchdown with more joy than their own, you know you are looking at something special.

Selfishness destroys talent. Selfless brotherhood multiplies it ten-fold.

What are you doing this weekend to reinforce genuine trust within your team?

👉 Bring world-class team dynamics and culture coaching to your organization. Keynotes & executive consulting: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 7: Sunday, Sep 20, 2026 (Film Session & Reset)
    {
        "id": 13,
        "theme_arc": "Sunday Film Session",
        "slot": "Sunday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-20T14:30:00.000Z",
        "displayTime": "Sunday, Sep 20, 2026 - 8:30 AM MDT",
        "assetFile": "colorado-buffs-julian-ready-03.png",
        "assetUrl": f"{CDN_BASE}/colorado-buffs-julian-ready-03.png",
        "cta": "Books & Speaking (lornettedaye.com/speaking)",
        "text": f"""SUNDAY FILM STUDY: THE EYE IN THE SKY DOES NOT LIE. 📽️🔍🏈

On Sunday morning, the crowd is gone, the music is silent, and the film room lights flick on.

Elite coaches and athletes know that you are never quite as good as you look when you win, and never as bad as you look when you lose. The greatness of players like Julian Lewis is their appetite for critical feedback. They don't watch the five touchdowns—they study the three incompletions.

Championship growth happens when you fall in love with correcting the details that nobody else noticed.

Are you brave enough to dissect your own mistakes with brutal honesty?

👉 Master the high-performance mental edge. Order *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books | Book Lornette Daye for Keynote Speaking: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 14,
        "theme_arc": "Weekly Reset & Atmosphere",
        "slot": "Sunday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-20T23:00:00.000Z",
        "displayTime": "Sunday, Sep 20, 2026 - 5:00 PM MDT",
        "assetFile": "colorado-buffs-folsom-belief-04.png",
        "assetUrl": f"{CDN_BASE}/colorado-buffs-folsom-belief-04.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""WEEK 1 IN THE BOOKS. THE STANDARDS RESET TOMORROW AT DAWN. 🌅🏔️

As we wrap up Week 1 of our Colorado Buffaloes leadership series, reflect on what makes Folsom Field's atmosphere so electric:

It is the tangible conviction that winning is no longer an occasional surprise—it is the expected outcome of superior preparation.

When an entire organization commits to higher standards, every tomorrow becomes brighter. But those standards must be renewed every single week with fresh sweat and focused intentionality.

Get some rest tonight. Tomorrow morning, we lace up and push the standard even higher.

👉 Schedule Lornette Daye to ignite your university athletics department or corporate leadership team: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # =========================================================================
    # WEEK 2: HIGH-LEVEL EXECUTION, CULTURE & SCALE (Sep 21 - Sep 27, 2026)
    # =========================================================================
    # DAY 8: Monday, Sep 21, 2026
    {
        "id": 15,
        "theme_arc": "Compounding Standards",
        "slot": "Monday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-21T14:30:00.000Z",
        "displayTime": "Monday, Sep 21, 2026 - 8:30 AM MDT",
        "assetFile": "colorado-buffs-52-points-05.png",
        "assetUrl": f"{CDN_BASE}/colorado-buffs-52-points-05.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""WEEK 2 KICKOFF: THE COMPOUNDING INTEREST OF RELENTLESS STANDARDS. 📈🏈

52 points on the board. 578 total offensive yards. That isn't luck; it's the compounding interest of showing up every day and demanding perfection in the fundamental details.

In corporate leadership and collegiate athletics, too many organizations search for a magical breakthrough scheme. But true competitive dominance comes from doing ordinary things with extraordinary discipline over long periods of time.

When your daily floor is higher than your competitor's ceiling, winning takes care of itself.

What fundamental standard are you compounding in your organization this week?

👉 Book Olympic Coach Lornette Daye for your keynote address on sustaining organizational excellence: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 16,
        "theme_arc": "Coaching Instinct vs Structure",
        "slot": "Monday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-21T23:00:00.000Z",
        "displayTime": "Monday, Sep 21, 2026 - 5:00 PM MDT",
        "assetFile": "colorado-buffs-growing-fast-06.png",
        "assetUrl": f"{CDN_BASE}/colorado-buffs-growing-fast-06.png",
        "cta": "Keynote Speaking & Leadership (lornettedaye.com/speaking)",
        "text": f"""COACHING YOUNG TALENT: HOW TO PROVIDE STRUCTURE WITHOUT KILLING INSTINCT. 🏈🎯💡

When you watch Colorado's young stars play fast, notice what Coach Prime and his staff have created:

Uncompromising structural discipline, paired with total freedom to let their natural instincts attack the defense.

Micromanagement strangles creativity. Lack of discipline creates chaos. Elite leadership finds that rare sweet spot where athletes have mastered the playbook so thoroughly that their physical brilliance can flow completely unhindered.

Are you empowering your team to play fast, or are you paralyzing them with fear of failure?

👉 Bring Lornette Daye to your leadership retreat to master modern athletic and corporate coaching: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 9: Tuesday, Sep 22, 2026
    {
        "id": 17,
        "theme_arc": "Accountability as Love",
        "slot": "Tuesday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-22T14:30:00.000Z",
        "displayTime": "Tuesday, Sep 22, 2026 - 8:30 AM MDT",
        "assetFile": "colorado-buffs-standard-07.png",
        "assetUrl": f"{CDN_BASE}/colorado-buffs-standard-07.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""ACCOUNTABILITY IS NOT PUNISHMENT: IT IS REVERENCE FOR THE OUTCOME. 🛡️🏆

Three offensive plays to go up 14-0. That kind of lightning strike only occurs when 11 individual players are locked into absolute accountability to each other.

If the left tackle misses his block, the play is blown. If the receiver runs a lazy route, the ball is intercepted. If the quarterback rushes his progression, the opportunity is lost.

In elite sport, holding your teammates accountable is the highest form of respect. You hold them to a standard because you believe in their greatness.

Do your leaders invite hard accountability, or do they retreat behind excuses?

👉 Inspire a culture of fearless mutual accountability across your organization. Book Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 18,
        "theme_arc": "Sustaining Momentum Post-Breakthrough",
        "slot": "Tuesday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-22T23:00:00.000Z",
        "displayTime": "Tuesday, Sep 22, 2026 - 5:00 PM MDT",
        "assetFile": "colorado-buffs-turning-point-08.png",
        "assetUrl": f"{CDN_BASE}/colorado-buffs-turning-point-08.png",
        "cta": "Books & Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""SUSTAINING MOMENTUM: WHAT HAPPENS AFTER THE TURNING POINT? 🔄⏳🔥

Breaking through is hard. Handling the applause and sustaining greatness afterward is where most programs crumble.

When you drop 52 points, everyone wants to pat you on the back. National television talks about your quarterback. Fans crown you champions in September.

This is precisely when true leaders sound the alarm. Complacency is the silent poison of good teams. You have to be hungrier after a win than you were after an embarrassing loss.

How are you guarding your organization against the trap of premature celebration?

👉 Dive into Lornette Daye's Olympic journey on rising after triumphs and heartbreaks. Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books | Keynote inquiries: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 10: Wednesday, Sep 23, 2026
    {
        "id": 19,
        "theme_arc": "Eliminating Doubt Through Conviction",
        "slot": "Wednesday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-23T14:30:00.000Z",
        "displayTime": "Wednesday, Sep 23, 2026 - 8:30 AM MDT",
        "assetFile": "colorado-buffs-conviction-09.png",
        "assetUrl": f"{CDN_BASE}/colorado-buffs-conviction-09.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""WHY ELITE EXECUTION REQUIRES THE TOTAL ELIMINATION OF DOUBT. 🎯💥

Look at the conviction on Julian Lewis's face before the snap. In college football, a microsecond of hesitation will get your pass batted down or your quarterback sacked.

Doubt is the friction that slows elite performers down.

The only antidote to doubt is relentless, exhaustive preparation. When you have taken 10,000 reps in practice, you don't 'think' on Saturday—you react with pure conviction.

When you walk into high-stakes negotiations or game-defining moments, is your mind clouded with doubt, or cleared by preparation?

👉 Book Lornette Daye for your corporate summit to equip your executive teams with elite cognitive clarity and unshakeable conviction: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 20,
        "theme_arc": "Realized Potential in Boulder",
        "slot": "Wednesday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-23T23:00:00.000Z",
        "displayTime": "Wednesday, Sep 23, 2026 - 5:00 PM MDT",
        "assetFile": "colorado-buffs-future-boulder-10.png",
        "assetUrl": f"{CDN_BASE}/colorado-buffs-future-boulder-10.png",
        "cta": "Speaking & Student Growth (lornettedaye.com/speaking)",
        "text": f"""FROM POTENTIAL TO REALIZED POWER. ⚡🏔️🏈

The sports world is littered with athletes and organizations who possessed endless 'potential' but never produced tangible results.

What is happening in Boulder with this Colorado Buffaloes team is the bridge between raw potential and realized power. Julian Lewis stepping into the starting role, throwing 5 touchdowns, and commanding the field like a veteran proves that potential only counts when backed by courage and execution.

Don't let your potential die in the realm of theory. Step onto the field and make it real.

What project or goal have you been treating as 'future potential' that needs to be executed today?

👉 Empower your students and young athletes to bridge the gap between talent and achievement. Read *Survival Skills for Students* ($14.99 CAD): lornettedaye.com/books | Keynote Speaking: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 11: Thursday, Sep 24, 2026
    {
        "id": 21,
        "theme_arc": "Statements Need Habit",
        "slot": "Thursday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-24T14:30:00.000Z",
        "displayTime": "Thursday, Sep 24, 2026 - 8:30 AM MDT",
        "assetFile": "colorado-buffs-statement-01.png",
        "assetUrl": f"{CDN_BASE}/colorado-buffs-statement-01.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""STATEMENTS FADE UNLESS REINFORCED BY HABIT. 🔄💪

Making a statement in Week 2 is exciting. But what happens in Week 4? Week 8? In the freezing cold of November when the initial buzz has worn off?

The greats don't rely on adrenaline to fuel their performance. They rely on cold, calculated habit.

Whether you are leading an athletic department competing for a Big 12 title or guiding an enterprise through market volatility: Your habits will either protect your statement or expose it as a fluke.

What daily habit is your team locking down today?

👉 Transform your conference or department retreat with a powerhouse keynote from 40+ year Olympic coach Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 22,
        "theme_arc": "Protecting Identity Against Noise",
        "slot": "Thursday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-24T23:00:00.000Z",
        "displayTime": "Thursday, Sep 24, 2026 - 5:00 PM MDT",
        "assetFile": "colorado-buffs-identity-02.png",
        "assetUrl": f"{CDN_BASE}/colorado-buffs-identity-02.png",
        "cta": "Executive Speaking (lornettedaye.com/speaking)",
        "text": f"""HOW CHAMPIONS PROTECT THEIR IDENTITY AGAINST OUTSIDE NOISE. 🛡️🤫🏈

When Colorado wins big, the national media circus amplifies. When Colorado faces adversity, critics swarm.

The only way to survive that kind of spotlight is to build an identity so deeply rooted on the inside that external noise cannot sway you. 578 yards at Folsom Field is proof that when a team locks its eyes on internal standards, external chatter becomes irrelevant background static.

Do not let other people's opinions define your identity. Build it yourself, brick by brick.

Leaders: How are you filtering the noise out of your organization's locker room?

👉 Book Lornette Daye for an executive keynote on mental fortress building and high-pressure focus: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 12: Friday, Sep 25, 2026
    {
        "id": 23,
        "theme_arc": "Calm in the Eye of the Storm",
        "slot": "Friday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-25T14:30:00.000Z",
        "displayTime": "Friday, Sep 25, 2026 - 8:30 AM MDT",
        "assetFile": "colorado-buffs-julian-ready-03.png",
        "assetUrl": f"{CDN_BASE}/colorado-buffs-julian-ready-03.png",
        "cta": "Athlete Books & Keynotes (lornettedaye.com/speaking)",
        "text": f"""FRIDAY EVE: FINDING THE CALM CENTER IN THE STORM. 🧘‍♂️⚡🏈

Look again at Julian Lewis sitting on the stone wall above Folsom Field. Helmets resting, mountains towering behind him, sun shining on the stadium.

Behind him is all the roar and chaos of major college football. But within him? Utter tranquility.

True champions do not match the chaotic energy of their environment. They project their own inner calm into the environment until the game slows down to their speed.

When the stakes escalate in your life this weekend, will you match the chaos, or will you command the calm?

👉 Equip your competitors with the mental toughness of world-class athletes. Order *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books | Book Lornette Daye for your Keynote: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 24,
        "theme_arc": "What Was Built in the Dark",
        "slot": "Friday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-25T23:00:00.000Z",
        "displayTime": "Friday, Sep 25, 2026 - 5:00 PM MDT",
        "assetFile": "colorado-buffs-folsom-belief-04.png",
        "assetUrl": f"{CDN_BASE}/colorado-buffs-folsom-belief-04.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""WHEN 50,000 PEOPLE WITNESS WHAT YOU BUILT IN THE DARK. 🏟️✨🔥

Tomorrow is game day again. When the Buffs sprint out of the tunnel, the crowd will see the jerseys, the lights, the pageantry, and the celebration.

What they won't see are the 5:30 AM winter weight sessions. The endless film breakdowns in July. The quiet reps when nobody was cheering and no cameras were rolling.

Greatness is never born in front of an audience. Greatness is merely confirmed under the lights.

Respect the dark work, and the bright stage will take care of itself.

👉 Bring Olympic Coach Lornette Daye to inspire your teams with the unyielding truth of champion development: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 13: Saturday, Sep 26, 2026
    {
        "id": 25,
        "theme_arc": "Demanding More of Yourself",
        "slot": "Saturday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-26T14:30:00.000Z",
        "displayTime": "Saturday, Sep 26, 2026 - 8:30 AM MDT",
        "assetFile": "colorado-buffs-52-points-05.png",
        "assetUrl": f"{CDN_BASE}/colorado-buffs-52-points-05.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""DEMAND MORE FROM YOURSELF THAN ANY COACH OR BOSS CAN ASK. 🏈🔥

When Colorado racked up 52 points, they were competing against their own highest potential—not just the opponent across the line.

The greatest athletes I have ever coached in four decades of international competition shared one unmistakable trait: They were their own toughest critics. When their coach told them 'good job', they were already thinking about how to refine their footwork by two inches.

If you only work hard when someone is watching or demanding it, you will remain average. When you demand elite performance from yourself for your own pride, you become unstoppable.

Step onto your field today and set the standard.

👉 Elevate your organization's internal drive. Book Lornette Daye for your annual leadership convention: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 26,
        "theme_arc": "4 Decades of Coaching Wisdom",
        "slot": "Saturday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-26T23:00:00.000Z",
        "displayTime": "Saturday, Sep 26, 2026 - 5:00 PM MDT",
        "assetFile": "colorado-buffs-growing-fast-06.png",
        "assetUrl": f"{CDN_BASE}/colorado-buffs-growing-fast-06.png",
        "cta": "Speaking & Mentorship (lornettedaye.com/speaking)",
        "text": f"""WHAT 4 DECADES OF COACHING TAUGHT ME ABOUT YOUNG TALENT STEPPING INTO GREATNESS. 🏆🌱

Watching young athletes mature in real time on national television is a masterclass in human capability.

I have stood beside young men and women on the Olympic stage who felt the weight of an entire nation on their shoulders. The ones who thrive do not do so because they are fearless; they thrive because their trust in their teammates and coaches outweighs their fear of failure.

Give young talent a clear purpose, hold them to an Olympian standard, and stand firmly in their corner. They will shock the world.

Who is a young leader you are pouring belief into this week?

👉 Book Lornette Daye for executive mentorship workshops and conference keynotes: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 14: Sunday, Sep 27, 2026 (Grand Finale)
    {
        "id": 27,
        "theme_arc": "The Non-Negotiable Standard",
        "slot": "Sunday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-27T14:30:00.000Z",
        "displayTime": "Sunday, Sep 27, 2026 - 8:30 AM MDT",
        "assetFile": "colorado-buffs-standard-07.png",
        "assetUrl": f"{CDN_BASE}/colorado-buffs-standard-07.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""THE STANDARD IS NON-NEGOTIABLE. 🛡️⚖️

Fast start. Real command. Mature response.

As we conclude our 14-day Colorado Buffaloes leadership masterclass, take this truth into your next chapter:

Culture is not established by the goals you write in your strategic deck. Culture is defined by the worst behavior and poorest execution your leadership is willing to tolerate.

When Coach Prime and the Buffs established their standard from snap one, they set a precedent for the entire season.

Hold the standard. Protect the culture. Build a brighter tomorrow.

👉 Bring Olympic Coach Lornette Daye to your university or corporate event to install champion-grade standards: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 28,
        "theme_arc": "From A Moment to A Movement",
        "slot": "Sunday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-27T23:00:00.000Z",
        "displayTime": "Sunday, Sep 27, 2026 - 5:00 PM MDT",
        "assetFile": "colorado-buffs-turning-point-08.png",
        "assetUrl": f"{CDN_BASE}/colorado-buffs-turning-point-08.png",
        "cta": "Speaking & Complete Catalog (lornettedaye.com/speaking)",
        "text": f"""THE FINALE: FROM A MOMENT TO A MOVEMENT. 🏔️✨🚀

52 points. 578 yards. A freshman quarterback announcing himself to the nation. A roaring stadium in Boulder that believes anything is possible.

Wins come and go on sports calendars. But when a group of human beings discovers what they are truly capable of when they sacrifice self for team, a turning point becomes an enduring movement.

Thank you for joining this 2-week journey into elite athletic psychology, culture building, and leadership excellence.

Whatever your arena—on the turf, in the boardroom, or in your personal journey—finish strong.

👉 Book Lornette Daye for your next conference keynote: lornettedaye.com/speaking
👉 Explore the official digital book catalog (*Survival Skills for Athletes*, *Finish Strong*, and more at $14.99 CAD): lornettedaye.com/books

#CUBuffs #ColoradoFootball #CoachPrime #JulianLewis #WeKeepReceipts #SkoBuffs #FolsomField #CollegeFootball #Big12 #FinishStrong #LeadershipExcellence #ChampionMindset #LornetteDaye #KeynoteSpeaker"""
    }
]

def check_media_head(url):
    req = urllib.request.Request(url, method='HEAD', headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
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
    print("🏈 LORNETTE DAYE - 2-WEEK COLORADO BUFFALOES CAMPAIGN SCHEDULER")
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

    report_path = os.path.join(os.path.dirname(__file__), "colorado-scheduled-report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("------------------------------------------------------")
    print(f"🎉 Colorado Campaign Report saved to {report_path}")
    successful = sum(1 for r in results if r.get("status") == "scheduled")
    print(f"Summary: {successful}/{len(posts_data)} posts scheduled in Buffer Scheduled Queue.")
    print("------------------------------------------------------")

if __name__ == "__main__":
    main()
