export type TrackId = "golf" | "hockey" | "corporate" | "europe";

export type CadenceStep = {
  step: string;
  title: string;
  desc: string;
};

export type GrillMeScenario = {
  id: string;
  title: string;
  stakes: string;
  context: string;
  challengePrompt: string;
};

export type QuickActionLabels = {
  journeyDesc: string;
  lessonsDesc: string;
  assessmentsDesc: string;
  resourcesDesc: string;
};

export type TrackConfig = {
  id: TrackId;
  label: string;
  shortTag: string;
  editorialBadge: string;
  overviewRoute: string;
  heroHeadline: string;
  heroSubtitle: string;
  heroTagline: string;
  heroDescription: string;
  heroImage: string;
  heroImageAlt: string;
  quoteEyebrow: string;
  quote: string;
  bottomImage: string;
  quickActionLabels: QuickActionLabels;
  routineTitle: string;
  routineSubtitle: string;
  routineSteps: CadenceStep[];
  goalTemplates: string[];
  grillMeScenarios: GrillMeScenario[];
};

export const TRACK_REGISTRY: Record<TrackId, TrackConfig> = {
  golf: {
    id: "golf",
    label: "Golf",
    shortTag: "Golf Championship",
    editorialBadge: "LORNETTE’S FOUNDATIONS GOLF",
    overviewRoute: "/foundations/golf",
    heroHeadline: "WELCOME TO MY PERFORMANCE EDGE",
    heroSubtitle: "Powered by the Performance Edge Framework",
    heroTagline: "Your guided Golf performance journey starts here.",
    heroDescription:
      "Build the mindset, habits, and somatic discipline to play with clarity, confidence, and consistency under tournament pressure.",
    heroImage: "/foundations/golf/dashboard/lornette-table-notebook-pen.png",
    heroImageAlt:
      "Lornette Daye with reflection journal and coffee on clubhouse terrace overlooking the fairway",
    quoteEyebrow: "FOUNDATION PRINCIPLE · LORNETTE DAYE",
    quote: "“A stronger you creates a stronger game.”",
    bottomImage: "/foundations/golf/sunlight-golf-fairway-sunrise.jpg",
    quickActionLabels: {
      journeyDesc: "Track your tournament milestones and weekly progress.",
      lessonsDesc: "10 Athletic Foundations for repeatable ball striking and focus.",
      assessmentsDesc: "Pre-shot cadence and emotional regulation benchmarks.",
      resourcesDesc: "Tournament warm-up blueprints, audio primers, and guides.",
    },
    routineTitle: "Pre-Shot Routine Cadence",
    routineSubtitle: "Repeatable execution before every swing under competition pressure",
    routineSteps: [
      {
        step: "1",
        title: "Target Assessment & Line",
        desc: "Stand behind the ball, identify precise target line and commit completely to club selection.",
      },
      {
        step: "2",
        title: "Diaphragmatic Breath & Grip",
        desc: "Take one smooth breath, release shoulder tension, and establish calibrated grip pressure.",
      },
      {
        step: "3",
        title: "Visual Lock & Commitment",
        desc: "Step in, align feet, gaze once at target, and execute the swing without doubt.",
      },
    ],
    goalTemplates: [
      "Break 74 in tournament qualifying round",
      "Zero double bogeys stemming from emotional frustration",
      "Maintain 100% pre-shot routine cadence consistency on back nine",
    ],
    grillMeScenarios: [
      {
        id: "sc-golf-18th-water",
        title: "18th Tee with Water Left & Out of Bounds Right",
        stakes: "Club Championship Final Round · 1-Shot Lead",
        context:
          "You are 1 shot off or holding a 1-shot lead on the 18th tee box. Water hugs the left side; thick trees and out-of-bounds line the right. The group ahead took 15 minutes to clear the green, so you've been standing in the wind. Your hands feel cold and your pulse is noticeably elevated.",
        challengePrompt:
          "Grill me: What is your exact physical reset cadence, where do your eyes lock, and what is your non-negotiable anchor cue before stepping into this shot?",
      },
      {
        id: "sc-golf-bogey-cascade",
        title: "Back-to-Back Bogeys Entering Tough 3-Hole Stretch",
        stakes: "Medal Play · Holes 16-18",
        context:
          "You just three-putted 14 and lipped out for par on 15. Your lead has vanished. A voice in your head says: 'You're giving this away again.' You have 3 minutes walking to the 16th tee box.",
        challengePrompt:
          "Grill me: How do you definitively close the door on the previous hole so your previous shot cannot hit your next shot?",
      },
      {
        id: "sc-golf-downhill-slider",
        title: "3-Foot Downhill Slider to Force Playoff",
        stakes: "18th Green · Match On The Line",
        context:
          "You have a 3-foot downhill, right-to-left putt to force sudden-death playoff. The entire clubhouse gallery is surrounding the fringe. You feel an impulse to hit it quickly just to get it over with.",
        challengePrompt:
          "Grill me: How do you govern your breath, pace your routine, and strike the putt with pure visual commitment?",
      },
    ],
  },

  hockey: {
    id: "hockey",
    label: "Hockey",
    shortTag: "Hockey High-Performance",
    editorialBadge: "LORNETTE’S FOUNDATIONS HOCKEY",
    overviewRoute: "/foundations/hockey",
    heroHeadline: "WELCOME TO HIGH-PERFORMANCE HOCKEY",
    heroSubtitle: "Championship Team Culture & Composure Systems",
    heroTagline:
      "Mental poise through high-speed transitions, third-period intensity, and physical pressure.",
    heroDescription:
      "Develop locked-in focus, five-second bench reset protocols, and non-defensive communication standards that elevate every shift.",
    heroImage: "/foundations/pathways/hockey/lornette-hockey-huddle-landscape.png",
    heroImageAlt: "Olympic-level coach Lornette Daye guiding competitive hockey team during on-ice practice",
    quoteEyebrow: "CHAMPIONSHIP CULTURE · LORNETTE DAYE",
    quote: "“Your last shift cannot play your next shift.”",
    bottomImage: "/foundations/banners/cinematic-hockey-rink.jpg",
    quickActionLabels: {
      journeyDesc: "Monitor shift consistency, reset logs, and season goals.",
      lessonsDesc: "10 Foundations for bench composure, physical poise, and speed.",
      assessmentsDesc: "Pressure response audits and shift reset evaluations.",
      resourcesDesc: "Locker room routines, shift checklists, and mental drills.",
    },
    routineTitle: "Pre-Shift Reset Cadence",
    routineSubtitle: "Five-second somatic bench reset before opening the gate",
    routineSteps: [
      {
        step: "1",
        title: "Gate Touch & Exhale",
        desc: "Touch glove to the boards, release breath fully, and dump emotion from the prior shift.",
      },
      {
        step: "2",
        title: "Shoulder Roll & Visual Lock",
        desc: "Roll shoulders back, unlock jaw tension, and locate ice space and immediate puck assignment.",
      },
      {
        step: "3",
        title: "Commitment Verbal Cue",
        desc: "Say your personal anchor cue out loud or mentally, and leap over the boards into full speed.",
      },
    ],
    goalTemplates: [
      "Zero retaliatory penalties after whistles through regular season",
      "Execute complete 5-second bench reset on 100% of shifts",
      "Lead bench communication with non-defensive, solution-focused callouts",
    ],
    grillMeScenarios: [
      {
        id: "sc-hockey-dzone-turnover",
        title: "Costly Defensive-Zone Turnover Leads to Tie Goal",
        stakes: "Third Period · 3 Minutes Remaining in Elimination Game",
        context:
          "A blind cross-ice clearing attempt was picked off at the blue line and slotted past your goalie. You skate back to the bench hearing murmurs from the crowd. Your defenseman partner is visibly angry. The coach stares right at you.",
        challengePrompt:
          "Grill me: What is your exact 5-second somatic reset process sitting on the bench to prevent this mistake from carrying over into your next ice shift?",
      },
      {
        id: "sc-hockey-bench-provocation",
        title: "Targeted Physical Provocation & Cheap Whistle",
        stakes: "Second Period · Opponent Trailing by 1",
        context:
          "Opposing agitator cross-checked you behind the play after the whistle. The referee missed it. As you skate past their bench, their players chirp your family name and attempt to bait you into a 4-minute retaliation major.",
        challengePrompt:
          "Grill me: How do you govern your somatic nervous system, protect your team from a disastrous penalty, and channel that adrenaline into speed?",
      },
      {
        id: "sc-hockey-penalty-kill",
        title: "5-on-3 Penalty Kill in Final Minute of Championship",
        stakes: "Final 60 Seconds · Holding a 1-Goal Lead",
        context:
          "Your team took two penalties in consecutive whistles. You are out on the ice blocking shots against the tournament’s top power play unit. Your legs burn, your stick vibrates from a blocked slapshot, and the arena noise is deafening.",
        challengePrompt:
          "Grill me: What is your visual attention anchor, how do you communicate with your goalie, and how do you execute clear defensive poise under extreme fatigue?",
      },
    ],
  },

  corporate: {
    id: "corporate",
    label: "Corporate",
    shortTag: "Corporate Leadership",
    editorialBadge: "LORNETTE’S FOUNDATIONS CORPORATE",
    overviewRoute: "/foundations/corporate",
    heroHeadline: "EXECUTIVE MENTAL PERFORMANCE & LEADERSHIP",
    heroSubtitle: "People-Centred Composure & Strategic Clarity",
    heroTagline:
      "Anchor your team with authoritative calm, disciplined execution, and high-trust accountability.",
    heroDescription:
      "Translate Olympic championship pedagogy into boardroom poise, calm sales floor consultation, and sustainable executive energy.",
    heroImage: "/foundations/pathways/corporate/lornette-corporate-keynote-stage.png",
    heroImageAlt: "Executive leadership workshop led by Olympic-level coach Lornette Daye in warm light",
    quoteEyebrow: "EXECUTIVE PEDAGOGY · LORNETTE DAYE",
    quote: "“Calm leadership creates confident teams.”",
    bottomImage: "/foundations/pathways/corporate/lornette-corporate-boardroom-portrait.png",
    quickActionLabels: {
      journeyDesc: "Review leadership milestones, quarterly goals, and team impact.",
      lessonsDesc: "10 Foundations for emotional regulation, focus, and strategic trust.",
      assessmentsDesc: "Executive stress triggers and cognitive reset diagnostics.",
      resourcesDesc: "Dealership consultation routines, decision frameworks, and tools.",
    },
    routineTitle: "Executive Meeting & Consultation Cadence",
    routineSubtitle: "Grounding protocol before high-stakes presentations and negotiations",
    routineSteps: [
      {
        step: "1",
        title: "Cognitive Clean-Slate Pause",
        desc: "Close laptop, silence devices 2 minutes prior, and clear emotional residue from previous emails.",
      },
      {
        step: "2",
        title: "Diaphragmatic Grounding",
        desc: "Take two calm abdominal breaths, plant both feet flat on the floor, and anchor physical posture.",
      },
      {
        step: "3",
        title: "Strategic Priority Anchor",
        desc: "Reaffirm the single non-negotiable outcome for the meeting before speaking.",
      },
    ],
    goalTemplates: [
      "Maintain non-defensive composure during heated monthly stakeholder review",
      "Eliminate reactive email responses within 20 minutes of trigger",
      "Conduct weekly 1-on-1 coaching debriefs using active-listening frameworks",
    ],
    grillMeScenarios: [
      {
        id: "sc-corp-boardroom-pushback",
        title: "Aggressive Boardroom Budget Veto & Public Challenge",
        stakes: "Annual Strategic Review · Board of Directors Present",
        context:
          "Midway through presenting your quarterly expansion initiative, a key director interrupts sharply, calling your operational projections 'reckless wishful thinking' and demanding an immediate line-item defense in front of the entire leadership team.",
        challengePrompt:
          "Grill me: How do you neutralize the surge of adrenaline, keep your vocal cadence authoritative, and re-frame the challenge without becoming defensive?",
      },
      {
        id: "sc-corp-showroom-objection",
        title: "Tense Dealership Trade-In Valuation Breakdown",
        stakes: "Month-End Closing Saturday · High-Value Client Threatens to Walk",
        context:
          "A premier client discovers their trade-in appraisal is $6,000 less than they expected. They slam their keys on the sales desk, accuse your team of dishonest dealing, and demand a discount in the showroom in front of other prospective buyers.",
        challengePrompt:
          "Grill me: What is your exact somatic composure routine to de-escalate the tension, protect your team’s dignity, and lead the client back to a collaborative consultation?",
      },
      {
        id: "sc-corp-crisis-timeline",
        title: "Operational Failure & Urgent Executive Crisis Briefing",
        stakes: "Product Launch Morning · 45 Minutes to Media Conference",
        context:
          "A major system outage has delayed scheduled deliveries across three regional distribution centers. Panic is erupting across Slack and the floor. You have 45 minutes to brief press, shareholders, and department heads.",
        challengePrompt:
          "Grill me: What protocol do you enact in the first 5 minutes to restore order, establish priority triage, and project unshakeable executive poise?",
      },
    ],
  },

  europe: {
    id: "europe",
    label: "European Sports",
    shortTag: "European Sports & GDPR",
    editorialBadge: "LORNETTE’S FOUNDATIONS EUROPE",
    overviewRoute: "/foundations/europe",
    heroHeadline: "EUROPEAN SPORT EXCELLENCE & ACADEMY SYSTEMS",
    heroSubtitle: "EU GDPR Compliant Platform · Mediterranean & Nordic Hubs",
    heroTagline:
      "Transatlantic high-performance mental conditioning and academy partnership pathways.",
    heroDescription:
      "Bridging North American championship pedagogy with European sport clubs, federations, and sports science ecosystems while maintaining complete EU data sovereignty.",
    heroImage: "/foundations/europe/european-sport-campus.png",
    heroImageAlt: "European sport campus in warm golden light with academy athletes",
    quoteEyebrow: "EUROPEAN ACADEMY PRINCIPLE · LORNETTE DAYE",
    quote: "“Excellence in sport begins with integrity in character.”",
    bottomImage: "/foundations/europe/sports-science-partnership.png",
    quickActionLabels: {
      journeyDesc: "Track international academy milestones and transatlantic tour progress.",
      lessonsDesc: "10 Foundations for character, poise, and high-performance consistency.",
      assessmentsDesc: "Somatic resilience diagnostics and academy selection benchmarks.",
      resourcesDesc: "Transatlantic travel protocols, academy guides, and research briefs.",
    },
    routineTitle: "International Competition Readiness Cadence",
    routineSubtitle: "Pre-match preparation across time zones, travel, and academy pathways",
    routineSteps: [
      {
        step: "1",
        title: "Travel & Circadian Sync",
        desc: "Hydration protocol, light exposure regulation, and somatic grounding after transatlantic travel.",
      },
      {
        step: "2",
        title: "Academy Culture Alignment",
        desc: "Respect local sporting heritage while executing Lornette Daye’s 10-Foundation personal reset.",
      },
      {
        step: "3",
        title: "Competition Focus Commitment",
        desc: "Engage pre-competition visualization calibrated to European federation playing conditions.",
      },
    ],
    goalTemplates: [
      "Maintain consistent mental routine across multi-city European competition tour",
      "Achieve full dual-career academic and athletic balance across 10 weeks",
      "Complete weekly somatic reflection debriefs within 24 hours of match day",
    ],
    grillMeScenarios: [
      {
        id: "sc-eu-academy-selection",
        title: "Continental Academy Selection Camp Pressure",
        stakes: "Final Evaluation Day · 3 Open Spots for 40 Athletes",
        context:
          "You are competing at a centralized European sports academy evaluation in Italy. Scouts, sports directors, and national coaches are watching from the sideline taking notes. In the first 10 minutes, you commit an unforced error.",
        challengePrompt:
          "Grill me: How do you reset immediately without allowing self-criticism or national performance anxiety to distort the rest of your assessment?",
      },
      {
        id: "sc-eu-hostile-away",
        title: "Hostile European Away Environment & Language Barrier",
        stakes: "Cup Quarterfinal Match · 5,000 Fanatical Supporters",
        context:
          "You are playing in an unfamiliar stadium in Greece or Central Europe with flares, chanting, and partisan refereeing. Communication with your teammates is nearly impossible due to the noise. Your heart is racing.",
        challengePrompt:
          "Grill me: How do you narrow your visual focus, rely on somatic anchor cues, and remain poised when the entire environment is designed to destabilize you?",
      },
      {
        id: "sc-eu-dual-career",
        title: "High-Stakes University Exams Clashing with Playoff Week",
        stakes: "Final Exam Tuesday · Federation Championship Semifinal Thursday",
        context:
          "You have 48 hours to study for critical university qualifications while attending double training sessions for the regional semifinals. Exhaustion is setting in, and you find yourself doubting whether you can sustain both commitments.",
        challengePrompt:
          "Grill me: How do you compartmentalize your cognitive energy so academic anxiety does not leak into competition, and physical fatigue does not cloud your academic focus?",
      },
    ],
  },
};

export function getTrackConfig(trackId: TrackId | string): TrackConfig {
  const normalized = (trackId || "golf").toLowerCase() as TrackId;
  return TRACK_REGISTRY[normalized] || TRACK_REGISTRY.golf;
}
