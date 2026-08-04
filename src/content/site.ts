import type { Metadata } from "next";
import type { StaticImageData } from "next/image";

import alternatePortrait from "../../images/chrome_nRMcvAaFwK.png";
import monogram from "../../images/Beige & Black Elegant Typography Monogram Initials AP Logo_20251127_172032_0000.png";
import featuredOnCollage from "../../images/chrome_pclmdSgQoj.png";
import brandStatement from "../../images/c298ebb1-01e5-497d-a41e-33c2dba1b74c.png";
import podcastCard from "../../images/588657892_17845278915616562_7038671232751376482_n.jpg";
import speakingPoster from "../../images/unnamed (6).jpg";
import inclusionPoster from "../../images/unnamed (3).jpg";
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
import survivalSkillsMen from "../../images/survival-skills-for-men-cover-new.png";
import survivingLife from "../../images/surviving-life-cover-new.jpg";
import finishStrongBook from "../../images/finish-strong-cover-new.jpg";
import womensBook from "../../images/womensbook.jpg";
import toastmastersLogo from "../../images/Toastmasters_2011.png";
import rotaryLogo from "../../images/Rotary-Club-of-St-Albert--1-.jpeg";
import flightPoster from "../../images/image.png";

export const siteUrl = "https://lornettedaye.com";

export type SiteImage = {
  src: StaticImageData | string;
  alt: string;
  crop?: string;
  caption?: string;
  aspect?: string;
  frameTone?: "warm-ivory";
  showBottomFade?: boolean;
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

export type MediaBandIcon = "film" | "mic" | "download" | "calendar" | "users" | "target";

export type MediaBandCard = {
  icon: MediaBandIcon;
  title: string;
  body: string;
};

export type MediaBandContent = {
  eyebrow?: string;
  title?: string;
  body?: string;
  primaryLabel?: string;
  primaryHref?: string;
  secondaryLabel?: string;
  secondaryHref?: string;
  videoTitle?: string;
  videoSummary?: string;
  cards?: MediaBandCard[];
  footerLabel?: string;
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
  mediaBand?: MediaBandContent;
};

export type Post = {
  slug: string;
  title: string;
  excerpt: string;
  category: string;
  image: SiteImage;
  date: string;
  author: string;
  readTime: string;
  body: {
    intro: string[];
    sections: {
      heading: string;
      paragraphs: string[];
      bullets?: {
        label: string;
        text: string;
      }[];
    }[];
    conclusion?: string[];
  };
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

export const siteCopy = {
  brandName: "Lornette Daye",
  contactEmail: "ldayespeaking@gmail.com",
  seoTitle: "Lornette Daye | Transformational Speaker",
  seoDescription:
    "Keynote speaking, leadership development, inclusion, mentorship, youth development, and performance coaching with Lornette Daye.",
  descriptor:
    "Professional Keynote Speaker | Olympic-level Athlete & Coach | Canadian National Sprint Champion | Certified Transformational Speaker | Author | Youth Leader & Mentor | Project Manager",
  mainMessage:
    "Helping people rise through challenge, remember their worth, and move forward with purpose.",
  homepageHeadline: "Keynotes That Move People Forward.",
  homepageEventHeadline: "Make Your Event Unforgettable.",
  homepageSubheadline:
    "Lornette brings four decades of elite sport, coaching, mentorship, and lived resilience to every room she enters",
  homepageIntro:
    "Her talks help audiences strengthen confidence, navigate adversity, lead with compassion, and believe again in what is possible.",
  biography:
    "Certified Toastmasters Speaker, Olympic-level Athlete & Coach, Canadian National Sprint Champion, Author, and Transformational Speaker with over 40 years of experience inspiring individuals, teams, and organizations to achieve excellence, resilience, and purpose-driven success.",
  biographyExtended:
    "Through decades of elite competition and coaching over 500 athletes, including 150+ international competitors, she has developed a profound understanding of performance psychology, mindset mastery, goal-setting, and discipline.",
  mission:
    "Her mission is to help people rise through challenge, remember their worth, and move forward with purpose. True success is measured not only by personal accomplishments but by the lives we touch, the communities we strengthen, and the leaders we develop.",
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
    { label: "LinkedIn", href: "https://www.linkedin.com/in/lornette-d-419276358" },
    { label: "Email", href: "mailto:ldayespeaking@gmail.com" },
  ],
};

export const mainNav: NavItem[] = [
  { label: "Home", href: "/" },
  { label: "Speaker", href: "/speaking" },
  { label: "Leadership", href: "/leadership" },
  { label: "Books", href: "/books" },
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
  "/impact",
  "/programs",
  "/events",
  "/blog",
  "/speaker-kit",
  "/book",
];

export const images = {
  homeHeroPortrait: {
    src: "/generated/lornette-home-hero-original-cutout.png",
    alt: "Seated portrait of Lornette Daye in an ivory blazer.",
    crop: "object-center scale-[1.06]",
    frameTone: "warm-ivory" as const,
    showBottomFade: false,
  },
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
    alt: "Lornette Daye monogram.",
  },
  featuredOn: {
    src: featuredOnCollage,
    alt: "Collage of organizations, media appearances, and community references connected to Lornette Daye.",
    crop: "object-bottom scale-[1.04]",
  },
  brandStatement: {
    src: brandStatement,
    alt: "Lornette Daye speaker brand artwork cropped to the portrait area.",
    crop: "object-[76%_44%] scale-[1.78]",
  },
  speakingChampionMindset: {
    src: "/generated/speaking-champion-abstract-gold-flow.png",
    alt: "Abstract elegant gold and white flowing artwork for the speaking topics section.",
    crop: "object-[72%_50%]",
  },
  podcastCard: {
    src: podcastCard,
    alt: "Podcast appearance artwork featuring Lornette Daye.",
    crop: "object-top scale-[1.12]",
  },
  recognitionDiversityAward: {
    src: recognitionDiversityAward,
    alt: "Diversity Awards Friends of Diversity recognition artwork featuring Lornette Daye.",
    crop: "object-[50%_52%] scale-[1.02]",
  },
  recognitionCommunityAwards: {
    src: "/generated/recognition-awards-community-gold-centered.png",
    alt: "Minimalist gold-themed artwork representing awards and community outreach.",
    crop: "object-center",
  },
  toastmastersLogo: {
    src: toastmastersLogo,
    alt: "Toastmasters International logo.",
  },
  rotaryLogo: {
    src: rotaryLogo,
    alt: "Rotary Club of St. Albert logo.",
  },
};

export const metrics = [
  { value: "40+", label: "Years Speaking, Coaching & Mentoring" },
  { value: "500+", label: "Athletes Mentored and Coached" },
  { value: "150+", label: "International-Level Competitors Guided" },
  { value: "Global", label: "Perspective From Canada to the World" },
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
    title: "Keynotes & Speaking",
    body: "Messages that help audiences remember their worth, rise through adversity, and leave with practical next steps.",
    href: "/speaking",
  },
  {
    title: "Resilient Leadership",
    body: "Help leaders carry pressure with perspective, communicate with courage, and move people toward shared purpose.",
    href: "/leadership",
  },
  {
    title: "Diversity & Inclusion",
    body: "Create spaces where people feel seen, respected, and responsible for building real belonging.",
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
    title: "Workshops & Training",
    body: "Interactive sessions that turn inspiration into practice, reflection, and usable next steps.",
    href: "/events",
  },
  {
    title: "Purpose & Resilience Coaching",
    body: "Purpose-centered support for people seeking clarity, confidence, and steady forward movement.",
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
      "Signature keynotes and facilitated sessions on achievement, adversity, change, disappointment, resilience, and perspective.",
    heroImage: {
      src: speakingPoster,
      alt: "Transformational public speaking artwork, cropped to keep the focus on the stage visual.",
      crop: "object-center scale-[1.58]",
    },
    pillars: [
      "Road to the Olympics",
      "Navigating Change and Disappointment",
      "Staying Grounded After Adversity",
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
    eyebrow: "Resilient Leadership",
    description:
      "Practical leadership development for people who need to communicate, execute, and lead with composure under pressure.",
    heroImage: {
      src: "/generated/leadership-soft-cream-gold-hero.png",
      alt: "Soft cream and gold abstract pathway suggesting resilient leadership and purposeful movement.",
      crop: "object-[50%_48%]",
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
        title: "What leaders practice",
        items: [
          "Decision-making clarity",
          "High-trust communication",
          "Accountability without shame",
          "Resilient execution habits",
        ],
      },
      {
        title: "Team outcomes",
        items: [
          "Clearer standards",
          "Stronger teams",
          "Better performance conversations",
          "Purpose-driven action",
        ],
      },
      {
        title: "Leadership sessions",
        items: [
          "Leading Through Pressure",
          "Communication That Builds Trust",
          "Execution With Purpose",
        ],
      },
    ],
    cta: "Schedule a Leadership Consultation",
    mediaBand: {
      eyebrow: "A Preview of Lornette in the Room",
      title: "Hear the warmth, clarity, and challenge she brings to leaders.",
      body: "Watch how Lornette connects personal resilience with communication, accountability, and confident leadership under pressure.",
      primaryLabel: "Watch Speaker Reel",
      secondaryLabel: "View Speaker Kit",
      videoTitle: "Leadership Speaking Preview",
      videoSummary:
        "A quick look at Lornette's presence, storytelling, and ability to connect practical leadership lessons to real-life pressure.",
      cards: [
        {
          icon: "film",
          title: "Watch Her Speak",
          body: "Get a quick feel for Lornette's tone, presence, and ability to connect leadership lessons to real life.",
        },
        {
          icon: "target",
          title: "Match the Message",
          body: "See how her message connects to resilience, communication, accountability, and leading under pressure.",
        },
        {
          icon: "calendar",
          title: "Plan The Session",
          body: "Use the speaker kit to shape the right leadership experience around your audience, goals, format, and date.",
        },
      ],
      footerLabel: "Ready to plan a leadership session",
    },
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
      src: "/generated/mentorship-podium-soft-background.png",
      alt: "Gold podium artwork with a simplified cream and gold background for mentorship and youth development.",
      crop: "object-center",
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
        title: "How young people are supported",
        items: [
          "Name strengths and pressures",
          "Build discipline and confidence",
          "Practice healthy accountability",
          "Leave with clear next steps",
        ],
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
        title: "Team sessions and takeaways",
        items: [
          "Mindset before performance",
          "Preparation under pressure",
          "Confidence through repetition",
        ],
      },
    ],
    cta: "Inquire About Performance Coaching",
  },
};

export const testimonials = [
  {
    category: "Coaching & Transformation",
    quote:
      "As a Life coach and Transformational Speaker, she indeed changes lives by drawing on vast life experiences and actionable insights.",
    name: "Ayo",
    context: "Accounting, Technology Leadership & Healthcare Professional",
  },
  {
    category: "Keynote Speaking",
    quote:
      "Lornette, you are flat-out top of the charts for your ability to connect and interact with your audience to deliver a powerful message.",
    name: "Harriet Tinka",
    context: "Founder/CEO, Empowered Me Inc.",
  },
  {
    category: "Faith & Wellness",
    quote:
      "Lornette encouraged me to increase the intensity and speed slowly, and now I have been consistent with very brisk walking daily.",
    name: "Carol",
    context: "Wellness audience member",
  },
  {
    category: "Youth Coaching",
    quote:
      "Lornette is truly an inspiration to today's youth. She is an exceptional track coach, truly dedicated, and cares deeply about her athletes' futures.",
    name: "Shawna Randolph",
    context:
      "Sole Proprietor, Shawna Randolph Communications | Media Relations & Public Speaking Coach",
  },
];

export const mediaItems: MediaItem[] = [
  {
    title: "Speaker Reel",
    category: "Keynotes",
    summary: "Watch Lornette speak with heart, clarity, and hard-earned wisdom about resilience, confidence, and the courage to keep going.",
    image: {
      src: "/generated/speaker-reel-bronze-nature-thumbnail.png",
      alt: "Bronze-gold abstract nature artwork for the speaker reel thumbnail.",
      crop: "object-center",
    },
    videoSrc: "/media/speaker-reel.mp4",
    duration: "1:51",
  },
  {
    title: "One-Minute Speaking Moment",
    category: "Interviews",
    summary: "A quick glimpse of Lornette's warmth, presence, and message in action.",
    image: images.podcastCard,
    videoSrc: "https://youtube.com/shorts/kkQw4iC2QgU?feature=share",
    duration: "Short",
  },
  {
    title: "Speaking Clip: Resilience & Purpose",
    category: "Short Insights",
    summary: "A concise message clip for teams exploring resilience, identity, and next steps.",
    image: {
      src: "/media/frames/speaker-reel-20.jpg",
      alt: "Still frame from Lornette Daye's speaker reel video.",
      crop: "object-[50%_28%]",
    },
    videoSrc: "https://youtu.be/n8bzPA16hjw?si=fH7C44WRPIQ7B0Ww",
    duration: "YouTube",
  },
  {
    title: "Athlete Mindset Coaching",
    category: "Keynotes",
    summary: "Elite-athlete lessons on mindset, discipline, preparation, and confidence under pressure.",
    image: {
      src: athletePoster,
      alt: "Athlete and performance coaching artwork, cropped to remove footer social icons.",
      crop: "object-top scale-[1.12]",
    },
    status: "Coaching Focus",
  },
  {
    title: "Podcast & Interview Features",
    category: "Podcasts",
    summary: "Conversations on resilience, purpose, leadership, and the experiences that shape Lornette's work.",
    image: {
      src: mediaThumbnail,
      alt: "Speaker reel and media thumbnail artwork for podcast and interview features.",
      crop: "object-top",
    },
    status: "Interviews",
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
      "Drawing from her journey as an elite sprinter, Lornette shows audiences how discipline, faith, confidence, and perspective can carry them through setbacks without losing sight of who they are.",
    fit:
      "A powerful elite-athlete story on rising above adversity without losing yourself.",
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
    "Spruce Grove Rotary Club",
  ],
  recognitionHighlights: [
    "Diversity Award winner for inclusion and community impact",
    "Community volunteer committed to youth, belonging, and service",
    "Former national 100m and 200m sprint champion",
    "National coach who has mentored athletes across decades",
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
    slug: "your-setback-is-not-your-finish-line",
    title: "Your Setback Is Not Your Finish Line",
    excerpt:
      "When life challenges our resilience, it is easy to view a painful setback as an ending. Here is how athletes, leaders, and communities can shift their mindset, practice resilience, and turn painful seasons into enduring purpose.",
    category: "Mindset Mastery",
    date: "2026-08-03",
    author: "Lornette Daye",
    readTime: "3 min read",
    image: {
      src: "/generated/blog-setback-finish-line.jpg",
      alt: "Your Setback Is Not Your Finish Line artwork featuring running shoes, a whistle, microphone, medal, and performance plan.",
      caption: "Turning pain into purpose on the path to finishing strong.",
      aspect: "aspect-square",
      crop: "object-center",
    },
    body: {
      intro: [
        "In athletics, business, and daily life, we all encounter obstacles that threaten to stall our progress. A sudden setback—whether a career shift, an injury, a disappointment, or an unexpected transition—can easily feel like a permanent roadblock. But a true champion's perspective reminds us: a stumble on the track does not dictate the end of your race.",
        "The true test of leadership and personal fortitude isn't avoiding hardship; it is discovering the capacity to rise above it. When you actively reframe your struggles, you uncover the profound opportunity to transform personal adversity and pain into powerful purpose.",
      ],
      sections: [
        {
          heading: "The Four Pillars of the Performance Plan",
          paragraphs: [
            "Rebuilding momentum requires more than wishful thinking—it calls for an actionable strategy and unwavering commitment. Whether you are leading a team, coaching youth, or personally striving for your next breakthrough, building a sturdy framework will anchor you when pressure builds.",
          ],
          bullets: [
            {
              label: "Focus",
              text: "Direct your emotional and cognitive energy toward what you can control. Rather than looking backward at what was lost, fix your eyes forward on the actionable steps in front of you.",
            },
            {
              label: "Preparation",
              text: "True confidence is forged through deliberate preparation. Every setback offers invaluable lessons that enable you to refine your habits, study your terrain, and re-enter the arena better prepared than before.",
            },
            {
              label: "Perseverance",
              text: "Endurance is built in the extra miles. When fatigue and self-doubt arise, perseverance means making the simple, courageous decision to keep stepping forward, one day at a time.",
            },
            {
              label: "Purpose",
              text: "Your 'why' is your greatest source of sustainable fuel. When your personal goals connect to a lasting mission—inspiring others, uplifting your community, and leading with integrity—no setback can extinguish your drive.",
            },
          ],
        },
        {
          heading: "Mindset, Discipline, and Resilience",
          paragraphs: [
            "An elite mindset isn't born entirely out of easy victories; it is carefully shaped through overcoming adversity. Discipline bridges the gap between motivation and enduring achievement. By committing to daily acts of self-improvement and keeping faith through difficult seasons, resilience becomes your quiet strength.",
            "When leaders and athletes embrace this empowering viewpoint, communities benefit. Your willingness to stand up after falling gives others permission and courage to do the exact same thing.",
          ],
        },
      ],
      conclusion: [
        "No matter where you find yourself today, remember that your current chapter is just one part of your broader story. Draw a line in the sand, embrace your renewed purpose, and fix your eyes on the road ahead. Your setback is simply the setup for your ultimate comeback—get ready to finish strong.",
      ],
    },
  },
  {
    slug: "embrace-new-beginnings",
    title: "When It's Time to Begin Again",
    excerpt:
      "Fresh starts can feel uncertain. This reflection offers courage, practical steps, and a reminder that change can become a place of growth.",
    category: "Purpose-Driven Success",
    date: "2026-03-16",
    author: "Lornette Daye",
    readTime: "2 min read",
    image: {
      src: "/generated/blog-embrace-new-beginnings-forest.png",
      alt: "A golden sunlit path winding through a quiet forest.",
      caption: "A winding path through a forest.",
      crop: "object-center",
    },
    body: {
      intro: [
        "Starting over can feel like standing at the edge of a vast unknown. It is natural to hesitate when faced with the idea of leaving behind what is familiar. Yet the power of new beginnings lies in its ability to open doors to growth, self-discovery, and renewed purpose.",
        "This post explores why embracing fresh starts is essential, shares inspiring stories of people who reinvented themselves, and offers practical steps to help you overcome fear and take that first step toward change.",
      ],
      sections: [
        {
          heading: "Why Starting Over Matters",
          paragraphs: [
            "Life rarely follows a straight line. Careers shift, relationships change, and personal goals evolve. When circumstances push us to start over, it can feel like a setback. But starting over is often a chance to realign with what truly matters.",
            "New beginnings encourage resilience. Each time you embrace change, you strengthen your ability to adapt and thrive. This mindset turns challenges into opportunities. Instead of fearing failure, you begin to see every ending as a doorway to something better.",
          ],
        },
        {
          heading: "How to Overcome Fear and Take the First Step",
          paragraphs: [
            "Fear of the unknown often holds people back from starting over. Here are practical ways to move past that fear:",
          ],
          bullets: [
            {
              label: "Acknowledge Your Feelings",
              text: "Recognize that fear is normal. Instead of fighting it, accept it as part of the process. This reduces its power over you.",
            },
            {
              label: "Break Change Into Small Steps",
              text: "Big changes can feel overwhelming. Divide your goal into manageable actions. If you want a new career, start by researching fields, then take a course, then apply for jobs.",
            },
            {
              label: "Seek Support",
              text: "Talk to friends, mentors, or support groups. Sharing your plans and fears can provide encouragement and new perspectives.",
            },
            {
              label: "Learn From Setbacks",
              text: "Expect some bumps along the way. Treat mistakes as learning opportunities rather than failures.",
            },
            {
              label: "Commit to Growth",
              text: "Focus on what you will gain rather than what you might lose. Growth requires stepping outside your comfort zone.",
            },
          ],
        },
        {
          heading: "Seeing Starting Over as Opportunity",
          paragraphs: [
            "Starting over is not a sign of failure but a chance to rewrite your story. It offers:",
          ],
          bullets: [
            {
              label: "Self-Discovery",
              text: "You learn more about your values, strengths, and desires when you step into new roles or environments.",
            },
            {
              label: "Renewed Energy",
              text: "New challenges can reignite passion and creativity.",
            },
            {
              label: "Improved Confidence",
              text: "Each successful step builds belief in your ability to handle change.",
            },
            {
              label: "Expanded Horizons",
              text: "You meet new people, explore different ideas, and open doors you never imagined.",
            },
          ],
        },
      ],
      conclusion: [
        "I hope this post inspires you to embrace new beginnings with an open heart. Remember, trusting yourself to navigate uncertainty is a powerful step toward creating a fulfilling life. As you embark on this journey, know that each challenge is an opportunity for growth, and every new path can lead to experiences you never imagined.",
      ],
    },
  },
  {
    slug: "power-of-vulnerability",
    title: "The Courage to Ask for Help",
    excerpt:
      "Vulnerability is not weakness. It can be the honest first step toward support, healing, and renewed strength.",
    category: "Purpose-Driven Success",
    date: "2026-01-28",
    author: "Lornette Daye",
    readTime: "5 min read",
    image: {
      src: "/generated/blog-vulnerability-bench.png",
      alt: "A quiet bench in a golden park with a contemplative figure seated alone.",
      caption: "A quiet bench beneath warm golden light.",
      crop: "object-center",
    },
    body: {
      intro: [
        "Asking for help can feel like admitting weakness. Many people hesitate to reach out when they need support because they fear judgment or worry about appearing incapable.",
        "But vulnerability is not the opposite of strength. It is often the place where strength begins to grow.",
      ],
      sections: [
        {
          heading: "Why Help Matters",
          paragraphs: [
            "No one grows alone. A trusted voice, a mentor, a friend, or a community can help us see what fear makes blurry. Support gives us language for what we are carrying and courage for the next step.",
          ],
        },
        {
          heading: "Practicing Courage Through Vulnerability",
          paragraphs: [
            "Vulnerability does not require sharing everything with everyone. It means choosing safe, wise places where honesty can lead to healing and growth.",
          ],
          bullets: [
            {
              label: "Name what you need",
              text: "Clarity begins when you can say what kind of support would actually help.",
            },
            {
              label: "Choose trusted people",
              text: "Share with people who have earned access to your story.",
            },
            {
              label: "Receive without shame",
              text: "Let encouragement, guidance, and care strengthen you instead of resisting it.",
            },
          ],
        },
      ],
      conclusion: [
        "There is strength in reaching out. When you allow help to meet you where you are, you create room for resilience, wisdom, and renewed confidence.",
      ],
    },
  },
  {
    slug: "power-of-nature",
    title: "What Nature Teaches Us About Faith",
    excerpt:
      "The natural world has a quiet way of teaching patience, provision, renewal, and trust when we slow down enough to notice.",
    category: "Purpose-Driven Success",
    date: "2025-11-08",
    author: "Lornette Daye",
    readTime: "1 min read",
    image: {
      src: "/generated/blog-nature-flower.png",
      alt: "A white flower glowing in warm sunlight in a peaceful meadow.",
      caption: "A flower reaching toward warm sunlight.",
      crop: "object-center",
    },
    body: {
      intro: [
        "Growing up, I spent a lot of time in nature. I loved climbing trees, picking fresh fruit, and enjoying the sounds of life all around me.",
        "Nature has a way of teaching us if we are willing to slow down and pay attention.",
      ],
      sections: [
        {
          heading: "Lessons Hidden in Creation",
          paragraphs: [
            "A flower does not rush its blooming. A tree does not apologize for growing through seasons. The natural world reminds us that life has rhythm, timing, beauty, and purpose.",
          ],
          bullets: [
            {
              label: "Patience",
              text: "Growth often happens quietly before it becomes visible.",
            },
            {
              label: "Provision",
              text: "There are signs of care and abundance in the details around us.",
            },
            {
              label: "Renewal",
              text: "Every season carries an invitation to begin again.",
            },
          ],
        },
      ],
      conclusion: [
        "When we pause long enough to notice, nature can point us back to gratitude, faith, and the steady hope that new life is always possible.",
      ],
    },
  },
  {
    slug: "stay-close-to-your-source",
    title: "Stay Close to Your Source",
    excerpt:
      "When life gets noisy, return to the people, practices, and faith that steady you and remind you who you are.",
    category: "Purpose-Driven Success",
    date: "2025-10-03",
    author: "Lornette Daye",
    readTime: "2 min read",
    image: {
      src: "/generated/blog-source-ship.png",
      alt: "A vintage sailing ship on calm golden water at sunrise.",
      caption: "A ship staying close to calm golden waters.",
      crop: "object-center",
    },
    body: {
      intro: [
        "Many times in life, we can drift away from the things that grounded and encouraged us at the start of our journey. It could be a person, an activity, a place, a practice, or a quiet source of faith.",
        "Staying close to your source helps you remember who you are and why you began.",
      ],
      sections: [
        {
          heading: "What Grounds You?",
          paragraphs: [
            "Your source is the place you return to when life becomes noisy. It reminds you of your values, your strength, and the truth that you are not defined by pressure.",
          ],
        },
        {
          heading: "Returning With Intention",
          paragraphs: [
            "When you feel disconnected, do not shame yourself. Pause, breathe, and take one step back toward what restores you.",
          ],
          bullets: [
            {
              label: "Reconnect",
              text: "Make space for the people and practices that strengthen your spirit.",
            },
            {
              label: "Reflect",
              text: "Notice what pulls you away from peace and purpose.",
            },
            {
              label: "Realign",
              text: "Choose one grounded action that brings you back to what matters.",
            },
          ],
        },
      ],
      conclusion: [
        "When you stay close to your source, you carry steadiness into every new season.",
      ],
    },
  },
  {
    slug: "survival-skills-for-athletes",
    title: "Survival Skills for Athletes: Promoting Focus & Excellence in Every Stage of Life",
    excerpt:
      "Whether on the track or in life after sport, elite performance demands more than physical strength. Discover how to cultivate mental focus, handle competitive pressure, and carry athletic excellence into every stage of life.",
    category: "Athlete & Performance Coaching",
    date: "2026-08-03",
    author: "Lornette Daye",
    readTime: "4 min read",
    image: {
      src: "/books/survival-skills-for-athletes-cover.jpg",
      alt: "Survival Skills for Athletes book cover artwork by Lornette Daye.",
      caption: "Cultivating focus, grit, and athletic excellence beyond the finish line.",
      aspect: "aspect-[2/3]",
      crop: "object-contain",
    },
    body: {
      intro: [
        "In sports, physical talent gets you to the starting line, but mental focus and emotional resilience are what carry you across the finish line. Every athlete encounters seasons of intense competition, unexpected injury, or performance plateaus where physical effort alone isn't enough.",
        "Drawing from my career as a Canadian National Champion sprint athlete and performance coach, I wrote Survival Skills for Athletes to equip competitors, coaches, and leaders with the internal blueprints needed for long-term excellence.",
      ],
      sections: [
        {
          heading: "Core Pillars for High-Performance Focus",
          paragraphs: [
            "Athletic success is built on quiet habits, emotional control, and intentional recovery. When you master these core skills, you become unshakeable under pressure.",
          ],
          bullets: [
            {
              label: "Identity Beyond Performance",
              text: "Separate your self-worth from win-loss statistics so setbacks never destroy your confidence.",
            },
            {
              label: "Focus Under Pressure",
              text: "Develop pre-performance routines that quiet anxiety and lock in sharp concentration.",
            },
            {
              label: "Transition Mastery",
              text: "Learn to translate athletic discipline into career, business, and personal leadership.",
            },
          ],
        },
        {
          heading: "Carrying Excellence Beyond Sport",
          paragraphs: [
            "The discipline forged in athletic training is one of the most powerful assets you possess. When you direct that same focus toward personal growth, relationships, and leadership, you create a legacy that far outlasts your competitive career.",
          ],
        },
      ],
      conclusion: [
        "Whether you are competing at the highest level or mentoring the next generation, remember: true champions build resilience from the inside out.",
      ],
    },
  },
  {
    slug: "survival-skills-for-women",
    title: "Survival Skills for Women: Living with Hope, Resilience, and Meaning",
    excerpt:
      "A comprehensive guide for women navigating seasons of change, emotional demands, and leadership. Learn how to protect your peace, embrace your worth, and build an enduring legacy of purpose.",
    category: "Resilience & Mindset",
    date: "2026-08-03",
    author: "Lornette Daye",
    readTime: "4 min read",
    image: {
      src: "/books/survival-skills-for-women-cover.png",
      alt: "Survival Skills for Women book cover artwork by Lornette Daye.",
      caption: "A comprehensive guide to living with hope, resilience, and meaning.",
      aspect: "aspect-[2/3]",
      crop: "object-contain",
    },
    body: {
      intro: [
        "Women are often called to balance countless roles—leading in careers, nurturing families, supporting communities, and holding together circles of strength. Yet in the midst of giving so much to others, it is easy to lose sight of your own renewal and purpose.",
        "Survival Skills for Women was written as a warm, empowering roadmap to help you reclaim your space, honor your journey, and thrive with quiet confidence through every transition.",
      ],
      sections: [
        {
          heading: "Reclaiming Your Space & Inner Peace",
          paragraphs: [
            "True strength does not mean carrying every burden alone. It means knowing when to pause, establish healthy boundaries, and replenish your spirit.",
          ],
          bullets: [
            {
              label: "Self-Compassion & Healing",
              text: "Replace perfectionism with self-grace, honoring the seasons where rest is your greatest victory.",
            },
            {
              label: "Purpose Alignment",
              text: "Clarify your core values so your daily choices reflect what truly matters to you.",
            },
            {
              label: "Community & Support",
              text: "Surround yourself with uplifting connections that encourage your personal and professional growth.",
            },
          ],
        },
        {
          heading: "Thriving in Every Season",
          paragraphs: [
            "No matter what challenges you have faced in the past, your future is full of potential. When you step into your worth with intentionality, you inspire every woman around you to do the same.",
          ],
        },
      ],
      conclusion: [
        "Take a deep breath and give yourself permission to grow. You possess everything you need to live with profound hope and purpose.",
      ],
    },
  },
  {
    slug: "survival-skills-for-believers",
    title: "Survival Skills for Believers: Living with Wisdom, Grace, and Peace",
    excerpt:
      "In times of uncertainty, standing firm in faith requires spiritual grounding and practical wisdom. Explore how grace, patience, and intentional living bring peace into everyday life.",
    category: "Spiritual Growth",
    date: "2026-08-03",
    author: "Lornette Daye",
    readTime: "4 min read",
    image: {
      src: "/books/survival-skills-for-believers-cover.png",
      alt: "Survival Skills for Believers book cover artwork by Lornette Daye.",
      caption: "A Christian guide to living with wisdom, grace, and peace.",
      aspect: "aspect-[2/3]",
      crop: "object-contain",
    },
    body: {
      intro: [
        "Living out faith in a complex, fast-paced world demands both spiritual depth and daily practical wisdom. When life brings unexpected storms, our foundation must be rooted in unshakeable truth and grace.",
        "Survival Skills for Believers offers scriptural encouragement and practical reflections designed to help you navigate hardship, anchor your heart in divine peace, and shine as a light in your home and workplace.",
      ],
      sections: [
        {
          heading: "Anchoring Your Heart in Unshakeable Truth",
          paragraphs: [
            "Spiritual resilience is cultivated day by day through prayer, scripture reflection, and choosing trust over fear.",
          ],
          bullets: [
            {
              label: "Wisdom in Decision-Making",
              text: "Seek divine guidance before reacting to life's sudden challenges.",
            },
            {
              label: "Grace Under Pressure",
              text: "Respond to hostility and stress with patient grace and steady confidence.",
            },
            {
              label: "Resting in Peace",
              text: "Guard your heart against anxiety by entrusting your unknown future to a known God.",
            },
          ],
        },
        {
          heading: "Walking Out Your Calling",
          paragraphs: [
            "Your faith is not just for quiet moments; it is meant to inspire your leadership, service, and community. When you walk with wisdom and peace, you become a sanctuary of hope for others.",
          ],
        },
      ],
      conclusion: [
        "May you walk with quiet courage today, knowing that grace surrounds every step of your path.",
      ],
    },
  },
  {
    slug: "umattr-devotional-reflections",
    title: "UMATTR Devotional: Reflections for the Moments That Ask You to Keep Going",
    excerpt:
      "When fatigue sets in and the path forward feels steep, small daily reflections can reignite your purpose. Take time to pause, breathe, and remember that your journey deeply matters.",
    category: "Personal Growth",
    date: "2026-08-03",
    author: "Lornette Daye",
    readTime: "3 min read",
    image: {
      src: "/books/umattr-devotional-cover.png",
      alt: "UMATTR Devotional book cover artwork by Lornette Daye.",
      caption: "Reflections for the moments that ask you to keep going.",
      aspect: "aspect-[2/3]",
      crop: "object-contain",
    },
    body: {
      intro: [
        "There are moments in every journey when the weight of responsibility feels heavy, and staying motivated seems difficult. In those quiet times, what we need isn't more pressure—it is gentle encouragement and a reminder of why we started.",
        "The UMATTR Devotional was created as a peaceful space for daily reflection. Each entry offers a brief, powerful thought to help you ground your mind, renew your spirit, and keep moving forward.",
      ],
      sections: [
        {
          heading: "Daily Prompts for Renewal",
          paragraphs: [
            "Taking five minutes each day to write, reflect, and pray transforms how you handle daily stress.",
          ],
          bullets: [
            {
              label: "Pause & Reset",
              text: "Create stillness amidst your busy schedule to listen to your inner voice.",
            },
            {
              label: "Remember Your Value",
              text: "Affirm your inherent worth—you matter, your story matters, and your contribution counts.",
            },
            {
              label: "One Step at a Time",
              text: "Focus on making progress today without worrying about tomorrow's mountain.",
            },
          ],
        },
        {
          heading: "A Companion for the Road Ahead",
          paragraphs: [
            "Whether you keep this devotional on your nightstand or desk, let it serve as a gentle reminder that every small step of endurance leads toward a greater legacy.",
          ],
        },
      ],
      conclusion: [
        "Never underestimate the power of showing up for yourself. You matter—keep going.",
      ],
    },
  },
  {
    slug: "survival-skills-for-men-guide",
    title: "Survival Skills for Men: Living with Balance, Meaning, and Impact",
    excerpt:
      "A practical blueprint for men balancing career, family, leadership, and emotional well-being. Learn to quiet the noise, lead with integrity, and build habits that sustain long-term strength.",
    category: "Leadership & Men's Health",
    date: "2026-08-03",
    author: "Lornette Daye",
    readTime: "4 min read",
    image: {
      src: "/books/survival-skills-for-men-2026-cover.png",
      alt: "2026 Survival Skills for Men book cover artwork by Lornette Daye.",
      caption: "A comprehensive guide to living with balance, meaning, and impact.",
      aspect: "aspect-[2/3]",
      crop: "object-contain",
    },
    body: {
      intro: [
        "Men today face subtle yet intense pressure: to perform at work, provide for family, maintain strength, and remain emotionally grounded. Yet many men carry this weight silently without practical tools to manage stress or evaluate their true direction.",
        "Survival Skills for Men provides honest, action-oriented strategies to help men break free from isolation, build emotional discipline, and lead their lives with authentic purpose.",
      ],
      sections: [
        {
          heading: "Building Steadier Habits & Emotional Strength",
          paragraphs: [
            "Real manhood isn't defined by invulnerability; it is demonstrated through self-awareness, discipline, and intentional brotherhood.",
          ],
          bullets: [
            {
              label: "Stress & Pressure Management",
              text: "Recognize burnout early and establish healthy physical and mental outlets.",
            },
            {
              label: "Purposeful Leadership",
              text: "Lead your family, business, or team by modeling integrity and open communication.",
            },
            {
              label: "Authentic Community",
              text: "Build trusted friendships with men who hold you accountable to your highest standards.",
            },
          ],
        },
        {
          heading: "Leaving a Lasting Impact",
          paragraphs: [
            "When a man gets clear on his principles and aligns his daily habits, everyone around him benefits. You have the power to shape a legacy of honor, resilience, and strength.",
          ],
        },
      ],
      conclusion: [
        "Stand tall, step into your responsibility, and lead with balance and purpose.",
      ],
    },
  },
  {
    slug: "finish-strong-chasing-the-olympic-dream",
    title: "Finish Strong: Lessons from Chasing the Olympic Dream",
    excerpt:
      "A story of athletic grit, unwavering confidence, and overcoming setbacks. Lornette Daye shares the mindsets that transform fierce competition into a legacy of lasting impact.",
    category: "Keynotes & Mindset",
    date: "2026-08-03",
    author: "Lornette Daye",
    readTime: "5 min read",
    image: {
      src: "/books/finish-strong-main-cover.png",
      alt: "Finish Strong: Chasing the Olympic Dream book cover artwork by Lornette Daye.",
      caption: "A story of resilience. A message of confidence. A legacy of impact.",
      aspect: "aspect-[2/3]",
      crop: "object-contain",
    },
    body: {
      intro: [
        "Every dream worth pursuing will test your resolve. On the track, as a Canadian National Sprint Champion chasing the Olympic dream, I learned that victory isn't determined when you're feeling fresh—it is forged in the final 50 meters when your lungs burn and every impulse tells you to quit.",
        "Finish Strong is my personal memoir and strategic framework. It details how to maintain focus when facing heartbreaks, injuries, and setbacks, transforming life's hardest trials into your greatest strength.",
      ],
      sections: [
        {
          heading: "Key Mindsets for Finishing Strong",
          paragraphs: [
            "Whether you are striving for business breakthroughs, recovery, or athletic excellence, these principles apply across every arena.",
          ],
          bullets: [
            {
              label: "The Final Push",
              text: "How to summon deep internal power when you feel like giving up.",
            },
            {
              label: "Overcoming Heartbreak",
              text: "Rebuilding your game plan after missing a long-sought goal.",
            },
            {
              label: "Unwavering Confidence",
              text: "Believing in your preparation even when standing against elite odds.",
            },
          ],
        },
        {
          heading: "Passing the Torch of Impact",
          paragraphs: [
            "Your story doesn't end when the race is over; it begins when you use your experience to coach, mentor, and inspire others to run their own race with conviction.",
          ],
        },
      ],
      conclusion: [
        "It doesn't matter how you started your season or where you fell. What matters is how you finish. Finish strong!",
      ],
    },
  },
  {
    slug: "survival-skills-surviving-to-thriving",
    title: "Survival Skills: From Surviving to Thriving",
    excerpt:
      "Surviving is the first step, but thriving is your ultimate destination. Discover actionable strategies to shift out of survival mode and into a vibrant, intentional life of fulfillment.",
    category: "Transformational Growth",
    date: "2026-08-03",
    author: "Lornette Daye",
    readTime: "4 min read",
    image: {
      src: "/books/survival-skills-surviving-to-thriving-cover.png",
      alt: "2026 Survival Skills: Surviving to Thriving book cover artwork by Lornette Daye.",
      caption: "Surviving to Thriving—building a life of enduring joy and fulfillment.",
      aspect: "aspect-[2/3]",
      crop: "object-contain",
    },
    body: {
      intro: [
        "When life hits hard, staying afloat is our initial instinct. We go into survival mode—managing crisis, enduring stress, and getting through the day. But survival was never meant to be your permanent state.",
        "Survival Skills: From Surviving to Thriving is designed to guide you past survival mode and into a season of vitality, clarity, and thriving purpose.",
      ],
      sections: [
        {
          heading: "Shifting Your Mindset for Growth",
          paragraphs: [
            "Moving from surviving to thriving requires intentional reframing and practical tools to rebuild momentum.",
          ],
          bullets: [
            {
              label: "Breaking the Crisis Cycle",
              text: "Transition from reactive survival habits to proactive, peaceful planning.",
            },
            {
              label: "Cultivating Vitality",
              text: "Prioritize physical wellness, emotional rest, and joy.",
            },
            {
              label: "Designing Your Thriving Plan",
              text: "Set clear goals aligned with your highest vision for life.",
            },
          ],
        },
        {
          heading: "Your Season of Fullness",
          paragraphs: [
            "You are meant for more than just getting by. When you adopt a thriving mindset, you unlock the energy and vision to achieve your dreams.",
          ],
        },
      ],
      conclusion: [
        "Step out of survival mode today. Your season of thriving starts now.",
      ],
    },
  },
  {
    slug: "survival-skills-for-students",
    title: "Survival Skills for Students: Strength, Wisdom, and Intentionality",
    excerpt:
      "Equipping the next generation of leaders with academic focus, emotional balance, and confidence. How students can navigate academic pressure and build a foundation for lifelong success.",
    category: "Youth & Leadership",
    date: "2026-08-03",
    author: "Lornette Daye",
    readTime: "4 min read",
    image: {
      src: "/books/survival-skills-for-students-cover.png",
      alt: "2026 Survival Skills for Students book cover artwork by Lornette Daye.",
      caption: "A comprehensive guide to living with strength, wisdom, and intentionality.",
      aspect: "aspect-[2/3]",
      crop: "object-contain",
    },
    body: {
      intro: [
        "Students today navigate unique challenges: academic demands, social media comparison, peer pressure, and decisions about future careers. Without strong guidance, it is easy to feel overwhelmed or unsure of one's path.",
        "Survival Skills for Students was written to provide young adults and students with essential tools for building personal discipline, emotional resilience, and clear focus.",
      ],
      sections: [
        {
          heading: "Essential Tools for Student Success",
          paragraphs: [
            "Success in school and life is built on positive habits, strong character, and self-belief.",
          ],
          bullets: [
            {
              label: "Academic Focus & Discipline",
              text: "Master time management and study habits to reduce stress and excel.",
            },
            {
              label: "Confidence & Resilience",
              text: "Learn to handle setbacks, peer pressure, and social anxieties with steady self-worth.",
            },
            {
              label: "Vision & Purpose",
              text: "Discover your unique gifts and set meaningful goals for higher education and career paths.",
            },
          ],
        },
        {
          heading: "Empowering the Next Generation",
          paragraphs: [
            "When young people learn these survival skills early, they gain a lifelong advantage. They step into adulthood prepared to lead, create, and inspire.",
          ],
        },
      ],
      conclusion: [
        "To every student reading this: your potential is limitless. Invest in your growth and live with intentionality!",
      ],
    },
  },
];

export const speakerKitDownloads = [
  { id: "short-bio", title: "Short Bio", href: "/speaker-kit/lornette-short-bio.pdf" },
  { id: "long-bio", title: "Long Bio", href: "/speaker-kit/lornette-long-bio.pdf" },
  {
    id: "speaker-one-sheet",
    title: "Speaker One-Sheet",
    cardTitle: "Speaker One-Sheet Site",
    href: "https://ld-speaker-onesheet.vercel.app",
  },
  { id: "av-requirements", title: "AV Requirements", href: "/speaker-kit/av-requirements-sample.html" },
];

const stripeBookLinks = {
  survivalSkillsForMen:
    process.env.NEXT_PUBLIC_STRIPE_SURVIVAL_SKILLS_FOR_MEN_URL ??
    "https://buy.stripe.com/9B6bJ1542gA262JfCG1VK00",
  roadToTheOlympics:
    process.env.NEXT_PUBLIC_STRIPE_ROAD_TO_THE_OLYMPICS_URL ??
    "https://buy.stripe.com/8x28wP9ki1F8ezf9ei1VK0A",
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
      "For men seeking clarity and practical strategies to navigate pressure, stress, and leadership with confidence.",
    priceLabel: "$14.99 CAD",
    format: "Digital Edition",
    image: {
      src: survivalSkillsMen,
      alt: "Survival Skills for Men book cover artwork, cropped to focus on the book.",
      crop: "object-center",
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
    title: "Finish Strong: Chasing the Olympic Dream",
    subtitle: "A journey of resilience, purpose, and legacy.",
    description:
      "A motivational autobiography drawn from Lornette's elite-athlete lens, focused on perseverance, identity, discipline, and rising again after setbacks.",
    audience:
      "For aspiring athletes, coaches, youth leaders, and anyone driven to achieve ambitious goals.",
    priceLabel: "$14.99 CAD",
    format: "Digital Edition",
    image: {
      src: finishStrongBook,
      alt: "Finish Strong: Chasing the Olympic Dream book cover artwork.",
      crop: "object-center",
    },
    purchaseUrl: stripeBookLinks.roadToTheOlympics,
    stripePaymentLinkId: "plink_1TqLPUH99Nljn2XPX4TUpSQU",
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
      "A warm, encouraging guide for readers rebuilding hope, confidence, and perspective after difficult seasons.",
    audience:
      "For individuals, women's groups, mentoring circles, faith communities, and anyone seeking practical encouragement.",
    priceLabel: "$14.99 CAD",
    format: "Digital Edition",
    image: {
      src: survivingLife,
      alt: "Surviving Life book cover artwork, cropped to focus on the book.",
      crop: "object-center",
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

export const bookFeatures = [
  {
    title: "Surviving Life",
    subtitle: "A guide to resilience when life hits hard.",
    image: { src: survivingLife, alt: "Surviving Life book cover artwork.", crop: "object-top" },
  },
  {
    title: "Finish Strong: Chasing the Olympic Dream",
    subtitle: "A journey of resilience, purpose, and legacy.",
    image: {
      src: finishStrongBook,
      alt: "Finish Strong: Chasing the Olympic Dream book cover artwork.",
      crop: "object-top",
    },
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
    alt: "Athletic achievement artwork.",
    crop: "object-top scale-[1.04]",
  },
  athleteStrategy: {
    src: athleteStrategyPoster,
    alt: "Strategy, leadership, and elite execution artwork.",
    crop: "object-top scale-[1.03]",
  },
  aboutTimeline: {
    src: aboutTimelinePoster,
    alt: "Graduation and champion athlete story artwork.",
    crop: "object-top scale-[1.05]",
  },
  testimonialComposite: {
    src: testimonialComposite,
    alt: "Audience testimonial artwork.",
    crop: "object-top",
  },
  testimonialYouth: {
    src: testimonialYouth,
    alt: "Youth coaching testimonial artwork.",
    crop: "object-top",
  },
  eventWorkshop: {
    src: eventWorkshop,
    alt: "Workshop and event artwork.",
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
    alt: "Flight attendant graduate artwork.",
    crop: "object-top scale-[1.02]",
  },
  programOverview: {
    src: programOverview,
    alt: "Speaking and services overview artwork.",
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
