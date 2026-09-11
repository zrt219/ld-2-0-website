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

CDN_BASE = 'https://lornettedaye.com/campaigns/como-win'

HASHTAGS = "#Como1907 #SemmCumasch #Lariani #NelNomeDiComo #StadioSinigaglia #InEuropa #ForzaComo #Calcio #SerieA #UCL #ChampionsLeague #UEFAChampionsLeague #CescFabregas #AssaneDiao #MaximoPerrone #RBLeipzig #CalcioItaliano #LornetteDaye #HighPerformance #ChampionMindset #Leadership"

posts_data = [
    # =========================================================================
    # PHASE 1: TONIGHT'S VICTORY CELEBRATION (Thursday Night, Sep 10, 2026)
    # =========================================================================
    {
        "id": 1,
        "theme_arc": "Thursday Victory Launch",
        "slot": "Tonight (9:25 PM MDT)",
        "dueAt": "2026-09-11T03:25:00.000Z",
        "displayTime": "Thursday, Sep 10, 2026 - 9:25 PM MDT",
        "assetFile": "como-img-01-fulltime.png",
        "assetUrl": f"{CDN_BASE}/como-img-01-fulltime.png",
        "isVideo": False,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""*SEMM CUMASCH!* 💙⚽🔥

Full-time at Stadio Sinigaglia: Como 1907 4, RB Leipzig 1. European nights on the shores of Lake Como just wrote history!

To watch a club climb from Serie D to dismantling a European powerhouse in the UEFA Champions League is a clinic in culture, belief, and relentless tactical discipline. Cesc Fàbregas and his squad proved tonight that pedigree doesn't dictate destiny—preparation does.

Fan Question: Where were you watching from tonight when the fourth goal hit the net, and what was your raw reaction? Drop your city below! 👇

When underdogs refuse to accept limitations, they redefine what is possible in world football.

👉 Discover the psychological blueprints of champions who rise from obscurity to dominate on the world stage: lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 2,
        "theme_arc": "Thursday Victory Launch",
        "slot": "Tonight (10:05 PM MDT)",
        "dueAt": "2026-09-11T04:05:00.000Z",
        "displayTime": "Thursday, Sep 10, 2026 - 10:05 PM MDT",
        "assetFile": "como-vid-02-goal.mp4",
        "assetUrl": f"{CDN_BASE}/como-vid-02-goal.mp4",
        "isVideo": True,
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""The pace. The movement. The ice in the veins. ⚡🎥⚽

Watch the build-up and the ruthless finish that put Como 3-0 up against RB Leipzig. This wasn't luck—this was four-phase positional precision executed at maximum intensity under the brightest European lights.

Fan Question: Was Assane Diao's composure on this strike the defining moment of the match? Let me know your favorite play from tonight!

In 40+ years coaching Olympic champions, I always teach: *Under pressure, you don't rise to the occasion; you sink to the level of your training.* Como trained to win.

👉 Transform your team's collective composure under elite pressure. Book Olympian Coach Lornette Daye for your corporate keynote: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 3,
        "theme_arc": "Thursday Victory Launch",
        "slot": "Tonight (10:55 PM MDT)",
        "dueAt": "2026-09-11T04:55:00.000Z",
        "displayTime": "Thursday, Sep 10, 2026 - 10:55 PM MDT",
        "assetFile": "como-vid-04-cbs-interview.mp4",
        "assetUrl": f"{CDN_BASE}/como-vid-04-cbs-interview.mp4",
        "isVideo": True,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""When football royalty stops to applaud. 🎙️👑

Thierry Henry, Jamie Carragher, and Micah Richards had nothing but awe on CBS Sports Golazo as Cesc Fàbregas broke down Como's tactical masterclass following their 4-1 triumph.

Notice how Cesc speaks about his players—not about ego, but about shared sacrifice, clarity of role, and unwavering belief in the project. *La nostra gente. Più di una squadra.*

Fan Question: How high can Como fly in this Champions League campaign? Next stop: Barcelona! Are they ready to stun Spain?

👉 Build an unbreakable culture of shared purpose across your organization. Read *Survival Skills for Believers*: lornettedaye.com/books

{HASHTAGS}"""
    },

    # =========================================================================
    # PHASE 2: 7-DAY SPRINT (Friday Sep 11 – Thursday Sep 17, 2026)
    # =========================================================================

    # --- DAY 1: Friday, Sep 11, 2026 ---
    {
        "id": 4,
        "theme_arc": "European Shockwave",
        "slot": "Friday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-11T14:30:00.000Z",
        "displayTime": "Friday, Sep 11, 2026 - 8:30 AM MDT",
        "assetFile": "como-vid-01-anthem.mp4",
        "assetUrl": f"{CDN_BASE}/como-vid-01-anthem.mp4",
        "isVideo": True,
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""Goosebumps across Lake Como. 🎵🏟️💙

The iconic UEFA Champions League anthem blaring through Stadio Giuseppe Sinigaglia as the Curva unveiled the massive *COMO* tifo. Morning after, and Lombardy is still dreaming awake!

*Lariani nel mondo. Una passione senza confini.* When an entire community pours its soul into a team, the stadium turns into an impenetrable fortress.

Fan Question: Did you ever imagine five years ago that Champions League football would be echoing across Lake Como?

👉 Inspire your workforce with the audacity to build championship environments from the ground up. Book Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 5,
        "theme_arc": "European Shockwave",
        "slot": "Friday Midday (12:30 PM MDT)",
        "dueAt": "2026-09-11T18:30:00.000Z",
        "displayTime": "Friday, Sep 11, 2026 - 12:30 PM MDT",
        "assetFile": "como-img-04-assane-diao.png",
        "assetUrl": f"{CDN_BASE}/como-img-04-assane-diao.png",
        "isVideo": False,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""Fearless talent seizing the global stage! 🌟⚡

Assane Diao making European defenses look static. At 3-0, Como wasn't just managing the game—they were playing with joyful aggression and total clarity.

*Passione. Identità. Bellezza sempre.* Elite performance is never about playing safe. It’s about aggressive conviction when the stakes are highest.

Fan Question: Which young breakout star in European football has impressed you most this season?

👉 Master the courage required to take big shots on big stages. Explore Lornette Daye's leadership library: lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 6,
        "theme_arc": "European Shockwave",
        "slot": "Friday Afternoon (4:30 PM MDT)",
        "dueAt": "2026-09-11T22:30:00.000Z",
        "displayTime": "Friday, Sep 11, 2026 - 4:30 PM MDT",
        "assetFile": "como-vid-03-cesc-celebration.mp4",
        "assetUrl": f"{CDN_BASE}/como-vid-03-cesc-celebration.mp4",
        "isVideo": True,
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""Look at this bond between coach and supporters! 👏💙🇮🇹

Cesc Fàbregas walking the touchline at Stadio Sinigaglia, applauding every stand. This isn't corporate detachment—this is raw, authentic mutual respect between leadership and the faithful.

*Semm Cumasch. Sempre con voi ovunque.* In modern leadership, you cannot command loyalty; you have to earn it through shared sweat, empathy, and integrity.

Fan Question: What makes Cesc Fàbregas such an inspiring manager for this new generation of footballers?

👉 Elevate leadership empathy and culture in your executive suite. Schedule a keynote consultation with Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 7,
        "theme_arc": "European Shockwave",
        "slot": "Friday Evening (8:30 PM MDT)",
        "dueAt": "2026-09-12T02:30:00.000Z",
        "displayTime": "Friday, Sep 11, 2026 - 8:30 PM MDT",
        "assetFile": "como-img-02-in-europa.png",
        "assetUrl": f"{CDN_BASE}/como-img-02-in-europa.png",
        "isVideo": False,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""*IN EUROPA. DAL LAGO ALL'EUROPA.* 🌊✨🏆

Generations of Como faithful standing side by side under the golden alpine glow. Grandfathers who watched Serie C struggles now standing shoulder to shoulder with grandchildren watching the Champions League.

*Football. People. Belonging. Forever.* Great organizations don't just chase quarterly metrics; they honor their roots while boldly claiming their place in the future.

Fan Question: What is your club's greatest memory that gets passed down from generation to generation?

👉 Build generational resilience in your career and life. Pick up your copy of *Survival Skills for Believers*: lornettedaye.com/books

{HASHTAGS}"""
    },

    # --- DAY 2: Saturday, Sep 12, 2026 ---
    {
        "id": 8,
        "theme_arc": "Architect of Belief",
        "slot": "Saturday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-12T14:30:00.000Z",
        "displayTime": "Saturday, Sep 12, 2026 - 8:30 AM MDT",
        "assetFile": "como-img-07-one-club.png",
        "assetUrl": f"{CDN_BASE}/como-img-07-one-club.png",
        "isVideo": False,
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""*ONE CLUB. ONE CITY. PIÙ DI UNA SQUADRA.* 🏟️🤝

Saturday morning reflection on high-performance architecture: Look at Cesc Fàbregas with his men. Tactical plans are useless without absolute psychological buy-in. When 11 players move as one organism, giants fall.

*Il lago. La gente. La storia. Un solo cuore.* That is the formula behind Como 4 - 1 Leipzig.

Fan Question: How do you align a diverse team around one single uncompromising vision?

👉 Book Olympian Coach Lornette Daye to empower your organization with championship-grade team unity: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 9,
        "theme_arc": "Architect of Belief",
        "slot": "Saturday Midday (12:30 PM MDT)",
        "dueAt": "2026-09-12T18:30:00.000Z",
        "displayTime": "Saturday, Sep 12, 2026 - 12:30 PM MDT",
        "assetFile": "como-vid-04-cbs-interview.mp4",
        "assetUrl": f"{CDN_BASE}/como-vid-04-cbs-interview.mp4",
        "isVideo": True,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""The studio was speechless. 🎙️🔥

When Thierry Henry and Jamie Carragher ask you about beating a Bundesliga powerhouse 4-1, and Cesc Fàbregas remains laser-calm and humble—that is the signature of true greatness.

Humility before glory. Work before praise.

Fan Question: What stood out most to you from Cesc's post-match analysis?

👉 Develop the mental discipline that separates flash-in-the-pan success from enduring excellence. Read Lornette Daye: lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 10,
        "theme_arc": "Architect of Belief",
        "slot": "Saturday Afternoon (4:30 PM MDT)",
        "dueAt": "2026-09-12T22:30:00.000Z",
        "displayTime": "Saturday, Sep 12, 2026 - 4:30 PM MDT",
        "assetFile": "como-img-05-maximo-perrone.png",
        "assetUrl": f"{CDN_BASE}/como-img-05-maximo-perrone.png",
        "isVideo": False,
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""*GOAL! Máximo Perrone puts the exclamation mark on European history!* 💥4️⃣-1️⃣

At 4-1, Stadio Sinigaglia was shaking. Midfield domination, vision, and timing. Perrone controlled the tempo from minute 1 to 90.

In elite sports, control of the midfield is control of the narrative. Who is controlling the tempo in your organization?

Fan Question: Rate Máximo Perrone's performance out of 10 against Leipzig! 👇

👉 Master strategic timing and tempo in competitive business environments. Book Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 11,
        "theme_arc": "Architect of Belief",
        "slot": "Saturday Evening (8:30 PM MDT)",
        "dueAt": "2026-09-13T02:30:00.000Z",
        "displayTime": "Saturday, Sep 12, 2026 - 8:30 PM MDT",
        "assetFile": "como-vid-02-goal.mp4",
        "assetUrl": f"{CDN_BASE}/como-vid-02-goal.mp4",
        "isVideo": True,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""Saturday night reel replay: The speed of transition! ⚡⚽

Look at how Como exploits space in behind the defense. When preparation meets opportunity, speed becomes lethal.

*Nel nome di Como combattiamo.*

Fan Question: Can Como’s high-press transitional attack replicate this damage against FC Barcelona?

👉 Learn how to exploit competitive advantages when nobody expects you to win. Read Lornette Daye's books: lornettedaye.com/books

{HASHTAGS}"""
    },

    # --- DAY 3: Sunday, Sep 13, 2026 ---
    {
        "id": 12,
        "theme_arc": "Identity & Culture",
        "slot": "Sunday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-13T14:30:00.000Z",
        "displayTime": "Sunday, Sep 13, 2026 - 8:30 AM MDT",
        "assetFile": "como-img-06-sinigaglia-night.png",
        "assetUrl": f"{CDN_BASE}/como-img-06-sinigaglia-night.png",
        "isVideo": False,
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""*SEMM CUMASCH: European Nights at Stadio Sinigaglia.* 🏔️✨⚽

Sunday morning view: Lake Como shimmering beneath the stadium lights, mountains framing the pitch, and the roar of the Curva echoing into the night.

Location provides atmosphere, but culture provides victory. When athletes play with a sense of place and heritage, they find a fifth gear that tactics alone can never ignite.

Fan Question: Is Stadio Giuseppe Sinigaglia officially the most picturesque venue in all of European football?

👉 Instill purpose and proud organizational identity into your workforce. Book Olympian Coach Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 13,
        "theme_arc": "Identity & Culture",
        "slot": "Sunday Midday (12:30 PM MDT)",
        "dueAt": "2026-09-13T18:30:00.000Z",
        "displayTime": "Sunday, Sep 13, 2026 - 12:30 PM MDT",
        "assetFile": "como-vid-01-anthem.mp4",
        "assetUrl": f"{CDN_BASE}/como-vid-01-anthem.mp4",
        "isVideo": True,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""Turn your volume UP. 🔊🎶💙

When 13,000 voices sing the Champions League anthem as one, the energy is electric. This is what sports is truly about—transcending the individual and lifting an entire city.

*Stessi colori. Stessi sogni. Sempre insieme.*

Fan Question: Which stadium anthem gives you chills every single time you hear it?

👉 Fortify your mindset for moments of massive pressure. Order *Survival Skills for Believers*: lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 14,
        "theme_arc": "Identity & Culture",
        "slot": "Sunday Afternoon (4:30 PM MDT)",
        "dueAt": "2026-09-13T22:30:00.000Z",
        "displayTime": "Sunday, Sep 13, 2026 - 4:30 PM MDT",
        "assetFile": "como-img-08-lariani-flag.png",
        "assetUrl": f"{CDN_BASE}/como-img-08-lariani-flag.png",
        "isVideo": False,
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""*LARIANI. NEL NOME DI COMO.* 🚩👑💙

The flag flies high above Lombardy. Como 1907 represents far more than 90 minutes of football; it represents Italian grit, aesthetic heritage, and an unwavering commitment to excellence.

*Passione. Identità. Bellezza.* Leadership is about protecting what matters while expanding your horizons.

Fan Question: What does your team's flag represent to you personally?

👉 Cultivate authentic organizational leadership. Book keynote speaker Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 15,
        "theme_arc": "Identity & Culture",
        "slot": "Sunday Evening (8:30 PM MDT)",
        "dueAt": "2026-09-14T02:30:00.000Z",
        "displayTime": "Sunday, Sep 13, 2026 - 8:30 PM MDT",
        "assetFile": "como-vid-03-cesc-celebration.mp4",
        "assetUrl": f"{CDN_BASE}/como-vid-03-cesc-celebration.mp4",
        "isVideo": True,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""The smile of a coach whose vision was validated. 😊🔥

Cesc Fàbregas took over a project many doubted. Tonight, those doubts evaporated into the alpine air.

When you have the courage to stick to your tactical philosophy even when critics push for compromise, the results speak for themselves.

Fan Question: In your life, when did sticking to your principles finally pay off?

👉 Build moral fortitude and unwavering strategic discipline. Visit: lornettedaye.com/books

{HASHTAGS}"""
    },

    # --- DAY 4: Monday, Sep 14, 2026 ---
    {
        "id": 16,
        "theme_arc": "Execution Under Global Spotlight",
        "slot": "Monday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-14T14:30:00.000Z",
        "displayTime": "Monday, Sep 14, 2026 - 8:30 AM MDT",
        "assetFile": "como-img-03-match-report.png",
        "assetUrl": f"{CDN_BASE}/como-img-03-match-report.png",
        "isVideo": False,
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""*MATCH REPORT: COMO 1907. UNA NOTTE DA RICORDARE.* 📰✨

Monday morning executive breakdown:
4 Goals. 62% Possession. 18 Shots. 0 Hesitation.

Como didn't park the bus. They imposed their identity upon RB Leipzig from the opening whistle. True authority is not defensive; it is creative, courageous, and proactive.

Fan Question: What was the tactical highlight that impressed you most from Como’s masterclass?

👉 Bring Olympic-tested high-performance strategies to your executive boardroom. Book Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 17,
        "theme_arc": "Execution Under Global Spotlight",
        "slot": "Monday Midday (12:30 PM MDT)",
        "dueAt": "2026-09-14T18:30:00.000Z",
        "displayTime": "Monday, Sep 14, 2026 - 12:30 PM MDT",
        "assetFile": "como-vid-02-goal.mp4",
        "assetUrl": f"{CDN_BASE}/como-vid-02-goal.mp4",
        "isVideo": True,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""Notice the anticipation before the pass is even kicked. 🧠⚽

Elite athletic vision is never reactive; it anticipates two moves ahead. That’s how Como dismantled one of Germany’s best pressing units.

*Dal lago all'Europa.*

Fan Question: Is vision innate, or can it be trained through relentless pattern recognition?

👉 Train your mental faculties for proactive decision-making. Order Lornette Daye's books: lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 18,
        "theme_arc": "Execution Under Global Spotlight",
        "slot": "Monday Afternoon (4:30 PM MDT)",
        "dueAt": "2026-09-14T22:30:00.000Z",
        "displayTime": "Monday, Sep 14, 2026 - 4:30 PM MDT",
        "assetFile": "como-img-01-fulltime.png",
        "assetUrl": f"{CDN_BASE}/como-img-01-fulltime.png",
        "isVideo": False,
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""4 - 1. The scoreline that silenced the skeptics. 📊💥

When Como qualified for Europe, commentators questioned whether they were ready for this tier. This scoreline answered every question.

*La nostra Europa. Semm Cumasch.* Never let external skeptics determine your internal ceiling.

Fan Question: Who was your Player of the Match? Diao, Perrone, or the tactical brain Fàbregas?

👉 Equip your leaders with the confidence to thrive under scrutiny. Book keynote speaker Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 19,
        "theme_arc": "Execution Under Global Spotlight",
        "slot": "Monday Evening (8:30 PM MDT)",
        "dueAt": "2026-09-15T02:30:00.000Z",
        "displayTime": "Monday, Sep 14, 2026 - 8:30 PM MDT",
        "assetFile": "como-vid-04-cbs-interview.mp4",
        "assetUrl": f"{CDN_BASE}/como-vid-04-cbs-interview.mp4",
        "isVideo": True,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""“We prepare every detail. But more than tactics, they believe.” — Cesc Fàbregas on CBS Sports. 🎙️

Tactics provide structure, but belief provides fire. Without belief, the most brilliant playbook falls apart under pressure.

Fan Question: How do you restore belief when a team has suffered past defeats?

👉 Learn how to cultivate champion-level self-belief from 40+ years of Olympic coaching: lornettedaye.com/books

{HASHTAGS}"""
    },

    # --- DAY 5: Tuesday, Sep 15, 2026 ---
    {
        "id": 20,
        "theme_arc": "From Serie D to Europe",
        "slot": "Tuesday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-15T14:30:00.000Z",
        "displayTime": "Tuesday, Sep 15, 2026 - 8:30 AM MDT",
        "assetFile": "como-img-02-in-europa.png",
        "assetUrl": f"{CDN_BASE}/como-img-02-in-europa.png",
        "isVideo": False,
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""From mud pitches in the amateur leagues to the Champions League stars. ⭐🇮🇹

The Como 1907 story is one of the most romantic and rigorous ascents in modern sports. It proves that with patient capital, brilliant scouting, and world-class leadership, miracles can be engineered.

*Più di un club. Una storia che continua.*

Fan Question: Is Como's journey the greatest football resurgence story of the 2020s?

👉 Inspire your organization with the endurance required for long-term transformation. Book Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 21,
        "theme_arc": "From Serie D to Europe",
        "slot": "Tuesday Midday (12:30 PM MDT)",
        "dueAt": "2026-09-15T18:30:00.000Z",
        "displayTime": "Tuesday, Sep 15, 2026 - 12:30 PM MDT",
        "assetFile": "como-vid-03-cesc-celebration.mp4",
        "assetUrl": f"{CDN_BASE}/como-vid-03-cesc-celebration.mp4",
        "isVideo": True,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""Never forget who you are fighting for. 💙

In this video, watch how Cesc points toward the supporters. He understands that a sports team is a public trust, not just a balance sheet.

*Como 1907 sempre.*

Fan Question: What is the emotional heart of your favorite team?

👉 Ground your career in purpose and lasting value. Explore Lornette Daye's publications: lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 22,
        "theme_arc": "From Serie D to Europe",
        "slot": "Tuesday Afternoon (4:30 PM MDT)",
        "dueAt": "2026-09-15T22:30:00.000Z",
        "displayTime": "Tuesday, Sep 15, 2026 - 4:30 PM MDT",
        "assetFile": "como-img-07-one-club.png",
        "assetUrl": f"{CDN_BASE}/como-img-07-one-club.png",
        "isVideo": False,
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""*LIBERTÀ. BELLEZZA. COMO.* 🌊⚽

Freedom of expression on the pitch backed by intense tactical rigor. That is modern Italian football at its finest.

Great coaching does not suffocate individual genius; it provides the protective framework where creativity flourishes.

Fan Question: Who gives players more creative freedom: Fàbregas or Guardiola?

👉 Unleash creative high performance within disciplined operational systems. Book Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 23,
        "theme_arc": "From Serie D to Europe",
        "slot": "Tuesday Evening (8:30 PM MDT)",
        "dueAt": "2026-09-16T02:30:00.000Z",
        "displayTime": "Tuesday, Sep 15, 2026 - 8:30 PM MDT",
        "assetFile": "como-vid-01-anthem.mp4",
        "assetUrl": f"{CDN_BASE}/como-vid-01-anthem.mp4",
        "isVideo": True,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""Under the lights, under the pressure, champions are forged. ⚡🏟️

Listen to the roar of Stadio Sinigaglia. When you train in the dark, the lights can't blind you.

*Passione identità bellezza sempre.*

Fan Question: Do you perform better with everyone watching, or in the quiet grind behind closed doors?

👉 Read *Survival Skills for Believers* to cultivate unbreakable focus: lornettedaye.com/books

{HASHTAGS}"""
    },

    # --- DAY 6: Wednesday, Sep 16, 2026 ---
    {
        "id": 24,
        "theme_arc": "Eyes on Barcelona",
        "slot": "Wednesday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-16T14:30:00.000Z",
        "displayTime": "Wednesday, Sep 16, 2026 - 8:30 AM MDT",
        "assetFile": "como-img-04-assane-diao.png",
        "assetUrl": f"{CDN_BASE}/como-img-04-assane-diao.png",
        "isVideo": False,
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""The next summit awaits: FC Barcelona. ⚔️🇪🇸

Beating Leipzig 4-1 put Europe on high alert. But champions don't dwell on yesterday's trophies. The real test is consistency against the continental elite.

Assane Diao and the front line are already gearing up for their greatest test yet.

Fan Question: Can Como pull off the unthinkable and score at the Camp Nou / Montjuïc against Barcelona?

👉 Learn how to sustain peak performance after achieving monumental milestones. Book Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 25,
        "theme_arc": "Eyes on Barcelona",
        "slot": "Wednesday Midday (12:30 PM MDT)",
        "dueAt": "2026-09-16T18:30:00.000Z",
        "displayTime": "Wednesday, Sep 16, 2026 - 12:30 PM MDT",
        "assetFile": "como-vid-04-cbs-interview.mp4",
        "assetUrl": f"{CDN_BASE}/como-vid-04-cbs-interview.mp4",
        "isVideo": True,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""Cesc Fàbregas facing his boyhood club FC Barcelona. 💙❤️ vs 💙🤍

The storylines don't get richer than this. Cesc returning to face the club that sculpted his football philosophy, now leading his own Italian project.

Poise under sentimental and competitive pressure will decide that clash.

Fan Question: What is your score prediction for Barcelona vs Como 1907? Drop your numbers below!

👉 Prepare your mind for moments where emotion and execution collide. Visit: lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 26,
        "theme_arc": "Eyes on Barcelona",
        "slot": "Wednesday Afternoon (4:30 PM MDT)",
        "dueAt": "2026-09-16T22:30:00.000Z",
        "displayTime": "Wednesday, Sep 16, 2026 - 4:30 PM MDT",
        "assetFile": "como-img-05-maximo-perrone.png",
        "assetUrl": f"{CDN_BASE}/como-img-05-maximo-perrone.png",
        "isVideo": False,
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""Midfield mastery is how you disrupt European dynasties. ♟️⚽

Máximo Perrone's tactical intelligence will be the fulcrum when Como faces Barcelona's midfield carousel. When you respect the fundamentals, you can shock the world.

Fan Question: Who wins the midfield battle: Perrone and Como or Pedri and Barcelona?

👉 Master foundational execution that stands strong against elite opposition. Book Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 27,
        "theme_arc": "Eyes on Barcelona",
        "slot": "Wednesday Evening (8:30 PM MDT)",
        "dueAt": "2026-09-17T02:30:00.000Z",
        "displayTime": "Wednesday, Sep 16, 2026 - 8:30 PM MDT",
        "assetFile": "como-vid-02-goal.mp4",
        "assetUrl": f"{CDN_BASE}/como-vid-02-goal.mp4",
        "isVideo": True,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""Execution under the microscope. 🔍⚽

When the opportunity opens against Barcelona, Como will have seconds to strike. Revisit this Leipzig counter-attack—this is the template for European giant-killing.

*Semm Cumasch.*

Fan Question: Is counter-attacking or possession-based play more effective against top European clubs?

👉 Read *Survival Skills for Believers* for razor-sharp strategic execution: lornettedaye.com/books

{HASHTAGS}"""
    },

    # --- DAY 7: Thursday, Sep 17, 2026 ---
    {
        "id": 28,
        "theme_arc": "Semm Cumasch Grand Finale",
        "slot": "Thursday Morning (8:30 AM MDT)",
        "dueAt": "2026-09-17T14:30:00.000Z",
        "displayTime": "Thursday, Sep 17, 2026 - 8:30 AM MDT",
        "assetFile": "como-img-08-lariani-flag.png",
        "assetUrl": f"{CDN_BASE}/como-img-08-lariani-flag.png",
        "isVideo": False,
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""*SEMM CUMASCH: ONE WEEK LATER, THE PRIDE BURNS STRONGER.* 🏔️💙

Seven days ago, Como 1907 shook European football with a 4-1 victory. The excitement hasn't faded—it has solidified into permanent self-belief.

*Lariani. Nel nome di Como.* When you realize you belong at the top table, your whole posture changes.

Fan Question: Has Como earned a permanent spot among Europe's most exciting clubs to watch?

👉 Empower your organization with the permanent posture of a champion. Book Olympian Coach Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 29,
        "theme_arc": "Semm Cumasch Grand Finale",
        "slot": "Thursday Midday (12:30 PM MDT)",
        "dueAt": "2026-09-17T18:30:00.000Z",
        "displayTime": "Thursday, Sep 17, 2026 - 12:30 PM MDT",
        "assetFile": "como-vid-01-anthem.mp4",
        "assetUrl": f"{CDN_BASE}/como-vid-01-anthem.mp4",
        "isVideo": True,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""The anthem that started a new era. 🎵⭐

Let the music of the Champions League at Stadio Sinigaglia remind you: No dream is too ambitious if you have the discipline to build brick by brick.

*Football. People. Places. Forever.*

Fan Question: What is your biggest goal this year that others think is impossible?

👉 Fuel your ambition with practical mental mastery tools from Lornette Daye: lornettedaye.com/books

{HASHTAGS}"""
    },
    {
        "id": 30,
        "theme_arc": "Semm Cumasch Grand Finale",
        "slot": "Thursday Afternoon (4:30 PM MDT)",
        "dueAt": "2026-09-17T22:30:00.000Z",
        "displayTime": "Thursday, Sep 17, 2026 - 4:30 PM MDT",
        "assetFile": "como-img-06-sinigaglia-night.png",
        "assetUrl": f"{CDN_BASE}/como-img-06-sinigaglia-night.png",
        "isVideo": False,
        "cta": "Speaking (lornettedaye.com/speaking)",
        "text": f"""*EUROPEAN NIGHTS AT STADIO SINIGAGLIA.* ✨🏟️

A sanctuary of sport on the edge of the water. Como 1907 has demonstrated to the entire sporting world how to marry ancient community tradition with modern high-performance sports science.

*Più di una squadra. Una città. Un popolo.*

Fan Question: Which club in world sport best embodies its city's spirit?

👉 Bring Olympic-caliber cultural architecture to your enterprise. Book Lornette Daye: lornettedaye.com/speaking

{HASHTAGS}"""
    },
    {
        "id": 31,
        "theme_arc": "Semm Cumasch Grand Finale",
        "slot": "Thursday Evening (8:30 PM MDT)",
        "dueAt": "2026-09-18T02:30:00.000Z",
        "displayTime": "Thursday, Sep 17, 2026 - 8:30 PM MDT",
        "assetFile": "como-vid-03-cesc-celebration.mp4",
        "assetUrl": f"{CDN_BASE}/como-vid-03-cesc-celebration.mp4",
        "isVideo": True,
        "cta": "Books (lornettedaye.com/books)",
        "text": f"""*FORZA COMO! SEMPRE!* 💙🏆🇮🇹

As the celebration sprint concludes, the real European campaign begins. Barcelona awaits. The eyes of the world are watching.

Cesc Fàbregas and Como 1907 have proven that fear has no place in championship ambition. When preparation meets heart, history is made.

Fan Question: Will you be tuning in when Como takes on Barcelona in Matchday 2? Drop a 💙 if you're backing the Lariani!

👉 Prepare your life and career for world-class challenges. Read *Survival Skills for Believers* by Lornette Daye: lornettedaye.com/books

{HASHTAGS}"""
    }
]

mutation = """
mutation CreatePost($input: CreatePostInput!) {
  createPost(input: $input) {
    __typename
    ... on PostActionSuccess {
      post {
        id
        text
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

def buffer_request(query, variables):
    ctx = ssl._create_unverified_context()
    payload = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    req = urllib.request.Request(
        "https://api.buffer.com",
        data=payload,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }
    )
    with urllib.request.urlopen(req, context=ctx) as resp:
        body = json.loads(resp.read().decode("utf-8"))
        if "errors" in body:
            print(f"   ❌ GraphQL Errors: {body['errors']}")
        return body.get("data", {})

def probe_assets():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    unique_urls = sorted(list(set(p["assetUrl"] for p in posts_data)))
    print(f"🔍 Pre-flight checking {len(unique_urls)} unique production URLs on https://lornettedaye.com...")
    all_ok = True
    for url in unique_urls:
        try:
            req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, context=ctx) as resp:
                status = resp.status
                cl = resp.headers.get("Content-Length", "unknown")
                if status == 200:
                    print(f"  ✅ [200 OK] {url} ({cl} bytes)")
                else:
                    print(f"  ❌ [{status}] {url}")
                    all_ok = False
        except Exception as e:
            print(f"  ❌ [ERROR] {url} -> {e}")
            all_ok = False
    return all_ok

def main():
    print("======================================================")
    print("  Como 1907 Champions League Victory Campaign: 31 Posts")
    print(f"  Channel: {CHANNEL_ID}")
    print(f"  Total posts to schedule: {len(posts_data)}")
    print("======================================================\n")

    if not probe_assets():
        print("🛑 Pre-flight verification failed! One or more assets did not return HTTP 200.")
        sys.exit(1)

    results = []

    for idx, p in enumerate(posts_data):
        print(f"[{idx + 1}/{len(posts_data)}] Scheduling Post #{p['id']} ({p['theme_arc']}): \"{p['slot']}\"")
        print(f"   Due: {p['dueAt']} | CTA: {p['cta']}")
        print(f"   Asset: {p['assetUrl']} (Video: {p['isVideo']})")

        if p.get("isVideo", False):
            asset_payload = [{"video": {"url": p["assetUrl"]}}]
        else:
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

    report_path = os.path.join(os.path.dirname(__file__), "como-win-scheduled-report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print("------------------------------------------------------")
    print(f"🎉 Como Win Campaign Report saved to {report_path}")
    successful = sum(1 for r in results if r.get("status") == "scheduled")
    print(f"Summary: {successful}/{len(posts_data)} posts scheduled in Buffer Scheduled Queue.")
    print("------------------------------------------------------")

if __name__ == "__main__":
    main()
