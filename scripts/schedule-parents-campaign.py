# -*- coding: utf-8 -*-
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

CDN_BASE = 'https://lornettedaye.com/campaigns/parents-set-1'

HASHTAGS = "#BehindTheChampion #SportsParents #ParentingChampions #BenShelton #BryanShelton #NaomiOsaka #TamakiOsaka #YouthSports #CoachingExcellence #SportsLeadership #OlympicMindset #LornetteDaye #FamilyFoundation"

posts_data = [
    # =========================================================================
    # WEEK 1: THE FOUNDATION & THE UNSEEN SACRIFICE (Sep 14 - Sep 20, 2026)
    # =========================================================================
    # DAY 1: Monday, Sep 14, 2026 (Ben & Bryan Shelton)
    {
        "id": 1,
        "slot": "Monday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-14T14:30:00.000Z",
        "assetFile": "parents-1.png",
        "assetUrl": f"{CDN_BASE}/parents-1.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""THE SCOREBOARD SAYS SHELTON. THE STORY HAS TWO OF THEM. 🎾🇺🇸

Look at Arthur Ashe Stadium. 24,000 screaming fans are watching Ben Shelton fire a 149 mph ace down the T.

The world sees a confident, electric 21-year-old superstar with thunder in his left arm. But look up into the player’s box. There sits Bryan Shelton—his father, his coach, his former collegiate mentor at Florida, and the man who taught him to swing a racket when he could barely see over the net.

In my 40+ years coaching Olympic athletes and national champions, I tell parents and athletic directors: No champion stands alone on the podium. Behind every explosive athlete is a parent who drove them to 6:00 AM practice in a rusted car, who iced their knees, and who taught them how to win with grace and lose without bitterness.

Parents & Coaches: When your young athlete achieves early success, how do you keep them grounded in character rather than blinded by ego?

👉 Book Lornette Daye for keynotes and workshops on parenting champions and nurturing youth sports talent sustainably: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 2,
        "slot": "Monday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-14T19:00:00.000Z",
        "assetFile": "parents-2.png",
        "assetUrl": f"{CDN_BASE}/parents-2.png",
        "cta": "Survival Skills for Men Book (lornettedaye.com/books)",
        "text": f"""DAD. COACH. MENTOR. BRYAN SHELTON WAS THERE LONG BEFORE THE SPOTLIGHT. 🤝🎾

Bryan Shelton was an ATP top-60 player himself. He coached the Florida Gators to national championships. He knew the tennis mountain from base to peak.

Yet what Bryan gave Ben wasn't just technical footwork or serve toss mechanics. It was the emotional anchor of a father's unwavering presence. On court changeovers, when the crowd is deafening and pressure is suffocating, Ben doesn't see a drill sergeant—he sees his father.

Fatherhood in high-performance sports is a delicate tightrope. When you push too hard, you fracture the bond. When you lead with love and firm discipline, you build an impenetrable foundation.

Fathers and Mentors: How do you balance being your son’s coach while never forgetting you are first and foremost his father?

👉 Build purpose, steady emotional resilience, and grounded leadership as a man. Read *Survival Skills for Men* by Lornette Daye ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 3,
        "slot": "Monday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-15T00:00:00.000Z",
        "assetFile": "parents-3.png",
        "assetUrl": f"{CDN_BASE}/parents-3.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""BEFORE THE WORLD STARTED CHEERING FOR BEN, HIS FATHER WAS ALREADY THERE. 🏟️✨

It is easy to cheer when an athlete is in the semifinals of the US Open. It’s easy to celebrate when sponsors are lining up and television networks are begging for interviews.

Bryan Shelton was there on cracked public courts in the Florida humidity when Ben double-faulted on game point in junior tournaments. He was there during tears, frustration, and the exhaustion of travel.

As an Olympic coach, I have seen too many young athletes burn out because parents love the trophy more than the child. Bryan loved the child first—and built the player second.

Athletic Directors, Academy Founders & Youth Sports Leaders: What culture are you fostering in your parent bleachers?

👉 Bring Lornette Daye to your school, academy, or coaching symposium to speak on family leadership in youth athletics: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 2: Tuesday, Sep 15, 2026 (Naomi & Tamaki Osaka)
    {
        "id": 4,
        "slot": "Tuesday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-15T14:30:00.000Z",
        "assetFile": "parents-6.png",
        "assetUrl": f"{CDN_BASE}/parents-6.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""THE WORLD SAW THE TROPHY. NAOMI SAW HER MOTHER'S SACRIFICE. 🏆🇯🇵

When Naomi Osaka lifted the US Open trophy into the New York night, flashbulbs lit up the sky. The cameras focused on the gleaming silver cup, the Nike kit, and the historic victory.

Naomi’s eyes looked straight past the trophy and into the player's box—at her mother, Tamaki Osaka.

Before the world knew Naomi’s name, Tamaki was working grueling double shifts in New York and Florida. Sleeping in her clothes. Sacrificing sleep, vacations, and any semblance of personal comfort so that Leonard could take Naomi and Mari to public courts with used tennis balls.

Mothers carry the invisible weight of high-performance dreams.

Moms & Sports Families: What is a sacrifice you made for your children that nobody in the stadium ever saw?

👉 Honor the mothers and family foundations behind champions. Book Lornette Daye for your sports organization keynote: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 5,
        "slot": "Tuesday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-15T19:00:00.000Z",
        "assetFile": "parents-7.png",
        "assetUrl": f"{CDN_BASE}/parents-7.png",
        "cta": "Survival Skills for Women Book (lornettedaye.com/books)",
        "text": f"""SHE WORKED SO HER DAUGHTERS COULD DREAM: A TRIBUTE TO TAMAKI OSAKA. 🌸🎾

Think about the courage of Tamaki Osaka.

Leaving her home in Nemuro, Hokkaido. Facing cultural estrangement and intense skepticism for building a multicultural family. Moving across continents and working endless hours in unfamiliar cities to support her daughters' athletic aspirations.

Tamaki never played professional tennis. She didn't know the technical nuances of a topspin backhand. What she gave Naomi and Mari was something infinitely more potent: unconditional maternal resilience and quiet, unshakable belief.

Women carry the generational torch. When a mother refuses to surrender, she expands the horizon for every woman who comes after her.

👉 Rebuild your confidence, embrace purpose, and thrive through life's hardest chapters. Read *Survival Skills for Women* by Lornette Daye ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 6,
        "slot": "Tuesday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-16T00:00:00.000Z",
        "assetFile": "parents-8.png",
        "assetUrl": f"{CDN_BASE}/parents-8.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""BEFORE NAOMI COULD CHASE THE DREAM, HER MOTHER HELPED PAY FOR THE CHANCE. 💵🎾

Tennis is an expensive, unforgiving sport. Court fees, stringing, entry fees, travel, coaching, equipment—the financial barriers weed out thousands of brilliant kids every year.

The Osakas didn't have corporate sponsors or federation stipends when Naomi was nine years old. Every single racket stringing came out of Tamaki Osaka’s paycheck from long, exhausting workdays.

In 40+ years of Olympic coaching, I have watched mothers skip meals, refinance mortgages, and work weekend shifts just so their daughter could compete in a qualifier.

Youth Sports Programs & Nonprofits: How can we build athletic ecosystems that support working families and dismantle economic barriers for young athletes?

👉 Partner with Olympic coach Lornette Daye for keynote speaking and youth sports strategy: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 3: Wednesday, Sep 16, 2026 (Ben & Bryan Shelton)
    {
        "id": 7,
        "slot": "Wednesday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-16T14:30:00.000Z",
        "assetFile": "parents-4.png",
        "assetUrl": f"{CDN_BASE}/parents-4.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""EVERY GREAT RUN HAS SOMEONE IN THE CORNER: HONOR THE FATHER. HONOR THE COACH. 🥊🎾

Look at Bryan Shelton applauding Ben in this picture. Hands clasped, eyes locked with proud intensity.

In 2023, Bryan Shelton did something that shocked the collegiate tennis world: After 11 glorious years leading the Florida Gators men’s team, winning the 2021 NCAA National Championship, he stepped down from his prestigious coaching job.

Why? To be on the road full-time with his son.

To walk away from security, tenure, and collegiate prestige to travel 40 weeks a year in hotel rooms because your son needs your steady hand on the ATP Tour—that is parental devotion.

Coaches & Parents: Have you ever sacrificed a career milestone to protect and nurture your child’s future?

👉 Book Lornette Daye to speak on sacrifice, mentorship, and championship team dynamics: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 8,
        "slot": "Wednesday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-16T19:00:00.000Z",
        "assetFile": "parents-5.png",
        "assetUrl": f"{CDN_BASE}/parents-5.png",
        "cta": "Survival Skills for Athletes Book (lornettedaye.com/books)",
        "text": f"""SOME COACHES BUILD PLAYERS. SOME FATHERS BUILD PEOPLE. BRYAN SHELTON DID BOTH. 🧱❤️

Here is Bryan Shelton's famous coaching principle:
"Tennis is what you do. It is NOT who you are."

When an athlete believes their human value depends on whether a ball lands inside the white line, they become emotionally fragile. They choke on break points because they are defending their self-worth.

Bryan insulated Ben from that trap. He made sure Ben knew he was loved unconditionally whether he won the NCAA title or lost in the first round of a challenger. That emotional security is why Ben plays with such fearless joy.

Athletes: Do you know who you are when the racket is in the bag?

👉 Build champion-level mental poise grounded in permanent identity. Read *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 9,
        "slot": "Wednesday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-17T00:00:00.000Z",
        "assetFile": "parents-1.png",
        "assetUrl": f"{CDN_BASE}/parents-1.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""BEHIND THE ROAR: THE LESSONS OF FLORIDA TENNIS 🐊🎾

At the University of Florida, Bryan coached Ben to the 2022 NCAA Singles Championship.

People assumed Ben was handed the #1 singles spot because he was the coach's son. But Bryan made Ben earn every single set in practice. He held his own son to a stricter standard of punctuality, humility, and locker-room cleanup than anyone else on the roster.

Favoritism destroys team culture. Integrity and equal accountability build enduring championship character.

Athletic Leaders & Head Coaches: How do you handle coaching your own children or relatives without compromising the locker room standard?

👉 Invite Lornette Daye to lead an Olympic culture and accountability workshop for your athletic department: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 4: Thursday, Sep 17, 2026 (Naomi & Tamaki Osaka)
    {
        "id": 10,
        "slot": "Thursday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-17T14:30:00.000Z",
        "assetFile": "parents-9.png",
        "assetUrl": f"{CDN_BASE}/parents-9.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""EVERY TROPHY HAS A STORY THE CAMERA NEVER SAW: THIS ONE IS FOR MOM. 🏆🤱

Look at Tamaki adjusting Naomi’s towel on the changeover. That gentle, tender touch in a world of cutthroat global competition.

When Naomi faced intense global media scrutiny, mental health battles, and the overwhelming pressure of becoming the highest-paid female athlete in history, where did she retreat? She retreated to the calm, safe harbor of her mother's presence.

Tamaki never asked Naomi for titles or ranking points. She asked if she was eating well, if she was sleeping, and if her heart was at peace.

Parenting High Achievers: Are we checking in on our children’s internal hearts, or only on their external report cards and scorecards?

👉 Book Lornette Daye to address student-athletes, parents, and coaches on holistic mental wellness: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 11,
        "slot": "Thursday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-17T19:00:00.000Z",
        "assetFile": "parents-10.png",
        "assetUrl": f"{CDN_BASE}/parents-10.png",
        "cta": "UMATTR Devotional (lornettedaye.com/books)",
        "text": f"""THE CHAMPION STOOD IN THE LIGHT. HER MOTHER HELPED CARRY THE JOURNEY. ✨💛

Tamaki Osaka rarely gave public interviews. She didn't seek the limelight or brand endorsements.

She chose to remain the steady, prayerful foundation in the background. In a culture obsessed with self-promotion, Tamaki’s selfless presence proves that the greatest power in a champion's life is often quiet, understated, and steadfast.

To every mother, grandmother, and mentor holding the ladder while your child climbs toward the light: Your labor is seen. Your love matters.

👉 Anchor your soul with daily reminders of worth, hope, and purpose. Explore the *UMATTR Devotional* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 12,
        "slot": "Thursday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-18T00:00:00.000Z",
        "assetFile": "parents-6.png",
        "assetUrl": f"{CDN_BASE}/parents-6.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""WHAT MOTHERS TEACH US ABOUT ENDURANCE: LESSONS FROM 40 YEARS OF COACHING 🌸🏅

I have coached athletes who came from extreme privilege, and athletes who came from single-parent households working three jobs to buy running spikes.

Nine times out of ten, the athlete who outlasts the storm is the one who remembers the quiet sacrifice of their mother. When pain sets in during the fourth quarter or the third set, they don't fight for themselves—they fight to honor the woman who sacrificed everything so they could stand on that floor.

Coaches: How are you cultivating grateful athletes who compete for something bigger than their own ego?

👉 Book Lornette Daye to inspire your athletic program with the power of purpose-driven competition: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 5: Friday, Sep 18, 2026 (Ben & Bryan Shelton)
    {
        "id": 13,
        "slot": "Friday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-18T14:30:00.000Z",
        "assetFile": "parents-2.png",
        "assetUrl": f"{CDN_BASE}/parents-2.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""THE ART OF THE SIDELINE WHISPER: COMMUNICATION UNDER FIRE 🎾🗣️

Watch Bryan Shelton lean over the railing to speak to Ben between sets.

Notice his posture: No wild hand gestures. No panic. No scolding. Just two calm, measured sentences delivered with unwavering eye contact.

In championship moments, athletes don't need speeches. They need clarity. They need one tactical adjustment and a reminder to breathe. A frantic coach produces a frantic athlete; a centered mentor creates a composed champion.

Coaches & Parents: What does your body language communicate to your athletes when they make a mistake in a crucial moment?

👉 Learn high-performance communication and emotional composure from Olympic coach Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 14,
        "slot": "Friday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-18T19:00:00.000Z",
        "assetFile": "parents-3.png",
        "assetUrl": f"{CDN_BASE}/parents-3.png",
        "cta": "Survival Skills for Men Book (lornettedaye.com/books)",
        "text": f"""MASCULINITY, BROTHERHOOD, AND FATHERHOOD IN MODERN SPORTS 🛡️👨‍👦

Look at the warmth and mutual respect between Ben and Bryan Shelton.

For decades, sports culture promoted a toxic model of father-coach relationships—angry outbursts, fear-based motivation, and emotional coldness. Bryan Shelton presents a masterclass in modern fatherhood: combining rigorous athletic discipline with deep emotional warmth, shared laughter, and mutual respect.

When a young man feels respected by his father, he carries no fear onto the court.

Men & Fathers: Are you leading the young men in your life through fear, or through steady, loving strength?

👉 Discover practical prompts and emotional resilience for modern men. Read *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 15,
        "slot": "Friday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-19T00:00:00.000Z",
        "assetFile": "parents-4.png",
        "assetUrl": f"{CDN_BASE}/parents-4.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""COLLEGE TO PROS: HOW BRYAN PREPARED BEN FOR THE TOUR TRANSITION 🎓🚀

Thousands of brilliant collegiate athletes fail to survive the transition to the professional ranks.

Why? Because in college, you have trainers, teammates, meals, and structure provided. On the pro tour, you are alone in airports, dealing with jet lag, contracts, and ruthless competitors fighting for prize money.

Bryan used Ben’s two years at Florida not just to win matches, but to build an autonomous professional mindset.

Collegiate Athletic Directors: How well does your department prepare student-athletes for the psychological cliff of transitioning to life after college?

👉 Book Lornette Daye for your student-athlete development curriculum and transition workshops: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 6: Saturday, Sep 19, 2026 (Naomi & Tamaki Osaka)
    {
        "id": 16,
        "slot": "Saturday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-19T14:30:00.000Z",
        "assetFile": "parents-7.png",
        "assetUrl": f"{CDN_BASE}/parents-7.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""CULTURAL IDENTITY AND MATERNAL ROOTS: THE OSAKA STORY 🇯🇵🇭🇹🇺🇸

Naomi Osaka’s story is a tapestry of cultures: Japanese mother, Haitian father, raised in America, competing under the Japanese flag.

Navigating multicultural identity under the harsh glare of global media is an immense psychological burden. Tamaki Osaka gave Naomi the greatest gift a parent can give: unconditional acceptance of her complete self.

She grounded Naomi in Japanese values of respect, quiet focus, and humility, while celebrating her bold individuality.

Educators & Youth Directors: How is your athletic organization embracing and supporting athletes from diverse cultural backgrounds?

👉 Partner with Olympic coach Lornette Daye to foster inclusive, resilient athletic environments: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 17,
        "slot": "Saturday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-19T19:00:00.000Z",
        "assetFile": "parents-8.png",
        "assetUrl": f"{CDN_BASE}/parents-8.png",
        "cta": "Survival Skills for Women Book (lornettedaye.com/books)",
        "text": f"""WHEN THE DREAM COSTS EVERYTHING: FINANCIAL SACRIFICE IN YOUTH SPORTS 💸🎾

Let's speak frankly: Most families cannot afford elite youth sports.

Tamaki Osaka didn't come from wealth. She worked extra shifts, budgeted every dollar, and made sacrifices that most parents would consider unreasonable. She did it not with a guarantee of Grand Slam millions, but out of pure belief in her daughters' potential.

To every mother currently driving the 5:00 AM carpool, packing brown-bag lunches between double shifts, and wondering if the sacrifice will ever pay off:

The real reward isn't the trophy. It’s the resilient, disciplined woman your daughter becomes along the way.

👉 Find hope, strength, and practical wisdom for life's hardest seasons. Read *Survival Skills for Women* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 18,
        "slot": "Saturday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-20T00:00:00.000Z",
        "assetFile": "parents-9.png",
        "assetUrl": f"{CDN_BASE}/parents-9.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""PROTECTING ATHLETE MENTAL HEALTH: WHAT PARENTS MUST KNOW 🧠❤️

In 2021, Naomi Osaka stepped away from Roland Garros to protect her mental health, opening a worldwide conversation on athlete depression and anxiety.

Who stood beside her without judgment? Her mother Tamaki.

Too many parents push their children to play through emotional agony because they fear losing rankings or sponsorships. Tamaki reminded the sports world of a sacred truth: Your child's mental well-being is worth infinitely more than any tournament title.

Sports Leaders & Parents: Are we creating spaces where athletes feel safe to say, "I am struggling"?

👉 Book Lornette Daye for your organization’s mental performance and wellness keynote: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 7: Sunday, Sep 20, 2026 (Ben & Bryan Shelton)
    {
        "id": 19,
        "slot": "Sunday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-20T14:30:00.000Z",
        "assetFile": "parents-5.png",
        "assetUrl": f"{CDN_BASE}/parents-5.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""HALF-TIME REFLECTION: THE SHELTON FATHERHOOD STANDARD 👨‍👦🎾

We have completed Week 1 of our campaign examining the parents behind champions.

Look at the smile on Ben and Bryan Shelton’s faces in this photo. That is not the smile of a coach and a player who only connect through stats. That is the joy of a father and son who genuinely enjoy being in each other’s presence.

When you invest in the human being first, the athlete flourishes naturally.

Coaches & Parents: What is one thing you can do this week to show your athlete you value them for who they are, not just what they produce on the field?

👉 Elevate your youth sports program with Lornette Daye's leadership masterclass: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 20,
        "slot": "Sunday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-20T19:00:00.000Z",
        "assetFile": "parents-1.png",
        "assetUrl": f"{CDN_BASE}/parents-1.png",
        "cta": "Survival Skills for Athletes Book (lornettedaye.com/books)",
        "text": f"""PLAYING WITH JOY: HOW BRYAN KEPT BEN’S SPARK ALIVE ⚡🎾

Have you ever watched Ben Shelton play tennis? The exuberant fist pumps, the high-fives with fans, the raw passion.

In an era of robotic, scripted athletes, Ben plays like a kid who just discovered the game yesterday. That joy is Bryan’s greatest masterpiece. Bryan never turned tennis into a joyless job. He preserved Ben's love for the battle.

Athletes: Are you playing with joy today, or has the pressure stolen your smile?

👉 Reignite your passion, focus, and competitive discipline. Read *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 21,
        "slot": "Sunday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-21T00:00:00.000Z",
        "assetFile": "parents-2.png",
        "assetUrl": f"{CDN_BASE}/parents-2.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""THE PARENT-COACH RETIREMENT PLAN: KNOWING WHEN TO STEP BACK 🛑🌱

One of the hardest decisions for any parent-coach is knowing when to let outside voices in.

Bryan Shelton was wise enough to know his strengths, but also humble enough to welcome outside tactical minds and fitness coaches into Ben's team. He never let his ego stand in the way of his son’s development.

Parent-Coaches: Can you step aside when your child needs a different voice to reach the next level?

In Olympic coaching, parental selflessness is the hallmark of true maturity.

👉 Bring Lornette Daye to consult on coaching dynamics and athletic transitions: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # =========================================================================
    # WEEK 2: LEGACY, MATURITY & RAISING CHAMPIONS SUSTAINABLY (Sep 21 - Sep 27, 2026)
    # =========================================================================
    # DAY 8: Monday, Sep 21, 2026 (Naomi & Tamaki Osaka)
    {
        "id": 22,
        "slot": "Monday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-21T14:30:00.000Z",
        "assetFile": "parents-10.png",
        "assetUrl": f"{CDN_BASE}/parents-10.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""STRONG WOMEN RAISE CHAMPIONS: THE UNBROKEN CHAIN 🌸🔗

Tamaki Osaka passed on to Naomi something money cannot buy: the strength to stand tall in the light without losing your soul.

Now, as Naomi Osaka navigates motherhood herself with her daughter Shai, she draws upon the identical reservoir of unconditional love and quiet dignity that Tamaki poured into her.

The greatest legacy of an athletic parent is not the medals in the display case—it is the character passed down through generations.

Mothers & Daughters: How has your mother's quiet resilience shaped who you are today?

👉 Book Olympic coach Lornette Daye for your women in leadership or athletic summit: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 23,
        "slot": "Monday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-21T19:00:00.000Z",
        "assetFile": "parents-6.png",
        "assetUrl": f"{CDN_BASE}/parents-6.png",
        "cta": "Survival Skills for Women Book (lornettedaye.com/books)",
        "text": f"""WHEN THE STADIUM GOES DARK: WHO IS STILL SITTING NEXT TO YOU? 🏟️🌑

When Naomi wins a Grand Slam, thousands of people want a piece of her time. Brands, agents, celebrities, fans.

When Naomi loses in the second round and sits crying in the locker room, the entourage vanishes. Only Tamaki is there. Only a mother sits in the silence, holding her hand, reminding her that she is loved, valued, and safe.

Never confuse fair-weather fans with the unconditional foundation of family.

👉 Rebuild your foundation, discover purpose, and thrive beyond external validation. Read *Survival Skills for Women* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 24,
        "slot": "Monday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-22T00:00:00.000Z",
        "assetFile": "parents-7.png",
        "assetUrl": f"{CDN_BASE}/parents-7.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""THE SILENT PARTNERS: HONOURING WORKING-CLASS SPORTS FAMILIES 🛠️🎾

In elite tennis, you rarely hear about the working-class families. The sport often markets itself as country clubs, white linens, and champagne.

Tamaki Osaka broke that mold. She proved that a working woman from Hokkaido, through grit, long hours, and ferocious love, could raise a four-time Grand Slam champion and global trailblazer.

Sports Organizations & Foundations: Are your talent search programs reaching into the working-class neighborhoods where the next Naomi Osaka is practicing against a brick wall?

👉 Partner with Lornette Daye to develop accessible, grassroots athletic development pipelines: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 9: Tuesday, Sep 22, 2026 (Ben & Bryan Shelton)
    {
        "id": 25,
        "slot": "Tuesday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-22T14:30:00.000Z",
        "assetFile": "parents-3.png",
        "assetUrl": f"{CDN_BASE}/parents-3.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""TEACHING ACCOUNTABILITY: WHY BRYAN NEVER BLAMED THE UMPIRES 🎾⚖️

Notice Ben Shelton on court: You will never see him smash a racket into pieces, verbally assault a chair umpire, or make excuses in post-match press conferences.

That is Bryan Shelton’s signature. Bryan taught Ben that an elite athlete takes 100% radical responsibility for every ball. If you missed, you missed. Go back to the practice court and fix it.

Coaches & Parents: Are you allowing your young athletes to blame referees and court conditions, or are you teaching them the strength of personal accountability?

👉 Book Lornette Daye to train your coaches and athletes on accountability and emotional discipline: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 26,
        "slot": "Tuesday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-22T19:00:00.000Z",
        "assetFile": "parents-4.png",
        "assetUrl": f"{CDN_BASE}/parents-4.png",
        "cta": "Survival Skills for Men Book (lornettedaye.com/books)",
        "text": f"""THE POWER OF PATIENCE: WHY BEN WAITED TO TURN PRO ⏳🎾

In today’s hyper-commercialized tennis world, parents rush 16-year-olds into the pro ranks, chasing prize money and sponsor contracts. Most burn out by age 20.

Bryan Shelton took a completely different path. He kept Ben in college at Florida for two full years. He let Ben mature physically, earn his college stripes, win the NCAA singles championship, and learn how to be a dependable teammate before throwing him into the ATP meat-grinder.

Patience is a competitive advantage.

Men & Leaders: Are you rushing toward the spotlight before your foundation is strong enough to carry the weight?

👉 Strengthen your personal foundation and build steady habits. Read *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 27,
        "slot": "Tuesday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-23T00:00:00.000Z",
        "assetFile": "parents-5.png",
        "assetUrl": f"{CDN_BASE}/parents-5.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""THE HIGHER CALLING OF YOUTH COACHING: BUILDING CITIZENS FIRST 🏛️❤️

When Bryan Shelton reflects on his coaching career, he doesn't brag about the NCAA trophies or ATP rankings.

He talks about the boys who became faithful husbands, honest businessmen, and loving fathers. He talks about character.

In over 40 years of Olympic coaching, I remind administrators: Sport is merely the vehicle; character is the destination. If we produce champions on the court who fail in life off the court, we have failed as mentors.

Collegiate ADs & Coaches: What is the true measure of success in your program?

👉 Bring Lornette Daye’s Olympic Masterclass to your campus or coaching clinic: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 10: Wednesday, Sep 23, 2026 (Naomi & Tamaki Osaka)
    {
        "id": 28,
        "slot": "Wednesday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-23T14:30:00.000Z",
        "assetFile": "parents-8.png",
        "assetUrl": f"{CDN_BASE}/parents-8.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""RESILIENCE THROUGH SKEPTICISM: WHEN NOBODY BELIEVES BUT MOM 🛡️🌸

When Tamaki and Leonard decided to raise their daughters to be world-class tennis champions, outsiders told them it was impossible.

They had no money. They had no tennis background. They didn't fit the traditional country club archetype. People laughed behind their backs.

Tamaki tuned out the noise. She woke up at 5:00 AM, went to work, and believed. A mother's faith is stronger than the skepticism of the entire world.

Parents: When others doubt your child’s unconventional dream, do you have the courage to keep believing?

👉 Book Lornette Daye to ignite your sports organization with relentless belief: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 29,
        "slot": "Wednesday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-23T19:00:00.000Z",
        "assetFile": "parents-9.png",
        "assetUrl": f"{CDN_BASE}/parents-9.png",
        "cta": "Survival Skills for Women Book (lornettedaye.com/books)",
        "text": f"""A MOTHER'S BOUNDARIES: KNOWING WHEN TO SAY 'ENOUGH' 🛑🌸

One of the most profound lessons from Tamaki Osaka was her ability to set boundaries around her daughters.

She protected Naomi from predatory managers, greedy sponsors, and exploitative environments. She ensured that home was always a sacred sanctuary free from contract negotiations and tennis talk.

Every young athlete needs a parent who is willing to be the shield against the business of sports.

Mothers: Are you creating safe boundaries that protect your children’s emotional well-being?

👉 Empower yourself with practical tools for boundary setting and purposeful living. Read *Survival Skills for Women* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 30,
        "slot": "Wednesday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-24T00:00:00.000Z",
        "assetFile": "parents-10.png",
        "assetUrl": f"{CDN_BASE}/parents-10.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""THE LEGACY OF MOTHERS IN SPORT: INSPIRING GENERATIONS 🌸✨

Look at Naomi holding that trophy with Tamaki by her side.

That image inspired millions of young girls across Asia, Africa, the Caribbean, and North America to pick up a tennis racket. But more than that, it inspired mothers everywhere to know that their daily sacrifices are never in vain.

Sport has the power to elevate humanity when it is anchored in the warmth of family.

👉 Bring Lornette Daye to your school district, sports conference, or parenting keynote: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 11: Thursday, Sep 24, 2026 (Ben & Bryan Shelton)
    {
        "id": 31,
        "slot": "Thursday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-24T14:30:00.000Z",
        "assetFile": "parents-1.png",
        "assetUrl": f"{CDN_BASE}/parents-1.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""THE FATHER AS SHIELD: PROTECTING BEN FROM THE HYPE MACHINE 🛡️🎾

When Ben Shelton reached the quarterfinals of the Australian Open in his very first trip outside the United States, the media exploded.

Suddenly, he was hailed as the next great savior of American men's tennis. Sponsors descended. Experts declared he would win multiple Grand Slams before age 22.

Bryan Shelton stood firmly in front of the hype machine. He kept Ben focused on footwork, recovery, and daily reps. He told the press: "Ben is a work in progress. Let him develop at his own pace."

Parents: How do you protect your talented child from the poison of premature hype?

👉 Book Lornette Daye for your athletic department’s keynotes on managing modern pressure: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 32,
        "slot": "Thursday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-24T19:00:00.000Z",
        "assetFile": "parents-2.png",
        "assetUrl": f"{CDN_BASE}/parents-2.png",
        "cta": "Survival Skills for Athletes Book (lornettedaye.com/books)",
        "text": f"""LISTENING AS A SUPERPOWER: WHY BEN TRUSTS BRYAN 👂🎾

Watch Ben on the changeover in this shot.

He isn't looking at his phone. He isn't staring into the crowd. His eyes are locked on his father's lips. That level of absolute, undivided attention is rare in young athletes today.

Ben listens because Bryan has earned his trust over 20 years of consistency, honesty, and unconditional love. You cannot demand an athlete’s attention; you have to earn it through your own character.

Coaches & Parents: Does your athlete listen to you because they fear you, or because they trust you with their life?

👉 Build trust and unshakeable coach-athlete connection. Read *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 33,
        "slot": "Thursday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-25T00:00:00.000Z",
        "assetFile": "parents-3.png",
        "assetUrl": f"{CDN_BASE}/parents-3.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""FROM FATHER-SON TO WORLD CONTENDERS: THE SHELTON BLUEPRINT 🇺🇸🏆

Ben and Bryan Shelton represent the best of what sports can be: family loyalty, mutual respect, and relentless pursuit of excellence.

As Ben continues his rise through the ATP rankings, the foundation remains unchanged: God, family, hard work, and humility.

Athletic Programs: Are you teaching your athletes the technical game, or are you building the character foundations that make them champions for life?

👉 Partner with Lornette Daye for high-performance leadership consulting: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 12: Friday, Sep 25, 2026 (Naomi & Tamaki Osaka)
    {
        "id": 34,
        "slot": "Friday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-25T14:30:00.000Z",
        "assetFile": "parents-6.png",
        "assetUrl": f"{CDN_BASE}/parents-6.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""BEYOND THE SILVER TROPHY: THE ETERNAL VALUE OF A MOTHER'S LOVE 🏆🌸

Trophies collect dust on mantels. Ranking points expire every 52 weeks. Endorsement contracts come and go.

What lasts forever is the knowledge that someone loved you enough to work overnight shifts in Queens so you could hit tennis balls at dawn. Tamaki’s legacy is written not in silver or marble, but in the heart of her daughter.

In 40+ years of Olympic coaching, I have never seen a medal that shines brighter than a mother's selfless sacrifice.

To every mother reading this: Your sacrifice matters.

👉 Bring Olympic coach Lornette Daye to speak at your school, academy, or women's conference: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 35,
        "slot": "Friday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-25T19:00:00.000Z",
        "assetFile": "parents-7.png",
        "assetUrl": f"{CDN_BASE}/parents-7.png",
        "cta": "Survival Skills for Women Book (lornettedaye.com/books)",
        "text": f"""THE COURAGE TO START FROM ZERO: LESSONS FROM TAMAKI OSAKA 🌸🌱

Tamaki Osaka had every excuse to give up.

She was in a foreign country, raising two young daughters with very little money, and pursuing an athletic dream with odds of less than one in a million. Most people would have chosen the safe, conventional path.

Tamaki chose courage. She chose to work, sacrifice, and give her daughters a chance to touch the sky.

Women & Leaders: Where in your life are you letting fear of failure stop you from pursuing a bold, meaningful dream?

👉 Step out of survival mode and into purposeful thriving. Read *Survival Skills for Women* by Lornette Daye ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 36,
        "slot": "Friday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-26T00:00:00.000Z",
        "assetFile": "parents-8.png",
        "assetUrl": f"{CDN_BASE}/parents-8.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""HONOURING THE UNSEEN HEROES OF YOUTH SPORTS 🏅🤱

Behind every youth soccer team, track club, gymnastics squad, and tennis clinic are the mothers and fathers who make it possible.

They pack the orange slices. They pay the tournament registrations. They wait in cold parking lots during 3-hour practices. They wipe away the tears after a tough loss.

They don't get the medals, the applause, or the television cameras. But without them, sports would not exist.

Coaches & Athletic Directors: When was the last time your program took an evening to honor and celebrate your sports parents?

👉 Book Lornette Daye to deliver a memorable, emotional keynote at your annual athletic banquet: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 13: Saturday, Sep 26, 2026 (Ben & Bryan Shelton)
    {
        "id": 37,
        "slot": "Saturday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-26T14:30:00.000Z",
        "assetFile": "parents-4.png",
        "assetUrl": f"{CDN_BASE}/parents-4.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""THE SHELTON STANDARD: HUMILITY IN VICTORY, CLASS IN DEFEAT 🏆🤝

Whether Ben wins in five thrilling sets on Arthur Ashe Stadium or loses in a tiebreak, his post-match routine is identical:

He hugs his opponent at the net. He thanks the ball kids. He waves to the fans. And he looks up at Bryan with gratitude in his eyes.

Class is not an accident; it is taught at the kitchen table.

Parents & Coaches: What values are you instilling at your kitchen table that show up when your athlete is under the spotlight?

👉 Elevate your youth sports culture with an Olympic leadership keynote from Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 38,
        "slot": "Saturday Mid-day (1:00 PM MDT)",
        "dueAt": "2026-09-26T19:00:00.000Z",
        "assetFile": "parents-5.png",
        "assetUrl": f"{CDN_BASE}/parents-5.png",
        "cta": "Survival Skills for Men Book (lornettedaye.com/books)",
        "text": f"""FATHERHOOD THAT ENDURES BEYOND THE SCORESHEET 👨‍👦🎾

One day, Ben Shelton’s playing career will end. The racket will be stored away, the knees will ache, and the stadium roar will be a distant memory.

What will remain is the relationship he built with his father Bryan.

Too many sports parents destroy their relationship with their children over junior tournaments that nobody remembers ten years later. Bryan kept the relationship sacred.

Fathers: Protect your bond with your child. The scoreboard is temporary; fatherhood is eternal.

👉 Read *Survival Skills for Men* by Lornette Daye ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 39,
        "slot": "Saturday Evening (6:00 PM MDT)",
        "dueAt": "2026-09-27T00:00:00.000Z",
        "assetFile": "parents-9.png",
        "assetUrl": f"{CDN_BASE}/parents-9.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""THE MOTHERS WHO NEVER GAVE UP: CELEBRATING TAMAKI OSAKA 🌸👑

As we approach the finale of our 2-week campaign, we honor Tamaki Osaka once again.

Her quiet perseverance on behalf of Naomi and Mari remains one of the most inspiring stories of modern sports motherhood. She didn't seek fame; she sought opportunity for her children.

To every parent fighting against heavy odds to give your children a better tomorrow: Stand firm. Your work is not in vain.

👉 Connect with Olympic coach Lornette Daye for inspiring keynote speaking: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 14: Sunday, Sep 27, 2026 (Grand Finale Drops across both families)
    {
        "id": 40,
        "slot": "Sunday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-27T14:30:00.000Z",
        "assetFile": "parents-1.png",
        "assetUrl": f"{CDN_BASE}/parents-1.png",
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""BEHIND EVERY CHAMPION: THE PARENTS WHO CARRIED THE DREAM 🏆❤️

Over the past 14 days, we have journeyed through two extraordinary stories:
- Bryan Shelton, who walked away from collegiate security to be his son’s father and coach on the world stage.
- Tamaki Osaka, who worked endless double shifts so her daughters could swing on public tennis courts.

The athlete might stand in the spotlight and lift the trophy. But the foundation was poured in the dark by parents who loved without condition and sacrificed without complaint.

Thank you to the parents, coaches, and sports mentors who make greatness possible.

👉 Book Lornette Daye for your sports organization's annual keynote: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 41,
        "slot": "Sunday Mid-day Encore (1:00 PM MDT)",
        "dueAt": "2026-09-27T19:00:00.000Z",
        "assetFile": "parents-10.png",
        "assetUrl": f"{CDN_BASE}/parents-10.png",
        "cta": "Complete Catalog & Speaking (lornettedaye.com)",
        "text": f"""THE ULTIMATE QUESTION FOR SPORTS PARENTS & COACHES ❓❤️

As we bring this 2-week campaign to a close, ask yourself this foundational question:

When your child or athlete hangs up their uniform for the final time, what will they remember most?

Will they remember the pressure and the anger over missed shots? Or will they remember your loving presence, your quiet sacrifice, and your steady hand on their shoulder?

Make sure your legacy as a parent or coach is built on love, character, and lifelong support.

👉 Explore Lornette Daye’s books and speaking offerings:
• Keynotes: lornettedaye.com/speaking
• Books ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 42,
        "slot": "Sunday Night Grand Finale (6:00 PM MDT)",
        "dueAt": "2026-09-28T00:00:00.000Z",
        "assetFile": "parents-5.png",
        "assetUrl": f"{CDN_BASE}/parents-5.png",
        "cta": "Speaking & Books (lornettedaye.com)",
        "text": f"""GRAND FINALE: HONOR THE FATHER. HONOR THE MOTHER. HONOR THE JOURNEY. 👑✨

Champions come and go. But the bonds of family, the lessons of discipline, and the love poured into a child endure for generations.

To Bryan Shelton, Tamaki Osaka, and millions of parents worldwide who sacrifice daily for their children’s dreams: We honor you.

From four decades of Olympic coaching, Lornette Daye salutes the true foundations behind the podium.

Higher, further, together.

👉 Book Lornette Daye for your school, club, or conference keynote: lornettedaye.com/speaking
👉 Explore the complete book collection ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    }
]

def schedule_post(post):
    query = """
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
    """

    variables = {
        "input": {
            "channelId": CHANNEL_ID,
            "text": post["text"],
            "mode": "customScheduled",
            "dueAt": post["dueAt"],
            "schedulingType": "automatic",
            "needsApproval": False,
            "saveToDraft": False,
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
    except Exception as e:
        return {"error": str(e)}

def main():
    print(f"Starting Buffer queue scheduling for Parents Set 1 Campaign (42 posts)...")
    print(f"Channel: {CHANNEL_ID}")
    print(f"Token: {TOKEN[:6]}...{TOKEN[-4:]}")
    print("-" * 60)

    results = []
    success_count = 0

    for idx, post in enumerate(posts_data, 1):
        print(f"[{idx}/42] Scheduling: Post #{post['id']} ({post['slot']}) - {post['dueAt']}...")
        resp = schedule_post(post)

        create_post_data = resp.get("data", {}).get("createPost", {})
        typename = create_post_data.get("__typename")
        post_obj = create_post_data.get("post")

        if typename == "PostActionSuccess" and post_obj and post_obj.get("id"):
            post_id = post_obj["id"]
            status = post_obj.get("status")
            due_at = post_obj.get("dueAt")
            print(f"   --> SUCCESS! Post ID: {post_id} | Status: {status} | Due: {due_at}")
            results.append({
                "id": post["id"],
                "slot": post["slot"],
                "dueAt": post["dueAt"],
                "bufferPostId": post_id,
                "status": status,
                "assetUrl": post["assetUrl"],
                "cta": post["cta"],
                "success": True
            })
            success_count += 1
        else:
            err_msg = create_post_data.get("message") or resp.get("errors") or resp.get("error") or str(resp)
            print(f"   --> FAILED: {err_msg}")
            results.append({
                "id": post["id"],
                "slot": post["slot"],
                "dueAt": post["dueAt"],
                "error": err_msg,
                "success": False
            })

        time.sleep(1.0)

    print("-" * 60)
    print(f"Parents Campaign Scheduling Complete: {success_count}/42 posts successfully placed into Buffer Scheduled Queue.")

    report_path = os.path.join(os.path.dirname(__file__), "parents-scheduled-report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump({
            "campaign": "Behind the Champion - Parents Set 1",
            "total_posts": len(posts_data),
            "successful_posts": success_count,
            "channelId": CHANNEL_ID,
            "scheduled_at": time.strftime("%Y-%m-%d %H:%M:%S"),
            "results": results
        }, f, indent=2)
    print(f"Report saved to {report_path}")

if __name__ == "__main__":
    main()
