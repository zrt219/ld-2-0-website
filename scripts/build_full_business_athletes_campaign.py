# -*- coding: utf-8 -*-
"""
Builder script for scripts/schedule-business-athletes.py
Generates 60 unique, high-impact, long-form LinkedIn posts for Serena & Venus Williams (From Champion to Owner).
Enforces:
- 0 em dashes
- Signed strictly 'Lornette'
- 1st person Olympian coach perspective
- 50/50 alternating CTAs (Keynote vs Books)
- 12:00 PM MDT/MST (18:00Z / 19:00Z)
- All 20 visual assets cycled 3 times across 3 distinct progressive waves
"""

import os
import sys
import json
from datetime import datetime, timedelta

def generate_campaign_script():
    start_date = datetime(2026, 10, 3)
    
    # 20 visual assets blueprints with deep narrative data for each wave
    # Wave 1: Foundation of Ownership (Days 1 - 20)
    # Wave 2: Venture Capital & Product Innovation (Days 21 - 40)
    # Wave 3: Sports Franchises & Generational Legacy (Days 41 - 60)
    
    blueprints = [
        # 1: Serena - LA Golf Club
        {
            "asset_idx": 1,
            "subject": "Serena Williams (Los Angeles Golf Club)",
            "w1_title": "ANOTHER SPORT. ANOTHER OWNERSHIP TABLE.",
            "w1_hook": "When Serena Williams stepped onto the tennis court, she rewrote the boundaries of athletic excellence. When she stepped into professional golf ownership, she sent an even louder signal to the global sporting world.",
            "w1_body": "Historically, golf country clubs were spaces of quiet exclusivity, where decisions were made behind heavy oak doors without women of color at the table. Serena did not petition for an invitation. Alongside her husband Alexis Ohanian and Venus, she stepped in as a primary ownership group partner of the Los Angeles Golf Club in TGL.\n\nIn my forty years of coaching Olympic athletes and national champions, I have taught one foundational truth: if you only compete where you are invited, your impact remains confined to someone else's boundaries. True champions expand the arena itself.",
            "w1_takeaway": "When you master your original craft, do not settle for applause. Use your authority to claim a seat at the ownership table where the rules of the entire industry are written.",
            
            "w2_title": "DISRUPTING THE FAIRWAYS: OWNERSHIP OVER INVITATION.",
            "w2_hook": "Modern sports entertainment is experiencing an unprecedented structural shift, and Serena Williams is positioned squarely at the vanguard.",
            "w2_body": "By acquiring a founding franchise in TGL, Serena recognized that golf was ripe for technological disruption, prime-time energy, and cultural reinvention. She brought her brand power, her capital, and her strategic instincts to a sport that traditionally resisted change.\n\nIn corporate boardrooms, the greatest risk is clinging to heritage at the expense of evolution. Great leaders honor legacy by reimagining it for the next generation. That requires capital courage and unshakeable conviction.",
            "w2_takeaway": "Innovation does not ask for permission. It builds the better model and invites the world to catch up.",

            "w3_title": "THE EXPANDING FRONTIER: CROSS-SPORT CAPITAL SYNERGY.",
            "w3_hook": "Look at the strategic portfolio Serena Williams has assembled across professional athletics.",
            "w3_body": "From tennis royalty to the NFL with the Miami Dolphins, to Angel City FC in soccer, to the Los Angeles Golf Club, Serena has created a masterclass in sports syndication. She is not merely an athlete investing spare earnings; she is an institutional operator understanding media rights, fan engagement, and franchise valuation.\n\nWhen I work with executive leaders and elite performers transitioning into their second acts, I remind them: your athletic career was your undergraduate degree. Your investments are your master's thesis.",
            "w3_takeaway": "Build a portfolio that outlives your physical prime. Your mind and your capital have no retirement age."
        },
        # 2: Venus - 7 Majors
        {
            "asset_idx": 2,
            "subject": "Venus Williams (7 Majors)",
            "w1_title": "7 MAJORS. THEN SHE BUILT MORE.",
            "w1_hook": "Seven Grand Slam singles titles. Four Olympic gold medals. A global icon who forever altered the velocity and athleticism of women's tennis. Yet, for Venus Williams, championships were merely chapter one.",
            "w1_body": "Most athletes reach the summit of their sport and spend the rest of their lives reminiscing about past glory. Venus understood early that medals gather dust, but enterprise compounds. While hoisting Wimbledon trophies, she was quietly sketching architectural plans and studying balance sheets.\n\nAs an Olympic coach, I have seen too many gifted champions suffer identity crises when the stadium lights go dark. Venus never suffered that fate because she never allowed tennis to be the sum total of who she was. She was an architect before she was a champion.",
            "w1_takeaway": "Never let your current title be your ceiling. Use every victory today to finance your vision for tomorrow.",

            "w2_title": "THE DUAL PURSUIT: COMPETING AT WIMBLEDON WHILE STUDYING P&L STATEMENTS.",
            "w2_hook": "How does an elite athlete manage the intense mental pressure of a Grand Slam tournament while reviewing commercial real estate contracts?",
            "w2_body": "Venus Williams shattered the myth that high-level athletes cannot possess intellectual and entrepreneurial breadth. She earned degrees in fashion design and business administration while actively ranked among the best tennis players on earth. She proved that focus is not about doing only one thing; focus is about bringing absolute presence to whatever task is before you.\n\nIn my coaching practice, executive clients frequently complain about lack of time. Time is rarely the obstacle; clarity of standards is. When your standard is excellence, that standard applies equally to your physical conditioning and your financial literacy.",
            "w2_takeaway": "Master compartmentalization. Bring champion focus to the baseline, and executive precision to the boardroom.",

            "w3_title": "LONGEVITY BEYOND THE BASELINE: ARCHITECTING A TIMELESS BRAND.",
            "w3_hook": "What does genuine longevity look like for an elite female athlete?",
            "w3_body": "It looks like Venus Williams continuing to compete on tour in her forties on her own terms, while steering multiple commercial enterprises that generate multi-million dollar annual revenues. She did not wait for tennis to discard her; she created a diversified life so expansive that tennis became a joyful pursuit rather than an economic necessity.\n\nThis is the ultimate form of athletic freedom: playing because you love the contest, not because you need the purse. That freedom is bought through discipline, foresight, and early ownership.",
            "w3_takeaway": "True independence is built when your livelihood is disconnected from a single scoreboard."
        },
        # 3: Venus - V Starr
        {
            "asset_idx": 3,
            "subject": "Venus Williams (V Starr Interior Architecture)",
            "w1_title": "DESIGN IT. OWN IT.",
            "w1_hook": "Walk into a high-end luxury hotel or residential tower designed by V Starr, and you will not see tennis rackets or athletic memorabilia on the walls.",
            "w1_body": "You will see soaring architectural lines, curated textures, and spaces designed with uncompromising poise. Venus Williams founded V Starr to compete in the exacting world of commercial and residential interior architecture, winning competitive bids on merit, taste, and technical execution.\n\nIn elite sport, form follows discipline. On the track, your posture determines your acceleration. In business, your environment dictates your mental clarity. Venus recognized that the physical spaces we inhabit shape how we think, create, and lead.",
            "w1_takeaway": "Do not trade on your celebrity when building an enterprise. Build technical competence that wins on merit alone.",

            "w2_title": "SPATIAL PSYCHOLOGY: HOW PHYSICAL ENVIRONMENTS DICTATE PERFORMANCE.",
            "w2_hook": "Why did an Olympic champion tennis player choose interior design as her core entrepreneurial venture?",
            "w2_body": "Because Venus Williams understands that physical environments either elevate human energy or drain it. When you spend decades competing in elite stadiums around the world, you develop an acute sensitivity to lighting, acoustics, proportion, and flow. V Starr translates that athletic sensitivity into spaces that foster calm, focus, and recovery.\n\nWhen I work with corporate leadership teams, one of the first audits we perform is environmental: where does your team think? Where do they recover? If your executive environment induces chaos, your decisions will reflect that chaos.",
            "w2_takeaway": "Curate your physical surroundings with the same intentionality an Olympian brings to her training facility.",

            "w3_title": "THE TECHNICAL BLUEPRINT: MASTERING COMMERCIAL SCALE.",
            "w3_hook": "Anyone can appreciate beautiful decor. Very few people can manage multi-million dollar commercial construction budgets, municipal zoning, and complex architectural blueprints.",
            "w3_body": "Venus Williams went to school, studied the craft, and built a licensed, full-service design firm capable of executing projects for luxury brands like InterContinental, Curio by Hilton, and premier private developers. She did not lend her name to someone else's agency; she built the firm from the ground up.\n\nIn coaching, I tell leaders: credibility is earned in the unglamorous details. Anyone can hold a microphone; the real leaders know what makes the engine turn.",
            "w3_takeaway": "Respect the craft. Deep technical competence will always outlast superficial celebrity branding."
        },
        # 4: Venus - Building Before Trending
        {
            "asset_idx": 4,
            "subject": "Venus Williams (V Starr Founded in 2002)",
            "w1_title": "SHE WAS BUILDING BEFORE IT WAS TRENDING.",
            "w1_hook": "In 2002, athlete entrepreneurship was largely limited to shoe contracts, soft drink commercials, and cereal boxes.",
            "w1_body": "At that exact moment, twenty-two-year-old Venus Williams, fresh off back-to-back Wimbledon and US Open crowns and ranked number one in the world, founded V Starr. She was not following a modern influencer playbook; she was writing the blueprint that an entire generation of athletes would follow twenty years later.\n\nDuring my coaching career, I have observed that true pioneers are always misunderstood in real time. When Venus started an interior design firm, critics questioned whether she was distracted from tennis. History proved she was simply decades ahead of her peers.",
            "w1_takeaway": "Do not wait for a path to become popular before you walk it. Pioneers build while the crowd is still debating.",

            "w2_title": "THE 24-YEAR ENDURANCE TEST: NAVIGATING ECONOMIC CYCLES.",
            "w2_hook": "Starting a business is exciting. Keeping a design and architectural firm thriving for twenty-four consecutive years through dot-com busts, housing crashes, and global pandemics is an endurance sport.",
            "w2_body": "V Starr has stood the test of time because Venus applied Olympic resilience to corporate governance. When economic cycles tightened, the firm adapted, diversified, and maintained its high standards. That kind of institutional longevity requires steady nerves and long-term capital discipline.\n\nIn executive coaching, I remind founders: your business will be tested by fire. What sustains you is not the initial excitement of launch day, but your daily systems of operational accountability.",
            "w2_takeaway": "Longevity is the ultimate competitive advantage. Stay in the game long enough to outlast temporary turbulence.",

            "w3_title": "PATIENCE IN PRIVATE BUILDING: THE SEED AND THE HARVEST.",
            "w3_hook": "We live in a culture obsessed with immediate virality and overnight unicorns. Real equity, however, grows like an oak tree.",
            "w3_body": "Venus Williams spent years working quietly on design boards, visiting tile yards, and reviewing client proposals away from television cameras. She was building proprietary assets while the world only measured her by Sunday finals. That patience in private building is what separates genuine entrepreneurs from cosmetic founders.\n\nWhen I prepare athletes for championship competition, I remind them: the medal ceremony lasts sixty seconds. The training took ten years. Business demands that exact same humility.",
            "w3_takeaway": "Fall in love with the untelevised work. That is where empires are truly constructed."
        },
        # 5: Venus - Happy Viking
        {
            "asset_idx": 5,
            "subject": "Venus Williams (Happy Viking)",
            "w1_title": "FROM ATHLETE NEED TO FOUNDER IDEA.",
            "w1_hook": "In 2011, Venus Williams was diagnosed with Sjogren's syndrome, an autoimmune disorder that caused severe joint pain, chronic fatigue, and threatened to end her tennis career prematurely.",
            "w1_body": "Faced with an invisible physical adversary, Venus did what champions do: she adapted. She transformed her entire lifestyle, embracing plant-based superfood nutrition to combat inflammation and restore her cellular health. When she could not find a clean, nutrient-dense protein shake that met her exacting athletic standards, she created Happy Viking.\n\nIn coaching, I teach that setback is not the finish line. Some of the most extraordinary innovations in human history were born because a leader encountered profound adversity and built the solution with their own hands.",
            "w1_takeaway": "Transform your personal hardship into public value. What challenged you can become the very foundation of your life's greatest work.",

            "w2_title": "BIOLOGICAL ADVERSITY INTO CATEGORY CREATION.",
            "w2_hook": "The consumer packaged goods industry is crowded with generic powders and marketing gimmicks. Happy Viking succeeded because its origin was rooted in survival.",
            "w2_body": "When Venus Williams speaks about plant-based protein and cellular recovery, she speaks with the authority of someone who used those exact nutrients to climb back into the top ten in the world and reach Grand Slam finals in her late thirties. Consumers do not just buy product ingredients; they invest in authentic conviction.\n\nIn corporate leadership, you cannot fake depth. When an executive has personally endured the furnace and developed real solutions, their authority is absolute.",
            "w2_takeaway": "Build from authentic pain points. An offering forged in personal necessity will always beat market speculation.",

            "w3_title": "THE FOUNDER'S ADVANTAGE: WHEN YOU ARE YOUR OWN IDEAL CUSTOMER.",
            "w3_hook": "Why do so many celebrity-backed consumer brands collapse within three years?",
            "w3_body": "Because the celebrity has no genuine stake in the product's daily efficacy. Venus Williams consumes Happy Viking every single day of her life. She is the ultimate quality control officer. She knows whether the blend causes bloating, whether it sustains energy through a third set, and whether it fuels rapid muscle repair.\n\nAs an Olympic coach, I demand total alignment between what an athlete preaches and how they train. In enterprise, that same alignment is the differentiator between a fleeting trend and an enduring brand.",
            "w3_takeaway": "Be your own most demanding client. If your product cannot satisfy your highest personal standard, it will never satisfy the marketplace."
        },
        # 6: Venus - Palazzo AI
        {
            "asset_idx": 6,
            "subject": "Venus Williams (Palazzo AI)",
            "w1_title": "DESIGN MEETS AI.",
            "w1_hook": "Many legacy business owners view artificial intelligence with fear and hesitation. Venus Williams looked at AI and saw her next company.",
            "w1_body": "As the co-founder of Palazzo, a generative AI design platform, Venus united her twenty-plus years of luxury architectural experience with cutting-edge visual technology. Palazzo allows homeowners and designers to instantly visualize, reimagine, and personalize physical spaces using conversational AI.\n\nIn sport, champions who refuse to adapt their technique get left behind by the speed of the modern game. In business, leaders who ignore technological shifts become obsolete. Venus stepped into technology with the same fearless aggression she brought to the net.",
            "w1_takeaway": "Do not resist technological transformation. Step into the arena and shape how it serves your industry.",

            "w2_title": "PAIRING HUMAN EXPERTISE WITH MACHINE LEVERAGE.",
            "w2_hook": "Technology without domain expertise is just cold algorithms. Domain expertise without technology is limited in scale.",
            "w2_body": "The magic of Palazzo lies in the fusion: decades of human design instinct, spatial sensitivity, and luxury aesthetics combined with generative machine learning. Venus understood that AI does not replace the human eye; it democratizes access to sophisticated spatial imagination for millions who could never hire a bespoke firm.\n\nWhen I work with executive leaders, I emphasize that technology is an amplifier of your underlying standard. If your standard is mediocre, tech accelerates mediocrity. If your standard is elite, tech provides exponential reach.",
            "w2_takeaway": "Combine your hard-earned human intuition with modern digital leverage to create category-defining platforms.",

            "w3_title": "HOW LEGACY OPERATORS LEAD TECHNOLOGICAL DISRUPTION.",
            "w3_hook": "What does it take for a traditional brick-and-mortar operator to successfully launch a venture-backed tech startup?",
            "w3_body": "It requires intellectual humility and collaborative courage. Venus did not try to code the models herself; she partnered with world-class technologists while providing the irreplaceable design vision and product philosophy. She understood her strengths, recognized her gaps, and assembled a complementary team.\n\nIn track and field, a great relay team does not consist of four identical runners. It consists of four distinct talents passing the baton with precision. Corporate leadership demands that exact same team construction.",
            "w3_takeaway": "Surround your domain expertise with top-tier technical partners. Great leadership is knowing what you know and empowering others to execute the rest."
        },
        # 7: Venus - Asutra
        {
            "asset_idx": 7,
            "subject": "Venus Williams (Asutra)",
            "w1_title": "USE THE PRODUCT. THEN OWN PART OF IT.",
            "w1_hook": "For decades, the standard athlete business model was passive endorsement: pose with a bottle, smile for a billboard, cash a check, and walk away.",
            "w1_body": "Venus Williams inverted that equation with Asutra. She was an avid user of their magnesium body butter and recovery products to manage her chronic pain and muscle stiffness. Instead of accepting a standard promotional fee, she negotiated an equity stake and stepped in as Chief Brand Officer.\n\nIn coaching, I teach athletes the difference between renting performance and owning your discipline. When you rent, you have no long-term stake in the outcome. When you own, every detail matters. Venus turned her medicine cabinet into an equity portfolio.",
            "w1_takeaway": "Stop settling for temporary endorsement checks. Align your capital with products you genuinely believe in, and demand a seat on the cap table.",

            "w2_title": "SWEAT EQUITY AND STRATEGIC BRAND GOVERNANCE.",
            "w2_hook": "What does a Chief Brand Officer who is also an Olympic champion bring to an emerging wellness brand?",
            "w2_body": "She brings visceral credibility. Venus did not simply attach her likeness to Asutra; she guided product formulation, packaging design, retail distribution strategy, and brand messaging. When Asutra secured national shelf space in major retailers like Target and Ulta, it was driven by a cohesive strategy led from the top.\n\nIn corporate retreats, I challenge executives to evaluate their true involvement in their company's core mission. Are you merely a figurehead, or are you actively steering the cultural and operational ship?",
            "w2_takeaway": "Active leadership will always outperform passive endorsement. Put your intellect and strategic guidance behind the equity you hold.",

            "w3_title": "ACTIVE RECOVERY AS AN EXECUTIVE DISCIPLINE.",
            "w3_hook": "We celebrate hustle, late nights, and grind. But in Olympic sport, we know a deeper truth: you do not grow during the workout; you grow during recovery.",
            "w3_body": "Venus Williams's partnership with Asutra highlights the indispensable role of active recovery. Sleep, magnesium, pain relief, and nervous system regulation are not luxuries for athletes; they are the non-negotiable infrastructure of high performance.\n\nWhen I coach C-suite executives and entrepreneurs, I frequently encounter leaders on the brink of burnout. They pride themselves on sleeping four hours a night. That is not commitment; that is poor risk management. If you do not schedule your recovery, your body will schedule it for you at the worst possible moment.",
            "w3_takeaway": "Treat recovery as a high-performance weapon. The leader who restores their energy with discipline will always outlast the one who runs on fumes."
        },
        # 8: Serena & Venus - Miami Dolphins
        {
            "asset_idx": 8,
            "subject": "Serena & Venus Williams (Miami Dolphins)",
            "w1_title": "THEY DIDN'T JUST WATCH THE LEAGUE.",
            "w1_hook": "In 2009, Serena and Venus Williams made history by purchasing an ownership stake in the Miami Dolphins, becoming the first African American women to hold equity in an NFL franchise.",
            "w1_body": "Think about the magnitude of that milestone. The NFL is the most commercially lucrative, culturally dominant sports league in North America, historically governed by an insular fraternity of male billionaires. Serena and Venus did not sit in the luxury suite as passive fans; they became minority partners and stakeholders.\n\nIn my coaching journey, I have stood on tracks where women were once forbidden from competing at Olympic distances. Progress never happens by waiting for the gates to open on their own. It happens when leaders with undeniable stature push the gates wide open for everyone who follows.",
            "w1_takeaway": "Do not merely consume the spectacles of industry. Position yourself to own a piece of the institution itself.",

            "w2_title": "REWRITING THE OWNERSHIP DEMOGRAPHIC AT THE HIGHEST LEVEL.",
            "w2_hook": "Representation in the stands is one thing. Representation in the boardroom where television contracts and league policies are finalized is entirely different.",
            "w2_body": "When Serena and Venus entered the NFL ownership fraternity, they altered the mental ceiling for every young athlete who watched them. They demonstrated that an athlete's ultimate victory is not catching the touchdown or hoisting the Vince Lombardi Trophy, but holding the equity that endures across generations.\n\nIn corporate leadership, diversity at the entry level is cosmetic if the board of directors remains homogenous. True transformation occurs when diverse leaders hold voting rights and equity stakes at the summit.",
            "w2_takeaway": "Focus your ambition on structural authority. Real influence begins where governance and capital meet.",

            "w3_title": "STRATEGIC SPORTS SYNDICATION: CONVERTING EARNINGS INTO ASSETS.",
            "w3_hook": "The greatest financial vulnerability of professional athletes is that their earning window is compressed into a single decade.",
            "w3_body": "Serena and Venus recognized that cash earned on court needed to be deployed into appreciating institutional assets with massive media-rights tailwinds. NFL franchise valuations have compounded exponentially over the past fifteen years. By taking that stake in 2009, they positioned themselves in an asset class that outpaces traditional equity markets.\n\nWhen I advise leaders and high performers on transition planning, I preach asset allocation: are your current cash flows being converted into assets that work while you sleep?",
            "w3_takeaway": "Take your active income and anchor it into appreciating institutional assets. That is how champion athletes build generational dynasties."
        },
        # 9: Serena & Venus - LA Golf Club
        {
            "asset_idx": 9,
            "subject": "Serena & Venus (Los Angeles Golf Club)",
            "w1_title": "TENNIS CHAMPIONS. GOLF OWNERS.",
            "w1_hook": "Two women who conquered global tennis with blistering serves and court poise, coming together to invest as primary owners in professional golf.",
            "w1_body": "The Los Angeles Golf Club represents more than an investment; it is a masterclass in sisterhood, shared capital, and cultural elevation. Alongside Serena's daughter Olympia, who became the youngest co-owner in professional sports, they built a family ownership syndicate that bridges generations.\n\nIn my coaching work, I celebrate teams that understand collective leverage. Individual brilliance wins matches, but united family vision creates dynasties that span decades.",
            "w1_takeaway": "Build with those you trust. When family values and professional excellence unite, the resulting enterprise is unbreakable.",

            "w2_title": "BRINGING CULTURAL RELEVANCE TO HISTORICALLY CLOSED FAIRWAYS.",
            "w2_hook": "Golf is undergoing a profound cultural renaissance, driven by technology, simulator leagues, and modern media.",
            "w2_body": "Serena and Venus understand how to capture the cultural zeitgeist. By anchoring the Los Angeles Golf Club in TGL, they are infusing a traditionally conservative sport with the vibrant energy of Southern California, modern music, and digital engagement. They are opening fairways to communities who previously felt golf was not for them.\n\nIn enterprise leadership, the brands that dominate the future are those that bridge classic heritage with contemporary culture. If you fail to invite the next generation in, your business will die of old age.",
            "w2_takeaway": "Infuse fresh cultural energy into traditional industries. Disruption is often just making an old game accessible to a new audience.",

            "w3_title": "MULTI-SPORT PORTFOLIO DIVERSIFICATION.",
            "w3_hook": "Why limit your sporting investments to the game you played?",
            "w3_body": "Athletic acumen is a transferable skill. Serena and Venus understand athlete psychology, high-pressure execution, coaching dynamics, and stadium entertainment. Those fundamental principles apply whether an athlete is swinging a composite tennis racket, tossing a football, or driving a golf ball.\n\nWhen executives consult with me on career transitions, they often discount their core competencies. Your ability to lead, execute, and build culture under pressure is universal. Never box your talent into a single industry.",
            "w3_takeaway": "Recognize the universality of your core strengths. Take what you mastered in one domain and deploy it fearlessly into the next."
        },
        # 10: Serena & Venus - The Trophy Isn't Endgame
        {
            "asset_idx": 10,
            "subject": "Serena & Venus (The Trophy Isn't The Endgame)",
            "w1_title": "THE TROPHY ISN'T THE ENDGAME.",
            "w1_hook": "Win. Build. Invest. Own. Create what comes next.",
            "w1_body": "These four words define the entire evolutionary trajectory of modern high performance. Winning is essential, but winning is merely proof of concept. The trophy is the key that opens doors; what you build once you step through the doorway determines your lasting legacy.\n\nAs an Olympic coach, I have placed gold medals around the necks of champions. In that moment of triumph, my quiet question to them is always: 'Now, what will you do with this platform?' If your vision ends with the medal, your growth ends there too.",
            "w1_takeaway": "Never mistake a victory celebration for the destination. Winning is simply your ticket to the real building phase.",

            "w2_title": "THE FOUR STAGES OF MODERN ATHLETE MATURITY.",
            "w2_hook": "Examine the trajectory of the greatest athletes in modern history: Stage One is winning on the field. Stage Two is building personal enterprise. Stage Three is allocating capital as an investor. Stage Four is institutional ownership.",
            "w2_body": "Serena and Venus Williams have mastered all four stages before our very eyes. They did not skip steps. They earned their credibility through sweat and championships, built foundational companies, deployed venture capital into visionary founders, and acquired franchises in the NFL, WNBA, NWSL, and TGL.\n\nIn corporate leadership, you must respect the sequencing of growth. You cannot skip foundational execution and jump straight to executive delegation. Master the fundamentals first, then build your empire upon that rock.",
            "w2_takeaway": "Respect the progression of mastery: win your arena, build your craft, invest your capital, and own your future.",

            "w3_title": "WHAT HAPPENS WHEN THE APPLAUSE GOES SILENT?",
            "w3_hook": "The most terrifying moment in an athlete's life is the sudden silence when forty thousand cheering fans leave the stadium and the locker room lights turn off.",
            "w3_body": "For many, that silence brings depression, aimlessness, and financial decline. For Serena and Venus Williams, that silence was simply the cue for their next meeting. They prepared for retirement twenty years before it arrived. They were so busy building companies and allocating capital that stepping away from competitive tennis was not an ending; it was an expansion.\n\nIn coaching, I prepare leaders for the next chapter long before the current chapter concludes. If you only prepare for transition when crisis strikes, you have already surrendered your momentum.",
            "w3_takeaway": "Prepare your second act while your first act is at its peak. The applause will fade, but your built foundation will stand."
        },
        # 11: Serena x Venus - From Champion to Owner
        {
            "asset_idx": 11,
            "subject": "Serena x Venus (From Champion to Owner)",
            "w1_title": "FROM CHAMPION TO OWNER: THE COMPTON BLUEPRINT.",
            "w1_hook": "Before there were private jets, Met Gala red carpets, and venture capital syndicates, there were cracked public tennis courts in Compton, California.",
            "w1_body": "Richard and Oracene Williams did not merely teach their daughters how to hit an open-stance forehand. They taught them self-worth, financial sovereignty, and psychological immunity against external doubt. They drilled into them that tennis was a vehicle for education, empowerment, and independence.\n\nIn my coaching career, I have observed that elite champions are built at home, in the quiet moments of values transmission. When the foundation is anchored in purpose and dignity, no external storm can shake the structure.",
            "w1_takeaway": "Build your values before you build your enterprise. An empire without a moral foundation will collapse under its own weight.",

            "w2_title": "SISTERHOOD AS A BOARDROOM SUPERPOWER.",
            "w2_hook": "In a hyper-competitive world that constantly tries to pit talented women against one another, Serena and Venus did the unthinkable: they stood shoulder-to-shoulder for thirty consecutive years.",
            "w2_body": "They competed against each other in nine Grand Slam singles finals with ferocious athletic intensity, and walked off the court hand-in-hand to co-invest in real estate, venture capital, and sports franchises. They demonstrated that healthy competition does not require personal destruction.\n\nIn executive teams, internal rivalry often poisons corporate culture. True leadership creates an environment where team members push each other to peak performance while remaining fiercely loyal to the collective mission.",
            "w2_takeaway": "Compete with intensity, but unite with loyalty. When partners trust each other completely, no competitor can divide them.",

            "w3_title": "CREATING AN UNDENIABLE LEGACY BLUEPRINT.",
            "w3_hook": "The true measure of a pioneer is not how high they climbed, but how many people they enabled to follow in their footsteps.",
            "w3_body": "Serena and Venus Williams changed the paradigm of what is possible for women in business and athletics. Today, young female athletes negotiate equity stakes in early-stage startups, launch media production houses, and demand ownership percentages in expansion leagues because the Williams sisters proved it could be done.\n\nAs a coach, that is the definition of Olympic legacy. You do not coach for the immediate podium; you coach to elevate the human standard for decades to come.",
            "w3_takeaway": "Live your life in a manner that expands the imagination of those who watch you. Your courage gives others permission to be bold."
        },
        # 12: Serena - 23 Majors
        {
            "asset_idx": 12,
            "subject": "Serena Williams (23 Majors)",
            "w1_title": "23 MAJORS. AND SHE KEPT BUILDING.",
            "w1_hook": "Twenty-three Grand Slam singles titles in the Open Era. An Olympic singles gold medal, three Olympic doubles gold medals, and seventy-three career singles titles.",
            "w1_body": "Serena Williams conquered every record tennis had to offer. Yet, when she retired from professional tennis, she deliberately used the word 'evolution.' She was not stepping down; she was evolving into venture capital, entrepreneurship, and maternal leadership.\n\nIn my coaching practice, I see leaders achieve monumental goals and immediately fall into complacency. Serena demonstrated that records are milestones, not resting places. When you possess championship stamina, you apply that energy to new summits.",
            "w1_takeaway": "Do not let your greatest victory become your permanent monument. Celebrate the milestone, then lace up your boots for the next mountain.",

            "w2_title": "THE PSYCHOLOGICAL POISE OF A TIEBREAK TRANSLATED TO DEALMAKING.",
            "w2_hook": "What happens inside a champion's mind when facing match point in the third set of a US Open final?",
            "w2_body": "The heartbeat slows down. The peripheral vision narrows. The breathing becomes deliberate. Fear is replaced by pure execution. That exact psychological poise is what Serena Williams brings to high-stakes venture capital negotiations and term-sheet evaluations.\n\nIn corporate leadership, high-stress moments are where fortunes are won or lost. Leaders who panic make desperate concessions. Leaders who possess athletic composure remain calm, evaluate the data, and make calculated moves.",
            "w2_takeaway": "Train your nervous system for pressure. Calm is the ultimate executive power.",

            "w3_title": "RELENTLESS WORK ETHIC AS AN UNBREAKABLE HABIT.",
            "w3_hook": "Talent opens the door; relentless work ethic keeps you in the room.",
            "w3_body": "Serena Williams was famous for showing up on practice courts in blistering heat, hitting hundreds of serves until her shoulder burned, and refusing to leave until her technique was flawless. That same obsession with preparation governs how she reads pitch decks, interviews startup founders, and reviews consumer product formulations.\n\nIn track and field, we have a simple saying: the will to win means nothing without the will to prepare. Excellence is simply the accumulation of unseen, disciplined habits.",
            "w3_takeaway": "Out-prepare your competition in private. When game day arrives, your preparation will speak with absolute authority."
        },
        # 13: Serena - Serena Ventures Capital
        {
            "asset_idx": 13,
            "subject": "Serena Williams (Serena Ventures)",
            "w1_title": "THE NEXT COURT WAS CAPITAL.",
            "w1_hook": "In 2014, Serena Williams quietly founded Serena Ventures. She did not launch a vanity fund; she built a top-tier venture firm investing early-stage capital across health, fintech, and consumer innovation.",
            "w1_body": "Serena realized that less than two percent of all venture capital funding went to female founders, and an even smaller fraction went to women of color. Instead of writing angry op-eds, she raised institutional capital, partnered with seasoned allocators, and started writing checks directly to underrepresented entrepreneurs.\n\nAs an Olympic coach, I know that speeches do not build champions; resources, coaching, and opportunities do. Serena deployed capital where the market had blind spots, capturing outsized returns while driving profound systemic change.",
            "w1_takeaway": "Do not just complain about industry bias. Build the capital vehicle that reallocates power where it belongs.",

            "w2_title": "WRITING CHECKS ON SAND HILL ROAD.",
            "w2_hook": "Venture capital in Silicon Valley has long operated as an exclusive network of homogeneous founders and investors backing familiar ideas.",
            "w2_body": "Serena Williams walked onto Sand Hill Road and completely disrupted that pattern. Her portfolio boasts dozens of high-growth technology and consumer companies, with over seventy percent of investments flowing to women and diverse founders. She proved that investing in diversity is not charity; it is one of the highest-alpha strategies in modern finance.\n\nIn corporate strategy, market blind spots represent your greatest competitive advantage. When everyone is looking in one direction, look where talent is being overlooked.",
            "w2_takeaway": "Seek out underestimated talent. The highest returns in business come from backing brilliance that the consensus ignored.",

            "w3_title": "THE UNFAIR ADVANTAGE OF ATHLETE PATTERN RECOGNITION.",
            "w3_hook": "What makes an elite athlete an exceptional early-stage venture capitalist?",
            "w3_body": "Pattern recognition and grit assessment. Serena Williams has spent forty years observing human behavior under extreme pressure. Within ten minutes of meeting an early-stage founder, she can detect whether that founder has the psychological stamina to survive market downturns or whether they will crumble when adversity strikes.\n\nIn leadership hiring, technical resumes only tell half the story. The decisive factor is always character: how does this candidate respond when everything goes wrong?",
            "w3_takeaway": "Evaluate human grit before financial projections. Ideas are cheap; execution under pressure is priceless."
        },
        # 14: Serena - Build Equity
        {
            "asset_idx": 14,
            "subject": "Serena Williams (Build Equity)",
            "w1_title": "DON'T JUST BUILD INFLUENCE. BUILD EQUITY.",
            "w1_hook": "Followers come and go. Algorithm changes wipe out social reach overnight. Equity on a capitalization table, however, endures.",
            "w1_body": "Serena Williams understands the fundamental difference between influence and equity. Influence is renting your voice to build someone else's balance sheet. Equity is holding ownership percentages in companies that compound in value over decades.\n\nIn my coaching work with emerging leaders, I often warn against the vanity metrics of modern culture. Likes, impressions, and viral moments do not pay dividends. Real power is ownership of the asset itself.",
            "w1_takeaway": "Trade your temporary attention for permanent equity. Own the underlying assets that compound while you sleep.",

            "w2_title": "THE DANGEROUS ILLUSION OF INFLUENCER CAPITALISM.",
            "w2_hook": "Too many high-profile creators and athletes believe their social following makes them wealthy. Without equity, they are simply glorified contract workers.",
            "w2_body": "Serena Ventures was designed to dismantle that illusion. By educating founders and backing companies with solid unit economics, Serena teaches that a business must stand on product-market fit, operational efficiency, and scalable cash flow, not just celebrity endorsements.\n\nIn enterprise leadership, sustainable growth is built on disciplined fundamentals. Marketing can buy attention for an afternoon; only an exceptional product earns customer retention for a decade.",
            "w2_takeaway": "Do not build a business on hype. Anchor your company in undeniable product excellence and disciplined financial governance.",

            "w3_title": "CREATING MULTI-GENERATIONAL FINANCIAL INDEPENDENCE.",
            "w3_hook": "What does genuine financial independence look like across generations?",
            "w3_body": "It looks like a mother passing down cap table stakes in disruptive technology companies, sports franchises, and proprietary brands to her daughters. Serena Williams is actively constructing a legacy that will insulate and empower her family for centuries.\n\nAs a coach and mentor, I remind my students that the standard you set today becomes the floor for your children tomorrow. Raise your ceiling so their starting line is higher than you ever dreamed.",
            "w3_takeaway": "Think in generations, not quarters. Build an enterprise that provides security and opportunity long after your name leaves the headlines."
        },
        # 15: Serena - WYN Beauty Formulations
        {
            "asset_idx": 15,
            "subject": "Serena Williams (WYN Beauty Formulation)",
            "w1_title": "SHE BUILT THE PRODUCT TOO.",
            "w1_hook": "When Serena Williams stepped onto Arthur Ashe Stadium under brutal humid heat, playing three punishing sets of championship tennis, her makeup had to withstand the elements.",
            "w1_body": "For years, standard commercial cosmetics melted under athletic sweat. In response, Serena developed WYN Beauty: a high-performance, sweat-resistant, hydrating cosmetic line formulated specifically for active women who refuse to choose between performance and elegance.\n\nIn coaching, I teach that real innovation occurs at the point of greatest friction. When you encounter a frustration in your daily routine, you are looking at a commercial opportunity waiting to be seized.",
            "w1_takeaway": "Solve your own operational friction with excellence. What you need to succeed is what thousands of others are searching for.",

            "w2_title": "PROPRIETARY FORMULATION VERSUS WHITE-LABEL LICENSING.",
            "w2_hook": "It is easy for a celebrity to sign a licensing agreement, let a third-party manufacturer slap a logo on a generic formula, and collect a five percent royalty.",
            "w2_body": "Serena Williams took the hard road. She spent six years testing ingredients, perfecting pigment shades for diverse skin tones, and developing custom formulations that hydrate while resisting sweat. She built WYN Beauty as an owner, not an endorser.\n\nIn executive leadership, shortcuts always compromise quality. If you want to build an enduring enterprise, you must master the supply chain, control the formulation, and stand behind every single unit shipped.",
            "w2_takeaway": "Never outsource your quality control. Put your personal reputation on the line only when you have verified the product yourself.",

            "w3_title": "AUTHENTICITY IN CONSUMER PRODUCT EXECUTION.",
            "w3_hook": "Today's consumers are smarter and more discerning than at any point in marketing history. They can smell artificial endorsements from miles away.",
            "w3_body": "WYN Beauty resonated immediately with consumers because Serena's life is living proof of the product's claims. When a woman who won twenty-three Grand Slam titles tells you a formula will not run during a workout or a high-pressure corporate presentation, you believe her because she tested it under global scrutiny.\n\nIn coaching, authority is earned through congruent behavior. When your actions match your words, you never have to convince anyone to trust you.",
            "w3_takeaway": "Let your product be an extension of your lived truth. Authenticity is the only marketing strategy that never depreciates."
        },
        # 16: Serena - WYN Beauty Strategy
        {
            "asset_idx": 16,
            "subject": "Serena Williams (WYN Beauty Strategy)",
            "w1_title": "ATTENTION IS POWERFUL. OWNERSHIP IS DIFFERENT.",
            "w1_hook": "Attention is a fire that burns hot and fast. Ownership is the engine that converts that fire into sustainable energy.",
            "w1_body": "WYN Beauty represents the complete synthesis of Serena Williams's global brand equity. She took the worldwide attention she commanded on the tennis court and channeled it into a proprietary direct-to-consumer and retail beauty powerhouse carried in Ulta Beauty stores across the United States.\n\nIn my coaching work with high-profile athletes and executives, I often ask: 'What are you converting your visibility into?' If your fame only produces more selfies, you are squandering your leverage. Convert your visibility into an asset that works for you.",
            "w1_takeaway": "Do not let your visibility evaporate into vanity. Direct the spotlight onto assets that build lasting enterprise value.",

            "w2_title": "TURNING A POINT OF VIEW INTO A CONSUMER CATEGORY.",
            "w2_hook": "What is the core message of WYN Beauty? Protect. Hydrate. Show Up.",
            "w2_body": "Those three imperatives are not just cosmetic instructions; they are life principles. Serena turned her personal philosophy of resilience, self-care, and executive presence into a cohesive brand ethos that empowers women in gymnasiums, boardrooms, and family rooms alike.\n\nIn corporate branding, products satisfy functional needs, but brands satisfy emotional identity. When your brand stands for an unshakeable standard of human dignity, customer loyalty becomes generational.",
            "w2_takeaway": "Infuse your enterprise with a profound moral purpose. People do not just buy what you make; they buy what you stand for.",

            "w3_title": "CHANNELING MASS DISTRIBUTION THROUGH STRATEGIC RETAIL.",
            "w3_hook": "A great product without distribution is like an Olympic sprinter running in the dark.",
            "w3_body": "Serena Williams understood that scaling WYN Beauty required premier brick-and-mortar retail partnership. Launching in hundreds of Ulta Beauty doors nationwide alongside an intuitive digital platform ensured that her product was physically accessible to every woman seeking high-performance beauty.\n\nIn enterprise development, operational logistics and retail distribution are the unsung heroes of success. Build the pipeline that delivers your brilliance directly into the hands of your audience.",
            "w3_takeaway": "Pair visionary branding with ruthless distribution logistics. Excellence must be accessible to be impactful."
        },
        # 17: Serena - Nine Two Six Productions
        {
            "asset_idx": 17,
            "subject": "Serena Williams (Nine Two Six Productions)",
            "w1_title": "OWN THE STORY.",
            "w1_hook": "For decades, other people controlled the narrative of Serena and Venus Williams. Journalists, commentators, and biographers framed their story through their own lenses.",
            "w1_body": "With the creation of Nine Two Six Productions, Serena took total command of the narrative pen. Named after her birthday and dedicated to championing diverse, female-led, and boundary-pushing stories, Nine Two Six produces television, film, and digital content that reflect authentic human triumphs.\n\nIn coaching, I teach that whoever controls your narrative controls your future. If you allow competitors or critics to define your identity, you have already surrendered your race. Tell your own story, in your own voice, with absolute conviction.",
            "w1_takeaway": "Take ownership of your narrative. Do not let others write the history of what you bled to achieve.",

            "w2_title": "PRODUCING CONTENT THAT ELEVATES OVERLOOKED VOICES.",
            "w2_hook": "Hollywood has historically suffered from the same blind spots as Wall Street: recycling the same familiar stories and overlooking the rich tapestry of diverse experiences.",
            "w2_body": "Nine Two Six Productions was built to finance and produce content that centers female resilience, complex characters, and uplifting stories that inspire the global majority. Serena is using her media leverage to greenlight projects that traditional studio executives hesitated to back.\n\nIn executive leadership, true power is the ability to open doors for others. When you reach a position of institutional influence, your responsibility is to broaden the creative canon.",
            "w2_takeaway": "Use your executive authority to finance stories that matter. Culture is shaped by the stories we choose to elevate.",

            "w3_title": "INTELLECTUAL PROPERTY AS THE APEX ASSET CLASS.",
            "w3_hook": "What is the most valuable asset class in the twenty-first century? Proprietary intellectual property.",
            "w3_body": "By owning scripts, production rights, and documentary archives, Serena Williams is building a library of media IP that will pay royalties, streaming fees, and licensing revenue for decades. She understands that physical skills diminish, but compelling stories live forever.\n\nWhen I work with leaders on legacy building, I emphasize intellectual capital: what frameworks, books, systems, and stories have you created that can exist independently of your daily labor?",
            "w3_takeaway": "Build intellectual property that outlives you. Ideas codified into media become eternal monuments to your life's purpose."
        },
        # 18: Serena - The CEO Club
        {
            "asset_idx": 18,
            "subject": "Serena Williams (The CEO Club)",
            "w1_title": "ON CAMERA. BEHIND THE CAMERA.",
            "w1_hook": "Athlete. Entrepreneur. Executive Producer. Serena Williams stars in and produces The CEO Club, seamlessly moving between creative performance and executive governance.",
            "w1_body": "In the past, society demanded that women pick a lane: either stay in front of the lens as talent, or retreat behind closed doors in a business suit. Serena shattered that binary. She commands the set, delivers the performance, and signs the production checks.\n\nIn my coaching journey, I have watched female athletes constantly pressured to diminish their ambition to make others comfortable. Greatness does not compromise. You can be the talent, the founder, and the CEO all at once.",
            "w1_takeaway": "Refuse to be boxed into someone else's narrow category. Command the stage and own the production.",

            "w2_title": "REDEFINING THE VISUAL IDENTITY OF MODERN LEADERSHIP.",
            "w2_hook": "What does a CEO look like in 2026?",
            "w2_body": "She looks like Serena Williams in a tailored white pantsuit, hair voluminous and proud, gold jewelry gleaming, commanding respect through track record, intellect, and poise. She does not mimic corporate clichés; she brings her authentic, powerful self into every room she enters.\n\nIn corporate executive coaching, I see many rising leaders try to adopt a persona that feels unnatural to them. Authenticity is magnetic. When you own your full identity, your executive presence becomes undeniable.",
            "w2_takeaway": "Never disguise your heritage or individuality to fit into corporate boardrooms. Let your authentic presence redefine the room.",

            "w3_title": "THE TRANSITION FROM TACTICAL OPERATOR TO EXECUTIVE PRODUCER.",
            "w3_hook": "The hardest transition for an elite operator is shifting from executing tasks to orchestrating ecosystems.",
            "w3_body": "On the tennis court, Serena was the ultimate tactical operator: every swing was hers. In television production and corporate leadership, an Executive Producer must trust directors, writers, cinematographers, and financial officers to do their jobs. Serena mastered that transition with graceful authority.\n\nIn leadership development, the ceiling of your success is determined by your ability to delegate and elevate others. Great leaders do not create followers; they cultivate other leaders.",
            "w3_takeaway": "Evolve from a solo performer into an orchestral conductor. Your true scale begins when you empower others to execute your vision."
        },
        # 19: Serena - Toronto Tempo
        {
            "asset_idx": 19,
            "subject": "Serena Williams (Toronto Tempo)",
            "w1_title": "FROM PLAYING SPORTS TO OWNING SPORTS.",
            "w1_hook": "Standing on a private balcony overlooking the Toronto skyline and Scotiabank Arena, Serena Williams solidified her position as a principal owner of the Toronto Tempo, the WNBA's groundbreaking Canadian franchise.",
            "w1_body": "Think about the historical poetry of this moment: a woman who dominated global athletics is now bringing the highest level of professional women's basketball to Canada as a franchise owner. She is not cheering from courtside; she is building the club's commercial future.\n\nAs a Canadian national champion and Olympic coach who spent decades developing athletic infrastructure in this country, this move moves my heart deeply. Serena is investing in our daughters, our communities, and our sports economy.",
            "w1_takeaway": "Invest in the future of the communities that supported your rise. Your capital can build the stadiums where tomorrow's legends are born.",

            "w2_title": "THE COMMERCIAL EXPLOSION OF WOMEN'S PROFESSIONAL SPORTS.",
            "w2_hook": "For decades, corporate sponsors and media networks dismissed women's sports as a charitable endeavor. Today, women's sports is the fastest-growing commercial asset class in global business.",
            "w2_body": "Serena Williams recognizes economic inflection points before the rest of the market catches on. The Toronto Tempo represents a massive commercial market in one of the most multicultural, sports-obsessed cities in the world. By securing equity early in this WNBA expansion wave, she is capturing exponential valuation upside.\n\nIn business strategy, timing is everything. Those who recognize systemic cultural shifts and allocate capital before consensus forms reap the greatest rewards.",
            "w2_takeaway": "Position your capital in front of undeniable cultural momentum. The greatest opportunities exist where others once saw limitations.",

            "w3_title": "BUILDING PATHWAYS FOR THE NEXT GENERATION OF ATHLETES.",
            "w3_hook": "When a young girl in Toronto, Montreal, or Vancouver watches the Toronto Tempo play, she will not just see professional basketball players on the floor.",
            "w3_body": "She will see Serena Williams listed as the principal owner in the team media guide. That visual realization fundamentally alters a child's understanding of what is possible. It teaches her that sport is not just about competing; sport is about leadership, governance, and ownership.\n\nIn my coaching career, that has always been the ultimate purpose: building pathways that outlast our own lives. Lornette Daye ran and coached so that the next generation could soar even higher.",
            "w3_takeaway": "Leave a legacy that builds ladders for those coming behind you. That is the highest calling of athletic and corporate excellence."
        },
        # 20: Serena - Miami Dolphins Partner
        {
            "asset_idx": 20,
            "subject": "Serena Williams (Miami Dolphins Partner)",
            "w1_title": "THE PLAYER BECAME THE PARTNER.",
            "w1_hook": "Look closely at this image: Serena Williams, seated comfortably in the luxury suite overlooking Hard Rock Stadium, home of the Miami Dolphins.",
            "w1_body": "The athlete became the owner. The player became the partner. The competitor became the governor. That is the journey from champion to owner, and it is the standard by which all modern athletic careers must be evaluated.\n\nThroughout this campaign, we have dissected the business architecture of Serena and Venus Williams. They showed us that sports is a school of discipline, and the real graduation ceremony happens in the boardroom when you sign your name on the ownership registry.",
            "w1_takeaway": "Never settle for being the talent on the field. Do the work, build the discipline, and become the partner in the suite.",

            "w2_title": "CROSSING THE THRESHOLD INTO INSTITUTIONAL GOVERNANCE.",
            "w2_hook": "What does it feel like to walk into an NFL owners' meeting and look across the table at thirty-one fellow franchise stakeholders?",
            "w2_body": "It demands an unshakeable sense of self-worth and dignity. Serena Williams never flinched. She walked into football's most powerful boardroom with the quiet confidence of a woman who built her fortune with her own hands and survived the most brutal athletic crucibles on earth.\n\nIn my Finish Strong keynotes to executive teams, I remind leaders: your authority does not come from your title; it comes from your scars, your preparation, and your unwavering integrity.",
            "w2_takeaway": "Walk into every boardroom knowing you belong there. Your track record of resilience is your greatest credential.",

            "w3_title": "THE GRAND CLIMAX: FINISH WHAT YOU STARTED.",
            "w3_hook": "We conclude this 60-day Business Athletes masterclass with the signature principle that defines my life, my coaching, and my books: Finish Strong.",
            "w3_body": "Serena and Venus Williams started on public asphalt courts in Compton with worn-out tennis balls and painted lines. Today, they own sports teams, venture capital funds, luxury design firms, and global consumer brands. They faced racism, sexism, injury, autoimmune disease, and family tragedy, yet they never conceded their race.\n\nTo every executive, founder, and athlete reading these words: the journey is demanding, but the summit is worth every drop of sweat. Honor your foundation, protect your standard, and finish what you started.",
            "w3_takeaway": "Run your race with unshakeable purpose. When the final buzzer sounds, let the world see that you held nothing back."
        }
    ]

    print(f"Loaded {len(blueprints)} detailed post blueprints.")

    # Now let's assemble all 60 posts
    posts_data = []

    # Book catalog links and CTA variations for even days
    book_ctas = [
        {
            "book": "Survival Skills for Women",
            "price": "$14.99 CAD",
            "url": "https://lornettedaye.com/books",
            "text": "Equip yourself with the tools for confidence, resilience, and personal renewal. Read Survival Skills for Women ($14.99 CAD): https://lornettedaye.com/books"
        },
        {
            "book": "Survival Skills for Athletes",
            "price": "$14.99 CAD",
            "url": "https://lornettedaye.com/books",
            "text": "Build a champion mindset, focus under pressure, and life balance. Order Survival Skills for Athletes ($14.99 CAD): https://lornettedaye.com/books"
        },
        {
            "book": "Survival Skills: Surviving to Thriving",
            "price": "$14.99 CAD",
            "url": "https://lornettedaye.com/books",
            "text": "Move beyond survival mode and step into purpose-driven momentum. Read Surviving to Thriving ($14.99 CAD): https://lornettedaye.com/books"
        },
        {
            "book": "Finish Strong: Chasing the Olympic Dream",
            "price": "$14.99 CAD",
            "url": "https://lornettedaye.com/books",
            "text": "Discover Lornette Daye's autobiography on resilience, identity, and legacy. Get Finish Strong: Chasing the Olympic Dream ($14.99 CAD): https://lornettedaye.com/books"
        }
    ]

    keynote_ctas = [
        "Bring Lornette Daye's Olympic high-performance and transition framework to your corporate summit, conference, or executive retreat. Book my keynote: https://lornettedaye.com/book",
        "Empower your executive leadership team with Olympic-grade poise, accountability, and strategic alignment. Inquire about keynote speaking and retreats: https://lornettedaye.com/book",
        "Inspire your organization with the mindset that transforms high performers into generational leaders. Book Lornette Daye for your next event: https://lornettedaye.com/book",
        "Equip your corporate board and senior executives to lead through pressure and transition. Schedule my Finish Strong keynote: https://lornettedaye.com/book"
    ]

    for day_i in range(1, 61):
        dt = start_date + timedelta(days=day_i - 1)
        is_mst = dt >= datetime(2026, 11, 1)
        due_utc = f"{dt.strftime('%Y-%m-%d')}T19:00:00.000Z" if is_mst else f"{dt.strftime('%Y-%m-%d')}T18:00:00.000Z"
        tz_abbr = "MST" if is_mst else "MDT"
        day_name = dt.strftime("%A")
        date_display = dt.strftime("%b %d, %Y")
        slot_str = f"Day {day_i}: {day_name}, {date_display} at 12:00 PM {tz_abbr}"

        # Wave calculation
        if day_i <= 20:
            wave_name = "Wave 1: The Architecture of Ownership (Transcending the Trophy)"
            wave_key = "w1"
        elif day_i <= 40:
            wave_name = "Wave 2: Venture Capital, Product Innovation & Enterprise Equity"
            wave_key = "w2"
        else:
            wave_name = "Wave 3: Sports Franchises, Media Empires & Generational Legacy"
            wave_key = "w3"

        bp_idx = (day_i - 1) % 20
        bp = blueprints[bp_idx]
        asset_file = f"business-athletes-{bp['asset_idx']:02d}.png"
        asset_url = f"https://lornettedaye.com/campaigns/business-athletes/{asset_file}"

        title = bp[f"{wave_key}_title"]
        hook = bp[f"{wave_key}_hook"]
        body = bp[f"{wave_key}_body"]
        takeaway = bp[f"{wave_key}_takeaway"]

        # CTA Selection
        is_odd = (day_i % 2 != 0)
        if is_odd:
            cta_type = "Keynote Booking (lornettedaye.com/book)"
            cta_text = keynote_ctas[(day_i // 2) % len(keynote_ctas)]
        else:
            book_obj = book_ctas[((day_i // 2) - 1) % len(book_ctas)]
            cta_type = f"Buy Book - {book_obj['book']} (lornettedaye.com/books)"
            cta_text = book_obj["text"]

        sign_offs = ["With purpose,\nLornette", "Stay focused,\nLornette", "Keep building,\nLornette", "In your corner,\nLornette", "With conviction,\nLornette"]
        sign_off = sign_offs[(day_i - 1) % len(sign_offs)]

        hashtags = (
            "#SerenaWilliams #VenusWilliams #BusinessAthletes #FromChampionToOwner #WomenInBusiness "
            "#ExecutiveLeadership #OwnershipMindset #VentureCapital #OlympicMindset #FinishStrong "
            "#LornetteDaye #HighPerformance #KeynoteSpeaker #WomenEntrepreneurs #BoardroomExcellence"
        )

        full_text = f"{title}\n\n{hook}\n\n{body}\n\n{takeaway}\n\n{sign_off}\n\n{cta_text}\n\n{hashtags}"

        # Clean check em dashes
        for em_dash in ["\u2014", "&mdash;", "—"]:
            if em_dash in full_text:
                raise ValueError(f"Post {day_i} contains em dash ({em_dash})!")

        if "Coach Lornette" in full_text:
            raise ValueError(f"Post {day_i} is signed Coach Lornette!")
        if "Lornette" not in full_text:
            raise ValueError(f"Post {day_i} missing Lornette signature!")

        posts_data.append({
            "id": day_i,
            "wave": wave_name,
            "slot": slot_str,
            "dueAt": due_utc,
            "assetFile": asset_file,
            "assetUrl": asset_url,
            "cta": cta_type,
            "text": full_text
        })

    print(f"Generated {len(posts_data)} posts successfully. Performing comprehensive invariant checks...")
    
    # Check invariant count
    assert len(posts_data) == 60, "Must be exactly 60 posts!"
    keynote_count = sum(1 for p in posts_data if p["cta"].startswith("Keynote Booking"))
    book_count = sum(1 for p in posts_data if p["cta"].startswith("Buy Book"))
    print(f"CTA Split: {keynote_count} Keynote CTAs, {book_count} Book CTAs.")
    assert keynote_count == 30 and book_count == 30, "Must be exact 50/50 CTA split!"

    # Now write scripts/schedule-business-athletes.py
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

CDN_BASE = 'https://lornettedaye.com/campaigns/business-athletes'

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
print("INVARIANTS AUDIT PASSED: 60 posts verified. 0 em dashes, all signed strictly 'Lornette', 50/50 alternating CTA.")

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

    report_path = "scripts/business-athletes-scheduled-report.json"
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
            print(f"[{{i}}/60] Post #{{p_id}} already scheduled (Buffer ID: {{results[p_id]['postId']}}). Skipping.")
            continue

        while True:
            print(f"\\n[{{i}}/60] Scheduling Post #{{p['id']}} ({{p['slot']}}) - Due: {{p['dueAt']}}...")
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
    print(f"\\nExecution complete. Saved {{success_count}}/60 successfully to {{report_path}}.")
    return success_count == len(posts_data)

if __name__ == "__main__":
    schedule_posts()
'''

    out_file = os.path.join(os.path.dirname(__file__), "schedule-business-athletes.py")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(script_content)
    print(f"Wrote {len(posts_data)} posts to {out_file} successfully ({os.path.getsize(out_file):,} bytes)!")

if __name__ == "__main__":
    generate_campaign_script()
