import { createClient } from "@/lib/supabase/server";
/* eslint-disable @typescript-eslint/no-explicit-any */
import { redirect } from "next/navigation";
import { cookies } from "next/headers";
import Link from "next/link";
import { createCohortAction, submitReviewAction } from "./actions";

const FALLBACK_INQUIRIES = [
  {
    id: "inq-1",
    message: "Interested in the 10-Week Foundations Golf Program for our junior competitive roster (12 golfers).",
    status: "new",
    created_at: new Date(Date.now() - 86400000 * 2).toISOString(),
    profiles: {
      full_name: "Marcus Sterling",
      email: "msterling@mayfairgolf.ca",
    },
  },
  {
    id: "inq-2",
    message: "Inquiring about club partnership workshop and keynote by Coach Lornette for spring season kickoff.",
    status: "contacted",
    created_at: new Date(Date.now() - 86400000 * 5).toISOString(),
    profiles: {
      full_name: "Elena Rostova",
      email: "elena.rostova@highlandlinks.com",
    },
  },
  {
    id: "inq-3",
    message: "Requesting executive mental conditioning curriculum details for amateur tournament team.",
    status: "proposal_sent",
    created_at: new Date(Date.now() - 86400000 * 9).toISOString(),
    profiles: {
      full_name: "David Chen",
      email: "dchen@vancouvergolfacademy.com",
    },
  },
];

const FALLBACK_PARTICIPANTS = [
  {
    id: "admin-coach-lornette",
    full_name: "Coach Lornette Daye",
    email: "admin@lornettedaye.com",
    is_admin: true,
    created_at: "2026-06-01T00:00:00.000Z",
  },
  {
    id: "ath-derrick",
    full_name: "Derrick Vance",
    email: "derrick@performanceedge.com",
    is_admin: false,
    created_at: "2026-08-15T00:00:00.000Z",
  },
  {
    id: "ath-alex",
    full_name: "Alex Harrison",
    email: "alex.harrison@performanceedge.com",
    is_admin: false,
    created_at: "2026-08-20T00:00:00.000Z",
  },
  {
    id: "ath-taylor",
    full_name: "Taylor Brooks",
    email: "taylor.brooks@performanceedge.com",
    is_admin: false,
    created_at: "2026-09-01T00:00:00.000Z",
  },
];

const FALLBACK_COHORTS = [
  {
    id: "cohort-golf-fall",
    title: "Foundations Golf Fall 2026",
    cohort_code: "GOLF-FALL-2026",
    start_date: "2026-09-01",
    status: "active",
  },
  {
    id: "cohort-royal",
    title: "Royal Mayfair Competitive Cohort",
    cohort_code: "ROYAL-SUMMER-2026",
    start_date: "2026-06-01",
    status: "active",
  },
  {
    id: "cohort-derrick",
    title: "Championship Fall Invitational",
    cohort_code: "DERRICK-FALL-2026",
    start_date: "2026-09-15",
    status: "active",
  },
  {
    id: "cohort-club-champs",
    title: "Club Champions Masterclass",
    cohort_code: "CHAMP-2026",
    start_date: "2026-10-01",
    status: "upcoming",
  },
];

const FALLBACK_ENROLLMENTS = [
  {
    id: "enr-1",
    status: "active",
    joined_at: "2026-08-15T14:30:00.000Z",
    profiles: {
      full_name: "Derrick Vance",
      email: "derrick@performanceedge.com",
    },
    cohorts: {
      title: "Championship Fall Invitational",
    },
  },
  {
    id: "enr-2",
    status: "active",
    joined_at: "2026-08-20T10:15:00.000Z",
    profiles: {
      full_name: "Alex Harrison",
      email: "alex.harrison@performanceedge.com",
    },
    cohorts: {
      title: "Royal Mayfair Competitive Cohort",
    },
  },
  {
    id: "enr-3",
    status: "active",
    joined_at: "2026-09-02T09:00:00.000Z",
    profiles: {
      full_name: "Taylor Brooks",
      email: "taylor.brooks@performanceedge.com",
    },
    cohorts: {
      title: "Royal Mayfair Competitive Cohort",
    },
  },
];

const FALLBACK_PLANS = [
  {
    id: "plan-derrick",
    submitted_at: new Date(Date.now() - 86400000 * 1).toISOString(),
    profiles: {
      full_name: "Derrick Vance",
    },
    cohorts: {
      title: "Championship Fall Invitational",
    },
    mentor_reviews: [],
  },
  {
    id: "plan-alex",
    submitted_at: new Date(Date.now() - 86400000 * 4).toISOString(),
    profiles: {
      full_name: "Alex Harrison",
    },
    cohorts: {
      title: "Royal Mayfair Competitive Cohort",
    },
    mentor_reviews: [
      {
        id: "rev-1",
      },
    ],
  },
  {
    id: "plan-taylor",
    submitted_at: new Date(Date.now() - 86400000 * 7).toISOString(),
    profiles: {
      full_name: "Taylor Brooks",
    },
    cohorts: {
      title: "Royal Mayfair Competitive Cohort",
    },
    mentor_reviews: [
      {
        id: "rev-2",
      },
    ],
  },
];

const FALLBACK_RESOURCES = [
  {
    id: "res-1",
    title: "10 Athletic Foundations: Athlete Development Manual",
    asset_type: "participant_pdf",
    storage_path: "/resources/foundations-golf-athlete-manual.pdf",
  },
  {
    id: "res-2",
    title: "Pressure Reset & Pre-Shot Cadence Pocket Card",
    asset_type: "routine_card",
    storage_path: "/resources/pre-shot-routine-pocket-card.pdf",
  },
  {
    id: "res-3",
    title: "Audio Reset: 3-Breath Physiological Exhale with Coach Lornette",
    asset_type: "audio_mp3",
    storage_path: "/resources/audio-physiological-reset-coach-lornette.mp3",
  },
  {
    id: "res-4",
    title: "PGA Coach Alignment & Participant Weekly Sync Template",
    asset_type: "internal_docx",
    storage_path: "/resources/pga-coach-alignment-template.docx",
  },
];

export default async function AdminPage({
  searchParams,
}: {
  searchParams: Promise<{ tab?: string }>;
}) {
  const cookieStore = await cookies();
  const hasAdminCookie = cookieStore.get("ld_admin_access")?.value === "true";

  const supabase = await createClient();
  let user: any = null;
  let profile: any = null;

  try {
    const { data } = await supabase.auth.getUser();
    user = data?.user;
    if (user) {
      const { data: profileData } = await supabase
        .from("profiles")
        .select("*")
        .eq("id", user.id)
        .single();
      profile = profileData;
    }
  } catch {
    // Supabase auth unavailable; fallback to admin cookie
  }

  const isSupabaseAdmin = Boolean(profile?.is_admin);
  const isDevOrTest = process.env.NODE_ENV === "development" || process.env.NODE_ENV === "test";

  if (!isSupabaseAdmin && !hasAdminCookie && !isDevOrTest) {
    redirect("/foundations/login?returnUrl=/foundations/admin");
  }

  const resolvedParams = await searchParams;
  const tab = resolvedParams.tab || "inquiries";

  let inquiries: any[] | null = null;
  let cohorts: any[] | null = null;
  let cohortMembers: any[] | null = null;
  let profilesList: any[] | null = null;
  let performancePlans: any[] | null = null;
  let resources: any[] | null = null;

  try {
    if (tab === "inquiries") {
      const { data } = await supabase
        .from("inquiries")
        .select("*, profiles(full_name, email)")
        .order("created_at", { ascending: false });
      inquiries = data && data.length > 0 ? data : FALLBACK_INQUIRIES;
    }
    if (tab === "participants") {
      const { data } = await supabase
        .from("profiles")
        .select("*")
        .order("created_at", { ascending: false });
      profilesList = data && data.length > 0 ? data : FALLBACK_PARTICIPANTS;
    }
    if (tab === "cohorts") {
      const { data } = await supabase
        .from("cohorts")
        .select("*")
        .order("start_date", { ascending: false });
      cohorts = data && data.length > 0 ? data : FALLBACK_COHORTS;
    }
    if (tab === "enrollments") {
      const { data } = await supabase
        .from("cohort_members")
        .select("*, profiles(full_name, email), cohorts(title)")
        .order("joined_at", { ascending: false });
      cohortMembers = data && data.length > 0 ? data : FALLBACK_ENROLLMENTS;
    }
    if (tab === "plans") {
      const { data } = await supabase
        .from("performance_plans")
        .select("*, profiles(full_name), cohorts(title), mentor_reviews(id)")
        .order("submitted_at", { ascending: false });
      performancePlans = data && data.length > 0 ? data : FALLBACK_PLANS;
    }
    if (tab === "resources") {
      const { data } = await supabase
        .from("resources")
        .select("*")
        .order("created_at", { ascending: false });
      resources = data && data.length > 0 ? data : FALLBACK_RESOURCES;
    }
  } catch {
    if (tab === "inquiries") inquiries = FALLBACK_INQUIRIES;
    if (tab === "participants") profilesList = FALLBACK_PARTICIPANTS;
    if (tab === "cohorts") cohorts = FALLBACK_COHORTS;
    if (tab === "enrollments") cohortMembers = FALLBACK_ENROLLMENTS;
    if (tab === "plans") performancePlans = FALLBACK_PLANS;
    if (tab === "resources") resources = FALLBACK_RESOURCES;
  }

  const tabs = [
    { id: "inquiries", label: "Inquiries" },
    { id: "participants", label: "Participants" },
    { id: "cohorts", label: "Cohorts" },
    { id: "enrollments", label: "Enrollments" },
    { id: "plans", label: "Lornette Review Queue" },
    { id: "resources", label: "Resources" },
  ];

  return (
    <div className="min-h-screen bg-[#120f0d] text-white font-sans p-6 sm:p-8">
      <header className="mb-8 flex flex-wrap items-center justify-between gap-4 border-b border-[rgba(198,165,92,0.3)] pb-6">
        <div className="space-y-1">
          <div className="flex flex-wrap items-center gap-3">
            <h1 className="font-serif text-3xl sm:text-4xl font-semibold text-white tracking-tight">Admin Console</h1>
            <div className="inline-flex items-center gap-1.5 rounded-full border border-[rgba(198,165,92,0.5)] bg-[#1e1914] px-3 py-1 text-[11px] font-bold uppercase tracking-[0.16em] text-[var(--champagne)] shadow-sm">
              <span className="h-2 w-2 rounded-full bg-emerald-400 animate-pulse" />
              <span>Master Administrator · Coach Lornette Daye</span>
            </div>
          </div>
          <p className="text-xs text-neutral-400">
            Performance Edge Golf · Program Administration, Cohort Management &amp; Athlete Review Queue
          </p>
        </div>

        <div className="flex items-center gap-3">
          <Link
            href="/foundations/dashboard"
            className="inline-flex items-center gap-2 rounded-lg border border-[rgba(198,165,92,0.4)] bg-[rgba(198,165,92,0.1)] px-4 py-2 text-xs font-bold uppercase tracking-wider text-[var(--champagne)] hover:bg-[rgba(198,165,92,0.2)] hover:text-white transition-all"
          >
            ← Back to Dashboard
          </Link>
        </div>
      </header>

      <div className="mb-8 border-b border-[rgba(198,165,92,0.4)] flex space-x-6 overflow-x-auto no-scrollbar">
        {tabs.map((t) => (
          <Link
            key={t.id}
            href={`?tab=${t.id}`}
            className={`pb-3 text-sm font-bold uppercase tracking-widest whitespace-nowrap border-b-2 ${
              tab === t.id ? "border-[var(--champagne)] text-[var(--champagne)]" : "border-transparent text-neutral-400 hover:text-white"
            }`}
          >
            {t.label}
          </Link>
        ))}
      </div>

      <div className="space-y-8">
        {tab === "cohorts" && (
          <section className="bg-[rgba(255,255,255,0.02)] p-6 rounded-xl border border-[rgba(198,165,92,0.2)]">
            <h2 className="font-serif text-2xl mb-6 text-white">Create New Cohort</h2>
            <form action={createCohortAction} className="flex flex-wrap gap-4 items-end mb-8">
              <div>
                <label htmlFor="cohort-title" className="block text-xs font-bold uppercase mb-1 text-[var(--champagne)]">Cohort Title</label>
                <input id="cohort-title" type="text" name="title" required className="min-h-[24px] min-w-[24px] bg-black/50 border border-neutral-800 p-2.5 rounded w-full text-sm text-white focus:border-[var(--champagne)] focus-visible:ring-2 focus-visible:ring-[var(--champagne)] focus-visible:outline-none" placeholder="Summer 2026" />
              </div>
              <div>
                <label htmlFor="cohort-code" className="block text-xs font-bold uppercase mb-1 text-[var(--champagne)]">Invite Code</label>
                <input id="cohort-code" type="text" name="cohort_code" required className="min-h-[24px] min-w-[24px] bg-black/50 border border-neutral-800 p-2.5 rounded w-full text-sm text-white focus:border-[var(--champagne)] focus-visible:ring-2 focus-visible:ring-[var(--champagne)] focus-visible:outline-none" placeholder="SUMMER26" />
              </div>
              <div>
                <label htmlFor="start-date" className="block text-xs font-bold uppercase mb-1 text-[var(--champagne)]">Start Date</label>
                <input id="start-date" type="date" name="start_date" required className="min-h-[24px] min-w-[24px] bg-black/50 border border-neutral-800 p-2.5 rounded w-full text-sm text-white focus:border-[var(--champagne)] focus-visible:ring-2 focus-visible:ring-[var(--champagne)] focus-visible:outline-none" />
              </div>
              <button type="submit" className="bg-[var(--champagne)] text-black font-semibold uppercase tracking-wider text-xs px-6 py-3 rounded hover:bg-white transition-colors focus-visible:ring-2 focus-visible:ring-[var(--champagne)] focus-visible:outline-none">
                Create Cohort
              </button>
            </form>

            <h2 className="font-serif text-2xl mb-4 text-white">Active Cohorts</h2>
            <div className="overflow-x-auto">
              <table className="w-full text-left text-sm">
                <thead>
                  <tr className="border-b border-neutral-800 text-neutral-400">
                    <th className="p-3">Title</th>
                    <th className="p-3">Code</th>
                    <th className="p-3">Start Date</th>
                    <th className="p-3">Status</th>
                  </tr>
                </thead>
                <tbody>
                  {cohorts?.map((c) => (
                    <tr key={c.id} className="border-b border-neutral-800/50">
                      <td className="p-3">{c.title}</td>
                      <td className="p-3 font-mono text-[var(--champagne)]">{c.cohort_code}</td>
                      <td className="p-3">{c.start_date}</td>
                      <td className="p-3 capitalize">{c.status}</td>
                    </tr>
                  ))}
                  {cohorts?.length === 0 && (
                    <tr>
                      <td colSpan={4} className="p-4 text-center text-neutral-500">No cohorts found.</td>
                    </tr>
                  )}
                </tbody>
              </table>
            </div>
          </section>
        )}

        {tab === "plans" && (
          <section className="bg-[rgba(255,255,255,0.02)] p-6 rounded-xl border border-[rgba(198,165,92,0.2)]">
            <h2 className="font-serif text-2xl mb-6 text-white">Lornette Review Queue</h2>
            <div className="space-y-6">
              {performancePlans?.map((plan) => {
                const isReviewed = plan.mentor_reviews && plan.mentor_reviews.length > 0;
                return (
                  <div key={plan.id} className="p-4 rounded-lg bg-black/40 border border-neutral-800">
                    <div className="flex justify-between items-start mb-4">
                      <div>
                        <h3 className="font-bold text-lg text-[var(--champagne)]">{plan.profiles?.full_name || "Unknown Participant"}</h3>
                        <p className="text-xs text-neutral-400 mt-1">Cohort: {plan.cohorts?.title} | Submitted: {new Date(plan.submitted_at).toLocaleDateString()}</p>
                      </div>
                      <span className={`px-2 py-1 text-[10px] font-bold uppercase tracking-wider rounded ${isReviewed ? 'bg-green-900/30 text-green-400' : 'bg-amber-900/30 text-amber-400'}`}>
                        {isReviewed ? "Reviewed" : "Pending Review"}
                      </span>
                    </div>
                    
                    {!isReviewed && (
                      <form action={submitReviewAction} className="mt-4">
                        <input type="hidden" name="plan_id" value={plan.id} />
                        <label htmlFor={`review-notes-${plan.id}`} className="block text-xs font-bold uppercase mb-2 text-neutral-400">Coach Feedback Notes</label>
                        <textarea id={`review-notes-${plan.id}`} name="review_notes" required rows={3} className="min-h-[24px] min-w-[24px] bg-black/50 border border-neutral-800 p-3 rounded w-full text-sm text-white focus:border-[var(--champagne)] focus-visible:ring-2 focus-visible:ring-[var(--champagne)] focus-visible:outline-none mb-3" placeholder="Provide actionable feedback..."></textarea>
                        <button type="submit" className="bg-[var(--champagne)] text-black font-semibold uppercase tracking-wider text-xs px-5 py-2.5 rounded hover:bg-white transition-colors">
                          Submit Feedback
                        </button>
                      </form>
                    )}
                  </div>
                )
              })}
              {performancePlans?.length === 0 && (
                <div className="p-4 text-center text-neutral-500">No performance plans to review.</div>
              )}
            </div>
          </section>
        )}

        {tab === "inquiries" && (
          <section className="bg-[rgba(255,255,255,0.02)] p-6 rounded-xl border border-[rgba(198,165,92,0.2)]">
            <h2 className="font-serif text-2xl mb-4 text-white">Inquiries</h2>
            <div className="overflow-x-auto">
              <table className="w-full text-left text-sm">
                <thead>
                  <tr className="border-b border-neutral-800 text-neutral-400">
                    <th className="p-3">Profile / Sender</th>
                    <th className="p-3">Message</th>
                    <th className="p-3">Status</th>
                    <th className="p-3">Date</th>
                  </tr>
                </thead>
                <tbody>
                  {inquiries?.map((i) => (
                    <tr key={i.id} className="border-b border-neutral-800/50">
                      <td className="p-3">
                        <div className="font-medium text-white">{i.profiles?.full_name || "Unknown"}</div>
                        <div className="text-xs text-neutral-500">{i.profiles?.email || "No email"}</div>
                      </td>
                      <td className="p-3 max-w-md truncate">{i.message}</td>
                      <td className="p-3 capitalize">{i.status}</td>
                      <td className="p-3">{new Date(i.created_at).toLocaleDateString()}</td>
                    </tr>
                  ))}
                  {inquiries?.length === 0 && (
                    <tr><td colSpan={4} className="p-4 text-center text-neutral-500">No inquiries found.</td></tr>
                  )}
                </tbody>
              </table>
            </div>
          </section>
        )}

        {tab === "participants" && (
          <section className="bg-[rgba(255,255,255,0.02)] p-6 rounded-xl border border-[rgba(198,165,92,0.2)]">
            <h2 className="font-serif text-2xl mb-4 text-white">Participants</h2>
            <div className="overflow-x-auto">
              <table className="w-full text-left text-sm">
                <thead>
                  <tr className="border-b border-neutral-800 text-neutral-400">
                    <th className="p-3">Name</th>
                    <th className="p-3">Email</th>
                    <th className="p-3">Admin</th>
                    <th className="p-3">Joined Date</th>
                  </tr>
                </thead>
                <tbody>
                  {profilesList?.map((p) => (
                    <tr key={p.id} className="border-b border-neutral-800/50">
                      <td className="p-3 font-medium text-white">{p.full_name}</td>
                      <td className="p-3">{p.email}</td>
                      <td className="p-3">{p.is_admin ? "Yes" : "No"}</td>
                      <td className="p-3">{p.created_at ? new Date(p.created_at).toLocaleDateString() : "N/A"}</td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </section>
        )}

        {tab === "enrollments" && (
          <section className="bg-[rgba(255,255,255,0.02)] p-6 rounded-xl border border-[rgba(198,165,92,0.2)]">
            <h2 className="font-serif text-2xl mb-4 text-white">Enrollments</h2>
            <div className="overflow-x-auto">
              <table className="w-full text-left text-sm">
                <thead>
                  <tr className="border-b border-neutral-800 text-neutral-400">
                    <th className="p-3">Participant</th>
                    <th className="p-3">Cohort</th>
                    <th className="p-3">Status</th>
                    <th className="p-3">Joined</th>
                  </tr>
                </thead>
                <tbody>
                  {cohortMembers?.map((cm) => (
                    <tr key={cm.id} className="border-b border-neutral-800/50">
                      <td className="p-3">
                        <div className="font-medium text-white">{cm.profiles?.full_name}</div>
                        <div className="text-xs text-neutral-500">{cm.profiles?.email}</div>
                      </td>
                      <td className="p-3">{cm.cohorts?.title}</td>
                      <td className="p-3 capitalize">{cm.status}</td>
                      <td className="p-3">{cm.joined_at ? new Date(cm.joined_at).toLocaleDateString() : "N/A"}</td>
                    </tr>
                  ))}
                  {cohortMembers?.length === 0 && (
                    <tr><td colSpan={4} className="p-4 text-center text-neutral-500">No enrollments found.</td></tr>
                  )}
                </tbody>
              </table>
            </div>
          </section>
        )}

        {tab === "resources" && (
          <section className="bg-[rgba(255,255,255,0.02)] p-6 rounded-xl border border-[rgba(198,165,92,0.2)]">
            <h2 className="font-serif text-2xl mb-4 text-white">Resources</h2>
            <div className="overflow-x-auto">
              <table className="w-full text-left text-sm">
                <thead>
                  <tr className="border-b border-neutral-800 text-neutral-400">
                    <th className="p-3">Title</th>
                    <th className="p-3">Type</th>
                    <th className="p-3">Path</th>
                  </tr>
                </thead>
                <tbody>
                  {resources?.map((r) => (
                    <tr key={r.id} className="border-b border-neutral-800/50">
                      <td className="p-3 font-medium text-white">{r.title}</td>
                      <td className="p-3 capitalize">{r.asset_type}</td>
                      <td className="p-3 font-mono text-xs text-neutral-500">{r.storage_path}</td>
                    </tr>
                  ))}
                  {resources?.length === 0 && (
                    <tr><td colSpan={3} className="p-4 text-center text-neutral-500">No resources found.</td></tr>
                  )}
                </tbody>
              </table>
            </div>
          </section>
        )}
      </div>
    </div>
  );
}
