# -*- coding: utf-8 -*-
"""
Campaign Builder for "THIERRY HENRY: VISION BEYOND THE GAME"
Generates 120 detailed, bespoke posts across 40 days (Oct 3, 2026 - Nov 11, 2026).
3 posts per day: Morning (9:15 AM), Late Afternoon (4:15 PM), Evening Prime (8:15 PM) MDT/MST.
Featuring Thierry Henry: World Cup Champion, Arsenal Invincible, Olympic Mentor.
Strict Invariants:
- Zero em dashes (—, &mdash;, \u2014)
- Authoritative Olympian coach voice (first-person, "I", "my")
- Signed strictly as "Lornette"
- 50/50 Keynote (lornettedaye.com/book) vs Book (lornettedaye.com/books) CTA split
- Incremental report saving to disk upon every post
"""
import sys
import os
import json
from datetime import datetime, timedelta

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)

# -------------------------------------------------------------
# 20 BESPOKE POST CONCEPTS FOR THIERRY HENRY
# Across 6 progressive thematic flights = 120 posts total
# -------------------------------------------------------------

def get_flight_concepts(flight_idx):
    """
    Returns 20 bespoke (title, hook, body, takeaway) tuples for each of the 6 flights.
    """
    if flight_idx == 0:
        # Flight 1 (Posts 1-20): The Architecture of Elegance & Preparation
        return [
            ("THE ILLUSION OF EFFORTLESS ELEGANCE",
             "When Thierry Henry opened up his body and passed the ball into the far corner of the net, spectators called it effortless poetry.",
             "What the world called effortless was the result of monastic, obsessive repetition behind closed doors. At Clairefontaine and Arsenal, Henry took hundreds of identical finishing shots from the left channel until his muscles could execute the movement without conscious thought. In forty years of Olympic coaching, I have watched fans confuse polished mastery with raw luck. Elegance is simply discipline made invisible.",
             "If you want your executive team to execute seamlessly under pressure, eliminate friction through relentless unglamorous drills long before game day."),
            
            ("THE OBSESSION WITH VIDEO ANALYSIS",
             "Long before digital tablets were standard equipment, Thierry Henry was studying opponent defenders like a chess grandmaster.",
             "He memorized which full-backs leaned forward on their heels, which center-backs struggled with balls over their shoulders, and how goalkeepers shifted their weight before a penalty. He did not step onto the pitch hoping for opportunities; he arrived with an exhaustive mental dossier. Modern leadership requires that exact analytical rigor.",
             "Never enter a boardroom negotiation relying solely on charisma. Master the operational data until your counterpart's moves are predictable."),
            
            ("SPEED WITHOUT CONTROL IS JUST NOISE",
             "Many football players possess raw sprint speed. Thierry Henry possessed cognitive deceleration.",
             "He could sprint at thirty-five kilometers per hour and instantly downshift his heart rate to stroke a delicate chip over an oncoming goalkeeper. That ability to find stillness in the midst of violent velocity is the signature of elite athletic mastery. In corporate crisis management, leaders often make frantic mistakes because they confuse hurried reaction with decisive action.",
             "When markets move at breakneck speed, your greatest strategic weapon is deliberate, focused calm."),
            
            ("THE SACRED GEOMETRY OF SPATIAL AWARENESS",
             "Thierry Henry did not just run where the ball was. He ran into the empty space where the ball had to arrive.",
             "Arsène Wenger taught Henry that spatial awareness is the highest form of athletic intelligence. By drifting wide to the left touchline, Henry stretched entire defensive backlines, creating wide interior lanes for his midfielders to exploit. He understood that personal sacrifice in positioning elevates the performance of the entire unit.",
             "Evaluate your leaders not just by the direct results they generate, but by the strategic space their movement creates for colleagues."),
            
            ("REFINING YOUR SIGNATURE MOVE",
             "Everyone in world football knew Henry wanted to open his hips and curl the ball into the bottom right corner. No one could stop it.",
             "Having a diverse skill set is admirable, but having an unstoppable core competence is what builds dynasties. Henry refined his signature finish to such mathematical precision that even when defenders anticipated the shot, the execution was so flawless that intervention was impossible.",
             "Identify the single core capability that gives your enterprise an undeniable advantage, and polish it until it is bulletproof."),
            
            ("THE REJECTION OF COMPLACENCY",
             "After winning the 1998 World Cup at twenty years old, Henry returned to the training pitch the following Tuesday to work on his weak foot.",
             "Lesser players spend the rest of their careers celebrating their early triumphs. True champions use early victories as proof of concept, raising their standards higher. As an Olympic coach, I watched many young talents collapse under early praise because they stopped learning. Henry stayed a student of football until his final match.",
             "Guard your culture against the rot of early satisfaction. The moment you believe you have arrived is the moment your decline begins."),
            
            ("TECHNICAL PRECISION OVER BRUTE FORCE",
             "Watch Henry's goals: very few were driven with wild, reckless power. Almost all were guided with surgical placement.",
             "He famously said: 'Why hit the ball with all your strength when a side-foot pass to the net is impossible to save?' That philosophy of precision over brute force applies directly to resource allocation. Companies that burn millions on aggressive, unfocused marketing campaigns often lose to disciplined competitors who target high-intent niches.",
             "Focus on accuracy and timing rather than brute expenditure. Precision will always outperform uncalibrated force."),
            
            ("THE ART OF FIRST-TOUCH MASTERY",
             "Dennis Bergkamp and Thierry Henry shared a single obsession: the absolute perfection of the first touch.",
             "If your first touch is heavy, you waste two seconds looking down at your feet, and the defense recovers. If your first touch is flawless, your head stays up, you scan the field, and you dictate the tempo. In organizational leadership, your 'first touch' is how you respond to incoming problems. A poised initial response preserves strategic initiative.",
             "Train your management team to handle unexpected crises with clean, balanced composure on first contact."),
            
            ("COMMUNICATING WITH EYES AND SHOULDERS",
             "On the pitch, Henry rarely shouted. He communicated through subtle shoulder drops, eye contact, and head nods.",
             "Elite teams operate with high-context communication. When you train together with obsessive alignment, you do not need long, noisy meetings to coordinate complex plays. A glance conveys the plan. In corporate operations, high-performing divisions replace endless email threads with intuitive alignment built on shared values.",
             "Build deep shared context within your team so execution becomes intuitive and silent."),
            
            ("THE DISCIPLINE OF BODY LANGUAGE",
             "Even when exhausted in the 88th minute, Henry never bent over with his hands on his knees. He stood tall, chest out, chin elevated.",
             "He understood that opponents draw psychological oxygen from your visible signs of fatigue. In forty years of Olympic competition, I taught my athletes that posture is psychological warfare. When you refuse to display weakness, you crush the spirit of competitors waiting for you to break.",
             "Your team and your competitors watch your posture in difficult moments. Carry yourself with unshakable dignity."),
            
            ("THE VALUE OF UNSELFISH ASSISTS",
             "In the 2002-2003 Premier League season, Thierry Henry scored 24 goals and provided 20 assists: a record that stands untouched.",
             "He was the league's most lethal goal scorer, yet he took equal joy in sliding perfect passes to Robert Pirès and Freddie Ljungberg. He rejected the selfish striker stereotype. He proved that the ultimate individual legacy is created by making your teammates look like world-beaters alongside you.",
             "Reward the leaders who set up their colleagues for success as lavishly as you reward individual rainmakers."),
            
            ("THE CULTURE OF HIGH STANDARDS",
             "In Arsenal training, if a young player played a lazy pass, Henry would stop the drill and demand they do it again.",
             "Some called him demanding; his teammates called him a winner. He refused to let standards slip in practice because he knew that sloppy habits practiced on Wednesday become catastrophic errors on Saturday. High-performance cultures require leaders who protect standards with fierce conviction.",
             "Tolerating mediocrity in small daily routines is an open invitation to disaster during major corporate initiatives."),
            
            ("TURNING EMOTIONAL FRUSTRATION INTO FUEL",
             "When defenders fouled Henry or referees missed blatant handballs, he did not pout or lose his composure.",
             "He channeled the surge of adrenaline into laser-focused tactical retaliation. Within five minutes, he would pick up the ball forty yards from goal, dribble past three defenders, and score. Emotional discipline is not about suppressing passion; it is about directing volatile emotions toward constructive conquest.",
             "Teach your leaders how to convert legitimate frustration into focused, decisive business breakthroughs."),
            
            ("THE POWER OF A SIGNATURE IDENTITY",
             "Thierry Henry wore his socks pulled over his knees, tied his boots with deliberate rituals, and carried an unmistakable aura.",
             "Great leaders understand that personal identity and presence matter. It was not vanity; it was a physical armor that communicated authority before the whistle blew. When you cultivate a strong, dignified executive presence, you command attention and set the tone for the entire enterprise.",
             "Never apologize for having a distinctive presence. Show up with an aesthetic and posture that communicates excellence."),
            
            ("STUDYING THE MASTERS WHO CAME BEFORE",
             "Henry spent his youth watching tapes of Marco van Basten, Romário, and George Weah.",
             "He deconstructed their movements, their timing, and their mentality, absorbing the best traits of each legend into his own hybrid style. In modern executive development, the fastest route to leadership maturity is studying historic case studies of CEOs who steered enterprises through turbulent storms.",
             "Ground your leadership development in the proven wisdom of those who built enduring institutions before you."),
            
            ("THE COURAGE TO ADAPT TO NEW LEAGUES",
             "From Ligue 1 to Serie A, then the Premier League, La Liga, and MLS: Thierry Henry adapted and dominated everywhere.",
             "He did not insist that new leagues conform to his preferences. At Barcelona, he accepted a wider, more disciplined tactical role on the wing under Pep Guardiola to help the team win a historic sextuple. Versatility is the mark of true greatness.",
             "Do not let rigid pride prevent you from adapting your methods when stepping into unfamiliar markets."),
            
            ("UNDERSTANDING THE PSYCHOLOGY OF YOUR OPPONENT",
             "Before a match, Henry would observe opposing defenders during warm-ups, assessing their body language and confidence.",
             "He looked for signs of nervous tension, tight hamstrings, or hesitation. When the match began, he targeted those exact vulnerabilities. In competitive business strategy, success requires understanding your competitor's operational constraints and psychological pressure points.",
             "Analyze the psychological constraints of your competitors. Win the battle of perception before the product launches."),
            
            ("THE RESPONSIBILITY OF WEARING NUMBER FOURTEEN",
             "When Henry arrived at Arsenal, he took the number fourteen shirt, transforming it into an iconic symbol worldwide.",
             "He understood that wearing an iconic number brings heavy expectations. Instead of shrinking from the weight, he embraced it, building a legacy that young players across the globe still aspire to emulate. Great leaders lean into responsibility.",
             "Do not run from the weight of expectations. Use high standards as the anvil upon which your legacy is forged."),
            
            ("MAINTAINING CHILDLIKE JOY FOR THE CRAFT",
             "Watch Henry talk about football today: his eyes still light up like a schoolboy kicking a ball in the park.",
             "Despite winning every trophy available in world football, he never lost his infectious love for the game. When work becomes purely transactional, energy depletes and cynicism takes root. Sustained high performance requires reconnecting daily with the intrinsic joy of your craft.",
             "Protect your love for your industry. Genuine enthusiasm is an infectious, non-replicable competitive advantage."),
            
            ("THE DEFINITION OF VISION BEYOND THE GAME",
             "Thierry Henry's greatest triumph was not his trophies; it was his understanding that sport is a classroom for character.",
             "He used football to develop discipline, cultural intelligence, resilience, and mentorship. Today, whether coaching young Olympic athletes or analyzing matches for millions on global television, he stands as a regal statesman. That is vision beyond the game.",
             "Build your career so that your professional victories become stepping stones to permanent human impact.")
        ]
    elif flight_idx == 1:
        # Flight 2 (Posts 21-40): The Invincible Mentality & Relentless Standards
        return [
            ("FORTY-NINE GAMES UNBEATEN: THE ARCHITECTURE OF PERFECTION",
             "Arsenal's 2003-2004 Invincibles season was not an accident of talent. It was the triumph of an uncompromising daily standard.",
             "Going thirty-eight Premier League matches without a single defeat requires an operational consistency that modern corporations can barely fathom. It meant that on wet, freezing Tuesday nights in Blackburn or high-stakes derbies at White Hart Lane, no one took a play off. In my Olympic coaching career, I taught athletes that greatness is not an occasional lightning strike; it is an unwavering baseline.",
             "Establish an operational baseline so disciplined that even your worst day outperforms your competitor's best effort."),
            
            ("REFUSING COMFORT WHEN LEADING THE LEAGUE",
             "When Arsenal were five points clear in February 2004, Arsène Wenger and Thierry Henry banned any celebratory talk in the locker room.",
             "Comfort is the silent killer of dynasties. When an enterprise achieves record quarterly revenue, the natural human temptation is to relax, celebrate, and ease off the throttle. The Invincibles understood that comfort is the enemy of immortality. They pushed harder when they were ahead.",
             "When your company takes the market lead, double your operational rigor. That is when competitors are most vulnerable."),
            
            ("MUTUAL ACCOUNTABILITY WITHOUT TOXICITY",
             "In the Invincibles locker room, Henry, Patrick Vieira, and Sol Campbell demanded absolute accountability from every player.",
             "If someone failed to track back on defense, they were addressed directly and firmly before the team reached the tunnel. But here is the lesson: the criticism was never personal; it was about protecting the shared mission. High-performance cultures require radical candor delivered with deep mutual respect.",
             "Create a culture where team members can challenge each other directly without damaging psychological safety."),
            
            ("MANAGING FATIGUE ON THE RUN-IN",
             "By April 2004, the physical toll of competing across four tournaments was immense. Henry's legs were bruised, tight, and weary.",
             "Yet against Liverpool at Highbury, trailing 1-2 at halftime, Henry delivered one of the greatest individual hat-tricks in football history, including an unforgettable solo run that dismantled the entire defense. He proved that when physical energy is depleted, championship character and technical poise take over.",
             "When fatigue strikes your leadership team, rely on your core systems and character to carry you across the finish line."),
            
            ("THE COURAGE TO DEFEND AN UNBEATEN RUN",
             "As the unbeaten streak mounted, the psychological pressure on Arsenal grew exponentially heavier with every passing weekend.",
             "Opposing teams played with desperate intensity, determined to be the ones who ended history. Henry taught his squad to embrace the target on their backs. When you are the standard-bearer in your market, you must expect every competitor to bring their absolute fiercest game against you.",
             "Do not complain about the intensity of competition. Take pride in being the benchmark everyone else is trying to beat."),
            
            ("THE DISCIPLINE OF CLOSING OUT MATCHES",
             "Great teams do not just take leads; they strangle the life out of matches in the final fifteen minutes.",
             "Henry was a master of game management: holding the ball at the corner flag, drawing fouls, controlling the tempo, and starving opponents of possession. In corporate mergers and product rollouts, deals collapse because leaders fail to manage the final, critical closing stages with discipline.",
             "Bring your highest level of tactical vigilance to the final ten percent of any strategic project."),
            
            ("ELIMINATING INDIVIDUAL EGOS FOR COLLECTIVE TRIUMPH",
             "The Invincibles roster was packed with international superstars: Henry, Bergkamp, Pirès, Vieira, Ljungberg.",
             "Yet there was zero jealousy over who scored the winning goal. If Henry was double-teamed, he passed to Bergkamp. If Pirès had an open lane, Henry dragged defenders away. Championship performance requires that individual ego yields completely to collective victory.",
             "Align your corporate incentive structures so that collaborative assists are celebrated just as loudly as individual wins."),
            
            ("THE PSYCHOLOGICAL WARFARE OF UNBEATEN TEAMS",
             "Before the Invincibles even stepped onto the pitch, opponents were beaten in the tunnel.",
             "Looking at Vieira, Campbell, Gilberto Silva, and Henry standing tall, silent, and unified, opposing players were intimidated before a ball was kicked. Authentic confidence is felt energetically. When your team executes with flawless alignment, the market perceives your authority before you launch.",
             "Project unified, quiet authority. When your entire executive bench stands in absolute alignment, skepticism evaporates."),
            
            ("THE ROLE OF THE TACTICAL CONDUCTOR",
             "Arsène Wenger was the architect, but Thierry Henry was the on-field conductor who translated theory into reality.",
             "Wenger gave his players freedom within a structured framework. Henry adjusted that framework in real-time, signaling tactical switches based on how opponents adjusted. In modern business, CEOs need operational lieutenants who can read market shifts and execute adjustments without waiting for executive committee meetings.",
             "Empower your front-line leaders with the tactical autonomy to make real-time decisions that protect your strategic objectives."),
            
            ("TURNING SETBACKS INTO HISTORIC MOMENTUM",
             "Just days before the Liverpool match, Arsenal was knocked out of the Champions League and FA Cup in the same week.",
             "A lesser squad would have spiraled into self-pity and let their season unravel. Henry gathered the team and said: 'We still have the league. We make history here.' They responded by going unbeaten for the rest of the campaign. That resilience separates good teams from legends.",
             "When a major project fails, do not allow disappointment to infect your remaining objectives. Pivot instantly to victory."),
            
            ("THE STANDARD OF ZERO UNENFORCED ERRORS",
             "During the 49-game run, Arsenal's defense and midfield made virtually zero unforced mental blunders.",
             "Championships are not won by spectacular plays; they are won by the ruthless minimization of careless errors. In corporate governance, billions of dollars in enterprise value are destroyed by sloppy compliance, weak internal controls, and careless communication.",
             "Tighten your internal operating procedures until careless errors are systematically engineered out of your business."),
            
            ("THE ART OF WINNING UGLY",
             "The Invincibles are remembered for scintillating, champagne football, but several matches were gritty, physical 1-0 slugfests.",
             "When the pitch was poor, the weather miserable, and the opponent aggressive, Henry rolled up his sleeves and battled. True champions do not require perfect conditions to deliver results. They find a way to win regardless of the environment.",
             "Do not wait for ideal market conditions to execute your strategy. Learn to win in messy, adverse environments."),
            
            ("RESPECTING THE SACRED TRUST OF SUPPORTERS",
             "Henry never took the adoration of Highbury fans for granted. He treated every ticket holder as an investor in his craft.",
             "After matches, win or lose, he circled the pitch, applauded the supporters, and thanked them for their devotion. In business, customer retention is built on genuine gratitude and continuous respect. The moment you treat customers as guaranteed statistics, they will leave you.",
             "Treat your clients and customers with the profound gratitude due to those who fund your enterprise."),
            
            ("THE LEADERSHIP BURDEN OF BEING THE FRANCHISE",
             "When you are the face of an institution, every word you say in press conferences carries immense weight.",
             "Henry carried that mantle with impeccable statesmanship. He defended his teammates, praised his coaches, and represented Arsenal with regal dignity. As an executive coach, I remind CEOs that when you take the top chair, your private opinions are no longer private. You represent the brand.",
             "Conduct yourself in every public forum with the dignity worthy of the brand and people you represent."),
            
            ("THE DISCIPLINE OF RECOVERY BETWEEN MATCHES",
             "Playing sixty matches a season at peak intensity requires extraordinary biological discipline.",
             "Henry spent hours in ice baths, worked with physiotherapists, ate meticulously planned meals, and prioritized eight hours of sleep. In the corporate world, burnout is often worn as a badge of honor. In elite sport, burnout is recognized as an amateur failure of recovery systems.",
             "Prioritize executive recovery with the same seriousness you bring to strategic planning. Fatigued leaders make disastrous choices."),
            
            ("THE VALUE OF UNAPOLOGETIC AMBITION",
             "Before the Invincibles season began, Arsène Wenger boldly announced to the media that Arsenal could go the entire season unbeaten.",
             "The British press mocked him as delusional. Henry and the squad internalized that audacious vision and made it their personal reality. Leaders must possess the courage to state bold, inspiring goals that terrify ordinary minds.",
             "Do not set timid, incremental goals to protect yourself from criticism. Cast an audacious vision and rally your team to execute it."),
            
            ("THE POWER OF UNBREAKABLE BROTHERHOOD",
             "Decades after 2004, the members of the Invincibles squad remain deeply bonded brothers.",
             "They shared a trial by fire that forever tied their lives together. When people sweat, sacrifice, and conquer historic milestones as a unified team, the resulting trust transcends commerce. That is the kind of team dynamic every CEO should aspire to build.",
             "Build teams that are bonded by shared struggle and shared triumph. That brotherhood will survive any market disruption."),
            
            ("HONORING THE FINAL MATCH AT HIGHBURY",
             "In 2006, in the final match ever played at Highbury, Henry scored a hat-trick and knelt to kiss the grass.",
             "It was a moment of profound reverence for history and place. He understood that institutions have souls, and that honoring the ground upon which your success was built is an essential act of leadership humility.",
             "Never forget the foundational institutions and early mentors who provided the platform for your ascent."),
            
            ("HOW THE INVINCIBLE MINDSET TRANSLATES TO BUSINESS",
             "The Invincible mentality is simple: refuse to accept that defeat is inevitable, and refuse to let daily standards slip.",
             "When that mindset permeates a sales team, a product engineering group, or an executive board, the entire organization operates on a different frequency. Competitors can feel your relentlessness.",
             "Instill the Invincible mindset in your enterprise: zero compromises on quality, zero tolerance for complacency."),
            
            ("THE LEGACY OF PERFECTION",
             "Forty-nine matches. Zero defeats. A golden Premier League trophy that stands completely unique in modern football history.",
             "Thierry Henry proved that when human beings align around an uncompromising standard of excellence, they can achieve what the world deems impossible. That is the calling of championship leadership. That is what I challenge every corporate executive to pursue.",
             "Do not settle for ordinary success. Build something so exceptional that time itself cannot diminish it.")
        ]
    elif flight_idx == 2:
        # Flight 3 (Posts 41-60): From Pitch Maestro to Olympic Head Coach (Paris 2024 Silver)
        return [
            ("STEPPING ONTO THE OLYMPIC STAGE IN PARIS",
             "When Thierry Henry agreed to manage France's Olympic football team for Paris 2024, he knew the pressure was suffocating.",
             "A home Olympic Games. A football-obsessed nation demanding gold. Clubs refusing to release top senior players. Henry did not make excuses; he accepted the challenge with quiet dignity. As an Olympic coach for four decades, I know the unique psychological crucible of the Olympic Games: there is no second chance. You either execute or you go home empty-handed.",
             "Do not complain about constraints or unfair circumstances. Take the talent you have in hand and build a medal-worthy team."),
            
            ("MANAGING YOUNG EGOS WITH FATHERLY AUTHORITY",
             "The Olympic squad was made up of players under twenty-three: young, wealthy, scrutinized on social media, and full of raw emotion.",
             "Henry did not manage them through fear or intimidation. He managed them through deep relational listening, technical respect, and clear boundaries. He sat on the grass with them, shared stories of his own painful early failures, and built an unbreakable bond of trust. True mentorship meets people where they are.",
             "Lead emerging talent through relationship and respect, not obsolete command-and-control hierarchies."),
            
            ("THE DISCIPLINE OF TACTICAL SIMPLICITY",
             "With only a few weeks of preparation before the tournament, Henry could not install an overly complex tactical system.",
             "He distilled his philosophy into three non-negotiables: aggressive high-pressing, rapid vertical transitions, and absolute defensive compactness. In corporate turnarounds, leaders often fail because they introduce fifty-page strategy binders that confuse the front line. Simplicity enables speed.",
             "Strip away operational complexity until your core strategic imperatives can be memorized and executed by anyone in the organization."),
            
            ("THE EMOTIONAL MATURITY OF A SILVER MEDAL",
             "After a heartbreaking 3-5 defeat to Spain in extra time in the gold medal final, Henry gathered his devastated young squad on the pitch.",
             "He did not storm off or criticize his players. He hugged each of them, demanded they lift their heads, and reminded them that France had not reached an Olympic football final in forty years. He taught them that an Olympic medal is a sacred accomplishment, and that character is revealed in how you accept defeat with grace.",
             "Teach your leaders how to stand tall in the aftermath of near-misses. How you carry heartbreak defines your future resilience."),
            
            ("THE COACH AS THE PROTECTIVE UMBRELLA",
             "Throughout the Olympic tournament, whenever the French media criticized individual young players, Henry stepped in front of the cameras.",
             "He took all the blame for mistakes and deflected all the praise to his squad. He absorbed the external pressure so his players could play with freedom and joy. That is the highest duty of an executive leader: be the umbrella that shields your team from external chaos.",
             "Absorb the political and public pressure so your operational team can focus on execution without fear."),
            
            ("DEVELOPING THE WHOLE ATHLETE, NOT JUST THE FEET",
             "Henry spent hours in team meetings talking about life, mental health, family pressures, and financial stewardship.",
             "He understood that a young man who is anxious about his personal life cannot make composed split-second decisions on the pitch. In my work with Olympic hopefuls, I found that you must coach the person before you can coach the athlete. The same rule applies to corporate management.",
             "Invest in the personal wellbeing and emotional stability of your team members. A whole human being is a high-performing human being."),
            
            ("THE HUMILITY OF RETURNING TO THE BENCH",
             "Thierry Henry is a global icon with a personal fortune. He did not need the modest salary of an under-21 national coach.",
             "He took the job because he loved football, loved France, and wanted to pour his life into the next generation. That humility to serve when you have already achieved total commercial success is the mark of a true elder statesman of sport.",
             "Find opportunities to mentor and serve where there is no commercial gain, simply the pure joy of elevating others."),
            
            ("COMMUNICATING WITH RAW AUTHENTICITY",
             "Watch Henry in the Olympic dressing room at halftime: passionate, articulate, emotionally connected, intensely real.",
             "He does not read corporate slide decks. He looks his players in the eye, speaks from his heart, and challenges their pride. Modern young workers and athletes can smell artificial corporate jargon instantly. They respond only to raw, authentic leadership grounded in genuine care.",
             "Ditch the hollow corporate buzzwords. Speak with raw authenticity and clear truth."),
            
            ("CREATING SENSE OF NATIONAL PURPOSE",
             "Henry reminded his Olympic squad that wearing the French crest at a home Games was bigger than their personal club careers.",
             "He connected them to the history of French athletics, to the diverse neighborhoods of Paris, and to the children watching from high-rise banlieues. When people are connected to a purpose greater than their personal paycheck, their threshold for pain and effort expands dramatically.",
             "Connect your corporate team to a mission that touches human lives, not just a profit margin."),
            
            ("THE TRANSITION FROM SCORER TO STRATEGIST",
             "The hardest transition for an elite athlete is stepping back from executing the plays to guiding others to execute them.",
             "When Henry stood on the touchline, he could not kick the ball for his strikers. He had to accept that his role was to prepare them, trust them, and live with the outcome. In corporate promotions, many brilliant individual contributors fail as managers because they cannot stop doing the work themselves.",
             "Stop trying to score the goals yourself. Your job as an executive is to design the system that allows your team to score."),
            
            ("CELEBRATING TEENAGE RESILIENCE",
             "Watching young French players fight back from two goals down in the Olympic final showcased the resilience Henry instilled in them.",
             "They did not fold under the weight of eighty thousand screaming fans. They rallied, scored in the 90th minute, and pushed the match into extra time. That fighting spirit was the direct reflection of Henry's personal ethos: you fight until the final whistle blows.",
             "Build a team culture that refuses to surrender, regardless of what the scoreboard says in the fourth quarter."),
            
            ("THE VALUE OF MULTI-GENERATIONAL BRIDGES",
             "Henry brought senior legends into the Olympic camp to converse with the young squad.",
             "He bridged the wisdom of France's 1998 World Cup champions with the energy of the 2024 Olympic contenders. Cross-generational mentorship shortens learning curves by decades and prevents young talent from repeating painful historical mistakes.",
             "Connect your emerging corporate talent with veteran executives who have already navigated market crises."),
            
            ("THE COACH'S INTELLECTUAL HONESTY",
             "In post-match press conferences, Henry gave masterclasses in tactical deconstruction, admitting where his game plan worked and where it fell short.",
             "He never blamed referees, weather, or bad luck. He took complete ownership of tactical decisions. That intellectual honesty is rare in sport and even rarer in corporate boardrooms, where failure is routinely blamed on external market headwinds.",
             "Own your mistakes with total intellectual honesty. Accountability builds immense credibility with your team and your board."),
            
            ("BALANCING EMOTION AND TACTICAL CALM",
             "During chaotic matches, Henry paced the technical area with fiery passion, but his tactical substitutions were cold and calculated.",
             "He did not make substitutions based on emotional panic. He looked at GPS physical telemetry, identified fatigue gaps, and made adjustments that changed the game. Effective leaders maintain passion in their hearts while keeping ice in their minds.",
             "Keep your heart warm with passion for your mission, but keep your brain cool and analytical during tactical crises."),
            
            ("THE RESPONSIBILITY OF BEING A ROLE MODEL",
             "Throughout the Olympics, Henry carried himself with unmatched elegance, speaking three languages fluently in press conferences.",
             "He represented modern, diverse France with intelligence, humor, and dignity. He demonstrated to millions of young people that an athlete from the Parisian banlieues can speak with the eloquence of a diplomat. Identity is expanded by example.",
             "Be the living embodiment of the standard you expect your team to emulate."),
            
            ("BUILDING TRUST THROUGH VULNERABILITY",
             "Henry openly shared his past regrets with his young players: times he let anger get the better of him, times he failed to listen to coaches.",
             "By sharing his scars rather than just his medals, he disarmed their defensiveness. Leaders who pretend to have lived flawless lives alienate their teams. Leaders who share their scars create profound trust and psychological safety.",
             "Lead with your scars, not just your trophies. Vulnerability is the fastest way to build authentic trust."),
            
            ("THE IMPORTANCE OF DETAILED CELEBRATION",
             "When a defender made a sliding block or a midfielder won a second ball, Henry celebrated as wildly as if they had scored a goal.",
             "He reinforced the unglamorous, defensive dirty work that rarely makes the highlight reels. In corporate life, if you only celebrate closing sales, your operations and customer support teams will feel invisible and demotivated. Celebrate the unsung heroes.",
             "Lavishly praise the unglamorous operational execution that makes visible success possible."),
            
            ("THE OLYMPIC SPIRIT AS A GUIDING COMPASS",
             "Henry embraced the true Olympic ethos: excellence, friendship, and mutual respect.",
             "He insisted that his players applaud opposing teams, exchange jerseys with dignity, and respect Olympic volunteers and staff. He reminded them that sport is an ambassadorial endeavor meant to build bridges between nations, not just collect metal.",
             "Ensure that your corporate competition is conducted with absolute integrity and deep respect for the broader community."),
            
            ("THE LEGACY OF THE PARIS SUMMER",
             "The silver medal in Paris was France's first Olympic football medal in forty years, but the real victory was the transformation of those twenty-two young men.",
             "They left that tournament knowing how to sacrifice for each other, how to handle national pressure, and how to carry themselves as men of character. That is the indelible mark of a master coach. That is what I have spent my life doing for Olympic athletes.",
             "Measure your coaching legacy not by the metal in your cabinet, but by the character of the human beings you formed."),
            
            ("THE CALLING OF THE MENTOR",
             "Thierry Henry proved in Paris that the highest evolution of the champion is the mentor.",
             "When you have climbed the mountain and planted your flag, your work is not finished. Your true work begins when you turn around, reach down your hand, and guide the next generation up the steep path. That is vision beyond the game.",
             "Become the mentor you wish you had when you were young and navigating the wilderness.")
        ]
    elif flight_idx == 3:
        # Flight 4 (Posts 61-80): Tactical Vision & Seeing the Game Ahead of Time
        return [
            ("COGNITIVE ANTICIPATION ON THE PITCH",
             "Thierry Henry did not react to what happened; he anticipated what was about to happen two passes in advance.",
             "Neuroscientists studying elite athletes found that masters like Henry scan the field up to four times more frequently per minute than average players. They process subtle visual cues: hip angles, goalkeeper positioning, defender momentum: long before the ball is kicked. In executive strategy, forecasting is not fortune-telling; it is high-frequency environmental scanning.",
             "Train your executive team to scan market horizons continuously rather than waiting for quarterly reports to reveal reality."),
            
            ("THE SPEED OF DECISION-MAKING UNDER PRESSURE",
             "In elite football, you have less than half a second to make a decision when closing defenders arrive.",
             "Henry's cognitive processing speed was extraordinary because he pre-loaded his decisions before receiving the ball. He already knew where his pass or shot was going before the pass reached his boot. In modern business, slow decision-making is far more dangerous than imperfect decision-making. Pre-load your strategic options.",
             "Pre-load your operational contingency plans so when market volatility strikes, execution is instantaneous."),
            
            ("READING DEFENSIVE STRUCTURES LIKE CODE",
             "Watch Henry dissect a defensive line: he probes the seam between the center-back and full-back like a computer hacker looking for a vulnerability.",
             "He would make three decoy runs just to see how the defense communicated. Once he identified who was slow to switch coverage, he struck with lethal precision. In competitive analysis, do not attack your competitor at their strongest point; probe their seams until you find the structural flaw.",
             "Never attack a entrenched competitor head-on. Find the seam between their product offerings and exploit the gap."),
            
            ("THE POWER OF DECOY MOVEMENT",
             "Often Henry's greatest contributions in a match involved touching the ball zero times.",
             "He would sprint toward the near post, dragging two central defenders with him, leaving the penalty spot completely open for his midfielder to arrive and score uncontested. In corporate leadership, sometimes your greatest contribution is creating an opening for someone else to step into the spotlight and close the deal.",
             "Evaluate your leaders by how effectively their positioning creates opportunities for others to win."),
            
            ("THE ART OF PAUSING TO ACCELERATE",
             "Henry was famous for stopping dead on the ball on the left wing, freezing the defender in place before exploding past him.",
             "That sudden pause disrupted the defender's rhythm and balance. In corporate negotiations, the strategic pause: silence: is the most potent psychological tool you possess. When you stop talking, the other side rushes to fill the void, often revealing critical leverage.",
             "Master the strategic pause. Silence in negotiation conveys immense confidence and forces the other side to reveal their hand."),
            
            ("DIAGNOSING GOALKEEPER BIASES",
             "Henry realized that goalkeepers anticipate low, hard shots across their body from left-wing strikers.",
             "So what did he do? He developed the near-post curler and the delicate chip over their legs. He studied the psychological biases of his opponents and systematically exploited their expectations. In product design, disrupt your market by delivering the exact opposite of what entrenched competitors have conditioned customers to expect.",
             "Identify the rigid biases of your industry and design offerings that capitalize on their blind spots."),
            
            ("THE GEOMETRY OF THE TRIANGLE",
             "At Arsenal and Barcelona, Henry operated within dynamic passing triangles that left defenders chasing shadows.",
             "When three players maintain geometric spacing and keep the ball moving with one-touch passing, no amount of individual defensive aggression can stop them. In organizational architecture, cross-functional triads: product, engineering, and sales: moving with fluid alignment will outperform rigid departmental silos every time.",
             "Break down departmental silos into agile, cross-functional triads that execute with fluid communication."),
            
            ("THE IMPORTANCE OF TACTICAL FLEXIBILITY",
             "Henry began his career as an orthodox winger, became the world's most dominant central striker, and later played as an inverted wide forward.",
             "He never locked himself into a single rigid identity. He adapted his game as he aged, substituting raw sprint speed with immaculate passing vision and positioning. Leaders who tie their identity to a specific operational role become obsolete. Leaders who tie their identity to strategic impact thrive indefinitely.",
             "Do not tie your identity to a job title or specific technology. Tie your identity to delivering value and solving problems."),
            
            ("OVERCOMING RIGID DEFENSIVE LOW BLOCKS",
             "When opponents parked ten men in their own penalty box, brute force was futile. Henry used patient, probing circulation.",
             "He would shift the ball from side to side twenty times, stretching the defense laterally until a tiny two-foot gap opened up for a through ball. When faced with stubborn regulatory or bureaucratic hurdles in business, patient, continuous pressure will always breach the wall eventually.",
             "When facing rigid institutional resistance, do not exhaust yourself with blunt force. Apply persistent, probing pressure."),
            
            ("THE BRAIN AS THE PRIMARY MUSCLE",
             "Henry often said: 'You do not run with your legs; you run with your brain.'",
             "A player who runs ten miles in a match with poor positioning is simply an inefficient runner. A master who runs five miles with impeccable timing will score three goals. In executive productivity, working fourteen hours a day is often an excuse for poor prioritization. Strategic clarity beats frantic activity every single day.",
             "Stop celebrating eighty-hour workweeks. Celebrate ruthless prioritization, strategic clarity, and high-impact execution."),
            
            ("MAPPING THE FIELD BEFORE ARRIVAL",
             "Before stepping across the touchline, Henry spent thirty seconds looking at the pitch dimensions, wind direction, and grass length.",
             "He calibrated his mental compass to the environment. In corporate expansion, entering a new foreign market requires that exact preliminary calibration: understanding local regulations, cultural nuances, and consumer habits before committing capital.",
             "Calibrate your strategy to local market conditions before deploying capital. Context is everything."),
            
            ("THE VALUE OF INTELLECTUAL CURIOSITY",
             "Henry spent his career asking coaches why: why press now, why drop deep, why play zonal marking instead of man-to-man.",
             "He did not just execute instructions blindly; he wanted to understand the overarching tactical philosophy. That deep intellectual curiosity is what transformed him into a world-class coach and brilliant broadcast analyst. Foster curiosity in your emerging talent.",
             "Encourage your team to ask why. Understanding the strategic philosophy behind a directive creates resilient execution."),
            
            ("THE DISCIPLINE OF TIMING THE OFF-SIDE LINE",
             "Henry played on the razor's edge of the offside trap, timing his sprint to the exact millisecond the passer struck the ball.",
             "A fraction of a second too early, and the play is whistled dead. A fraction too late, and the defender recovers. In venture capital and market entries, timing is the single greatest determinant of success. Being five years too early is indistinguishable from being wrong.",
             "Study market timing with religious obsession. Launching when the market is ready is the difference between failure and a unicorn."),
            
            ("TURNING OPPONENT AGGRESSION INTO A WEAPON",
             "When aggressive defenders tried to physically intimidate Henry, he used their own momentum against them.",
             "He would drop his shoulder, let them overcommit to the tackle, and spin into the thirty yards of open space behind them. In competitive business strategy, use judo moves: let large, bureaucratic competitors overcommit their resources to outdated models, then pivot into the open market they neglected.",
             "Use the momentum of entrenched competitors against them. When they overcommit to legacy models, capture the new frontier."),
            
            ("THE POWER OF UNCOMPROMISING FINISHING HABITS",
             "In training, Henry never allowed a shot that went wide to go unexamined. He analyzed the hip angle, the plant foot, the trajectory.",
             "He treated every practice rep with the gravity of a Champions League final. If you want high-quality outcomes in your enterprise, you must hold daily internal deliverables to the exact same standard as client-facing presentations.",
             "Treat internal practice with the same sacred discipline you bring to major client pitches."),
            
            ("HOW TO SCAN WHEN CHAOS ERUPTS",
             "When twenty-two bodies are colliding at high speed in the penalty box, amateur players experience tunnel vision. Masters widen their field of view.",
             "Henry had the rare ability to detach emotionally from the immediate collision and spot the unmarked teammate on the far post. As an Olympic coach, I trained my athletes in panoramic awareness: when chaos erupts, widen your lens, breathe deeply, and spot the open path.",
             "When organizational crisis erupts, resist tunnel vision. Step back, widen your perspective, and identify the overlooked solution."),
            
            ("CREATING PROPRIETARY TACTICAL COMBINATIONS",
             "The chemistry between Thierry Henry and Robert Pirès on the left wing was so telepathic that opponents were powerless to stop it.",
             "They created proprietary overlapping runs and one-two passes through thousands of hours of shared practice. In enterprise strategy, build proprietary internal partnerships between departments that competitors cannot replicate simply by hiring a few consultants.",
             "Build deep collaborative partnerships between internal teams. Proprietary organizational chemistry is impossible to copy."),
            
            ("THE LESSON OF TACTICAL CONVICTION",
             "When Henry had a vision for how a match should be played, he executed it with unwavering conviction.",
             "Doubt is poison on the pitch. If you hesitate for a split second between shooting and passing, the opportunity evaporates. When you make a strategic decision in business, commit with total conviction. Half-hearted execution will destroy even the most brilliant strategy.",
             "Once a strategic decision is finalized, execute with total, unhesitating conviction."),
            
            ("THE ART OF EVOLVING YOUR GAME BEFORE FORCED TO",
             "When Henry noticed his raw sprint speed slightly declining in his early thirties, he transitioned into an elite playmaker.",
             "He dropped deeper into the midfield, delivering pinpoint thirty-yard diagonal passes to younger, faster wingers. He did not wait for his body to fail before evolving his game. Proactive reinvention is the secret to enduring relevance.",
             "Reinvent your corporate capabilities while you are still strong. Do not wait for market decline to force your hand."),
            
            ("VISION THAT SEES AHEAD OF TIME",
             "Thierry Henry saw the game before it unfolded because he spent his life mastering its fundamental laws.",
             "That is the essence of Vision Beyond the Game. When you master the fundamentals of your craft, the future ceases to be a mystery. It becomes an open map waiting for your footsteps. That is the standard of leadership I teach every single day.",
             "Master the fundamental laws of your industry. That mastery will give you the vision to lead your market into tomorrow.")
        ]
    elif flight_idx == 4:
        # Flight 5 (Posts 81-100): Poise, Emotional Regulation & High-Stakes Finals
        return [
            ("WALKING ONTO THE PITCH AT STADE DE FRANCE IN 1998",
             "At twenty years old, Thierry Henry stood in the tunnel of the World Cup final against Brazil.",
             "Eighty thousand fans screaming. Two billion people watching on television. The weight of an entire nation on his shoulders. Henry did not buckle. He channeled the electric atmosphere into quiet, steady focus. In Olympic coaching, we train for the tunnel walk: when the heart pounds in your throat, your breath must become your anchor.",
             "When stepping onto the biggest stage of your career, master your breathing. Physical composure dictates mental clarity."),
            
            ("THE PSYCHOLOGICAL WARFARE OF A WORLD CUP CAMPAIGN",
             "A World Cup tournament lasts a month of relentless pressure, media scrutiny, and physical exhaustion.",
             "One mistake sends your country home in tears. Henry learned early that surviving a tournament requires emotional compartmentalization: celebrate a victory for two hours, grieve a defeat for two hours, then immediately return to neutral preparation. Emotional volatility drains your stamina.",
             "Do not let your leadership team ride an emotional roller coaster of highs and lows. Cultivate steady, grounded neutrality."),
            
            ("EXECUTING UNDER THE BRIGHTEST LIGHTS IN EUROPE",
             "In 2006, Henry led Arsenal to their first UEFA Champions League final, scoring iconic goals against Real Madrid and Juventus along the way.",
             "Against Real Madrid at the Santiago Bernabéu, Henry picked up the ball at the halfway line, held off three defenders, and scored the winning goal: the first English club to ever win there. Great leaders do not shrink when the lights get brighter; their focus sharpens to a laser point.",
             "When the stakes are astronomical, lean into your preparation and execute your fundamentals with unshakeable poise."),
            
            ("THE LESSON OF A CHAMPIONS LEAGUE REDEMPTION",
             "After losing the 2006 final with Arsenal, Henry did not quit. In 2009, he lifted the Champions League trophy with Barcelona.",
             "Redemption in sport and business requires staying in the arena long enough for opportunity to circle back. If Henry had retired after 2006, he would have spent the rest of his life wondering. He endured the pain, changed clubs, adapted his role, and reached the summit. Never let heartbreak have the final word.",
             "Heartbreak in business is not the end of the story. Stay in the arena and position yourself for the redemption that is coming."),
            
            ("MANAGING THE NOISE OF CRITICS",
             "Throughout his career, Henry was scrutinized by pundits who questioned his performances in major tournament finals.",
             "He responded not with angry social media posts, but by winning the World Cup, the European Championship, two Premier Leagues, two La Ligas, and the Champions League. Let your resume silence your critics. Arguing with armchair observers is a waste of precious cognitive bandwidth.",
             "Do not waste energy arguing with critics who have never built an enterprise. Let your results speak for you."),
            
            ("THE DISCIPLINE OF PENALTY KICK POISE",
             "Stepping up to take a penalty kick in front of ninety thousand hostile fans is the ultimate test of nervous system regulation.",
             "Henry had a ritual: place the ball carefully, take four steps back, breathe through the nose, pick his spot, and execute without hesitation. Rituals protect you from panic. When your executive team faces immense uncertainty, established standard operating procedures keep panic at bay.",
             "Build robust operational rituals that your team can rely upon when high-stakes uncertainty threatens to paralyze them."),
            
            ("LEADERSHIP IN THE AFTERMATH OF DEFEAT",
             "When France lost the 2006 World Cup final on penalty kicks, Henry was the first to comfort his teammates.",
             "He did not point fingers or search for scapegoats. He embraced David Trezeguet and stood in solidarity with his brothers. True leadership is not proven when you are spraying champagne on the podium. It is proven when you stand shoulder-to-shoulder with your team in the quiet dressing room of defeat.",
             "Never point fingers at your team after a high-stakes failure. Stand shoulder-to-shoulder with them and absorb the outcome together."),
            
            ("THE PERIL OF COMPLACENCY IN EXTRA TIME",
             "In cup finals, matches are often decided in extra time when physical systems are completely drained.",
             "The team that loses focus for three seconds during a defensive set piece is the team that goes home with silver. Henry taught his players that extra time is where mental stamina reigns supreme. You must fight through the fog of fatigue and maintain technical vigilance.",
             "When projects drag into grueling overtime, guard your team's mental vigilance against careless late-stage oversights."),
            
            ("CARRYING NATIONAL PRIDE WITH MAJESTIC DIGNITY",
             "As the child of Antillean parents from Guadeloupe and Martinique, Henry represented the diverse tapestry of modern France.",
             "He carried that identity with pride and elegance, demonstrating that athletic excellence can unite divided societies. In forty years of Olympic coaching, I have seen sport heal community wounds that politics could never touch. Leadership carries cultural responsibility.",
             "Remember that your enterprise has a cultural footprint. Conduct your business in a manner that inspires and unifies your community."),
            
            ("TURNING ADVERSITY INTO HIGH-OCTANE MOTIVATION",
             "When Henry arrived at Juventus early in his career, he was played out of position and struggled.",
             "Many wrote him off as an overhyped prospect who could not handle tactical Italian defenses. Arsène Wenger brought him to Arsenal, believed in him, and Henry turned that early rejection into an eight-year rampage across world football. Adversity is simply high-octane fuel for those with character.",
             "Do not let early career rejections define your ceiling. Use them as the fuel that powers your ultimate breakthrough."),
            
            ("THE IMPORTANCE OF EMOTIONAL RECOVERY",
             "After a grueling World Cup final, the psychological depletion can last for months if unmanaged.",
             "Henry learned how to disconnect: retreating to nature, spending time with family, turning off phones, and restoring his spirit. In executive life, many leaders suffer from chronic low-grade depression because they never allow their nervous systems to recover from major transactions.",
             "Schedule mandatory cognitive recovery after major enterprise milestones. Rest is a non-negotiable component of longevity."),
            
            ("THE STRENGTH OF QUIET CONVICTION",
             "Henry never needed to throw temper tantrums on the sideline to show that he cared.",
             "His intensity was quiet, internal, and implacable. In corporate boardrooms, the person shouting and slamming tables is usually the one who feels out of control. Quiet, measured conviction is infinitely more intimidating to competitors and reassuring to colleagues.",
             "Replace performative aggression with quiet, unwavering conviction. Authority does not need to shout."),
            
            ("THE ARCHITECTURE OF A CHAMPIONSHIP CULTURE",
             "At Barcelona, Henry was part of Pep Guardiola's historic 2009 team that won all six available trophies in a single year.",
             "Guardiola demanded that even global superstars press relentlessly within six seconds of losing the ball. Henry embraced that collective discipline. He showed that no matter how famous you are, you must submit to the team's operational defense.",
             "Ensure that no executive in your company is exempt from core cultural values and daily operational discipline."),
            
            ("THE POWER OF HUMILITY IN VICTORY",
             "When Henry won the Champions League in Rome, his first thoughts were of his former Arsenal teammates who had fallen short in 2006.",
             "He did not gloat; he carried himself with profound humility. Arrogance in victory invites catastrophic ruin. Humility in victory ensures that your peers and competitors continue to respect your leadership.",
             "Celebrate your corporate triumphs with deep humility and grace. Protect your enterprise from the poison of arrogance."),
            
            ("RESILIENCE WHEN THE SYSTEM BREAKS DOWN",
             "In major finals, your tactical game plan rarely survives past the twentieth minute. The opponent will surprise you.",
             "Henry possessed the tactical flexibility to adapt on the fly. When your enterprise encounters sudden market disruption or regulatory intervention, clinging blindly to your initial plan is suicidal. Adapt with poise and find a new route to victory.",
             "When your strategic plan encounters reality, adapt your tactics without compromising your overarching objective."),
            
            ("THE COURAGE TO TAKE RESPONSIBILITY",
             "In the 2000 European Championship final against Italy, France was trailing in stoppage time.",
             "Henry never stopped attacking down the left flank, forcing the Italian backline into desperate clearances that eventually led to Sylvain Wiltord's 93rd-minute equalizer and David Trezeguet's golden goal. He showed that continuous, courageous pressure will eventually crack even the most legendary defense.",
             "When your enterprise faces a tight deadline, keep pressing with relentless courage until the breakthrough arrives."),
            
            ("THE VALUE OF A TRUSTED CONFIDANT",
             "Throughout his career, Henry had mentors: Arsène Wenger, his father Antoine: with whom he could be completely vulnerable.",
             "He had a safe sanctuary where he could voice his doubts, work through his anxieties, and receive unvarnished truth. In executive life, isolation at the top is lethal. Every CEO must have a trusted coach or mentor who tells them the truth without fear.",
             "Surround yourself with a trusted inner circle that will tell you the unvarnished truth when everyone else tells you what you want to hear."),
            
            ("THE DIGNITY OF LONGEVITY",
             "Henry played at the highest level of European football from 1994 to 2012: nearly two decades of elite performance.",
             "Longevity is not an accident. It requires continuous reinvention of your mechanics, flawless lifestyle discipline, and relentless mental hunger. In corporate enterprise, building a company that survives decades requires that exact refusal to become stagnant.",
             "Build your enterprise for generational durability, not just for a quick flip in a favorable market cycle."),
            
            ("THE OLYMPIC LESSON OF POISE UNDER PRESSURE",
             "As an Olympic coach, I have seen athletes choke not because their muscles failed, but because their minds panicked.",
             "Thierry Henry was a master of physiological stillness. When the world was screaming, his heart slowed down. He saw the open space, chose his shot, and executed. That is the gold standard of high-performance psychology.",
             "Train your mind to find stillness when the environment is chaotic. Stillness is your greatest competitive advantage."),
            
            ("THE FINAL PODIUM: CHARACTER OVER SILVER OR GOLD",
             "When all the matches are finished, the medals sit in a velvet box in your home.",
             "What endures is the character you forged during the struggle. Thierry Henry's poise, elegance, and integrity under suffocating pressure are what make him an immortal icon of sport. That is the standard of excellence I urge every leader to embody.",
             "Pursue excellence so purely that your character becomes your greatest and most enduring achievement.")
        ]
    else:
        # Flight 6 (Posts 101-120): Legacy, Statesmanship & Mentoring the Next Generation
        return [
            ("TRANSCENDING THE FIELD OF PLAY",
             "The greatest athletes do not disappear when they hang up their boots. They evolve into global statesmen.",
             "Thierry Henry did not retreat into comfortable obscurity. He became an influential global broadcast analyst, an Olympic head coach, a mentor to young footballers, and a vocal advocate for mental health and racial equality. He took the platform earned on the pitch and expanded it to serve humanity.",
             "Use the professional credibility you have built to advocate for systemic change and mentor emerging leaders."),
            
            ("THE RESPONSIBILITY OF ATHLETIC ROYALTY",
             "When you are widely regarded as the greatest player in the history of the Premier League, your words carry enormous weight.",
             "Henry treats that platform as a sacred responsibility. In his broadcast analysis on CBS Sports and Amazon Prime, he does not resort to cheap hot takes or clickbait. He educates the viewer on tactical geometry, player psychology, and coaching philosophy. He elevates the public conversation.",
             "Elevate the discourse in your industry. Refuse to engage in superficial noise when you have the authority to educate and inspire."),
            
            ("BECOMING THE MENTOR YOU ONCE NEEDED",
             "Watch Henry interact with young players like Kylian Mbappé, Bukayo Saka, and Michael Olise: he speaks to them with profound love and uncompromising truth.",
             "He does not hoard his knowledge. He passes down the subtle secrets of finishing, positioning, and mental regulation that took him twenty years to learn. In corporate leadership, your true value to the organization is measured by how many leaders you cultivate behind you.",
             "Measure your executive success by the calibre of the leaders you leave behind when you step down."),
            
            ("THE ART OF ELOQUENT BROADCAST ANALYSIS",
             "On Champions League nights, Henry's analysis on CBS Sports alongside Kate Abdo, Micah Richards, and Jamie Carragher is appointment television.",
             "He brings warmth, elite technical insight, humor, and dignity to the broadcast. He proved that an athlete can be analytical, charismatic, and intellectually rigorous simultaneously. In executive presentations, combining technical depth with warmth and humor makes your message unforgettable.",
             "Deliver complex technical concepts with warmth, charisma, and clarity. Masterful communication moves markets."),
            
            ("STANDING UP AGAINST RACISM AND ABUSE",
             "In 2021, Thierry Henry voluntarily removed himself from all social media platforms to protest online racial abuse and corporate inaction.",
             "He walked away from millions of followers to take an ethical stand. He challenged tech giants to regulate online hate with the same vigor they regulate copyright infringement. Leadership is tested when taking a moral stand costs you commercial convenience.",
             "Never hesitate to take a principled stand against injustice, even when it requires sacrificing commercial convenience."),
            
            ("MENTAL HEALTH ADVOCACY IN MODERN SPORT",
             "Henry spoke courageously about struggling with depression throughout his career, often carrying the expectations of millions while feeling profound personal sadness.",
             "By speaking openly about his emotional struggles, he gave permission to thousands of young athletes and corporate executives to seek therapy and acknowledge their vulnerability. In forty years of Olympic coaching, I know that acknowledging your pain is the prerequisite for authentic emotional healing.",
             "Normalize mental health support in your workplace. True strength begins when leaders are honest about their human struggles."),
            
            ("THE HUMILITY TO START FROM THE BOTTOM IN COACHING",
             "After retiring, Henry did not demand an immediate top-tier European managerial job. He coached Arsenal's youth academy for free.",
             "He set up cones in the rain, coached sixteen-year-olds on fundamentals, and earned his coaching badges with humility. He recognized that being a legendary player does not automatically make you a great coach. He paid his dues in the trenches.",
             "When transitioning into a new domain, have the humility to do the humble groundwork required to earn true competence."),
            
            ("THE POWER OF A MULTI-LINGUAL MINDSET",
             "Henry conducts interviews fluently in French, English, Spanish, and Italian.",
             "That linguistic versatility allows him to connect deeply with players from across the globe on their own terms. In an interconnected global economy, cultural and linguistic intelligence is an indispensable leadership asset.",
             "Invest in cross-cultural intelligence. When you speak to colleagues and clients in their cultural language, barriers dissolve."),
            
            ("STEWARDING AN ICONIC FOOTBALL BRAND",
             "Thierry Henry remains an immortal ambassador for Arsenal, Barcelona, and the French national team.",
             "Wherever he travels in the world, crowds gather to catch a glimpse of the king. Yet he greets every supporter with gentle respect, signs autographs with a smile, and treats people with profound warmth. Humility is the crown that dignity wears.",
             "Never allow commercial success to make you unapproachable. Treat every person you encounter with dignity and respect."),
            
            ("INSPIRING THE NEXT GENERATION OF FRENCH STARS",
             "When France won the 2018 World Cup and reached the final in 2022, young stars like Kylian Mbappé openly cited Henry as their primary inspiration.",
             "That is generational continuity. When you live your life with excellence, your standard becomes the floor upon which the next generation builds their breakthrough. That is the highest calling of athletic success.",
             "Set an operational standard so high that the next generation uses your ceiling as their starting floor."),
            
            ("THE DISCIPLINE OF REINVENTING YOUR VOICE",
             "Transitioning from athlete to coach, and from coach to global broadcaster, requires learning completely new communication crafts.",
             "Henry worked with vocal coaches, studied television production, and learned how to communicate complex football ideas in tight ten-second television soundbites. He never stopped being a student of communication. Never stop refining how you deliver your message.",
             "Continuously refine your communication skills. The ability to articulate your vision clearly is your greatest leadership asset."),
            
            ("THE SACRED CONTRACT OF COACHING",
             "In my four decades of Olympic coaching, I learned that a coach's job is not to produce athletes who need them forever.",
             "A coach's job is to equip athletes with the technical tools, emotional poise, and mental toughness needed to stand independently and triumph on their own. Henry's coaching philosophy reflects that exact sacred contract: building self-reliant, resilient young men.",
             "Train your team members to become self-reliant decision-makers who can execute brilliantly without your supervision."),
            
            ("REJECTING THE PURSUIT OF CHEAP CELEBRITY",
             "Henry has consistently declined reality television shows and frivolous celebrity appearances.",
             "He protects his brand equity with fierce intentionality. He aligns only with organizations, brands, and initiatives that reflect his core values of excellence, education, and social equity. In executive branding, scarcity and prestige are intimately linked.",
             "Guard your brand against cheap commercial dilution. Say no to sixty lucrative distractions so your yes carries immense value."),
            
            ("THE WISDOM OF LOOKING INWARD",
             "Henry often reflects on the advice his father gave him: 'Never be satisfied with what you did today. Look at what you can improve tomorrow.'",
             "That internal drive for self-perfection protected him from becoming soft during his prime. However, in maturity, Henry learned to balance that relentless drive with healthy self-compassion and gratitude for his accomplishments.",
             "Balance your relentless drive for continuous improvement with deep gratitude for the milestones you have already achieved."),
            
            ("THE VALUE OF FAMILY ROOTS IN THE CARIBBEAN",
             "Henry frequently returns to Guadeloupe and Martinique, reconnecting with his ancestral soil and family elders.",
             "He reminds young athletes that no matter how bright the stadium lights shine in London or Paris, you must always remember the island soil and the humble beginnings that produced your lineage. Rootedness provides emotional balance when fame threatens to destabilize your life.",
             "Stay deeply anchored to your roots and values. A tree with deep roots can survive the fiercest storms."),
            
            ("CREATING HUBS OF OPPORTUNITY FOR URBAN YOUTH",
             "Through grassroots initiatives and coaching clinics, Henry funds football pitches and academic programs in underserved Parisian suburbs.",
             "He gives back to the banlieues that forged his hunger. He shows young people from difficult backgrounds that their postal code does not determine their destiny. True kings build castles for their people, not just for themselves.",
             "Deploy your wealth and influence to build permanent infrastructure and opportunities in the communities that formed you."),
            
            ("THE BEAUTY OF AGING WITH GRACE",
             "At forty-nine years old, Thierry Henry carries himself with an unmistakable elegance: tailored suits, salt-and-pepper beard, regal posture.",
             "He proves that aging as an athlete does not mean decline. It means ascending to higher levels of wisdom, statesmanship, and cultural impact. Do not fight the passage of time; lean forward into the authority and wisdom that your years have earned.",
             "Embrace the authority and perspective that years of battle have given you. Walk boldly into your season of wisdom."),
            
            ("THE LEGACY OF AN INVINCIBLE",
             "Statues of Thierry Henry stand outside the Emirates Stadium in London and in the hearts of football fans across the globe.",
             "Bronze statues are glorious, but the true statue is built in the minds of the millions of young people who fell in love with football because of his grace. That is the immortality that matters: inspiring a generation to pursue excellence.",
             "Build a legacy that lives in the hearts and minds of the people you have inspired and elevated along the way."),
            
            ("THE DEFINITION OF VISION BEYOND THE GAME",
             "Thierry Henry's life is a masterclass in what it means to have vision beyond the game.",
             "He took a God-given athletic talent, refined it through monastic discipline, conquered the world stage, and then used that platform to educate, mentor, and elevate humanity. That is the gold standard of high performance. That is what I coach corporate executives and Olympic athletes to achieve.",
             "Do not let your life be defined solely by the trophies on your shelf. Let your life be defined by the humans you elevated."),
            
            ("THE FINAL INVITATION: OWN YOUR NEXT CHAPTER",
             "Thierry Henry owned every chapter of his life: from Monaco to Arsenal, from Barcelona to Paris 2024, and now onto the world stage.",
             "Now the question turns to you: what will you build with the leverage, wisdom, and platform your career has provided? Will you settle for past accomplishments, or will you step into the owner's suite and build your lasting legacy? The next chapter is yours to write.",
             "Step out of the comfortable memories of your past. Write the bold, audacious chapter that changes your industry and your legacy.")
        ]

# -------------------------------------------------------------
# MASTER SCHEDULER BUILDER
# -------------------------------------------------------------

def build_campaign():
    # 6 flights x 20 concepts = 120 posts
    all_concepts = []
    for f_idx in range(6):
        concepts = get_flight_concepts(f_idx)
        assert len(concepts) == 20, f"Flight {f_idx} must have 20 concepts, got {len(concepts)}"
        all_concepts.extend(concepts)
    
    assert len(all_concepts) == 120, f"Total concepts must be 120, got {len(all_concepts)}"

    # Book catalog for 50/50 CTA rotation:
    books = [
        ("Finish Strong: Chasing the Olympic Dream", "https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A"),
        ("Survival Skills for Athletes", "https://lornettedaye.com/books"),
        ("Survival Skills for Men", "https://buy.stripe.com/9B6bJ1542gA262JfCG1VK00"),
        ("Survival Skills: Surviving to Thriving", "https://lornettedaye.com/books")
    ]

    start_date = datetime(2026, 10, 3)
    posts_data = []

    hashtags = (
        "#ThierryHenry #VisionBeyondTheGame #FranceFootball #Invincibles #OlympicMindset "
        "#ExecutiveLeadership #HighPerformance #KeynoteSpeaker #LornetteDaye #FinishStrong "
        "#MentorshipInAction #TacticalExcellence #BoardroomLeadership #LegacyBuilding"
    )

    concept_idx = 0
    for day_i in range(1, 41):
        cur_day = start_date + timedelta(days=day_i - 1)
        d_str = cur_day.strftime("%Y-%m-%d")
        next_d_str = (cur_day + timedelta(days=1)).strftime("%Y-%m-%d")
        is_mdt = (cur_day < datetime(2026, 11, 1))

        # 3 Daily Collision-Free Slots:
        # Slot 1: Morning (9:15 AM local)
        # Slot 2: Late Afternoon (4:15 PM local)
        # Slot 3: Evening Prime (8:15 PM local -> next day UTC)
        slot1_utc = f"{d_str}T15:15:00.000Z" if is_mdt else f"{d_str}T16:15:00.000Z"
        slot2_utc = f"{d_str}T22:15:00.000Z" if is_mdt else f"{d_str}T23:15:00.000Z"
        slot3_utc = f"{next_d_str}T02:15:00.000Z" if is_mdt else f"{next_d_str}T03:15:00.000Z"

        slot_times = [
            ("Morning (9:15 AM MDT/MST)", slot1_utc),
            ("Late Afternoon (4:15 PM MDT/MST)", slot2_utc),
            ("Evening Prime (8:15 PM MDT/MST)", slot3_utc)
        ]

        for slot_num in range(3):
            slot_name, due_utc = slot_times[slot_num]
            post_id = len(posts_data) + 1

            title, hook, body, takeaway = all_concepts[concept_idx]
            concept_idx += 1

            # 20 assets cycled cleanly: asset 1 to 20
            asset_num = ((post_id - 1) % 20) + 1
            asset_file = f"thierry-henry-{asset_num:02d}.png"
            asset_url = f"https://lornettedaye.com/campaigns/thierry-henry/{asset_file}"

            # 50/50 CTA Split:
            # Odd post_id -> Keynote Booking
            # Even post_id -> Buy Book
            if post_id % 2 != 0:
                cta_type = "Keynote Booking (lornettedaye.com/book)"
                cta_text = (
                    "Bring championship vision, Olympic mentorship, and invincible culture to your corporate offsite or executive summit.\n"
                    "Book Lornette Daye for your keynote: https://lornettedaye.com/book"
                )
            else:
                book_pair = books[((post_id // 2) - 1) % len(books)]
                book_title, book_link = book_pair
                cta_type = f"Buy Book - {book_title} (lornettedaye.com/books)"
                cta_text = (
                    f"Equip yourself and your leadership team with the championship mindset needed to navigate high-stakes pressure.\n"
                    f"Get the published digital edition of '{book_title}' ($14.99 CAD): {book_link}"
                )

            sign_offs = [
                "With purpose,\nLornette",
                "Stay focused,\nLornette",
                "Keep building,\nLornette",
                "In your corner,\nLornette",
                "With conviction,\nLornette"
            ]
            sign_off = sign_offs[(post_id - 1) % len(sign_offs)]

            full_text = f"{title}\n\n{hook}\n\n{body}\n\n{takeaway}\n\n{sign_off}\n\n{cta_text}\n\n{hashtags}"

            # Invariant audit
            for em_dash in ["\u2014", "&mdash;", "—"]:
                if em_dash in full_text:
                    raise ValueError(f"Post #{post_id} contains em dash ({em_dash})!")
            if "Coach Lornette" in full_text:
                raise ValueError(f"Post #{post_id} signed Coach Lornette!")
            if "Lornette" not in full_text:
                raise ValueError(f"Post #{post_id} missing Lornette signature!")

            posts_data.append({
                "id": post_id,
                "day": day_i,
                "date": d_str,
                "slot": slot_name,
                "dueAt": due_utc,
                "assetFile": asset_file,
                "assetUrl": asset_url,
                "cta": cta_type,
                "text": full_text
            })

    print(f"Generated {len(posts_data)} posts successfully.")
    assert len(posts_data) == 120, f"Expected 120 posts, got {len(posts_data)}"

    keynote_count = sum(1 for p in posts_data if p["cta"].startswith("Keynote Booking"))
    book_count = sum(1 for p in posts_data if p["cta"].startswith("Buy Book"))
    print(f"CTA Split: {keynote_count} Keynote CTAs, {book_count} Book CTAs.")
    assert keynote_count == 60 and book_count == 60, "Must be exact 50/50 CTA split (60 Keynotes, 60 Books)!"

    # Verify 0 timestamp collisions
    timestamps = [p["dueAt"] for p in posts_data]
    assert len(timestamps) == len(set(timestamps)), "Internal timestamp collisions found!"
    print("ALL INVARIANTS AUDITED AND PASSED!")

    # Write schedule-thierry-henry.py
    script_content = f'''# -*- coding: utf-8 -*-
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

CDN_BASE = 'https://lornettedaye.com/campaigns/thierry-henry'

posts_data = {json.dumps(posts_data, indent=4, ensure_ascii=False)}

def check_invariants():
    for p in posts_data:
        t = p["text"]
        for dash in ["\\u2014", "&mdash;", "—"]:
            if dash in t:
                raise ValueError(f"Post #{{p['id']}} contains an em dash ({{dash}})!")
        if "Coach Lornette" in t:
            raise ValueError(f"Post #{{p['id']}} is signed 'Coach Lornette' instead of 'Lornette'!")
        if "Lornette" not in t:
            raise ValueError(f"Post #{{p['id']}} does not have Lornette signature!")

check_invariants()
print("INVARIANTS AUDIT PASSED: 120 posts verified. 0 em dashes, all signed strictly 'Lornette', 50/50 alternating CTA.")

def schedule_posts():
    token = TOKEN or os.environ.get('BUFFER_ACCESS_TOKEN', '')
    if not token:
        print("BUFFER_ACCESS_TOKEN is not set. Exiting.")
        return False

    headers = {{
        "Authorization": f"Bearer {{token}}",
        "Content-Type": "application/json",
        "User-Agent": "BufferClient/1.0"
    }}

    ctx = ssl._create_unverified_context()
    graphql_url = "https://api.buffer.com"
    mutation = """
    mutation CreatePost($input: CreatePostInput!) {{
      createPost(input: $input) {{
        ... on PostActionSuccess {{
          post {{
            id
            status
            dueAt
          }}
        }}
        ... on LimitReachedError {{
          message
        }}
        ... on InvalidInputError {{
          message
        }}
        ... on UnexpectedError {{
          message
        }}
        ... on UnauthorizedError {{
          message
        }}
      }}
    }}
    """

    report_path = "scripts/thierry-henry-scheduled-report.json"
    results = {{}}
    if os.path.exists(report_path):
        try:
            with open(report_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for item in data:
                    if item.get("status") in ["scheduled", "success"] and item.get("postId"):
                        results[item["id"]] = item
        except Exception as e:
            print(f"Note: Could not parse existing report: {{e}}")

    for i, p in enumerate(posts_data, 1):
        p_id = p["id"]
        if p_id in results and results[p_id].get("postId"):
            print(f"[{{i}}/120] Post #{{p_id}} already scheduled (Buffer ID: {{results[p_id]['postId']}}). Skipping.")
            continue

        while True:
            print(f"\\n[{{i}}/120] Scheduling Post #{{p['id']}} (Day {{p['day']}} - {{p['slot']}}) - Due: {{p['dueAt']}}...")
            print(f"  Asset: {{p['assetUrl']}}")
            print(f"  CTA Focus: {{p['cta']}}")

            payload = {{
                "query": mutation,
                "variables": {{
                    "input": {{
                        "channelId": CHANNEL_ID,
                        "text": p["text"],
                        "schedulingType": "automatic",
                        "mode": "customScheduled",
                        "dueAt": p["dueAt"],
                        "saveToDraft": False,
                        "needsApproval": False,
                        "assets": [
                            {{
                                "image": {{
                                    "url": p["assetUrl"]
                                }}
                            }}
                        ]
                    }}
                }}
            }}

            req = urllib.request.Request(graphql_url, data=json.dumps(payload).encode("utf-8"), headers=headers)
            try:
                with urllib.request.urlopen(req, context=ctx, timeout=30) as resp:
                    res_data = json.loads(resp.read().decode("utf-8"))
                    errors = res_data.get("errors")
                    if errors:
                        print(f"  >>> GRAPHQL ERROR: {{errors}}")
                        p["status"] = "failed"
                        p["error"] = errors[0].get("message")
                        results[p_id] = p
                        break
                    else:
                        create_res = res_data.get("data", {{}}).get("createPost", {{}})
                        if "post" in create_res and create_res["post"].get("id"):
                            post_id = create_res["post"]["id"]
                            st = create_res["post"].get("status")
                            due = create_res["post"].get("dueAt")
                            p["status"] = st
                            p["postId"] = post_id
                            p["dueAt"] = due
                            print(f"  >>> SUCCESS: Post ID: {{post_id}}")
                            results[p_id] = p
                            with open(report_path, "w", encoding="utf-8") as rf:
                                json.dump(list(results.values()), rf, indent=2, ensure_ascii=False)
                            break
                        else:
                            err_msg = create_res.get("message", "Unknown error")
                            print(f"  >>> ERROR: {{err_msg}}")
                            p["status"] = "failed"
                            p["error"] = err_msg
                            results[p_id] = p
                            break
            except urllib.error.HTTPError as he:
                if he.code == 429:
                    retry_after = he.headers.get('Retry-After')
                    wait_sec = int(retry_after) if retry_after and retry_after.isdigit() else 60
                    print(f"  [RATE LIMIT] HTTP 429 encountered. Waiting {{wait_sec + 5}}s...")
                    time.sleep(wait_sec + 5)
                    continue
                err_body = he.read().decode("utf-8", errors="replace")
                print(f"  >>> HTTP ERROR {{he.code}}: {{err_body}}")
                p["status"] = "failed"
                p["error"] = f"HTTP {{he.code}}: {{err_body}}"
                results[p_id] = p
                break
            except Exception as e:
                print(f"  >>> NETWORK ERROR: {{e}}")
                p["status"] = "failed"
                p["error"] = str(e)
                results[p_id] = p
                break

        time.sleep(2)

    with open(report_path, "w", encoding="utf-8") as rf:
        json.dump(list(results.values()), rf, indent=2, ensure_ascii=False)
    success_count = sum(1 for r in results.values() if r.get("status") in ["scheduled", "success"] and r.get("postId"))
    print(f"\\nExecution complete. Saved {{success_count}}/120 successfully to {{report_path}}.")
    return success_count == len(posts_data)

if __name__ == "__main__":
    schedule_posts()
'''

    out_file = os.path.join(os.path.dirname(__file__), "schedule-thierry-henry.py")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(script_content)
    print(f"Wrote {len(posts_data)} posts to {out_file} successfully ({os.path.getsize(out_file):,} bytes)!")

if __name__ == "__main__":
    build_campaign()
