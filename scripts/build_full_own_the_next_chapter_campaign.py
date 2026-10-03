# -*- coding: utf-8 -*-
"""
Campaign Builder for "OWN THE NEXT CHAPTER"
Generates 180 detailed, bespoke posts across 60 days (Oct 3, 2026 - Dec 1, 2026).
3 posts per day: Morning (7:45 AM), Afternoon (2:30 PM), Evening (6:30 PM) MDT/MST.
Featuring 6 icons:
1. Tiger Woods (30 posts)
2. Stephen Curry (30 posts)
3. Ayesha Curry (30 posts)
4. Stephen & Ayesha Curry (30 posts)
5. Serena Williams (30 posts)
6. Lewis Hamilton (30 posts)
Strict Invariants:
- Zero em dashes (—, &mdash;, \u2014)
- Authoritative Olympian coach voice (first-person, "I", "my")
- Signed strictly as "Lornette"
- 50/50 Keynote (lornettedaye.com/book) vs Book (lornettedaye.com/books) CTA split
"""
import sys
import os
import json
from datetime import datetime, timedelta

sys.stdout.reconfigure(encoding='utf-8', line_buffering=True)
sys.stderr.reconfigure(encoding='utf-8', line_buffering=True)

# -------------------------------------------------------------
# ATHLETE BLUEPRINTS (30 bespoke posts per athlete = 180 total)
# -------------------------------------------------------------

# We will define a generator function for each athlete returning 30 tuples:
# (title, hook, body, takeaway, asset_filename)

def get_tiger_blueprints():
    items = []
    # Wave 1: The Transition from Athlete to Ecosystem Architect (Posts 1-10)
    w1_concepts = [
        ("THE ECOSYSTEM BEYOND THE TROPHY",
         "When Tiger Woods dominated the Masters, he was perfecting his swing. When he founded TGR, he was designing a permanent ecosystem.",
         "Most athletes spend their prime trading physical energy for podium finishes. The greatest realize early that physical prime has an expiration date, but structural knowledge does not. Tiger did not just endorse golf clubs. He studied course architecture, retail operations, and event management. He understood that true sovereignty in sport means owning the infrastructure, not merely performing inside of it.",
         "As an Olympic coach for four decades, I tell leaders: mastery in your craft is only step one. Step two is building the platform that outlasts your personal participation.",
         "tiger-woods-01.png"),
        ("TURNING INTELLECT INTO PERMANENT ASSETS",
         "Tiger Woods understood that winning 15 majors gives you leverage. What you do with that leverage determines whether you are remembered as a player or an architect.",
         "Every time Tiger stepped onto a golf course, he was gathering data on player psychology, spectator movement, course aesthetics, and commercial real estate. Through TGR Design, he transformed decades of technical course knowledge into an architectural firm that shapes communities worldwide. He turned fleeting athletic glory into tangible, appreciating property.",
         "In my work with executive teams, I ask one question: are you capturing the intellectual property of your daily victories, or are you letting that wisdom dissipate once the project ends?",
         "tiger-woods-02.png"),
        ("DISCIPLINE IN THE BOARDROOM",
         "The same ice-water patience that Tiger used over a championship putt on Sunday afternoon is the patience required in multi-decade investments.",
         "People think business discipline is different from athletic discipline. It is identical. It requires emotional regulation when markets fluctuate, relentless preparation before negotiations, and the ability to execute without emotion. Tiger brought his Sunday-red focus into boardroom partnerships, vetting partners with the same ruthless precision he applied to his golf bag.",
         "Execution is not an accident. It is a repeatable habit built through decades of quiet, unglamorous reps.",
         "tiger-woods-03.png"),
        ("BUILDING BEYOND SELF-INTEREST",
         "At the height of his career, Tiger made a conscious pivot. He looked past personal wealth and created the TGR Foundation.",
         "Many foundations are public relations vehicles. Tiger engineered his foundation as an operational engine for STEM education and college access. When you look at the TGR Learning Labs in Anaheim and Washington, you see high-tech classrooms, robotics labs, and college counseling centers. He understood that true legacy is measured by the opportunities you engineer for those who have never held a golf club.",
         "Championship caliber is defined by how wide you open the door behind you once you have reached the pinnacle.",
         "tiger-woods-04.png"),
        ("THE COURAGE TO REBUILD YOUR SWING",
         "In 2000, Tiger Woods held all four major trophies simultaneously. Then he voluntarily dismantled his swing to build a better one.",
         "Corporate executives rarely possess that level of courage. When companies are profitable, leadership clings to existing playbooks until disruption forces their hand. Tiger understood that peak performance today does not guarantee survival tomorrow. He tore down his mechanics at the height of his fame because he was chasing longevity, not comfort.",
         "If you want to dominate your industry for decades, you must be willing to disrupt your own winning formula before the market does it for you.",
         "tiger-woods-05.png"),
        ("THE ARCHITECTURE OF AN AMBITIOUS VISION",
         "Tiger Woods did not wait for retirement to envision his next chapter. He was laying foundations while holding the number one ranking.",
         "Athletic transition fails when athletes wait until the final whistle to wonder what comes next. Tiger surrounded himself with seasoned business advisors while he was still winning PGA Tour events. He studied enterprise governance, contract structuring, and brand equity. When physical injuries mounted, his enterprise did not stall. It accelerated.",
         "Preparation is your strongest armor against transition anxiety. Begin building your second act while your first act is at its peak.",
         "tiger-woods-01.png"),
        ("STANDARDS DO NOT NEGOTIATE",
         "Watch how Tiger manages his course designs. He walks the dirt. He tests the green speeds. He scrutinizes every bunker placement.",
         "Delegation is essential for scale, but abdication is fatal. Tiger lends his name to nothing that does not meet his personal standard of excellence. In an era where athletes license their likenesses indiscriminately, Tiger curated his brand with monastic restraint. Every enterprise bearing the TGR mark reflects his personal work ethic.",
         "Your reputation is your highest-yielding currency. Protect it by holding every product and partnership to an uncompromising standard.",
         "tiger-woods-02.png"),
        ("RESILIENCE AS A STRATEGIC CAPABILITY",
         "Spinal fusion surgery. Five knee surgeries. Public crises. Tiger Woods was written off by every sports analyst on television.",
         "Then came the 2019 Masters. What the world saw on that Sunday was not just a comeback victory. It was a masterclass in psychological resilience, pain management, and emotional poise. In my Olympic coaching career, I watched champions break when circumstances changed. Tiger proved that resilience is not a personality trait. It is a daily decision to keep showing up.",
         "When setback strikes your organization, do not ask why it happened. Ask what systems you must build to rise above it.",
         "tiger-woods-03.png"),
        ("THE TGR LEARNING LABS PHILOSOPHY",
         "Over two million students have walked through the doors of the TGR Learning Labs. That is Tiger's greatest scorecard.",
         "In high-poverty communities, talent is everywhere, but opportunity is scarce. Tiger engineered a curriculum focused on marine biology, biomedical engineering, graphic design, and robotics. He gave young minds the technical tools to compete in modern economies. That is structural philanthropy: solving root challenges rather than offering temporary relief.",
         "If your wealth creation does not create upward mobility for the next generation, you have built wealth, but you have not built a legacy.",
         "tiger-woods-04.png"),
        ("FROM PHENOM TO INSTITUTION",
         "Tiger began as a child prodigy on national television. Today, he is an enduring American institution.",
         "That transition did not happen by chance. It required an intentional shift in identity. Tiger had to let go of being merely an athlete and embrace being an enterprise steward. In my executive coaching work, the hardest shift leaders make is stepping away from individual execution to institutional stewardship.",
         "You cannot scale what depends entirely on your personal presence. Build systems that succeed whether you are in the room or not.",
         "tiger-woods-05.png"),
    ]

    # Wave 2: Education, Access & Enterprise Systems (Posts 11-20)
    w2_concepts = [
        ("THE VALUE OF INTELLECTUAL SOVEREIGNTY",
         "Tiger Woods never permitted outside entities to dictate the core values of his enterprise. He maintained equity and creative control.",
         "In corporate deal-making, many founders surrender control for short-term capital. Tiger structured partnerships where his vision remained paramount. Whether partnering in hospitality ventures or course development, he insisted on governance rights. He understood that true wealth is not the size of your paycheck, but the degree of your autonomy.",
         "Control over your vision is priceless. Never sacrifice long-term governance for short-term liquidity.",
         "tiger-woods-01.png"),
        ("THE POWER OF UNCOMPROMISING PREPARATION",
         "Long before the gallery arrived at sunrise, Tiger was already sweating through practice sessions in the dark.",
         "The public only celebrates the final round trophy. They do not see the thousand hours of silent, tedious repetition in the gym and on the putting green. In corporate leadership, deals are won in the research phase, not during the pitch. When you prepare so thoroughly that doubt has no oxygen to survive, execution becomes second nature.",
         "Confidence is not bravado. Confidence is the earned byproduct of exhaustive, disciplined preparation.",
         "tiger-woods-02.png"),
        ("NAVIGATING CRISIS WITH EMOTIONAL REGULATION",
         "When pressure reaches suffocating levels, the amateur reacts with panic. The master slows their breathing and narrows their focus.",
         "I have coached athletes at the Olympic Games when the entire country was watching. The difference between a gold medal and heartbreak is often two seconds of emotional composure. Tiger mastered the art of walking between shots with absolute neutrality, conserving cognitive energy for the moments that matter.",
         "Leaders who cannot regulate their emotions under pressure will inevitably infect their entire team with chaos.",
         "tiger-woods-03.png"),
        ("INVESTING IN NEXT-GENERATION TALENT",
         "Through the Earl Woods Scholar Program, Tiger created a 98 percent graduation rate among first-generation college students.",
         "This was not accomplished by simply writing scholarship checks. It was accomplished through mentorship, internship placements, and emotional support networks. Tiger realized that money without mentorship leaves young talent vulnerable. He built a human support system around every scholar.",
         "Great leadership is not measured by how many followers you attract, but by how many leaders you cultivate.",
         "tiger-woods-04.png"),
        ("STRATEGIC ALLIANCES THAT EXPAND HORIZONS",
         "Tiger's partnership with luxury hospitality and entertainment brands showcases the art of high-caliber joint ventures.",
         "When scaling an enterprise, choosing the right partner is more important than choosing the fastest opportunity. Tiger aligned with partners who shared his obsession with quality and durability. They created immersive environments where sports, dining, and technology intersect seamlessly.",
         "Alignment of values must precede any conversation about alignment of profits.",
         "tiger-woods-05.png"),
        ("THE ART OF THE SECOND CAREER",
         "Most athletes grieve when their physical dominance wanes. Tiger leaned forward into the intellectual challenge of enterprise building.",
         "Transition is painful only when you define yourself solely by your past achievements. Tiger defined himself by his curiosity, his strategic instincts, and his commitment to excellence. When you view every career milestone as a foundation rather than a finish line, transition becomes a promotion, not an ending.",
         "Do not cling to titles you have outgrown. Step boldly into the arena your experience has prepared you to conquer.",
         "tiger-woods-01.png"),
        ("CREATING PERMANENT FOOTPRINTS IN COMMUNITIES",
         "A championship banner hangs in an arena until someone takes it down. A learning lab educates children for generations.",
         "Tiger recognized that the most enduring footprint an athlete can leave is physical and educational infrastructure. Buildings where children learn coding, design thinking, and environmental science create ripples across families that no trophy case can rival.",
         "Shift your focus from vanity metrics to generational infrastructure.",
         "tiger-woods-02.png"),
        ("PRECISION IN CAPITAL DEPLOYMENT",
         "Tiger does not scatter his capital across dozens of trendy ventures. He concentrates resources in domains he deeply understands.",
         "The downfall of many high-earning professionals is diversification into areas where they possess zero operational insight. Tiger stayed close to sports, leisure, hospitality, and educational technology. He deployed capital where his brand and insight provided an insurmountable competitive advantage.",
         "Invest where your domain expertise protects you from foolish assumptions.",
         "tiger-woods-03.png"),
        ("CULTIVATING CHAMPION HABITS DAILY",
         "Championship performance is not an act you perform on game day. It is an operating system running twenty-four hours a day.",
         "Tiger's daily routine during his prime was legendary: five-mile run at dawn, four hours of range work, two hours of short game, gym session, and evening practice. That level of rigor is terrifying to the undisciplined, but to the committed, it is the only path to immortality.",
         "You cannot demand excellence from your team while living in compromise yourself. Set the standard with your own calendar.",
         "tiger-woods-04.png"),
        ("THE MEASURE OF TRUE VICTORY",
         "When history writes the definitive book on Tiger Woods, the chapters on golf will be glorious, but the chapters on human impact will endure.",
         "Medals collect dust. Records are eventually broken. But the thousands of young people who became engineers, doctors, and community leaders because of the TGR Foundation will continue shaping the world long after our names are forgotten.",
         "Live your life and build your business with eternity in mind, not just the next fiscal quarter.",
         "tiger-woods-05.png"),
    ]

    # Wave 3: Generational Impact, Capital Discipline & Longevity (Posts 21-30)
    w3_concepts = [
        ("THE SOVEREIGN MINDSET IN MODERN SPORT",
         "Tiger Woods demonstrated that athletes are not commodities to be bought and sold. They are sovereign economic forces.",
         "He shifted the power dynamic between players and sanctioning bodies, proving that the value of the spectacle resides with the creators of excellence. Today's business leaders must recognize that talent retention requires respecting sovereignty and creating shared equity, not merely offering compensation.",
         "When talent understands its worth, leadership must offer partnership, not command-and-control.",
         "tiger-woods-01.png"),
        ("BUILDING INFRASTRUCTURE FOR THE UNSEEN",
         "The greatness of TGR Design lies in making courses that test the elite while welcoming the amateur.",
         "In business product design, this is the Holy Grail: creating solutions that possess institutional depth while remaining accessible and intuitive to the newcomer. Tiger's philosophy is rooted in removing friction so that more people can experience the beauty of the game.",
         "Simplicity on the surface backed by sophisticated architecture underneath is the hallmark of great product design.",
         "tiger-woods-02.png"),
        ("HOW PRESSURE REVEALS FAULT LINES",
         "Put an ordinary player under major championship pressure, and their flaws are instantly magnified. Put Tiger under pressure, and his fundamentals solidify.",
         "Pressure does not create character; it reveals preparation. In corporate crisis management, organizations collapse not because the crisis was novel, but because their internal communication systems and standard operating procedures were fragile.",
         "Stress-test your operational systems during calm seasons so they hold firm during the storm.",
         "tiger-woods-03.png"),
        ("ELEVATING THE CONVERSATION ABOUT ATHLETE EQUITY",
         "Tiger paved the way for every multi-million-dollar athletic brand deal in existence today.",
         "Before Tiger, golfers wore modest logos and earned modest prize money. Tiger elevated the entire financial ecosystem of golf, raising purses for every competitor on the tour. That is the definition of abundance leadership: lifting the floor for everyone while setting a new ceiling.",
         "A true leader does not compete for a bigger slice of the pie. They bake a larger pie for the entire industry.",
         "tiger-woods-04.png"),
        ("THE DISCIPLINE OF SAYING NO",
         "For every business opportunity Tiger accepted, he declined fifty others.",
         "The greatest threat to a prestigious brand is dilution. When you are successful, opportunities flood your desk daily. The ability to reject lucrative offers that dilute your core purpose is the rarest skill in executive leadership.",
         "Focus is not about what you say yes to. Focus is defined by the profitable temptations you have the strength to reject.",
         "tiger-woods-05.png"),
        ("TURNING PHYSICAL PAIN INTO PURPOSEFUL SYSTEMS",
         "When back injuries threatened to end Tiger's career, he channeled his energy into expanding his business footprint.",
         "Physical limitations often force mental evolution. When you cannot rely solely on brute force or personal hours, you are forced to build systems, empower teams, and delegate authority. Tiger's enterprise grew stronger because he could not do everything himself.",
         "Let your constraints force you into higher levels of operational sophistication.",
         "tiger-woods-01.png"),
        ("LEGACY IS AN EVERYDAY CONSTRUCTION SITE",
         "You do not inherit a legacy; you construct it with every email, every contract, and every interaction.",
         "Tiger's legacy is active. He is designing courses, mentoring his son Charlie, guiding the PGA Tour through tectonic commercial shifts, and funding educational laboratories. He remains an active builder, not a ceremonial relic.",
         "Never settle into retirement mindset while your mind is still sharp and your hands can still build.",
         "tiger-woods-02.png"),
        ("THE LESSON OF SUNDAY AT AUGUSTA",
         "In 2019, when Tiger walked off the 18th green at Augusta with his children waiting, it was not about validation. It was about demonstration.",
         "He wanted his children to see that setbacks, mistakes, and surgeries do not have the final word in a human life. What you demonstrate through your recovery is infinitely more powerful than what you preach in your victories.",
         "Your greatest leadership lesson to your team is how you handle your darkest setbacks.",
         "tiger-woods-03.png"),
        ("MASTERING THE ART OF TIMING",
         "In golf, tempo is everything. A swing rushed by two milliseconds ends up in the trees. In corporate acquisitions, tempo is equally decisive.",
         "Tiger never rushed the expansion of TGR. He waited until the foundational team was seasoned, the brand was bulletproof, and the capital structure was clean. Moving fast is overrated; moving with precision and impeccable timing is what wins.",
         "Do not confuse activity with progress. Move when the strategic advantage is entirely in your favor.",
         "tiger-woods-04.png"),
        ("THE ARCHITECT'S FINAL SCORECARD",
         "When all the trophies are cataloged and the records stand in bronze, Tiger's true victory will be the generation of leaders who walked through his learning labs.",
         "That is the shift from champion to owner, and from owner to builder of humanity. That is the highest calling of athletic success. That is what I have spent forty years teaching Olympic hopefuls and corporate CEOs alike.",
         "Build something that continues serving people long after you have walked off the field.",
         "tiger-woods-05.png"),
    ]

    for c in w1_concepts + w2_concepts + w3_concepts:
        items.append(c)
    assert len(items) == 30, f"Tiger items must be 30, got {len(items)}"
    return items

def get_stephen_blueprints():
    items = []
    # Stephen Curry: Underrated Golf & Opening Doors
    concepts = [
        ("CHANGING WHO GETS TO PLAY THE GAME",
         "Stephen Curry did not need to play professional golf to change who gets to compete in it.",
         "Golf has historically been one of the most closed ecosystems in sport, guarded by private club fees, expensive equipment, and country club networks. Steph recognized that athletic talent is universal, but access to competitive circuits is fiercely restricted. He launched Underrated Golf not as a casual celebrity tournament, but as an elite junior tour providing all-expenses-paid travel, equipment, and ranking opportunities for young players.",
         "True innovation is not just creating a new product. It is dismantling artificial barriers to entry so exceptional talent can rise on merit.",
         "stephen-curry-01.png"),
        ("REWRITING THE JUNIOR PIPELINE",
         "Underrated Golf is not just about swinging clubs. It is about building a college recruiting pipeline that scouts cannot ignore.",
         "Junior golf requires thousands of dollars in tournament fees and travel just to get ranked in front of NCAA Division I coaches. Steph understood that without tournament visibility, young athletes from working-class backgrounds never get scholarship offers. Underrated Golf brings the college coaches directly to the players, bridging the scouting divide.",
         "In executive hiring, if your recruiting pipeline only fishes in the same elite waters, you are systematically overlooking the hungriest talent.",
         "stephen-curry-02.png"),
        ("PAIRING SPORT WITH CORPORATE BOARDROOM ACCESS",
         "At every Underrated Golf tour stop, junior players spend half their time in leadership workshops with Fortune 500 executives.",
         "Steph understands that only a percentage of junior golfers will reach the PGA or LPGA Tour. But every single one of them can become a corporate executive, an entrepreneur, or an institutional leader. He uses the golf course as a networking accelerator, teaching young athletes how to converse with CEOs, pitch ideas, and navigate corporate culture.",
         "Sport is a vehicle, not the final destination. Use athletic discipline to unlock intellectual and economic sovereignty.",
         "stephen-curry-03.png"),
        ("THE DISCIPLINE OF EXPANDING YOUR HORIZONS",
         "Steph Curry is already a four-time NBA champion and Olympic gold medalist. Why spend capital building a golf ecosystem?",
         "Because a champion's mind refuses to stay confined to a single arena. Steph recognized that his platform as a basketball superstar gave him unique cultural leverage to democratize a completely different sport. He leveraged his corporate relationships with brands like Callaway and KPMG to fund a vision that transforms lives.",
         "Do not allow your current title to box in your potential. Use your existing credibility to solve problems across new industries.",
         "stephen-curry-04.png"),
        ("ELIMINATING THE HIDDEN FINANCIAL TAX ON TALENT",
         "Talent does not disappear when a family cannot afford five thousand dollars for tournament travel. It simply gets starved of opportunity.",
         "When Underrated Golf covers flights, lodging, meals, and greens fees for student athletes and their parents, it levels the competitive playing field. Suddenly, the kid from an inner-city public course can stand on the same tee box as the kid with a private swing coach and country club membership.",
         "When you remove financial friction, meritocracy finally functions as promised.",
         "stephen-curry-05.png"),
        ("GLOBAL EXPANSION WITH REGAL PURPOSE",
         "Underrated Golf did not stay in the United States. Steph took the tour to historic venues like Walton Heath in the United Kingdom.",
         "By taking young American golfers overseas to compete alongside top European junior talent, Steph expanded their worldview. He taught them that athletic excellence and cultural poise have no geographic borders. Playing links golf in England changes a young person's concept of what is possible in their life.",
         "Expose your emerging talent to global environments early. World-class exposure creates world-class expectations.",
         "stephen-curry-01.png"),
        ("THE LESSON OF THE UNDERRATED MINDSET",
         "Remember where Steph Curry started: a three-star recruit with no major scholarship offers, deemed too small to play high-major basketball.",
         "The 'Underrated' brand is not a marketing gimmick; it is Steph's autobiography. He built his entire career on being overlooked and outworking the pedigree players. When he looks at junior golfers who lack institutional backing, he sees himself at sixteen years old. That empathy is the secret engine of his philanthropy.",
         "Your greatest business breakthroughs will often emerge directly from the pain and rejection of your early career.",
         "stephen-curry-02.png"),
        ("CREATING PATHWAYS TO THE PROFESSIONAL RANKS",
         "Underrated Golf is already producing players competing in USGA championships and earning collegiate scholarships.",
         "Proof of concept is everything in business and sport. Steph did not just create feel-good press releases. He measured outcomes: how many tournament invitations, how many college commitments, and how many handicap reductions. That operational rigor is what separates enduring programs from vanity projects.",
         "Hold your philanthropic initiatives to the same rigorous KPIs that govern your revenue-generating business units.",
         "stephen-curry-03.png"),
        ("THE ROLE OF CORPORATE COALITIONS",
         "Steph did not fund Underrated Golf alone. He assembled a coalition of corporate heavyweights who put skin in the game.",
         "He brought in enterprise partners who committed not just sponsor checks, but executive mentorship, career internships, and equipment technology. Steph showed corporations that supporting equity in golf is not charity; it is an investment in the future leaders of their own companies.",
         "Strategic coalitions multiply your impact. Rally partners around a shared mission where everyone has an authentic stake.",
         "stephen-curry-04.png"),
        ("TEACHING POISE UNDER PRESSURE ON THE GREENS",
         "Golf is the most psychologically demanding individual sport in the world. Steph uses it to teach emotional regulation.",
         "In basketball, you can run off frustration on defense. In golf, you have five minutes to walk in complete silence to your ball after hitting a terrible drive. That requires Olympic-level emotional mastery. Steph is equipping these young athletes with psychological tools that will serve them in boardrooms for the next fifty years.",
         "Teach your emerging leaders how to manage the silent minutes between their mistakes and their next decisions.",
         "stephen-curry-05.png"),
        # Wave 2 (11-20)
        ("A CULTURE OF MUTUAL ACCOUNTABILITY",
         "Watch the culture Steph builds among his junior golfers: competition on the course, brotherhood and sisterhood off the course.",
         "He demands that every participant conduct themselves with dignity, dress impeccably, respect tournament staff, and support their competitors. In an era of toxic online posturing, Steph is reviving the noble traditions of sportsmanship and mutual respect.",
         "Culture is not what you write on the wall. Culture is the standard of behavior you enforce every single day.",
         "stephen-curry-01.png"),
        ("REDEFINING THE GOLF AESTHETIC",
         "Steph brought youthful energy, contemporary fashion, and cultural relevance to a game often viewed as stuffy and elitist.",
         "By introducing modern apparel lines and vibrant music into practice rounds, Underrated Golf made the game appealing to a new generation without compromising respect for golf's timeless etiquette. He modernized the wrapper while preserving the core integrity of the sport.",
         "You do not have to abandon timeless fundamentals to make your brand resonate with modern audiences.",
         "stephen-curry-02.png"),
        ("THE VALUE OF INTENTIONAL SPONSORSHIP",
         "When Steph Curry puts his personal capital behind Howard University's golf program, he isn't just writing checks. He is reviving history.",
         "He funded the relaunch of the men's and women's golf teams at an iconic HBCU, providing six years of financial backing. He understood that representation at the collegiate level inspires thousands of middle school and high school athletes to keep swinging.",
         "Target your capital where it creates systemic, institutional revival rather than fleeting social media applause.",
         "stephen-curry-03.png"),
        ("THE ART OF UNSELFISH LEADERSHIP",
         "Steph Curry's signature on the basketball court is his off-ball movement. He runs constantly to create open shots for his teammates.",
         "That exact philosophy governs his business endeavors. He does not need his face on every banner. He creates the open lane, passes the ball, and celebrates when young golfers sink life-changing putts. Unselfish leadership is the rarest competitive advantage in modern enterprise.",
         "The most influential leaders are not those who hoard the spotlight, but those whose movement creates room for others to shine.",
         "stephen-curry-04.png"),
        ("MENTAL TOUGHNESS ON THE BACK NINE",
         "In championship golf, the tournament does not begin until the back nine on Sunday. That is where mental fatigue tests your character.",
         "Steph teaches young athletes that fatigue is an emotion, not a physical mandate. When your legs are tired and pressure mounts, your routine must become your sanctuary. Having coached Olympic athletes through the most grueling medal rounds, I know that routine is what protects talent from panic.",
         "Under severe pressure, you do not rise to the occasion. You sink to the level of your training and daily routines.",
         "stephen-curry-05.png"),
        ("THE POWER OF VISIBILITY AND ROLE MODELS",
         "You cannot dream of being what you cannot see.",
         "When a young girl from an underserved community sees Steph Curry walking alongside her on the fairway, giving her swing tips, her ceiling of expectation shatters permanently. She no longer wonders if she belongs in elite golf; she knows she does.",
         "Your presence in the lives of emerging leaders speaks ten times louder than any piece of advice you will ever give.",
         "stephen-curry-01.png"),
        ("LESSONS IN STRATEGIC PATIENCE",
         "Golf rewards the strategist, not the reckless attacker. Steph's golf tour teaches young players how to manage course risks.",
         "Taking a double bogey because you tried a hero shot from the trees is a failure of discipline, not skill. Steph's coaches teach course management: take your medicine, punch out to the fairway, save bogey, and play the long game. That is identical to executive capital management.",
         "Avoid the temptation of hero maneuvers when a disciplined, steady play preserves your strategic capital.",
         "stephen-curry-02.png"),
        ("BUILDING BRIDGES ACROSS GENERATIONS",
         "Steph regularly connects Underrated Golf participants with legendary senior players and PGA Tour veterans.",
         "He bridges the wisdom of the past with the dynamism of the future. Cross-generational mentorship accelerates learning curves by decades, saving young people from repeating the painful mistakes of their predecessors.",
         "Surround your young high-potentials with seasoned veterans who have already navigated the minefields.",
         "stephen-curry-03.png"),
        ("THE BUSINESS LESSON OF THE LONG DRIVE",
         "Everyone loves watching a 350-yard drive, but tournaments are won inside of 100 yards with wedge play and putting.",
         "In business, flashy launches attract headlines, but operational execution, customer retention, and unit economics are what generate lasting profits. Steph teaches junior golfers to fall in love with the dull, repetitive short-game practice that casual players neglect.",
         "Fall in love with the mundane details that amateur competitors consider boring. That is where the margin of victory lives.",
         "stephen-curry-04.png"),
        ("THE CURRY LEGACY BLUEPRINT",
         "Steph's legacy will be far wider than four championship rings. It will include hundreds of college graduates who got their degrees through golf.",
         "That is how an athlete transforms cultural capital into generational equity. He is not merely entertaining audiences on television; he is systematically rewiring the economic trajectory of families across the globe.",
         "Ask yourself: will your business metrics matter in thirty years, or are you building something that changes family lineages?",
         "stephen-curry-05.png"),
        # Wave 3 (21-30)
        ("ELEVATING THE STANDARD OF EQUALITY",
         "Underrated Golf treats male and female athletes with equal investment, equal prize opportunities, and equal prestige.",
         "From day one, Steph insisted that the women's division receives the exact same tournament venues, media coverage, and corporate introductions as the men. He rejected the traditional sports hierarchy that treats female athletics as an afterthought.",
         "True equity is not lip service; it is an identical allocation of budget, attention, and executive sponsorship.",
         "stephen-curry-01.png"),
        ("THE HUMILITY TO BE A STUDENT OF GOLF",
         "Despite being an elite basketball genius, Steph approached golf with the humility of a beginner.",
         "He spent hours asking questions, studying swing mechanics from world-class instructors, and accepting that greatness in one field does not automatically transfer to another. That humility is what allowed him to build credibility within the golf establishment.",
         "Never let mastery in your primary domain convince you that you have nothing left to learn in new arenas.",
         "stephen-curry-02.png"),
        ("INVESTING IN PARENTAL AND FAMILY SUPPORT",
         "Junior sports can strain family finances and relationships. Underrated Golf supports the parents as much as the players.",
         "Steph provides hospitality, educational workshops on college compliance, and travel stipends for parents. He recognizes that behind every resilient junior athlete is a family sacrificing hours and resources to make dreams possible.",
         "When developing high-potential leaders, support the ecosystem that sustains them when they leave your office.",
         "stephen-curry-03.png"),
        ("LEVERAGING ENTERPRISE PARTNERSHIPS FOR SOCIAL GOOD",
         "Steph turned corporate brand deals from vanity endorsements into social impact alliances.",
         "Every corporate partner who signs with Curry Brand or Thirty Ink must commit resources to community initiatives like Underrated Golf. He made social responsibility a non-negotiable term of commercial engagement.",
         "Do not just ask what a partner will pay you. Ask what problems they are willing to solve alongside you.",
         "stephen-curry-04.png"),
        ("TEACHING POST-COMPETITION PERSPECTIVE",
         "When a junior golfer misses a cut or cards an 82, Steph's coaches do not treat it as a tragedy. They treat it as curriculum.",
         "As an Olympic coach, I have seen young athletes tie their entire self-worth to a scoreboard. Steph teaches them that your score reflects your golf game today, not your value as a human being. That psychological separation is what prevents burnout and despair.",
         "Never confuse your performance with your identity. You are always greater than your latest quarterly results.",
         "stephen-curry-05.png"),
        ("CREATING MEMORABLE RITUALS OF EXCELLENCE",
         "From custom tour bags to professional caddie access, Underrated Golf treats every participant like a tour pro.",
         "When you elevate an environment, people naturally elevate their behavior to match it. When young players see their names on leaderboards and receive professional-grade equipment, they stop viewing themselves as underdogs and begin carrying themselves as contenders.",
         "Design environments that communicate dignity and high expectations. Your people will rise to meet them.",
         "stephen-curry-01.png"),
        ("NAVIGATING SKEPTICISM WITH QUIET COMPETENCE",
         "When a basketball player announced he was launching a national golf tour, traditionalists were openly skeptical.",
         "Steph did not engage in public arguments. He simply executed five-star tournaments, secured top-tier courses, and let the quality of the competition silence every critic. Quiet competence is always the most devastating response to skepticism.",
         "Do not waste energy arguing with doubters. Build something so exceptional that its existence renders their arguments obsolete.",
         "stephen-curry-02.png"),
        ("THE DISCIPLINE OF CONSISTENCY OVER TIME",
         "Launching a tour is easy; sustaining it across multiple seasons requires relentless operational commitment.",
         "Steph has expanded Underrated Golf year after year, adding European stops, increasing corporate funding, and growing participant counts. Consistency is the true differentiator between a passing vanity fad and an enduring institution.",
         "Brilliance without consistency is meaningless. Show up with the same rigor on rainy Tuesdays that you bring to opening day.",
         "stephen-curry-03.png"),
        ("INSPIRING A GENERATION OF UNCONVENTIONAL CHAMPIONS",
         "The faces on the Underrated Golf leaderboards do not look like traditional country club rosters, and that is precisely the victory.",
         "Young Black, Hispanic, and Asian junior golfers are walking fairways that their grandparents were not allowed to enter. Steph used his stardom to rewrite the cultural DNA of an entire sport. That is the highest manifestation of athletic influence.",
         "Use your seat at the table to expand the guest list, not to pull up the ladder.",
         "stephen-curry-04.png"),
        ("THE SCORECARD THAT NEVER FADES",
         "Steph Curry has made hundreds of millions of dollars and scored thousands of three-pointers, but Underrated Golf is his timeless masterpiece.",
         "Every time a young girl from an underserved zip code earns a college scholarship through this tour, Steph's legacy expands into eternity. That is what it means to own the next chapter. That is the standard of leadership I challenge every CEO and founder to pursue.",
         "Make your next chapter the one where your success becomes someone else's breakthrough.",
         "stephen-curry-05.png"),
    ]
    assert len(concepts) == 30, f"Steph items must be 30, got {len(concepts)}"
    return concepts

def get_ayesha_blueprints():
    items = []
    # Ayesha Curry: Sweet July, Food, Media, Premium Hospitality (10 assets cycled 3 times = 30 posts)
    concepts = [
        ("TURNING TASTE INTO A DESTINATION",
         "Sweet July Cafe brings Ayesha Curry's food and lifestyle vision into premium hospitality.",
         "Ayesha did not wait for approval to build an empire. She took her intuitive love for food, design, and gathering, and translated it into Sweet July: a luxury lifestyle brand, magazine, and flagship cafe destination. She proved that hospitality is not merely serving coffee; it is curating an atmosphere where community, elegance, and warmth coexist seamlessly.",
         "In business, you do not just sell a service. You sell the feeling and identity of the environment you create.",
         "ayesha-curry-01.png"),
        ("THE ART OF AUTHENTIC BRAND ARCHITECTURE",
         "Ayesha did not license her name to an existing restaurant chain. She built Sweet July from the soil up.",
         "When you build your own brand, you own the creative vision, the supply chain, and the customer experience. Ayesha selected every artisanal product, curated local Black-owned vendors, and designed a retail footprint that reflects her personal aesthetic. That authenticity is why her brand commands fierce customer loyalty.",
         "Never outsource your soul for rapid scale. Build an enterprise whose every detail reflects your core values.",
         "ayesha-curry-02.png"),
        ("CREATING SPACES WHERE WOMEN GATHER AND THRIVE",
         "Sweet July was created as a sanctuary for women to pause, recharge, and celebrate life's sweeter moments.",
         "Modern women navigate overwhelming professional and personal demands. Ayesha recognized the profound need for hospitality spaces that prioritize tranquility, beauty, and emotional rejuvenation. Sweet July is not just a cafe; it is a community anchor that honors the feminine journey.",
         "When your business solves an emotional and relational need, customer retention takes care of itself.",
         "ayesha-curry-03.png"),
        ("THE COURAGE TO STEP INTO YOUR OWN LIGHT",
         "Standing next to a global sports icon can easily overshadow your personal ambitions. Ayesha chose to forge her own distinct legacy.",
         "She carved out her own identity as a New York Times bestselling author, television host, culinary entrepreneur, and venture investor. She proved that partnership in marriage does not require sacrificing individual enterprise. Her voice, her brand, and her commercial ventures stand proudly on their own merit.",
         "Never dim your personal brilliance to fit into someone else's orbit. Step boldly into the work you were born to build.",
         "ayesha-curry-04.png"),
        ("THE RIGOR OF CULINARY EXCELLENCE",
         "Food is one of the most unforgiving industries in the world. Passion gets you started, but operational rigor keeps the doors open.",
         "Ayesha spent years testing recipes, studying food chemistry, understanding labor margins, and mastering culinary logistics. Long before International Smoke and Sweet July became commercial successes, she was doing the unglamorous prep work in commercial kitchens. Excellence in hospitality requires an obsession with consistency.",
         "Do not expect applause for half-baked execution. Master the operational mechanics of your trade before scaling.",
         "ayesha-curry-05.png"),
        ("SUPPORTING EMERGING ENTREPRENEURS ON HER SHELVES",
         "Walk through a Sweet July flagship store and look at the retail shelves. You will see products from underrepresented female founders.",
         "Ayesha uses her retail distribution to elevate female artisans, skincare creators, and culinary makers who would otherwise struggle to access premium shelf space. She turned her brand into a launchpad for other women. That is true economic sisterhood in action.",
         "When you build a premier platform, turn your distribution into an elevator for emerging talent.",
         "ayesha-curry-06.png"),
        ("THE EXPANSION INTO LUXURY HOSPITALITY DESTINATIONS",
         "Sweet July is not confined to Oakland. Ayesha expanded the concept into premier resort destinations like Grand Cayman.",
         "Taking a lifestyle brand from a local flagship to an international luxury resort requires sophisticated operational systems and brand consistency. Ayesha proved that her aesthetic translates across global markets, appealing to discerning travelers who value authentic Caribbean and lifestyle storytelling.",
         "Do not underestimate the global appetite for authentic, culturally rich luxury experiences.",
         "ayesha-curry-07.png"),
        ("BALANCING MOTHERHOOD, ENTERPRISE, AND PURPOSE",
         "Four children, multiple restaurants, a media company, and a foundation. Ayesha dispels the myth of effortless perfection.",
         "She speaks openly about the grueling discipline of time management, the necessity of delegation, and the non-negotiable boundaries required to protect family life. In my coaching with executive women, I emphasize that balance is not a static state; it is dynamic prioritization built on crystal-clear values.",
         "You cannot do everything alone. Build a trusted operational team that executes your standards with precision.",
         "ayesha-curry-08.png"),
        ("THE POWER OF MEDIA STORYTELLING",
         "Sweet July is not just physical stores; it is a full media company publishing lifestyle magazines and digital content.",
         "Ayesha understood that content drives commerce, and commerce sustains content. By controlling her own media narrative, she tells stories of resilience, food heritage, wellness, and self-care on her own terms, completely independent of traditional publishing gatekeepers.",
         "Own your media channel. When you own the storytelling engine, you dictate how your value is communicated to the world.",
         "ayesha-curry-09.png"),
        ("THE PHILOSOPHY OF THE SWEET JULY MOMENT",
         "The name 'Sweet July' was inspired by the month where all of Ayesha's children were born, and where she married Steph.",
         "It represents that window of life where everything aligns, where gratitude overflows, and where joy is celebrated without reservation. Ayesha translated a deeply personal emotional anchor into a commercial universe that invites every customer to experience that same sense of warmth and abundance.",
         "Infuse your enterprise with authentic personal meaning. Customers can feel when a brand has a genuine soul.",
         "ayesha-curry-10.png"),
        # Repeat cycle 2 with fresh angles (11-20)
        ("ELEVATING CARIBBEAN HERITAGE THROUGH MODERN CUISINE",
         "Ayesha's culinary vision celebrates her rich Jamaican, Chinese, and African-American roots.",
         "Rather than flattening her heritage to appeal to generic tastes, she leaned into bold flavors, island spices, and vibrant presentation. She showed that culinary heritage, when presented with luxury plating and hospitality, commands premium market appreciation.",
         "Your unique cultural background is your proprietary competitive edge. Never dilute what makes your perspective distinct.",
         "ayesha-curry-01.png"),
        ("INVESTING IN FEMALE FOUNDERS",
         "Through her Sweet July Skin line and angel investments, Ayesha directs capital directly to female-led businesses.",
         "Less than three percent of venture capital goes to female founders. Ayesha does not just complain about the statistic; she writes checks and opens retail doors. She understands that economic empowerment for women is the fastest way to stabilize families and revitalize communities.",
         "If you want to see change in your industry, deploy your capital where traditional gatekeepers refuse to look.",
         "ayesha-curry-02.png"),
        ("THE ART OF HIGH-TOUCH CUSTOMER EXPERIENCE",
         "Every touchpoint at Sweet July Cafe is engineered to evoke sensory delight: the aroma of bread pudding, the curated playlist, the warmth of the lighting.",
         "In a digital-first economy where everything is transactional, physical hospitality that provides sensory nourishment is a massive differentiator. Ayesha created a physical haven where customers do not feel rushed; they feel welcomed and cherished.",
         "Invest in sensory details. When your customer feels emotionally nourished, price sensitivity disappears.",
         "ayesha-curry-03.png"),
        ("THE STRENGTH OF EDITORIAL DISCIPLINE",
         "Look at the Sweet July lifestyle magazine: clean photography, intentional essays, recipes with soul.",
         "It does not chase clickbait or celebrity gossip. It celebrates quiet rituals of joy, entrepreneurial courage, and holistic wellbeing. Ayesha maintained editorial integrity in an era of media noise, building a publication that readers collect and preserve on coffee tables.",
         "Durability beats virality every single time. Create work that people want to keep, not just scroll past.",
         "ayesha-curry-04.png"),
        ("OVERCOMING PUBLIC SCRUTINY WITH CLASS",
         "When you build a business in the public eye, every misstep is dissected by critics. Ayesha responded with dignified silence and unrelenting execution.",
         "As an Olympic coach, I have seen athletes unravel because they let critics into their heads. Ayesha demonstrated that the best response to public noise is a five-star dining room, a thriving retail brand, and a growing community of loyal supporters.",
         "Never enter a debate with people who have never built an enterprise. Let your results deliver the verdict.",
         "ayesha-curry-05.png"),
        ("COMMUNITY ROOTEDNESS IN OAKLAND",
         "When Ayesha launched Sweet July, she chose Uptown Oakland, investing directly in the city that embraced her family.",
         "She did not take the concept straight to Beverly Hills or Manhattan. She planted her flag in Oakland, creating local jobs, contracting local builders, and establishing a beacon of luxury within the community. That rootedness generated immense civic pride and authentic neighborhood love.",
         "Invest in the communities that believed in you before you became a national headline.",
         "ayesha-curry-06.png"),
        ("THE METICULOUS FORMULATION OF SWEET JULY SKIN",
         "Ayesha did not simply private-label skincare products. She spent years researching Caribbean superfoods like guava, soursop, and papaya.",
         "She combined natural island remedies with clean clinical science, creating a skincare line that honors her ancestral beauty rituals while delivering dermatological results. That respect for craftsmanship is why the product line earned national accolades.",
         "Honor tradition while leveraging modern science. That intersection is where groundbreaking innovation lives.",
         "ayesha-curry-07.png"),
        ("CREATING JOINT VALUE WITHOUT ENMESHMENT",
         "Ayesha and Steph collaborate brilliantly, but they maintain distinct professional domains.",
         "Steph has Thirty Ink and Curry Brand; Ayesha has Sweet July and Sweet July Productions. They support each other's launches, but each operates with independent operational leadership and strategic clarity. This prevents personal friction and allows both enterprises to flourish.",
         "Clear boundaries strengthen partnerships. Ensure every collaborator has full sovereignty over their domain.",
         "ayesha-curry-08.png"),
        ("LEADERSHIP WITH INTENTIONAL KINDNESS",
         "Ayesha's leadership philosophy rejects the myth that high-performing kitchens must be abusive and chaotic.",
         "She fosters a culture of mutual respect, dignity, and calm communication across her cafes and culinary teams. Having worked in high-stress Olympic environments for decades, I know that fear breeds mistakes, while psychological safety unlocks creativity and sustained excellence.",
         "You do not need to be ruthless to demand excellence. High standards delivered with deep respect will inspire loyalty.",
         "ayesha-curry-09.png"),
        ("THE SWEET FRUIT OF RELENTLESS PERSEVERANCE",
         "From filming home cooking videos in a tiny kitchen to operating an international lifestyle hospitality empire.",
         "Ayesha's journey reminds every woman that small, faithful beginnings matter. You do not need a massive production studio to start; you need an authentic voice, a commitment to your craft, and the willingness to learn from every early failure.",
         "Start where you are, with what you have in your hands. Faithful daily execution will open doors you cannot yet see.",
         "ayesha-curry-10.png"),
        # Repeat cycle 3 (21-30)
        ("A MODERN MASTERCLASS IN FEMALE OWNERSHIP",
         "Ayesha Curry represents the new generation of female enterprise owners who refuse to be pigeonholed.",
         "She is simultaneously a mother, an author, a restaurateur, a beauty founder, and an executive producer. She shattered the outdated expectation that women must choose between domestic fulfillment and commercial ambition. She built an ecosystem that honors both.",
         "Refuse the false choices imposed by small minds. Build a life and a business that encompasses the full breadth of your calling.",
         "ayesha-curry-01.png"),
        ("DESIGNING EXPERIENCES THAT RESIST COMMODITIZATION",
         "Anyone can sell coffee beans. Very few can create a space where walking through the door feels like an exhale.",
         "Ayesha understood that the commodity is cheap, but the sanctuary is priceless. In an increasingly anxious and fragmented culture, spaces that provide peace, aesthetic order, and genuine warmth will always command a premium.",
         "Do not compete in the race to the bottom on price. Elevate the emotional experience until you are in a category of one.",
         "ayesha-curry-02.png"),
        ("THE DISCIPLINE OF SAYING NO TO EASY MONEY",
         "Ayesha has turned down countless fast-money endorsements that did not align with the Sweet July ethos.",
         "When you build a luxury brand, dilution is lethal. Ayesha protects the integrity of Sweet July with relentless vigilance. She understands that brand equity built over a decade can be destroyed in ten seconds by an off-brand partnership.",
         "Guarding your brand's integrity requires the discipline to walk away from deals that compromise your reputation.",
         "ayesha-curry-03.png"),
        ("THE SOUL OF HOSPITALITY IS LISTENING",
         "Great restaurateurs do not just watch the kitchen; they watch the faces of their guests.",
         "Ayesha studies customer reactions, reads feedback, and continuously refines menu items and retail selections. That humility to listen and adapt while holding the aesthetic line is the mark of a true hospitality visionary.",
         "Listen deeply to the people you serve. They will tell you exactly how to build an enduring enterprise.",
         "ayesha-curry-04.png"),
        ("CREATING PRODUCTS THAT TELL STORIES",
         "Every candle, every jar of honey, and every linen napkin in Sweet July has an intentional backstory.",
         "Consumers do not purchase objects; they purchase identity and narrative. When a customer takes home a Sweet July mug, they are taking home a reminder to savor their mornings and prioritize peace in their home.",
         "Wrap your products in narratives of meaning, heritage, and intentional living.",
         "ayesha-curry-05.png"),
        ("BUILDING BRIDGES BETWEEN CULINARY AND WELLNESS",
         "Ayesha recognizes that food, skincare, and mental health are intimately connected.",
         "Sweet July integrates culinary nutrition with topical skin wellness and mindful lifestyle routines. She created a 360-degree approach to wellbeing that treats the human being as a holistic ecosystem.",
         "Look across traditional industry silos. The most lucrative innovations occur at the intersections of disconnected domains.",
         "ayesha-curry-06.png"),
        ("THE ENDURANCE REQUIRED FOR MULTI-UNIT HOSPITALITY",
         "Opening store number two is harder than opening store number one. Scaling into luxury resorts requires flawless manuals.",
         "Ayesha translated her culinary intuition into standardized operating procedures, employee training modules, and brand style guides. That institutional documentation is what enables Sweet July to maintain its magic across geographies.",
         "If your business cannot run without your physical presence, you own a demanding job, not an enterprise. Build manuals.",
         "ayesha-curry-07.png"),
        ("LIFTING AS SHE CLIMBS",
         "Ayesha's retail ecosystem has generated millions in sales for independent, woman-owned small businesses.",
         "That is how wealth distribution ought to function. Rather than hoarding profits, she creates a pipeline where emerging female entrepreneurs gain credibility, exposure, and capital through her platform.",
         "Measure your enterprise success not just by your gross revenue, but by the commercial ecosystem you nurture around you.",
         "ayesha-curry-08.png"),
        ("GRACE UNDER THE BRIGHTEST LIGHTS",
         "Navigating corporate boardrooms, Hollywood studios, and family life requires immense emotional poise.",
         "Ayesha carries herself with an unmistakable grace: calm speech, thoughtful deliberation, and unshakeable conviction. In forty years of coaching, I have found that poise is the single most intimidating weapon a leader can wield against hostility.",
         "When the environment is chaotic, your calm is your greatest source of authority.",
         "ayesha-curry-09.png"),
        ("THE LEGACY OF A WOMAN WHO OWNED HER CHAPTER",
         "Ayesha Curry's story is a beacon for every woman who has ever questioned whether she has what it takes to build an empire.",
         "She took taste, turned it into a destination, turned that destination into a brand, and turned that brand into an enduring institution. That is what it means to own the next chapter. That is the standard of excellence I celebrate and teach every single day.",
         "Take ownership of your story today. Write the chapter that changes your life and your community.",
         "ayesha-curry-10.png"),
    ]
    assert len(concepts) == 30, f"Ayesha items must be 30, got {len(concepts)}"
    return concepts

def get_stephen_ayesha_blueprints():
    items = []
    # Stephen & Ayesha Curry: Eat.Learn.Play. Foundation (10 assets cycled 3 times = 30 posts)
    concepts = [
        ("THEY BUILT MORE THAN SUCCESS. THEY BUILT ACCESS.",
         "Through Eat.Learn.Play., Stephen and Ayesha Curry invest in meals, literacy, and safe places to play for Oakland kids.",
         "Success is what you achieve for yourself. Access is what you engineer for people who were never handed a fair start. Steph and Ayesha looked at the city of Oakland: a community that celebrated four NBA championships: and asked what they owed the children growing up in the shadows of the arena. They founded Eat.Learn.Play. not as a ceremonial check-writing hobby, but as an operational social enterprise.",
         "In my Olympic coaching journey, I learned that athletic greatness means nothing if it does not leave the community stronger than you found it.",
         "stephen-ayesha-01.png"),
        ("THE THREE PILLARS OF WHOLE-CHILD DEVELOPMENT",
         "Eat. Learn. Play. Three simple words that encapsulate the entire architecture of childhood flourishing.",
         "A child cannot learn if their stomach is empty. A child cannot dream if they cannot read grade-level books. And a child cannot build social confidence if they have no safe playground in their neighborhood. Steph and Ayesha addressed all three pillars simultaneously, attacking systemic childhood poverty from every angle.",
         "When solving complex problems in your organization, do not treat isolated symptoms. Address the entire ecosystem.",
         "stephen-ayesha-02.png"),
        ("ZERO OVERHEAD PROMISE: ONE HUNDRED PERCENT TO THE KIDS",
         "Steph and Ayesha personally cover all administrative and operating costs of Eat.Learn.Play.",
         "That means every single dollar donated by the public or corporate partners goes directly to meals, books, and schoolyards for Oakland youth. That level of personal financial stewardship built unshakeable institutional trust, allowing the foundation to mobilize tens of millions of dollars in record time.",
         "Trust is your greatest asset. When you demonstrate that you have skin in the game, partners will line up to back your vision.",
         "stephen-ayesha-03.png"),
        ("RADICAL LITERACY INTERVENTION IN OAKLAND SCHOOLS",
         "Eat.Learn.Play. has distributed over one million diverse, culturally affirming books to Oakland elementary students.",
         "If a child cannot read proficiently by the third grade, their statistical likelihood of high school graduation drops precipitously. Steph and Ayesha brought mobile book buses into neighborhood parks and funded professional literacy tutors across Oakland public schools, sparking a love for reading in children who had never owned a book.",
         "If you want to transform a community's future, put books in the hands of its eight-year-olds.",
         "stephen-ayesha-04.png"),
        ("REBUILDING TWENTY-FIVE ELEMENTARY SCHOOLYARDS",
         "Eat.Learn.Play. committed to transforming twenty-five schoolyards across Oakland into world-class play and sports spaces.",
         "Too many urban schoolyards are cracked asphalt and chain-link fences. Steph and Ayesha bring in landscape architects, turf fields, basketball courts, and community gardens. They give children colorful, dignified, safe spaces to run, climb, and develop athletic confidence.",
         "The physical environment you give a child communicates how much you value them. Build spaces worthy of their dreams.",
         "stephen-ayesha-05.png"),
        ("DELIVERING MILLIONS OF HEALTHY, NUTRITIOUS MEALS",
         "During the height of pandemic school closures, Eat.Learn.Play. delivered over twenty-five million meals to Oakland families.",
         "They did not just distribute shelf-stable cans; they partnered with local Oakland restaurants: pumping money back into struggling small businesses: to deliver fresh, hot, culturally relevant meals to families in need. That is circular economic philanthropy at its finest.",
         "Design your charitable efforts to support local commerce rather than bypassing it.",
         "stephen-ayesha-06.png"),
        ("THE POWER OF UNIFIED FAMILY STEWARDSHIP",
         "Watching Stephen and Ayesha lead together demonstrates the immense power of an aligned marital partnership.",
         "They do not compete for credit. Steph brings his global athletic megaphone and corporate alliances; Ayesha brings her culinary insight, hospitality standards, and community connection. Together, their combined impact is exponentially greater than what either could achieve in isolation.",
         "When two leaders align with mutual respect and zero ego, they can move mountains that stand in the way of justice.",
         "stephen-ayesha-07.png"),
        ("TEACHING CHILDREN THAT THEY MATTER",
         "Look at the smiles of the children surrounding Steph and Ayesha when they read together on a park bench.",
         "Those children do not just see famous celebrities; they feel seen, heard, and cherished. In my four decades as an Olympic coach, I have seen that children perform to the level of love and expectation poured into them. When world champions sit on the ground and read with you, your sense of self-worth is cemented.",
         "Never underestimate the life-altering impact of giving a child your undivided presence.",
         "stephen-ayesha-08.png"),
        ("SYSTEMIC PARTNERSHIP WITH OAKLAND UNIFIED",
         "Eat.Learn.Play. does not operate in a silo. They embedded their initiatives directly within the Oakland Unified School District.",
         "They worked alongside teachers, principals, and district administrators to identify the schools with the greatest structural deficits. They respected the institutional knowledge of local educators, providing the resources that school budgets could never cover.",
         "True leaders do not act as saviors from the outside. They partner with the boots on the ground already doing the work.",
         "stephen-ayesha-09.png"),
        ("TURNING CELEBRITY INTO SYSTEMIC CHANGE",
         "Many celebrities treat charity as a photo op. Steph and Ayesha engineered Eat.Learn.Play. as a permanent civic institution.",
         "They built an endowment, hired world-class nonprofit executives, and created governance boards that ensure the foundation will continue feeding, educating, and sheltering Oakland children long after Steph hangs up his sneakers.",
         "Build institutions that outlive your fame. That is the definitive mark of generational leadership.",
         "stephen-ayesha-10.png"),
        # Repeat cycle 2 (11-20)
        ("NUTRITION AS THE CORNERSTONE OF LEARNING",
         "A child experiencing food insecurity cannot concentrate on mathematics or reading comprehension.",
         "Steph and Ayesha made school breakfast and lunch programs a central battleground. By partnering with local farms and culinary leaders, they transformed school cafeteria menus into fresh, nutritious fuel that powers young brains throughout the school day.",
         "Fix the physiological foundation before you demand cognitive performance.",
         "stephen-ayesha-01.png"),
        ("FOSTERING A JOYFUL LOVE FOR PLAY",
         "In modern cities, unstructured play is disappearing, replaced by screens or safety fears. Eat.Learn.Play. is fighting for childhood.",
         "Play is where children learn negotiation, conflict resolution, emotional regulation, and teamwork. By building safe play spaces, Steph and Ayesha are restoring the vital joy of childhood to neighborhoods that have experienced immense trauma.",
         "Do not eliminate play from your life or your workplace. Play is the fertile soil where innovation and resilience grow.",
         "stephen-ayesha-02.png"),
        ("EQUITY IN YOUTH SPORTS ACCESS",
         "Private sports leagues have become pay-to-play engines that shut out low-income children. Eat.Learn.Play. levels the field.",
         "They fund youth sports leagues, provide free uniforms and coaching, and ensure that every Oakland child can experience the discipline and joy of organized sport, regardless of their parents' bank balance.",
         "Sport belongs to everyone. Defend the right of every young person to experience athletic brotherhood and sisterhood.",
         "stephen-ayesha-03.png"),
        ("THE RIPPLE EFFECT OF CULTURALLY AFFIRMING LITERATURE",
         "When children read books featuring characters who look like them, their engagement with reading skyrockets.",
         "Eat.Learn.Play. specifically curates books written by diverse authors celebrating Black, Latino, Asian, and Indigenous stories. They show young readers that their histories, neighborhoods, and dreams are worthy of literary celebration.",
         "Representation matters in books, in boardrooms, and in Olympic coaching. Ensure your library reflects the world you wish to build.",
         "stephen-ayesha-04.png"),
        ("CIVIC ENGAGEMENT THAT TRANSCENDS POLITICS",
         "Steph and Ayesha do not engage in petty partisan squabbles. They focus relentlessly on outcomes for kids.",
         "Whether working with local city councils, corporate donors, or grassroots activists, they maintain a laser focus on one question: does this initiative directly improve the life of an Oakland child? That clarity of mission disarms political friction.",
         "Keep the main thing the main thing. When your mission is unquestioned, detractors lose their power.",
         "stephen-ayesha-05.png"),
        ("MEASURABLE IMPACT OVER PRESS RELEASES",
         "Eat.Learn.Play. publishes rigorous annual impact reports detailing every dollar spent and every child reached.",
         "They measure third-grade reading improvements, school attendance rates, and athletic participation numbers. That data-driven discipline is why philanthropic institutions and major corporations entrust them with multi-million-dollar grants.",
         "Good intentions are not a metric. Measure your impact with unflinching data and accountability.",
         "stephen-ayesha-06.png"),
        ("THE COURAGE TO STAY COMMITTED TO OAKLAND",
         "Even after the Golden State Warriors relocated across the bay to San Francisco, Steph and Ayesha deepened their roots in Oakland.",
         "They did not abandon the city that loved them during their championship run. They maintained their foundation headquarters in Oakland and expanded their investments. That loyalty earned them the eternal devotion of the Oakland community.",
         "Loyalty during seasons of transition is the hallmark of genuine character. Never forget the soil that nourished your roots.",
         "stephen-ayesha-07.png"),
        ("EMPOWERING LOCAL MOTHERS AND FAMILIES",
         "Behind every child supported by Eat.Learn.Play. is a mother striving to provide a brighter future.",
         "Ayesha regularly hosts community circles, parenting roundtables, and wellness retreats for Oakland mothers, providing mental health resources and community solidarity. She understands that supporting the mother is the most effective way to protect the child.",
         "Strengthen the pillars of the family, and the entire community will stand upright.",
         "stephen-ayesha-08.png"),
        ("THE COMMUNITY GARDEN MOVEMENT",
         "At every rebuilt schoolyard, Eat.Learn.Play. installs edible community gardens where children plant seeds, tend vegetables, and taste fresh produce.",
         "They teach children where food comes from, instilling an early respect for agriculture, nutrition, and environmental stewardship. Watching an elementary student pull a fresh carrot from the ground they tended is a lesson in patience and harvest.",
         "Teach young minds that great things require patience, watering, and daily care before the harvest appears.",
         "stephen-ayesha-09.png"),
        ("A PARTNERSHIP FORGED IN PURPOSE",
         "Steph and Ayesha show the world that marriage can be a vehicle for monumental social change.",
         "They have built wealth, fame, and influence, but they channel those resources outward into the lives of vulnerable children. Their partnership is a masterclass in shared values, mutual elevation, and legacy creation.",
         "Align your personal relationships around shared purpose. Together, you can achieve what neither could accomplish alone.",
         "stephen-ayesha-10.png"),
        # Repeat cycle 3 (21-30)
        ("BREAKING THE CYCLE OF GENERATIONAL POVERTY",
         "Poverty is not just an absence of money; it is an absence of access, nourishment, and literacy.",
         "By attacking hunger, illiteracy, and physical inactivity simultaneously, Eat.Learn.Play. is breaking the generational transmission of poverty in Oakland. They are building a generation of healthy, literate, confident young people who will lead that city tomorrow.",
         "Do not apply bandages to systemic wounds. Attack the root causes that hold human potential hostage.",
         "stephen-ayesha-01.png"),
        ("CREATING HUBS OF HOPE IN HISTORIC NEIGHBORHOODS",
         "The playgrounds Steph and Ayesha build are not just for the school; they are open to the entire neighborhood on weekends.",
         "They become community gathering grounds where families hold picnics, neighbors converse, and children play safely under the California sun. That spatial revitalization reduces neighborhood crime and fosters community pride.",
         "Transform spaces of neglect into havens of beauty and joy. Beauty heals communities.",
         "stephen-ayesha-02.png"),
        ("THE DISCIPLINE OF LISTENING TO OAKLAND VOICES",
         "Before designing a single playground, Eat.Learn.Play. conducts listening sessions with the students and parents.",
         "They ask the kids what equipment they want: climbing walls, four-square courts, turf soccer fields: and they build what the children envisioned. That democratic design process gives the community immediate ownership and pride in the space.",
         "Never assume you know what people need. Ask them, listen with humility, and build their vision.",
         "stephen-ayesha-03.png"),
        ("CORPORATE RESPONSIBILITY WITH REAL TEETH",
         "Eat.Learn.Play. forces its corporate sponsors to volunteer on build days alongside Steph and Ayesha.",
         "CEOs and corporate executives roll up their sleeves, paint murals, spread mulch, and assemble playground equipment alongside neighborhood families. Steph and Ayesha break down corporate silos and bring executives face-to-face with the communities they serve.",
         "Get your hands dirty. Real leadership happens on the ground with tools in hand, not from an ivory tower.",
         "stephen-ayesha-04.png"),
        ("TEACHING KIDS TO FINISH STRONG",
         "The ethos of Olympic athletics: finishing strong when your lungs burn: permeates every literacy program and sports clinic Eat.Learn.Play. runs.",
         "They teach children that struggling with a difficult book is no different than struggling with a fourth-quarter deficit. You do not quit. You take a breath, ask for help, and finish strong. That mental toughness is life's ultimate survival skill.",
         "Instill resilience in young minds early. It is the greatest gift you can hand to the next generation.",
         "stephen-ayesha-05.png"),
        ("A CULTURE OF UNCEASING GRATITUDE",
         "Every time Steph and Ayesha speak about Eat.Learn.Play., their first words are gratitude to the Oakland community.",
         "They recognize that their NBA championships and cultural success were built on the backs of Oakland fans who filled Oracle Arena with electric passion for decades. Their foundation is an act of heartfelt thanksgiving, not patronizing benevolence.",
         "Approach your philanthropy with deep gratitude for the people who supported your ascent.",
         "stephen-ayesha-06.png"),
        ("NURTURING OLYMPIANS OF THE MIND",
         "Not every child will win a gold medal or an NBA championship, but every child can become an Olympic-level thinker and creator.",
         "Eat.Learn.Play. treats every student as a potential genius waiting to be unlocked. In my forty years of coaching elite athletes, I saw that the difference between an ordinary contender and a champion was the belief someone placed in them early.",
         "Look at the people under your leadership and see who they can become, not just who they are today.",
         "stephen-ayesha-07.png"),
        ("A MODEL FOR ATHLETES WORLDWIDE",
         "Eat.Learn.Play. has become the gold standard blueprint for how professional athletes should structure their foundations.",
         "Athletes from across the NFL, NBA, and Premier League regularly contact Steph and Ayesha's team to study their operational model, zero-overhead structure, and focus on systemic pillars. They are leading a revolution in athlete philanthropy.",
         "When you build something with excellence and integrity, the entire industry will study your blueprint.",
         "stephen-ayesha-08.png"),
        ("THE PROMISE OF BRIGHTER TOMORROWS",
         "Look at the banner behind Steph and Ayesha: 'Oakland Kids, Brighter Tomorrows.' That is not a slogan; it is a sacred contract.",
         "They have committed their lives, their fortune, and their ongoing energy to ensuring that every child in Oakland has the food, books, and play needed to realize their God-given potential. That is what it means to live for something greater than yourself.",
         "Dedicate your resources to a cause that will continue paying dividends long after you are gone.",
         "stephen-ayesha-09.png"),
        ("THE SCORE THAT MATTERS FOR ETERNITY",
         "Thirty points a game is impressive on television. Feeding twenty-five million meals and educating thousands of children is what echoes in eternity.",
         "Stephen and Ayesha Curry have mastered the art of owning the next chapter. They turned championship rings into keys that unlock doors for an entire city. That is the calling of high performance. That is the standard I urge every executive to embrace.",
         "Turn your personal victories into community access. That is true immortality.",
         "stephen-ayesha-10.png"),
    ]
    assert len(concepts) == 30, f"Steph & Ayesha items must be 30, got {len(concepts)}"
    return concepts

def get_serena_blueprints():
    items = []
    # Serena Williams: Serena Ventures, Angel City FC, Portfolios, Ownership (5 assets cycled 6 times = 30 posts)
    concepts = [
        ("TWENTY-THREE MAJORS. NOW SHE BUILDS PORTFOLIOS.",
         "Excellence on the court became experience Serena Williams could deploy across global venture capital.",
         "Serena did not retire from tennis to sit idly. She announced her 'evolution' away from sport to focus on Serena Ventures: an early-stage venture firm investing in founders who are traditionally ignored by Silicon Valley. She brought the same ruthless focus that conquered Wimbledon into vetting enterprise balance sheets and cap tables.",
         "As an Olympic coach, I know that championship focus does not die when you hang up your racket. It simply finds a larger arena.",
         "serena-williams-01.png"),
        ("INVESTING IN THE SEVENTY-EIGHT PERCENT",
         "Over 78 percent of Serena Ventures' portfolio companies are founded by women and people of color.",
         "In Silicon Valley, less than three percent of venture funding goes to female founders, and less than one percent to Black founders. Serena recognized this not as a lack of talent, but as a colossal market failure by myopic gatekeepers. She deployed her capital where market inefficiency created massive venture upside.",
         "Do not follow the herd into crowded trades. Look where prejudice has created undervalued, high-conviction opportunities.",
         "serena-williams-02.png"),
        ("THE TRANSITION FROM ATHLETE TO OWNER",
         "Serena Williams understands that an athlete's salary is taxed at the highest rates, while equity compounds tax-efficiently for generations.",
         "Throughout her playing days, Serena was already buying equity stakes in sports franchises like the Miami Dolphins and Angel City FC. She realized early that trophies represent past glory, but enterprise ownership represents permanent authority.",
         "Stop trading your finite hours for income. Start acquiring and building equity that works while you sleep.",
         "serena-williams-03.png"),
        ("DISCIPLINE IN CAP TABLE MANAGEMENT",
         "The composure required to save triple match point at Arthur Ashe is identical to negotiating equity terms in a Series A financing.",
         "Venture investing requires nerves of steel. Founders pitch grand dreams, but Serena looks at unit economics, burn rates, and founder resilience. She looks for founders who possess that rare Olympic fire: the ability to execute when everyone else has run out of gas.",
         "Invest in founders whose grit has been tested in fire, not those who only shine in sunny pitches.",
         "serena-williams-04.png"),
        ("PIONEERING ANGEL CITY FC AND WOMEN'S SPORTS EQUITY",
         "Serena was an early founding investor in Angel City FC, proving that women's sports is a multi-billion-dollar commercial asset.",
         "Naysayers claimed that women's soccer could not sell out stadiums or command premium enterprise valuations. Angel City FC shattered every attendance record, secured blockbuster sponsorships, and recently achieved a valuation exceeding two hundred million dollars.",
         "Never accept the limitations that small-minded observers project onto your industry. Prove them wrong with ledger sheets.",
         "serena-williams-05.png"),
        # Repeat cycle 2 (6-10)
        ("PREPARATION AS AN INSURMOUNTABLE ADVANTAGE",
         "Long before Serena wrote a check to an AI or fintech startup, she took executive education courses at Harvard and spent hours with Silicon Valley mentors.",
         "She did not rely on celebrity status to make her a competent venture capitalist. She did the homework, learned cap table mechanics, and mastered venture governance. Humility before new domains is the mark of a true champion.",
         "Never enter a new industry assuming your past fame guarantees present competence. Do the deep reading first.",
         "serena-williams-01.png"),
        ("THE POWER OF UNAPOLOGETIC AMBITION",
         "Throughout her tennis career, Serena was criticized for being too strong, too vocal, and too ambitious. She never apologized.",
         "She carried that exact unapologetic standard into corporate boardrooms. Women in business are often socialized to diminish their accomplishments and speak quietly. Serena reminds female founders that power is taken, not granted, and that excellence requires zero apologies.",
         "Own your power completely. When you demonstrate unshakeable conviction, the room will adjust to your presence.",
         "serena-williams-02.png"),
        ("NAVIGATING SETBACKS WITH RELENTLESS MOMENTUM",
         "Pulmonary embolisms, career-threatening surgeries, and heartbreaking finals losses could not stop Serena Williams.",
         "Every time she was knocked down, she analyzed the failure, restructured her training, and returned to win another Grand Slam. In venture investing, startups fail regularly. Serena understands that a loss is not a defeat; it is simply market tuition for the next breakthrough.",
         "Treat failure as data. Extract the lesson, discard the emotional baggage, and deploy your capital with greater precision.",
         "serena-williams-03.png"),
        ("THE ARCHITECTURE OF A DIVERSIFIED PORTFOLIO",
         "Serena Ventures has backed over eighty companies across fintech, digital health, e-commerce, and artificial intelligence.",
         "She does not put all her eggs in one basket. She builds diversified portfolios backed by rigorous thematic theses. She backs founders solving real human problems: accessible healthcare, financial inclusion, clean consumer products.",
         "Build resilience into your enterprise through intentional diversification and principled investment theses.",
         "serena-williams-04.png"),
        ("MOTHERHOOD AS A COMPETITIVE ADVANTAGE",
         "Serena won the 2017 Australian Open while eight weeks pregnant, and returned to four Grand Slam finals as a mother.",
         "She exploded the myth that motherhood diminishes professional intensity. In fact, she often notes that becoming a mother sharpened her focus and clarified her purpose. When she evaluates female founders who are mothers, she sees leaders who have mastered the ultimate crucible of multi-tasking and resilience.",
         "Recognize that life's greatest personal responsibilities often unlock your deepest professional capabilities.",
         "serena-williams-05.png"),
        # Repeat cycle 3 (11-15)
        ("BUILDING BRIDGES BETWEEN POP CULTURE AND VENTURE CAPITAL",
         "Serena can sit on the Met Gala red carpet on Monday and interrogate venture valuations on Tuesday morning.",
         "She bridges cultural relevance with institutional financial power. In the modern economy, cultural cachet drives distribution, and distribution makes startups explosive. Serena gives her portfolio companies unfair access to global consumer awareness.",
         "Pair cultural storytelling with financial rigor. That combination makes your portfolio companies untouchable.",
         "serena-williams-01.png"),
        ("DISRUPTING THE VENTURE CAPITAL BOYS' CLUB",
         "Venture capital has historically been dominated by a homogeneous group of investors who back founders who look like themselves.",
         "Serena walked into that room with twenty-three Grand Slam trophies and an iron will, demanding institutional capital allocations for diverse founders. She forced the venture ecosystem to recognize that investing in overlooked talent is not philanthropy: it is superior fiduciary execution.",
         "Break the mold in your industry. When you challenge comfortable assumptions, you capture immense untapped value.",
         "serena-williams-02.png"),
        ("THE ART OF EMOTIONAL REGULATION IN CRISIS",
         "When Serena was down 1-5 in the third set, her heart rate did not spike; her focus deepened.",
         "In business turnaround situations, amateur leaders become erratic and frantic. Serena teaches her startup CEOs that crisis requires surgical stillness. Slow your breathing, identify the single most critical variable, and execute the next shot with absolute precision.",
         "Stillness under pressure is the rarest and most potent leadership capability in modern commerce.",
         "serena-williams-03.png"),
        ("THE VALUE OF INTELLECTUAL PROPERTY SOVEREIGNTY",
         "Serena created S by Serena and Serena Ventures to ensure she retained full ownership of her likeness and commercial ideas.",
         "Too many athletes give away their name in licensing deals where third parties reap ninety percent of the profits. Serena insisted on equity ownership, board seats, and governance rights in every major deal she signed.",
         "Never surrender your name, your likeness, or your strategic governance for a temporary licensing fee.",
         "serena-williams-04.png"),
        ("TEACHING THE NEXT GENERATION OF GIRLS TO LEAD",
         "Serena's daughter Olympia is already a co-owner of Angel City FC and Los Angeles Golf Club.",
         "Serena is intentionally teaching her daughters the mechanics of capital ownership before they reach middle school. She is proving that generational wealth is not just about inheritance; it is about financial education, governance training, and ownership literacy.",
         "Teach your children the principles of ownership early. Give them an economic compass that guides their entire lives.",
         "serena-williams-05.png"),
        # Repeat cycle 4 (16-20)
        ("CHAMPION FOCUS IN BOARDROOM GOVERNANCE",
         "When Serena sits on a corporate board, she asks the hard, uncomfortable questions that others avoid.",
         "She does not show up as a decorative celebrity director. She reads the board materials, scrutinizes audit reports, and demands accountability on diversity and strategic execution. Her presence elevates the governance standard of every company she touches.",
         "Do not accept board seats or advisory roles if you are not willing to do the tedious governance work required.",
         "serena-williams-01.png"),
        ("THE COURAGE TO EVOLVE",
         "When Serena announced her transition from tennis in Vogue, she chose the word 'evolution' rather than 'retirement.'",
         "Retirement implies quitting, fading away, or concluding your utility. Evolution implies taking every ounce of wisdom, stamina, and competitive excellence you developed in one arena and directing it into your next great endeavor.",
         "Never retire. Evolve. Reallocate your championship energy into new mountains worthy of your capabilities.",
         "serena-williams-02.png"),
        ("THE METRICS THAT MATTER IN VENTURE",
         "In tennis, the scorecard is simple: games, sets, match. In venture, the scorecard is IRR, multiple on invested capital, and customer acquisition costs.",
         "Serena mastered the language of venture finance because she understood that respect in institutional finance is earned through numbers, not sentiment. She holds her portfolio companies to rigorous operational discipline.",
         "Master the definitive financial metrics of your industry. Speak the language of capital with absolute fluency.",
         "serena-williams-03.png"),
        ("BUILDING INFRASTRUCTURE FOR WOMEN'S SPORTS",
         "Serena's investment in Angel City FC catalyzed a global wave of institutional investment into women's athletics.",
         "She proved that women's sports is an undervalued asset class with passionate fans, surging viewership, and immense commercial runway. Today, private equity and institutional funds are pouring billions into women's sports because Serena proved the business thesis.",
         "Be the pioneer who validates a new asset class. The rewards of proving the thesis first are astronomical.",
         "serena-williams-04.png"),
        ("THE LESSON OF COMPTON TO THE WORLD STAGE",
         "Remember where Serena's journey began: public courts in Compton with cracked concrete and missing nets.",
         "Her father Richard Williams had a vision for his daughters that seemed absurd to the tennis establishment. Serena proved that when preparation, unshakeable family belief, and ferocious work ethic collide, no institutional barrier can stop you.",
         "Never let humble beginnings limit the scale of your global vision. The fire forged in adversity will fuel your empire.",
         "serena-williams-05.png"),
        # Repeat cycle 5 (21-25)
        ("THE DISCIPLINE OF LONGEVITY",
         "Serena competed at the highest echelon of professional tennis for four separate decades.",
         "That level of physical and mental longevity is unprecedented. It required continuous reinvention of her nutrition, recovery protocols, mental health boundaries, and tournament schedule. She brings that same multi-decade horizon to her venture fund investments.",
         "Think in decades, not quarters. Build an enterprise designed to weather every economic cycle and emerge victorious.",
         "serena-williams-01.png"),
        ("THE STRENGTH TO STAND ALONE",
         "In 2001, Serena faced immense hostility at Indian Wells. She walked away from that tournament for fourteen years on principle.",
         "She showed that dignity and principle must always supersede commercial convenience. When she returned in 2015, it was on her own terms, turning a moment of historical pain into a masterclass in grace and forgiveness.",
         "Never sell your principles for prize money or corporate approval. When you stand on integrity, time will vindicate you.",
         "serena-williams-02.png"),
        ("HOW EXCELLENCE CREATES LEVERAGE",
         "When you are undeniably the best in the world at what you do, you dictate the terms of your contracts.",
         "Serena did not beg sponsors for favorable terms. Her undeniable excellence on the court gave her the commercial leverage to negotiate equity clauses, creative control, and philanthropic commitments into every corporate agreement.",
         "Do not spend time lobbying for leverage. Spend your time building undeniable excellence. Leverage will follow automatically.",
         "serena-williams-03.png"),
        ("LESSONS FROM MATCH POINT CONVERSIONS",
         "In tennis, you can win more total points than your opponent and still lose the match if you fail to convert on big points.",
         "In business, closing the decisive transaction matters far more than having busy days. Serena was legendary for raising her level of play on break points and match points. She teaches founders how to execute under pressure when the term sheet is on the table.",
         "Identify the decisive moments that truly matter, and bring your absolute highest level of focus to those specific inflection points.",
         "serena-williams-04.png"),
        ("THE POWER OF A SISTERHOOD ALLIANCE",
         "The partnership between Serena and Venus Williams changed sports history forever.",
         "They pushed each other in practice, protected each other on tour, won fourteen Grand Slam doubles titles together with zero losses in finals, and built business empires side by side. That sisterhood proved that competition does not require tearing down your closest allies.",
         "Build alliances based on unshakeable loyalty. When you push each other to greatness, both of you conquer the world.",
         "serena-williams-05.png"),
        # Repeat cycle 6 (26-30)
        ("VENTURE AS AN INSTRUMENT OF CULTURAL CHANGE",
         "Serena does not view capital merely as a scorecard; she views it as a cultural lever.",
         "When she funds a startup that democratizes maternal health for women of color, she is saving lives while generating financial returns. That is conscious capitalism at the highest Olympic level.",
         "Deploy your capital so that every financial return simultaneously advances human flourishing.",
         "serena-williams-01.png"),
        ("THE RELENTLESS PURSUIT OF MASTERY",
         "Even after winning twenty Grand Slams, Serena was on the practice court at 6:00 AM working on second-serve consistency.",
         "Mastery is not a destination where you unpack your bags and rest. Mastery is a continuous commitment to refine the smallest details of your craft. That is the mentality she instills in the CEOs backed by Serena Ventures.",
         "Never allow your past accomplishments to convince you that you have arrived. Stay hungry on the practice courts of your industry.",
         "serena-williams-02.png"),
        ("THE PSYCHOLOGICAL WARFARE OF BOARDROOMS",
         "Intimidation in corporate deal-making is real. Serena Williams has stared down the most ferocious competitors in sports history.",
         "When she walks into a boardroom, she cannot be bullied, hurried, or patronized. Her posture, her calm tone, and her deep knowledge of the facts command immediate authority. She teaches women leaders to occupy space without apology.",
         "Walk into every room knowing you belong there. Your self-assurance sets the boundary for how others treat you.",
         "serena-williams-03.png"),
        ("CREATING PERMANENT FOOTPRINTS IN COMMERCE",
         "Trophies tarnish and records will be contested, but the companies Serena seeds will employ thousands and shape the global economy.",
         "That is the shift from champion to owner, and from owner to institution builder. Serena Williams has rewritten the playbook for every elite athlete who will follow her.",
         "Build something that outlives your personal celebrity. Build institutions that continue providing value across generations.",
         "serena-williams-04.png"),
        ("THE FINAL VICTORY: LIVING ON YOUR OWN TERMS",
         "Serena Williams' greatest victory was not at Wimbledon or Roland Garros. It was stepping away on her own timeline, with her head held high.",
         "She dictated her entry into the sport, dominated it for a generation, and exited to build a billion-dollar legacy on her own terms. That is the definition of true sovereignty. That is what I challenge every leader to achieve.",
         "Write your own story. Own your next chapter.",
         "serena-williams-05.png"),
    ]
    assert len(concepts) == 30, f"Serena items must be 30, got {len(concepts)}"
    return concepts

def get_lewis_blueprints():
    items = []
    # Lewis Hamilton: F1 Champion to Denver Broncos Owner, Media, Global Brands (5 assets cycled 6 times = 30 posts)
    concepts = [
        ("HE DOESN'T JUST COMPETE FOR TEAMS. HE OWNS ONE.",
         "Lewis Hamilton: seven-time Formula 1 world champion, Denver Broncos owner.",
         "Most professional athletes view team ownership as something reserved for tech billionaires and real estate moguls. Lewis shattered that ceiling by joining the ownership group of the NFL's Denver Broncos. He recognized that driving at 200 mph is only part of his purpose. The higher calling is acquiring institutional equity in the most valuable sports league on earth.",
         "As an Olympic coach for four decades, I teach champions: do not spend your entire career playing for someone else's franchise. Build enough capital and credibility to own one.",
         "lewis-hamilton-01.png"),
        ("EXTREME PRECISION UNDER SUFFOCATING PRESSURE",
         "Driving an F1 car at 220 miles per hour in the rain requires an operating state of absolute emotional neutrality.",
         "One millisecond of hesitation or emotional panic puts you into a concrete barrier. Lewis developed a mental discipline that allows him to process thousands of data points: tire degradation, brake balance, weather radar, radio telemetry: while heart rate remains rock-steady. That exact psychological composure is what allows him to negotiate complex multi-million-dollar ownership transactions.",
         "In high-stakes corporate negotiations, the person who regulates their emotions most effectively always controls the outcome.",
         "lewis-hamilton-02.png"),
        ("DAWN APOLLO FILMS AND THE BUSINESS OF CULTURE",
         "Lewis did not wait for Hollywood to tell racing stories. He founded Dawn Apollo Films to produce them.",
         "Partnering with Brad Pitt and Apple TV, Lewis took control of the narrative, serving as lead producer on major cinematic projects. He understood that whoever controls media storytelling controls global brand equity. He transitioned from being the subject of the camera to the executive producer who owns the negative rights.",
         "Do not let others monetize your story. Build your own production engine and retain the intellectual property rights.",
         "lewis-hamilton-03.png"),
        ("MISSION FORTY-FOUR AND RADICAL MERITOCRACY",
         "Lewis created Mission 44 to fund STEM education and motorsport apprenticeships for underrepresented youth.",
         "He did not just donate money; he launched the Hamilton Commission in partnership with the Royal Academy of Engineering to scientifically identify the barriers preventing diverse engineers from entering motorsport. He treated systemic exclusion as an engineering problem that requires data, metrics, and targeted interventions.",
         "Do not guess at why your industry lacks diversity. Commission the research, identify the structural bottlenecks, and fund the solution.",
         "lewis-hamilton-04.png"),
        ("SHATTERING FASHION STEREOTYPES IN THE PADDOCK",
         "In a traditional motorsport paddock dominated by corporate polos, Lewis turned race weekends into high-fashion runways.",
         "He partnered with Tommy Hilfiger, Dior, and Valentino, launching sustainable clothing lines and bringing avant-garde fashion into sports culture. He expanded his personal brand into luxury lifestyle, making him a household name in markets that had never watched an auto race.",
         "Refuse to conform to the drab dress codes of your industry. Use personal style and creative audacity to carve out an unforgettable identity.",
         "lewis-hamilton-05.png"),
        # Repeat cycle 2 (6-10)
        ("THE RELENTLESS PURSUIT OF MARGINAL GAINS",
         "In Formula 1, championships are decided by hundredths of a second across a sixty-lap race.",
         "Lewis works obsessively with his engineers to find fractional aerodynamic advantages, weight reductions, and throttle map optimizations. In corporate enterprise, marginal gains in logistics, customer retention, and operational overhead compound into massive competitive moats.",
         "Stop hunting for silver bullets. Find ten one-percent improvements across your business and watch your margins explode.",
         "lewis-hamilton-01.png"),
        ("THE COURAGE TO SPEAK TRUTH ON THE PODIUM",
         "When Lewis took a knee on the podium and wore shirts demanding justice, he faced intense pressure from racing authorities.",
         "He refused to be silenced. He leveraged the world's most watched motorsport broadcast to demand human rights, racial justice, and equality. He showed that authentic leadership requires using your podium to advocate for those who have no microphone.",
         "Leadership is tested when speaking the truth costs you corporate comfort. Stand on conviction regardless of the audience.",
         "lewis-hamilton-02.png"),
        ("THE DIET AND RECOVERY OF AN ELITE ATHLETE",
         "Lewis adopted a plant-based lifestyle and revolutionized his physical training to compete against drivers half his age.",
         "Driving an F1 car subjects your body to five Gs of lateral force for two hours while losing eight pounds of water weight. Lewis invested in hyperbaric chambers, cryotherapy, and precise nutrition. Longevity in business requires the exact same commitment to physical and cognitive recovery.",
         "You cannot lead an enterprise effectively if your body is exhausted and inflamed. Treat your physical recovery as a fiduciary duty.",
         "lewis-hamilton-03.png"),
        ("THE POWER OF UNCONVENTIONAL BACKGROUNDS",
         "Lewis grew up in a council house in Stevenage, with his father working four jobs to fund his go-karting.",
         "He did not have a wealthy family to buy him a racing team. He carried the hunger of someone who knew that one mistake meant packing up the kart forever. That working-class resilience made him bulletproof when competing against the sons of billionaires.",
         "Never apologize for having to fight for your seat at the table. Hunger built in adversity will outlast inherited privilege every time.",
         "lewis-hamilton-04.png"),
        ("MANAGING CRISIS AFTER HEARTBREAK",
         "The controversial final lap of Abu Dhabi in 2021 was the most agonizing moment in modern sports history.",
         "Lewis was robbed of an eighth world title by an administrative rule breach. What did he do? He shook his competitor's hand, hugged his father, congratulated the opposing team, and walked away with absolute dignity. He did not throw tantrums on television. That grace under devastating heartbreak cemented his status as a legendary statesman of sport.",
         "Your character is not revealed when you win the trophy. It is revealed in how you carry yourself when you are wronged.",
         "lewis-hamilton-05.png"),
        # Repeat cycle 3 (11-15)
        ("THE ART OF PIT STOP TRUST",
         "Lewis enters the pit lane at fifty miles per hour, trusting twenty mechanics to change four tires in two seconds flat.",
         "That level of speed requires absolute psychological safety and operational trust. There is no room for second-guessing. In executive management, if you have to micromanage your leadership team during a product release, your culture is already broken.",
         "Train your team until execution is automatic, then get out of their way and let them execute.",
         "lewis-hamilton-01.png"),
        ("INSTITUTIONAL INVESTING IN THE NFL",
         "Joining the Walton-Penner family ownership group of the Denver Broncos placed Lewis in the most exclusive ownership club in the world.",
         "NFL teams are among the most secure, appreciating institutional assets on the planet. Lewis brought global marketing insights, sports science acumen, and diversity perspectives to the Broncos board, proving that European sports champions belong at the American ownership table.",
         "Expand your investment horizon across continents and industries. Cross-pollinate insights between disconnected domains.",
         "lewis-hamilton-02.png"),
        ("REDUCING CARBON FOOTPRINTS IN MOTORSPORT",
         "Lewis pushed Formula 1 and Mercedes to adopt net-zero carbon targets and sustainable aviation fuel.",
         "He sold his private jet, eliminated single-use plastics from his operations, and launched non-alcoholic agave spirits (Almave) that celebrate sustainability. He recognized that modern luxury must be compatible with environmental responsibility.",
         "Align your products with the values of the future, not the wasteful habits of the past.",
         "lewis-hamilton-03.png"),
        ("THE DISCIPLINE OF MENTAL HEALTH ADVOCACY",
         "Lewis has spoken openly about his struggles with depression and the psychological toll of racing under constant scrutiny.",
         "By normalizing vulnerability, he dismantled the toxic motorsport machismo that forces drivers to hide emotional pain. In my executive coaching work, the strongest CEOs are those who acknowledge mental fatigue and install emotional support systems for themselves and their teams.",
         "Vulnerability is not weakness; it is the prerequisite for authentic emotional strength.",
         "lewis-hamilton-04.png"),
        ("THE BOLD MOVE TO FERRARI",
         "At thirty-nine years old, after six world titles with Mercedes, Lewis signed a multi-year deal to drive for Scuderia Ferrari.",
         "He refused to settle into a comfortable, safe retirement ride. He chose the most iconic, high-pressure, emotionally volatile seat in motorsport because he wanted the ultimate challenge. Great champions seek new crucibles to test their capabilities.",
         "When comfort threatens to dull your edge, put yourself back in the arena where everything is on the line.",
         "lewis-hamilton-05.png"),
        # Repeat cycle 4 (16-20)
        ("THE VALUE OF A SINGLE-MINDED VISION",
         "At ten years old, Lewis walked up to McLaren boss Ron Dennis and said: 'One day I want to be racing your cars.'",
         "He had an unshakeable vision long before he had the resources to back it up. Vision is what pulls you out of bed on freezing mornings when every external circumstance tells you to quit. In corporate strategy, vision is what keeps your team aligned when cash flow is tight.",
         "Cast a vision so clear and compelling that doubt has nowhere to hide in your organization.",
         "lewis-hamilton-01.png"),
        ("NAVIGATING THE TEAMMATE RIVALRY",
         "In Formula 1, your teammate is your fiercest rival because they drive identical machinery.",
         "Lewis managed high-stakes rivalries with Fernando Alonso, Jenson Button, and Nico Rosberg. He learned that internal competition can elevate an organization, provided respect for the overarching team objective is never violated.",
         "Channel internal competition toward collective excellence rather than petty sabotage.",
         "lewis-hamilton-02.png"),
        ("CREATING PRODUCTS THAT DISRUPT TRADITION",
         "With Almave, Lewis created the world's first non-alcoholic blue agave spirit made using authentic Mexican distilling techniques.",
         "He did not just create another non-alcoholic soda; he worked with master distillers in Jalisco to create a luxury beverage that honors Mexican heritage while supporting mindful, high-performance lifestyles. That is true product innovation.",
         "Do not settle for superficial brand extensions. Create products that genuinely innovate within traditional crafts.",
         "lewis-hamilton-03.png"),
        ("THE DISCIPLINE OF THE RACING LINE",
         "On any racetrack, there is only one optimal mathematical trajectory: the racing line. Deviating by two inches bleeds speed.",
         "Lewis drives with a geometric elegance that makes violent physics look effortless. In business execution, adhering to your core strategic trajectory protects you from unnecessary friction and wasted capital.",
         "Identify the definitive trajectory for your business and hold your line with uncompromising precision.",
         "lewis-hamilton-04.png"),
        ("THE IMPORTANCE OF FAMILY ALLIANCES",
         "Anthony Hamilton mortgaged his house and worked night shifts to keep Lewis in karting competitions.",
         "Lewis never forgets that debt of gratitude. He keeps his family close, honoring his father and brother Nicolas at every career milestone. He proves that athletic and commercial conquest is hollow if it destroys the family bonds that sustained you in the beginning.",
         "Protect your family and core relationships at all costs. They are your true sanctuary when the stadium lights go out.",
         "lewis-hamilton-05.png"),
        # Repeat cycle 5 (21-25)
        ("ELEVATING THE GLOBAL CONVERSATION ON DIVERSITY",
         "When Lewis entered Formula 1 in 2007, he was the first and only Black driver in the history of the sport.",
         "Seventeen years later, he is the most successful driver to ever sit in a cockpit: 104 race victories, 104 pole positions. He did not just break the barrier; he established a standard of excellence that no one before him had ever attained.",
         "Do not just break ceilings. Build permanent floors upon which the next generation can stand.",
         "lewis-hamilton-01.png"),
        ("MANAGING TIRE DEGRADATION IN THE CLOSING LAPS",
         "The greatest F1 drivers are not those who drive the fastest lap; they are those who preserve their equipment until the end.",
         "Lewis is a master of tire management, nursing worn rubber through thirty laps while defending against younger challengers. In business, capital preservation and customer relationship management are your tires. Burn through them carelessly, and you will not finish the race.",
         "Pace your resources. The goal is to finish first, not to post the flashiest split time in lap ten and crash out.",
         "lewis-hamilton-02.png"),
        ("CULTIVATING A MULTI-HYPHENATE IDENTITY",
         "Lewis is a driver, an owner, a producer, a designer, an investor, and a philanthropist.",
         "He rejected the outdated advice that athletes should 'stick to sports.' He understood that a multifaceted life fuels creativity and prevents burnout in your primary domain.",
         "Embrace your diverse passions. Creative cross-pollination will make you sharper in your primary enterprise.",
         "lewis-hamilton-03.png"),
        ("THE ART OF RADIO SILENCE",
         "Listen to Lewis on team radio during the most chaotic races: concise, measured, informative.",
         "He does not scream or vent panic. He reports track conditions, asks for tire temperature data, and confirms tactical decisions. In corporate crisis management, leaders who clog communication channels with noise create paralysis.",
         "Keep your operational communication lean, factual, and actionable during critical moments.",
         "lewis-hamilton-04.png"),
        ("TURNING ADVERSITY INTO HIGH-OCTANE FUEL",
         "Every penalty, every engine failure, and every unfair stewards' decision became fuel for Lewis's next dominant weekend.",
         "He has an extraordinary psychological capability to transmute anger into laser-like technical focus. That is the hallmark of an Olympic-caliber champion.",
         "Do not let unfair circumstances make you bitter. Let them make you untouchable.",
         "lewis-hamilton-05.png"),
        # Repeat cycle 6 (26-30)
        ("THE POWER OF A SIGNATURE PHILOSOPHY: STILL WE RISE",
         "Inscribed on Lewis Hamilton's helmet are Maya Angelou's words: 'Still I Rise.'",
         "It is not a decorative quote; it is his personal doctrine. When you have a core philosophical anchor, market downturns, unfair referee calls, and personal tragedies cannot derail your trajectory. You simply rise again.",
         "Anchor your enterprise in timeless principles that cannot be shaken by market turbulence.",
         "lewis-hamilton-01.png"),
        ("LESSONS FROM SEVEN WORLD CHAMPIONSHIPS",
         "Winning one championship is difficult. Winning seven requires rebuilding your motivation from scratch every single winter.",
         "After you have won everything, your greatest enemy is complacency. Lewis found new motivations every year: pushing for technical perfection, developing young mechanics, mentoring team members. He never allowed success to make him soft.",
         "Fight complacency with ferocious vigilance. The moment you believe you have mastered your craft is the moment decline begins.",
         "lewis-hamilton-02.png"),
        ("THE ART OF GLOBAL CITIZENSHIP",
         "Lewis races in Japan, Brazil, Italy, Abu Dhabi, and the United States, connecting authentically with local fans in every culture.",
         "He studies local customs, respects cultural heritage, and carries himself as a humble ambassador of sport. In an interconnected global economy, cultural intelligence is an invaluable leadership asset.",
         "Approach global markets with genuine curiosity, humility, and cultural respect.",
         "lewis-hamilton-03.png"),
        ("STEWARDING AN NFL FRANCHISE WITH PURPOSE",
         "As an owner of the Denver Broncos, Lewis brings an obsession with athlete wellness, nutrition, and mental health.",
         "He works with Broncos leadership to ensure players have world-class recovery facilities and community outreach programs. He is redefining what an active, hands-on minority owner can contribute to a legacy franchise.",
         "Do not be a passive investor. Bring your unique expertise and values to the governance table.",
         "lewis-hamilton-04.png"),
        ("THE ARCHITECT WHO TRANSCENDED THE COCKPIT",
         "Lewis Hamilton began in a Stevenage council house. Today, he sits in the owner's suite of an NFL stadium and commands a global empire.",
         "He did not just win races; he owned the next chapter. He turned athletic greatness into enterprise sovereignty, social equity, and generational legacy. That is the gold standard. That is what I challenge every leader to build.",
         "Step out of the cockpit of merely executing. Step into the owner's suite and build your lasting legacy.",
         "lewis-hamilton-05.png"),
    ]
    assert len(concepts) == 30, f"Lewis items must be 30, got {len(concepts)}"
    return concepts

# -------------------------------------------------------------
# MASTER SCHEDULER BUILDER
# -------------------------------------------------------------

def build_campaign():
    tiger = get_tiger_blueprints()
    steph = get_stephen_blueprints()
    ayesha = get_ayesha_blueprints()
    steph_ayesha = get_stephen_ayesha_blueprints()
    serena = get_serena_blueprints()
    lewis = get_lewis_blueprints()

    # Track indexes for each athlete (0..29)
    cur_idx = {
        "tiger": 0,
        "steph": 0,
        "ayesha": 0,
        "steph_ayesha": 0,
        "serena": 0,
        "lewis": 0
    }

    # 6-Day Repeating Athlete Rotation Matrix:
    # Day 0 (Cycle 1): Slot 1 = Tiger, Slot 2 = Steph, Slot 3 = Ayesha
    # Day 1 (Cycle 2): Slot 1 = Steph+Ayesha, Slot 2 = Serena, Slot 3 = Lewis
    # Day 2 (Cycle 3): Slot 1 = Ayesha, Slot 2 = Tiger, Slot 3 = Steph
    # Day 3 (Cycle 4): Slot 1 = Lewis, Slot 2 = Steph+Ayesha, Slot 3 = Serena
    # Day 4 (Cycle 5): Slot 1 = Steph, Slot 2 = Ayesha, Slot 3 = Tiger
    # Day 5 (Cycle 6): Slot 1 = Serena, Slot 2 = Lewis, Slot 3 = Steph+Ayesha
    cycle_schedule = [
        [("tiger", tiger), ("steph", steph), ("ayesha", ayesha)],
        [("steph_ayesha", steph_ayesha), ("serena", serena), ("lewis", lewis)],
        [("ayesha", ayesha), ("tiger", tiger), ("steph", steph)],
        [("lewis", lewis), ("steph_ayesha", steph_ayesha), ("serena", serena)],
        [("steph", steph), ("ayesha", ayesha), ("tiger", tiger)],
        [("serena", serena), ("lewis", lewis), ("steph_ayesha", steph_ayesha)],
    ]

    # CTAs: 50/50 split across each athlete's 30 posts (15 Keynote, 15 Book)
    # Book pairings per athlete:
    book_catalog = {
        "tiger": [
            ("Finish Strong: Chasing the Olympic Dream", "https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A"),
            ("Survival Skills for Athletes", "https://lornettedaye.com/books")
        ],
        "steph": [
            ("Survival Skills for Athletes", "https://lornettedaye.com/books"),
            ("Survival Skills for Students", "https://lornettedaye.com/books")
        ],
        "ayesha": [
            ("Survival Skills for Women", "https://lornettedaye.com/books"),
            ("Survival Skills: Surviving to Thriving", "https://lornettedaye.com/books")
        ],
        "steph_ayesha": [
            ("UMATTR Devotional", "https://lornettedaye.com/books"),
            ("Surviving Life", "https://buy.stripe.com/7sY8wPcwuabE62Jcqu1VK02")
        ],
        "serena": [
            ("Survival Skills for Women", "https://lornettedaye.com/books"),
            ("Finish Strong: Chasing the Olympic Dream", "https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A")
        ],
        "lewis": [
            ("Survival Skills for Men", "https://buy.stripe.com/9B6bJ1542gA262JfCG1VK00"),
            ("Finish Strong: Chasing the Olympic Dream", "https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A")
        ],
    }

    start_date = datetime(2026, 10, 3)
    posts_data = []

    # Hashtags per athlete
    athlete_hashtags = {
        "tiger": "#TigerWoods #TGRFoundation #BusinessAthletes #OwnTheNextChapter #ExecutiveLeadership #OlympicMindset #FinishStrong #LornetteDaye #HighPerformance #GolfLife #LegacyBuilding",
        "steph": "#StephenCurry #UnderratedGolf #YouthOpportunity #OwnTheNextChapter #BusinessAthletes #ChampionMindset #LornetteDaye #HighPerformance #KeynoteSpeaker #DisruptiveEquity",
        "ayesha": "#AyeshaCurry #SweetJuly #WomenInBusiness #OwnTheNextChapter #ExecutiveLeadership #HospitalityExcellence #LornetteDaye #FemaleFounders #LifestyleBrand #BrandArchitecture",
        "steph_ayesha": "#EatLearnPlay #StephenCurry #AyeshaCurry #OaklandKids #CommunityImpact #SocialEnterprise #OwnTheNextChapter #LornetteDaye #LegacyBuilding #FamilyLeadership",
        "serena": "#SerenaWilliams #SerenaVentures #AngelCityFC #OwnTheNextChapter #WomenInBusiness #VentureCapital #ExecutiveLeadership #LornetteDaye #HighPerformance #BoardroomExcellence",
        "lewis": "#LewisHamilton #DenverBroncos #Formula1 #OwnTheNextChapter #HighPerformance #ExecutiveLeadership #InstitutionalCapital #LornetteDaye #Mission44 #PrecisionExecution",
    }

    for day_i in range(1, 61):
        cur_day = start_date + timedelta(days=day_i - 1)
        d_str = cur_day.strftime("%Y-%m-%d")
        next_d_str = (cur_day + timedelta(days=1)).strftime("%Y-%m-%d")
        is_mdt = (cur_day < datetime(2026, 11, 1))

        # 3 Daily Collision-Free Slots:
        # Slot 1: Morning (7:45 AM local)
        # Slot 2: Afternoon (2:30 PM local)
        # Slot 3: Evening (6:30 PM local -> next day UTC)
        slot1_utc = f"{d_str}T13:45:00.000Z" if is_mdt else f"{d_str}T14:45:00.000Z"
        slot2_utc = f"{d_str}T20:30:00.000Z" if is_mdt else f"{d_str}T21:30:00.000Z"
        slot3_utc = f"{next_d_str}T00:30:00.000Z" if is_mdt else f"{next_d_str}T01:30:00.000Z"

        slot_times = [
            ("Morning (7:45 AM MDT/MST)", slot1_utc),
            ("Afternoon (2:30 PM MDT/MST)", slot2_utc),
            ("Evening (6:30 PM MDT/MST)", slot3_utc)
        ]

        cycle_idx = (day_i - 1) % 6
        cycle_row = cycle_schedule[cycle_idx]

        for slot_num in range(3):
            slot_name, due_utc = slot_times[slot_num]
            ath_key, ath_blueprints = cycle_row[slot_num]
            post_in_athlete = cur_idx[ath_key]
            cur_idx[ath_key] += 1

            title, hook, body, takeaway, asset_file = ath_blueprints[post_in_athlete]
            asset_url = f"https://lornettedaye.com/campaigns/own-the-next-chapter/{asset_file}"

            # 50/50 CTA split for this athlete:
            # Even post_in_athlete (0, 2, 4...) -> Keynote Booking
            # Odd post_in_athlete (1, 3, 5...) -> Buy Book
            if post_in_athlete % 2 == 0:
                cta_type = "Keynote Booking (lornettedaye.com/book)"
                cta_text = (
                    "Bring championship execution, Olympic focus, and boardroom sovereignty to your corporate offsite or annual leadership summit.\n"
                    "Book Lornette Daye for your keynote: https://lornettedaye.com/book"
                )
            else:
                book_pair = book_catalog[ath_key][(post_in_athlete // 2) % len(book_catalog[ath_key])]
                book_title, book_link = book_pair
                cta_type = f"Buy Book - {book_title} (lornettedaye.com/books)"
                cta_text = (
                    f"Equip yourself and your leadership team with the championship mindset needed to navigate high-stakes transition.\n"
                    f"Get the published digital edition of '{book_title}' ($14.99 CAD): {book_link}"
                )

            sign_offs = [
                "With purpose,\nLornette",
                "Stay focused,\nLornette",
                "Keep building,\nLornette",
                "In your corner,\nLornette",
                "With conviction,\nLornette"
            ]
            sign_off = sign_offs[post_in_athlete % len(sign_offs)]
            hashtags = athlete_hashtags[ath_key]

            full_text = f"{title}\n\n{hook}\n\n{body}\n\n{takeaway}\n\n{sign_off}\n\n{cta_text}\n\n{hashtags}"

            # Invariant audit
            for em_dash in ["\u2014", "&mdash;", "—"]:
                if em_dash in full_text:
                    raise ValueError(f"Post contains em dash ({em_dash}) on Day {day_i}, Slot {slot_num + 1}!")
            if "Coach Lornette" in full_text:
                raise ValueError(f"Post signed Coach Lornette on Day {day_i}, Slot {slot_num + 1}!")
            if "Lornette" not in full_text:
                raise ValueError(f"Post missing Lornette signature on Day {day_i}, Slot {slot_num + 1}!")

            posts_data.append({
                "id": len(posts_data) + 1,
                "day": day_i,
                "date": d_str,
                "athlete": ath_key,
                "slot": slot_name,
                "dueAt": due_utc,
                "assetFile": asset_file,
                "assetUrl": asset_url,
                "cta": cta_type,
                "text": full_text
            })

    print(f"Generated {len(posts_data)} posts successfully.")
    assert len(posts_data) == 180, f"Expected 180 posts, got {len(posts_data)}"

    # Audit athlete distributions
    for ath_key in ["tiger", "steph", "ayesha", "steph_ayesha", "serena", "lewis"]:
        count = sum(1 for p in posts_data if p["athlete"] == ath_key)
        assert count == 30, f"Athlete {ath_key} has {count} posts, expected 30!"

    keynote_count = sum(1 for p in posts_data if p["cta"].startswith("Keynote Booking"))
    book_count = sum(1 for p in posts_data if p["cta"].startswith("Buy Book"))
    print(f"CTA Split: {keynote_count} Keynote CTAs, {book_count} Book CTAs.")
    assert keynote_count == 90 and book_count == 90, "Must be exact 50/50 CTA split (90 Keynotes, 90 Books)!"

    # Check for duplicate timestamps
    timestamps = [p["dueAt"] for p in posts_data]
    assert len(timestamps) == len(set(timestamps)), "Internal timestamp collisions found!"
    print("ALL INVARIANTS AUDITED AND PASSED!")

    # Write schedule-own-the-next-chapter.py
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

CDN_BASE = 'https://lornettedaye.com/campaigns/own-the-next-chapter'

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
print("INVARIANTS AUDIT PASSED: 180 posts verified. 0 em dashes, all signed strictly 'Lornette', 50/50 alternating CTA.")

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

    report_path = "scripts/own-the-next-chapter-scheduled-report.json"
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
            print(f"[{{i}}/180] Post #{{p_id}} already scheduled (Buffer ID: {{results[p_id]['postId']}}). Skipping.")
            continue

        while True:
            print(f"\\n[{{i}}/180] Scheduling Post #{{p['id']}} (Day {{p['day']}} - {{p['athlete'].upper()}} - {{p['slot']}}) - Due: {{p['dueAt']}}...")
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
    print(f"\\nExecution complete. Saved {{success_count}}/180 successfully to {{report_path}}.")
    return success_count == len(posts_data)

if __name__ == "__main__":
    schedule_posts()
'''

    out_file = os.path.join(os.path.dirname(__file__), "schedule-own-the-next-chapter.py")
    with open(out_file, "w", encoding="utf-8") as f:
        f.write(script_content)
    print(f"Wrote {len(posts_data)} posts to {out_file} successfully ({os.path.getsize(out_file):,} bytes)!")

if __name__ == "__main__":
    build_campaign()
