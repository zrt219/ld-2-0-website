# Golf V1.1 Product Design Specification: Master Discovery Sprint

**Document Type:** Master Product Discovery and Architectural Specification  
**Workstream:** 02_GOLF_V1_1  
**Status:** DISCOVERY SPECIFICATION COMPLETE (NO PRODUCTION FEATURE CODE WRITTEN)  
**Target Release:** Golf V1.1  
**Date:** 2026-09-17  
**Author:** Antigravity AI in collaboration with Performance Edge Leadership Team  

---

## 1. Executive Summary and Strategic Guardrails

### 1.1 Context and Background
The first commercial club release, 01_MVP_CLUB, is frozen in the canonical status:
`MVP IMPLEMENTATION COMPLETE - READY FOR REAL-WORLD PILOT VALIDATION`.

All four P0 items (autosave draft protection, dynamic cohort capacity, roster invitation management, mobile authentication reliability) and all three P1 items (offline quick tools, coach companion roster views, board-ready aggregate reports) have been verified with complete automated test coverage and dedicated routes.

The purpose of this Master Discovery Sprint is to rigorously design the three prioritized Golf V1.1 capabilities without prematurely writing production code, executing schema migrations, or destabilizing the proven Golf V1 baseline:
1. **Tournament Mode** (Adaptive competition-week delivery layer)
2. **Match Play Scenario Bank** (High-leverage psychological decision-making library)
3. **Variable Cadence** (Situational pre-shot routine pacing)

Two other future items remain explicitly deferred:
- **Advanced Coach Reinforcement** (P1 Coach Companion is complete; further deep practice integration is deferred to V1.2)
- **Parent Companion** (Deferred until minor-enrollment legal pathways and club pilot evidence are collected)

Workstream 03 (Italy and FIG Institutional Expansion) remains strictly decoupled as institutional research and exerts zero influence on Golf V1.1 design.

### 1.2 Core Invariants and Non-Negotiable Boundaries
- **Canonical 10-Week / 10-Foundation Lock**: Lornette's Foundation Golf program is strictly a 10-week guided athlete development program based on 10 Athletic Foundations. Golf V1.1 does not create a second curriculum, a 4-week variant, or an 8-pillar system.
- **Human-Led Coaching Model**: Technology serves Coach Lornette Daye's authoritative voice and personalized guidance. Features must enhance, not replace, human connection.
- **Strict No Em Dash Policy**: In compliance with brand editorial rules, no em dashes (the long dash character) appear anywhere in user-facing copy, prompts, or technical documentation. Clean periods, commas, colons, and separate sentences are used instead.
- **Zero Production Feature Code in Discovery**: This sprint produces architectural specifications, scenario copy, user stories, and data contracts. No database tables are altered, no production endpoints are deployed, and no UI components are pushed to the main user tree.

---

## 2. Part I: Tournament Mode Deep Discovery

### 2.1 Architectural Definition and Boundaries
Tournament Mode is not a new course, a parallel curriculum, or an alternate database track. It is a **context-sensitive presentation and execution filter** applied to the athlete's current week within the canonical 10-week program.

When an athlete is in Week 4 (Resilience After Setback) and toggles Tournament Mode:
- They remain in Week 4 of 10.
- Their Foundation 4 core video, reflection questions, and milestones remain their academic home.
- The interface adapts the weekly calendar rhythm so that high-volume LMS coursework is front-loaded to Monday and Tuesday, tactical course planning occurs on Wednesday, and Thursday through Sunday transforms into a distraction-free, one-handed mobile execution tool.

What Tournament Mode is NOT:
- Not a GPS yardage book or shot tracker.
- Not a live tournament scoring or leaderboard tool.
- Not a swing video recorder or mechanical diagnostic engine.
- Not an audio metronome (which violates USGA and R&A Rule 4.3 regarding artificial training aids during a stipulated round).

### 2.2 Activation and Scheduling Models
We evaluated four potential activation models:

#### Option A: Athlete Manual Toggle
The athlete taps a single switch in their dashboard: 'Activate Tournament Mode for this week'.
- *Pros*: Maximum autonomy; zero configuration overhead; works for unannounced qualifiers.
- *Cons*: Athletes may forget to turn it on before leaving for the course, or forget to turn it off on Sunday evening.

#### Option B: Calendar Scheduled Dates
The athlete enters tournament start and end dates (for example, July 10 to July 13). The platform automatically toggles the view on those calendar days.
- *Pros*: Set-and-forget; eliminates morning-of-round setup friction.
- *Cons*: Requires date-picking UI, time zone handling, and rain-delay schedule modifications.

#### Option C: Club / Coach Cohort-Wide Schedule Push
The Head PGA Professional or Junior Academy Director schedules a tournament week for the entire team or cohort.
- *Pros*: Synchronizes team preparation across all 20 players.
- *Cons*: Individual tournament schedules diverge significantly. While junior team players may compete on the same weekend, amateur adults have individual tournament calendars. A mandatory club-wide push disrupts players who are on an off-week.

#### Option D: Hybrid Participant Toggle with Optional Calendar Anchor (Recommended)
The athlete has direct manual control via a 1-tap toggle on their dashboard header. Optionally, they can select an event date range (for example, 'Playing this Thursday through Saturday'). The platform uses client-side local storage with Supabase synchronization to maintain state. On Sunday night at 23:59 local time, the system gracefully resets to Standard Mode for the upcoming week, with an unobtrusive prompt: 'Tournament complete. Ready to begin your weekly debrief?'

**Decision**: Implement **Option D**. It respects athlete agency, accommodates irregular competitive schedules, and prevents athletes from becoming permanently trapped in a stripped-down execution view.

### 2.3 Lifecycle State Model
Tournament Mode follows a deterministic 4-state lifecycle:

```
[State 0: INACTIVE]
       │
       ▼ (Athlete toggles ON or date range starts)
[State 1: PREPARATION (Monday to Wednesday)]
       │  - Mon/Tue: Foundation Deep Work (Video + Master Reflection)
       │  - Wed: Pre-Round Intention & Tactical Mental Strategy
       ▼ (Thursday 00:01 local or manual match start)
[State 2: COMPETITION EXECUTION (Thursday to Sunday)]
       │  - Stripped 1-tap mobile dashboard
       │  - Fast Quick Tools access (5-Sec Reset, Pre-Shot Routine, Physiological Sigh)
       │  - Zero video playback, zero essay prompts
       ▼ (Round concludes / Sunday 23:59 / Athlete taps 'Conclude Event')
[State 3: POST-ROUND DEBRIEF]
       │  - 3-Question Athlete Reflection: What did you notice? What worked? What will you repeat?
       │  - Syncs to Foundation journal
       ▼ (Completed)
[State 0: INACTIVE (Standard Week Resumes)]
```

### 2.4 Weekly Rhythm Architecture
Tournament weeks require a disciplined psychological rhythm. Forcing an athlete to watch a 14-minute video lecture on Friday morning before an 8:15 AM tee time creates cognitive fatigue and disrupts focus. The weekly cadence is structured as follows:

| Day Phase | Primary Focus | Platform Experience | Required Athlete Actions |
|---|---|---|---|
| **Monday & Tuesday: Learn & Reflect** | Foundation Mastery | Full Course Player with full video lesson, deep reflection journal, and downloadable workbook study. | Complete weekly Foundation video and draft core reflection before travel. |
| **Wednesday: Prepare** | Tactical Mental Plan | Targeted preparation card: pin sheet mental walk-through, course hazard self-talk rules, wind response plan. | Submit 1-sentence Tournament Commitment statement. |
| **Thursday to Sunday: Execute** | Pure Execution | Stripped-down execution view: large touch targets, high contrast outdoor colors, instant offline Quick Tools. | Tap reset cues between holes; zero mandatory typing during active play. |
| **Sunday Evening / Post-Round** | Grounded Integration | Calm post-competition debrief card. Low-friction structured reflection. | Complete canonical 3-question review: Notice, Worked, Repeat. |

### 2.5 Mobile One-Handed UI and Outdoor Usability Contract
During an active competition round, an athlete may check their phone between holes while walking off the green or waiting on a tee box:
1. **One-Handed Thumb Zone**: All critical actions must sit within the lower 40 percent of the viewport. Top navigation rails and dropdown menus are suppressed.
2. **Glanceability Under Direct Sunlight**: The interface utilizes an ultra-high-contrast theme: solid dark slate background (`#0A0A0B`) with bright champagne text (`#F4E4BC`) and stark white headings. No subtle low-contrast gray-on-black text.
3. **No Continuous Scrolling**: The execution screen is a single fixed viewport card with no vertical scrolling required to find the 3 primary emergency mental tools.
4. **48px Minimum Touch Targets**: Buttons have a minimum height of 52px and generous padding to accommodate cold, wet, or golf-gloved fingers.
5. **Zero Loading Spinners**: All execution tools are pre-cached locally via client service worker or local storage cache, rendering in under 50 milliseconds even in zero-cell-coverage areas on the back nine.

### 2.6 Reuse and Integration with Quick Tools
Tournament Mode does not recreate new mental tools. It serves as an ultra-fast launcher for the proven tools already implemented in `/foundations/quick-tools`:
- **5-Second Physical Reset Tool**: Shoulder drop, exhale, ground contact, target re-lock.
- **6-Step Pre-Shot Routine**: Visual pacing guide mapped to Foundation 3.
- **Physiological Sigh Audio/Visual Guide**: Double inhale through nose, extended mouth sigh to immediately down-regulate sympathetic nervous system arousal.
- **Personal Anchor Cue**: Displays the athlete's custom anchor word or phrase formulated during Foundation 2.

In Tournament Mode, these tools appear as full-screen modal overlays that can be dismissed with a single downward swipe or tap, returning immediately to the standby screen.

### 2.7 Data Model and Offline Persistence Architecture
Tournament Mode state is maintained locally in the athlete browser and synchronized with Supabase when online:

```typescript
export interface TournamentModeState {
  isActive: boolean;
  activatedAt: string | null;
  scheduledEndDate: string | null;
  tournamentName?: string;
  currentPhase: 'PREPARATION' | 'EXECUTION' | 'DEBRIEF';
  dailyCommitmentStatement?: string;
  quickToolUsageCount: {
    fiveSecondReset: number;
    physiologicalSigh: number;
    preShotRoutine: number;
  };
  postRoundDebrief?: {
    completedAt: string;
    whatNoticed: string;
    whatWorked: string;
    whatWillRepeat: string;
  };
}
```

- **Persistence Layer**: Saved immediately to `localStorage.setItem('ld_tournament_mode_state', ...)`.
- **Sync Protocol**: When online, a debounced background sync writes to the `profiles` table or a dedicated `athlete_tournament_sessions` table. If the athlete plays 18 holes in a mountain valley with no cell service, all state and reflection drafts remain secure on the device.

### 2.8 Post-Round Check-In and Reflection Protocol
Immediately following the final round, the platform does not administer a lengthy exam. It presents Coach Lornette Daye's canonical 3-dimension reflection structure:
1. **What did you notice?** (Awareness of tension, external distractions, internal dialogue)
2. **What worked?** (Which specific Performance Edge tools stabilized the round?)
3. **What will you repeat?** (The single mental habit to carry into the next practice session)

This reflection automatically flows into the athlete's permanent Foundation Journal and appears in the Coach Companion aggregate summary for weekly club review.

### 2.9 Deactivation and Graceful Return to Standard Mode
When Tournament Mode concludes:
- The athlete taps 'Finish Tournament Week' or the scheduled end date passes.
- Any unsaved reflection text is committed to the local storage draft vault.
- The dashboard seamlessly restores full navigation, lessons library, and master progress indicators (`Week X of 10`).
- No lessons are marked skipped, and no academic penalties are applied.

---

## 3. Part II: Match Play Scenario Bank Deep Discovery

### 3.1 Rules Basis and Competitive Realism
Match play is governed by specific rules and psychological pressures that do not exist in medal stroke play. To ensure complete competitive credibility with elite junior golfers, collegiate coaches, and PGA teaching staff, every scenario is grounded in official USGA and R&A Rules of Golf:
- **Rule 3.2 (Match Play)**: The state of the match (holes up or down), concession of matches, holes, and next strokes, and resolving ties.
- **Rule 5.6 (Pace of Play)**: Playing at a prompt pace. Specifically, Rule 5.6b recommends playing a shot in no more than 40 seconds; however, this is an administrative pace guideline, not a mandatory mental routine duration.
- **Rule 22 and 23 (Foursomes and Four-Ball)**: Alternate shot partner dynamics and better-ball partner support.

### 3.2 Canonical Scenario Architecture Template
Every scenario in the bank follows a standardized pedagogical structure:

```markdown
### Scenario [Number]: [Title]
- **Target Audience**: Junior competitive players, collegiate golfers, club championship finalists
- **Rules of Golf Context**: Specific USGA / R&A rule reference
- **Foundation Mapping**: Foundation X (Name)
- **Performance Edge Tool**: Specific tool utilized
- **The Critical Moment**: Vivid, realistic narrative setting the competitive stakes
- **The Psychological Dilemma**: The internal emotional conflict, temptation to panic, or loss of composure
- **Coach Lornette Principle**: The authoritative guiding philosophy
- **Decision Choice (3 Options)**:
  - Option A: Reactive / Emotional reaction (The common amateur mistake)
  - Option B: Passive / Avoidant response (Fear of failure)
  - Option C: Grounded / Controlled execution (The champion mindset response)
- **Decision Analysis**: Breakdown of why Option C preserves composure and athletic freedom
- **Athlete Reflection Prompt**: 1 targeted prompt for practice or match journaling
```

---

### 3.3 Five Full Production-Ready Draft Scenarios

#### Scenario 1: Dormie Pressure (3 Down with 3 Holes to Play)
- **Target Audience**: Competitive juniors, amateur match play qualifiers
- **Rules of Golf Context**: Rule 3.2a (Match Result: A player is 'dormie' when they lead by the same number of holes that remain to be played)
- **Foundation Mapping**: Foundation 4 (Resilience After Setback)
- **Performance Edge Tool**: Focus and Mistake Reset
- **The Critical Moment**: You stand on the 16th tee box, 3 down with 3 holes to play. Your opponent needs only a half-point on any of the remaining three holes to win the match and eliminate you from the state amateur championship. The gallery is already shifting toward the clubhouse. Your caddie looks anxious, and your inner dialogue is calculating how embarrassing it will feel to shake hands before the 17th hole.
- **The Psychological Dilemma**: The temptation to press, try an impossible hero shot, or mentally surrender because the math feels insurmountable. When an athlete plays against the outcome instead of the immediate shot, muscle tension spikes and tempo collapses.
- **Coach Lornette Principle**: 'You cannot hit a shot from hole 18 while standing on the 16th tee. You have only one ball, one target, and one swing. Play this shot with pure commitment, and let the match take care of itself.'
- **Decision Choice**:
  - *Option A (Reactive)*: Try to drive the green through a narrow tree corridor to prove you are not giving up, taking an uncalculated risk.
  - *Option B (Passive)*: Hit a tentative iron off the tee with zero commitment, secretly hoping your opponent makes a catastrophic mistake.
  - *Option C (Grounded)*: Execute your standard pre-shot routine. Pick a precise intermediate target for your normal fairway club. Take a slow physiological sigh to release neck tension. Step in and execute the exact shot required by the golf hole, completely divorcing your swing from the match score.
- **Decision Analysis**: Option C keeps the athlete anchored in present-tense execution. You cannot control your opponent's play or win three holes in one swing. By playing the 16th hole with full athletic composure, you put pressure back on the opponent to close out the match.
- **Athlete Reflection Prompt**: When was the last time scoreboard math caused you to rush or force a shot, and what physical anchor will you use next time to stay in the present?

---

#### Scenario 2: The Must-Hole 6-Foot Putt to Extend the Match
- **Target Audience**: Elite junior tournament players, tournament amateurs
- **Rules of Golf Context**: Rule 3.2b (Concession of Next Stroke: A stroke may be conceded at any time, but this 6-foot downhill slider has NOT been conceded)
- **Foundation Mapping**: Foundation 5 (Pressure, Emotional Regulation & Recovery)
- **Performance Edge Tool**: Pre-Shot Routine and Physiological Sigh
- **The Critical Moment**: You have a 6-foot downhill left-to-right putt on the 17th green to tie the hole and keep the match alive. Your opponent has already made par and is standing quietly with arms crossed near their golf bag. You can feel your heart hammering in your chest, your hands feel tight on the grip, and you catch yourself thinking: 'If I miss this, our season is over.'
- **The Psychological Dilemma**: Paralysis by analysis. Under severe pressure, golfers often stand over short putts too long, second-guessing the read, letting anxiety stiffen their forearms, and steering the putter face rather than rolling the ball.
- **Coach Lornette Principle**: 'Pressure is not an enemy to fight; it is oxygen for a prepared competitor. Settle your pulse through your breath, trust your first read, and deliver your normal stroke.'
- **Decision Choice**:
  - *Option A (Reactive)*: Freeze over the ball for 30 seconds, re-reading the line three times, and push a defensive, deceleration stroke that dies short of the cup.
  - *Option B (Rushed)*: Step up quickly and tap it with minimal routine, wanting the uncomfortable tension to be over as fast as possible.
  - *Option C (Grounded)*: Step completely behind the ball. Take one deliberate physiological sigh (double nasal inhale, smooth mouth exhale). Confirm your line to the high side of the cup. Walk into address with your standard 8-second putting cadence. Look once at the target, settle eyes on the ball, and make a committed, accelerating roll.
- **Decision Analysis**: Option C pairs autonomic nervous system regulation (the physiological sigh) with a disciplined cadence. Lengthening your time over the ball increases anxiety; rushing produces sloppy contact. Returning to your verified rhythm produces clean execution under intense duress.
- **Athlete Reflection Prompt**: What happens to your physical rhythm over short putts when the stakes rise, and what single breath cue will you lock into your putting routine?

---

#### Scenario 3: Opponent Gamesmanship and Deliberate Distraction
- **Target Audience**: Match play contenders, college invitational qualifiers
- **Rules of Golf Context**: Rule 1.2a (Standards of Player Conduct: Players are expected to play with integrity and show consideration to others)
- **Foundation Mapping**: Foundation 2 (Champion Mindset)
- **Performance Edge Tool**: Focus and Mistake Reset
- **The Critical Moment**: On the 13th hole, your opponent repeatedly coughs during your takeaway, slowly walks across your peripheral vision line while you are reading your putt, and makes passive-aggressive comments like: 'Are you sure that 7-iron is enough club over the water into this wind?' You feel a surge of irritation and anger rising in your chest.
- **The Psychological Dilemma**: Allowing an external irritant or the opponent's behavior to steal your mental energy. If you engage in an argument or allow anger to poison your focus, the opponent has successfully influenced your nervous system without hitting a single golf shot.
- **Coach Lornette Principle**: 'No one can enter your mental real estate without your permission. Treat gamesmanship as external noise, like wind or rain. Step back, reset your boundary, and let your golf club do the talking.'
- **Decision Choice**:
  - *Option A (Reactive)*: Fire a sharp verbal insult back at the opponent, slam your club into the bag, and play the shot while fueled by furious adrenaline.
  - *Option B (Passive)*: Silently suffer the distraction, hurry through your shot out of timidness, and blame the resulting flared slice on their behavior.
  - *Option C (Grounded)*: Step back from the address position immediately. Look away from the opponent toward an open horizon or distant treetop. Drop your shoulders and take a 3-second resetting breath. If a direct breach of etiquette persists, calmly address the official or state once with clear, steady posture: 'Please hold your position until I complete my stroke.' Step in with complete commitment.
- **Decision Analysis**: Option C maintains supreme emotional poise. Champions do not surrender control of their attention to anyone else on the property. Backing off the ball resets the mind and establishes firm competitive boundaries without emotional turbulence.
- **Athlete Reflection Prompt**: What specific opponent behaviors trigger your impatience or anger, and how will you physically step back and clear your mental space when it happens?

---

#### Scenario 4: Extreme Slow Play and Multi-Group Fairway Stalls
- **Target Audience**: Tournament golfers across all junior and amateur ranks
- **Rules of Golf Context**: Rule 5.6 (Pace of Play and Prompt Pace)
- **Foundation Mapping**: Foundation 3 (Discipline Systems)
- **Performance Edge Tool**: Focus and Preparation
- **The Critical Moment**: After playing the first 5 holes in steady rhythm, your group hits a massive backup on the par-3 6th tee. Two groups are waiting ahead of you. A ruling on the green stretches the delay to 24 minutes. The wind begins to gust, the temperature drops slightly, your lower back feels stiff, and players in your group start complaining about tournament officials and pace of play.
- **The Psychological Dilemma**: Allowing mental and physical lethargy to set in during prolonged dead time. Players become mentally sluggish, cold, and irritable, then step onto the tee box without re-engaging their athletic readiness.
- **Coach Lornette Principle**: 'Patience is an athletic discipline, not passive waiting. When the pace stops, disengage your mental focus, keep your body warm, and re-engage your routine only when it is your turn to play.'
- **Decision Choice**:
  - *Option A (Reactive)*: Spend the entire 24 minutes scrolling social media on your phone, complaining loudly to spectators, and then rush to hit your shot without warming up when the green clears.
  - *Option B (Passive)*: Stand motionless by your golf bag, growing increasingly tense, frustrated, and cold.
  - *Option C (Grounded)*: Put on an extra layer if breezy. Consciously disengage your intense mental focus for the first 15 minutes: sip water, eat a high-protein snack, and chat lightly about non-golf topics. When the group ahead walks off the green, perform 3 light dynamic mobility stretches, step behind your ball, activate your 6-step pre-shot routine, and hit with full intensity.
- **Decision Analysis**: Option C conserves finite mental energy. You cannot maintain acute tournament focus for 5 continuous hours. Elite athletes master the art of cycling attention: turning the focus dial down to 2 during stalls, and ramping it back to 10 when preparing to strike.
- **Athlete Reflection Prompt**: How do long waits on the golf course currently impact your physical energy and shot quality, and what will your structured wait-time routine look like?

---

#### Scenario 5: The Conceded Putt Dynamic (When 'Gimmes' Stop on the 16th Green)
- **Target Audience**: Match play contenders, amateur club champions
- **Rules of Golf Context**: Rule 3.2b (Concession of Next Stroke: A concession is made only when clearly communicated. A player must not assume a concession)
- **Foundation Mapping**: Foundation 6 (Communication & Presence)
- **Performance Edge Tool**: Decision-Making and Emotional Regulation
- **The Critical Moment**: Throughout the front nine, your opponent generously conceded all 2-foot and 3-foot putts with a friendly wave. The match is now tied on the 16th green. You hit an approach to 32 inches. You bend down casually expecting the wave, but your opponent stands silent and stone-faced, watching you mark. An uninvited thought enters your head: 'Why are they making me putt this now? That is disrespectful after what I gave them on hole 8.'
- **The Psychological Dilemma**: Feeling offended or insulted by a non-concession. When a golfer takes a strategic match-play tactic personally, resentment compromises their routine, and they rush through the short putt out of wounded pride.
- **Coach Lornette Principle**: 'Never expect a gift in competition. A concession is a privilege, never an entitlement. Respect the match, embrace every putt as your craft, and execute with absolute dignity.'
- **Decision Choice**:
  - *Option A (Reactive)*: Roll your eyes, scoff visibly, hurry up to the ball without your regular routine, and jab at it casually to show you do not care, risking a lip-out.
  - *Option B (Anxious)*: Over-analyze the 32-inch putt, doubting your stroke and feeling betrayed by the opponent's shift in demeanor.
  - *Option C (Grounded)*: Mark the ball cleanly without hesitation. Clean your ball, check the line calmly, and step behind it. Treat the 32-inch putt with the exact same professional respect and pre-shot sequence as a 20-footer. Stroke the ball into the back of the cup with solid rhythm, pick it up, and walk to the 17th tee.
- **Decision Analysis**: Option C eliminates emotional reactivity. The opponent's refusal to concede is a tactical test of your composure. By executing your standard routine with quiet dignity, you demonstrate that your confidence does not depend on their generosity.
- **Athlete Reflection Prompt**: Do you ever feel entitled to conceded putts or frustrated when forced to putt out, and how can you reframe every short stroke as an opportunity to demonstrate composure?

---

### 3.4 Four Detailed Outlines for Secondary Scenarios

#### Scenario 6: Foursomes / Alternate Shot Emotional Burden
- **Rules of Golf Context**: Rule 22 (Foursomes: Two partners compete as a side by playing one ball in alternate strokes).
- **Foundation Mapping**: Foundation 7 (Family & Community Support).
- **Performance Edge Tool**: Mistake Reset & Emotional Regulation.
- **The Moment**: In alternate shot team play, your partner hits your drive out of bounds into the deep woods on a crucial hole. You now have to drop and play stroke 3 from an awkward lie, feeling internal anger that their mistake ruined your scorecard.
- **Lornette Guidance**: In alternate shot, you share the ball, not the blame. The moment you display negative body language, your partner collapses for the rest of the day. Own the next shot with fierce love and total partnership.
- **Core Action**: High-five the partner immediately, use the 5-Second Reset to discard frustration, and focus completely on striking a great recovery shot.

#### Scenario 7: Fourball Partner Collapse
- **Rules of Golf Context**: Rule 23 (Four-Ball: Two partners compete, each playing their own ball. The side's lower score is the team score).
- **Foundation Mapping**: Foundation 1 (Identity Beyond Sport).
- **Performance Edge Tool**: Decision-Making & Confidence.
- **The Moment**: Your partner has made double bogey on three consecutive holes and has visibly checked out emotionally. You realize every remaining hole depends solely on your ball.
- **Lornette Guidance**: Do not shrink to match your partner's energy, and do not try to become Superman. Stay within your identity and your game plan. Your steady composure is the best invitation for your partner to re-engage.
- **Core Action**: Re-commit to your trusted targets rather than playing ultra-conservative or overly reckless golf.

#### Scenario 8: Sudden-Death Playoff on the First Tee
- **Rules of Golf Context**: Rule 3.2a & Committee Procedures (Hole-by-hole sudden-death playoff).
- **Foundation Mapping**: Foundation 10 (Legacy & Community Impact).
- **Performance Edge Tool**: Visualization & Pressure Response.
- **The Moment**: Tied after 18 holes, you are called immediately to the 1st tee for sudden death. A large crowd has formed around the tee box. Your name is announced over the loudspeaker.
- **Lornette Guidance**: A playoff is a privilege earned through 18 holes of grit. The crowd is there to witness athletic excellence. Embrace the stage, narrow your vision to a single target leaf, and swing with freedom.
- **Core Action**: Use the 5-Second Physical Reset on the tee box: feel feet grounded in turf, exhale, lock eyes on the target, and release all tension through the takeaway.

#### Scenario 9: National or Team Championship Deciding Match
- **Rules of Golf Context**: Rule 3.2 (Overall team match tied at 2.5 to 2.5; your individual match on the 18th hole decides the entire team championship banner).
- **Foundation Mapping**: Foundation 9 (Personal Brand & Story).
- **Performance Edge Tool**: Focus & Inner Dialogue.
- **The Moment**: Both teams and coaches are lining the 18th fairway. You need to get up and down from a greenside bunker to win the national or conference title for your school.
- **Lornette Guidance**: You have hit this bunker shot ten thousand times in practice. Your teammates believe in you because of who you are every day, not just what this sand shot does. Trust your preparation.
- **Core Action**: Visual anchor to sand entry point 2 inches behind the ball, deep belly breath, committed follow-through.

### 3.5 Delivery Architecture and Course Player Integration
The Match Play Scenario Bank is designed as a **zero-migration content enhancement**:
1. **Curriculum Mapping**: Each scenario is cataloged as an optional 'Competitive Application' exercise within its respective Foundation in the existing `/foundations/lessons` player.
2. **Interactive Composure Selector**: The player UI displays the scenario, the critical moment, and provides an interactive 3-option choice. Upon selecting an option, Coach Lornette's audio or text analysis reveals why the chosen response builds or erodes athletic composure.
3. **No Database Schema Alterations**: Responses are stored in the existing `reflections` table utilizing a JSON payload or lightweight metadata key, preserving complete backward compatibility with the V1 data contract.

---

## 4. Part III: Variable Pre-Shot Routine Cadence Deep Discovery

### 4.1 Pacing Reality vs. Rigid Artificial Clock Doctrines
In athletic sports performance, one of the most destructive coaching errors is imposing rigid, artificial stopwatch prescriptions (such as 'every pre-shot routine must take exactly 22.5 seconds'). 

Real-world tournament conditions refute rigid timing:
- **Wind Gusts**: A sudden 25 mph crosswind gust requires an athlete to pause and re-assess club selection or ball flight.
- **Lie Variations**: A clean fairway lie requires simple visualization; a buried plug in a greenside bunker requires assessing sand density and stance stability.
- **Pace of Play Rules (R&A/USGA Rule 5.6b)**: The Rules recommend playing a shot within 40 seconds of being able to play without interference. Rigidly stretching out a routine to 35 seconds on every stroke creates pace penalties and social tension within the pairing.

The objective of Foundation 3 (Discipline Systems) is **rhythmic consistency and mental commitment**, not rigid chronological uniformity. Cadence is an athletic heartbeat, not a mechanical metronome.

### 4.2 The Three Situational Cadences Defined

```
[1. STANDARD CADENCE]          [2. QUICK-TRIGGER CADENCE]         [3. BACK-OFF / RESTART CADENCE]
     (14 to 18 seconds)                 (6 to 10 seconds)                      (Deliberate Reset)
             │                                   │                                     │
   • Stand behind ball                 • Set feet and posture                 • Step away completely
   • See trajectory and shape          • One clean target look                • 3-Second physiological breath
   • Deep physiological breath         • Smooth inhale-exhale                 • Clear the disruption
   • Walk in, settle grip              • Immediate trigger swing              • Step in with fresh focus
   • 1 waggle / target check                   │                                       │
   • Committed execution                       ▼                                       ▼
             │                        [Eliminates Freeze &                   [Intentional Courage,
             ▼                         Over-Analysis on Putts]                Never a Failure]
   [The Fairway Standard]
```

#### Cadence 1: Standard Full Cadence (14 to 18 Seconds)
- **Context**: Normal tee shots, fairway approach shots, and deliberate wedge layups.
- **Phases**:
  1. *Assessment & Trajectory (Behind the ball, 4-6s)*: Stand 6 feet behind ball, pick intermediate target line, visualize ball flight.
  2. *Breath & Approach (2-3s)*: Slow physiological exhale, walk into address.
  3. *Set & Aim (3-4s)*: Align clubface to intermediate mark, set stance width.
  4. *Target Re-Check (2s)*: Look to final target, bring eyes back to ball.
  5. *Execution Trigger (1-2s)*: Smooth takeaway with zero hesitation.

#### Cadence 2: Quick-Trigger Cadence (6 to 10 Seconds)
- **Context**: Putting, short chip shots, or moments of intense pressure when standing over the ball breeds toxic doubt.
- **Phases**:
  1. *Decide Line Behind Ball (Pre-routine)*: Lock the read before stepping into address.
  2. *Step In & Set (3-4s)*: Sole the putter face square to line, settle stance.
  3. *Single Target Glance (2s)*: Look to cup to calibrate speed.
  4. *Inhale-Exhale-Stroke (2s)*: Eyes return to ball, stroke triggered immediately upon exhale. Eliminates the second-guessing that causes golfers to freeze.

#### Cadence 3: Wind / Back-Off / Restart Protocol (Step-Back Reset)
- **Context**: Gusting wind, unexpected gallery movement, sudden doubt, or poor lie realization.
- **Phases**:
  1. *Acknowledge and Step Back*: Back off the ball cleanly and decisively. Do not shuffle feet while remaining bent over the shot.
  2. *Drop the Hands*: Stand tall, let arms hang, drop shoulders.
  3. *Reset Breath (3s)*: Take a deep physiological sigh to flush adrenaline.
  4. *Re-Select Target*: Confirm club and line.
  5. *Re-Enter Address*: Walk in as if approaching a brand-new shot.

### 4.3 Mapping Cadences to Foundation 3 and the 6-Step Routine
The canonical 6-step pre-shot routine established in Foundation 3 remains the master architecture:
1. Stop & Breathe (Physiological down-regulation)
2. Read & Select (Lie, wind, distance, club)
3. Visualize Trajectory (Ball flight shape and landing zone)
4. Approach & Align (Clubface first, then stance)
5. Settle & Trust (Target lock, release muscle tension)
6. Deliver with Commitment (Uninhibited athletic execution)

Variable cadence does not alter these 6 steps. It simply adjusts the time spent in Steps 2 through 4 depending on situational demands. In the Quick-Trigger cadence, Steps 1 through 3 are completed entirely before stepping to the ball.

### 4.4 The Mental Mechanics of Backing Off
Amateur golfers often view backing off the ball as an embarrassing sign of weakness or nerves. They think: 'I should just hit it; people are waiting.' Consequently, they swing while filled with doubt and strike a terrible shot.

Under Coach Lornette Daye's framework:
- **Backing off is an act of supreme athletic discipline and self-respect.**
- If your eye catches a moving golf cart or your mind whispers 'water left' as you look at the target, swinging anyway is a surrender of mental control.
- Stepping back proves that you refuse to hit any golf shot without complete mental clarity.
- When an athlete steps back intentionally, takes a breath, and re-engages, they regain control over their performance.

### 4.5 SME Consultation Questions for Coach Lornette and PGA Staff
Before transitioning Variable Cadence to production implementation, the following 5 questions must be formally reviewed with Coach Lornette Daye and certified PGA instructors:
1. *Putting Freeze Protocol*: Do you recommend that athletes under high pressure reduce their practice strokes on the putting green, or maintain their exact practice stroke count?
2. *Wind Read Threshold*: At what wind velocity or gust variability should a junior golfer be instructed to step back and wait for a gust to pass?
3. *Back-Off Limit*: How do you coach an athlete who backs off repeatedly (3 or more times) due to chronic over-thinking, without violating Rule 5.6 pace of play?
4. *Visual Anchors*: What specific intermediate target distance (for example, 2 feet ahead vs. 6 feet ahead) does Lornette prefer for high-pressure fairway alignment?
5. *Terminology Check*: Does Coach Lornette prefer the term 'Quick-Trigger Cadence' or 'Rhythm-Lock Cadence' for putting and high-arousal execution?

---

## 5. Part IV: Integrated Architecture, Scoping and Governance

### 5.1 V1.1 Minimum Viable Scope Matrix

| Feature Component | Must Have (V1.1 Core) | Nice to Have (Post-V1.1) | Defer to V1.2+ | Rationale |
|---|---|---|---|---|
| **Tournament Mode Toggle** | Manual 1-Tap Toggle (Option D) | Automatic Calendar Schedule | Club-Wide Push Sync | Simple, resilient athlete autonomy first. |
| **Execution Screen** | 3 Big Button Tools (Reset, Sigh, Routine) | Custom Anchor Word display | Voice memo round recorder | Zero distraction on course. |
| **Post-Round Review** | Canonical 3-Question Debrief (Notice, Worked, Repeat) | Photo upload of scorecard | Automated handicap differential | Keeps focus on mental habits, not math. |
| **Match Play Scenarios** | 5 Core Written Scenarios with Lornette Audio/Text | 4 Additional Scenarios | Interactive video branch decision tree | Rich content value with zero code bloat. |
| **Variable Cadence Guide** | 3 Cadence Definitions and Step-Back Guide in F3 | Visual pacing animation in Quick Tools | Audio metronome during practice | Preserves Rules of Golf compliance. |
| **Coach Reinforcement** | Existing P1 Coach Companion roster view | Automated weekly cohort recap emails | Custom drill assignment portal | P1 already satisfies coach needs. |
| **Parent Companion** | None | Read-only junior progress digest | Parent-child messaging system | Needs legal and minor privacy clearance. |

### 5.2 Anti-Superapp Boundaries (Explicit Non-Goals)
To preserve the luxury prestige, dignified voice, and athletic focus of Lornette Daye's platform, the following product boundaries are permanently locked:
- **No GPS Rangefinders or Satellite Maps**: We do not compete with Arccos, 18Birdies, or Bushnell.
- **No Swing Video Analysis or AI Pose Estimation**: Mechanical swing instruction is the domain of the club's PGA teaching professional. Lornette coaches the mind, composure, and identity.
- **No Live Scoring or Handicap Calculation**: We do not build scorecards or compete with Golf Genius or the USGA GHIN system.
- **No Social Feeds or Public Leaderboards**: The athlete's reflection journal is private and sanctuary-grade. We will never add social likes, public comments, or competitive comparison feeds.
- **No In-Round Audio Signals**: No beeps, metronome clicks, or alerts during competitive rounds.

### 5.3 Privacy, Confidentiality and Outdoor Accessibility
1. **Sanctuary-Grade Reflection Privacy**:
   - Athlete reflections submitted during tournament debriefs are visible only to the athlete and Coach Lornette Daye.
   - Club PGA coaches see only aggregated participation counts and completion percentages through the P1 Coach Companion. Coaches NEVER see personal reflection text or emotional self-talk notes.
2. **Outdoor Sun Visibility**:
   - Background: Dark obsidian (`#0A0A0B`).
   - Primary Text: High-luminance champagne (`#F4E4BC`) with 12.8:1 contrast ratio against background (far exceeding WCAG AAA standard of 7:1).
   - Touch Target Minimum: 48px by 48px bounding box with 16px spatial padding.
3. **One-Handed Usability**:
   - Key interaction targets positioned in the lower thumb zone (bottom 250px of mobile screen).

### 5.4 Failure States, Offline Degradation and Error Recovery
- **Offline Round in Dead Zone**: When cell reception drops on the course, the service worker serves cached Quick Tools instantly. Local storage records reset button taps and drafts.
- **Accidental Toggle**: If an athlete accidentally toggles Tournament Mode on Monday, a confirmation toast provides a 1-tap 'Undo' action, and navigation to the full curriculum is never disabled.
- **Browser Crash / Battery Depletion**: If an athlete's phone dies on the 14th hole, upon recharging and reopening the browser, the exact state and any drafted notes are restored from the local storage vault without data loss.

### 5.5 Pilot Validation Protocol and Questions for Partner Clubs
During the upcoming pilot validation phase with partner clubs (such as Mountain Ridge Country Club), the following questions will be evaluated:
1. Did junior tournament players open the app during tournament travel days, or did they experience app friction?
2. Did coaches feel Tournament Mode complemented or conflicted with their on-site tournament coaching?
3. How many athletes used the 5-Second Reset or Physiological Sigh during competitive tournament weeks?
4. Did players report feeling pressured to complete reflections during tournament play, or did the Wednesday-to-Sunday rhythm alleviate academic guilt?

### 5.6 Complete User Stories

#### Story 1: Competitive Junior Tournament Golfer
*As an* elite 16-year-old junior golfer competing in a 36-hole American Junior Golf Association (AJGA) invitational,  
*I want* my Foundation dashboard to hide lengthy video coursework starting Thursday and give me immediate 1-tap access to my 5-Second Reset and Physiological Sigh tools,  
*So that* I can stay mentally composed on the golf course without feeling guilty about school or LMS assignments during competition.

#### Story 2: Head PGA Golf Professional
*As a* Director of Golf managing 20 junior academy golfers,  
*I want* to know that my athletes are practicing elite mental routines during tournament weeks without the platform interfering with our tactical swing game plan,  
*So that* our club's competitive performance and tournament composure improve measurably.

#### Story 3: Adult Amateur Club Championship Competitor
*As a* competitive amateur golfer playing in the semi-finals of our annual club championship,  
*I want* realistic match-play composure scenarios that teach me how to respond when my opponent stops conceding short putts or attempts deliberate gamesmanship,  
*So that* I do not surrender my emotional stamina or waste energy on frustration.

### 5.7 Domain TypeScript Specifications (Specification Only)
These interfaces define the domain contracts for future V1.1 implementation:

```typescript
// Specification only: Not deployed to production in this sprint

export type TournamentModePhase = 'LEARN' | 'PREPARE' | 'EXECUTE' | 'DEBRIEF';

export interface TournamentConfiguration {
  id: string;
  athleteId: string;
  cohortId?: string;
  eventName: string;
  startDate: string; // ISO 8601 Date
  endDate: string;   // ISO 8601 Date
  activeFoundationWeek: number; // 1 to 10
  currentPhase: TournamentModePhase;
  commitmentStatement?: string;
  isCompleted: boolean;
}

export interface MatchPlayScenario {
  id: string;
  scenarioNumber: number;
  title: string;
  rulesContext: string;
  foundationWeek: number; // 1 to 10
  performanceEdgeTool: string;
  criticalMomentText: string;
  dilemmaText: string;
  lornettePrinciple: string;
  options: {
    id: 'A' | 'B' | 'C';
    type: 'REACTIVE' | 'PASSIVE' | 'GROUNDED';
    label: string;
    analysis: string;
  }[];
  reflectionPrompt: string;
}

export interface VariableCadenceDefinition {
  id: 'standard' | 'quick_trigger' | 'back_off_reset';
  name: string;
  typicalDurationSeconds: { min: number; max: number };
  bestUsedFor: string[];
  steps: {
    stepNumber: number;
    name: string;
    description: string;
    breathCue?: string;
  }[];
}
```

### 5.8 Route and View Decisions
To preserve Next.js 16 Server Component boundaries and prevent route bloat, Tournament Mode will be delivered as:
1. **Primary Route**: `/foundations/tournament`
   - Dedicated, lightweight Server Component wrapper.
   - Consumes the authenticated athlete session via `@supabase/ssr`.
   - Uses the existing `LearnerShell` visual design tokens with minimal headers.
2. **Dashboard Quick Toggle**:
   - On `/foundations/dashboard`, a discreet status pill in the top banner reads: `Tournament Mode: Active (Week 4)`.
   - Clicking the pill toggles between the full dashboard view and the streamlined execution interface without requiring page reloads.

---

## 6. Next Steps and V1.1 Decision Gate Transition

With the completion of this Master Discovery Specification:
1. **01_MVP_CLUB Remains Frozen**: Production pilot validation can proceed without distraction.
2. **Backlog Transition**: The items in `LORNETTES_FOUNDATION/02_GOLF_V1_1/` are updated to cite this specification.
3. **Lornette Daye & PGA Review**: Present the 5 draft match play scenarios and 5 SME cadence questions to Coach Lornette Daye and certified PGA staff for editorial approval.
4. **No Code Written**: The codebase remains completely clean, with 0 new production feature files, 0 database migrations, and 0 lint or typecheck regressions.
