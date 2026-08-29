/**
 * Automated LinkedIn Post Scheduler for Lornette Daye
 * 
 * Campaign: Melissa Vargas - Power, Pressure, Performance
 * Scope: 21 Days (3 Weeks), 3 Posts/Day (6:00 PM, 7:00 PM, 8:00 PM MDT) = 63 Posts
 * Channel: Lornette D (LinkedIn) via Buffer GraphQL API
 */

import fs from 'fs';
import path from 'path';

const BUFFER_ACCESS_TOKEN = process.env.BUFFER_ACCESS_TOKEN || 'mLbjEsRdn5FKtGOskFoGzK-gW2CGTl8dfAK8klDVEPC';
const BUFFER_API_URL = 'https://api.buffer.com';
const CHANNEL_ID = '6a39d30c5ab6d2f1065f5301';
const BASE_IMAGE_URL = 'https://lornettedaye.com/campaigns/vargas';

// Generate MDT ISO string for a given date offset and hour (18, 19, 20)
// Mountain Daylight Time (MDT) is UTC-6.
function getDueAt(dayOffset, hour) {
  // Base date: August 28, 2026
  const year = 2026;
  const month = 7; // August (0-indexed)
  const baseDay = 28;

  const targetDate = new Date(Date.UTC(year, month, baseDay + dayOffset, hour + 6, 0, 0, 0));
  return targetDate.toISOString();
}

// 63 Custom Captions in Lornette Daye's voice (40+ years experience, Olympian coach, National Champion)
const campaignPosts = [
  // ==========================================
  // WEEK 1: HIGH-PERFORMANCE, POWER & GRIT
  // ==========================================
  {
    imageIndex: 1, // vargas-01
    text: `In over 40 years around elite athletics, I have seen thousands of athletes with talent. But the world only remembers the ones who turn raw power into relentless execution.

Melissa Vargas doesn't just step onto the court—she commands the atmosphere. When power meets unwavering discipline, the outcome isn’t luck; it’s inevitable.

What standard are you setting in your arena today?

Learn more about building high-performance resilience at lornettedaye.com

#LornetteDaye #HighPerformance #Leadership #Resilience #MelissaVargas #Volleyball #AthleticMindset`,
  },
  {
    imageIndex: 2, // vargas-02
    text: `33 points in a championship final isn’t just an athletic stat—it is a masterclass in staying locked in when the lights are brightest.

As a former national sprint champion and coach, I know that championship moments aren't won during the final set. They are won in the thousands of unseen hours before anyone turned the cameras on.

Excellence is never an accident. It is a decision repeated daily.

Explore keynote speaking and leadership programs: lornettedaye.com/speaking

#LornetteDaye #MentalToughness #HighPerformance #KeynoteSpeaker #ChampionshipMindset #VNL #Resilience`,
  },
  {
    imageIndex: 3, // vargas-03
    text: `When the pressure rises, some people pull back. Champions elevate.

Watching Melissa Vargas drop 33 points to take MVP honors in the VNL Final reminds us of a fundamental rule in sports and in life: Pressure doesn't create character; it reveals preparation.

When the stakes get high in your career or organization, do you shrink, or do you rise?

Read more insights on overcoming pressure: lornettedaye.com/blog

#LornetteDaye #ExecutiveCoaching #PeakPerformance #LeadershipDevelopment #MelissaVargas #PressureIsAPrivilege`,
  },
  {
    imageIndex: 4, // vargas-04
    text: `Number 4. Power from the service line. Power above the net. Power when it matters most.

There is nothing ordinary about someone who has learned to trust their preparation completely. When you align explosive strength with sharp mental clarity, you become undeniable.

Stop waiting for permission to step into your full capability. Own your space.

Connect with Lornette Daye for team and executive coaching: lornettedaye.com/athlete-coaching

#LornetteDaye #YouthMentorship #HighPerformanceCoaching #Unstoppable #Volleyball #AthleticExcellence`,
  },
  {
    imageIndex: 5, // vargas-05
    text: `Winning an MVP title is impressive. Doing it back-to-back across multiple seasons proves it was never a fluke.

Some athletes reach the moment. True leaders become the moment.

Consistency is the rarest currency in performance. If you want sustainable success, fallen momentum cannot be your excuse. Build habits that outlast the hype.

Discover practical strategies for sustained excellence: lornettedaye.com

#LornetteDaye #Consistency #LeadershipExcellence #FinishStrong #MVP #SustainedPerformance #WorkEthic`,
  },
  {
    imageIndex: 6, // vargas-06
    text: `Istanbul. The home court. The world stage.

When you wear the colors of your team or your community, you carry something bigger than individual ambition. Melissa Vargas stepping onto the court in Türkiye red shows what happens when purpose meets platform.

When your "why" is bigger than yourself, fatigue takes a back seat.

Bring transformational leadership to your next conference: lornettedaye.com/speaking

#LornetteDaye #PurposeDriven #TeamCulture #EuroVolley #RepresentationMatters #InclusionInSport`,
  },
  {
    imageIndex: 7, // vargas-07
    text: `She doesn't just score points—she changes what a match feels like.

True game-changers don't just participate in the tempo; they dictate it. Whether it's 33 points in a VNL final or 24 against Hungary, the presence of a determined leader shifts the energy of everyone around them.

Are you reacting to the environment around you, or are you setting the tone?

Explore leadership and culture workshops at lornettedaye.com/programs

#LornetteDaye #ToneSetter #LeadershipMindset #CultureMatters #AthleticLeadership #MelissaVargas`,
  },
  {
    imageIndex: 8, // vargas-08
    text: `From Cuba to Türkiye to the top of the world.

Talent can begin anywhere, but opportunity and courage change everything. Melissa Vargas's journey is proof that when you refuse to let boundaries define your ceiling, your impact becomes global.

Your starting point does not dictate your finish line. Keep running your race.

Learn more about Lornette's story of resilience: lornettedaye.com/about

#LornetteDaye #Resilience #ImmigrantGrit #GlobalImpact #OvercomingObstacles #FinishStrong #Inclusion`,
  },
  {
    imageIndex: 9, // vargas-09
    text: `Great seasons happen. Greatness repeats.

In 40 years of sprinting, coaching, and mentoring, I have seen many people flash brilliance for a season. But repeating it year after year requires a different level of humility, recovery, and focus.

Stay hungry, especially after you win.

Book Lornette Daye for your next keynote: lornettedaye.com/book

#LornetteDaye #RepeatChampion #LegacyMindset #KeynoteSpeaker #HighPerformanceHabits #Discipline`,
  },
  {
    imageIndex: 10, // vargas-10
    text: `24 Points. 5 Aces. 3 Sets.

Melissa Vargas isn't waiting for the tournament to heat up—she brings the heat from the very first whistle.

High performers do not ease into challenges; they attack the start with decisive precision. How you start often dictates how you finish.

Start with purpose today.

Check out Lornette's book 'Finish Strong' at lornettedaye.com/books

#LornetteDaye #FinishStrong #StartDecisive #FastStart #Volleyball #EuroVolley2026 #PerformanceCoaching`,
  },
  {
    imageIndex: 11, // vargas-11
    text: `Power. Timing. Nerve.

Big moments don't negotiate. They demand that your physical readiness and your mental calm meet in a single fraction of a second.

Melissa Vargas was built for big moments because she respects the craft behind the scenes. Trust your training and take your shot.

Elevate your athletes and leaders: lornettedaye.com/athlete-coaching

#LornetteDaye #BigMoments #Composure #MentalConditioning #EliteAthlete #SportsPsychology`,
  },
  {
    imageIndex: 12, // vargas-12
    text: `Composure. Force. Finish.

This is what pressure looks like when it has been mastered. When chaos is swirling in the arena, the greatest athletes find stillness inside.

Learn to quiet the external noise so your execution remains razor sharp.

Deepen your focus with Lornette Daye's keynote sessions: lornettedaye.com/speaking

#LornetteDaye #FocusUnderFire #Composure #LeadershipPresence #KeynoteSpeaking #PeakState`,
  },
  {
    imageIndex: 13, // vargas-13
    text: `The match turns when she does.

Every winning team has an anchor—someone whose body language and relentless drive spark belief across the entire roster. 

When things get tough, be the person whose energy lifts the room, not drains it.

Strengthen your team dynamics: lornettedaye.com/programs

#LornetteDaye #TeamAnchor #LeadershipCulture #BodyLanguage #CompetitiveDrive #VolleyballStar`,
  },
  {
    imageIndex: 14, // vargas-14
    text: `Serve. Strike. Silence.

When the ball leaves Melissa Vargas's hand, the momentum of the match shifts immediately. That level of impact comes from years of refining the fundamentals.

Never outgrow the basics. The fundamentals are what protect you under maximum stress.

Master the fundamentals of resilience: lornettedaye.com/blog

#LornetteDaye #FundamentalsFirst #Precision #PowerServe #MasterTheCraft #VolleyballSkills`,
  },
  {
    imageIndex: 15, // vargas-15
    text: `Red hot. Ice cold.

Fire in the execution. Total calm in the mind.

The best competitors operate in that exact paradox—intense passion for the goal, combined with absolute emotional control under pressure.

How are you balancing intensity and poise in your daily leadership?

Explore performance coaching at lornettedaye.com

#LornetteDaye #EmotionalIntelligence #HighPerformanceLeadership #PoiseUnderPressure #MelissaVargas`,
  },
  {
    imageIndex: 16, // vargas-16
    text: `Point after point.

Pressure doesn't slow elite performers down; it sharpens their vision. When you embrace friction as feedback rather than a roadblock, you accelerate your growth.

Don't run from the friction. Use it to sharpen your edge.

Read Lornette's articles on athletic mindset: lornettedaye.com/blog

#LornetteDaye #FrictionToFocus #GrowthMindset #SharpenYourEdge #AthleteLife #Resilience`,
  },
  {
    imageIndex: 17, // vargas-17
    text: `Big stage. Bigger presence.

Some players arrive at the arena. Others own it from the second their shoes hit the floor.

Presence isn't about arrogance—it's the quiet certainty that you have put in the work and you belong in the room. Walk into your rooms with confidence today.

Book Lornette Daye for leadership keynotes: lornettedaye.com/book

#LornetteDaye #ExecutivePresence #OwnTheRoom #QuietConfidence #KeynoteSpeaker #Leadership`,
  },
  {
    imageIndex: 18, // vargas-18
    text: `No fear at the line. The calm before the ace.

Standing at the service line with thousands watching requires an unshakeable breath and absolute trust in muscle memory.

When it's your turn to step up to the line, take a breath, trust your preparation, and execute.

Discover youth mentorship & empowerment programs: lornettedaye.com/mentorship

#LornetteDaye #NoFear #AceMindset #TakeTheShot #YouthEmpowerment #MentalDiscipline`,
  },
  {
    imageIndex: 19, // vargas-19
    text: `Every eye. One star.

When the arena rises, Melissa Vargas rises higher. True champions elevate everyone who comes to watch them compete.

Are you inspiring those who look up to you to reach for higher ground?

Connect with Lornette Daye: lornettedaye.com

#LornetteDaye #InspirationInAction #RoleModel #HighJump #ElevateOthers #VolleyballWorld`,
  },
  {
    imageIndex: 20, // vargas-20
    text: `She raises the level.

The standard of the entire game changes when an elite competitor steps on court. That is what transformative leadership looks like in sport and business.

Raise the standard in your organization today.

Discover Lornette's impact and mission: lornettedaye.com/impact

#LornetteDaye #RaiseTheStandard #CultureShift #TransformativeLeadership #HighStandards`,
  },
  {
    imageIndex: 1, // vargas-01
    text: `As we wrap up Week 1 of our high-performance focus: remember that power without discipline is wasted motion.

Melissa Vargas proves that raw athletic gifts only reach legendary status when paired with relentless, day-in, day-out commitment.

Keep building the habits that make your success inevitable.

Visit lornettedaye.com for keynotes, workshops, and coaching.

#LornetteDaye #HighPerformanceHabits #DisciplineEqualsFreedom #WeeklyReflection #MelissaVargas`,
  },

  // ==========================================
  // WEEK 2: MENTAL TOUGHNESS & RESILIENCE UNDER FIRE
  // ==========================================
  {
    imageIndex: 2, // vargas-02
    text: `Week 2 Focus: Mental Toughness Under Fire.

When the scoreboard shows the final set, numbers like 33 points don't happen because an athlete is lucky. They happen because fatigue was conquered in the mind long before the body gave in.

What mental hurdles are you pushing past this week?

Keynotes and workshops: lornettedaye.com/speaking

#LornetteDaye #MentalToughness #OvercomeFatigue #MindOverMatter #HighPerformance #Volleyball`,
  },
  {
    imageIndex: 3, // vargas-03
    text: `Pressure is not a penalty. It is the greatest validator of how far you have come.

When Melissa Vargas steps up in the VNL Final, she welcomes the weight of the moment. If you want to achieve extraordinary results, you have to learn to embrace the heat.

Transform pressure into your greatest competitive advantage: lornettedaye.com/athlete-coaching

#LornetteDaye #EmbraceTheHeat #CompetitiveAdvantage #LeadershipUnderPressure #FinishStrong`,
  },
  {
    imageIndex: 4, // vargas-04
    text: `Power isn't just physical force—it's mental certainty.

When you see Number 4 step up, you see someone whose mind has already executed the play a hundred times before the whistle blows. Mental rehearsal is the secret weapon of champions.

Train your mind with the same rigor you train your craft.

Read Lornette's insights on champion visualization: lornettedaye.com/blog

#LornetteDaye #MentalRehearsal #Visualization #SportsPsychology #MindsetMatters #MelissaVargas`,
  },
  {
    imageIndex: 5, // vargas-05
    text: `Repeating an MVP milestone isn't about doing something brand new—it’s about refusing to lower your standards after the world applauds.

Complacency is the silent killer of great teams and promising careers. Keep your hunger sharper than your trophy case.

Develop enduring leadership stamina: lornettedaye.com/programs

#LornetteDaye #NoComplacency #StayHungry #StandardOfExcellence #LeadershipStamina`,
  },
  {
    imageIndex: 6, // vargas-06
    text: `Playing on home soil in front of thousands brings massive expectations. But great athletes turn home crowd energy into fuel rather than fear.

How are you channeling external expectations in your career? Don't let expectations weigh you down—let them propel you forward.

Learn about team alignment and executive keynotes: lornettedaye.com/speaking

#LornetteDaye #ExpectationsIntoFuel #Focus #EuroVolley #TurkiyeVolleyball #ChampionshipMindset`,
  },
  {
    imageIndex: 7, // vargas-07
    text: `Impact is measured in how the team responds when adversity strikes.

When the score is tight and momentum is slipping, true anchors don't panic. They reset, look their teammates in the eyes, and raise the standard.

Be the calming, decisive force your team needs when the storm hits.

Explore Lornette's leadership framework: lornettedaye.com

#LornetteDaye #CrisisLeadership #CalmInTheStorm #AnchorYourTeam #ResilienceInAction`,
  },
  {
    imageIndex: 8, // vargas-08
    text: `Resilience is forged when you have to adapt to entirely new terrains.

From Cuba to international arenas to leading Türkiye, Melissa Vargas has embraced change with immense grace and grit. In life and leadership, your ability to adapt determines your longevity.

Adaptability is the cornerstone of true resilience.

Discover Lornette's journey in 'Surviving Life': lornettedaye.com/books

#LornetteDaye #Adaptability #Grit #SurvivingLife #OvercomingOdds #LifeLessonsFromSport`,
  },
  {
    imageIndex: 9, // vargas-09
    text: `Consistency over hype.

Anyone can have a hot streak. But sustained champions show up on the rainy Tuesday mornings when nobody is watching and enthusiasm has worn off.

Commit to the process, not just the applause.

Book Lornette Daye for your next event: lornettedaye.com/book

#LornetteDaye #ProcessOverApplause #ConsistencyIsKey #UnseenHours #SprintMindset #Excellence`,
  },
  {
    imageIndex: 10, // vargas-10
    text: `5 aces in 3 sets isn't luck—it's ruthless precision under competitive stress.

When the pressure peaks, do you rush your process, or do you slow your breathing down and trust your mechanics?

Trust the mechanics you have built over years of dedication.

Coaching and mentoring programs: lornettedaye.com/mentorship

#LornetteDaye #PrecisionUnderPressure #TrustTheMechanics #AthleticDiscipline #VolleyballLife`,
  },
  {
    imageIndex: 11, // vargas-11
    text: `Big moments don't care about excuses. They only recognize execution.

Melissa Vargas thrives on the biggest stages because she treats every practice repetition as if the gold medal were on the line.

Treat the small moments with championship reverence, and the big moments will take care of themselves.

Keynote speaker profile & booking: lornettedaye.com/speaker-kit

#LornetteDaye #NoExcuses #BigStageReady #ChampionshipReverence #KeynoteSpeaker #Leadership`,
  },
  {
    imageIndex: 12, // vargas-12
    text: `Composure is a trained skill.

When the stakes are high, amateur minds panic while master minds slow time down. That stillness in the middle of chaos is what separates good from legendary.

Train your composure every single day.

Read more at lornettedaye.com/blog

#LornetteDaye #TrainedComposure #MindfulExecution #SportsScience #PeakPerformanceMindset`,
  },
  {
    imageIndex: 13, // vargas-13
    text: `Energy is contagious. When one player refuses to lose, it shifts the entire collective belief of the team.

Be the catalyst for belief in your workplace, your home, and your community.

Empower your community and youth leaders: lornettedaye.com/mentorship

#LornetteDaye #BeliefIsContagious #CatalystForChange #YouthLeadership #TeamEnergy`,
  },
  {
    imageIndex: 14, // vargas-14
    text: `Silence the doubt. Strike with conviction.

When you hesitate, you give away your power. When you commit fully to the decision, the outcome aligns with your intention.

Stop second-guessing your potential. Strike with conviction.

Explore keynote topics: lornettedaye.com/speaking

#LornetteDaye #DecisiveLeadership #NoHesitation #Conviction #HighPerformanceMindset`,
  },
  {
    imageIndex: 15, // vargas-15
    text: `Cool head, fiery heart.

That is the balance that sustained my athletic career across 4 decades and continues to guide my coaching today. Passion gives you drive; calm gives you accuracy.

Never let anger or anxiety hijack your technique.

Learn more about athletic mindset coaching: lornettedaye.com/athlete-coaching

#LornetteDaye #CoolHeadFieryHeart #EmotionalBalance #TechniqueUnderPressure #CoachLornette`,
  },
  {
    imageIndex: 16, // vargas-16
    text: `Every point is a fresh start.

One of the hardest lessons in elite sport is learning to flush mistakes instantly. Melissa Vargas doesn't carry the previous error into the next spike—she attacks the next ball with clean clarity.

Don't let yesterday's mistake steal today's victory.

Read 'Finish Strong': lornettedaye.com/books

#LornetteDaye #NextPlaySpeed #FlushTheMistake #MentalAgility #FinishStrong #Volleyball`,
  },
  {
    imageIndex: 17, // vargas-17
    text: `When you step into your arena, make your presence felt before you even touch the ball.

True leadership presence radiates from preparation, respect for the opponent, and uncompromising self-belief.

Walk tall into every challenge this week.

Connect at lornettedaye.com

#LornetteDaye #LeadershipPresence #SelfBelief #UncompromisingStandards #OlympicMindset`,
  },
  {
    imageIndex: 18, // vargas-18
    text: `The line between fear and focus is where champions live.

Standing at the service line, fear says "what if you miss?" Focus says "execute the rhythm." Always choose rhythm over fear.

Choose rhythm over fear in your big decisions today.

Explore programs: lornettedaye.com/programs

#LornetteDaye #RhythmOverFear #ServiceLineFocus #FocusOnTheProcess #Empowerment`,
  },
  {
    imageIndex: 19, // vargas-19
    text: `Greatness is not about outshining others—it is about illuminating what is possible for everyone around you.

When Melissa Vargas flies above the net, she inspires a whole generation of young girls to dream without limits.

Who are you inspiring with your effort today?

Youth development & impact: lornettedaye.com/impact

#LornetteDaye #WomenInSports #InspireTheNextGeneration #YouthDevelopment #Representation`,
  },
  {
    imageIndex: 20, // vargas-20
    text: `When you raise your personal standard, you give everyone on your team permission to do the same.

Leadership is never about words; it is about the standard you embody when nobody is forcing you to work.

Embody the standard you wish to see.

Learn more at lornettedaye.com

#LornetteDaye #EmbodyTheStandard #LeadByExample #CultureOfExcellence #FinishStrong`,
  },
  {
    imageIndex: 1, // vargas-01
    text: `End of Week 2 reflection:

Resilience isn't just about bouncing back—it is about bouncing forward with greater clarity and sharper purpose.

Keep pushing your boundaries. You are built for more.

Visit lornettedaye.com for coaching, books, and keynotes.

#LornetteDaye #BounceForward #ResilienceInSport #LifeLeadership #MelissaVargas`,
  },

  // ==========================================
  // WEEK 3: COACHING, LEADERSHIP & LONG-TERM LEGACY
  // ==========================================
  {
    imageIndex: 2, // vargas-02
    text: `Week 3 Focus: Coaching, Leadership & Enduring Legacy.

When you look at Melissa Vargas's historic 33-point VNL Final record, you see the result of years of coaching, trust, and mutual accountability.

Great champions aren't built in isolation—they are shaped by mentors who saw their greatness before they fully saw it themselves.

Who are you mentoring today?

Mentorship & youth leadership programs: lornettedaye.com/mentorship

#LornetteDaye #MentorshipMatters #CoachingExcellence #LegacyLeadership #YouthMentorship`,
  },
  {
    imageIndex: 3, // vargas-03
    text: `In 40+ years of coaching athletes and speaking to corporate teams, one truth remains timeless: 

When the pressure hits maximum, you don't rise to the occasion—you sink to the level of your training.

Make sure your daily training is rigorous enough to hold you when the storm comes.

Strengthen your foundation with Lornette Daye: lornettedaye.com/athlete-coaching

#LornetteDaye #LevelOfTraining #DailyHabits #PeakPreparation #KeynoteSpeaker #CoachingWisdom`,
  },
  {
    imageIndex: 4, // vargas-04
    text: `Number 4 on the court, Number 1 in dedication.

Talent without work ethic is wasted opportunity. But when you match world-class talent with unshakeable discipline, you write history.

Never let someone outwork your talent.

Explore Lornette's corporate speaking topics: lornettedaye.com/speaking

#LornetteDaye #WorkEthic #WriteHistory #UnshakeableDiscipline #ExecutiveCoaching`,
  },
  {
    imageIndex: 5, // vargas-05
    text: `The true test of an MVP is how much better they make their teammates look.

Melissa Vargas draws defenders, creates space, and breathes confidence into every rotation. That is the hallmark of transformational leadership.

Are you creating space for your teammates to shine?

Discover team leadership keynotes at lornettedaye.com

#LornetteDaye #TransformationalLeadership #TeamFirst #EmpowerOthers #MVPSpirit`,
  },
  {
    imageIndex: 6, // vargas-06
    text: `Wearing the jersey is an honor; defending the culture is a duty.

Whether on the international volleyball court or in your local organization, culture is built on mutual respect, relentless effort, and shared purpose.

Protect and elevate your culture every single day.

Learn about inclusion and culture programs: lornettedaye.com/inclusion

#LornetteDaye #CultureOfRespect #SharedPurpose #TeamJersey #InclusionMatters`,
  },
  {
    imageIndex: 7, // vargas-07
    text: `Numbers tell part of the story, but impact tells the whole truth.

33 points in a final or 24 against Hungary are headlines, but the heart behind those points is what captures the world.

Play with heart. Lead with authenticity.

Connect with Lornette Daye for your next keynote: lornettedaye.com/book

#LornetteDaye #AuthenticLeadership #PlayWithHeart #LeadWithPurpose #KeynoteSpeaker`,
  },
  {
    imageIndex: 8, // vargas-08
    text: `A journey from Cuba to international stardom teaches us that boundaries exist only in geography, never in human capability.

When young athletes ask me how to navigate systemic barriers, I tell them: Root your identity in faith, discipline, and purpose, and no barrier can permanently stop you.

Unleash your true potential: lornettedaye.com/about

#LornetteDaye #OvercomingBarriers #FaithAndDiscipline #HumanPotential #FinishStrong`,
  },
  {
    imageIndex: 9, // vargas-09
    text: `2023 MVP. 2026 MVP.

The mark of a true master is that they continue refining the nuances of their craft even after they reach the mountaintop.

What skill are you committed to mastering this month?

Explore executive coaching programs: lornettedaye.com/athlete-coaching

#LornetteDaye #Mastery #ContinuousImprovement #KaizenMindset #ExecutiveExcellence`,
  },
  {
    imageIndex: 10, // vargas-10
    text: `Aces don't happen by swinging wildly. They happen through intentional angle, speed, and focus.

In your business and career, stop swinging wildly at every distraction. Focus on the high-leverage actions that move the needle.

Refine your strategic focus: lornettedaye.com

#LornetteDaye #StrategicFocus #IntentionalAction #HighLeverage #LeadershipClarity`,
  },
  {
    imageIndex: 11, // vargas-11
    text: `Built for big moments because she respects the grind of everyday training.

If you love the process, the prize will take care of itself. When you fall in love with the work, fatigue loses its sting.

Fall in love with the process of becoming great.

Order 'Finish Strong' today: lornettedaye.com/books

#LornetteDaye #LoveTheGrind #ProcessOriented #FinishStrong #SprintChampion`,
  },
  {
    imageIndex: 12, // vargas-12
    text: `Composure under pressure is a gift you give to everyone around you.

When the leader remains grounded, panic cannot take root in the team. Anchor yourself so your team can thrive.

Book Lornette Daye for your next executive retreat: lornettedaye.com/speaking

#LornetteDaye #ExecutivePresence #GroundedLeadership #ComposureInCrisis #Leadership`,
  },
  {
    imageIndex: 13, // vargas-13
    text: `The match turns when you decide to take full ownership of the moment.

No finger-pointing, no waiting for rescue. Step forward and claim the responsibility.

Ownership is the foundational pillar of leadership.

Learn more about Lornette's leadership pillars: lornettedaye.com/leadership

#LornetteDaye #ExtremeOwnership #StepForward #LeadershipPillars #Accountability`,
  },
  {
    imageIndex: 14, // vargas-14
    text: `Serve with clarity. Strike with power. Silence the critics.

Your results will always speak louder than someone else's commentary. Let your work do the talking.

Focus on your craft and let the scoreboard tell the story.

Visit lornettedaye.com for articles and resources.

#LornetteDaye #LetResultsSpeak #QuietWork #ScoreboardTruth #AthleteMindset`,
  },
  {
    imageIndex: 15, // vargas-15
    text: `Fire in your soul, ice in your decisions.

When you lead with strategic calm, you see solutions that emotional reactions blind others to.

Step back, breathe, and choose the highest-impact move.

Connect with Lornette Daye: lornettedaye.com

#LornetteDaye #StrategicCalm #HigherPerspective #DecisionMaking #ExecutiveLeadership`,
  },
  {
    imageIndex: 16, // vargas-16
    text: `Every point is an opportunity to reassert your commitment.

Never let temporary setbacks dictate your permanent trajectory. Realign, reload, and get back on the attack.

Your setback is just the setup for your comeback.

Read 'Surviving Life' by Lornette Daye: lornettedaye.com/books

#LornetteDaye #SetupForComeback #SurvivingLife #ResilienceCoach #KeepMovingForward`,
  },
  {
    imageIndex: 17, // vargas-17
    text: `Walk into every room knowing you carry decades of preparation and heart.

The stage doesn't create your greatness—it simply provides the canvas for your discipline to be witnessed.

Own your arena today.

Keynotes that inspire action: lornettedaye.com/speaking

#LornetteDaye #OwnYourCanvas #DecadesOfDiscipline #KeynoteSpeaker #InspirationalLeadership`,
  },
  {
    imageIndex: 18, // vargas-18
    text: `When fear whispers "step back", let your faith and preparation answer "step up".

There is no room for doubt when you are committed to the mission. Step up to your line with boldness.

Youth and athlete empowerment: lornettedaye.com/mentorship

#LornetteDaye #FaithOverFear #BoldLeadership #StepUp #EmpowermentMatters`,
  },
  {
    imageIndex: 19, // vargas-19
    text: `Every eye watching is a reminder that leadership is a sacred responsibility.

When people look to you for direction, give them clarity, empathy, and courage.

Lead with love, discipline, and purpose.

Explore Lornette Daye's mission: lornettedaye.com/about

#LornetteDaye #SacredResponsibility #LeadWithLove #PurposefulLeadership #CommunityChange`,
  },
  {
    imageIndex: 20, // vargas-20
    text: `Raising the level isn't a one-time event; it is a lifetime standard.

In 40+ years on track tracks, in locker rooms, boardrooms, and auditoriums, I have learned that the highest honor is knowing you left the standard higher than you found it.

How will you elevate the standard today?

Finish strong.

Explore speaking, coaching, and books at lornettedaye.com

#LornetteDaye #FinishStrong #RaiseTheStandard #LifetimeLegacy #HighPerformanceLeadership #MelissaVargas`,
  },
  {
    imageIndex: 1, // vargas-01
    text: `As we conclude this 3-week journey through power, pressure, and performance:

Remember that champion status isn't reserved for a chosen few—it belongs to anyone willing to embrace the discipline, withstand the pressure, and finish strong.

Thank you for running this race with me.

Book Lornette Daye for your next conference or keynote: lornettedaye.com/book

#LornetteDaye #FinishStrong #ClosingReflection #KeynoteSpeaker #ChampionshipMindset #MelissaVargas #Volleyball #LeadershipExcellence`,
  },
];

async function main() {
  console.log(`====================================================`);
  console.log(`Starting Buffer Scheduling for Lornette Daye Campaign`);
  console.log(`Total Posts: ${campaignPosts.length}`);
  console.log(`Schedule: 3 Posts/Day at 18:00, 19:00, 20:00 MDT (6pm, 7pm, 8pm)`);
  console.log(`Channel ID: ${CHANNEL_ID}`);
  console.log(`====================================================\n`);

  const results = [];
  const hours = [18, 19, 20]; // 6pm, 7pm, 8pm MDT

  for (let i = 0; i < campaignPosts.length; i++) {
    const post = campaignPosts[i];
    const dayOffset = Math.floor(i / 3);
    const hourSlot = hours[i % 3];
    const dueAt = getDueAt(dayOffset, hourSlot);

    const imgNum = String(post.imageIndex).padStart(2, '0');
    const imageUrl = `${BASE_IMAGE_URL}/vargas-${imgNum}.png`;

    const input = {
      channelId: CHANNEL_ID,
      text: post.text,
      mode: 'customScheduled',
      dueAt,
      schedulingType: 'automatic',
      needsApproval: false,
      saveToDraft: false,
      assets: [
        {
          image: {
            url: imageUrl,
          },
        },
      ],
    };

    console.log(`[${i + 1}/${campaignPosts.length}] Scheduling Post (Day ${dayOffset + 1}, ${hourSlot}:00 MDT / ${dueAt})...`);
    console.log(`   Image: vargas-${imgNum}.png`);
    console.log(`   Preview: "${post.text.split('\n')[0].substring(0, 60)}..."`);

    let retries = 3;
    let success = false;
    let postData = null;

    while (retries > 0 && !success) {
      try {
        const response = await fetch(BUFFER_API_URL, {
          method: 'POST',
          headers: {
            'Authorization': `Bearer ${BUFFER_ACCESS_TOKEN}`,
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            query: `
              mutation CreatePost($input: CreatePostInput!) {
                createPost(input: $input) {
                  __typename
                  ... on PostActionSuccess {
                    post {
                      id
                      text
                      status
                      shareMode
                      dueAt
                    }
                  }
                  ... on NotFoundError { message }
                  ... on UnauthorizedError { message }
                  ... on UnexpectedError { message }
                  ... on LimitReachedError { message }
                  ... on InvalidInputError { message }
                }
              }
            `,
            variables: { input },
          }),
        });

        const json = await response.json();
        if (json.data?.createPost?.post) {
          success = true;
          postData = json.data.createPost.post;
          console.log(`   ✅ Success! Buffer Post ID: ${postData.id} (Due: ${postData.dueAt})`);
          results.push({
            index: i + 1,
            day: dayOffset + 1,
            timeMDT: `${hourSlot}:00 MDT`,
            dueAt: postData.dueAt,
            postId: postData.id,
            image: `vargas-${imgNum}.png`,
            status: 'scheduled',
          });
        } else {
          console.error(`   ⚠️ Error response:`, JSON.stringify(json, null, 2));
          retries--;
          if (retries > 0) {
            console.log(`   Retrying in 2 seconds...`);
            await new Promise(r => setTimeout(r, 2000));
          }
        }
      } catch (err) {
        console.error(`   ⚠️ Network error:`, err.message);
        retries--;
        if (retries > 0) {
          console.log(`   Retrying in 2 seconds...`);
          await new Promise(r => setTimeout(r, 2000));
        }
      }
    }

    if (!success) {
      console.error(`   ❌ Failed to schedule post ${i + 1}`);
      results.push({
        index: i + 1,
        day: dayOffset + 1,
        timeMDT: `${hourSlot}:00 MDT`,
        dueAt,
        image: `vargas-${imgNum}.png`,
        status: 'failed',
      });
    }

    // Delay between calls to prevent rate limiting
    await new Promise(r => setTimeout(r, 400));
  }

  // Save report
  fs.writeFileSync('scripts/scheduled-campaign-report.json', JSON.stringify(results, null, 2));
  console.log(`\n🎉 Campaign scheduling complete! Report written to scripts/scheduled-campaign-report.json`);
}

main().catch(console.error);
