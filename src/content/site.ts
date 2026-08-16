import type { Metadata } from "next";
import type { StaticImageData } from "next/image";

import alternatePortrait from "../../images/chrome_nRMcvAaFwK.png";
import monogram from "../../images/Beige & Black Elegant Typography Monogram Initials AP Logo_20251127_172032_0000.png";
import featuredOnCollage from "../../images/chrome_pclmdSgQoj.png";
import brandStatement from "../../images/c298ebb1-01e5-497d-a41e-33c2dba1b74c.png";
import podcastCard from "../../images/588657892_17845278915616562_7038671232751376482_n.jpg";
import diversityAwardAcceptance from "../../images/diversity-awards-acceptance.png";
import speakingPoster from "../../images/unnamed (6).jpg";
import leadershipPoster from "../../images/Gemini_Generated_Image_ekc5q1ekc5q1ekc5.png";
import inclusionPoster from "../../images/unnamed (3).jpg";
import mentorshipPoster from "../../images/Gemini_Generated_Image_tpd8xftpd8xftpd8.png";
import athletePoster from "../../images/unnamed (5).jpg";
import athleteInfoPoster from "../../images/Gemini_Generated_Image_6dpu516dpu516dpu.png";
import athleteStrategyPoster from "../../images/Gemini_Generated_Image_imi2b2imi2b2imi2.png";
import aboutTimelinePoster from "../../images/Gemini_Generated_Image_gwugscgwugscgwug.png";
import recognitionDiversityAward from "../../images/recognition-diversity-awards.png";
import mediaThumbnail from "../../images/unnamed (48).jpg";
import testimonialComposite from "../../images/unnamed (19).jpg";
import testimonialYouth from "../../images/unnamed (21).jpg";
import programOverview from "../../images/unnamed (7).jpg";
import eventWorkshop from "../../images/unnamed (1).jpg";
import trainingPoster from "../../images/unnamed (8).jpg";
import resiliencePoster from "../../images/unnamed (4).jpg";
import blogSource from "../../images/unnamed (47).jpg";
import blogNature from "../../images/unnamed (50).jpg";
import blogVulnerability from "../../images/unnamed (51).jpg";
import survivalSkillsMen from "../../images/unnamed (45).jpg";
import survivingLife from "../../images/SURVIVING LIFE.jpg";
import roadBook from "../../images/road.jpg";
import womensBook from "../../images/womensbook.jpg";
import toastmastersLogo from "../../images/Toastmasters_2011.png";
import rotaryLogo from "../../images/Rotary-Club-of-St-Albert--1-.jpeg";
import flightPoster from "../../images/image.png";

export const siteUrl = "https://lornettedaye.com";

export type SiteImage = {
  src: StaticImageData | string;
  alt: string;
  crop?: string;
};

export type MediaItem = {
  title: string;
  category: string;
  summary: string;
  image: SiteImage;
  videoSrc?: string;
  duration?: string;
  status?: string;
};

export type NavItem = {
  label: string;
  href: string;
};

export type ServicePage = {
  slug: string;
  navLabel: string;
  title: string;
  eyebrow: string;
  description: string;
  heroImage: SiteImage;
  pillars: string[];
  sections: {
    title: string;
    body?: string;
    items: string[];
  }[];
  cta: string;
};

export type Post = {
  slug: string;
  title: string;
  excerpt: string;
  category: string;
  image: SiteImage;
  date: string;
};

export type BookListing = {
  slug: string;
  title: string;
  subtitle: string;
  description: string;
  audience: string;
  priceLabel: string;
  format: string;
  image: SiteImage;
  purchaseUrl: string;
  stripePaymentLinkId: string;
  highlights: string[];
};

export type SpeakerAppRoute = {
  label: string;
  href: string;
  appTab: "Home" | "Speaking" | "Notes" | "Book";
};

export type SpeakerNotesMode = "private-seeded" | "public-blank";

export type Testimonial = {
  quote: string;
  excerpt: string;
  name: string;
  context: string;
  category: string;
};

export const siteCopy = {
  brandName: "Lornette Daye",
  contactEmail: "lornettedaye@outlook.com",
  seoTitle: "Lornette Daye | Transformational Speaker",
  seoDescription:
    "Keynote speaking, leadership development, inclusion, mentorship, youth development, and performance coaching with Lornette Daye.",
  descriptor:
    "Professional Keynote Speaker | Olympic-level Athlete & Coach | Canadian National Sprint Champion | Certified Transformational Speaker | Author | Youth Leader & Mentor | Project Manager",
  mainMessage:
    "Transforming the lives of others that they can overcome anything because they matter.",
  homepageHeadline: "Transforming Lives. Reminding People They Matter.",
  homepageSubheadline:
    "Professional Keynote Speaker | Olympic-level Athlete & Coach | Canadian National Sprint Champion | Certified Transformational Speaker | Author | Youth Leader & Mentor | Project Manager",
  homepageIntro:
    "For over four decades, Lornette Daye has inspired individuals, teams, and organizations to achieve excellence, resilience, and purpose-driven success through public speaking, leadership development, diversity and inclusion, mentorship, and athlete performance coaching.",
  biography:
    "Certified Toastmasters Speaker, Olympic-level Athlete & Coach, Canadian National Sprint Champion, Author, and Transformational Speaker with over 40 years of experience inspiring individuals, teams, and organizations to achieve excellence, resilience, and purpose-driven success.",
  biographyExtended:
    "Through decades of elite competition and coaching over 500 athletes, including 150+ international competitors, she has developed a profound understanding of performance psychology, mindset mastery, goal-setting, and discipline.",
  mission:
    "Her mission is transforming the lives of others that they can overcome anything because they matter. True success is measured not only by personal accomplishments but by the lives we touch, the communities we strengthen, and the leaders we develop.",
  verifiedClaims: [
    "Professional Keynote Speaker",
    "Olympic-level Athlete & Coach",
    "Canadian National Sprint Champion",
    "Certified Transformational Speaker",
    "Author",
    "Youth Leader & Mentor",
    "Project Manager",
    "Certified Toastmasters Speaker",
    "Former National Track Champion (100m & 200m)",
    "National Coach",
    "Diversity Award Winner",
  ],
  socialLinks: [
    { label: "Instagram", href: "https://www.instagram.com/lornettedaye" },
    { label: "LinkedIn", href: "https://www.linkedin.com/in/lornette-d-419276358" },
    { label: "Email", href: "mailto:lornettedaye@outlook.com" },
  ],
};

export const speakerAppConfig = {
  appName: "LD Speaker",
  androidPackage: "com.lornettedaye.speaker",
  appUrlEnv: "LD_APP_URL",
  notesModeEnv: "LD_NOTES_MODE",
  notesModes: ["private-seeded", "public-blank"] satisfies SpeakerNotesMode[],
  routes: [
    { label: "Home", href: "/", appTab: "Home" },
    { label: "Speaking", href: "/speaking", appTab: "Speaking" },
    { label: "Notes", href: "native://speaker-notes", appTab: "Notes" },
    { label: "Book", href: "/book", appTab: "Book" },
  ] satisfies SpeakerAppRoute[],
  marketingFocus: [
    "Hero promise",
    "Public speaking",
    "About",
    "Programs",
    "Contact and booking",
    "Selective credibility and media proof",
  ],
};

export const mainNav: NavItem[] = [
  { label: "Home", href: "/" },
  { label: "Speaker", href: "/speaking" },
  { label: "Leadership", href: "/leadership" },
  { label: "Books", href: "/books" },
  { label: "Collection", href: "/collection" },
  { label: "Mentorship", href: "/mentorship" },
  { label: "About", href: "/about" },
  { label: "Media", href: "/media" },
  { label: "Blog", href: "/blog" },
  { label: "Book Lornette", href: "/book" },
];

export const requiredRoutes = [
  "/",
  "/speaking",
  "/leadership",
  "/inclusion",
  "/mentorship",
  "/athlete-coaching",
  "/about",
  "/media",
  "/recognition",
  "/books",
  "/collection",
  "/impact",
  "/programs",
  "/events",
  "/blog",
  "/blog/the-champion-mindset",
  "/speaker-kit",
  "/book",
];

export const images = {
  heroPortrait: {
    src: "/generated/lornette-hero-reference.png",
    alt: "Portrait-style speaker image of Lornette Daye in an ivory blazer.",
    crop: "object-center",
  },
  alternatePortrait: {
    src: alternatePortrait,
    alt: "Close portrait of Lornette Daye.",
    crop: "object-center",
  },
  monogram: {
    src: monogram,
    alt: "Lornette Daye monogram supplied in brand assets.",
  },
  signatureBlack: {
    src: "/ld-signature-black.png",
    alt: "Black Lornette Daye LD signature mark.",
  },
  featuredOn: {
    src: featuredOnCollage,
    alt: "Brand-provided collage of organizations and media references for review.",
    crop: "object-bottom scale-[1.04]",
  },
  brandStatement: {
    src: brandStatement,
    alt: "Lornette Daye speaker brand artwork cropped to the portrait area.",
    crop: "object-[76%_44%] scale-[1.78]",
  },
  podcastCard: {
    src: podcastCard,
    alt: "Podcast appearance artwork featuring Lornette Daye.",
    crop: "object-top scale-[1.12]",
  },
  diversityAwardAcceptance: {
    src: diversityAwardAcceptance,
    alt: "Lornette Daye accepting recognition at a Diversity Awards event.",
    crop: "object-top",
  },
  recognitionDiversityAward: {
    src: recognitionDiversityAward,
    alt: "Diversity Awards Friends of Diversity recognition artwork featuring Lornette Daye.",
    crop: "object-[50%_52%] scale-[1.02]",
  },
  toastmastersLogo: {
    src: toastmastersLogo,
    alt: "Toastmasters International logo supplied in project assets.",
  },
  rotaryLogo: {
    src: rotaryLogo,
    alt: "Rotary Club of St. Albert logo supplied in project assets.",
  },
};

export const metrics = [
  { value: "40+", label: "Years of Inspiring Impact" },
  { value: "500+", label: "Athletes Coached" },
  { value: "150+", label: "International Competitors" },
  { value: "Global", label: "Impact" },
];

export const audienceTypes = [
  "Universities",
  "Schools",
  "Athletic associations",
  "Nonprofit organizations",
  "Government agencies",
  "Corporate teams",
];

export const services = [
  {
    title: "Public Speaking",
    body: "Dynamic keynotes that motivate, educate, and leave a lasting impact.",
    href: "/speaking",
  },
  {
    title: "Leadership Development",
    body: "Build confident leaders who inspire, influence, and drive results.",
    href: "/leadership",
  },
  {
    title: "Diversity & Inclusion",
    body: "Create inclusive cultures where everyone belongs and thrives.",
    href: "/inclusion",
  },
  {
    title: "Athlete & Performance Coaching",
    body: "Train the mindset, discipline, and habits behind repeatable performance.",
    href: "/athlete-coaching",
  },
  {
    title: "Mentorship and Youth Development",
    body: "Empower the next generation to dream bigger and lead boldly.",
    href: "/mentorship",
  },
  {
    title: "Resilience & Mindset Coaching",
    body: "Help audiences turn pressure, change, and setbacks into growth.",
    href: "/programs",
  },
  {
    title: "Training",
    body: "Actionable workshops for practical skills and measurable momentum.",
    href: "/events",
  },
  {
    title: "Life Coaching",
    body: "Purpose-centered support for clarity, confidence, and next steps.",
    href: "/programs",
  },
];

export const servicePages: Record<string, ServicePage> = {
  speaking: {
    slug: "/speaking",
    navLabel: "Speaking",
    title: "Powerful Messages. Lasting Impact.",
    eyebrow: "Speaking / Keynotes",
    description:
      "Signature keynotes and facilitated sessions that connect resilience, leadership, purpose, and action.",
    heroImage: {
      src: speakingPoster,
      alt: "Transformational public speaking artwork, cropped to keep the focus on the stage visual.",
      crop: "object-center scale-[1.58]",
    },
    pillars: [
      "The Champion Mindset",
      "Purpose in Motion",
      "Leadership That Lasts",
      "Inclusion in Action",
      "Rise Above Adversity",
    ],
    sections: [
      {
        title: "Audiences served",
        items: [
          "Schools & Students",
          "Corporate Teams & Organizations",
          "Athletic Clubs",
          "Community & Nonprofit Organizations",
          "Faith-based Events",
        ],
      },
      {
        title: "Audience outcomes",
        items: [
          "Elevated mindset",
          "Stronger leadership",
          "Shared purpose",
          "Practical next steps",
        ],
      },
      {
        title: "Formats",
        items: ["Keynotes", "Workshops", "Panels", "Virtual/Hybrid", "Retreats"],
      },
    ],
    cta: "Bring Lornette's Message to Your Next Event",
  },
  leadership: {
    slug: "/leadership",
    navLabel: "Leadership",
    title: "Leadership That Builds Resilience, Confidence, and Results.",
    eyebrow: "Leadership Development",
    description:
      "Practical leadership development for people who need to communicate, execute, and lead with composure under pressure.",
    heroImage: {
      src: leadershipPoster,
      alt: "Leadership development artwork with gold staircase, cropped to focus on the main visual.",
      crop: "object-[50%_60%] scale-[1.65]",
    },
    pillars: [
      "Strategic Thinking",
      "Self-Accountability",
      "Communication Excellence",
      "Team Cohesion",
      "Resilience Under Pressure",
    ],
    sections: [
      {
        title: "Program overview",
        items: [
          "Decision-making clarity",
          "High-trust communication",
          "Accountability without shame",
          "Resilient execution habits",
        ],
      },
      {
        title: "Outcomes",
        items: [
          "Clearer standards",
          "Stronger teams",
          "Better performance conversations",
          "Purpose-driven action",
        ],
      },
      {
        title: "Workshop cards",
        items: [
          "Leading Through Pressure",
          "Communication That Builds Trust",
          "Execution With Purpose",
        ],
      },
    ],
    cta: "Schedule a Leadership Consultation",
  },
  inclusion: {
    slug: "/inclusion",
    navLabel: "Inclusion",
    title: "Inclusion in Action. Belonging That Drives Performance.",
    eyebrow: "Diversity & Inclusion",
    description:
      "Grounded conversations and workshops that connect belonging, collaboration, and human dignity without empty buzzwords.",
    heroImage: {
      src: inclusionPoster,
      alt: "Diversity and inclusion artwork, cropped to focus on the abstract connection visual.",
      crop: "object-center scale-[1.45]",
    },
    pillars: ["Diversity", "Inclusion", "Belonging", "Collaboration", "Equity"],
    sections: [
      {
        title: "Workshop themes",
        items: [
          "Listening across difference",
          "Building trust in mixed rooms",
          "Belonging in everyday behavior",
          "Leadership accountability",
        ],
      },
      {
        title: "Expected outcomes",
        items: [
          "Stronger engagement",
          "More honest collaboration",
          "Improved psychological safety",
          "Clearer team standards",
        ],
      },
      {
        title: "Who she partners with",
        items: ["Schools", "Community organizations", "Teams", "Public-sector groups"],
      },
    ],
    cta: "Explore Inclusion Workshops",
  },
  mentorship: {
    slug: "/mentorship",
    navLabel: "Mentorship",
    title: "Mentorship That Builds Leaders for Life.",
    eyebrow: "Mentorship & Youth Development",
    description:
      "Youth-focused mentorship and development experiences that help young people build discipline, confidence, and self-belief.",
    heroImage: {
      src: mentorshipPoster,
      alt: "Mentorship and youth development artwork, cropped to focus on the gold pathway visual.",
      crop: "object-[50%_72%] scale-[2.05]",
    },
    pillars: [
      "One-on-One Mentoring",
      "Youth Leadership Sessions",
      "Athlete Mindset Coaching",
      "School & Group Programs",
      "Family & Community Impact",
    ],
    sections: [
      {
        title: "Mentorship process",
        items: ["Discover", "Develop", "Empower", "Elevate"],
      },
      {
        title: "Youth outcomes",
        items: [
          "Stronger self-belief",
          "Better habits under pressure",
          "Clearer personal goals",
          "Healthy accountability",
        ],
      },
      {
        title: "Program settings",
        items: ["Schools", "Teams", "Community groups", "Family-centered events"],
      },
    ],
    cta: "Build a Youth Development Program",
  },
  "athlete-coaching": {
    slug: "/athlete-coaching",
    navLabel: "Athlete Coaching",
    title: "Elite Performance. Everyday Discipline.",
    eyebrow: "Athlete & Performance Coaching",
    description:
      "Performance psychology, sprint champion mindset, preparation, resilience, teamwork, and goal-setting for athletes and coaches.",
    heroImage: {
      src: athletePoster,
      alt: "Athlete and performance coaching artwork, cropped to focus on the motion and performance visual.",
      crop: "object-center scale-[1.42]",
    },
    pillars: [
      "Athlete mindset",
      "Mental toughness",
      "Discipline and preparation",
      "Team performance",
      "Coaching outcomes",
    ],
    sections: [
      {
        title: "Performance translation",
        items: [
          "Goal-setting systems",
          "Pressure preparation",
          "Communication between athletes and coaches",
          "Repeatable performance habits",
        ],
      },
      {
        title: "Coaching outcomes",
        items: [
          "Stronger focus",
          "Better preparation",
          "Resilient team standards",
          "Confidence under pressure",
        ],
      },
      {
        title: "Visual resources",
        items: [
          "Elite performance begins at the mental level",
          "Strategy. Leadership. Elite Execution",
          "Champion mindset development",
        ],
      },
    ],
    cta: "Inquire About Performance Coaching",
  },
};

export const testimonials: Testimonial[] = [
  {
    quote:
      "Lornette is a passionate track coach. She encouraged my daughter to step up to the challenges of becoming a noteworthy track athlete by building a very good rapport with her and by making her set up track goals for herself which she held her accountable for. As a Life coach and Transformational Speaker, she indeed changes lives by drawing on vast life experiences and actionable insights that not only leave persons motivated but also leads to profound shifts in mindsets and behavior patterns. I find in her a good friend, always understanding, honest and trustworthy and would recommend Lornette any day.",
    excerpt:
      "As a Life coach and Transformational Speaker, she indeed changes lives by drawing on vast life experiences and actionable insights.",
    name: "Ayo",
    context: "Professional",
    category: "Coaching & Transformation",
  },
  {
    quote:
      "I have witnessed countless business and motivational speakers over my career of 15 years. Lornette you are flat-out top of the charts for your ability to connect and interact with your audience to deliver a powerful message and generate positive change. Your takeaways were simple and easy to implement immediately. Lornette, you care about your audience and it was evident from your prepared work and customization before the presentation. Thank you for the keynote. Many were touched by your story and your success and felt honored that you came to speak to them. Your message was powerful and gave us an insight to refocus our energy on good effects and free ourselves from harmful ones. It was also timely and essential to the audience. I look forward to working with you again.",
    excerpt:
      "Lornette, you are flat-out top of the charts for your ability to connect and interact with your audience to deliver a powerful message.",
    name: "Harriet Tinka",
    context: "Founder/CEO, Bestselling Author, Turning Point Expert, Empowered Me Inc",
    category: "Keynote Speaking",
  },
  {
    quote:
      "The first time I met Lornette we connected right away but I did not know what the connection meant. As we got to know each other and she shared with me her life journey I understood the connection. Lornette overcame challenges and she shared how her faith and coaching helped her to manage. I listened to her share about coaching and how she incorporates her faith as a daily practice with coaching and encouraging the young people she coaches to sweat it out. I thought that is a good strategy to physically sweat it out because it releases the stress. I got so motivated to be physically active. I then started walking and incorporating prayer as part of my walk. I would share with Lornette about my experience about my prayer walk and she encouraged me to increase the intensity and speed slowly, which I did and now I have been consistent with very brisk walking daily and including prayer and reflection as part of my walk. Lornette encouraged me and when I felt tired I would hear her beautiful voice gently reminding me to just sweat it out and I also hear her laughter when I tell her I have done it. She has a beautiful contagious laughter that even when you are tired you cannot help but to laugh as well.",
    excerpt:
      "Lornette encouraged me to increase the intensity and speed slowly, and now I have been consistent with very brisk walking daily.",
    name: "Carol",
    context: "Audience testimonial",
    category: "Faith & Wellness",
  },
  {
    quote:
      "Lornette is truly an inspiration to today's youth. She is an exceptional track coach truly dedicated, and cares deeply for her athletes' futures. Lornette was my daughter's track coach for a few years while she was in middle school and high school, and taught her so much about focusing on goals, staying dedicated, and believing in herself. Her confidence during high school track competitions soared, which helped her succeed greatly as part of her three-time Metro-Edmonton Gold-Medal winning girls' relay team. My daughter's main reason why we turned to Lornette in the first place was to help her with her speed for her main sport, soccer. Lornette's impressive training sessions and motivational guidance helped a great deal. My daughter is now a varsity soccer player while in university, a key goal she had while she was a youth, and her coaches often comment on her impressive speed on the field. I highly recommend Lornette as a youth track coach and mentor.",
    excerpt:
      "Lornette is truly an inspiration to today's youth. She is an exceptional track coach, truly dedicated, and cares deeply for her athletes' futures.",
    name: "Shawna Randolph",
    context: "Youth coaching testimonial",
    category: "Youth Coaching",
  },
];

export const mediaItems: MediaItem[] = [
  {
    title: "Speaker Reel",
    category: "Keynotes",
    summary: "Primary speaker reel for event planners reviewing Lornette's message, presence, and audience fit.",
    image: {
      src: "/generated/speaker-reel-reference.png",
      alt: "Speaker reel thumbnail showing Lornette Daye on a keynote stage.",
      crop: "object-center",
    },
    videoSrc: "/media/speaker-reel.mp4",
    duration: "1:51",
  },
  {
    title: "Recent Speaking Short",
    category: "Interviews",
    summary: "Approved public YouTube short for reviewing Lornette's recent speaking presence and audience-facing message.",
    image: images.podcastCard,
    videoSrc: "https://youtube.com/shorts/kkQw4iC2QgU?feature=share",
    duration: "Short",
  },
  {
    title: "Speaker Message Clip",
    category: "Short Insights",
    summary: "Approved public YouTube clip that supports speaker-bureau review and booking conversations.",
    image: {
      src: "/media/frames/speaker-reel-20.jpg",
      alt: "Still frame from the supplied speaker reel video.",
      crop: "object-[50%_28%]",
    },
    videoSrc: "https://youtu.be/n8bzPA16hjw?si=fH7C44WRPIQ7B0Ww",
    duration: "YouTube",
  },
  {
    title: "Performance Coaching Preview",
    category: "Keynotes",
    summary: "A future clip area for athletic mindset, discipline, and performance coaching.",
    image: {
      src: athletePoster,
      alt: "Athlete and performance coaching artwork, cropped to remove footer social icons.",
      crop: "object-top scale-[1.12]",
    },
    status: "Clip pending",
  },
  {
    title: "Diversity Award Recognition",
    category: "Featured Appearances",
    summary: "Recognition artwork for Friends of Diversity, supporting Lornette's inclusion and community-impact platform.",
    image: images.recognitionDiversityAward,
    status: "Recognition",
  },
  {
    title: "Podcast Holding Card",
    category: "Podcasts",
    summary: "Podcast and interview area ready for approved audio or video links.",
    image: {
      src: mediaThumbnail,
      alt: "Speaker reel and media thumbnail artwork cropped as a podcast holding card.",
      crop: "object-top",
    },
    status: "Audio pending",
  },
];

export const speakerSubmissionProfile = {
  role:
    "Former National Track Champion (100m & 200m) | National Coach | Diversity Award Winner | Motivational Speaker | Thought Leader",
  travelingFrom: "Alberta, Canada",
  expertise: [
    "Elite athletic achievement",
    "National coaching leadership",
    "Diversity, equity, and inclusion",
    "Mental resilience and performance",
    "Fitness, identity, and purpose",
    "Faith-based leadership",
    "Start-up business and community building",
    "Authorship and personal growth",
  ],
  biography: [
    "Lornette Daye is a former track athlete, national coach, Diversity Award Winner, author, and motivational speaker whose credibility is grounded in elite athletic achievement, lived resilience, decades of mentorship, and measurable community impact.",
    "Her athletic background includes multiple national and Western Canada Games titles in the 100m and 200m sprints, along with provincial and city championships. Her career as an elite athlete took her across Canada, the United States, and Europe, including Poland and Germany.",
    "As a Black athlete in the 1970s, Lornette experienced tremendous adversity, including housing insecurity and discrimination. Those challenges became part of the foundation for her message on resilience, identity, faith, courage, and helping younger athletes rise through similar struggles.",
    "Across decades as an elite competitor, national coach, entrepreneur, mentor, and author, Lornette has built the authority to speak to schools, organizations, churches, women, youth, athletes, founders, and community leaders who need practical tools for confidence, resilience, and purpose.",
  ],
  primaryKeynote: {
    title: "Road to the Olympics: Lessons Learned as an Elite Athlete",
    description:
      "Everybody wants to achieve great things, but few are equipped to overcome the obstacles that inevitably appear along the way. In this keynote, audiences gain tools and strategies drawn directly from championship-level competition, learning how to rise above adversity while maintaining perspective, discipline, and self-esteem.",
    fit:
      "Tailored for corporate, faith-based, youth, women's, athletic, community, and leadership audiences.",
    attendeeResults: [
      "Understand how foundational experiences shape elite outcomes.",
      "Develop a disciplined strategy for sustaining confidence and motivation.",
      "Recognize how adversity builds character and competitive advantage.",
      "Apply principles of focus, giving, and clarity to long-term success.",
    ],
  },
  videoLinks: [
    {
      label: "Recent Speaking Short",
      href: "https://youtube.com/shorts/kkQw4iC2QgU?feature=share",
    },
    {
      label: "Speaker Message Clip",
      href: "https://youtu.be/n8bzPA16hjw?si=fH7C44WRPIQ7B0Ww",
    },
  ],
  travelRequirements:
    "Traveling from Alberta, Canada. Business-class international travel and standard professional AV/stage specifications for eligible events.",
  authoredBooks: [
    "Road to the Olympics: Lornette Daye's Journey to the World Stage",
    "Surviving Life",
    "Survival Skills for Athletes: A Holistic Guide to Mastering Performance, Purpose, and Legacy",
    "Survival Skills for Men: A Comprehensive Guide to Living with Balance, Meaning, and Impact",
    "Survival Skills for Women: A Comprehensive Guide to Living with Balance, Meaning, and Impact",
    "Survival Skills for Students",
    "Umattr Devotional",
  ],
  selectedSpeakingEngagements: [
    "Empowering Black Girls",
    "Sir George Simpson, now Ecole Hillgrove School",
    "St. Albert Rotary Club",
    "Speak Feed Lead Project",
    "Millionaire Woman Podcast",
  ],
  recognitionHighlights: [
    "Diversity Award Winner",
    "Friends of Diversity recognition artwork supplied by brand materials",
    "Former National Track Champion in 100m and 200m sprint events",
    "National Coach with decades of athlete mentorship",
    "Author of resilience, performance, purpose, and personal-growth resources",
  ],
};

export const categories = [
  "Mindset Mastery",
  "Performance Psychology",
  "Leadership",
  "Diversity & Inclusion",
  "Athlete Mindset",
  "Youth Development",
  "Purpose-Driven Success",
];

export const posts: Post[] = [
  {
    slug: "the-champion-mindset",
    title: "The Champion Mindset: How Elite Athletes Translate Pressure Into Performance",
    excerpt:
      "Pressure does not create character from nowhere; it reveals the preparation, discipline, resilience, and teamwork already trained into the body.",
    category: "Performance Psychology",
    date: "2026-02-09",
    image: {
      src: blogSource,
      alt: "Editorial artwork for champion mindset article.",
      crop: "object-center",
    },
  },
  {
    slug: "leadership-clarity",
    title: "Leadership Clarity Starts With Self-Accountability",
    excerpt:
      "A practical reflection on leading with steadiness, honesty, and repeatable habits.",
    category: "Leadership",
    date: "2026-02-08",
    image: {
      src: blogSource,
      alt: "Editorial blog artwork about staying close to your source.",
      crop: "object-center",
    },
  },
  {
    slug: "inclusion-in-action",
    title: "Inclusion in Action Is Built in Small Daily Choices",
    excerpt:
      "Belonging becomes real when people practice listening, accountability, and shared courage.",
    category: "Diversity & Inclusion",
    date: "2026-02-08",
    image: {
      src: blogNature,
      alt: "Warm nature editorial artwork for reflective blog content.",
      crop: "object-center",
    },
  },
  {
    slug: "purpose-driven-success",
    title: "Purpose-Driven Success Needs Resilience",
    excerpt:
      "A reflection on vulnerability, support, and strength during growth.",
    category: "Purpose-Driven Success",
    date: "2026-02-08",
    image: {
      src: blogVulnerability,
      alt: "Warm park bench editorial artwork for vulnerability article.",
      crop: "object-center",
    },
  },
];

export const speakerKitDownloads = [
  { id: "short-bio", title: "Short Bio", href: "/speaker-kit/short-bio-sample.html" },
  { id: "long-bio", title: "Long Bio", href: "/speaker-kit/long-bio-sample.html" },
  { id: "speaker-one-sheet", title: "Speaker One-Sheet", href: "/speaker-kit/speaker-one-sheet-sample.html" },
  { id: "headshots", title: "Headshots", href: "/speaker-kit/headshots-sample.html" },
  { id: "topic-sheet", title: "Topic Sheet", href: "/speaker-kit/topic-sheet-sample.html" },
  { id: "intro-script", title: "Intro Script", href: "/speaker-kit/intro-script-sample.html" },
  { id: "av-requirements", title: "AV Requirements", href: "/speaker-kit/av-requirements-sample.html" },
  { id: "logo-pack", title: "Logo Pack", href: "/speaker-kit/logo-pack-sample.html" },
];

const stripeBookLinks = {
  survivalSkillsForMen:
    process.env.NEXT_PUBLIC_STRIPE_SURVIVAL_SKILLS_FOR_MEN_URL ??
    "https://buy.stripe.com/9B6bJ1542gA262JfCG1VK00",
  roadToTheOlympics:
    process.env.NEXT_PUBLIC_STRIPE_ROAD_TO_THE_OLYMPICS_URL ??
    "https://buy.stripe.com/bJe4gz686fvY1Mt9ei1VK01",
  survivingLife:
    process.env.NEXT_PUBLIC_STRIPE_SURVIVING_LIFE_URL ??
    "https://buy.stripe.com/7sY8wPcwuabE62Jcqu1VK02",
};

export const bookListings: BookListing[] = [
  {
    slug: "survival-skills-for-men",
    title: "Survival Skills for Men",
    subtitle: "Build resilience, balance, and purpose in every part of your life.",
    description:
      "A practical digital guide for men who want to strengthen emotional resilience, clarify purpose, and build steadier daily habits through seasons of pressure and transition.",
    audience:
      "For readers, leaders, fathers, mentors, community builders, and men navigating personal growth.",
    priceLabel: "$14.99 CAD",
    format: "PDF download",
    image: {
      src: survivalSkillsMen,
      alt: "Survival Skills for Men book cover artwork, cropped to focus on the book.",
      crop: "object-[50%_35%] scale-[1.16]",
    },
    purchaseUrl: stripeBookLinks.survivalSkillsForMen,
    stripePaymentLinkId: "plink_1TYMDiH99Nljn2XPaPvvbDhp",
    highlights: [
      "Resilience and balance",
      "Purpose-centered reflection",
      "Practical growth prompts",
    ],
  },
  {
    slug: "road-to-the-olympics",
    title: "Road to the Olympics",
    subtitle: "A journey of resilience, purpose, and legacy.",
    description:
      "A motivational PDF resource drawn from Lornette's elite-athlete lens, focused on perseverance, identity, discipline, and rising again after setbacks.",
    audience:
      "For athletes, coaches, youth leaders, schools, teams, and readers who need a champion-mindset reset.",
    priceLabel: "$14.99 CAD",
    format: "PDF download",
    image: {
      src: roadBook,
      alt: "Road to the Olympics book cover artwork, cropped to focus on the book.",
      crop: "object-[50%_35%] scale-[1.16]",
    },
    purchaseUrl: stripeBookLinks.roadToTheOlympics,
    stripePaymentLinkId: "plink_1TYMKfH99Nljn2XPQs08iLxk",
    highlights: [
      "Elite athlete mindset",
      "Resilience after pressure",
      "Purpose and legacy",
    ],
  },
  {
    slug: "surviving-life",
    title: "Surviving Life",
    subtitle: "A guide to resilience when life hits hard.",
    description:
      "A warm, encouraging PDF guide for readers rebuilding hope, confidence, and perspective after difficult seasons.",
    audience:
      "For individuals, women's groups, mentoring circles, faith communities, and anyone seeking practical encouragement.",
    priceLabel: "$14.99 CAD",
    format: "PDF download",
    image: {
      src: survivingLife,
      alt: "Surviving Life book cover artwork, cropped to focus on the book.",
      crop: "object-[50%_34%] scale-[1.16]",
    },
    purchaseUrl: stripeBookLinks.survivingLife,
    stripePaymentLinkId: "plink_1TYMVSH99Nljn2XPYvPsZSw0",
    highlights: [
      "Hope after hardship",
      "Resilience practices",
      "Confidence and renewal",
    ],
  },
];

// ─── Student-Athlete Workbooks & Guides (from 10 F's library) ────────────────

export const workbookListings: BookListing[] = [
  {
    slug: "01-athlete-devotional",
    title: "Finish Strong Athlete Devotional",
    subtitle: "A faith-centered daily reset for athletes.",
    description:
      "A 30-day devotional covering identity, pressure, discipline, setbacks, confidence, and resilience. Designed to help athletes anchor their worth and purpose outside of performance.",
    audience: "Best for: Daily spiritual and mental grounding.",
    priceLabel: "$25.99 USD",
    format: "PDF · Word · Kindle",
    image: {
      src: "/images/products/01-athlete-devotional-cover.png",
      alt: "Finish Strong Athlete Devotional cover",
    },
    purchaseUrl: "https://buy.stripe.com/14AcN53ZYcjM9eV3TY1VK0d",
    stripePaymentLinkId: "",
    highlights: [
      "Stronger identity beyond performance",
      "Daily reflective routine",
      "Faith-based resilience cues",
    ],
  },
  {
    slug: "02-motivational-reflections",
    title: "Finish Strong Motivational Reflections for Athletes",
    subtitle: "Short-form encouragement that still leads to action.",
    description:
      "30 motivational reflections featuring executive-level challenges, action steps, and Finish Strong statements. Quick-hit reflection for momentum language and sharper perspective.",
    audience: "Best for: Quick daily motivation and mindset shifts.",
    priceLabel: "$25.99 USD",
    format: "PDF · Word · Kindle",
    image: {
      src: "/images/products/02-motivational-reflections-cover.png",
      alt: "Finish Strong Motivational Reflections for Athletes cover",
    },
    purchaseUrl: "https://buy.stripe.com/6oUaEXfIGbfIfDj9ei1VK0e",
    stripePaymentLinkId: "",
    highlights: [
      "Short reflection cadence",
      "Momentum recovery after setbacks",
      "Action-led mindset prompts",
    ],
  },
  {
    slug: "03-speak-life-affirmations",
    title: "Speak Life: Athlete Affirmations and Declarations",
    subtitle: "A confidence-building language bank for athletes.",
    description:
      "100 athlete affirmations covering identity, confidence, game day pressure, and life beyond sport. Repeatable declarations for hard moments and pre-competition confidence resets.",
    audience: "Best for: Building unshakeable confidence and focus.",
    priceLabel: "$25.99 USD",
    format: "PDF · Word · Kindle",
    image: {
      src: "/images/products/03-speak-life-affirmations-cover.png",
      alt: "Speak Life: Athlete Affirmations and Declarations cover",
    },
    purchaseUrl: "https://buy.stripe.com/fZueVd8ge83w3UBfCG1VK0f",
    stripePaymentLinkId: "",
    highlights: [
      "Improved self-talk",
      "Pre-competition confidence reset",
      "Identity language you can repeat",
    ],
  },
  {
    slug: "04-mental-wellness-reset",
    title: "Athlete Mental Wellness Reset Workbook",
    subtitle: "Rebuild structure after your hardest weeks.",
    description:
      "A 7-day reset plan focusing on emotional check-ins, pressure management, and healthy routines. Slows the system down and rebuilds structure for overloaded athletes.",
    audience: "Best for: Athletes feeling overwhelmed or burned out.",
    priceLabel: "$25.99 USD",
    format: "PDF · Word · Kindle",
    image: {
      src: "/images/products/04-mental-wellness-reset-cover.png",
      alt: "Athlete Mental Wellness Reset Workbook cover",
    },
    purchaseUrl: "https://buy.stripe.com/9B628rgMKgA22Qx8ae1VK0g",
    stripePaymentLinkId: "",
    highlights: [
      "Pressure decompression plan",
      "Better emotional awareness",
      "Reset routine for hard weeks",
    ],
  },
  {
    slug: "05-gratitude-journal",
    title: "Because You Matter Student-Athlete Gratitude Journal",
    subtitle: "Keep perspective when expectations rise.",
    description:
      "A 90-day gratitude journal designed specifically for the unique challenges of student-athletes. Helps athletes slow down, notice what is still good, and stay grounded.",
    audience: "Best for: Developing a positive, grounded perspective.",
    priceLabel: "$25.99 USD",
    format: "PDF · Word · Kindle",
    image: {
      src: "/images/products/05-gratitude-journal-cover.png",
      alt: "Because You Matter Student-Athlete Gratitude Journal cover",
    },
    purchaseUrl: "https://buy.stripe.com/9B614n3ZYabEezf4Y21VK0h",
    stripePaymentLinkId: "",
    highlights: [
      "Daily gratitude rhythm",
      "Perspective reset under pressure",
      "More grounded emotional recovery",
    ],
  },
  {
    slug: "06-responsible-ai-guide",
    title: "Responsible AI Prompt Guide for Student-Athletes",
    subtitle: "Smarter workflows without crossing integrity lines.",
    description:
      "A practical guide on using AI safely for career prep, networking, and studying without violating integrity. A practical AI playbook for athletes who want smarter workflows.",
    audience: "Best for: Modern student-athletes navigating AI tools.",
    priceLabel: "$25.99 USD",
    format: "PDF · Word · Kindle",
    image: {
      src: "/images/products/06-responsible-ai-guide-cover.png",
      alt: "Responsible AI Prompt Guide for Student-Athletes cover",
    },
    purchaseUrl: "https://buy.stripe.com/4gMbJ1gMK97Abn33TY1VK0i",
    stripePaymentLinkId: "",
    highlights: [
      "Safer AI usage habits",
      "Career-prep prompt systems",
      "Clearer academic integrity judgment",
    ],
  },
  {
    slug: "07-career-readiness-workbook",
    title: "Life After Sport Career Readiness Workbook",
    subtitle: "Translate athletic discipline into career language.",
    description:
      "Translate your athletic discipline into career language. Includes resume examples and interview builders. Helps athletes name transferable skills and move to a visible next step.",
    audience: "Best for: Athletes transitioning into the workforce.",
    priceLabel: "$25.99 USD",
    format: "PDF · Word · Kindle",
    image: {
      src: "/images/products/07-career-readiness-workbook-cover.png",
      alt: "Life After Sport Career Readiness Workbook cover",
    },
    purchaseUrl: "https://buy.stripe.com/00w5kD9kibfI0Ipaim1VK0j",
    stripePaymentLinkId: "",
    highlights: [
      "Career story translation",
      "Interview preparation",
      "Visible next-step planning",
    ],
  },
  {
    slug: "08-personal-brand-workbook",
    title: "Student-Athlete Personal Brand Workbook",
    subtitle: "Build a strong, authentic public image.",
    description:
      "Audit your social media, define your values, and build a professional image for life and NIL deals. A personal brand system for better image control and clearer values.",
    audience: "Best for: Building a strong, authentic public image.",
    priceLabel: "$25.99 USD",
    format: "PDF · Word · Kindle",
    image: {
      src: "/images/products/08-personal-brand-workbook-cover.png",
      alt: "Student-Athlete Personal Brand Workbook cover",
    },
    purchaseUrl: "https://buy.stripe.com/dRm8wPcwudnQ3UBbmq1VK0k",
    stripePaymentLinkId: "",
    highlights: [
      "Brand clarity",
      "Social audit workflow",
      "Professional image decisions",
    ],
  },
  {
    slug: "09-nil-digital-reputation",
    title: "NIL & Digital Reputation Decision Guide",
    subtitle: "Better filters around risk, visibility, and consequences.",
    description:
      "Understand how online decisions affect future opportunities and learn to navigate NIL safely. A reputation and NIL judgment guide for athletes who need better decision filters.",
    audience: "Best for: Navigating sponsorships and digital footprint.",
    priceLabel: "$25.99 USD",
    format: "PDF · Word · Kindle",
    image: {
      src: "/images/products/09-nil-digital-reputation-cover.png",
      alt: "NIL & Digital Reputation Decision Guide cover",
    },
    purchaseUrl: "https://buy.stripe.com/00wfZheECcjMfDj1LQ1VK0l",
    stripePaymentLinkId: "",
    highlights: [
      "Reputation risk awareness",
      "Safer NIL decisions",
      "Long-term digital judgment",
    ],
  },
  {
    slug: "10-finish-strong-action-planner",
    title: "30-Day Finish Strong Action Planner",
    subtitle: "Better execution, sequencing, and follow-through.",
    description:
      "A structured planner balancing athletic, academic, wellness, and future-building habits every day. For athletes who need better execution, not more inspiration.",
    audience: "Best for: Creating structure and achieving major goals.",
    priceLabel: "$25.99 USD",
    format: "PDF · Word · Kindle",
    image: {
      src: "/images/products/10-finish-strong-action-planner-cover.png",
      alt: "30-Day Finish Strong Action Planner cover",
    },
    purchaseUrl: "https://buy.stripe.com/cNicN5aom0B49eVeyC1VK0m",
    stripePaymentLinkId: "",
    highlights: [
      "30-day execution structure",
      "Goal sequencing",
      "Finish-strong accountability",
    ],
  },
];

// ─── 10 F's Masterclass Courses ──────────────────────────────────────────────

export const masterclassListings: BookListing[] = [
  {
    slug: "course-faith",
    title: "The Faith Blueprint Masterclass",
    subtitle: "Ground your identity beyond the scoreboard.",
    description:
      "A deep-dive video course designed to help athletes anchor their worth and purpose outside of performance. Rebuilds inner steadiness when external results feel uncertain.",
    audience: "Best for: Athletes struggling with identity and pressure.",
    priceLabel: "$997/yr ($297 deposit)",
    format: "Video Course · Community Access",
    image: {
      src: "/images/products/01-athlete-devotional-cover.png",
      alt: "The Faith Blueprint Masterclass",
    },
    purchaseUrl: "https://buy.stripe.com/cNi5kDfIG2JcfDj0HM1VK0n",
    stripePaymentLinkId: "",
    highlights: [
      "Unshakeable identity",
      "Mental resilience under pressure",
      "Performance without fear",
    ],
  },
  {
    slug: "course-fitness",
    title: "The Fitness & Recovery Masterclass",
    subtitle: "Master your physical readiness and recovery rhythm.",
    description:
      "Learn the exact discipline, recovery protocols, and injury prevention strategies elite athletes use. Optimizes the physical foundation that supports every other F.",
    audience: "Best for: Athletes needing better training consistency and recovery.",
    priceLabel: "$997/yr ($297 deposit)",
    format: "Video Course · Community Access",
    image: {
      src: "/images/products/04-mental-wellness-reset-cover.png",
      alt: "The Fitness & Recovery Masterclass",
    },
    purchaseUrl: "https://buy.stripe.com/cNi8wPeECcjMaiZ76a1VK0o",
    stripePaymentLinkId: "",
    highlights: [
      "Optimized recovery",
      "Injury prevention strategies",
      "Peak physical readiness",
    ],
  },
  {
    slug: "course-food",
    title: "The Athlete Fueling Masterclass",
    subtitle: "Stabilize your daily fuel plan for sustained energy.",
    description:
      "A comprehensive nutrition strategy course covering hydration, game-day fueling, and healthy relationships with food. Sustained energy and better recovery nutrition.",
    audience: "Best for: Athletes wanting to optimize their nutrition.",
    priceLabel: "$997/yr ($297 deposit)",
    format: "Video Course · Community Access",
    image: {
      src: "/images/products/05-gratitude-journal-cover.png",
      alt: "The Athlete Fueling Masterclass",
    },
    purchaseUrl: "https://buy.stripe.com/dRmfZh9ki0B4cr72PU1VK0p",
    stripePaymentLinkId: "",
    highlights: [
      "Sustained energy and focus",
      "Better recovery nutrition",
      "Healthy body image",
    ],
  },
  {
    slug: "course-friends",
    title: "The Inner Circle Masterclass",
    subtitle: "Tighten your support circle and protect your standards.",
    description:
      "Learn how to build a network of peers and mentors who elevate you, and how to set healthy boundaries. Positive peer influence and strong accountability structures.",
    audience: "Best for: Athletes needing to elevate their environment.",
    priceLabel: "$997/yr ($297 deposit)",
    format: "Video Course · Community Access",
    image: {
      src: "/images/products/03-speak-life-affirmations-cover.png",
      alt: "The Inner Circle Masterclass",
    },
    purchaseUrl: "https://buy.stripe.com/28E5kD7cafvYbn34Y21VK0q",
    stripePaymentLinkId: "",
    highlights: [
      "Positive peer influence",
      "Strong boundaries",
      "Valuable mentorship",
    ],
  },
  {
    slug: "course-family",
    title: "The Family Dynamics Masterclass",
    subtitle: "Navigate family expectations without losing your pace.",
    description:
      "A guide to communicating boundaries, handling pressure, and building a legacy your family can be proud of. Clear communication and reduced family pressure.",
    audience: "Best for: Athletes feeling overwhelmed by family expectations.",
    priceLabel: "$997/yr ($297 deposit)",
    format: "Video Course · Community Access",
    image: {
      src: "/images/products/02-motivational-reflections-cover.png",
      alt: "The Family Dynamics Masterclass",
    },
    purchaseUrl: "https://buy.stripe.com/cNifZhaombfIfDjduy1VK0r",
    stripePaymentLinkId: "",
    highlights: [
      "Clear communication",
      "Reduced family pressure",
      "Healthy support systems",
    ],
  },
  {
    slug: "course-finance",
    title: "The Financial Playbook Masterclass",
    subtitle: "Build financial decision control and understand NIL safely.",
    description:
      "Master budgeting, credit, contracts, and NIL decision-making to secure your financial future. Financial literacy and safe NIL decisions for long-term wealth habits.",
    audience: "Best for: Athletes navigating NIL and basic finances.",
    priceLabel: "$997/yr ($297 deposit)",
    format: "Video Course · Community Access",
    image: {
      src: "/images/products/09-nil-digital-reputation-cover.png",
      alt: "The Financial Playbook Masterclass",
    },
    purchaseUrl: "https://buy.stripe.com/eVq28r6861F8fDjduy1VK0s",
    stripePaymentLinkId: "",
    highlights: [
      "Financial literacy",
      "Safe NIL decisions",
      "Long-term wealth habits",
    ],
  },
  {
    slug: "course-fashion",
    title: "The Personal Brand & Presentation Masterclass",
    subtitle: "Strengthen your public presence and professional image.",
    description:
      "Learn how to manage your digital footprint, interview with confidence, and build an authentic brand. Polished public image and strong personal brand for media readiness.",
    audience: "Best for: Athletes wanting to monetize their name and image.",
    priceLabel: "$997/yr ($297 deposit)",
    format: "Video Course · Community Access",
    image: {
      src: "/images/products/08-personal-brand-workbook-cover.png",
      alt: "The Personal Brand & Presentation Masterclass",
    },
    purchaseUrl: "https://buy.stripe.com/bJe3cv9ki4Rkcr7aim1VK0t",
    stripePaymentLinkId: "",
    highlights: [
      "Polished public image",
      "Media readiness",
      "Strong personal brand",
    ],
  },
  {
    slug: "course-fun",
    title: "The Athlete Joy & Recovery Masterclass",
    subtitle: "Schedule recovery that feels human and protect your joy.",
    description:
      "Discover how to decompress, maintain hobbies outside of sport, and keep the passion for the game alive. Burnout prevention and renewed passion for the game.",
    audience: "Best for: Athletes experiencing burnout or loss of passion.",
    priceLabel: "$997/yr ($297 deposit)",
    format: "Video Course · Community Access",
    image: {
      src: "/images/products/02-motivational-reflections-cover.png",
      alt: "The Athlete Joy & Recovery Masterclass",
    },
    purchaseUrl: "https://buy.stripe.com/bJe5kD8ge4Rk0Ipcqu1VK0u",
    stripePaymentLinkId: "",
    highlights: [
      "Burnout prevention",
      "Work-life balance",
      "Renewed passion for sport",
    ],
  },
  {
    slug: "course-future",
    title: "The Career Transition Masterclass",
    subtitle: "Make your next chapter visible and prepare for life after sport.",
    description:
      "Translate your athletic skills onto a resume, network effectively, and build confidence for the professional world. Strong resume, networking skills, and career confidence.",
    audience: "Best for: Athletes nearing the end of their athletic career.",
    priceLabel: "$997/yr ($297 deposit)",
    format: "Video Course · Community Access",
    image: {
      src: "/images/products/07-career-readiness-workbook-cover.png",
      alt: "The Career Transition Masterclass",
    },
    purchaseUrl: "https://buy.stripe.com/9B6bJ1fIG1F84YFcqu1VK0v",
    stripePaymentLinkId: "",
    highlights: [
      "Strong resume",
      "Networking skills",
      "Career confidence",
    ],
  },
  {
    slug: "course-finish-strong",
    title: "The Finish Strong Execution Masterclass",
    subtitle: "Turn good intentions into a finish-strong plan.",
    description:
      "Master time management, goal setting, accountability, and the responsible use of AI tools. Real structure for athletes who want better execution and accountability.",
    audience: "Best for: Athletes needing better execution and accountability.",
    priceLabel: "$997/yr ($297 deposit)",
    format: "Video Course · Community Access",
    image: {
      src: "/images/products/10-finish-strong-action-planner-cover.png",
      alt: "The Finish Strong Execution Masterclass",
    },
    purchaseUrl: "https://buy.stripe.com/placeholder_finish_strong",
    stripePaymentLinkId: "",
    highlights: [
      "Goal achievement",
      "Time management mastery",
      "Accountability systems",
    ],
  },
];

export const bookFeatures = [
  {
    title: "Surviving Life",
    subtitle: "A guide to resilience when life hits hard.",
    image: { src: survivingLife, alt: "Surviving Life book cover artwork.", crop: "object-top" },
  },
  {
    title: "Road to the Olympics",
    subtitle: "A journey of resilience, purpose, and legacy.",
    image: { src: roadBook, alt: "Road to the Olympics book cover artwork.", crop: "object-top" },
  },
  {
    title: "Survival Skills for Women",
    subtitle: "Thrive with balance, confidence, and purpose.",
    image: { src: womensBook, alt: "Survival Skills for Women cover artwork.", crop: "object-top" },
  },
];

export const suppliedLogos = [
  {
    name: "Toastmasters International",
    image: images.toastmastersLogo,
    status: "Brand asset",
  },
  {
    name: "Rotary Club of St. Albert",
    image: images.rotaryLogo,
    status: "Brand asset",
  },
];

export const additionalImages = {
  athleteInfo: {
    src: athleteInfoPoster,
    alt: "Athletic achievement artwork supplied in brand materials.",
    crop: "object-top scale-[1.04]",
  },
  athleteStrategy: {
    src: athleteStrategyPoster,
    alt: "Strategy leadership elite execution artwork supplied in brand materials.",
    crop: "object-top scale-[1.03]",
  },
  aboutTimeline: {
    src: aboutTimelinePoster,
    alt: "Graduation and champion athlete story artwork supplied in brand materials.",
    crop: "object-top scale-[1.05]",
  },
  testimonialComposite: {
    src: testimonialComposite,
    alt: "Audience testimonial artwork supplied in brand materials.",
    crop: "object-top",
  },
  testimonialYouth: {
    src: testimonialYouth,
    alt: "Youth coaching testimonial artwork supplied in brand materials.",
    crop: "object-top",
  },
  eventWorkshop: {
    src: eventWorkshop,
    alt: "Workshop and event artwork supplied in brand materials.",
    crop: "object-top",
  },
  trainingPoster: {
    src: trainingPoster,
    alt: "Training and workshops artwork, cropped to reduce social footer.",
    crop: "object-top scale-[1.1]",
  },
  resiliencePoster: {
    src: resiliencePoster,
    alt: "Resilience and mindset coaching artwork, cropped to reduce social footer.",
    crop: "object-top scale-[1.1]",
  },
  flightPoster: {
    src: flightPoster,
    alt: "Flight attendant graduate artwork supplied in brand materials.",
    crop: "object-top scale-[1.02]",
  },
  programOverview: {
    src: programOverview,
    alt: "Speaking and services overview artwork supplied in brand materials.",
    crop: "object-top scale-[1.06]",
  },
};

export function createMetadata(title: string, description: string, path: string): Metadata {
  const url = `${siteUrl}${path}`;
  return {
    title,
    description,
    alternates: { canonical: url },
    openGraph: {
      title,
      description,
      url,
      siteName: siteCopy.brandName,
      type: "website",
    },
    twitter: {
      card: "summary_large_image",
      title,
      description,
    },
  };
}
