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

CDN_BASE = 'https://lornettedaye.com/campaigns/japan-volleyball'

HASHTAGS = "#RyujinNIPPON #龍神NIPPON #JapanVolleyball #YukiIshikawa #RanTakahashi #YujiNishida #LA2028 #Olympics #Volleyball #AVC #AsianChampionship #OlympicMindset #LornetteDaye #HighPerformance #FinishStrong #SportsLeadership"

posts_data = [
    # =========================================================================
    # WEEK 1: OLYMPIC QUALIFICATION & THE CRUCIBLE OF PRESSURE (Sep 14 - Sep 20, 2026)
    # =========================================================================
    # DAY 1: Monday, Sep 14, 2026
    {
        "id": 1,
        "theme_arc": "Japan Going to LA 2028",
        "slot": "Monday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-14T14:30:00.000Z",
        "displayTime": "Monday, Sep 14, 2026 - 8:30 AM MDT",
        "assetFile": "japan-volleyball-going-to-la-01.png",
        "assetUrl": f"{CDN_BASE}/japan-volleyball-going-to-la-01.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": f"""その挑戦は、世界を動かす。JAPAN IS GOING TO LA 2028! 🇯🇵🏐🔥

Asian Men's Volleyball Championship Final: Japan 3 • Iran 1. The ticket to the Los Angeles 2028 Olympic Games is officially punched!

In over 40 years of coaching Olympic athletes and national championship contenders, I know the suffocating weight of an Olympic qualification match. You train for four years in cold gyms, through surgeries and heartbreak, all to have your entire Olympic dream decided in four sets.

When Ryujin Nippon (龍神NIPPON) stepped onto that floor against Iran, they didn't play not to lose. They attacked with furious precision, clinical floor defense, and unshakeable brotherhood.

That is the Olympic mindset: When the pressure peaks, your standards must rise higher than the moment.

Volleyball & Sports Fans: What went through your chest when Ishikawa, Nishida, and Ran locked arms at match point?

👉 Discover how elite competitors rise after crushing setbacks to seize their Olympic destiny. Read *Finish Strong: Chasing the Olympic Dream* by Lornette Daye ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 2,
        "theme_arc": "One Match, One Dream (Idomu)",
        "slot": "Monday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-14T23:00:00.000Z",
        "displayTime": "Monday, Sep 14, 2026 - 5:00 PM MDT",
        "assetFile": "japan-volleyball-one-match-dream-02.png",
        "assetUrl": f"{CDN_BASE}/japan-volleyball-one-match-dream-02.png",
        "cta": "Survival Skills for Athletes (lornettedaye.com/books)",
        "text": f"""挑む (IDOMU) — TO CHALLENGE. ONE MATCH. ONE OLYMPIC DREAM. 🏔️🏐⚡

Look at Yuki Ishikawa rising above the towering Iranian block. Mount Fuji behind him, the palm trees of Los Angeles on the horizon.

At this level of international competition, physical skill is only the price of entry. What separates champions when the score is tied 22-22 in the fourth set is psychological poise. The ability to slow down your heart rate, pick your spot past three sets of hands, and swing with pure conviction.

Japan delivered under maximum pressure and booked its place at LA 2028 because their mental training was as rigorous as their vertical leap.

Higher, further, together. Sport connects a brighter tomorrow.

How do you train your mind to stay composed when everything you've worked for is on the line?

👉 Build champion-level mental toughness, discipline, and competitive resilience. Order *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },

    # DAY 2: Tuesday, Sep 15, 2026
    {
        "id": 3,
        "theme_arc": "Qualified: The Dream Becomes Real",
        "slot": "Tuesday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-15T14:30:00.000Z",
        "displayTime": "Tuesday, Sep 15, 2026 - 8:30 AM MDT",
        "assetFile": "japan-volleyball-qualified-bound-03.png",
        "assetUrl": f"{CDN_BASE}/japan-volleyball-qualified-bound-03.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": f"""夢を、もっと先へ。QUALIFIED: JAPAN IS OFFICIALLY OLYMPIC-BOUND. 🇯🇵✨🏅

Look at the raw, unadulterated joy on the faces of Ishikawa, Nishida, and Ran Takahashi.

After beating Iran, the dream becomes real. But what fans see as an explosion of confetti and smiles is actually the release of thousands of unseen hours of agony, self-doubt, and relentless sacrifice.

As an Olympic coach, I have stood in locker rooms where athletes wept because they missed qualification by a single point. And I have stood with those who crossed the threshold into history.

The difference isn't talent; it is the refusal to surrender when the process demands more of you than you thought you had to give.

Japan to the world. Higher together for a brighter tomorrow.

What goal are you chasing today that demands you push your dream further ahead?

👉 Read the inspiring true story of Olympic perseverance, identity, and rising after defeat. *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 4,
        "theme_arc": "Home Crowd Voltage",
        "slot": "Tuesday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-15T23:00:00.000Z",
        "displayTime": "Tuesday, Sep 15, 2026 - 5:00 PM MDT",
        "assetFile": "japan-volleyball-home-crowd-moment-04.png",
        "assetUrl": f"{CDN_BASE}/japan-volleyball-home-crowd-moment-04.png",
        "cta": "Survival Skills for Men (lornettedaye.com/books)",
        "text": f"""HOME CROWD. HUGE MOMENT. 世界へ、再び (TO THE WORLD, ONCE AGAIN). 🏟️🇯🇵❤️

ありがとう、日本！ (Thank you, Japan!)

When 15,000 fans in the arena and millions across the nation are living on every spike, dig, and serve, pressure can either crush you or elevate you into an unstoppable flow state.

Look at Yuji Nishida and Masahiro Sekita embracing their captain. In men's high-performance sports, true strength is not isolated individualism; it is the brotherhood that allows men to lean on each other when the burden feels too heavy to bear alone.

Brotherhood multiplies courage. Trust eliminates hesitation.

Gentlemen & Leaders: Who are the men in your corner who give you strength when the stakes are highest?

👉 Cultivate resilience, emotional balance, and purposeful leadership. Read *Survival Skills for Men* by Lornette Daye ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },

    # DAY 3: Wednesday, Sep 16, 2026
    {
        "id": 5,
        "theme_arc": "Precision Over Power (Japan 3 - Iran 1)",
        "slot": "Wednesday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-16T14:30:00.000Z",
        "displayTime": "Wednesday, Sep 16, 2026 - 8:30 AM MDT",
        "assetFile": "japan-volleyball-defeats-iran-05.png",
        "assetUrl": f"{CDN_BASE}/japan-volleyball-defeats-iran-05.png",
        "cta": "Survival Skills for Athletes (lornettedaye.com/books)",
        "text": f"""JAPAN 3 • IRAN 1: OUT-EXECUTING POWER THROUGH SURGICAL PRECISION. 🎯🏐💥

AVC Asian Championship Final. Champions qualify for Los Angeles 2028.

Iran brought immense physical height, intimidating power at the net, and continental prestige. But Japan answered with something far more lethal: surgical precision, lightning-fast transition sets from Sekita, and relentless defensive ground coverage.

In athletics and executive business alike, you do not beat a bigger, well-funded rival by trying to play their game. You beat them by mastering your own identity, out-working them in the transitions, and refusing to give away unforced errors.

Precision beats power. Discipline beats size.

Are you playing your competitor's game, or are you enforcing your own high-precision system?

👉 Master the high-performance mental edge that allows underdog competitors to dominate. Order *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 6,
        "theme_arc": "Pressure. Poise. Japan.",
        "slot": "Wednesday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-16T23:00:00.000Z",
        "displayTime": "Wednesday, Sep 16, 2026 - 5:00 PM MDT",
        "assetFile": "japan-volleyball-pressure-poise-06.png",
        "assetUrl": f"{CDN_BASE}/japan-volleyball-pressure-poise-06.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""PRESSURE. POISE. JAPAN. WHEN THE MOMENT CAME, THEY DELIVERED. ⚡🇯🇵🏅

その先の、夢へ。 (Beyond that, toward the dream.)

Look into the eyes of Yuki Ishikawa. That is not the look of an athlete hoping to win. That is the look of a captain who has accepted the full weight of his responsibility and converted it into calm, lethal focus.

When a team falls into a 0-1 set deficit or faces set points against them, the sideline doesn't look at the scoreboard; they look at their leader's face. If the leader panics, the team unravels. If the leader radiates quiet composure, belief ignites.

True leadership is emotional poise under fire.

👉 Bring four decades of Olympic coaching wisdom to your organization. Book Lornette Daye for your corporate keynote or athletic department conference on Poise Under Pressure: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 4: Thursday, Sep 17, 2026
    {
        "id": 7,
        "theme_arc": "Road to LA 2028",
        "slot": "Thursday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-17T14:30:00.000Z",
        "displayTime": "Thursday, Sep 17, 2026 - 8:30 AM MDT",
        "assetFile": "japan-volleyball-road-to-la-07.png",
        "assetUrl": f"{CDN_BASE}/japan-volleyball-road-to-la-07.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": f"""ROAD TO LA 2028: A HIGHER STAGE AWAITS. 🌴☀️🏅

From Asia to a Brighter Tomorrow. Japan takes the next monumental step.

Qualifying for the Olympic Games is a mountaintop moment. But true champions know that reaching the base camp of the Olympics is merely where the real climb begins.

Between now and Los Angeles 2028 lie thousands of hours of conditioning, international VNL tours, tactical adjustments, and physical recovery protocols. The teams that celebrate too long after qualifying get left behind on the Olympic podium.

Greatness is not a destination. It is the perpetual daily commitment to push your standard higher.

How do you reset your hunger after achieving a major milestone?

👉 Keep your fire burning through long, demanding seasons of growth. Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 8,
        "theme_arc": "Champions at Home & Brotherhood",
        "slot": "Thursday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-17T23:00:00.000Z",
        "displayTime": "Thursday, Sep 17, 2026 - 5:00 PM MDT",
        "assetFile": "japan-volleyball-champions-at-home-08.png",
        "assetUrl": f"{CDN_BASE}/japan-volleyball-champions-at-home-08.png",
        "cta": "Survival Skills for Men (lornettedaye.com/books)",
        "text": f"""CHAMPIONS AT HOME: JAPAN WINS THE BIG MOMENT. 🏆🇯🇵✨

Lifting the AVC Asian Championship trophy in front of home supporters with gold medals around their necks.

Look closely at the body language of these men: arms wrapped tightly around each other, heads thrown back in uninhibited celebration. In a world that often teaches men to guard their emotions and compete in isolation, high-performance sport teaches the exact opposite:

The greatest masculine power is found in complete, unreserved commitment to the brotherhood beside you. When you trust your brother to cover your back, you can throw yourself completely into the fight.

More than a game. A brighter tomorrow together.

👉 Strengthen your emotional resilience, purpose, and brotherhood. Order *Survival Skills for Men* by Lornette Daye ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },

    # DAY 5: Friday, Sep 18, 2026
    {
        "id": 9,
        "theme_arc": "Yamamoto's Floor Defense: What A Match",
        "slot": "Friday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-18T14:30:00.000Z",
        "displayTime": "Friday, Sep 18, 2026 - 8:30 AM MDT",
        "assetFile": "japan-volleyball-what-a-match-09.png",
        "assetUrl": f"{CDN_BASE}/japan-volleyball-what-a-match-09.png",
        "cta": "Survival Skills for Athletes (lornettedaye.com/books)",
        "text": f"""WHAT A MATCH! THIS IS WHY WE LOVE SPORT. 🏐🌊💥

Look at Tomohiro Yamamoto diving parallel to the floor, fingers scraping the taraflex to pop up a 120 km/h spike. Look at Ishikawa timing his approach in mid-air above the net.

Spikes get the highlights on social media, but defense wins Olympic berths.

When an athlete is willing to throw their body across hardwood and take the bruises so their teammate can score the point, that is when a team ceases to be six individuals and becomes a unified organism.

Selfless sacrifice creates unstoppable momentum.

Friday Question: What unglamorous, defensive dirty-work are you doing for your team today?

👉 Master the daily discipline and champion mindset of elite performers. Read *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 10,
        "theme_arc": "They Delivered: From Asia to L.A.",
        "slot": "Friday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-18T23:00:00.000Z",
        "displayTime": "Friday, Sep 18, 2026 - 5:00 PM MDT",
        "assetFile": "japan-volleyball-they-delivered-10.png",
        "assetUrl": f"{CDN_BASE}/japan-volleyball-they-delivered-10.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": f"""THEY DELIVERED. JAPAN'S MEN ARE OLYMPIC-BOUND. 🇯🇵🌟🌴

A huge win over Iran. A dream realized. From Asia to L.A. 2028.

Talk is cheap in professional athletics. Every team claims they are working hard. Every coach talks about culture during pre-season press conferences.

But when the lights burn white-hot, when Iran is charging back, and when the entire gymnasium is screaming on edge—can you deliver?

Ryujin Nippon answered that question with thunderous clarity: YES. THEY DELIVERED.

Deliver on your promises. Honor your preparation. Finish strong.

👉 Step boldly into your own Olympic moment. Read *Finish Strong: Chasing the Olympic Dream* by Lornette Daye ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },

    # DAY 6: Saturday, Sep 19, 2026
    {
        "id": 11,
        "theme_arc": "Nishida & Ishikawa Synergy",
        "slot": "Saturday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-19T14:30:00.000Z",
        "displayTime": "Saturday, Sep 19, 2026 - 8:30 AM MDT",
        "assetFile": "japan-volleyball-going-to-la-01.png",
        "assetUrl": f"{CDN_BASE}/japan-volleyball-going-to-la-01.png",
        "cta": "Survival Skills for Athletes (lornettedaye.com/books)",
        "text": f"""SATURDAY HIGH PERFORMANCE: THE LETHAL SYNCHRONICITY OF NISHIDA & ISHIKAWA. ⚡🏐🔥

When you examine Japan's offensive architecture, notice the complementary genius between Yuki Ishikawa and Yuji Nishida.

Ishikawa brings calculated elegance, tactical shot selection, and ice-cold captaincy. Nishida brings raw volcanic emotion, explosive left-handed velocity, and an energy that electrifies the building.

Championship teams do not require identical personalities. They require complementary strengths anchored by mutual respect and a common standard of excellence.

Does your leadership team celebrate diverse styles, or are you trying to force everyone into the exact same mold?

👉 Unlock peak team dynamics and individual athletic brilliance. Read *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 12,
        "theme_arc": "Managing Expectations on Global Stage",
        "slot": "Saturday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-19T23:00:00.000Z",
        "displayTime": "Saturday, Sep 19, 2026 - 5:00 PM MDT",
        "assetFile": "japan-volleyball-one-match-dream-02.png",
        "assetUrl": f"{CDN_BASE}/japan-volleyball-one-match-dream-02.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": f"""MANAGING THE WEIGHT OF GLOBAL ADORATION. 🌏🏐✨

Ryujin Nippon is not just a sports team—they are a global cultural phenomenon. From sold-out arenas in Manila and Gdansk to massive crowds in Tokyo, millions of fans follow their every movement.

With that level of adoration comes immense psychological gravity. Young athletes can easily get seduced by social media followers and commercial endorsements, losing the edge that made them great.

What keeps Ishikawa and Ran Takahashi grounded is an Olympic coach's greatest asset: uncompromising reverence for the craft. They practice like unranked walk-ons even when the world treats them like rock stars.

Stay humble in victory. Stay hungry in preparation.

👉 Ground your identity in purpose rather than fleeting applause. Order *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },

    # DAY 7: Sunday, Sep 20, 2026 (Film Session & Reset)
    {
        "id": 13,
        "theme_arc": "Sunday Film Study: The Crunch-Time Digs",
        "slot": "Sunday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-20T14:30:00.000Z",
        "displayTime": "Sunday, Sep 20, 2026 - 8:30 AM MDT",
        "assetFile": "japan-volleyball-qualified-bound-03.png",
        "assetUrl": f"{CDN_BASE}/japan-volleyball-qualified-bound-03.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""SUNDAY OLYMPIC FILM STUDY: DISSECTING THE MOMENTS THAT BROKE IRAN. 📽️🏐🔍

Sunday morning in elite athletics is for the tape.

When you rewind the tape of Japan's 3-1 victory over Iran, you see the turning point wasn't a highlight spike; it was three consecutive scramble digs in the third set when Iran had all the momentum.

Japan didn't panic. They communicated with two-word cues, reset their defensive perimeter, and forced Iran into attacking errors.

Games are won in the micro-moments when fatigue is whispering excuses in your ear and you choose discipline instead.

Are you studying your own film to find the micro-adjustments that unlock victory?

👉 Bring Olympic Coach Lornette Daye to your leadership summit to analyze Championship Decision-Making & Crunch-Time Execution: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 14,
        "theme_arc": "Weekly Reset: When Pride Unites a Nation",
        "slot": "Sunday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-20T23:00:00.000Z",
        "displayTime": "Sunday, Sep 20, 2026 - 5:00 PM MDT",
        "assetFile": "japan-volleyball-home-crowd-moment-04.png",
        "assetUrl": f"{CDN_BASE}/japan-volleyball-home-crowd-moment-04.png",
        "cta": "Survival Skills for Men (lornettedaye.com/books)",
        "text": f"""WEEK 1 IN THE BOOKS: WHEN PRIDE UNITES AN ENTIRE NATION. 🇯🇵🌅✨

As we close out Week 1 of our Japan Men's Volleyball Olympic tribute, look at the sea of red and white flags in the arena.

When athletes play for something larger than their personal contracts or individual statistics—when they carry the honor of their country and the pride of millions—their stamina deepens. Purpose is the only fuel that outlasts physical exhaustion.

Find your 'Why.' Anchor your work to a purpose that cannot be shaken by temporary setbacks.

Rest well tonight. Tomorrow morning, Week 2 begins.

👉 Build unshakeable purpose and resilience through every chapter of life. Get *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },

    # =========================================================================
    # WEEK 2: MENTAL TOUGHNESS & SUSTAINED OLYMPIC DRIVE (Sep 21 - Sep 27, 2026)
    # =========================================================================
    # DAY 8: Monday, Sep 21, 2026
    {
        "id": 15,
        "theme_arc": "Psychology of Overcoming Rivals",
        "slot": "Monday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-21T14:30:00.000Z",
        "displayTime": "Monday, Sep 21, 2026 - 8:30 AM MDT",
        "assetFile": "japan-volleyball-defeats-iran-05.png",
        "assetUrl": f"{CDN_BASE}/japan-volleyball-defeats-iran-05.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": f"""WEEK 2 KICKOFF: THE PSYCHOLOGY OF OVERCOMING HISTORIC RIVALS. ⚔️🏐🧠

For over a decade, Iran was the gold standard of Asian volleyball—dominant, physically imposing, and mentally ruthless.

To defeat a rival that has historically dominated you, you cannot simply improve your physical strength; you must dismantle the psychological pedestal you placed them on.

Japan stopped viewing Iran as a mountain to fear and started treating them as a puzzle to solve. When you replace fear with curiosity and tactical discipline, giants fall.

What 'giant' in your industry or personal life have you placed on an untouchable pedestal?

👉 Break through mental limits and claim your victory. Order *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 16,
        "theme_arc": "Heart Rate Control at 24-24",
        "slot": "Monday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-21T23:00:00.000Z",
        "displayTime": "Monday, Sep 21, 2026 - 5:00 PM MDT",
        "assetFile": "japan-volleyball-pressure-poise-06.png",
        "assetUrl": f"{CDN_BASE}/japan-volleyball-pressure-poise-06.png",
        "cta": "Survival Skills for Athletes (lornettedaye.com/books)",
        "text": f"""CONTROLLING HEART RATE AT 24-24 IN THE FOURTH SET. 💓🏐🧘‍♂️

Imagine standing on the service line. The score is 24-24. If you miss, your opponent has championship point. If you ace, your country is one ball away from the Olympic Games.

Your chest is pounding, your palms are sweaty, and 15,000 people are holding their breath.

Elite athletes don't eliminate nervousness—they master it. They use autonomic breathing techniques to lower cortisol, visualize the flight path of the ball, and trust their muscle memory.

Pressure is merely physiological arousal. You choose whether to interpret it as panic or readiness.

How do you breathe and recalibrate when high stakes threaten your composure?

👉 Master breathwork, cognitive focus, and pressure management with *Survival Skills for Athletes* by Lornette Daye ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },

    # DAY 9: Tuesday, Sep 22, 2026
    {
        "id": 17,
        "theme_arc": "Continental Dominance to Olympic Gold",
        "slot": "Tuesday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-22T14:30:00.000Z",
        "displayTime": "Tuesday, Sep 22, 2026 - 8:30 AM MDT",
        "assetFile": "japan-volleyball-road-to-la-07.png",
        "assetUrl": f"{CDN_BASE}/japan-volleyball-road-to-la-07.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": f"""FROM ASIAN CHAMPIONS TO OLYMPIC GOLD CONTENDERS. 🥇🌏🌴

Winning the AVC Championship proves Japan is the undisputed king of Asian volleyball. But the vision of this squad reaches far beyond continental trophies.

They want the top step of the podium in Los Angeles 2028.

To bridge the gap between regional dominance and Olympic gold, an organization must continually raise the bar on its internal metrics. What was good enough to beat Iran will not be enough to beat Poland, France, or the USA in an Olympic semi-final.

Never benchmark yourself against where you are today. Benchmark yourself against the champion you are called to become.

What higher standard do you need to adopt this week?

👉 Elevate your standards and chase your highest dreams. Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 18,
        "theme_arc": "Vulnerability and Strength",
        "slot": "Tuesday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-22T23:00:00.000Z",
        "displayTime": "Tuesday, Sep 22, 2026 - 5:00 PM MDT",
        "assetFile": "japan-volleyball-champions-at-home-08.png",
        "assetUrl": f"{CDN_BASE}/japan-volleyball-champions-at-home-08.png",
        "cta": "Survival Skills for Men (lornettedaye.com/books)",
        "text": f"""VULNERABILITY AND STRENGTH: WHY CHAMPION MEN WEEP TEARS OF JOY. 💧🏆❤️

Look at the emotion when the final whistle blew. Hardened elite athletes falling to their knees, weeping openly, and embracing their brothers.

Tears of joy are not weakness. They are the undeniable evidence of how deeply these men cared. They gave every ounce of their physical, mental, and emotional capacity to the mission.

When a man commits to something with that level of fierce vulnerability, cynicism dies. Passion takes over.

Gentlemen: When was the last time you cared about a mission so deeply that it moved your soul?

👉 Reconnect with passion, integrity, and unyielding strength. Order *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },

    # DAY 10: Wednesday, Sep 23, 2026
    {
        "id": 19,
        "theme_arc": "The Grittiest Plays Define Championships",
        "slot": "Wednesday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-23T14:30:00.000Z",
        "displayTime": "Wednesday, Sep 23, 2026 - 8:30 AM MDT",
        "assetFile": "japan-volleyball-what-a-match-09.png",
        "assetUrl": f"{CDN_BASE}/japan-volleyball-what-a-match-09.png",
        "cta": "Survival Skills for Athletes (lornettedaye.com/books)",
        "text": f"""THE ART OF THE PANCAKE DIG: WHY THE GRITTIEST PLAYS DEFINE TITLES. 🥞🏐🛡️

In volleyball, a 'pancake' is when a defender slides their palm flat on the floor split seconds before the ball impacts the ground, letting the leather bounce off the back of the hand.

It requires complete disregard for personal safety, instantaneous reaction time, and absolute trust that your teammate will be there to set the ricochet.

Championships are not won on polished speeches or clean plays. Championships are won when players are willing to get their knees scraped and dive into the floor when everyone else has given up on the point.

Are you willing to make the uncomfortable, gritty effort that keeps your project alive?

👉 Build champion grit and competitive focus. Read *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 20,
        "theme_arc": "40 Years of Olympic Coaching Wisdom",
        "slot": "Wednesday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-23T23:00:00.000Z",
        "displayTime": "Wednesday, Sep 23, 2026 - 5:00 PM MDT",
        "assetFile": "japan-volleyball-they-delivered-10.png",
        "assetUrl": f"{CDN_BASE}/japan-volleyball-they-delivered-10.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""40 YEARS OF OLYMPIC COACHING WISDOM: QUALIFIED TEAMS VS PODIUM FINISHERS. 🏅⏱️📜

Having coached at the highest international level for over four decades, I can tell you what separates teams that merely participate in the Olympics from those who bring home medals:

It is the culture they maintain when the cameras leave.

The qualifying euphoria fades within 48 hours. What remains is the relentless grind of technical repetition, film study, and emotional accountability.

Podium teams fall in love with the unglamorous daily curriculum of excellence.

Does your organization possess the stamina to turn initial qualification into enduring greatness?

👉 Book Olympic Coach Lornette Daye for your corporate keynote or athletic department conference: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 11: Thursday, Sep 24, 2026
    {
        "id": 21,
        "theme_arc": "Ran Takahashi's Evolution",
        "slot": "Thursday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-24T14:30:00.000Z",
        "displayTime": "Thursday, Sep 24, 2026 - 8:30 AM MDT",
        "assetFile": "japan-volleyball-going-to-la-01.png",
        "assetUrl": f"{CDN_BASE}/japan-volleyball-going-to-la-01.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": f"""RAN TAKAHASHI'S EVOLUTION: BALANCING STARDOM WITH RELENTLESS RIGOR. 🌟🏐🚀

At just 25 years old, Ran Takahashi is a global sporting icon. But behind the commercial fame in Italy and Japan lies one of the most disciplined backcourt passers and pipe-attackers in world volleyball.

When young leaders experience massive acclaim early in their careers, the danger of complacency is enormous.

What makes Ran extraordinary is his work ethic. In every drill, he dives with the hunger of a player fighting for a roster spot. He understands that your brand is only as strong as your daily output.

Never let your fame outgrow your work ethic.

👉 Learn how to navigate early pressure and stay locked into your purpose. Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 22,
        "theme_arc": "Taking Dreams Further (Yume o, Motto Saki e)",
        "slot": "Thursday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-24T23:00:00.000Z",
        "displayTime": "Thursday, Sep 24, 2026 - 5:00 PM MDT",
        "assetFile": "japan-volleyball-one-match-dream-02.png",
        "assetUrl": f"{CDN_BASE}/japan-volleyball-one-match-dream-02.png",
        "cta": "Survival Skills for Athletes (lornettedaye.com/books)",
        "text": f"""夢を、もっと先へ (TAKING DREAMS FURTHER): THE UNYIELDING SPIRIT OF RYUJIN NIPPON. 🇯🇵🔥🏐

When Japanese volleyball was struggling a decade ago, skeptics said Asian teams could no longer compete with the physical height of European powerhouses.

Ryujin Nippon refused that narrative. They revolutionized the game with faster tempo, pipe sets from the back row, and unmatched floor defense.

They didn't just qualify for LA 2028—they redefined how the sport of volleyball is played worldwide.

Never let small-minded critics tell you what is impossible in your field. Reinvent the game and take your dream further.

What conventional wisdom are you ready to shatter in your industry?

👉 Build the mindset of an innovator and world-class competitor. Order *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },

    # DAY 12: Friday, Sep 25, 2026
    {
        "id": 23,
        "theme_arc": "When Skeptics Said You Were Too Small",
        "slot": "Friday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-25T14:30:00.000Z",
        "displayTime": "Friday, Sep 25, 2026 - 8:30 AM MDT",
        "assetFile": "japan-volleyball-qualified-bound-03.png",
        "assetUrl": f"{CDN_BASE}/japan-volleyball-qualified-bound-03.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": f"""FRIDAY REFLECTION: WHEN THEY SAID YOU WERE TOO SMALL, OUT-JUMP THEM. 🚀🏐✨

On paper, volleyball is a sport designed for giants. The Iranian roster towered over Japan by several inches at almost every position.

But vertical jumping power, approach speed, and timing are the great equalizers. Yuji Nishida stands 6'1" and touches nearly 11'6" in the air with a 40-inch vertical, hitting over triple blocks with jaw-dropping ferocity.

Do not allow disadvantages on paper to dictate your ceiling in reality. Develop your unique edge until it outshines what the opposition was born with.

What is your unique competitive advantage that makes size irrelevant?

👉 Turn disadvantages into your greatest strengths. Read *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 24,
        "theme_arc": "Channeling Collective Energy",
        "slot": "Friday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-25T23:00:00.000Z",
        "displayTime": "Friday, Sep 25, 2026 - 5:00 PM MDT",
        "assetFile": "japan-volleyball-home-crowd-moment-04.png",
        "assetUrl": f"{CDN_BASE}/japan-volleyball-home-crowd-moment-04.png",
        "cta": "Survival Skills for Men (lornettedaye.com/books)",
        "text": f"""THE SOUND OF 15,000 FANS HOLDING THEIR BREATH. 🏟️🤫⚡

There is a sacred quiet in a stadium right before a serve on match point. 15,000 people silent in prayer and anticipation.

In those seconds, an athlete can either feel suffocated by the tension or fueled by the collective love and hope of the crowd.

Japan channeled that voltage into clean, decisive execution. They didn't shrink; they expanded to meet the moment.

When pressure surrounds you this weekend, don't run from it. Breathe it in and let it fuel your focus.

A brighter tomorrow through sport.

👉 Master emotional stability, mental focus, and purposeful living. Read *Survival Skills for Men* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },

    # DAY 13: Saturday, Sep 26, 2026
    {
        "id": 25,
        "theme_arc": "Sekita's Deceptive Setting",
        "slot": "Saturday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-26T14:30:00.000Z",
        "displayTime": "Saturday, Sep 26, 2026 - 8:30 AM MDT",
        "assetFile": "japan-volleyball-defeats-iran-05.png",
        "assetUrl": f"{CDN_BASE}/japan-volleyball-defeats-iran-05.png",
        "cta": "Survival Skills for Athletes (lornettedaye.com/books)",
        "text": f"""TACTICAL MASTERY: HOW MASAHIRO SEKITA DISMANTLED TALL BLOCKERS. 🧠🏐🎯

Look at setter Masahiro Sekita (#6). In a sport dominated by 6'6" setters, Sekita stands at 5'9"—and he is widely regarded as one of the top three setters in world volleyball.

Why? Because his hands are invisible. He holds the ball to the microsecond before release, looking off middle blockers and distributing passes with millimeter accuracy.

When you master the art of deceptive execution and strategic distribution, you make your entire team look twice as dangerous as they are.

Are you distributing opportunity effectively across your team, or are you predictable in your leadership?

👉 Elevate your tactical intelligence and high-performance habits. Order *Survival Skills for Athletes* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 26,
        "theme_arc": "The Unbroken Chain of Trust",
        "slot": "Saturday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-26T23:00:00.000Z",
        "displayTime": "Saturday, Sep 26, 2026 - 5:00 PM MDT",
        "assetFile": "japan-volleyball-pressure-poise-06.png",
        "assetUrl": f"{CDN_BASE}/japan-volleyball-pressure-poise-06.png",
        "cta": "Keynote Speaking (lornettedaye.com/speaking)",
        "text": f"""THE UNBROKEN CHAIN: HOW MUTUAL TRUST ELIMINATES HESITATION. 🔗🤝⚡

In volleyball, every touch is restricted to a fraction of a second. You cannot carry the ball, hold it, or take time to deliberate.

The passer must trust the setter. The setter must trust the hitter. The hitter must trust that if their spike is dug, the back row will cover them.

If a single link in that chain second-guesses their teammate for even half a heartbeat, the point is lost.

High-performance teams do not move at the speed of technology; they move at the speed of trust.

How are you strengthening the chain of trust within your executive team?

👉 Bring world-class team dynamics and culture coaching to your organization. Keynotes & leadership summits: lornettedaye.com/speaking

{HASHTAGS}"""
    },

    # DAY 14: Sunday, Sep 27, 2026 (Grand Finale)
    {
        "id": 27,
        "theme_arc": "The Daily Grind of Olympic Cycles",
        "slot": "Sunday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-27T14:30:00.000Z",
        "displayTime": "Sunday, Sep 27, 2026 - 8:30 AM MDT",
        "assetFile": "japan-volleyball-road-to-la-07.png",
        "assetUrl": f"{CDN_BASE}/japan-volleyball-road-to-la-07.png",
        "cta": "Finish Strong Book (lornettedaye.com/books)",
        "text": f"""THE COUNTDOWN TO LA 2028 BEGINS TODAY. ⏳🌴🏅

The Asian Championship trophy is in the cabinet. The Olympic berth is secured.

Starting tomorrow morning, the slate is wiped clean.

Between today and the Opening Ceremony in Los Angeles, Ryujin Nippon will jump hundreds of thousands of times. They will analyze miles of video. They will endure grueling road trips across continents.

Greatness requires the willingness to fall back in love with the unglamorous daily routine long after the initial applause has faded.

Whatever your arena, stay in love with the work. Finish strong.

👉 Re-anchor your long-term vision and finish your journey with pride. Order *Finish Strong: Chasing the Olympic Dream* ($14.99 CAD): lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 28,
        "theme_arc": "Grand Finale: The Spirit of Ryujin Nippon",
        "slot": "Sunday Evening (5:00 PM MDT)",
        "dueAt": "2026-09-27T23:00:00.000Z",
        "displayTime": "Sunday, Sep 27, 2026 - 5:00 PM MDT",
        "assetFile": "japan-volleyball-they-delivered-10.png",
        "assetUrl": f"{CDN_BASE}/japan-volleyball-they-delivered-10.png",
        "cta": "Complete Catalog & Speaking (lornettedaye.com/books)",
        "text": f"""GRAND FINALE: BEYOND THE GAME — THE SPIRIT OF RYUJIN NIPPON INSPIRING THE WORLD. 🇯🇵✨🏆

Japan 3 • Iran 1. Qualified. Olympic-bound.

This victory is bigger than sports. It is a testament to the power of human dedication, humble collaboration, and relentless courage.

To Ishikawa, Nishida, Ran, Sekita, Yamamoto, and the entire Japanese national squad: Thank you for showing the world what it means to dare, to unite, and to deliver under pressure.

その挑戦は、世界を動かす。 (The challenge moves the world.)

To every reader pursuing an ambitious goal in business, athletics, or life: Keep fighting. Hold your standard. Honor your brothers and sisters. Finish strong.

👉 Book Lornette Daye for your next conference keynote: lornettedaye.com/speaking
👉 Explore the official digital book catalog (*Finish Strong*, *Survival Skills for Athletes*, *Survival Skills for Men*, $14.99 CAD each): lornettedaye.com/books

#RyujinNIPPON #龍神NIPPON #JapanVolleyball #YukiIshikawa #RanTakahashi #YujiNishida #LA2028 #Olympics #Volleyball #AVC #AsianChampionship #FinishStrong #LornetteDaye #LeadershipExcellence #OlympicCoach"""
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
    print("🏐 LORNETTE DAYE - 2-WEEK JAPAN MEN'S VOLLEYBALL CAMPAIGN SCHEDULER")
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

    report_path = os.path.join(os.path.dirname(__file__), "japan-volleyball-scheduled-report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("------------------------------------------------------")
    print(f"🎉 Japan Volleyball Campaign Report saved to {report_path}")
    successful = sum(1 for r in results if r.get("status") == "scheduled")
    print(f"Summary: {successful}/{len(posts_data)} posts scheduled in Buffer Scheduled Queue.")
    print("------------------------------------------------------")

if __name__ == "__main__":
    main()
