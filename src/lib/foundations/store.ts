"use client";

import { useSyncExternalStore } from "react";
import { createClient } from "@/lib/supabase/client";

export type ReviewStatus =
  | "pending_review"
  | "reviewed"
  | "approved"
  | "needs_revision";

export type WeeklyReflection = {
  foundationId: number;
  foundationTitle: string;
  noticed: string;
  worked: string;
  repeated: string;
  updatedAt: string;
};

export type PreShotStep = {
  step: string;
  title: string;
  desc: string;
};

export type GoalItem = {
  id: string;
  text: string;
  completed: boolean;
};

export type GrillMeSubmission = {
  id: string;
  scenarioId: string;
  scenarioTitle: string;
  pressureContext: string;
  golferResponse: string;
  resetProtocolApplied: string;
  anchorCueUsed: string;
  submittedAt: string;
  coachCritique?: string;
  status: "pending_grill" | "reviewed_by_lornette";
};

export type AthleteSubmission = {
  id: string;
  golferName: string;
  email: string;
  club: string;
  handicap: string;
  division: string;
  coachName: string;
  pressureSignal: string;
  resetProtocol: string;
  anchorCue: string;
  preShotRoutine: PreShotStep[];
  goals: GoalItem[];
  submittedAt: string;
  status: ReviewStatus;
  coachFeedbackNotes: string;
  reviewedAt?: string;
  reviewerName?: string;
  cohortId?: string;
  completedFoundations: number[];
  currentWeek: number;
  reflections: Record<number, WeeklyReflection>;
  grillMeSubmissions: GrillMeSubmission[];
};

export type InquiryItem = {
  id: string;
  name: string;
  organization: string;
  email: string;
  type: string;
  date: string;
  status: "new" | "contacted" | "proposal_sent" | "booked";
  notes: string;
};

export type CohortItem = {
  code: string;
  title: string;
  enrolled: number;
  capacity: number;
  currentWeek: number;
  startDate: string;
  club: string;
};

export type FoundationsStoreState = {
  isLoading: boolean;
  activeAthleteId: string;
  athletes: AthleteSubmission[];
  inquiries: InquiryItem[];
  cohorts: CohortItem[];
};

export const ADMIN_ATHLETE: AthleteSubmission = {
  id: "admin-coach-lornette",
  golferName: "Coach Lornette Daye",
  email: "admin@lornettedaye.com",
  club: "Royal Mayfair Golf Club & Private Practice",
  handicap: "+1.2",
  division: "Master Coach / Administrator",
  coachName: "Coach Lornette Daye",
  pressureSignal: "Accelerated tempo before critical approach",
  resetProtocol: "3-second diaphragmatic breath, club head rest, focal point anchor",
  anchorCue: "Composure first, swing second.",
  preShotRoutine: [
    { step: "1", title: "Target Assessment", desc: "Select target line and visualize trajectory." },
    { step: "2", title: "Breathing & Grip", desc: "Take a deep breath and lock consistent grip pressure." },
    { step: "3", title: "Commitment", desc: "Step in and execute without second guessing." },
  ],
  goals: [
    { id: "g1", text: "Master emotional regulation under tournament pressure", completed: true },
    { id: "g2", text: "Maintain strict pre-shot routine consistency across 18 holes", completed: true },
    { id: "g3", text: "Review weekly reflections with athletes after each round", completed: false },
  ],
  submittedAt: "2026-09-01T12:00:00.000Z",
  status: "approved",
  coachFeedbackNotes: "Outstanding poise on the back nine. Pre-shot routine is noticeably more stable under pressure.",
  completedFoundations: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
  currentWeek: 10,
  reflections: {
    1: {
      foundationId: 1,
      foundationTitle: "Foundation 1: Identity Beyond Sport",
      noticed: "Felt centered and grounded before competition.",
      worked: "Separating personal self-worth from score outcome.",
      repeated: "Morning mental focus reflection routine.",
      updatedAt: "2026-09-02T10:00:00.000Z",
    },
  },
  grillMeSubmissions: [],
};

export const SAMPLE_ATHLETES: AthleteSubmission[] = [
  ADMIN_ATHLETE,
  {
    id: "derrick-fall-2026",
    golferName: "Derrick Vance",
    email: "derrick@performanceedge.com",
    club: "Royal Mayfair Golf Club",
    handicap: "3.4",
    division: "Men's Amateur Championship",
    coachName: "Coach Lornette Daye",
    pressureSignal: "Tightened shoulders before tee shot",
    resetProtocol: "Exhale through tension, shoulder roll, refocus on target",
    anchorCue: "Smooth rhythm, trust the line.",
    preShotRoutine: [
      { step: "1", title: "Target & Lie", desc: "Assess lie and commit to club." },
      { step: "2", title: "Practice Swing", desc: "One fluid rehearsal feel." },
      { step: "3", title: "Step In", desc: "Align feet and swing with trust." },
    ],
    goals: [
      { id: "dg1", text: "Break 74 in qualifying", completed: true },
      { id: "dg2", text: "Zero double bogeys from emotional frustration", completed: false },
    ],
    submittedAt: "2026-09-05T14:00:00.000Z",
    status: "reviewed",
    coachFeedbackNotes: "Great progress on breathing discipline at the turn.",
    completedFoundations: [1, 2, 3, 4],
    currentWeek: 5,
    reflections: {},
    grillMeSubmissions: [],
  },
];

const DEFAULT_ATHLETE: AthleteSubmission = ADMIN_ATHLETE;

const DEFAULT_STORE: FoundationsStoreState = {
  isLoading: false,
  activeAthleteId: "admin-coach-lornette",
  athletes: SAMPLE_ATHLETES,
  inquiries: [],
  cohorts: [
    {
      code: "ROYAL-SUMMER-2026",
      title: "Royal Mayfair Competitive Cohort",
      enrolled: 12,
      capacity: 15,
      currentWeek: 4,
      startDate: "2026-06-01",
      club: "Royal Mayfair Golf Club",
    },
    {
      code: "DERRICK-FALL-2026",
      title: "Championship Fall Invitational",
      enrolled: 8,
      capacity: 12,
      currentWeek: 1,
      startDate: "2026-09-15",
      club: "Private Member Club",
    },
  ],
};

let memoryStore: FoundationsStoreState = DEFAULT_STORE;
let initialized = false;

const EVENT_KEY = "ld_foundations_store_update";

function getStore(): FoundationsStoreState {
  return memoryStore;
}

function notifyStoreUpdate(nextState: FoundationsStoreState) {
  memoryStore = nextState;
  if (typeof window !== "undefined") {
    window.dispatchEvent(new CustomEvent(EVENT_KEY, { detail: nextState }));
  }
}

function subscribeToStore(callback: () => void) {
  if (typeof window === "undefined") return () => {};
  window.addEventListener(EVENT_KEY, callback);
  return () => {
    window.removeEventListener(EVENT_KEY, callback);
  };
}

export function useFoundationsStore() {
  const state = useSyncExternalStore(subscribeToStore, getStore, () => DEFAULT_STORE);

  const activeAthlete =
    state.athletes.find((a) => a.id === state.activeAthleteId) || state.athletes[0] || DEFAULT_ATHLETE;

  const initData = async () => {
    if (initialized) return;
    initialized = true;
    try {
      const supabase = createClient();
      const { data: { user } } = await supabase.auth.getUser();
      if (!user) {
        notifyStoreUpdate({ ...memoryStore, isLoading: false });
        return;
      }
      
      const { data: profile } = await supabase.from('profiles').select('*').eq('id', user.id).single();
      if (!profile) {
        notifyStoreUpdate({ ...memoryStore, isLoading: false });
        return;
      }
      
      const { data: cohortMembers } = await supabase.from('cohort_members').select('*, cohorts(*)').eq('profile_id', user.id);
      const cohortMember = cohortMembers?.[0];
      
      const { data: plans } = await supabase.from('performance_plans').select('*').eq('profile_id', user.id);
      const plan = plans?.[0];
      
      let coachFeedbackNotes = "";
      let status: ReviewStatus = "pending_review";
      if (plan) {
         const { data: reviews } = await supabase.from('mentor_reviews').select('*').eq('plan_id', plan.id).order('reviewed_at', { ascending: false });
         if (reviews && reviews.length > 0) {
             coachFeedbackNotes = reviews[0].review_notes;
             status = "reviewed";
         }
      }
      
      const { data: reflections } = await supabase.from('weekly_reflections').select('*').eq('profile_id', user.id);
      const reflectionsRecord: Record<number, WeeklyReflection> = {};
      const completedFoundations = new Set<number>();
      
      if (reflections) {
        (reflections as unknown as Array<{
          week_number: number;
          what_noticed?: string;
          what_worked?: string;
          what_repeat?: string;
          submitted_at: string;
        }>).forEach((r) => {
          reflectionsRecord[r.week_number] = {
            foundationId: r.week_number,
            foundationTitle: `Foundation ${r.week_number}`,
            noticed: r.what_noticed || "",
            worked: r.what_worked || "",
            repeated: r.what_repeat || "",
            updatedAt: r.submitted_at,
          };
          completedFoundations.add(r.week_number);
        });
      }
      
      const { data: progress } = await supabase.from('participant_progress').select('*, curriculum_activities(*)').eq('profile_id', user.id);
      if (progress) {
        (progress as unknown as Array<{
          curriculum_activities?: { week_number?: number } | null;
        }>).forEach((p) => {
          if (p.curriculum_activities?.week_number) {
            completedFoundations.add(p.curriculum_activities.week_number);
          }
        });
      }
      
      const athlete: AthleteSubmission = {
        id: user.id,
        golferName: profile.full_name || "Golfer",
        email: profile.email || "",
        club: profile.home_club || "",
        handicap: profile.handicap_index || "",
        division: profile.division || "",
        coachName: profile.pga_coach_alignment || "",
        pressureSignal: plan?.pressure_signal || "",
        resetProtocol: plan?.reset_protocol || "",
        anchorCue: plan?.anchor_cue || "",
        preShotRoutine: (plan?.pre_shot_cadence as PreShotStep[]) || [],
        goals: (plan?.goals_30_day as GoalItem[]) || [],
        submittedAt: plan?.submitted_at || "",
        status: status,
        coachFeedbackNotes,
        completedFoundations: Array.from(completedFoundations).sort((a,b) => a-b),
        cohortId: cohortMember?.cohort_id || "",
        currentWeek: cohortMember?.current_week || 1,
        reflections: reflectionsRecord,
        grillMeSubmissions: [],
      };
      
      notifyStoreUpdate({
        ...memoryStore,
        isLoading: false,
        activeAthleteId: user.id,
        athletes: [athlete]
      });
      
    } catch(e) {
      console.error(e);
      notifyStoreUpdate({ ...memoryStore, isLoading: false });
    }
  };

  const updateActivePlan = async (updates: {
    pressureSignal?: string;
    resetProtocol?: string;
    anchorCue?: string;
    goals?: GoalItem[];
  }) => {
    const nextState: FoundationsStoreState = {
      ...state,
      athletes: state.athletes.map((ath) => {
        if (ath.id !== state.activeAthleteId) return ath;
        return {
          ...ath,
          pressureSignal: updates.pressureSignal ?? ath.pressureSignal,
          resetProtocol: updates.resetProtocol ?? ath.resetProtocol,
          anchorCue: updates.anchorCue ?? ath.anchorCue,
          goals: updates.goals ?? ath.goals,
          status: "pending_review",
        };
      }),
    };
    notifyStoreUpdate(nextState);
    
    try {
        const supabase = createClient();
        const { data: { user } } = await supabase.auth.getUser();
        if(!user) return;
        
        const { data: cohortMembers } = await supabase.from('cohort_members').select('*').eq('profile_id', user.id).limit(1);
        const cohort_id = cohortMembers?.[0]?.cohort_id;
        if(!cohort_id) return;
        
        const active = nextState.athletes.find(a => a.id === state.activeAthleteId)!;
        await supabase.from('performance_plans').upsert({
            profile_id: user.id,
            cohort_id: cohort_id,
            pressure_signal: active.pressureSignal,
            reset_protocol: active.resetProtocol,
            anchor_cue: active.anchorCue,
            goals_30_day: active.goals,
            updated_at: new Date().toISOString()
        }, { onConflict: 'profile_id, cohort_id' });
    } catch(e) {
        console.error(e);
    }
  };

  const saveReflection = async (
    foundationId: number,
    foundationTitle: string,
    noticed: string,
    worked: string,
    repeated: string
  ) => {
    const nextState: FoundationsStoreState = {
      ...state,
      athletes: state.athletes.map((ath) => {
        if (ath.id !== state.activeAthleteId) return ath;
        const newReflections = {
          ...ath.reflections,
          [foundationId]: {
            foundationId,
            foundationTitle,
            noticed,
            worked,
            repeated,
            updatedAt: new Date().toISOString(),
          },
        };
        const completedSet = new Set(ath.completedFoundations);
        completedSet.add(foundationId);
        return {
          ...ath,
          reflections: newReflections,
          completedFoundations: Array.from(completedSet).sort((a, b) => a - b),
        };
      }),
    };
    notifyStoreUpdate(nextState);
    
    try {
        const supabase = createClient();
        const { data: { user } } = await supabase.auth.getUser();
        if(!user) return;
        
        const { data: cohortMembers } = await supabase.from('cohort_members').select('*').eq('profile_id', user.id).limit(1);
        const cohort_id = cohortMembers?.[0]?.cohort_id;
        if(!cohort_id) return;
        
        const { data: existing } = await supabase.from('weekly_reflections')
            .select('id').eq('profile_id', user.id).eq('week_number', foundationId).single();
            
        if (existing) {
             await supabase.from('weekly_reflections').update({
                what_noticed: noticed,
                what_worked: worked,
                what_repeat: repeated,
                submitted_at: new Date().toISOString()
             }).eq('id', existing.id);
        } else {
             await supabase.from('weekly_reflections').insert({
                cohort_id: cohort_id,
                week_number: foundationId,
                profile_id: user.id,
                prompt_question: foundationTitle,
                response_text: "Reflection",
                what_noticed: noticed,
                what_worked: worked,
                what_repeat: repeated
             });
        }
    } catch(e) {
        console.error(e);
    }
  };

  const submitGrillMeChallenge = (submission: Omit<GrillMeSubmission, "id" | "submittedAt" | "status">) => {
      const newEntry: GrillMeSubmission = {
      ...submission,
      id: `grill-${Date.now()}`,
      submittedAt: new Date().toLocaleDateString("en-US", {
        month: "short",
        day: "numeric",
        year: "numeric",
      }),
      status: "pending_grill",
    };
    const nextState: FoundationsStoreState = {
      ...state,
      athletes: state.athletes.map((ath) => {
        if (ath.id !== state.activeAthleteId) return ath;
        return {
          ...ath,
          grillMeSubmissions: [newEntry, ...ath.grillMeSubmissions],
        };
      }),
    };
    notifyStoreUpdate(nextState);
    return newEntry;
  };
  
  const updateCoachReview = (
    athleteId: string,
    reviewData: {
      status: ReviewStatus;
      feedbackNotes: string;
      reviewerName?: string;
    }
  ) => {};
  const updateGrillMeCritique = (
    athleteId: string,
    grillSubmissionId: string,
    critique: string
  ) => {};
  const updateInquiryStatus = (
    inquiryId: string,
    status: InquiryItem["status"]
  ) => {};
  const setActiveAthleteId = (id: string) => {
    notifyStoreUpdate({
      ...state,
      activeAthleteId: id,
    });
  };

  const redeemCohortCode = (params: {
    name: string;
    email: string;
    code: string;
    handicap?: string;
    division?: string;
    coachName?: string;
  }): { success: boolean; message: string; athleteId?: string } => {
    const codeUpper = (params.code || "").trim().toUpperCase();
    const adminCodes = [
      "LD-ADMIN-2026",
      "ADMIN2026",
      "LORNETTE-ADMIN",
      "COACH2026",
    ];

    if (adminCodes.includes(codeUpper)) {
      setActiveAthleteId(ADMIN_ATHLETE.id);
      return {
        success: true,
        message: "Admin code accepted. Welcome Coach Lornette Daye.",
        athleteId: ADMIN_ATHLETE.id,
      };
    }

    const matched = state.cohorts.find(
      (c) => c.code.toUpperCase() === codeUpper
    );

    const newAthlete: AthleteSubmission = {
      ...DEFAULT_ATHLETE,
      id: `athlete-${Date.now()}`,
      golferName: params.name,
      email: params.email,
      club: matched?.club || "Private Member Club",
      handicap: params.handicap || "5.0",
      division: params.division || "Amateur",
      coachName: params.coachName || "Coach Lornette Daye",
      submittedAt: new Date().toISOString(),
      currentWeek: matched?.currentWeek || 1,
    };

    notifyStoreUpdate({
      ...state,
      activeAthleteId: newAthlete.id,
      athletes: [newAthlete, ...state.athletes],
    });

    return {
      success: true,
      message: `Welcome, ${params.name}. Your workspace has been activated.`,
      athleteId: newAthlete.id,
    };
  };

  const advanceCohortWeek = (code: string) => {
    notifyStoreUpdate({
      ...state,
      cohorts: state.cohorts.map((c) =>
        c.code.toUpperCase() === code.toUpperCase()
          ? { ...c, currentWeek: Math.min(10, c.currentWeek + 1) }
          : c
      ),
    });
  };

  const updateAthleteProfile = (
    updates: Partial<
      Pick<
        AthleteSubmission,
        "golferName" | "email" | "club" | "handicap" | "division" | "coachName"
      >
    >
  ) => {
    notifyStoreUpdate({
      ...state,
      athletes: state.athletes.map((ath) =>
        ath.id === state.activeAthleteId ? { ...ath, ...updates } : ath
      ),
    });
  };

  return {
    state,
    activeAthlete,
    updateActivePlan,
    saveReflection,
    submitGrillMeChallenge,
    updateCoachReview,
    updateGrillMeCritique,
    updateInquiryStatus,
    setActiveAthleteId,
    redeemCohortCode,
    advanceCohortWeek,
    updateAthleteProfile,
    initData,
  };
}
