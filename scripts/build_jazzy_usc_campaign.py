import json
import os
from datetime import datetime, timezone

BASE_MEDIA_URL = "https://lornettedaye.com/campaigns/jazzy-usc"
HASHTAGS = "#JazzyDavidson #JuJuWatkins #USCWBB #FightOn #WomensBasketball #NCAAW #BigTenWBB #USCTrojans #FreshmanOfTheYear #WomenInSports #BetterPeopleBetterPlayers #LornettesFoundations #AthleteDevelopment #ChampionMindset"

posts_data = [
    {
        "day": 1,
        "date_str": "2026-10-24T20:45:00-06:00", # Tonight Sat Oct 24 @ 8:45 PM MDT
        "image": "jazzy_usc_01.png",
        "title": "JUJU SET THE STANDARD: CAN JAZZY RAISE THE BAR?",
        "caption": f"""JUJU SET THE STANDARD: CAN JAZZY RAISE THE BAR?

USC Women's Basketball enters a historic new era. A bigger stage. The Big Ten Conference. And more history waiting to be written.

When JuJu Watkins delivered one of the greatest freshman seasons in collegiate history, she established an uncompromising benchmark at the Galen Center. Now, five-star phenom Jazzy Davidson arrives on campus ready to write the next chapter.

In my four decades coaching Olympic champions, people often ask: How does an incoming prodigy handle the weight of following a legend?

The answer is simple: You do not compete with your teammate's legacy. You build upon their standard.

Great programs are never built by one individual alone. They are forged when exceptional talents unite, challenge each other daily in practice, and elevate the entire culture of the team.

Fan Question: How high is the ceiling for this USC tandem as they embark on the 2026-27 Big Ten season?

Explore how elite athletes and programs build championship foundations that endure pressure:
https://lornettedaye.com/foundations

{HASHTAGS}"""
    },
    {
        "day": 2,
        "date_str": "2026-10-25T18:00:00-06:00", # Sun Oct 25 @ 6:00 PM MDT
        "image": "jazzy_usc_02.png",
        "title": "THE STANDARD IS SET: NOW THE CHASE CONTINUES",
        "caption": f"""THE STANDARD IS SET: NOW THE CHASE CONTINUES.

Greatness does not stop to admire yesterday's trophy.

At USC, the foundation has been poured with sweat, defensive intensity, and national recognition. But the chase for a national championship demands something deeper: an appetite for continuous evolution.

Jazzy Davidson brings length, shot-making versatility, and fearless transition play. But what truly separates world-class performers is their mental discipline between games.

In high-performance athlete development, we evaluate athletes on their emotional poise when adversity strikes. Can you stay composed when your shot is not falling? Can you anchor your team's defense when the away crowd is deafening?

Championship standards are measured in the details that never make the highlight reel.

Fan Question: What is the most important quality needed to transition successfully from high school phenom to collegiate champion?

Discover our Olympic frameworks for mental toughness and athlete development:
https://lornettedaye.com/foundations

{HASHTAGS}"""
    },
    {
        "day": 3,
        "date_str": "2026-10-26T18:00:00-06:00", # Mon Oct 26 @ 6:00 PM MDT
        "image": "jazzy_usc_03.png",
        "title": "DIFFERENT PATHS, SAME PURPOSE: JUJU, JAZZY, AND USC",
        "caption": f"""DIFFERENT PATHS, SAME PURPOSE: JUJU, JAZZY, AND USC.

Two generational stars. Two distinct journeys. One shared ambition.

JuJu Watkins represents Los Angeles royalty, carrying the city's pride with electric scoring and magnetic presence. Jazzy Davidson arrives with elite national credentials and an unselfish drive to win at the highest level.

When critics question whether two dominant scorers can share the floor, they misunderstand the psychology of true greatness.

In elite sport, championship partnerships thrive on mutual respect. When Watkins draws double teams, Davidson finds open space. When Davidson attacks the lane, the defense collapses, creating perimeter opportunities.

Brotherhood and sisterhood in sports are built through daily communication, honest feedback, and celebrating each other's success.

Fan Question: What makes a superstar backcourt partnership truly unguardable?

Learn how we train teams to build unbreakable locker room trust and alignment:
https://lornettedaye.com/foundations

{HASHTAGS}"""
    },
    {
        "day": 4,
        "date_str": "2026-10-27T18:00:00-06:00", # Tue Oct 27 @ 6:00 PM MDT
        "image": "jazzy_usc_04.png",
        "title": "574 POINTS: A REMARKABLE FRESHMAN FOUNDATION",
        "caption": f"""574 POINTS: A REMARKABLE FRESHMAN FOUNDATION.

574 points in a single freshman season is not just a statistic. It is a statement of intent.

It proves consistency across dozens of games, endurance through brutal travel schedules, and the ability to produce when opposing defensive coordinators build entire game plans around stopping you.

Yet in the Lornette Daye Performance Edge framework, we teach that your previous record cannot hit your next shot.

Milestones are anchors of belief, not resting places. When you achieve early greatness, the true challenge is staying hungry while maintaining the humility of a student who still has everything to learn.

The foundation is built. Now the real construction begins.

Fan Question: What impressed you most about Jazzy Davidson's rookie campaign?

Discover how elite athletes sustain hunger after early career breakthroughs:
https://lornettedaye.com/foundations

{HASHTAGS}"""
    },
    {
        "day": 5,
        "date_str": "2026-10-28T18:00:00-06:00", # Wed Oct 28 @ 6:00 PM MDT
        "image": "jazzy_usc_05.png",
        "title": "EXPECTATION AS PRIVILEGE: CARRYING THE TROJAN CREST",
        "caption": f"""EXPECTATION AS PRIVILEGE: CARRYING THE TROJAN CREST.

When you wear Cardinal and Gold inside the Galen Center, pressure is not a burden. It is a privilege earned through talent and dedication.

Cheryl Miller. Lisa Leslie. Tina Thompson. The lineage of women's basketball excellence at USC is sacred.

Athletes who crumble under high expectations are those who focus outward on media commentary and public rankings. Athletes who thrive are those who focus inward on daily execution systems:
- Mastering footwork on closeouts.
- Communicating switches with vocal authority.
- Maintaining disciplined sleep and nutrition routines.

When your daily process is world-class, external pressure dissolves into quiet confidence.

Fan Question: How do you handle high expectations in your own competitive arena?

Explore our frameworks for performing under extreme organizational pressure:
https://lornettedaye.com/foundations

{HASHTAGS}"""
    },
    {
        "day": 6,
        "date_str": "2026-10-29T18:00:00-06:00", # Thu Oct 29 @ 6:00 PM MDT
        "image": "jazzy_usc_06.png",
        "title": "THE ART OF THE BACKCOURT TANDEM: COEXISTENCE OVER EGO",
        "caption": f"""THE ART OF THE BACKCOURT TANDEM: COEXISTENCE OVER EGO.

Great backcourts are not born through individual shot attempts. They are born through trust.

When you have two players capable of scoring thirty points on any given night, the hardest skill to develop is passing up a good shot for a great shot.

In over four decades mentoring national and Olympic teams, I have seen super-teams fracture when individual pride supersedes team mission. And I have watched historic squads achieve immortality when star players take pride in screen-setting, perimeter defense, and making the hockey assist.

When your superstar teammate celebrates your success more loudly than her own, your team becomes mathematically impossible to stop.

Fan Question: Which historic college basketball duo does this JuJu and Jazzy tandem remind you of?

Learn how we help leaders cultivate unselfish culture and team alignment:
https://lornettedaye.com/foundations

{HASHTAGS}"""
    },
    {
        "day": 7,
        "date_str": "2026-10-30T18:00:00-06:00", # Fri Oct 30 @ 6:00 PM MDT
        "image": "jazzy_usc_07.png",
        "title": "DEFENSIVE IDENTITY IN THE BIG TEN: EARNING RESPECT ON BOTH ENDS",
        "caption": f"""DEFENSIVE IDENTITY IN THE BIG TEN: EARNING RESPECT ON BOTH ENDS.

Offense sells tickets. Defensive rebounding wins conference championships.

Competing in the Big Ten means navigating physical post play, deliberate half-court pacing, and punishing perimeter screens in hostile arenas.

Jazzy Davidson's greatest asset at USC will not be her jump shot. It will be her ability to disrupt passing lanes, contest without fouling, and use her length to ignite the fast break.

As a coach, when your most talented offensive weapons are also your most relentless defensive stoppers, your entire locker room buys in.

Defensive excellence is a choice. You do not need to be having a great shooting night to dominate on defense.

Fan Question: How will USC's defensive identity hold up across the demanding Big Ten schedule?

Explore our principles of emotional discipline and defensive culture:
https://lornettedaye.com/foundations

{HASHTAGS}"""
    },
    {
        "day": 8,
        "date_str": "2026-10-31T18:00:00-06:00", # Sat Oct 31 @ 6:00 PM MDT
        "image": "jazzy_usc_08.png",
        "title": "PREPARATION IN THE DARK: THE UNTELEVISED WORK",
        "caption": f"""PREPARATION IN THE DARK: THE UNTELEVISED WORK.

The crowd sees the step-back three with three seconds on the shot clock.

They do not see the 6:00 AM film sessions on a rainy Tuesday morning. They do not see the ice baths, the mobility work, or the hundreds of spot-up jumpers taken in an empty gym before campus wakes up.

In Olympic athletics, we say that medals are won in the dark and merely picked up in the light.

When Jazzy Davidson and JuJu Watkins step into the spotlight, their confidence is rooted in the hundreds of hours they spent perfecting their craft when nobody was filming.

Confidence is not an emotion. Confidence is the memory of exhaustive preparation.

Fan Question: What is the most important habit in your own routine that keeps you sharp when pressure arrives?

Discover how we coach athletes to build unshakable preparation systems:
https://lornettedaye.com/foundations

{HASHTAGS}"""
    },
    {
        "day": 9,
        "date_str": "2026-11-01T18:00:00-07:00", # Sun Nov 01 @ 6:00 PM MST (UTC-7)
        "image": "jazzy_usc_09.png",
        "title": "COURAGE IN TRANSITION: STEPPING ONTO THE BIGGEST STAGE",
        "caption": f"""COURAGE IN TRANSITION: STEPPING ONTO THE BIGGEST STAGE.

Transition is the greatest test of an athlete's character.

Moving from high school dominance to collegiate stardom requires a complete recalibration. The defenders are faster, the scouting reports are exhaustive, and the margin for error is razor-thin.

Athletes who succeed during transition are those who replace fear of failure with curiosity to learn.

When you make a mistake on the floor, do you look at the bench in frustration, or do you immediately reset your focus for the next possession?

In our Complete Athlete Development System, we teach that resilience after setback is what separates contenders from pretenders. Learn the lesson, let go of the emotional residue, and compete on the next play.

Fan Question: What was the biggest transition in your athletic or professional career, and how did you conquer it?

Learn more about building emotional resilience through major career transitions:
https://lornettedaye.com/foundations

{HASHTAGS}"""
    },
    {
        "day": 10,
        "date_str": "2026-11-02T18:00:00-07:00", # Mon Nov 02 @ 6:00 PM MST
        "image": "jazzy_usc_10.png",
        "title": "CONSISTENCY AS A COMPETITIVE WEAPON: 32 OUT OF 32 NIGHTS",
        "caption": f"""CONSISTENCY AS A COMPETITIVE WEAPON: 32 OUT OF 32 NIGHTS.

Anyone can be extraordinary once. Championship athletes are dependable every single day.

Over a 32-game collegiate campaign, an athlete will face travel delays, minor physical ailments, academic deadlines, and off-shooting nights.

The secret to true greatness is raising your floor. On your worst day, can you still provide world-class effort, lockdown defense, and positive bench leadership?

When a coaching staff knows exactly what standard you will bring to the floor every night, you earn trust that no single hot-shooting streak can ever replace.

Consistency is a weapon. And it is forged in daily discipline.

Fan Question: In your opinion, who is the most consistent player in women's basketball history?

Explore our frameworks for professional dependability and athlete longevity:
https://lornettedaye.com/foundations

{HASHTAGS}"""
    },
    {
        "day": 11,
        "date_str": "2026-11-03T18:00:00-07:00", # Tue Nov 03 @ 6:00 PM MST
        "image": "jazzy_usc_11.png",
        "title": "THE PSYCHOLOGY OF THE SHOT-MAKER: UNFLINCHING EMOTIONAL POISE",
        "caption": f"""THE PSYCHOLOGY OF THE SHOT-MAKER: UNFLINCHING EMOTIONAL POISE.

Elite shooters think differently than ordinary players.

When an average player misses three consecutive perimeter shots, doubt creeps in. They hesitate on the catch, adjust their release, and second-guess their mechanics.

An elite shot-maker like Jazzy Davidson maintains complete optical poise. In her mind, the next shot is already through the net.

In the Performance Edge Framework, we remind athletes: Your previous shot cannot hit your next shot. When you decouple your present action from past results, hesitation disappears. You execute with pure, uncluttered flow.

Shoot with freedom. Trust your preparation.

Fan Question: When the game is on the line, what goes through your mind before you take the deciding shot?

Discover how we train competitors in emotional regulation and clutch focus:
https://lornettedaye.com/foundations

{HASHTAGS}"""
    },
    {
        "day": 12,
        "date_str": "2026-11-04T18:00:00-07:00", # Wed Nov 04 @ 6:00 PM MST
        "image": "jazzy_usc_12.png",
        "title": "COMMUNICATION WITHOUT WORDS: EYE CONTACT AND COURT VISION",
        "caption": f"""COMMUNICATION WITHOUT WORDS: EYE CONTACT AND COURT VISION.

The highest level of team chemistry happens in silence.

When JuJu Watkins and Jazzy Davidson share the court, their effectiveness will be dictated by their unspoken synergy. A quick glance in transition. A nod on an off-ball screen. Anticipating each other's cutting angles before the defense reacts.

In high-performance leadership, we call this shared mental model. When teammates possess identical understanding of spacing and tempo, reaction times drop to milliseconds.

That level of connection cannot be drawn on a dry-erase board. It is cultivated through hundreds of shared reps and authentic locker-room brotherhood and sisterhood.

Fan Question: How important is non-verbal communication in high-stakes competition?

Learn how we train teams to develop supreme communication and presence:
https://lornettedaye.com/foundations

{HASHTAGS}"""
    },
    {
        "day": 13,
        "date_str": "2026-11-05T18:00:00-07:00", # Thu Nov 05 @ 6:00 PM MST
        "image": "jazzy_usc_13.png",
        "title": "MENTORSHIP AND RECEPTION: HOW VETERANS EMPOWER ROOKIES",
        "caption": f"""MENTORSHIP AND RECEPTION: HOW VETERANS EMPOWER ROOKIES.

A truly confident leader never feels threatened by an incoming talent.

Watching JuJu Watkins embrace Jazzy Davidson reflects the maturity of a player who understands that true legacy is defined by what you build with others.

When an established star welcomes a rising phenom with open arms, the entire locker room culture shifts from anxiety to empowerment. And when the young player listens with genuine humility, rapid developmental breakthroughs occur.

Mentorship is a two-way street. It requires a mentor willing to share wisdom, and a student humble enough to receive it.

Together, they make USC unstoppable.

Fan Question: Who was the most influential mentor in your own athletic or professional life?

Discover how we help organizations build cultures of intergenerational mentorship:
https://lornettedaye.com/foundations

{HASHTAGS}"""
    },
    {
        "day": 14,
        "date_str": "2026-11-06T18:00:00-07:00", # Fri Nov 06 @ 6:00 PM MST
        "image": "jazzy_usc_14.png",
        "title": "ROAD TRIP RESILIENCE: WINNING IN HOSTILE ENVIRONMENTS",
        "caption": f"""ROAD TRIP RESILIENCE: WINNING IN HOSTILE ENVIRONMENTS.

Playing at home in front of friendly crowds is easy. True champions are forged on the road.

Navigating Big Ten road trips means stepping off charter flights into freezing Midwest weather and walking onto hostile courts in front of fifteen thousand screaming fans.

In these environments, talent alone is insufficient. You need emotional endurance:
- Silencing the outside noise and focusing only on the six feet around you.
- Supporting your teammates through hostile scoring runs.
- Executing half-court offensive sets when the shot clock is draining.

Road victories bond a team like nothing else in sport. When you win together in hostile territory, your belief becomes bulletproof.

Fan Question: What is your favorite memory of watching your team pull off an epic road victory?

Learn how we train athletes and executives to thrive in hostile competitive environments:
https://lornettedaye.com/foundations

{HASHTAGS}"""
    },
    {
        "day": 15,
        "date_str": "2026-11-07T18:00:00-07:00", # Sat Nov 07 @ 6:00 PM MST
        "image": "jazzy_usc_15.png",
        "title": "NIL, VISIBILITY, AND GROUNDED ROOTS: PROTECTING YOUR INNER PEACE",
        "caption": f"""NIL, VISIBILITY, AND GROUNDED ROOTS: PROTECTING YOUR INNER PEACE.

Modern collegiate athletics has changed forever. Brand partnerships, national commercials, and social media followings can easily become full-time distractions.

The athletes who navigate this new landscape successfully are those who maintain an anchored identity beyond sport.

In our Foundations curriculum, Foundation 1 is Identity Beyond Sport. When you know who you are as a human being, external praise cannot inflate your ego, and external criticism cannot crush your spirit.

Jazzy Davidson and JuJu Watkins are proving that you can command national business visibility while maintaining absolute discipline on the hardwood.

Keep the main thing the main thing. The game always comes first.

Fan Question: How can young athletes best protect their mental health amidst the modern NIL boom?

Explore our athlete development curriculum on building grounded personal identity:
https://lornettedaye.com/foundations

{HASHTAGS}"""
    },
    {
        "day": 16,
        "date_str": "2026-11-08T18:00:00-07:00", # Sun Nov 08 @ 6:00 PM MST
        "image": "jazzy_usc_16.png",
        "title": "THE VALUE OF ROLE CLARITY: EVERY PIECE OF THE PUZZLE",
        "caption": f"""THE VALUE OF ROLE CLARITY: EVERY PIECE OF THE PUZZLE.

Superstars make headlines, but role players win national titles.

A championship basketball team is an intricate mosaic. You need rim-protecting bigs who embrace physical screens, defensive specialists who guard the opponent's primary creator, and floor-spacers who keep the paint open for Davidson and Watkins.

When every athlete on the roster accepts and celebrates their unique assignment, friction disappears.

In my four decades coaching Olympic athletes, the happiest and most successful teams have always been those where every competitor felt valued for their distinct contribution.

Every role matters. Every assignment is vital.

Fan Question: Who is an unsung hero on your favorite basketball team who deserves more national spotlight?

Learn how we help teams establish clear roles, accountability, and mutual respect:
https://lornettedaye.com/foundations

{HASHTAGS}"""
    },
    {
        "day": 17,
        "date_str": "2026-11-09T18:00:00-07:00", # Mon Nov 09 @ 6:00 PM MST
        "image": "jazzy_usc_17.png",
        "title": "RECOVERY AS A DISCIPLINE: THE INVISIBLE HABIT OF LONGEVITY",
        "caption": f"""RECOVERY AS A DISCIPLINE: THE INVISIBLE HABIT OF LONGEVITY.

Training is only half the equation. Elite performance is defined by how quickly your body and mind can recover.

Over an intense NCAA season, physical micro-tears, nervous system fatigue, and mental overload accumulate rapidly.

Athletes who dominate in March are not necessarily those who worked the hardest in November; they are those who treated recovery as a non-negotiable discipline:
- Prioritizing deep, restorative sleep.
- Hydrating with scientific precision.
- Taking mental breaks away from the basketball arena.

Your body is your instrument. Respect it, care for it, and it will reward you when the fourth quarter arrives.

Fan Question: What is your number one daily recovery habit that keeps your energy peak?

Discover our Olympic protocols for physical recovery and emotional regulation:
https://lornettedaye.com/foundations

{HASHTAGS}"""
    },
    {
        "day": 18,
        "date_str": "2026-11-10T18:00:00-07:00", # Tue Nov 10 @ 6:00 PM MST
        "image": "jazzy_usc_18.png",
        "title": "CHAMPIONSHIP STANDARDS: ACCEPTING HONEST FILM-ROOM TRUTHS",
        "caption": f"""CHAMPIONSHIP STANDARDS: ACCEPTING HONEST FILM-ROOM TRUTHS.

The film room is where championships are either embraced or avoided.

The projector screen does not lie. It reveals missed box-outs, slow rotations, and half-hearted transition sprints.

Average athletes get defensive when their errors are pointed out. Elite competitors lean forward, take notes, and thank their coaches for the correction.

Coachability is the ultimate competitive advantage. When an athlete of Jazzy Davidson's caliber hungers for constructive critique, her ceiling becomes limitless.

Welcome the truth. Correction is the shortcut to mastery.

Fan Question: How do you handle constructive criticism when someone challenges your work?

Learn how we help leaders and athletes turn honest feedback into accelerated growth:
https://lornettedaye.com/foundations

{HASHTAGS}"""
    },
    {
        "day": 19,
        "date_str": "2026-11-11T18:00:00-07:00", # Wed Nov 11 @ 6:00 PM MST
        "image": "jazzy_usc_19.png",
        "title": "INSPIRING THE NEXT GENERATION: YOUNG GIRLS IN THE STANDS",
        "caption": f"""INSPIRING THE NEXT GENERATION: YOUNG GIRLS IN THE STANDS.

Look up into the Galen Center stands during any USC home game.

You will see thousands of young girls wearing number 12 and number 9 jerseys, eyes wide with possibility, clutching basketballs in their hands.

When Jazzy Davidson and JuJu Watkins compete with poise, dignity, and ferocity, they are doing far more than winning basketball games. They are expanding what millions of young women believe is possible for their own lives.

In our foundations work, Foundation 10 is Legacy and Community Impact. True greatness is never selfish. It lifts as it climbs.

Play with purpose. The future is watching.

Fan Question: What female athlete inspired you most when you were growing up?

Explore Lornette Daye's programs for youth mentorship and character development:
https://lornettedaye.com/foundations

{HASHTAGS}"""
    },
    {
        "day": 20,
        "date_str": "2026-11-12T18:00:00-07:00", # Thu Nov 12 @ 6:00 PM MST
        "image": "jazzy_usc_20.png",
        "title": "THE LEGACY AHEAD: WRITING HISTORY AT USC",
        "caption": f"""THE LEGACY AHEAD: WRITING HISTORY AT USC.

Twenty days exploring the standards, the mindset, and the future of USC Women's Basketball leads to one undeniable conclusion:

History belongs to those who prepare for it with unrelenting dedication.

JuJu Watkins set the standard. Jazzy Davidson has arrived to help raise the bar. Together with their coaching staff and teammates, they stand on the threshold of an unforgettable journey in the Big Ten.

As Olympic coach Lornette Daye, my message to these young champions is simple: Honor your preparation. Stay rooted in your brotherhood and sisterhood. And remember that the true champion is defined by who you become along the way.

Better people make better players. Fight On.

Fan Question: What is your bold prediction for USC Women's Basketball this season?

Explore Lornette Daye's Complete Athlete Development System:
https://lornettedaye.com/foundations

{HASHTAGS}"""
    }
]

# Assertions
for p in posts_data:
    assert "*" not in p["caption"], f"Asterisk in caption day {p['day']}"
    assert "*" not in p["title"], f"Asterisk in title day {p['day']}"
    assert "—" not in p["caption"], f"Em-dash in caption day {p['day']}"
    assert "—" not in p["title"], f"Em-dash in title day {p['day']}"
    local_path = os.path.join(r"c:\Users\Zhane\Documents\New project\LD 2.0 WEBSITE\public\campaigns\jazzy-usc", p["image"])
    assert os.path.isfile(local_path), f"Asset missing: {local_path}"

queue = []
for p in posts_data:
    dt = datetime.fromisoformat(p["date_str"])
    due_at = dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")
    queue.append({
        "day": p["day"],
        "date": dt.strftime("%Y-%m-%d"),
        "dueAt": due_at,
        "title": p["title"],
        "caption": p["caption"],
        "image": f"{BASE_MEDIA_URL}/{p['image']}",
        "local_file": p["image"]
    })

out_path = r"c:\Users\Zhane\Documents\New project\LD 2.0 WEBSITE\scripts\master-jazzy-usc-queue.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(queue, f, indent=2, ensure_ascii=False)

print(f"Successfully generated {len(queue)} campaign posts in {out_path}!")
for q in queue:
    print(f"Day {q['day']:02d} | {q['dueAt']} | {q['image']}")
