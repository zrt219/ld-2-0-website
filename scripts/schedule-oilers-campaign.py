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

CDN_BASE = 'https://lornettedaye.com/campaigns/oilers'

posts_data = [
    # =========================================================================
    # WAVE 1: THE FOUNDATION & RELENTLESS WORK ETHIC (Days 1 - 10)
    # =========================================================================
    # Post 1 (Sat, Oct 03) - Asset: oilers-01.png
    {
        "id": 1,
        "wave": "Wave 1: The Foundation & Relentless Work Ethic",
        "slot": "Day 1: Saturday, Oct 03, 2026 at 04:30 PM MDT",
        "dueAt": "2026-10-03T22:30:00.000Z",
        "assetFile": "oilers-01.png",
        "assetUrl": f"{CDN_BASE}/oilers-01.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "THE CHAMPIONSHIP STANDARD: HOW GREAT TEAMS RESPOND WHEN EVERYTHING IS ON THE LINE. 🏒⚡\n\n"
            "In forty years of coaching Olympic athletes and world champions across Canada and internationally, "
            "I have learned that championship culture is not built during celebratory victory parades. "
            "It is built in the brutal crucible of adversity.\n\n"
            "Look at the Edmonton Oilers. When you watch Connor McDavid, Leon Draisaitl, and this locker room, "
            "you are watching an elite masterclass in relentless standard-setting. "
            "They do not rely on passive hope. They hold each other accountable to an unforgiving standard of daily execution.\n\n"
            "In enterprise leadership, high-performing organizations often struggle when the market turns volatile. "
            "The teams that survive and thrive are those that establish an unshakeable internal benchmark before the pressure peaks.\n\n"
            "Set the standard early. Protect it relentlessly.\n\n"
            "With purpose,\n"
            "Lornette\n\n"
            "Bring Olympic-level team accountability and high-performance culture to your executive retreat or corporate conference. "
            "Book my keynote presentation: https://lornettedaye.com/book\n\n"
            "#EdmontonOilers #OilersNation #LetsGoOilers #ConnorMcDavid #LeonDraisaitl #NHL #ChampionshipStandard #HighPerformance "
            "#OlympicMindset #ExecutiveLeadership #TeamAccountability #FinishStrong #LornetteDaye #CorporateKeynote"
        )
    },
    # Post 2 (Sun, Oct 04) - Asset: oilers-02.png
    {
        "id": 2,
        "wave": "Wave 1: The Foundation & Relentless Work Ethic",
        "slot": "Day 2: Sunday, Oct 04, 2026 at 04:30 PM MDT",
        "dueAt": "2026-10-04T22:30:00.000Z",
        "assetFile": "oilers-02.png",
        "assetUrl": f"{CDN_BASE}/oilers-02.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "THE LONELINESS OF ELITE PREPARATION: SUMMER SWEAT BUILDS WINTER PODIUMS. ❄️🏋️\n\n"
            "People love the euphoria of a third-period game winner in Rogers Place. "
            "What they never witness is the solitary summer sweat: five hours a day on obscure ice sheets in July, "
            "anaerobic threshold interval sprints, and rigorous video analysis when the world is on vacation.\n\n"
            "Connor McDavid did not become the greatest player on the planet by resting on his God-given acceleration. "
            "He out-worked every peer in the quiet months so that his execution on game night feels effortless.\n\n"
            "In business, organizations cannot expect to innovate during quarterly earnings panic if they neglected their fundamentals "
            "during ordinary operating cycles. The glory of Sunday belongs to the discipline of Tuesday morning.\n\n"
            "Do the unseen work.\n\n"
            "Stay disciplined,\n"
            "Lornette\n\n"
            "Elevate your organization's preparation habits and operational excellence. "
            "Schedule a conversation to book my corporate keynote: https://lornettedaye.com/book\n\n"
            "#UnseenWork #PreparationEqualsConfidence #EdmontonOilers #McDavid #OilersHockey #WorkEthic #OlympicStandard "
            "#ExecutiveExcellence #HighPerformanceHabits #FinishStrong #LornetteDaye #LeadershipSpeaker"
        )
    },
    # Post 3 (Mon, Oct 05) - Asset: oilers-03.png
    {
        "id": 3,
        "wave": "Wave 1: The Foundation & Relentless Work Ethic",
        "slot": "Day 3: Monday, Oct 05, 2026 at 04:30 PM MDT",
        "dueAt": "2026-10-05T22:30:00.000Z",
        "assetFile": "oilers-03.png",
        "assetUrl": f"{CDN_BASE}/oilers-03.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "ALIGNING SUPERSTAR EGOS FOR A COMMON QUEST. 🤝🏒\n\n"
            "In modern professional sports, having two of the greatest players of an era on the same roster often produces friction, "
            "jealousy, and fragmented locker rooms. "
            "Yet, Connor McDavid and Leon Draisaitl have forged one of the most selfless, lethal leadership partnerships in hockey history.\n\n"
            "Why? Because both men decided early on that the collective goal of bringing the Stanley Cup home to Canada "
            "mattered far more than personal scoring titles.\n\n"
            "In the C-suite, managing brilliant, high-ego executives is one of the toughest challenges a CEO faces. "
            "When leaders subordinate individual vanity for shared organizational legacy, the entire enterprise becomes unstoppable.\n\n"
            "Subordinate ego. Elevate mission.\n\n"
            "In your corner,\n"
            "Lornette\n\n"
            "Book my keynote on aligning executive teams and building high-trust partnerships for your summit: "
            "https://lornettedaye.com/book\n\n"
            "#LeadershipPartnership #McDavidAndDraisaitl #EdmontonOilers #OilersNation #ExecutiveAlignment #TeamFirst "
            "#HighTrustTeams #LockerRoomCulture #OlympicExcellence #LornetteDaye #FinishStrong"
        )
    },
    # Post 4 (Tue, Oct 06) - Asset: oilers-04.png
    {
        "id": 4,
        "wave": "Wave 1: The Foundation & Relentless Work Ethic",
        "slot": "Day 4: Tuesday, Oct 06, 2026 at 04:30 PM MDT",
        "dueAt": "2026-10-06T22:30:00.000Z",
        "assetFile": "oilers-04.png",
        "assetUrl": f"{CDN_BASE}/oilers-04.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "SPEED OF PROCESSING: DECISION-MAKING AT 25 MILES PER HOUR. ⚡🧠\n\n"
            "Hockey is the fastest team sport in existence. Skaters travel at 25 miles per hour on razor blades while tracking a rubber disc "
            "moving at over 90 miles per hour, all while absorbing heavy body contact.\n\n"
            "Connor McDavid's real superpower is not just his leg speed. It is his cognitive processing speed. "
            "He perceives passing lanes two strides before anyone else on the ice.\n\n"
            "As an Olympic coach, I train competitors to quiet their internal panic so their sensory acuity can operate without friction. "
            "In corporate boardrooms, market changes happen at blistering speed. "
            "The executives who succeed are the ones who can maintain absolute emotional calm while processing complex variables.\n\n"
            "Cultivate internal calm. Execute at full speed.\n\n"
            "With focus,\n"
            "Lornette\n\n"
            "Inquire about bringing me to address your senior leadership team: "
            "https://lornettedaye.com/book\n\n"
            "#ProcessingSpeed #CognitiveAgility #HighSpeedDecisionMaking #ConnorMcDavid #EdmontonOilers #ExecutivePresence "
            "#EmotionalPoise #OlympicTraining #FinishStrong #LornetteDaye #CorporateKeynote"
        )
    },
    # Post 5 (Wed, Oct 07) - Asset: oilers-05.png
    {
        "id": 5,
        "wave": "Wave 1: The Foundation & Relentless Work Ethic",
        "slot": "Day 5: Wednesday, Oct 07, 2026 at 04:30 PM MDT",
        "dueAt": "2026-10-07T22:30:00.000Z",
        "assetFile": "oilers-05.png",
        "assetUrl": f"{CDN_BASE}/oilers-05.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "PHYSICAL RESILIENCE AND THE COURAGE TO PLAY THROUGH PAIN. 🛡️🧊\n\n"
            "Leon Draisaitl's playoff performances while battling high-ankle sprains and severe physical trauma "
            "have become legendary across the National Hockey League. "
            "He does not ask for sympathy. He tape his skates, adjusts his center of gravity, and delivers 30 minutes of dominant ice time.\n\n"
            "True professional endurance is not about never experiencing hurt. "
            "It is about possessing a deep personal foundation that allows you to contribute even when you are operating below 100 percent.\n\n"
            "Leaders often carry silent personal battles while having to project certainty for their teams. "
            "Developing emotional stamina ensures you do not fold when circumstances get heavy.\n\n"
            "Stand firm through the test.\n\n"
            "With respect,\n"
            "Lornette\n\n"
            "Equip your leadership cohorts with world-class resilience frameworks. "
            "Book my Finish Strong keynote: https://lornettedaye.com/book\n\n"
            "#LeonDraisaitl #PhysicalResilience #EmotionalEndurance #EdmontonOilers #OilersNation #PlayoffToughness "
            "#MentalStamina #OlympicMindset #FinishStrong #LornetteDaye #KeynoteSpeaker"
        )
    },
    # Post 6 (Thu, Oct 08) - Asset: oilers-06.png
    {
        "id": 6,
        "wave": "Wave 1: The Foundation & Relentless Work Ethic",
        "slot": "Day 6: Thursday, Oct 08, 2026 at 04:30 PM MDT",
        "dueAt": "2026-10-08T22:30:00.000Z",
        "assetFile": "oilers-06.png",
        "assetUrl": f"{CDN_BASE}/oilers-06.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "THE DEFENSIVE BUY-IN: SACRIFICING GLORY FOR SYSTEM STABILITY. 🥅🛑\n\n"
            "For years, critics claimed the Edmonton Oilers were an all-offense novelty that could never win in the playoffs. "
            "The transformation occurred when the entire roster, beginning with McDavid and Draisaitl, bought into backchecking, "
            "blocking shots on the penalty kill, and protecting the house.\n\n"
            "Offense sells tickets. Defensive discipline wins championships.\n\n"
            "In every business, frontline sales capture headlines, but operational discipline, risk management, "
            "and client retention keep the company standing through economic winter. "
            "When your stars celebrate the unglamorous defensive duties, your entire company standard shifts.\n\n"
            "Celebrate the quiet disciplines.\n\n"
            "Stay steady,\n"
            "Lornette\n\n"
            "Book my keynote on operational discipline and culture alignment for your corporate conference: "
            "https://lornettedaye.com/book\n\n"
            "#DefensiveDiscipline #SystemIntegrity #EdmontonOilers #TeamFirst #ChampionshipCulture #OperationalExcellence "
            "#NHLPlayoffs #OlympicCoaching #FinishStrong #LornetteDaye #ExecutiveKeynote"
        )
    },
    # Post 7 (Fri, Oct 09) - Asset: oilers-07.png
    {
        "id": 7,
        "wave": "Wave 1: The Foundation & Relentless Work Ethic",
        "slot": "Day 7: Friday, Oct 09, 2026 at 04:30 PM MDT",
        "dueAt": "2026-10-09T22:30:00.000Z",
        "assetFile": "oilers-07.png",
        "assetUrl": f"{CDN_BASE}/oilers-07.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "THE POWER OF A UNIFIED BENCH: ENERGY AS AN OPERATIONAL ASSET. 📣🔥\n\n"
            "Watch the Edmonton Oilers bench during a critical penalty kill. "
            "The players not on the ice are not sitting passively waiting for their shift. "
            "They are standing, shouting communication, tapping sticks, and projecting belief onto the ice.\n\n"
            "In forty years of international competition, I can tell who will win a championship by inspecting the bench, not the starting lineup. "
            "When your supporting cast invests genuine emotional capital into the success of their peers, "
            "the collective energy becomes an insurmountable competitive advantage.\n\n"
            "How engaged is your organization's bench?\n\n"
            "Together in excellence,\n"
            "Lornette\n\n"
            "Bring this transformative perspective on bench culture and mutual accountability to your company. "
            "Book my keynote: https://lornettedaye.com/book\n\n"
            "#BenchCulture #TeamEnergy #EdmontonOilers #LockerRoomChemistry #PeerAccountability #HighPerformanceTeams "
            "#OlympicWisdom #FinishStrong #LornetteDaye #LeadershipDevelopment"
        )
    },
    # Post 8 (Sat, Oct 10) - Asset: oilers-08.png
    {
        "id": 8,
        "wave": "Wave 1: The Foundation & Relentless Work Ethic",
        "slot": "Day 8: Saturday, Oct 10, 2026 at 04:30 PM MDT",
        "dueAt": "2026-10-10T22:30:00.000Z",
        "assetFile": "oilers-08.png",
        "assetUrl": f"{CDN_BASE}/oilers-08.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "THE BURDEN OF NATIONAL EXPECTATION: PLAYING FOR CANADIAN HERITAGE. 🇨🇦🍁\n\n"
            "In Canada, hockey is not merely a pastime. It is cultural oxygen. "
            "Carrying the weight of a thirty-year Canadian Stanley Cup drought creates an atmosphere of immense national scrutiny.\n\n"
            "The Oilers do not run from that pressure. They embrace it as a sacred privilege. "
            "Pressure is the tax you pay for being in a position that genuinely matters.\n\n"
            "When your leadership team operates under the scrutiny of boards, public markets, or national headlines, "
            "you must teach them to view expectation not as a burden, but as validation of their capability.\n\n"
            "Embrace the expectation.\n\n"
            "Proudly,\n"
            "Lornette\n\n"
            "Inquire about executive keynote bookings and private leadership workshops: "
            "https://lornettedaye.com/book\n\n"
            "#CanadianHockey #EdmontonOilers #StanleyCupPursuit #PressureIsAPrivilege #NationalPride #ExecutivePresence "
            "#HighStakesLeadership #OlympicHeritage #FinishStrong #LornetteDaye"
        )
    },
    # Post 9 (Sun, Oct 11) - Asset: oilers-09.png
    {
        "id": 9,
        "wave": "Wave 1: The Foundation & Relentless Work Ethic",
        "slot": "Day 9: Sunday, Oct 11, 2026 at 04:30 PM MDT",
        "dueAt": "2026-10-11T22:30:00.000Z",
        "assetFile": "oilers-09.png",
        "assetUrl": f"{CDN_BASE}/oilers-09.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "MOMENTUM MANAGEMENT: RIDING THE SHIFTS OF FORTUNE. 🌊⛸️\n\n"
            "A hockey game swings violently. A disputed penalty, a fluke bounce off a skate, "
            "or an unexpected goal against can instantly suck the oxygen out of an arena.\n\n"
            "What separates the Oilers from ordinary teams is their ability to stop negative momentum before it cascades. "
            "One smart shift in the offensive zone, a hard cycle along the boards, or a poised goalie freeze resets the game.\n\n"
            "In corporate management, negative momentum is real: missed sales quotas, key employee departures, or technical outages. "
            "Great leaders know how to take a breath, call a timeout, and re-establish equilibrium before panic takes hold.\n\n"
            "Master the momentum shift.\n\n"
            "Stay poised,\n"
            "Lornette\n\n"
            "Book me to speak to your corporate leaders on managing volatility and emotional poise: "
            "https://lornettedaye.com/book\n\n"
            "#MomentumManagement #EmotionalPoise #CrisisLeadership #EdmontonOilers #OilersNation #NHL #GameManagement "
            "#OlympicCoaching #FinishStrong #LornetteDaye #ExecutiveKeynote"
        )
    },
    # Post 10 (Mon, Oct 12) - Asset: oilers-10.png
    {
        "id": 10,
        "wave": "Wave 1: The Foundation & Relentless Work Ethic",
        "slot": "Day 10: Monday, Oct 12, 2026 at 04:30 PM MDT",
        "dueAt": "2026-10-12T22:30:00.000Z",
        "assetFile": "oilers-10.png",
        "assetUrl": f"{CDN_BASE}/oilers-10.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "THE CAPTAIN'S LOG: LEADING BY ACTIONS, NOT RHETORIC. 🧢🎯\n\n"
            "Connor McDavid is not known for theatrical speeches or emotional theatrics. "
            "He leads through an unyielding, surgical commitment to preparation, dietary discipline, and relentless shift execution.\n\n"
            "When the captain backchecks 200 feet to break up an empty-net breakaway, nobody else on the bench has the right to coast. "
            "True leadership is moral authority earned through self-sacrifice.\n\n"
            "If you want your organization to increase its standard of excellence, look in the mirror before you send a memo. "
            "Your people are watching what you do, not what you say.\n\n"
            "Lead from the front.\n\n"
            "Finish strong,\n"
            "Lornette\n\n"
            "Reserve your keynote date on my calendar: "
            "https://lornettedaye.com/book\n\n"
            "#Captaincy #MoralAuthority #LeadByExample #ConnorMcDavid #EdmontonOilers #ExecutiveLeadership #AuthenticLeadership "
            "#OlympicStandard #FinishStrong #LornetteDaye #KeynoteSpeaker"
        )
    },

    # =========================================================================
    # WAVE 2: THE FIRE OF ADVERSITY & PLAYOFF RESILIENCE (Days 11 - 20)
    # =========================================================================
    # Post 11 (Tue, Oct 13) - Asset: oilers-01.png
    {
        "id": 11,
        "wave": "Wave 2: The Fire of Adversity & Playoff Resilience",
        "slot": "Day 11: Tuesday, Oct 13, 2026 at 04:30 PM MDT",
        "dueAt": "2026-10-13T22:30:00.000Z",
        "assetFile": "oilers-01.png",
        "assetUrl": f"{CDN_BASE}/oilers-01.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "DOWN 0-3 IN THE STANLEY CUP FINALS: THE HISTORIC REFUSAL TO BREAK. 🔴🔵\n\n"
            "Remember the 2024 Stanley Cup Finals. Down three games to zero. The entire hockey world had already etched the opponent's name on the trophy. "
            "The media was writing obituaries.\n\n"
            "What did the Edmonton Oilers do? They did not fold. They did not point fingers in the locker room. "
            "They took it one period at a time: Game 4, blowout victory. Game 5, road triumph. Game 6, electric home arena domination. "
            "They dragged the series all the way back to Game 7.\n\n"
            "That historic comeback showed the entire world what genuine athletic resilience looks like. "
            "When everyone writes you off, your only responsibility is to win the very next shift.\n\n"
            "Never concede your race.\n\n"
            "With admiration,\n"
            "Lornette\n\n"
            "Book my keynote on historic resilience and pulling teams out of deficits: "
            "https://lornettedaye.com/book\n\n"
            "#HistoricComeback #StanleyCupFinals #EdmontonOilers #OilersNation #ResilienceInSport #NeverSurrender "
            "#HighPerformanceMindset #OlympicCoach #FinishStrong #LornetteDaye #ExecutiveKeynote"
        )
    },
    # Post 12 (Wed, Oct 14) - Asset: oilers-02.png
    {
        "id": 12,
        "wave": "Wave 2: The Fire of Adversity & Playoff Resilience",
        "slot": "Day 12: Wednesday, Oct 14, 2026 at 04:30 PM MDT",
        "dueAt": "2026-10-14T22:30:00.000Z",
        "assetFile": "oilers-02.png",
        "assetUrl": f"{CDN_BASE}/oilers-02.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "ONE SHIFT AT A TIME: THE PSYCHOLOGY OF LARGE COMEBACKS. ⏱️🧊\n\n"
            "When you are down by multiple goals in hockey or multiple millions in enterprise revenue, "
            "trying to make up the entire deficit in a single play will guarantee a disastrous collapse.\n\n"
            "The secret to monumental turnarounds is micro-focus. You cannot score three goals on one rush. "
            "You can only win the next puck battle in the corner. You can only clear the puck out of the zone. "
            "You can only make one tape-to-tape pass.\n\n"
            "When you stack sixty seconds of disciplined execution fifty times in a row, the scoreboard inevitably catches up.\n\n"
            "Shrink your focus to this exact moment.\n\n"
            "Stay grounded,\n"
            "Lornette\n\n"
            "Learn how to lead corporate turnarounds through micro-execution and team discipline. "
            "Book my keynote: https://lornettedaye.com/book\n\n"
            "#MicroExecution #TurnaroundStrategy #EdmontonOilers #PsychologyOfComebacks #FocusOnTheProcess #HighPerformance "
            "#OlympicMentalTraining #FinishStrong #LornetteDaye #CorporateSpeaker"
        )
    },
    # Post 13 (Thu, Oct 15) - Asset: oilers-03.png
    {
        "id": 13,
        "wave": "Wave 2: The Fire of Adversity & Playoff Resilience",
        "slot": "Day 13: Thursday, Oct 15, 2026 at 04:30 PM MDT",
        "dueAt": "2026-10-15T22:30:00.000Z",
        "assetFile": "oilers-03.png",
        "assetUrl": f"{CDN_BASE}/oilers-03.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "THE VALUE OF A TRUSTED CO-PILOT IN HIGH-STAKES SEASONS. ✈️🏒\n\n"
            "Every Connor McDavid needs a Leon Draisaitl. In the highest levels of athletics and corporate leadership, "
            "carrying the burden of vision alone will eventually break even the most gifted individual.\n\n"
            "When opponents focus all their checking resources on slowing down McDavid, Draisaitl steps into the breach and takes over games. "
            "When Draisaitl is targeted with physical abuse, McDavid responds with blazing counter-attacks.\n\n"
            "Who is your leadership co-pilot? Having a peer who shares your standard, absorbs pressure, and speaks candid truth "
            "is the greatest leadership asset you can cultivate.\n\n"
            "Invest in your executive partners.\n\n"
            "Respectfully,\n"
            "Lornette\n\n"
            "Invite me to keynote your upcoming executive retreat or annual conference: "
            "https://lornettedaye.com/book\n\n"
            "#LeadershipCoPilot #MutualAccountability #McDavidDraisaitl #EdmontonOilers #ExecutiveLeadership #TeamTrust "
            "#OlympicPartnership #FinishStrong #LornetteDaye #ConferenceKeynote"
        )
    },
    # Post 14 (Fri, Oct 16) - Asset: oilers-04.png
    {
        "id": 14,
        "wave": "Wave 2: The Fire of Adversity & Playoff Resilience",
        "slot": "Day 14: Friday, Oct 16, 2026 at 04:30 PM MDT",
        "dueAt": "2026-10-16T22:30:00.000Z",
        "assetFile": "oilers-04.png",
        "assetUrl": f"{CDN_BASE}/oilers-04.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "HANDLING HOSTILE STADIUM NOISE: TUNING INTO YOUR INTERNAL CHANNEL. 🏟️📢\n\n"
            "In road playoff games, twenty thousand hostile fans are screaming for your demise. "
            "The decibels shake the glass, the opposing bench chirps constantly, and every whistle is contested.\n\n"
            "If your mental channel is tuned to the crowd, your heart rate spikes, your grip tightens, and your vision narrows. "
            "Champions operate on a different frequency. They hear the noise, but they listen only to their internal system.\n\n"
            "In executive leadership, external market noise is constant: social media critics, economic speculation, and competitive threats. "
            "Train your leaders to operate on their internal compass.\n\n"
            "Filter the noise. Trust your system.\n\n"
            "With conviction,\n"
            "Lornette\n\n"
            "Empower your senior team to lead with unshakeable poise through hostile market conditions. "
            "Book my keynote: https://lornettedaye.com/book\n\n"
            "#InternalChannel #HostileEnvironments #NoiseVsSignal #EdmontonOilers #RoadPlayoffs #ExecutivePoise "
            "#EmotionalRegulation #OlympicStandard #FinishStrong #LornetteDaye"
        )
    },
    # Post 15 (Sat, Oct 17) - Asset: oilers-05.png
    {
        "id": 15,
        "wave": "Wave 2: The Fire of Adversity & Playoff Resilience",
        "slot": "Day 15: Saturday, Oct 17, 2026 at 04:30 PM MDT",
        "dueAt": "2026-10-17T22:30:00.000Z",
        "assetFile": "oilers-05.png",
        "assetUrl": f"{CDN_BASE}/oilers-05.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "BOUNCING BACK FROM GAME 7 HEARTBREAK: TURNING SCARS INTO FUEL. 💔🔥\n\n"
            "Falling short by a single goal in Game 7 of the Stanley Cup Finals is a heartbreak few human beings will ever comprehend. "
            "You gave everything you had for eleven months, fought back from the brink of elimination, and watched the silver trophy stay just out of reach.\n\n"
            "The lesser team lets that pain become permanent trauma. The championship team lets that pain become nuclear fuel.\n\n"
            "In forty years of athletics, I have seen world-record holders forged in the ashes of Olympic silver. "
            "When you understand that heartbreak is merely education, you return to the ice with terrifying resolve.\n\n"
            "Turn your heartbreak into fuel.\n\n"
            "Finish strong,\n"
            "Lornette\n\n"
            "Book my keynote on rising from devastating setbacks and rebuilding championship culture: "
            "https://lornettedaye.com/book\n\n"
            "#Game7Heartbreak #ScarsIntoFuel #EdmontonOilers #BouncingBack #ResilienceInSport #OlympicMindset "
            "#FinishStrong #LornetteDaye #ExecutiveCoaching #CorporateSpeaker"
        )
    },
    # Post 16 (Sun, Oct 18) - Asset: oilers-06.png
    {
        "id": 16,
        "wave": "Wave 2: The Fire of Adversity & Playoff Resilience",
        "slot": "Day 16: Sunday, Oct 18, 2026 at 04:30 PM MDT",
        "dueAt": "2026-10-18T22:30:00.000Z",
        "assetFile": "oilers-06.png",
        "assetUrl": f"{CDN_BASE}/oilers-06.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "THE SPECIAL TEAMS CONTRACT: DOING THE SACRED UNGLAMOROUS WORK. 🥅🏒\n\n"
            "During the Stanley Cup run, the Edmonton Oilers penalty kill went on a historic run, "
            "killing off dozens of consecutive power plays against the most dangerous offenses in the league.\n\n"
            "Penalty killing is not about dazzling skill. It is about willingness to absorb vulcanized rubber at 100 miles per hour, "
            "clearing shooting lanes, and sacrificing personal stats for the team's survival.\n\n"
            "In enterprise, your special teams are your compliance officers, your IT infrastructure engineers, "
            "and your customer service responders. When leadership honors and values the unglamorous defensive units, "
            "the entire organization develops bulletproof integrity.\n\n"
            "Honor your special teams.\n\n"
            "With respect,\n"
            "Lornette\n\n"
            "Inquire about corporate workshops on organizational integrity and team selflessness: "
            "https://lornettedaye.com/book\n\n"
            "#SpecialTeams #PenaltyKill #UnglamorousWork #EdmontonOilers #TeamIntegrity #OperationalExcellence "
            "#HighPerformanceCulture #OlympicWisdom #FinishStrong #LornetteDaye"
        )
    },
    # Post 17 (Mon, Oct 19) - Asset: oilers-07.png
    {
        "id": 17,
        "wave": "Wave 2: The Fire of Adversity & Playoff Resilience",
        "slot": "Day 17: Monday, Oct 19, 2026 at 04:30 PM MDT",
        "dueAt": "2026-10-19T22:30:00.000Z",
        "assetFile": "oilers-07.png",
        "assetUrl": f"{CDN_BASE}/oilers-07.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "THE ART OF PLAYOFF RECOVERY: SLEEP, HYDRATION, AND MENTAL UNPLUGGING. 🛌💧\n\n"
            "Playing 25 playoff hockey games in eight weeks while crossing multiple time zones destroys the human body. "
            "The team that hoists the trophy is rarely the most talented. It is the team that manages recovery with religious discipline.\n\n"
            "Between games, the Oilers coaching staff and training staff implement elite cryotherapy, nutritional protocols, "
            "and deliberate mental decompression so players can step onto the ice fully recharged.\n\n"
            "In corporate leadership, burnout is an epidemic caused by treating rest as a sign of weakness. "
            "World-class leaders know that recovery is not the absence of work. Recovery is an active performance multiplier.\n\n"
            "Rest with purpose.\n\n"
            "Stay restored,\n"
            "Lornette\n\n"
            "Book my keynote on sustainable high performance and burnout prevention for your executives: "
            "https://lornettedaye.com/book\n\n"
            "#RecoveryIsAWeapon #BurnoutPrevention #EdmontonOilers #SportsScience #HighPerformanceWellness #ExecutiveEnergy "
            "#OlympicStandard #FinishStrong #LornetteDaye #LeadershipKeynote"
        )
    },
    # Post 18 (Tue, Oct 20) - Asset: oilers-08.png
    {
        "id": 18,
        "wave": "Wave 2: The Fire of Adversity & Playoff Resilience",
        "slot": "Day 18: Tuesday, Oct 20, 2026 at 04:30 PM MDT",
        "dueAt": "2026-10-20T22:30:00.000Z",
        "assetFile": "oilers-08.png",
        "assetUrl": f"{CDN_BASE}/oilers-08.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "OVERCOMING THE EARLY SEASON HOLE: WHY NOVEMBER DOES NOT DEFINE MAY. 🍂🏆\n\n"
            "Remember early in the 2023-24 season when the Edmonton Oilers were sitting in 31st place in the league? "
            "Critics called for trades, firings, and a total rebuild. "
            "Had the leadership panicked, the season would have been lost.\n\n"
            "Instead, they changed their coaching approach, simplified their systems, and went on a historic 16-game winning streak. "
            "A poor start to your fiscal year or an ugly first quarter does not dictate your final result.\n\n"
            "What matters is your willingness to confront hard truths, adjust your tactical alignment, and trust your core people.\n\n"
            "Do not let a slow start decide your finish.\n\n"
            "In your corner,\n"
            "Lornette\n\n"
            "Schedule a keynote on strategic realignment and mid-course turnarounds: "
            "https://lornettedaye.com/book\n\n"
            "#TurnaroundLeadership #16GameStreak #EdmontonOilers #OilersNation #NeverPanic #CourseCorrection "
            "#OlympicCoaching #FinishStrong #LornetteDaye #CorporateSpeaker"
        )
    },
    # Post 19 (Wed, Oct 21) - Asset: oilers-09.png
    {
        "id": 19,
        "wave": "Wave 2: The Fire of Adversity & Playoff Resilience",
        "slot": "Day 19: Wednesday, Oct 21, 2026 at 04:30 PM MDT",
        "dueAt": "2026-10-21T22:30:00.000Z",
        "assetFile": "oilers-09.png",
        "assetUrl": f"{CDN_BASE}/oilers-09.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "THE VOICE IN THE LOCKER ROOM: SPEAKING TRUTH WHEN TENSION PEAKS. 🗣️🔒\n\n"
            "Between periods of a playoff game when things are going wrong, the worst thing a locker room can experience is polite silence. "
            "Polite silence is the signature of a dying culture.\n\n"
            "In the Oilers dressing room, leaders speak with brutal honesty, but always through a foundation of deep mutual respect. "
            "They call out missed assignments without attacking character. They demand better execution because they believe in the person.\n\n"
            "If your corporate executive team lacks the psychological safety to speak candid truth during high-stakes reviews, "
            "you are flying blind into market storms. Build a culture where candor is celebrated.\n\n"
            "Speak the truth with respect.\n\n"
            "With conviction,\n"
            "Lornette\n\n"
            "Book my keynote on radical candor and psychological safety in executive leadership: "
            "https://lornettedaye.com/book\n\n"
            "#LockerRoomCandor #PsychologicalSafety #EdmontonOilers #RadicalCandor #ExecutiveCommunication #TeamTrust "
            "#OlympicExcellence #FinishStrong #LornetteDaye #LeadershipDevelopment"
        )
    },
    # Post 20 (Thu, Oct 22) - Asset: oilers-10.png
    {
        "id": 20,
        "wave": "Wave 2: The Fire of Adversity & Playoff Resilience",
        "slot": "Day 20: Thursday, Oct 22, 2026 at 04:30 PM MDT",
        "dueAt": "2026-10-22T22:30:00.000Z",
        "assetFile": "oilers-10.png",
        "assetUrl": f"{CDN_BASE}/oilers-10.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "REMAINING POISED IN THE EYE OF THE MEDIA CYCLONE. 🌪️🎙️\n\n"
            "Playing in an obsessed hockey market like Edmonton means your every turnover, facial expression, and bench sigh "
            "is dissected across national sports radio, television panels, and digital feeds twenty-four hours a day.\n\n"
            "Connor McDavid handles media scrums with dignified, Olympian calm. "
            "He never blames officials, never throws a teammate under the bus, and never allows external narratives to alter his mission.\n\n"
            "When your brand faces public scrutiny or social media noise, your executive composure sets the tone for your entire customer base. "
            "Calm is contagious.\n\n"
            "Protect your internal peace.\n\n"
            "Finish strong,\n"
            "Lornette\n\n"
            "Train your C-suite in high-stakes executive presence and crisis communication. "
            "Book me today: https://lornettedaye.com/book\n\n"
            "#MediaPoise #ExecutivePresence #CrisisManagement #ConnorMcDavid #EdmontonOilers #CalmIsContagious "
            "#OlympicPoise #FinishStrong #LornetteDaye #KeynoteSpeaker"
        )
    },

    # =========================================================================
    # WAVE 3: THE CHAMPIONSHIP QUEST & FINISH STRONG (Days 21 - 30)
    # =========================================================================
    # Post 21 (Fri, Oct 23) - Asset: oilers-01.png
    {
        "id": 21,
        "wave": "Wave 3: The Championship Quest & Finish Strong",
        "slot": "Day 21: Friday, Oct 23, 2026 at 04:30 PM MDT",
        "dueAt": "2026-10-23T22:30:00.000Z",
        "assetFile": "oilers-01.png",
        "assetUrl": f"{CDN_BASE}/oilers-01.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "THE HUNGER FOR THE CUP: REDEFINING SUCCESS BY THE ULTIMATE PRIZE. 🏆✨\n\n"
            "Individual trophies are nice. MVP awards and scoring titles validate your talent. "
            "However, every true champion knows that personal accolades gather dust if you never hoist the collective trophy with your brothers.\n\n"
            "Connor McDavid has won every individual honor hockey can bestow. Yet, his gaze remains locked on one single piece of silver: "
            "the Stanley Cup. That singular obsession elevates the standard of everyone who wears the copper and blue jersey.\n\n"
            "In your company, do your stars care more about their individual bonuses, or are they hungry for the collective victory of the firm? "
            "When everyone aims for the same summit, greatness is the only result.\n\n"
            "Aim for the ultimate prize.\n\n"
            "With purpose,\n"
            "Lornette\n\n"
            "Bring this championship alignment framework to your company's annual conference or executive summit. "
            "Book my keynote: https://lornettedaye.com/book\n\n"
            "#StanleyCupQuest #UltimatePrize #EdmontonOilers #OilersNation #TeamBeforeSelf #ChampionshipMindset "
            "#OlympicLegacy #FinishStrong #LornetteDaye #CorporateKeynote"
        )
    },
    # Post 22 (Sat, Oct 24) - Asset: oilers-02.png
    {
        "id": 22,
        "wave": "Wave 3: The Championship Quest & Finish Strong",
        "slot": "Day 22: Saturday, Oct 24, 2026 at 04:30 PM MDT",
        "dueAt": "2026-10-24T22:30:00.000Z",
        "assetFile": "oilers-02.png",
        "assetUrl": f"{CDN_BASE}/oilers-02.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "LEADERSHIP DURING OVERTIME: WHEN FATIGUE MEETS DESTINY. ⏳🏒\n\n"
            "Sudden-death playoff overtime is the purest test of mental poise in sport. "
            "Your legs are burning, your heart is pounding against your ribs, and one single mistake ends your entire year.\n\n"
            "Great leaders do not play overtime not to lose. They play with calculated aggression to win. "
            "They lean into their instincts, trust their conditioning, and skate toward the puck with conviction.\n\n"
            "When your company is in a sudden-death negotiation or high-stakes client renewal, "
            "do your executives retreat into fear, or do they step up with championship courage?\n\n"
            "Play to win. Finish what you started.\n\n"
            "Stay bold,\n"
            "Lornette\n\n"
            "Book my keynote on decisive execution and overtime poise for your corporate event: "
            "https://lornettedaye.com/book\n\n"
            "#PlayoffOvertime #DecisiveLeadership #PlayToWin #EdmontonOilers #OilersHockey #HighStakesExecution "
            "#OlympicDiscipline #FinishStrong #LornetteDaye #ExecutiveKeynote"
        )
    },
    # Post 23 (Sun, Oct 25) - Asset: oilers-03.png
    {
        "id": 23,
        "wave": "Wave 3: The Championship Quest & Finish Strong",
        "slot": "Day 23: Sunday, Oct 25, 2026 at 04:30 PM MDT",
        "dueAt": "2026-10-25T22:30:00.000Z",
        "assetFile": "oilers-03.png",
        "assetUrl": f"{CDN_BASE}/oilers-03.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "THE POWER OF CITYWIDE BELIEF: CONNECTING TO SOMETHING BIGGER THAN YOURSELF. 🏙️🔵🟠\n\n"
            "Look at the sea of copper, blue, and orange that takes over downtown Edmonton and the entire province of Alberta during a playoff run. "
            "Grandmothers, schoolkids, tradespeople, and business leaders all united in a single heartbeat.\n\n"
            "When athletes realize they are skating for an entire community's hope and pride, "
            "fatigue disappears. You tap into a reservoir of strength that personal ambition can never unlock.\n\n"
            "Great corporate leaders do the same: they connect their teams to a noble purpose that transcends quarterly earnings. "
            "When your employees know who they are fighting for, they will run through walls for your mission.\n\n"
            "Connect to a bigger purpose.\n\n"
            "Proudly,\n"
            "Lornette\n\n"
            "Invite me to inspire and unite your global team at your next annual gathering: "
            "https://lornettedaye.com/book\n\n"
            "#CitywideBelief #EdmontonOilers #OilersNation #PurposeDrivenLeadership #AlbertaPride #CommunityImpact "
            "#OlympicSpirit #FinishStrong #LornetteDaye #KeynoteSpeaker"
        )
    },
    # Post 24 (Mon, Oct 26) - Asset: oilers-04.png
    {
        "id": 24,
        "wave": "Wave 3: The Championship Quest & Finish Strong",
        "slot": "Day 24: Monday, Oct 26, 2026 at 04:30 PM MDT",
        "dueAt": "2026-10-26T22:30:00.000Z",
        "assetFile": "oilers-04.png",
        "assetUrl": f"{CDN_BASE}/oilers-04.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "ACCOUNTABILITY WITHOUT CRUELTY: THE MARK OF A MATURE LOCKER ROOM. ⚖️🤝\n\n"
            "In toxic organizations, accountability feels like punishment and finger-pointing. "
            "In elite championship cultures like the Edmonton Oilers, accountability feels like love and shared commitment.\n\n"
            "When a teammate misses an assignment, veterans pull them aside, review the film, and say: "
            "'We need you. We believe in your game. Here is how we execute this together on the next shift.'\n\n"
            "High performance does not require cruelty. High performance requires absolute clarity wrapped in genuine belief in your people.\n\n"
            "Elevate your culture of accountability.\n\n"
            "With respect,\n"
            "Lornette\n\n"
            "Book my keynote on high-performance accountability and leadership culture: "
            "https://lornettedaye.com/book\n\n"
            "#MatureAccountability #ChampionshipCulture #EdmontonOilers #PsychologicalSafety #TeamAlignment "
            "#ExecutiveLeadership #OlympicStandard #FinishStrong #LornetteDaye"
        )
    },
    # Post 25 (Tue, Oct 27) - Asset: oilers-05.png
    {
        "id": 25,
        "wave": "Wave 3: The Championship Quest & Finish Strong",
        "slot": "Day 25: Tuesday, Oct 27, 2026 at 04:30 PM MDT",
        "dueAt": "2026-10-27T22:30:00.000Z",
        "assetFile": "oilers-05.png",
        "assetUrl": f"{CDN_BASE}/oilers-05.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "THE VETERAN PRESENCE: CALMING THE WATER IN CRITICAL STORMS. ⚓🧊\n\n"
            "While superstars like McDavid and Draisaitl drive the offensive engine, "
            "the presence of seasoned veterans in the Oilers dressing room provides the ballast that keeps the ship steady.\n\n"
            "Veterans have seen every bad bounce, every blown lead, and every playoff storm before. "
            "Their calm in the face of pressure gives younger teammates permission to breathe.\n\n"
            "In corporate enterprise, seasoned senior directors and board members must serve as that same steady ballast. "
            "Do not add fuel to the company fire. Be the calm water that quiets the storm.\n\n"
            "Be the anchor for your team.\n\n"
            "Stay steady,\n"
            "Lornette\n\n"
            "Book me to speak to your board and executive committees on crisis poise: "
            "https://lornettedaye.com/book\n\n"
            "#VeteranLeadership #SteadyBallast #EdmontonOilers #LockerRoomWisdom #CrisisPoise #ExecutiveGovernance "
            "#OlympicWisdom #FinishStrong #LornetteDaye #KeynoteSpeaker"
        )
    },
    # Post 26 (Wed, Oct 28) - Asset: oilers-06.png
    {
        "id": 26,
        "wave": "Wave 3: The Championship Quest & Finish Strong",
        "slot": "Day 26: Wednesday, Oct 28, 2026 at 04:30 PM MDT",
        "dueAt": "2026-10-28T22:30:00.000Z",
        "assetFile": "oilers-06.png",
        "assetUrl": f"{CDN_BASE}/oilers-06.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "THE POWER OF PLAYBOOK CLARITY: ELIMINATING HESITATION. 📖🏒\n\n"
            "At 25 miles per hour on the ice, hesitation is fatal. "
            "If a defenseman has to think for half a second about where his winger is breaking, the puck is already in the back of the net.\n\n"
            "The Edmonton Oilers coaching staff achieved success by stripping away convoluted systems and installing crystal-clear, "
            "instinctive breakout protocols. When players know exactly where their teammates will be, they play with blistering speed.\n\n"
            "In your company, do your frontline teams have crystal-clear role clarity? "
            "Simplicity creates speed. Complexity breeds hesitation.\n\n"
            "Simplify your playbook.\n\n"
            "With clarity,\n"
            "Lornette\n\n"
            "Learn how to simplify strategy and execute with Olympic speed across your enterprise. "
            "Book my keynote: https://lornettedaye.com/book\n\n"
            "#StrategicClarity #EliminateHesitation #SpeedOfExecution #EdmontonOilers #HockeySystems #RoleClarity "
            "#ExecutiveStrategy #FinishStrong #LornetteDaye #CorporateSpeaker"
        )
    },
    # Post 27 (Thu, Oct 29) - Asset: oilers-07.png
    {
        "id": 27,
        "wave": "Wave 3: The Championship Quest & Finish Strong",
        "slot": "Day 27: Thursday, Oct 29, 2026 at 04:30 PM MDT",
        "dueAt": "2026-10-29T22:30:00.000Z",
        "assetFile": "oilers-07.png",
        "assetUrl": f"{CDN_BASE}/oilers-07.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "RESPECTING THE OPPONENT: HUMILITY AS A WEAPON. 🤺❄️\n\n"
            "Great competitors never underestimate their rivals. "
            "When the Oilers step onto the ice against the league's best, they do not arrive with careless arrogance. "
            "They arrive with deep respect for the opponent's threats, paired with total confidence in their own preparation.\n\n"
            "Arrogance breeds laziness. True humility breeds relentless scouting, disciplined puck management, and ruthless focus.\n\n"
            "In corporate competition, never dismiss your competitors. Respect their capabilities, study their playbooks, "
            "and out-execute them with quiet, dignified excellence.\n\n"
            "Compete with humble confidence.\n\n"
            "In your corner,\n"
            "Lornette\n\n"
            "Inquire about executive keynote bookings for your national leadership meeting: "
            "https://lornettedaye.com/book\n\n"
            "#HumbleConfidence #CompetitiveStrategy #EdmontonOilers #RespectTheOpponent #ExecutiveMaturity "
            "#OlympicExcellence #FinishStrong #LornetteDaye #KeynoteSpeaker"
        )
    },
    # Post 28 (Fri, Oct 30) - Asset: oilers-08.png
    {
        "id": 28,
        "wave": "Wave 3: The Championship Quest & Finish Strong",
        "slot": "Day 28: Friday, Oct 30, 2026 at 04:30 PM MDT",
        "dueAt": "2026-10-30T22:30:00.000Z",
        "assetFile": "oilers-08.png",
        "assetUrl": f"{CDN_BASE}/oilers-08.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "THE FINAL STRETCH OF THE YEAR: FINISHING WITH MAXIMUM RESOLVE. 🏁🔥\n\n"
            "As we approach the final two days of this campaign, look at the stamina required to navigate an 82-game NHL regular season "
            "and four rounds of playoff wars.\n\n"
            "Many teams enter the final period exhausted, looking at the clock, and hoping for the horn. "
            "The Edmonton Oilers treat the final minutes as their playground. "
            "They train their minds to believe that when fatigue peaks, their competitive advantage expands.\n\n"
            "Train your people to accelerate when others are slowing down.\n\n"
            "Accelerate through the tape.\n\n"
            "Stay relentless,\n"
            "Lornette\n\n"
            "Book my Finish Strong keynote presentation to ignite your team for fourth-quarter excellence: "
            "https://lornettedaye.com/book\n\n"
            "#AccelerateThroughTheTape #FourthQuarterFinish #EdmontonOilers #EnduranceMindset #HighPerformanceHabits "
            "#OlympicDiscipline #FinishStrong #LornetteDaye #ExecutiveKeynote"
        )
    },
    # Post 29 (Sat, Oct 31) - Asset: oilers-09.png
    {
        "id": 29,
        "wave": "Wave 3: The Championship Quest & Finish Strong",
        "slot": "Day 29: Saturday, Oct 31, 2026 at 04:30 PM MDT",
        "dueAt": "2026-10-31T22:30:00.000Z",
        "assetFile": "oilers-09.png",
        "assetUrl": f"{CDN_BASE}/oilers-09.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "LEGACY IS EARNED SHIFT BY SHIFT: WRITING YOUR OWN CHAPTER. 📖🖋️\n\n"
            "Edmonton is a city steeped in hockey royalty: Wayne Gretzky, Mark Messier, Jari Kurri, Paul Coffey. "
            "Five historic Stanley Cups hang in the rafters of Rogers Place.\n\n"
            "For years, that shadow overwhelmed previous rosters. "
            "Connor McDavid and Leon Draisaitl chose not to be intimidated by the past. "
            "They chose to honor the tradition by writing their own authentic chapter of athletic greatness.\n\n"
            "Do not be paralyzed by the giants who came before you in your industry. "
            "Honor their foundation, lace up your skates, and build your own legacy.\n\n"
            "Write your chapter.\n\n"
            "Proudly,\n"
            "Lornette\n\n"
            "Bring this inspiring perspective on building organizational legacy to your leadership summit: "
            "https://lornettedaye.com/book\n\n"
            "#LegacyBuilding #WriteYourChapter #EdmontonOilers #OilersHistory #HonorThePast #BuildTheFuture "
            "#OlympicLegacy #FinishStrong #LornetteDaye #LeadershipKeynote"
        )
    },
    # Post 30 (Sun, Nov 01) - Asset: oilers-10.png
    # Note: On Nov 1, Daylight Saving Time ends in North America. MDT (UTC-6) becomes MST (UTC-7). 04:30 PM MST is 23:30 UTC.
    {
        "id": 30,
        "wave": "Wave 3: The Championship Quest & Finish Strong",
        "slot": "Day 30: Sunday, Nov 01, 2026 at 04:30 PM MST",
        "dueAt": "2026-11-01T23:30:00.000Z",
        "assetFile": "oilers-10.png",
        "assetUrl": f"{CDN_BASE}/oilers-10.png",
        "cta": "Book Keynote (lornettedaye.com/book)",
        "text": (
            "THE GRAND CLIMAX: FINISH WHAT YOU STARTED. 🏆🍁✨\n\n"
            "We conclude this 30-day Edmonton Oilers campaign with the signature principle that defines my life and coaching career: "
            "Finish Strong.\n\n"
            "The journey to the summit is never easy. You will face heartbreak. You will face 0-3 deficits. "
            "You will encounter injuries, doubt, and moments where giving up feels logical.\n\n"
            "Never concede your race. Keep your skates on the ice. Support your brothers in the huddle. "
            "And when the final buzzer sounds, let the world see that you gave every ounce of what was built inside you.\n\n"
            "To every competitor, leader, and fan reading these words: always finish what you started.\n\n"
            "Your coach and friend,\n"
            "Lornette\n\n"
            "Bring Lornette Daye to deliver the Finish Strong keynote for your corporate summit, conference, or executive retreat: "
            "https://lornettedaye.com/book\n\n"
            "#FinishStrong #LornetteDaye #EdmontonOilers #OilersNation #StanleyCupQuest #ChampionshipMindset #OlympicLegacy "
            "#FinishWhatYouStarted #KeynoteSpeaker #CorporateKeynote #HighPerformanceCulture"
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
        if "Lornette" not in t:
            raise ValueError(f"Post #{p['id']} does not have Lornette signature!")
        # Invariant 3: 100% Keynote CTA
        if "lornettedaye.com/book" not in t:
            raise ValueError(f"Post #{p['id']} is missing keynote booking CTA!")

check_invariants()
print("INVARIANTS AUDIT PASSED: 0 em dashes, all signed strictly 'Lornette', 100% Keynote CTA.")

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

    report_path = "scripts/oilers-scheduled-report.json"
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

