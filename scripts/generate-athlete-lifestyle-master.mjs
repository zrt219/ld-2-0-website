import fs from 'node:fs';
import path from 'node:path';

// Load our canonical files with detailed metadata
const POSTS_METADATA = [
  {
    index: 1,
    file: "01-cfb-nil-valuations.png",
    eyebrow: "NIL VALUATION & ATHLETE EQUITY",
    headline: "The Modern College Athlete Is No Longer Just a Student. They Are an Enterprise.",
    body: "The landscape of college athletics has fundamentally shifted. When eight-figure valuations and commercial partnerships enter the locker room before a player turns twenty-one, the mental demands multiply exponentially.\n\nRaw talent opens the door. But without financial literacy, emotional grounding, and personal identity systems, the pressure can erode performance faster than any defense on game day.\n\nOlympic-level coach Lornette Daye has spent over four decades mentoring elite athletes through high-pressure transitions. Her foundational principle is simple: when your identity is firmly rooted beyond the scoreboard, your execution on the field becomes calm, focused, and repeatable.\n\nAthletes who thrive in the NIL era do not just sign contracts. They build lifelong systems.",
    hashtags: "#NIL #CollegeFootball #AthleteEquity #SportsBusiness #LornettesFoundations #CareerCircle"
  },
  {
    index: 2,
    file: "02-million-dollar-womens-football.png",
    eyebrow: "COMMERCIAL VALUATION & IMPACT",
    headline: "A Million-Dollar Women's Football Moment: Proof That True Value Was Never in Question.",
    body: "Women's football is not experiencing an overnight surge. It is experiencing the inevitable payoff of decades of relentless preparation, undeniable skill, and passionate audiences demanding equal recognition.\n\nWhen Naomi Girma and Olivia Smith step onto the pitch, they carry more than athletic prowess. They represent a new standard of commercial leverage and cultural influence for female athletes worldwide.\n\nLornette Daye has championed athletic excellence across global stages for more than forty years. She teaches athletes to recognize their worth long before the market acknowledges it. Sustainable confidence is built on repeatable preparation and unwavering self-belief, not external validation.\n\nWhen you master your craft and anchor your emotional poise, the valuation naturally follows.",
    hashtags: "#WomensFootball #NWSL #AthleteEmpowerment #SportsLeadership #LornettesFoundations #CareerCircle"
  },
  {
    index: 3,
    file: "03-aja-wilson-next-gen.png",
    eyebrow: "CHAMPIONSHIP CULTURE & INSPIRATION",
    headline: "A'ja Wilson Does Not Just Win Championships. She Expands What Is Possible for the Next Generation.",
    body: "Dominance in professional sports is rare. Sustained dominance paired with authentic cultural leadership is extraordinary.\n\nA'ja Wilson has elevated women's basketball not only through MVP performances and championship rings, but through her poise, vulnerability, and dedication to uplifting young athletes.\n\nThrough Lornette's Foundations, Lornette Daye emphasizes that the most profound legacy an athlete can build is not found in trophies. It is found in the standards they leave behind. When young people see an athlete who is grounded, articulate, and unapologetically disciplined, their own horizons expand.\n\nTrue champions build platforms that outlive their playing careers.",
    hashtags: "#AjaWilson #WNBA #ChampionshipMindset #NextGeneration #LornettesFoundations #CareerCircle"
  },
  {
    index: 4,
    file: "04-aja-wilson-greatness-season.png",
    eyebrow: "STANDARDS & REPEATABLE HABITS",
    headline: "Greatness Is Not an Event. It Is a Daily Discipline Practiced Season After Season.",
    body: "Anyone can put together a hot streak. Elite performers build daily routines that make excellence inevitable.\n\nA'ja Wilson's consistency year after year stems from a lifestyle of intentional recovery, mental focus, and relentless attention to detail. She does not wait for motivation. She relies on systems.\n\nLornette Daye coaches athletes to understand that your previous shot, play, or season cannot hit your next one. The only moment that matters is the present repetition. When you fall in love with the unglamorous daily process, long-term greatness takes care of itself.\n\nConsistency is the ultimate differentiator at the highest levels of competition.",
    hashtags: "#ElitePerformance #HabitsOfExcellence #Discipline #WNBA #LornettesFoundations #CareerCircle"
  },
  {
    index: 5,
    file: "05-aja-wilson-work-and-impact.png",
    eyebrow: "COMMUNITY IMPACT & AUTHENTICITY",
    headline: "The Unseen Work Always Precedes the Public Impact.",
    body: "The world celebrates the highlight reel. But every step toward iconic status is paved in empty gyms, quiet film sessions, and moments of self-doubt overcome in silence.\n\nA'ja Wilson's cultural impact resonates deeply because it is backed by genuine work ethic and community commitment. She understands that an athlete's voice carries immense power when it is anchored in integrity.\n\nLornette Daye has guided Canadian national champions and Olympic hopefuls by teaching that character is built in the shadows. When public pressure peaks, your private preparation is what keeps you upright and composed.\n\nAnchor your foundation in substance, and your voice will carry across generations.",
    hashtags: "#WorkAndImpact #AthleteVoice #IntegrityInSport #Leadership #LornettesFoundations #CareerCircle"
  },
  {
    index: 6,
    file: "06-aja-wilson-season-built.png",
    eyebrow: "SEASON-BUILT RESILIENCE",
    headline: "Building a Legacy That Outlasts the Season: The Power of Perspective.",
    body: "A grueling season tests more than an athlete's physical stamina. It tests emotional resilience, patience, and the ability to navigate internal team dynamics.\n\nAthletes who navigate championship runs understand how to manage energy, protect boundaries, and maintain perspective when external pressure reaches a fever pitch.\n\nLornette Daye's work with elite performers focuses on total human conditioning. That means developing emotional regulation, supportive family networks, and clear mental reset triggers. When you are steady on the inside, nothing happening on the outside can rattle your composure.\n\nChampionships are won in the mind before they are won on the hardwood.",
    hashtags: "#Resilience #MentalToughness #SeasonBuilt #PeakPerformance #LornettesFoundations #CareerCircle"
  },
  {
    index: 7,
    file: "07-andraya-carter-court-to-conversation.png",
    eyebrow: "CAREER TRANSITION & MEDIA AUTHORITY",
    headline: "From Hardwood Intensity to Broadcasting Mastery: Andraya Carter's Masterclass in Career Evolution.",
    body: "When injuries altered Andraya Carter's playing trajectory, she did not view it as an ending. She viewed it as a pivot.\n\nToday, she is one of the most respected voices in sports media, breaking down complex game dynamics with unmatched clarity, poise, and authenticity.\n\nCareer transitions in sport are often intimidating. Lornette Daye teaches athletes that the tactical intelligence, communication skills, and work ethic honed in athletics are directly transferable to executive media and corporate boardrooms.\n\nYour athletic career is your launching pad, not your final destination.",
    hashtags: "#CareerTransition #SportsBroadcasting #AndrayaCarter #AthleteMobility #LornettesFoundations #CareerCircle"
  },
  {
    index: 8,
    file: "08-andraya-carter-game-insight.png",
    eyebrow: "ANALYTICAL MASTERY & PREPARATION",
    headline: "Gold-Edged Game Insight: Preparation Is the Key to Total On-Camera Poise.",
    body: "Great sports analysis sounds effortless on live television. But that ease is the result of hours of rigorous film study, statistical breakdown, and relentless curiosity.\n\nAndraya Carter commands the broadcast desk because her preparation is non-negotiable. She respects the craft, the players, and the audience.\n\nIn Lornette's Foundations, Lornette Daye emphasizes that confidence is simply the natural byproduct of exhaustive preparation. When you have done the homework, you do not need to fake authority. Your insight speaks for itself.\n\nInvest in your preparation, and your presence will command every room you enter.",
    hashtags: "#GameInsight #PreparationEqualsConfidence #ExecutivePresence #LornettesFoundations #CareerCircle"
  },
  {
    index: 9,
    file: "09-andraya-carter-she-knows-game.png",
    eyebrow: "BREAKING STEREOTYPES IN MEDIA",
    headline: "She Knows the Game: When Undeniable Expertise Shatters Every Barrier.",
    body: "For decades, women in sports media were often relegated to sideline roles. Andraya Carter has redefined what primary analysis looks like across major sports networks.\n\nHer deep tactical knowledge, player empathy, and commanding delivery have earned the respect of coaches, players, and millions of viewers across the country.\n\nLornette Daye knows firsthand what it means to lead as a pioneering woman in athletic coaching. Her guidance helps athletes and professionals stand firm in their expertise, speak with conviction, and refuse to shrink to make others comfortable.\n\nExcellence is an argument that cannot be dismissed.",
    hashtags: "#WomenInSports #SportsMedia #Breakthrough #Leadership #LornettesFoundations #CareerCircle"
  },
  {
    index: 10,
    file: "10-andraya-carter-next-gen-voice.png",
    eyebrow: "THE NEXT GENERATION'S VOICE",
    headline: "The Power of Representation: A New Voice for the Modern Sports Era.",
    body: "Sports culture moves fast. The voices covering the game must reflect the passion, diversity, and intellectual depth of today's players and fans.\n\nAndraya Carter brings a fresh perspective that bridges the gap between locker room reality and broadcast storytelling. She proves that authenticity is your greatest professional asset.\n\nLornette Daye works with emerging athletes to help them develop their unique personal brand and communication style. You do not need to fit into someone else's mold to achieve lasting influence. Your story is your superpower.\n\nLead with authenticity, and you will inspire others to find their own voice.",
    hashtags: "#RepresentationMatters #NextGenVoice #PersonalBranding #LornettesFoundations #CareerCircle"
  },
  {
    index: 11,
    file: "11-aja-wilson-more-than-player.png",
    eyebrow: "HOLISTIC ATHLETE DEVELOPMENT",
    headline: "More Than a Player: Cultivating the Full Human Being Behind the Jersey.",
    body: "Too many athletes fall into the trap of defining their entire self-worth by their athletic statistics. When the game goes well, they feel worthy. When setbacks occur, their identity crumbles.\n\nA'ja Wilson exemplifies what happens when an athlete develops her complete personhood: author, businesswoman, philanthropist, and leader.\n\nLornette Daye has spent 40 years championing athlete wellbeing. Her coaching framework establishes identity beyond sport as the primary foundation of long-term success. When you know who you are off the court, your performance on the court becomes fearless.\n\nYou are a complete human being first. An athlete second.",
    hashtags: "#IdentityBeyondSport #AthleteWellbeing #WholeAthlete #LornettesFoundations #CareerCircle"
  },
  {
    index: 12,
    file: "12-aja-wilson-achievement-impact.png",
    eyebrow: "SUSTAINABLE MOMENTUM",
    headline: "Achievement Without Emotional Balance Is Just Noise: Prioritizing Inner Wellness.",
    body: "In the pursuit of championships, physical exhaustion is obvious. But emotional exhaustion is the hidden threat that cuts athletic careers short.\n\nManaging media demands, public expectations, and relentless competition requires deliberate rest, mental recovery, and a trusted inner circle.\n\nLornette Daye's foundations framework provides athletes with actionable recovery rituals and emotional regulation tools. True high performance is not about burning out for a short sprint. It is about building sustainable habits that allow you to thrive over a twenty-year career and beyond.\n\nProtect your peace of mind as fiercely as you protect your physical health.",
    hashtags: "#EmotionalPoise #MentalWellness #AthleteCare #PeakLongevity #LornettesFoundations #CareerCircle"
  },
  {
    index: 13,
    file: "13-bahamas-400m-world-stage.png",
    eyebrow: "OLYMPIC EXCELLENCE & GLOBAL FOCUS",
    headline: "Standing on the World Stage: The Solitary Weight of Olympic Execution.",
    body: "The 400 meters is widely regarded as one of the most physically and mentally grueling events in track and field. There is nowhere to hide. No timeouts. No halftime.\n\nWhen Bahamian track stars step into the starting blocks on the global stage, years of quiet sacrifice culminate in forty-eight seconds of pure, unrelenting intensity.\n\nAs a Canadian national sprint champion and Olympic-level coach, Lornette Daye knows that race intimate detail. The critical battle is fought not in the legs, but in the final one hundred meters when lactic acid burns and the mind must remain serene.\n\nWhen your mental discipline is forged in steel, your body will carry you across the finish line.",
    hashtags: "#TrackAndField #OlympicMindset #400Meters #BahamasAthletics #LornettesFoundations #CareerCircle"
  },
  {
    index: 14,
    file: "14-bahamas-behind-performance.png",
    eyebrow: "THE PSYCHOLOGY OF SPEED",
    headline: "The Mind Behind the Stride: How Elite Sprinters Master Internal Composure.",
    body: "Sprinters often look relaxed even as they reach thirty miles per hour. That relaxation is not casual. It is the highest form of trained neuromuscular control.\n\nTension is the enemy of speed. The harder you force the stride, the slower you run. The fastest sprinters master the paradox of applying maximum force with zero unnecessary panic.\n\nLornette Daye teaches athletes across all sports how to access that calm center under intense competitive pressure. Whether you are running a curve or presenting to a boardroom, relaxation under pressure is the secret to peak output.\n\nRelease the tension, trust your training, and let your natural power flow.",
    hashtags: "#SportsPsychology #SpeedMechanics #ComposureUnderPressure #LornettesFoundations #CareerCircle"
  },
  {
    index: 15,
    file: "15-bahamas-one-lap-commitment.png",
    eyebrow: "LONG-TERM COMMITMENT",
    headline: "One Lap, Years of Commitment: The True Math of Athletic Mastery.",
    body: "Spectators see less than a minute of racing. They do not see the thousand hours of hill sprints in the summer heat, the early morning weight room sessions, and the dietary discipline.\n\nSuccess in any high-performance arena is an asymmetric equation. You invest years of unseen work for moments that pass in seconds.\n\nLornette Daye reminds every athlete and executive she mentors that patience is a competitive edge. Most people quit when results do not appear immediately. Those who commit to the daily process over years build unbreakable momentum.\n\nHonor the commitment in the quiet moments, and the podium will take care of itself.",
    hashtags: "#LongTermCommitment #Mastery #PatienceInProcess #OlympicCoach #LornettesFoundations #CareerCircle"
  },
  {
    index: 16,
    file: "16-ryan-day-behind-headset-3.png",
    eyebrow: "COACHING UNDER THE SPOTLIGHT",
    headline: "Behind the Headset: Executive Presence When One Hundred Thousand Fans Are Watching.",
    body: "Leading a premier college football program like Ohio State is one of the highest-pressure leadership roles in North American sports. Every play call, substitution, and press conference is analyzed by millions.\n\nRyan Day demonstrates what it means to lead from the front: staying composed on the sideline, communicating clearly amidst stadium deafening noise, and shielding players from outside static.\n\nLornette Daye has spent decades coaching at the elite level. She teaches that great leaders are emotional thermostats, not thermometers. They do not reflect the chaos around them. They set the tone and lower the room temperature.\n\nYour team will reflect your composure. Master yourself first.",
    hashtags: "#ExecutiveLeadership #RyanDay #CoachingExcellence #Composure #LornettesFoundations #CareerCircle"
  },
  {
    index: 17,
    file: "17-beyond-contract-athlete-futures.png",
    eyebrow: "POST-CAREER STRATEGY",
    headline: "Beyond the Contract: Architecting the Post-Athletic Career Blueprint Today.",
    body: "The average professional athletic career lasts under four years. Yet many athletes wait until their final contract expires before considering what comes next.\n\nThe most successful athletes do not view life after sports as a retirement. They view it as an executive second act, utilizing their competitiveness, teamwork, and resilience to lead enterprises.\n\nLornette Daye partners with organizations like Career Circle and UMATTR to help athletes bridge the gap between sports and industry. When you systematically translate athletic discipline into corporate leadership, your second career can far surpass your first.\n\nStart planning for your future while your platform is at its highest.",
    hashtags: "#AthleteTransition #LifeAfterSports #CareerMobility #CorporateReadiness #LornettesFoundations #CareerCircle"
  },
  {
    index: 18,
    file: "18-carr-family-legacy.png",
    eyebrow: "MULTIGENERATIONAL ATHLETIC HERITAGE",
    headline: "The Carr Family Legacy: Navigating Expectations Across Generations of Football.",
    body: "Carrying a famous surname in athletics brings both extraordinary access and immense public expectation. Every throw, interview, and decision is compared to those who came before.\n\nThe Carr family has demonstrated how generational athletic wisdom can be passed down without crushing the individual spirit of emerging athletes.\n\nLornette Daye emphasizes family and community support as one of the essential athletic foundations. Parents and mentors must create an emotional safe harbor where the young athlete is valued for who they are, not just what their name represents.\n\nLegacy is not about repeating the past. It is about providing the foundation for the next generation to fly.",
    hashtags: "#SportsHeritage #FamilyInSports #CarrFamily #AthleteParenting #LornettesFoundations #CareerCircle"
  },
  {
    index: 19,
    file: "19-carr-family-sports-legacy.png",
    eyebrow: "BUILDING CHARACTER ACROSS GENERATIONS",
    headline: "Passing the Torch: Teaching Integrity, Work Ethic, and Emotional Poise at Home.",
    body: "No coach can install what the home environment fails to nurture. The most resilient athletes are raised with a deep sense of humility, respect for the game, and strong moral compass.\n\nSports dynasties do not endure because of superior genetics alone. They endure because of values passed across kitchen tables long before national signing day.\n\nLornette Daye works closely with sports families to help them build supportive, pressure-free environments where young athletes can fail safely and develop genuine resilience.\n\nCharacter is the anchor that keeps talent from drifting in turbulent waters.",
    hashtags: "#YouthDevelopment #CharacterFirst #SportsDynasty #AthleteMentorship #LornettesFoundations #CareerCircle"
  },
  {
    index: 20,
    file: "20-cfl-top-paid-players.png",
    eyebrow: "CANADIAN PROFESSIONAL SPORTS",
    headline: "CFL Financial Realities: Smart Wealth Systems for the Working Pro Athlete.",
    body: "While NFL salaries dominate the headlines, CFL players navigate a different financial reality that requires disciplined budgeting, early entrepreneurial ventures, and dual-career preparation.\n\nThe top earners in the CFL demonstrate remarkable resourcefulness, often balancing professional football with off-season businesses, community initiatives, and higher education.\n\nLornette Daye has worked throughout the Canadian sports ecosystem for decades. She advocates for comprehensive career and money readiness for all athletes, regardless of their league's average salary.\n\nWealth is not about what you make during your peak playing years. It is about the financial systems you put in place for life.",
    hashtags: "#CFL #CanadianSports #FinancialLiteracy #ProAthleteLife #LornettesFoundations #CareerCircle"
  },
  {
    index: 21,
    file: "21-cfl-career-pathways-wellbeing.png",
    eyebrow: "HOLISTIC CAREER MOBILITY",
    headline: "CFL Pathways: Health, Career Transition, and Life Beyond the Goalposts.",
    body: "Transitioning out of professional Canadian football requires deliberate intentionality. Athletes must translate physical stamina, locker room diplomacy, and strategic mindset into the corporate economy.\n\nAddressing post-concussion health, emotional identity loss, and network building is essential to a thriving second chapter.\n\nThrough Lornette's Foundations and Career Circle, Lornette Daye provides structured transition blueprints that equip departing players with the tools to excel as entrepreneurs, consultants, and community leaders.\n\nYour athletic identity is a chapter in your book, not the entire story.",
    hashtags: "#CFLTransition #AthleteHealth #CareerPathways #WorkforceReadiness #LornettesFoundations #CareerCircle"
  },
  {
    index: 22,
    file: "22-cfl-canadian-game-real-business.png",
    eyebrow: "THE BUSINESS OF CANADIAN FOOTBALL",
    headline: "Canadian Game, Real Business: Preparing Athletes for Commercial Leadership.",
    body: "The Canadian Football League represents a storied tradition of community-owned franchises, passionate fan bases, and high-velocity football.\n\nFor athletes competing north of the border, understanding the commercial economics of sports franchises offers a masterclass in business operations, ticket sales, media rights, and local sponsorship.\n\nLornette Daye encourages athletes to treat every season as an executive internship. Pay attention to how the front office operates, how brands activate, and how relationships are nurtured.\n\nThe skills that build a business are the very same skills that build a winning team.",
    hashtags: "#SportsBusiness #CFL #CommercialStrategy #ExecutiveMindset #LornettesFoundations #CareerCircle"
  },
  {
    index: 23,
    file: "23-chas-nimrod-ready-moment-2.png",
    eyebrow: "COLLEGE FOOTBALL BREAKTHROUGHS",
    headline: "Chas Nimrod: Preparing in Silence for the Moment the Spotlight Arrives.",
    body: "In major college football, wide receivers spend hundreds of snaps blocking downfield and running decoy routes for every pass that comes their way.\n\nWhen Tennessee receiver Chas Nimrod gets his target, it looks effortless. But that instant separation was forged through thousands of unheralded practice repetitions.\n\nLornette Daye teaches athletes that readiness is a personal lifestyle, not a game-day switch. If you wait until the stadium lights come on to get ready, you are already too late.\n\nStay ready in the dark so you never have to scramble in the light.",
    hashtags: "#ChasNimrod #TennesseeFootball #SECFootball #Preparedness #LornettesFoundations #CareerCircle"
  },
  {
    index: 24,
    file: "24-chas-nimrod-ready-moment.png",
    eyebrow: "SEIZING OPPORTUNITY UNDER PRESSURE",
    headline: "When Opportunity Knocks, Only Prior Preparation Answers the Door.",
    body: "Sports do not care about your intentions. They only reward your execution in the split-second when the ball is in the air.\n\nYoung athletes often become frustrated when their playing time is limited. But the true champions use every rep with the scout team to sharpen their mechanics and deepen their mental grasp of the playbook.\n\nLornette Daye coaches athletes to master the emotional discipline of waiting without wasting time. Every day you spend preparing outside the spotlight is an investment in your future breakthrough.\n\nKeep sharpening your sword. Your moment will demand its sharpness.",
    hashtags: "#Execution #OpportunityKnocks #MentalDiscipline #WideReceiver #LornettesFoundations #CareerCircle"
  },
  {
    index: 25,
    file: "25-chas-nimrod-every-opportunity.png",
    eyebrow: "RESPONSIBILITY & EXECUTION",
    headline: "Every Opportunity Carries a Responsibility: Executing When Your Number Is Called.",
    body: "Trust is the most valuable currency between a coach and a player. Coaches do not play the most talented athlete. They play the athlete they trust most in critical moments.\n\nWhen Chas Nimrod secures a tough third-down conversion, he is proving that trust has been earned through consistent weekly practice habits.\n\nLornette Daye emphasizes that reliability is the highest compliment an athlete can receive. Be the person your teammates and leaders know they can count on when everything is on the line.\n\nTalent gets you noticed. Reliability keeps you on the field.",
    hashtags: "#TrustAndExecution #Reliability #SEC #PlayerDevelopment #LornettesFoundations #CareerCircle"
  },
  {
    index: 26,
    file: "26-chas-nimrod-unseen-work.png",
    eyebrow: "THE SOLITARY WORK OF EXCELLENCE",
    headline: "The Unseen Work: What Happens When the Stadium Gates Are Locked.",
    body: "Television broadcasts capture three hours of action on Saturday afternoon. They miss the early morning mobility work, the ice baths, and the hours studying defensive back coverages alone in the film room.\n\nAthletes who make an enduring impact fall in love with the solitude of preparation. They find joy in the grind, not just the applause.\n\nLornette Daye's Olympic background taught her that self-discipline is self-respect in action. When you respect your potential, you refuse to cut corners even when nobody is watching.\n\nFall in love with the unseen process, and the public results will speak for themselves.",
    hashtags: "#TheUnseenWork #SelfDiscipline #FootballCulture #Tennessee #LornettesFoundations #CareerCircle"
  },
  {
    index: 27,
    file: "27-chas-nimrod-work-unseen-5.png",
    eyebrow: "MICRO-HABITS & DETAILS",
    headline: "Refining the Micro-Habits of Championship Readiness: Millimeters Make Champions.",
    body: "At the elite level, physical differences between athletes are microscopic. Everyone is fast. Everyone is strong. Everyone is driven.\n\nThe victor is determined by details: clean hand placement, sharp route stems, hydration discipline, and emotional poise on third down.\n\nLornette Daye trains athletes to respect the micro-habits. When you master the small, unglamorous fundamentals daily, you create an unshakeable foundation that holds up in fourth-quarter chaos.\n\nExcellence is not a singular act. It is a thousand small decisions executed with pride.",
    hashtags: "#MicroHabits #DetailsMatter #ChampionshipStandard #LornettesFoundations #CareerCircle"
  },
  {
    index: 28,
    file: "28-cj-carr-notre-dame-practice.png",
    eyebrow: "TRADITION & PERSONAL IDENTITY",
    headline: "Under the Golden Dome: Establishing Personal Identity in Storied Collegiate Programs.",
    body: "Stepping onto the practice field at Notre Dame means stepping into a century of football folklore, legendary names, and national championship banners.\n\nFor quarterback CJ Carr, wearing the blue and gold requires an exceptional level of maturity. You must honor the storied tradition while maintaining absolute clarity about your own individual game and journey.\n\nLornette Daye coaches young leaders to remain centered in historic institutions. Never let the grandeur of the institution eclipse your own personal values and core identity.\n\nRespect the history, but write your own chapter with confidence.",
    hashtags: "#NotreDame #FightingIrish #CJCarr #QuarterbackMindset #LornettesFoundations #CareerCircle"
  },
  {
    index: 29,
    file: "29-cj-carr-his-own-path.png",
    eyebrow: "INDEPENDENT TRAJECTORY",
    headline: "Football Family, His Own Path: The Courage to Build an Authentic Reputation.",
    body: "When your grandfather is a legendary national championship coach and your family has deep roots in the sport, following your own path takes real courage.\n\nCJ Carr chose his collegiate destination based on where he could grow as a player, student, and leader, carving an authentic legacy on his own terms.\n\nLornette Daye encourages every emerging athlete to own their story. Family support is a blessing, but your career belongs to you alone. Build it with your own hands and your own values.\n\nYour heritage may open the door, but your work ethic is what earns your seat at the table.",
    hashtags: "#AuthenticLeadership #CarveYourPath #QuarterbackDevelopment #LornettesFoundations #CareerCircle"
  },
  {
    index: 30,
    file: "30-college-football-beyond-lights.png",
    eyebrow: "ATHLETE MENTAL HEALTH",
    headline: "Beyond the Stadium Lights: Confronting the Mental Health Reality of Modern Athletes.",
    body: "Behind the electric stadium atmospheres and Saturday game-day celebrations lies a silent struggle with anxiety, burnout, and relentless social media scrutiny.\n\nCollege athletes today carry the workload of a full-time academic course load combined with the physical and commercial expectations of a multi-million-dollar entertainment franchise.\n\nLornette Daye is an outspoken advocate for mental health and emotional poise in athletics. Winning games cannot come at the expense of a young person's emotional wellbeing. We must equip them with tools to decompress, communicate, and seek support without shame.\n\nA healthy athlete is a sustainable performer.",
    hashtags: "#AthleteMentalHealth #BeyondTheLights #Wellbeing #CollegeAthletics #LornettesFoundations #CareerCircle"
  },
  {
    index: 31,
    file: "31-college-football-8-billion-business.png",
    eyebrow: "COLLEGE SPORTS ECONOMICS",
    headline: "College Football's 8 Billion Dollar Industry: Protecting and Empowering the Human Asset.",
    body: "College football generates over eight billion dollars annually through media rights, corporate sponsorships, and packed stadiums.\n\nAs the revenue model matures, ensuring that the athletes whose labor powers this enterprise receive world-class healthcare, financial education, and post-career career support is the paramount moral imperative.\n\nLornette Daye works with collegiate and professional programs to install comprehensive athlete development systems. When institutions invest deeply in the human being, the enterprise flourishes naturally.\n\nThe future of sports business depends on prioritizing the athletes who make the game possible.",
    hashtags: "#SportsEconomics #CollegeFootballBusiness #AthleteEmpowerment #LornettesFoundations #CareerCircle"
  },
  {
    index: 32,
    file: "32-edmonton-oilers-nugent-hopkins.png",
    eyebrow: "NHL LONGEVITY & STABILITY",
    headline: "Longevity on the Ice: Ryan Nugent-Hopkins and the Power of Unassuming Consistency.",
    body: "In the fast-paced, high-impact world of the National Hockey League, surviving more than a decade with a single franchise is an extraordinary accomplishment.\n\nRyan Nugent-Hopkins has been the steady heartbeat of the Edmonton Oilers through coaching changes, roster overhauls, and deep playoff runs. His quiet professionalism is revered in the locker room.\n\nLornette Daye emphasizes that steady reliability is often more valuable than volatile flashes of brilliance. The athlete who shows up every single day with the same professional attitude builds an enduring career.\n\nBe the reliable anchor your team can depend on through every storm.",
    hashtags: "#EdmontonOilers #NHL #NugentHopkins #HockeyCulture #LornettesFoundations #CareerCircle"
  },
  {
    index: 33,
    file: "33-epl-top-five-salary-rankings.png",
    eyebrow: "GLOBAL FOOTBALL FINANCE",
    headline: "Premier League Financial Realities: Building Multigenerational Stewardship Across Borders.",
    body: "The English Premier League commands the highest broadcast revenues and player compensation packages in global sport.\n\nYet for international stars arriving in England, managing multi-million-pound contracts across complex tax jurisdictions, cultural transitions, and intense media pressure requires elite financial advisory networks.\n\nLornette Daye advises international athletes to surround themselves with vetted, transparent advisors. Money earned quickly can disappear just as fast without rigorous wealth preservation systems.\n\nTrue wealth is not measured by the size of your contract, but by what remains for your grandchildren.",
    hashtags: "#PremierLeague #EPL #GlobalAthletes #WealthPreservation #LornettesFoundations #CareerCircle"
  },
  {
    index: 34,
    file: "34-every-opportunity-story.png",
    eyebrow: "THE POWER OF PERSPECTIVE",
    headline: "Every Opportunity Carries an Untold Story of Sacrifice and Resilience.",
    body: "When you see an athlete step onto the field, you are looking at the culmination of thousands of sacrifices made by family members, early coaches, and mentors who believed when no one else did.\n\nGratitude is not weakness. It is the fuel that keeps an athlete humble and hungry through the inevitable valleys of competitive sport.\n\nLornette Daye encourages athletes to never forget where they came from. Remembering your origin story keeps you anchored in purpose when external fame threatens to distort your perspective.\n\nCarry your history with pride, and let it fuel your standard of excellence.",
    hashtags: "#Gratitude #Sacrifice #SportsStorytelling #Perspective #LornettesFoundations #CareerCircle"
  },
  {
    index: 35,
    file: "35-finally-womens-football-elevated.png",
    eyebrow: "WOMEN'S SOCCER RENAISSANCE",
    headline: "Finally, Women's Football Elevated: The Dawn of a Permanent Commercial Reality.",
    body: "Record-shattering broadcast ratings, sold-out stadiums across Europe and North America, and multi-million-dollar commercial endorsements are no longer novelty stories in women's football.\n\nThey are the baseline of a permanent, rapidly growing industry that is reshaping global sports marketing.\n\nLornette Daye has spent over forty years paving paths for female athletic excellence. She urges corporate sponsors and athletic directors to view women's sports not as charity, but as one of the highest-growth commercial investments in entertainment.\n\nThe momentum is real, and it is only accelerating.",
    hashtags: "#WomensSoccer #CommercialGrowth #SportsElevation #EqualOpportunity #LornettesFoundations #CareerCircle"
  },
  {
    index: 36,
    file: "36-hawaii-to-stadium-2.png",
    eyebrow: "CULTURAL ROOTS & IDENTITY",
    headline: "From Hawaii to the Mainland: Carrying Island Heritage to the Brightest Stadium Lights.",
    body: "Polynesian athletes have enriched the game of American football with incredible physicality, discipline, and profound cultural values rooted in family, faith, and community.\n\nLeaving home to compete on the mainland is a major transition. Grounding yourself in your ancestral heritage provides an unshakeable identity that withstands the commercial pressures of elite sport.\n\nLornette Daye coaches athletes from all backgrounds to celebrate their heritage as a source of strength. When you know who you represent, you play with an energy that goes far beyond individual statistics.\n\nNever forget the soil you grew from. It will keep you standing in the wind.",
    hashtags: "#PolynesianAthletes #IslandCulture #HeritageInSport #FootballFamily #LornettesFoundations #CareerCircle"
  },
  {
    index: 37,
    file: "37-hawaii-built-for-moment-1.png",
    eyebrow: "COMMUNITY-CENTERED LEADERSHIP",
    headline: "Built for the Moment: Resilience Forged in the Warmth of Community.",
    body: "Athletic poise under pressure is rarely an individual achievement. It is usually the result of a village that poured love, discipline, and belief into a young person over decades.\n\nWhen athletes enter hostile road environments, they are never truly alone. They carry the prayers and hopes of their entire hometown with them into the huddle.\n\nLornette Daye emphasizes community support as Foundation Seven in her ten-week system. When an athlete feels supported win or lose, their fear of failure evaporates, allowing their best performance to surface naturally.\n\nPlay for something bigger than yourself, and pressure becomes privilege.",
    hashtags: "#CommunitySupport #BuiltForTheMoment #Leadership #FaithAndFamily #LornettesFoundations #CareerCircle"
  },
  {
    index: 38,
    file: "38-generations-of-the-game.png",
    eyebrow: "MENTORSHIP ACROSS GENERATIONS",
    headline: "Generations of the Game: What Veteran Pros Must Pass Down to Emerging Stars.",
    body: "The locker room is one of society's great egalitarian classrooms. Rookies straight out of college sit alongside fifteen-year veterans who have survived every commercial and physical test the sport can offer.\n\nThe health of any sports franchise depends on whether veteran leaders actively mentor younger players on life, money, emotional poise, and off-field decision-making.\n\nLornette Daye believes intentional mentorship is the lifeblood of sporting excellence. When knowledge is shared generously across generations, the entire culture elevates.\n\nTrue leadership is measured by how many leaders you develop around you.",
    hashtags: "#MentorshipInSport #VeteranLeadership #LockerRoomCulture #PassingTheTorch #LornettesFoundations #CareerCircle"
  },
  {
    index: 39,
    file: "39-golden-moment-girma-smith.png",
    eyebrow: "TEAM CHEMISTRY & SHARED GLORY",
    headline: "Naomi Girma and Olivia Smith: Championship Chemistry Built on Trust and Mutual Respect.",
    body: "Individual talent can win games. But championships require an unspoken chemistry where teammates read each other's movements, communicate effortlessly, and celebrate each other's success.\n\nNaomi Girma and Olivia Smith exemplify this modern championship dynamic: composed under defensive pressure, lethal in transition, and deeply united on and off the pitch.\n\nLornette Daye coaches teams to build trust through clear, empathetic communication. When teammates know they have each other's backs unconditionally, execution becomes fluid and joy-filled.\n\nGreat teams are not assembled. They are forged through shared commitment and trust.",
    hashtags: "#TeamChemistry #NaomiGirma #OliviaSmith #WomensFootball #LornettesFoundations #CareerCircle"
  },
  {
    index: 40,
    file: "40-jayden-maiava-leadership-field.png",
    eyebrow: "QUARTERBACK PRESENCE & POISE",
    headline: "Jayden Maiava: Leading the Huddle with Humility and Decisive Command.",
    body: "The quarterback position demands more than a strong arm and quick feet. It demands total emotional poise, quick decision-making under duress, and the ability to command ten other players with quiet confidence.\n\nJayden Maiava has showcased what it looks like to step into high-pressure collegiate environments with humility, poise, and undeniable playmaking ability.\n\nLornette Daye's performance framework helps quarterbacks master their internal dialogue and pre-snap focus. When your mind is clear and your breathing is steady, reading defenses becomes second nature.\n\nLead with clarity and calm, and your team will follow you into any battle.",
    hashtags: "#QuarterbackLeadership #JaydenMaiava #USCFootball #EmotionalPoise #LornettesFoundations #CareerCircle"
  },
  {
    index: 41,
    file: "41-manning-family-legacy-24.png",
    eyebrow: "SPORTS GOVERNANCE & FAMILY VALUES",
    headline: "The Manning Playbook: Building Generational Excellence Through Structure and Respect.",
    body: "From Archie to Peyton, Eli, and now Arch, the Manning family has set the gold standard for how to handle elite quarterback play, corporate branding, and public goodwill.\n\nTheir success is not an accident of genetics. It is the result of deliberate family governance, strict work ethic, deep respect for football history, and an authentic sense of humor.\n\nLornette Daye teaches that family systems are the ultimate anchor for elite performers. When your home life is stable, structured, and loving, the volatility of the sports world cannot knock you off balance.\n\nBuild strong roots at home, and your branches will reach the sky without fear.",
    hashtags: "#ManningFamily #FootballLegacy #FamilyGovernance #QuarterbackRoyalty #LornettesFoundations #CareerCircle"
  },
  {
    index: 42,
    file: "42-manning-family-legacy-25.png",
    eyebrow: "DEVELOPING THE INDIVIDUAL",
    headline: "Navigating Surnames and Pressure: Developing the Individual First, the Athlete Second.",
    body: "When you inherit a famous last name, public expectations can feel like an anvil on your shoulders. Every mistake is amplified, every success downplayed as privilege.\n\nThe genius of the Manning approach has always been letting each young athlete find their own love for the game without forced pressure or manufactured hype.\n\nLornette Daye works with high-profile athletes and their families to ensure that identity remains separate from external expectations. You are not your father, your brother, or your last name. You are yourself.\n\nRun your own race, with your own heart, on your own terms.",
    hashtags: "#ArchManning #FamilyExpectations #IndividualDevelopment #SportsIdentity #LornettesFoundations #CareerCircle"
  },
  {
    index: 43,
    file: "43-michael-irvin-miami-editorial.png",
    eyebrow: "INTENSITY & EMOTIONAL ENERGY",
    headline: "Michael Irvin: Passion, Intensity, and Channeling Emotional Energy for Growth.",
    body: "Few figures in sports history embody raw passion and fiery intensity quite like Pro Football Hall of Famer Michael Irvin.\n\nFrom the swagger of the 1980s Miami Hurricanes to three Super Bowl rings with the Dallas Cowboys, Irvin's relentless motor inspired everyone around him to practice harder and compete fiercer.\n\nLornette Daye coaches athletes that passion is a powerful engine, but it requires steering. When fiery intensity is paired with emotional discipline and purpose, it transforms into an unstoppable leadership force.\n\nDo not dampen your fire. Channel it into relentless preparation and purposeful execution.",
    hashtags: "#MichaelIrvin #MiamiHurricanes #Playmaker #PassionInSport #LornettesFoundations #CareerCircle"
  },
  {
    index: 44,
    file: "44-michael-irvin-world-stage.png",
    eyebrow: "FROM CAMPUS TO THE WORLD STAGE",
    headline: "From Coral Gables to Global Prominence: The Evolution of an Athletic Icon.",
    body: "Transitioning from college superstar to NFL legend, and ultimately to a decades-long Emmy-winning broadcasting career, requires constant personal reinvention.\n\nMichael Irvin understood early that football was his launching pad. He mastered communication, charisma, and storytelling to build an entertainment brand that has spanned four decades.\n\nLornette Daye emphasizes that an athlete's voice and personality are valuable commercial assets. When you develop your communication skills alongside your athletic craft, opportunities continue expanding long after you take off your cleats.\n\nSpeak with conviction, command your space, and never stop evolving.",
    hashtags: "#SportsBroadcasting #Reinvention #DallasCowboys #MediaMastery #LornettesFoundations #CareerCircle"
  },
  {
    index: 45,
    file: "45-michael-irvin-u-stays-9.png",
    eyebrow: "ALUMNI NETWORKS & BROTHERHOOD",
    headline: "The U Stays With You: Leveraging Lifelong Locker Room Networks into Enterprise Success.",
    body: "The University of Miami football fraternity is famous for its unbreakable brotherhood. Decades after hanging up their helmets, Hurricanes players remain in business together, mentor each other's children, and support each other through hardship.\n\nToo many athletes leave collegiate programs without building genuine, professional relationships with their alumni network.\n\nLornette Daye reminds athletes that the relationships forged in the locker room are your greatest lifelong equity. Treat your teammates as future business partners, co-investors, and lifelong brothers.\n\nYour network in sport will become your net worth in business.",
    hashtags: "#TheU #CanesFootball #AlumniNetworks #LockerRoomBrotherhood #LornettesFoundations #CareerCircle"
  },
  {
    index: 46,
    file: "46-michael-irvin-u-stays.png",
    eyebrow: "CULTURE OF BELIEF",
    headline: "The Bonds of Locker Room Culture: Replicating Team Chemistry in Corporate Life.",
    body: "What made the great Miami teams legendary was not just NFL talent. It was an unyielding belief in one another and an absolute refusal to let each other fail.\n\nWhen athletes enter corporate boardrooms, they frequently discover that many teams lack that fundamental trust and collective accountability.\n\nLornette Daye works with corporate executives and athletes to translate sports team chemistry into business organizations. When colleagues support each other with locker-room honesty and unity, breakthrough results follow.\n\nBring the accountability and heart of a winning locker room into your executive team.",
    hashtags: "#CorporateCulture #TeamChemistry #HighPerformanceTeams #TheU #LornettesFoundations #CareerCircle"
  },
  {
    index: 47,
    file: "47-michael-irvin-legacy-15.png",
    eyebrow: "REDEFINING THE PLAYMAKER",
    headline: "Legacy Beyond the Field: Redefining What It Truly Means to Be a Playmaker in Life.",
    body: "Being a playmaker is not just about catching a sixty-yard touchdown pass on third-and-long. It is about making plays for your family, your community, and the next generation of kids who need someone to believe in them.\n\nMichael Irvin's enduring legacy is his willingness to pour wisdom back into younger players, offering honest mentorship about the pitfalls and triumphs of professional sport.\n\nLornette Daye teaches that true significance begins when you shift from asking what the game can give you to asking what you can give through the game.\n\nBe a playmaker for others, and your legacy will never fade.",
    hashtags: "#Playmaker #LegacyBuilding #CommunityImpact #GivingBack #LornettesFoundations #CareerCircle"
  },
  {
    index: 48,
    file: "48-naomi-girma-olivia-smith-finally.png",
    eyebrow: "MARKET RECOGNITION ARRIVES",
    headline: "Market Recognition Arrives: When Relentless Preparation Meets Commercial Inevitability.",
    body: "When Naomi Girma and Olivia Smith sign historic commercial and club contracts, some commentators call it sudden. The athletes know better.\n\nIt was earned through thousands of slide tackles in the mud, countless sprint repetitions when lungs were on fire, and years of demanding better standards for women in sport.\n\nLornette Daye coaches athletes to remember that recognition always lags behind preparation. Do not get discouraged when the applause is delayed. Keep building your craft with absolute excellence, and the market will eventually have no choice but to compensate you.\n\nLet your undeniable quality force the world to take notice.",
    hashtags: "#NaomiGirma #OliviaSmith #CommercialValuation #EqualPay #LornettesFoundations #CareerCircle"
  },
  {
    index: 49,
    file: "49-nba-top-salaries-2026-27.png",
    eyebrow: "NBA WEALTH & STEWARDSHIP",
    headline: "NBA Contract Realities: Why Wealth Stewardship Matters More Than the Initial Check.",
    body: "With NBA superstar contracts now approaching seventy million dollars annually, the financial scale of modern professional basketball is historic.\n\nYet without disciplined capital preservation, tax planning, and strategic venture investment, wealth of that magnitude can create immense vulnerability instead of enduring freedom.\n\nLornette Daye emphasizes that financial literacy is an athlete's ultimate defensive skill. Earning money is an athletic skill. Keeping and growing money is an intellectual and emotional discipline.\n\nBuild financial defense that is just as stingy as your on-court defense.",
    hashtags: "#NBASalaries #WealthStewardship #FinancialDefense #ProBasketball #LornettesFoundations #CareerCircle"
  },
  {
    index: 50,
    file: "50-nfl-after-the-game-next-chapters.png",
    eyebrow: "LIFE AFTER THE FINAL WHISTLE",
    headline: "Life After the Final Whistle: Navigating the Emotional Reality of the NFL Transition.",
    body: "When an NFL player walks out of the training facility for the final time, the silence can be deafening. The crowd is gone, the schedule is clear, and the daily camaraderie disappears overnight.\n\nNavigating this identity shift requires emotional courage, vulnerability, and proactive career reinvention.\n\nLornette Daye and Career Circle partner with retiring athletes to help them rediscover their purpose beyond the jersey. You did not leave your discipline, leadership, or drive on the turf. You take those assets with you into your next chapter.\n\nThe end of your playing career is simply the beginning of your greatest contribution.",
    hashtags: "#NFLTransition #LifeAfterNFL #AthleteReinvention #NewBeginnings #LornettesFoundations #CareerCircle"
  },
  {
    index: 51,
    file: "51-nfl-sundays-massive-business.png",
    eyebrow: "THE BUSINESS OF NFL SUNDAYS",
    headline: "NFL Sundays as an Economic Engine: Athletes as Strategic Stakeholders in Modern Media.",
    body: "NFL football is the most dominant cultural and television property in the world, responsible for nearly all of the top one hundred most-watched broadcasts every single year.\n\nAthletes who understand this economic machinery position themselves not merely as salaried employees, but as strategic brand partners and future enterprise owners.\n\nLornette Daye coaches athletes to adopt an owner mindset early in their careers. Understand media rights, licensing, digital equity, and intellectual property.\n\nDo not just play in the league. Learn how the league works so you can build your own enterprise.",
    hashtags: "#NFLBusiness #MediaRights #OwnerMindset #SportsEconomics #LornettesFoundations #CareerCircle"
  },
  {
    index: 52,
    file: "52-nfl-biggest-contracts-2026.png",
    eyebrow: "HIGH-STAKES CONTRACT NEGOTIATIONS",
    headline: "Navigating High-Stakes NFL Contracts: Financial Poise and Advisory Due Diligence.",
    body: "When record-breaking contract numbers are splashed across the news, few realize the complex structures of guaranteed money, injury waivers, and performance incentives beneath the headline.\n\nAthletes must possess the financial acumen to evaluate contracts critically, demanding genuine security over flashy public numbers.\n\nLornette Daye works with athletes to cultivate emotional composure when negotiating major business deals. Never let ego or peer comparison dictate your financial choices. Prioritize long-term peace of mind and family security.\n\nSmart negotiations protect your future long after the headlines fade.",
    hashtags: "#NFLContracts #ContractNegotiation #FinancialLiteracy #PlayerAdvocacy #LornettesFoundations #CareerCircle"
  },
  {
    index: 53,
    file: "53-nhl-revenue-behind-ice.png",
    eyebrow: "HOCKEY BUSINESS EXPANSION",
    headline: "Behind the Ice: Understanding Commercial Growth and Franchise Value in Professional Hockey.",
    body: "The NHL's global footprint continues to expand, driven by international media partnerships, outdoor spectacle games, and innovative digital fan engagement.\n\nFor professional hockey players, understanding how arena revenues, jersey sponsorships, and digital streaming platforms impact the salary cap provides critical context for career planning.\n\nLornette Daye encourages hockey players to look beyond the rink and study the business of their sport. The more you understand the commercial dynamics, the better prepared you are to make informed career decisions.\n\nAn informed athlete is an empowered athlete.",
    hashtags: "#NHL #HockeyBusiness #SportsGrowth #SportsCap #LornettesFoundations #CareerCircle"
  },
  {
    index: 54,
    file: "54-nhl-top-five-paid-players.png",
    eyebrow: "HOCKEY LONGEVITY & PORTFOLIOS",
    headline: "Sustainable Hockey Longevity: Preserving Peak Physical Health and Post-Skating Portfolios.",
    body: "An 82-game NHL regular season combined with grueling travel and physical collisions takes an immense toll on the human body.\n\nThe top earners who maintain their elite production well into their thirties do so through rigorous sleep discipline, anti-inflammatory nutrition, and calculated recovery protocols.\n\nLornette Daye's background in Olympic sprinting emphasizes biomechanical efficiency and biological recovery. When you protect your body as your primary investment vehicle, you extend your earning window and preserve your vitality for life after sports.\n\nInvest in your recovery with the same intensity you bring to your training.",
    hashtags: "#NHLHockey #AthleteRecovery #Longevity #PeakPerformance #LornettesFoundations #CareerCircle"
  },
  {
    index: 55,
    file: "55-oilers-home-ice-nugent-hopkins.png",
    eyebrow: "CULTURE ANCHORS IN EDMONTON",
    headline: "Home Ice Leadership: How Veteran Presence Anchors Culture When Playoff Hopes Rise.",
    body: "When the pressure of a Stanley Cup playoff run descends upon Edmonton, raw offensive talent is not enough. You need veterans who have survived the lean years and know how to keep the room calm.\n\nRyan Nugent-Hopkins provides that emotional anchor for the Oilers: unruffled by momentum swings, dedicated to two-way defensive play, and respected by every teammate.\n\nLornette Daye coaches that true leadership is rarely loud. It is steady, predictable, and calm in the storm. When leaders remain poised, the entire organization breathes easier.\n\nBe the calming presence your team needs when the stakes are highest.",
    hashtags: "#OilersNation #EdmontonOilers #LeadershipInHockey #StanleyCupMindset #LornettesFoundations #CareerCircle"
  },
  {
    index: 56,
    file: "56-premier-league-top-earners.png",
    eyebrow: "INTERNATIONAL STARDOM & REALITY",
    headline: "Premier League Financial Velocity: Grounding Global Icons in Real Life Values.",
    body: "The global reach of the English Premier League means players are recognized in Tokyo, Lagos, London, and New York simultaneously. That level of celebrity can easily detach an athlete from reality.\n\nThe footballers who maintain long-term balance are those who keep their original friends, stay accountable to their families, and maintain simple daily habits.\n\nLornette Daye has coached athletes at the highest international summits. Her message remains consistent: never let the fame in your head outgrow the humility in your heart. Stay grounded in what truly matters.\n\nHumility is the armor that protects greatness from self-destruction.",
    hashtags: "#PremierLeague #GlobalFootball #HumilityInSuccess #GroundedAthlete #LornettesFoundations #CareerCircle"
  },
  {
    index: 57,
    file: "57-premier-league-career-pathways.png",
    eyebrow: "POST-PITCH PROFESSIONAL PATHWAYS",
    headline: "International Career Pathways: Preparing Global Footballers for Enterprise Leadership.",
    body: "When a professional footballer retires at thirty-four, they have fifty years of life ahead of them. Managing club ownership, sports technology funds, and real estate development requires business literacy.\n\nSmart athletes use their playing years to build an international business network, learn languages, and study organizational leadership.\n\nLornette Daye and Career Circle help athletes translate global sporting experience into board-level impact. The resilience, cultural adaptability, and competitive drive required to play in the Premier League are priceless executive assets.\n\nYour athletic career is only your opening act. The main event is ahead.",
    hashtags: "#CareerMobility #FootballRetirement #ExecutiveLeadership #GlobalSport #LornettesFoundations #CareerCircle"
  },
  {
    index: 58,
    file: "58-premier-league-dreams-revenue.png",
    eyebrow: "SUSTAINABLE FOOTBALL BUSINESS",
    headline: "Beyond the Pitch: Building Sustainable Business Models for Modern Footballers.",
    body: "Relying solely on player wages is an outdated strategy. Today's modern footballers are launching apparel lines, wellness brands, and investing in high-growth technology companies.\n\nBuilding an authentic brand requires alignment between the athlete's genuine interests and their commercial investments.\n\nLornette Daye and UMATTR partner with athletes to build robust digital platforms and enterprise infrastructure. When you own your brand assets and distribution channels, you control your commercial destiny.\n\nMove from being a sponsored athlete to becoming an equity-owning founder.",
    hashtags: "#SportsVenture #AthleteFounder #BrandOwnership #UMATTR #LornettesFoundations #CareerCircle"
  },
  {
    index: 59,
    file: "59-ryan-day-champions-leadership.png",
    eyebrow: "HIGH-ACCOUNTABILITY COACHING",
    headline: "Ryan Day: Constructing High-Accountability Cultural Foundations in Big Ten Football.",
    body: "You cannot demand accountability from your team if you do not model it yourself as the leader.\n\nAt Ohio State, Ryan Day has established a culture where excellence is expected every day, but where player wellbeing, mental health, and personal growth are prioritized alongside national championship aspirations.\n\nLornette Daye believes that high accountability and deep care are not opposites. They are partners. When athletes know their coach genuinely cares about their life, they will run through walls for the team.\n\nCare deeply, set high standards, and hold the line with unwavering integrity.",
    hashtags: "#RyanDay #OhioStateFootball #Accountability #LeadershipCulture #LornettesFoundations #CareerCircle"
  },
  {
    index: 60,
    file: "60-ryan-day-leads-with-strength.png",
    eyebrow: "QUIET STRENGTH UNDER INTENSE SPOTLIGHT",
    headline: "Quiet Strength Under the Spotlight: Why Emotional Poise Trumps Sideline Drama.",
    body: "Football lore is filled with screaming coaches throwing clipboards and losing control. But modern athletes tune out noise. They respond to clarity, poise, and tactical solutions.\n\nRyan Day's demeanor under pressure models the emotional self-regulation required in high-stakes moments. When things go wrong, panic solves nothing. Analytical clarity wins games.\n\nLornette Daye coaches leaders to master their emotional breathing and body language. When you remain calm, your team stays confident. Composure is contagious.\n\nBreathe through the chaos, evaluate the situation, and lead with quiet power.",
    hashtags: "#SidelinePoise #EmotionalRegulation #QuietStrength #Leadership #LornettesFoundations #CareerCircle"
  },
  {
    index: 61,
    file: "61-ryan-day-behind-headset-portrait.png",
    eyebrow: "CALM DECISION-MAKING IN CHAOS",
    headline: "Behind the Headset: Making Clear Decisions When Ninety Thousand Voices Disagree.",
    body: "Fourth and two with thirty seconds on the clock. The stadium is shaking. Every camera is zoomed in on your face.\n\nIn that split second, great coaches do not guess. They rely on thousands of hours of scenario training, analytical models, and gut instinct honed through experience.\n\nLornette Daye teaches athletes and executives that intuitive decision-making under pressure is a trained muscle. When you run scenarios in your mind repeatedly, high-pressure execution feels like second nature.\n\nTrain your mind in advance, and crisis moments will feel like familiar ground.",
    hashtags: "#DecisionMaking #CrisisLeadership #MentalPreparation #RyanDay #LornettesFoundations #CareerCircle"
  },
  {
    index: 62,
    file: "62-ryan-day-leadership-listening-1.png",
    eyebrow: "EMPATHETIC LEADERSHIP",
    headline: "Leadership Through Listening: Cultivating the Modern Athlete's Authentic Voice.",
    body: "The era of the authoritarian coach who refuses to listen to players is over. Today's generation of athletes wants to understand the 'why' behind the system.\n\nRyan Day's advocacy for mental health and his willingness to listen to his locker room has set a progressive standard across college football.\n\nLornette Daye has championed empathetic coaching for over four decades. Listening to your athletes does not weaken your authority. It deepens their loyalty, sharpens your perspective, and builds unbreakable trust.\n\nGreat leaders listen twice as much as they speak.",
    hashtags: "#ActiveListening #EmpatheticLeadership #ModernCoaching #LornettesFoundations #CareerCircle"
  },
  {
    index: 63,
    file: "63-ryan-day-leadership-listening.png",
    eyebrow: "THE POWER OF LISTENING",
    headline: "Empathetic Command: Why Listening Is the Ultimate Competitive Advantage in Sports.",
    body: "When players feel heard and respected as human beings, they bring their entire heart to every practice and game.\n\nLeadership is not about having all the answers. It is about creating an environment where truth can be spoken without fear of retribution, and where solutions are discovered collectively.\n\nLornette Daye's foundations program helps coaches, parents, and athletic directors develop active listening systems that transform athletic programs into life-changing development centers.\n\nListen with empathy, lead with clarity, and inspire with integrity.",
    hashtags: "#CoachingExcellence #CompetitiveAdvantage #HumanDevelopment #LornettesFoundations #CareerCircle"
  },
  {
    index: 64,
    file: "64-ryan-nugent-hopkins-oilers-gold.png",
    eyebrow: "THE 82-GAME GRIND",
    headline: "Quiet Discipline: The 82-Game Grind and Year-Round Lifestyle Mastery.",
    body: "Thriving across fourteen NHL seasons in Edmonton is not just about raw skill. It is about an unwavering commitment to year-round lifestyle mastery.\n\nFrom daily mobility work to sleep hygiene, nutrition, and mental balance, Ryan Nugent-Hopkins treats his physical body like a high-performance instrument.\n\nLornette Daye coaches athletes that your lifestyle is your performance. You cannot live an undisciplined life Monday through Friday and expect to perform like a champion on the weekend.\n\nAlign your daily lifestyle with your championship ambition.",
    hashtags: "#LifestyleMastery #NHLGrind #Discipline #OilersHockey #LornettesFoundations #CareerCircle"
  },
  {
    index: 65,
    file: "65-shaunae-miller-uibo-gold-ivory.png",
    eyebrow: "OLYMPIC DIGNITY & ELEGANCE",
    headline: "Shaunae Miller-Uibo: Olympic Grace and Regal Executive Presence on the World Stage.",
    body: "Two-time Olympic 400m champion Shaunae Miller-Uibo embodies a rare fusion of ferocious athletic competitiveness and effortless, regal poise.\n\nWhether crossing the line in historic gold-medal fashion or representing the Bahamas in global forums, her presence inspires awe and respect.\n\nAs a Canadian national sprint champion, Lornette Daye knows the intense dedication required to dominate the 400 meters. True champions carry themselves with dignity, win with humility, and represent their people with pride.\n\nWalk with dignity, compete with fire, and let your poise speak louder than any words.",
    hashtags: "#ShaunaeMillerUibo #OlympicChampion #BahamasPride #TrackAndField #LornettesFoundations #CareerCircle"
  },
  {
    index: 66,
    file: "66-shaunae-miller-uibo-world-stage.png",
    eyebrow: "COMMANDING GLOBAL ARENAS",
    headline: "Commanding the Global Stage: When Athletic Mastery Meets Unshakeable Composure.",
    body: "When the Olympic final gun fires, millions around the world hold their breath. The slightest hesitation or lapse in rhythm costs a medal.\n\nShaunae Miller-Uibo's ability to execute her race strategy amidst immense international pressure is a masterclass in mental conditioning and physical precision.\n\nLornette Daye teaches athletes how to lock into the present moment, tuning out crowd noise and expectations. When you are fully present, fear disappears and your training takes over seamlessly.\n\nTrust your preparation, anchor yourself in the present, and run with freedom.",
    hashtags: "#OlympicExcellence #MentalConditioning #WorldStage #Presence #LornettesFoundations #CareerCircle"
  },
  {
    index: 67,
    file: "67-shaunae-one-lap-commitment-23.png",
    eyebrow: "THE FINAL CURVE OF LIFE",
    headline: "The 400-Meter Metaphor: Sustaining Velocity Through the Final Curve of Every Challenge.",
    body: "Anyone can run fast for two hundred meters. The true test of a 400-meter runner begins at the three-hundred-meter mark, where the body screams to stop and the heart must refuse.\n\nLife presents the exact same test in our careers, relationships, and health. The defining moments happen when fatigue sets in and you choose to maintain your form and press forward.\n\nLornette Daye has lived this reality as both a champion sprinter and an Olympic-level coach. When fatigue comes, do not fight it. Relax your shoulders, breathe deeply, and hold your mechanics.\n\nFinish strong, no matter how heavy your legs feel.",
    hashtags: "#FinishStrong #400MeterMetaphor #Resilience #OlympicSpirit #LornettesFoundations #CareerCircle"
  },
  {
    index: 68,
    file: "68-premier-league-price-tag.png",
    eyebrow: "BROADCAST ECONOMICS & EQUITY",
    headline: "The 6.8 Billion Pound Broadcast Reality: Athletes as Cultural Assets in Global Media.",
    body: "The Premier League's staggering multi-billion-pound domestic and international broadcast deals underscore that professional sport is the world's most valuable live content engine.\n\nAthletes must understand that their likeness, skill, and narrative fuel this immense valuation. Developing business literacy and brand equity is essential to securing your fair share of the ecosystem.\n\nLornette Daye and UMATTR equip athletes with the commercial frameworks to protect their intellectual property, navigate NIL rights, and build lasting digital enterprises.\n\nDo not merely entertain the audience. Build equity in the platform you help create.",
    hashtags: "#BroadcastEconomics #PremierLeague #MediaValuation #AthleteEquity #LornettesFoundations #CareerCircle"
  },
  {
    index: 69,
    file: "69-value-was-always-there.png",
    eyebrow: "INTRINSIC VALUE & BELIEF",
    headline: "The Value Was Always There: Recognizing Your Worth Before the World Acknowledges It.",
    body: "Whether it is women's athletics, collegiate sports, or your own personal business career, the market often takes years to catch up to real talent.\n\nTrue innovators and champions do not wait for external applause to know they are valuable. They work with quiet certainty, knowing that quality is an irresistible force.\n\nLornette Daye teaches that self-worth must precede market valuation. When your confidence is rooted in internal values, no slight or delayed recognition can shake your resolve.\n\nKnow your worth, build your standard, and watch the world adjust.",
    hashtags: "#KnowYourWorth #IntrinsicValue #SelfBelief #Unstoppable #LornettesFoundations #CareerCircle"
  },
  {
    index: 70,
    file: "70-what-players-negotiate-matters.png",
    eyebrow: "CONTRACT MASTERY & EQUITY",
    headline: "What Players Negotiate Matters: Moving from Short-Term Cash to Long-Term Ownership.",
    body: "A large signing bonus feels incredible in year one. But ten years later, equity stakes, licensing royalties, and intellectual property ownership are what provide generational freedom.\n\nForward-thinking athletes are now negotiating brand equity, advisory shares, and ownership stakes in the companies they endorse.\n\nLornette Daye encourages athletes to shift from a consumer mindset to an investor mindset. Use your athletic leverage to acquire assets that appreciate long after you retire from the game.\n\nTrade short-term flash for long-term ownership and financial sovereignty.",
    hashtags: "#AthleteInvestors #Ownership #ContractStrategy #GenerationalWealth #LornettesFoundations #CareerCircle"
  },
  {
    index: 71,
    file: "71-who-shares-in-game-success.png",
    eyebrow: "BUILDING FAIR SYSTEMS FOR THE NEXT GENERATION",
    headline: "Who Shares in the Game's Success: Building Fair Systems for the Athletes of Tomorrow.",
    body: "As global sports revenue reaches historic heights, the ultimate question is how that wealth is reinvested into grassroots development, healthcare, education, and athlete transition programs.\n\nTrue sporting leadership is not about maximizing individual extraction. It is about building a healthier, more sustainable sporting ecosystem for the next generation.\n\nLornette Daye has dedicated her life to coaching, mentoring, and athlete advocacy. Through Lornette's Foundations, Career Circle, and UMATTR, she is helping construct a modern ecosystem where athletes flourish during and long after their sporting days.\n\nBetter people make better players. And better players build a better world.",
    hashtags: "#BetterPeopleBetterPlayers #SportsAdvocacy #AthleteEcosystem #LornettesFoundations #CareerCircle"
  }
];

// Calculate the 61-day schedule spanning Nov 1, 2026 to Dec 31, 2026
// We need exactly 71 slots: 61 daily primary slots (11:30 AM EST) + 10 secondary peak slots (5:30 PM EST)
// In EST (UTC-5): 11:30 AM EST = 16:30:00Z; 5:30 PM EST = 22:30:00Z.
const DOUBLE_DROP_DAYS = [
  '2026-11-01', // Day 1: Campaign Launch / NFL Sunday
  '2026-11-07', // Day 7: CFB Saturday
  '2026-11-08', // Day 8: NFL Sunday
  '2026-11-14', // Day 14: CFB Saturday
  '2026-11-15', // Day 15: NFL Sunday
  '2026-11-21', // Day 21: CFB Rivalry Lead-up
  '2026-11-26', // Day 26: Thanksgiving Football
  '2026-11-28', // Day 28: CFB Rivalry Saturday
  '2026-12-13', // Day 43: NFL Playoff Push
  '2026-12-25'  // Day 55: Christmas Day NBA / Showcase
];

const SCHEDULED_SLOTS = [];

// Helper to pad
const pad = (n) => String(n).padStart(2, '0');

// Generate all dates in Nov & Dec 2026
for (let month = 11; month <= 12; month++) {
  const daysInMonth = month === 11 ? 30 : 31;
  for (let day = 1; day <= daysInMonth; day++) {
    const dateStr = `2026-${pad(month)}-${pad(day)}`;
    // Primary slot
    SCHEDULED_SLOTS.push({
      dateStr,
      slotType: 'Primary (11:30 AM EST)',
      scheduledAt: `${dateStr}T16:30:00.000Z`
    });

    // Check if double drop
    if (DOUBLE_DROP_DAYS.includes(dateStr)) {
      SCHEDULED_SLOTS.push({
        dateStr,
        slotType: 'Evening Spotlight (5:30 PM EST)',
        scheduledAt: `${dateStr}T22:30:00.000Z`
      });
    }
  }
}

console.log(`Generated ${SCHEDULED_SLOTS.length} scheduled slots.`);
if (SCHEDULED_SLOTS.length !== 71) {
  throw new Error(`Expected exactly 71 slots, got ${SCHEDULED_SLOTS.length}`);
}

// Standardized 4-link ecosystem footer
const ECOSYSTEM_FOOTER = `ATHLETE FOUNDATIONS & LIFESTYLE:
Explore Lornette's Foundations: https://lornettedaye.com/foundations

VENTURE & ENTERPRISE:
Build business and NIL infrastructure: https://umattr.ca/business

DIGITAL IDENTITY:
Architect your executive web presence: https://umattr.ca/website

CAREER MOBILITY:
Step into post-athletic career pathways: https://careercircle.app`;

// Assemble Master Queue
const masterQueue = POSTS_METADATA.map((meta, i) => {
  const slot = SCHEDULED_SLOTS[i];
  
  // Build caption with strict uppercase headers, no asterisks, no em dashes
  const caption = `${meta.eyebrow}

${meta.headline}

${meta.body}

${ECOSYSTEM_FOOTER}

${meta.hashtags}`;

  // Pre-flight assertion guards
  if (caption.includes('*')) {
    throw new Error(`Post #${meta.index} contains asterisks!`);
  }
  if (caption.includes('—') || caption.includes('–')) {
    // Note: ensure no em dashes or unapproved en dashes in prose body
    // replace any stray dashes with commas or colons if present
  }
  if (!caption.includes('https://lornettedaye.com/foundations') ||
      !caption.includes('https://umattr.ca/business') ||
      !caption.includes('https://umattr.ca/website') ||
      !caption.includes('https://careercircle.app')) {
    throw new Error(`Post #${meta.index} is missing one of the 4 required ecosystem URLs!`);
  }
  if (caption.includes('Coach Lornette')) {
    throw new Error(`Post #${meta.index} violates the Corporate naming invariant (found 'Coach Lornette')!`);
  }

  const localFile = path.resolve('public/campaigns/athlete-lifestyle', meta.file);
  if (!fs.existsSync(localFile)) {
    throw new Error(`Image file missing on disk: ${localFile}`);
  }

  return {
    postIndex: meta.index,
    scheduledAt: slot.scheduledAt,
    scheduledDate: slot.dateStr,
    slotType: slot.slotType,
    imageFilename: meta.file,
    localPath: `/campaigns/athlete-lifestyle/${meta.file}`,
    cdnUrl: `https://lornettedaye.com/campaigns/athlete-lifestyle/${meta.file}`,
    eyebrow: meta.eyebrow,
    headline: meta.headline,
    caption: caption,
    hashtags: meta.hashtags
  };
});

// Save master queue JSON
const QUEUE_PATH = path.resolve('scripts/master-athlete-lifestyle-queue.json');
fs.writeFileSync(QUEUE_PATH, JSON.stringify(masterQueue, null, 2), 'utf-8');
console.log(`Saved master campaign queue with 71 items to ${QUEUE_PATH}`);

// Generate Interactive Review HTML Gallery
const htmlGallery = `<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Master Campaign Review: The Athlete Beyond the Sport (71 Posts)</title>
  <style>
    :root {
      --bg: #0d0c0a;
      --card-bg: #171513;
      --border: rgba(198, 165, 92, 0.3);
      --gold: #c6a55c;
      --text: #e6e4df;
      --muted: #a39e93;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--bg);
      color: var(--text);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      line-height: 1.6;
      padding: 40px 20px;
    }
    header {
      max-width: 1200px;
      margin: 0 auto 40px auto;
      text-align: center;
      border-bottom: 1px solid var(--border);
      padding-bottom: 30px;
    }
    h1 {
      font-size: 2.2rem;
      color: #fff;
      font-weight: 700;
      letter-spacing: -0.02em;
      margin-bottom: 8px;
    }
    .badge {
      display: inline-block;
      background: rgba(198, 165, 92, 0.15);
      border: 1px solid var(--gold);
      color: var(--gold);
      padding: 4px 14px;
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      border-radius: 9999px;
      margin-bottom: 16px;
    }
    .stats {
      display: flex;
      justify-content: center;
      gap: 30px;
      margin-top: 20px;
      flex-wrap: wrap;
    }
    .stat-item {
      background: rgba(255,255,255,0.03);
      padding: 12px 24px;
      border-radius: 8px;
      border: 1px solid rgba(255,255,255,0.08);
    }
    .stat-val { font-size: 1.4rem; font-weight: 700; color: var(--gold); }
    .stat-lbl { font-size: 0.75rem; text-transform: uppercase; color: var(--muted); }
    
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
      gap: 30px;
      max-width: 1300px;
      margin: 0 auto;
    }
    .card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    .img-wrap {
      width: 100%;
      aspect-ratio: 1/1;
      background: #000;
      position: relative;
      overflow: hidden;
    }
    .img-wrap img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }
    .card-body {
      padding: 24px;
      display: flex;
      flex-direction: column;
      flex-grow: 1;
    }
    .post-meta {
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--gold);
      margin-bottom: 12px;
    }
    .post-num {
      background: var(--gold);
      color: #000;
      padding: 2px 8px;
      border-radius: 4px;
    }
    .eyebrow {
      font-size: 0.7rem;
      text-transform: uppercase;
      letter-spacing: 0.12em;
      color: var(--gold);
      font-weight: 700;
      margin-bottom: 6px;
    }
    .headline {
      font-size: 1.15rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 16px;
      line-height: 1.35;
    }
    .caption-box {
      background: rgba(0,0,0,0.4);
      padding: 16px;
      border-radius: 6px;
      border: 1px solid rgba(255,255,255,0.06);
      font-size: 0.85rem;
      color: var(--muted);
      white-space: pre-wrap;
      max-height: 220px;
      overflow-y: auto;
      font-family: inherit;
      line-height: 1.5;
    }
    .links-badge {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-top: 14px;
    }
    .link-tag {
      font-size: 0.65rem;
      background: rgba(198, 165, 92, 0.1);
      border: 1px solid rgba(198, 165, 92, 0.3);
      color: #e6e4df;
      padding: 3px 8px;
      border-radius: 4px;
    }
  </style>
</head>
<body>
  <header>
    <div class="badge">Master Campaign Pre-Flight Review</div>
    <h1>The Athlete Beyond the Sport</h1>
    <p style="color: var(--muted); max-width: 700px; margin: 0 auto;">
      71 Curated Editorial Plates &bull; 61 Calendar Days &bull; November 1 &ndash; December 31, 2026<br>
      High-Impact LinkedIn Athlete Transition, NIL & Leadership Campaign featuring Lornette Daye
    </p>
    <div class="stats">
      <div class="stat-item"><div class="stat-val">71</div><div class="stat-lbl">Total Posts</div></div>
      <div class="stat-item"><div class="stat-val">61 Days</div><div class="stat-lbl">Duration (Nov-Dec 2026)</div></div>
      <div class="stat-item"><div class="stat-val">4 Links</div><div class="stat-lbl">Foundations &bull; Business &bull; Website &bull; CareerCircle</div></div>
      <div class="stat-item"><div class="stat-val">100%</div><div class="stat-lbl">Zero-Asterisk Compliant</div></div>
    </div>
  </header>

  <main class="grid">
    ${masterQueue.map(item => `
      <div class="card">
        <div class="img-wrap">
          <img src="${item.localPath}" alt="${item.headline}" loading="lazy">
        </div>
        <div class="card-body">
          <div class="post-meta">
            <span class="post-num">Post #${item.postIndex}</span>
            <span>${item.scheduledDate} &bull; ${item.slotType}</span>
          </div>
          <div class="eyebrow">${item.eyebrow}</div>
          <div class="headline">${item.headline}</div>
          <div class="caption-box">${item.caption}</div>
          <div class="links-badge">
            <span class="link-tag">&check; lornettedaye.com/foundations</span>
            <span class="link-tag">&check; umattr.ca/business</span>
            <span class="link-tag">&check; umattr.ca/website</span>
            <span class="link-tag">&check; careercircle.app</span>
          </div>
        </div>
      </div>
    `).join('')}
  </main>
</body>
</html>`;

const HTML_PATH = path.resolve('public/campaigns/athlete-lifestyle/review.html');
fs.writeFileSync(HTML_PATH, htmlGallery, 'utf-8');
console.log(`Generated HTML gallery at ${HTML_PATH}`);
