import fs from 'fs';

const TOTAL_DAYS = 90;
const POSTS_PER_DAY = 4;
const TOTAL_POSTS = TOTAL_DAYS * POSTS_PER_DAY; // 360

const TIME_SLOTS = [
  { name: 'Morning', localTime: '08:00 AM', mdtHour: 14, mstHour: 15, minute: 0 },
  { name: 'Midday', localTime: '12:00 PM', mdtHour: 18, mstHour: 19, minute: 0 },
  { name: 'Afternoon', localTime: '03:30 PM', mdtHour: 21, mstHour: 22, minute: 30 },
  { name: 'Evening', localTime: '07:00 PM', mdtHour: 1, mstHour: 2, minute: 0, nextDayUtc: true }
];

const PILLARS = [
  {
    slot: 1,
    name: 'Personal Mentorship & Executive Leadership',
    eyebrow: 'LEADERSHIP EXCELLENCE',
    hashtags: '#PersonalMentorship #ExecutiveLeadership #ChampionMindset #LornetteDaye #HighPerformance #CareerTransition #EmotionalPoise #LifeCoach #Resilience #Discipline #LeadershipDevelopment #UMATTR'
  },
  {
    slot: 2,
    name: "Lornette's Foundations (Athlete Development)",
    eyebrow: 'ATHLETE DEVELOPMENT',
    hashtags: '#LornettesFoundations #AthleteDevelopment #BetterPeopleBetterPlayers #SportsLeadership #YouthAthletes #NextGen #HighPerformance #CoachingExcellence #SportsPsychology #CharacterFirst #UMATTR'
  },
  {
    slot: 3,
    name: 'UMATTR Academy (Applied AI & Skills)',
    eyebrow: 'APPLIED AI EDUCATION',
    hashtags: '#UMATTRAcademy #AIEducation #FutureOfWork #WorkforceReadiness #AIForBusiness #PracticalAI #SkillsForTomorrow #CareerIntelligence #ContinuousLearning #TechLeadership #Innovation'
  },
  {
    slot: 4,
    name: 'Business Management, AI & Web Growth',
    eyebrow: 'BUSINESS & WEB GROWTH',
    hashtags: '#UMATTRBusiness #AIWorkflows #DigitalTransformation #BusinessGrowth #WebsiteDesign #OperationalExcellence #ModernEnterprise #Entrepreneurship #WebDevelopment #AIStrategy'
  }
];

// Content bank blueprints for each pillar to produce 90 distinct angles per pillar
const MENTORSHIP_TOPICS = [
  "Why High Achievers Stall Without Objective Feedback",
  "The Anatomy of Composure When Markets Shift",
  "Identity Beyond Title: Building Unshakeable Self-Worth",
  "The Solitary Grind of Decision-Making at the Top",
  "Discipline Systems Over Fleeting Motivation",
  "The Cost of Hesitation: How Fear Masks as Preparation",
  "Emotional Regulation in Hostile Boardrooms",
  "Navigating High-Stakes Career Pivots with Dignity",
  "How to Separate Feedback from Personal Attack",
  "Building an Inner Circle That Challenges Your Assumptions",
  "The Difference Between Being Busy and Building Legacy",
  "Recovering After Public Setbacks and Failed Ventures",
  "The Executive Reset: Reclaiming Your Morning Standard",
  "Why Clarity of Purpose Trumps Raw Ambition Every Time",
  "The Art of Strategic Silence in Negotiation",
  "Managing Overwhelm Through Deliberate Boundary Contracts",
  "Sustaining Peak Energy Across Decades of Leadership",
  "The Courage to Say No to Good Opportunities for Great Ones",
  "Overcoming Imposter Syndrome with Banked Repetitions",
  "Leading with Calm Authority in High-Velocity Environments",
  "The Power of Daily Reflection in Compounding Wisdom",
  "Reframing Stress as a Signal of Biological Readiness",
  "Why Consistency Beats Sporadic Brilliance Every Single Time",
  "Building Psychological Resilience Before Crisis Strikes",
  "The Mentor Standard: How Great Leaders Cultivate Successors",
  "Turning Pressure into Precision Under Scrutiny",
  "Breaking the Cycle of Reactive Management",
  "How Olympic Champions View Recovery as Competitive Advantage",
  "The Loneliness of Leadership and Finding Trusted Anchors",
  "Mastering the Mental Pivot When Strategy Collapses"
];

const FOUNDATIONS_TOPICS = [
  "Foundation 1: Identity Beyond Sport and the Transferable Self",
  "Foundation 2: The Champion Mindset Under Pressure",
  "Foundation 3: Structured Discipline Systems That Endure",
  "Foundation 4: Resilience After Crushing Setbacks",
  "Foundation 5: Emotional Regulation and Nervous System Poise",
  "Foundation 6: Communication and Commanding Presence",
  "Foundation 7: Building Rock-Solid Family and Team Support",
  "Foundation 8: Career and Financial Literacy for Competitors",
  "Foundation 9: Protecting Your Story and Personal Brand",
  "Foundation 10: Building Community Impact That Outlives the Score",
  "The Parent Playbook: Supporting Ambition Without Pressure",
  "Why Elite Athletes Must Learn to Decouple Worth From Wins",
  "The Pre-Competition Anchor: Establishing Repeatable Routines",
  "Overcoming Injury: The Psychological Battle of the Sideline",
  "How Subtle Body Language Dictates Competitor Mindset",
  "Next Play Mentality: Erasing Mistakes Before the Whistle",
  "Building Long-Term Athletic Trajectories Without Burnout",
  "The Micro-Habits of Championship Locker Rooms",
  "Why Character Flaws Magnify Under Tournament Pressure",
  "The Coach Contract: Developing the Person Before the Player",
  "Managing Social Media Distractions in Competitive Seasons",
  "Turning Scouting Feedback into Structured Action Plans",
  "The Myth of Overnight Greatness: 10,000 Unseen Repetitions",
  "How Poise on the Practice Court Translates to Clutch Victories",
  "Nutrition, Sleep, and Nervous System Recovery for Youth Athletes",
  "Cultivating Mental Stamina for Back-to-Back Showdowns",
  "The Power of Positive Self-Talk Under Exhaustion",
  "Navigating Roster Cuts, Demotions, and Depth Chart Adversity",
  "Why Foundations Matter More Than Tactical Gimmicks",
  "Better People Always Make Better Players on and off the Ice"
];

const ACADEMY_TOPICS = [
  "Closing the Capability Gap: Practical AI for Real Teams",
  "Beyond Chatbots: How Foundation Models Reshape Daily Work",
  "Workforce Intelligence: Equipping Teams to Think Alongside AI",
  "Hands-On Applied Projects: Why Theory Alone Fails in AI",
  "Building Practical Prompting Frameworks for Research and Analysis",
  "The 4 Levels of AI Literacy Every Professional Must Master",
  "Automating Tedious Workflows to Unlock Creative Strategy",
  "Why Every Career Now Demands Applied Intelligence Skills",
  "Data Privacy, Compliance, and Ethical AI Adoption in Practice",
  "Demystifying Large Language Models for Non-Technical Leaders",
  "Accelerating Research Synthesis: From Hours to Seconds",
  "The Modern Knowledge Worker Playbook for 2027 and Beyond",
  "Developing Custom GPT Assistants for Niche Business Workflows",
  "How Continuous Learning Protects Your Career Longevity",
  "The Bridge Between Human Intuition and Machine Precision",
  "Mastering Document Analysis and Automated Fact Extraction",
  "Why Organizations That Upskill First Dominate Market Share",
  "AI for Non-Profits, Educators, and Community Organizations",
  "Evaluating AI Tool Stacks: Separating Hype from Practical Utility",
  "Building Repeatable AI Systems for Customer Inquiry Routing",
  "The Executive Primer on AI Governance and Risk Mitigation",
  "How Small Teams Out-Execute Massive Enterprises with AI",
  "Practical Structured Output: Moving from Text to Automated Data",
  "The UMATTR Academy Roadmap: Skills Designed for Immediate Use",
  "AI for Creative Professionals: Expanding Imagination, Not Replacing It",
  "Turning Unstructured Customer Feedback into Product Roadmaps",
  "The Future of Professional Credentialing in an AI-First World",
  "Collaborative Human-in-the-Loop Workflows That Actually Scale",
  "Hands-On AI Labs: Why Immediate Execution Compounds Retention",
  "Your Career Future Is Created Today: Step Into the Academy"
];

const BUSINESS_TOPICS = [
  "Why Great Products Fail Without Modern Digital Presentation",
  "Streamlining Operations: Eliminating Friction in Customer Journeys",
  "Turning Website Visitors into Qualified Business Inquiries",
  "Automated Lead Capture That Protects Your Sales Pipeline",
  "Mobile-First Experiences: The Non-Negotiable Standard",
  "Integrating AI Consulting to Solve Real Operational Bottlenecks",
  "Modernizing Legacy Business Workflows Without Chaos",
  "The Anatomy of a High-Converting Luxury Digital Storefront",
  "Data-Driven Decisions: Listening to Real User Engagement Metrics",
  "Why Your Brand Voice Must Remain Authoritative Across Every Touchpoint",
  "Reducing Customer Acquisition Costs Through Organic Value Funnels",
  "The Operational Audit: Identifying Hidden Time Drains in Your Business",
  "Custom Web Architecture Built for Speed, Accessibility, and Trust",
  "Aligning Workforce Capabilities with Technological Infrastructure",
  "How Strategic Business Consulting Unlocks Untapped Revenue Streams",
  "The Power of Clear Positioning: Standing Out in Noisy Markets",
  "Automating Repetitive Admin Tasks so Founders Can Focus on Vision",
  "Building Digital Trust: Speed, Security, and Flawless Presentation",
  "Transforming Consultative Expertise into Scalable Digital Products",
  "Why Customer Retention Begins with Seamless Onboarding Systems",
  "The Small Business Playbook for Enterprise-Grade AI Deployment",
  "Designing Websites That Educate, Convince, and Convert 24/7",
  "From Fragmented Tools to an Integrated Business Operating System",
  "The ROI of Professional Presentation: Why First Impressions Compound",
  "Scaling B2B Partnerships with Structured Pipeline Management",
  "Crafting Clear Call-to-Actions That Remove Customer Hesitation",
  "The Sustainable Growth Engine: Aligning Systems, Team, and Tech",
  "Modernizing Your Company Brand to Reflect Elite Standards",
  "Building Resilient Systems That Run Smoothly Without the Founder",
  "Create Your Future: Uniting Leadership Wisdom with Digital Execution"
];

const TOPIC_ARRAYS = [MENTORSHIP_TOPICS, FOUNDATIONS_TOPICS, ACADEMY_TOPICS, BUSINESS_TOPICS];

// Generate the 360 posts
const posts = [];
const startDate = new Date('2026-10-29T00:00:00.000Z');

for (let day = 0; day < TOTAL_DAYS; day++) {
  const currentDate = new Date(startDate.getTime() + day * 24 * 60 * 60 * 1000);
  const dateStr = currentDate.toISOString().split('T')[0];
  
  // Format human date
  const options = { weekday: 'long', year: 'numeric', month: 'short', day: 'numeric' };
  const humanDate = currentDate.toLocaleDateString('en-US', options);

  // Check if DST ended (Nov 1, 2026 is Day 3)
  // In Alberta, DST ends Sunday Nov 1, 2026 at 2:00 AM MDT -> MST (UTC-7)
  const isMst = currentDate >= new Date('2026-11-01T08:00:00.000Z');
  const timezoneStr = isMst ? 'MST' : 'MDT';

  for (let slotIdx = 0; slotIdx < POSTS_PER_DAY; slotIdx++) {
    const postNumber = day * POSTS_PER_DAY + slotIdx + 1;
    const slotInfo = TIME_SLOTS[slotIdx];
    const pillarInfo = PILLARS[slotIdx];
    
    // Calculate UTC dueAt
    const hour = isMst ? slotInfo.mstHour : slotInfo.mdtHour;
    let dueAtDate = new Date(currentDate);
    if (slotInfo.nextDayUtc) {
      dueAtDate = new Date(currentDate.getTime() + 24 * 60 * 60 * 1000);
    }
    const yyyy = dueAtDate.getUTCFullYear();
    const mm = String(dueAtDate.getUTCMonth() + 1).padStart(2, '0');
    const dd = String(dueAtDate.getUTCDate()).padStart(2, '0');
    const hh = String(hour).padStart(2, '0');
    const min = String(slotInfo.minute).padStart(2, '0');
    const dueAt = `${yyyy}-${mm}-${dd}T${hh}:${min}:00.000Z`;

    // Visual asset: rotate through sports-01.png to sports-20.png
    const assetIndex = ((postNumber - 1) % 20) + 1;
    const assetName = `sports-${String(assetIndex).padStart(2, '0')}.png`;
    const assetUrl = `https://lornettedaye.com/campaigns/foundations-sports/${assetName}`;

    // Topic selection (loops through 30 topics for 3 full cycles of 30)
    const topicBank = TOPIC_ARRAYS[slotIdx];
    const topic = topicBank[day % topicBank.length];

    // Build unique, engaging caption
    const caption = buildCaption({
      postNumber,
      dayNumber: day + 1,
      slotName: slotInfo.name,
      pillarName: pillarInfo.name,
      eyebrow: pillarInfo.eyebrow,
      topic,
      hashtags: pillarInfo.hashtags
    });

    posts.push({
      id: postNumber,
      day: day + 1,
      slot: slotInfo.name,
      time: `${slotInfo.localTime} ${timezoneStr}`,
      date: humanDate,
      dueAt,
      pillar: pillarInfo.name,
      topic,
      assetName,
      assetUrl,
      caption
    });
  }
}

function buildCaption({ postNumber, dayNumber, slotName, pillarName, eyebrow, topic, hashtags }) {
  let hook, body, takeaway, question;

  if (pillarName.includes('Mentorship')) {
    hook = `${eyebrow}: ${topic.toUpperCase()}.

When pressure intensifies, leaders do not rise to the level of their hopes. They sink to the level of their preparation.`;
    body = `Throughout four decades of coaching national champions and guiding ambitious leaders, I have observed one undeniable law: true greatness requires objective, candid guidance in the corners where you cannot see yourself.

Mentorship is not about passive cheerleading. It is about structured accountability, emotional poise, and aligning your daily habits with your ultimate vision.`;
    takeaway = `THE LEADERSHIP REALITY:
You cannot navigate your biggest challenges with the same perspective that created them. An experienced mentor cuts through the noise, sharpens your focus, and ensures your foundation is built to withstand pressure.`;
    question = `To founders and executives: What is the single biggest operational or personal hurdle currently demanding your focus? Let us connect below.`;
  } else if (pillarName.includes('Foundations')) {
    hook = `${eyebrow}: ${topic.toUpperCase()}.

Talent might open the initial door. Only uncompromised character and solid systems keep you inside the room.`;
    body = `At Lornette's Foundations, we work with athletes across hockey, golf, and competitive sports to build complete competitors. We believe that athletic performance is an outward reflection of internal discipline, recovery habits, and emotional poise.

When you master your foundation, pressure transforms from a paralyzing threat into a catalyst for peak execution.`;
    takeaway = `THE FOUNDATION STANDARD:
Better people make better players. When you invest in identity, mental regulation, and long-term habits, victories become the natural byproduct of who you have become.`;
    question = `Athletes, parents, and coaches: Which pillar of performance preparation do you believe is most overlooked in competitive youth sports today?`;
  } else if (pillarName.includes('Academy')) {
    hook = `${eyebrow}: ${topic.toUpperCase()}.

The modern workplace is not being disrupted by artificial intelligence. It is being accelerated by those who learn to apply it with clarity.`;
    body = `The gap between talking about AI and applying it to generate tangible results is widening every single week. At UMATTR Academy, we focus on hands-on, practical learning across Foundations, Work, Business, and Career Intelligence.

You do not need to be a software engineer to harness machine intelligence. You simply need practical systems, guided frameworks, and the courage to build new capabilities.`;
    takeaway = `THE CAPABILITY PRINCIPLE:
Real innovation happens when human domain expertise pairs with intelligent tools. Invest in your skills before the marketplace demands it.`;
    question = `Professionals and team leads: What repetitive task in your daily workflow would you most like to automate with AI this quarter?`;
  } else {
    hook = `${eyebrow}: ${topic.toUpperCase()}.

A great vision without seamless digital presentation is an opportunity waiting to be overlooked.`;
    body = `In today's fast-moving business climate, your digital footprint is your primary storefront. From high-converting web architecture to automated customer inquiry workflows, your operational systems must work as hard as you do.

Through UMATTR Business and Website Services, we help entrepreneurs modernize workflows, eliminate bottlenecks, and build reliable digital engines that turn attention into sustained revenue.`;
    takeaway = `THE GROWTH CONTRACT:
Scale does not come from working longer hours. It comes from building intelligent infrastructure that serves your clients with speed and precision 24 hours a day.`;
    question = `Entrepreneurs: When was the last time you critically audited your website mobile experience and customer conversion path?`;
  }

  const directoryBlock = `DISCOVER THE FOUR CONNECTED OPPORTUNITIES:
- Personal Mentorship: https://lornettedaye.com/mentorship
- Lornette's Foundations: https://lornettedaye.com/foundations
- UMATTR AI Academy: https://www.umattr.ca/academy
- Business, AI & Web Growth: https://www.umattr.ca/business`;

  return `${hook}

${body}

${takeaway}

${directoryBlock}

${question}

${hashtags}`;
}

// Invariant assertions: ZERO asterisks and ZERO em dashes
let valid = true;
posts.forEach(p => {
  if (p.caption.includes('*')) {
    console.error(`ERROR: Post ${p.id} contains asterisks!`);
    valid = false;
  }
  if (p.caption.includes('—') || p.caption.includes('\u2014')) {
    console.error(`ERROR: Post ${p.id} contains em dashes!`);
    valid = false;
  }
  if (!p.caption.includes('https://lornettedaye.com/mentorship')) {
    console.error(`ERROR: Post ${p.id} missing mentorship URL!`);
    valid = false;
  }
  if (!p.caption.includes('https://lornettedaye.com/foundations')) {
    console.error(`ERROR: Post ${p.id} missing foundations URL!`);
    valid = false;
  }
  if (!p.caption.includes('https://www.umattr.ca/academy')) {
    console.error(`ERROR: Post ${p.id} missing academy URL!`);
    valid = false;
  }
  if (!p.caption.includes('https://www.umattr.ca/business')) {
    console.error(`ERROR: Post ${p.id} missing business URL!`);
    valid = false;
  }
});

if (!valid) {
  process.exit(1);
}

fs.writeFileSync('scripts/master-foundations-umattr-queue.json', JSON.stringify(posts, null, 2));
console.log(`Generated and validated master queue with ${posts.length} posts!`);
