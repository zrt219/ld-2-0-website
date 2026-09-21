-- ============================================================================
-- SUPABASE POSTGRES INITIAL MIGRATION: GOLF V1
-- CANONICAL 10-WEEK / 10-FOUNDATION ARCHITECTURE WITH RLS & SEED
-- ============================================================================

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- ----------------------------------------------------------------------------
-- 1. ENUMS
-- ----------------------------------------------------------------------------
CREATE TYPE organization_type AS ENUM ('private_club', 'corporate', 'public');
CREATE TYPE org_role AS ENUM ('admin', 'coach', 'member');
CREATE TYPE cohort_status AS ENUM ('upcoming', 'active', 'completed', 'archived');
CREATE TYPE member_status AS ENUM ('active', 'completed', 'dropped');
CREATE TYPE activity_type AS ENUM (
  'lornette_video',
  'whiteboard_video',
  'worksheet',
  'field_assignment',
  'performance_check',
  'reflection',
  'audio',
  'live_session',
  'plan_activity',
  'resource'
);
CREATE TYPE resource_asset_type AS ENUM ('participant_pdf', 'audio_mp3', 'internal_docx', 'routine_card');
CREATE TYPE assessment_type AS ENUM ('baseline', 'post', 'followup_30_day');
CREATE TYPE registration_type AS ENUM ('individual_paid', 'club_sponsored');

-- ----------------------------------------------------------------------------
-- 2. SPORTS & CANONICAL PROGRAM TAXONOMY
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS sports (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  slug TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  is_active BOOLEAN NOT NULL DEFAULT true,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS programs (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  sport_id UUID NOT NULL REFERENCES sports(id) ON DELETE RESTRICT,
  slug TEXT UNIQUE NOT NULL,
  title TEXT NOT NULL,
  tagline TEXT NOT NULL,
  format TEXT NOT NULL DEFAULT '10-Week Guided Cohort',
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS program_versions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  program_id UUID NOT NULL REFERENCES programs(id) ON DELETE CASCADE,
  version_semver TEXT NOT NULL,
  duration_weeks INTEGER NOT NULL DEFAULT 10 CHECK (duration_weeks = 10),
  is_active BOOLEAN NOT NULL DEFAULT true,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE(program_id, version_semver)
);

CREATE TABLE IF NOT EXISTS program_foundations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  program_id UUID NOT NULL REFERENCES programs(id) ON DELETE CASCADE,
  foundation_number INTEGER NOT NULL CHECK (foundation_number BETWEEN 1 AND 10),
  week_number INTEGER NOT NULL CHECK (week_number BETWEEN 1 AND 10),
  name TEXT NOT NULL,
  subtitle TEXT NOT NULL,
  description TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE(program_id, foundation_number),
  UNIQUE(program_id, week_number)
);

CREATE TABLE IF NOT EXISTS performance_edge_tools (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  slug TEXT UNIQUE NOT NULL,
  name TEXT NOT NULL,
  description TEXT NOT NULL,
  tool_order INTEGER NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS foundation_tool_mappings (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  foundation_id UUID NOT NULL REFERENCES program_foundations(id) ON DELETE CASCADE,
  tool_id UUID NOT NULL REFERENCES performance_edge_tools(id) ON DELETE CASCADE,
  integration_notes TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE(foundation_id, tool_id)
);

-- ----------------------------------------------------------------------------
-- 3. PROFILES, ORGANIZATIONS & COHORTS
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS profiles (
  id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  email TEXT UNIQUE NOT NULL,
  full_name TEXT NOT NULL,
  handicap_index TEXT,
  division TEXT DEFAULT 'Tournament Amateur',
  home_club TEXT,
  pga_coach_alignment TEXT,
  is_admin BOOLEAN NOT NULL DEFAULT false,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS organizations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name TEXT NOT NULL,
  slug TEXT UNIQUE NOT NULL,
  type organization_type NOT NULL DEFAULT 'private_club',
  contact_email TEXT NOT NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS organization_memberships (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  organization_id UUID NOT NULL REFERENCES organizations(id) ON DELETE CASCADE,
  profile_id UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  role org_role NOT NULL DEFAULT 'member',
  created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE(organization_id, profile_id)
);

CREATE TABLE IF NOT EXISTS cohorts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  program_id UUID NOT NULL REFERENCES programs(id) ON DELETE RESTRICT,
  program_version_id UUID NOT NULL REFERENCES program_versions(id) ON DELETE RESTRICT,
  organization_id UUID REFERENCES organizations(id) ON DELETE SET NULL,
  title TEXT NOT NULL,
  cohort_code TEXT UNIQUE NOT NULL,
  start_date DATE NOT NULL,
  status cohort_status NOT NULL DEFAULT 'active',
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS cohort_members (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  cohort_id UUID NOT NULL REFERENCES cohorts(id) ON DELETE CASCADE,
  profile_id UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  status member_status NOT NULL DEFAULT 'active',
  current_week INTEGER NOT NULL DEFAULT 1 CHECK (current_week BETWEEN 1 AND 10),
  joined_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE(cohort_id, profile_id)
);

-- ----------------------------------------------------------------------------
-- 4. CURRICULUM ACTIVITIES & RESOURCES
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS curriculum_activities (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  foundation_id UUID NOT NULL REFERENCES program_foundations(id) ON DELETE CASCADE,
  week_number INTEGER NOT NULL CHECK (week_number BETWEEN 1 AND 10),
  sequence_order INTEGER NOT NULL,
  activity_type activity_type NOT NULL,
  title TEXT NOT NULL,
  description TEXT,
  content_ref TEXT,
  duration_seconds INTEGER,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS resources (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  slug TEXT UNIQUE NOT NULL,
  title TEXT NOT NULL,
  asset_type resource_asset_type NOT NULL,
  storage_path TEXT NOT NULL,
  size_display TEXT,
  is_internal BOOLEAN NOT NULL DEFAULT false,
  foundation_id UUID REFERENCES program_foundations(id) ON DELETE SET NULL,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS activity_resources (
  activity_id UUID NOT NULL REFERENCES curriculum_activities(id) ON DELETE CASCADE,
  resource_id UUID NOT NULL REFERENCES resources(id) ON DELETE CASCADE,
  PRIMARY KEY (activity_id, resource_id)
);

-- ----------------------------------------------------------------------------
-- 5. ASSESSMENTS, REFLECTIONS & PERFORMANCE PLANS
-- ----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS assessments (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  profile_id UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  cohort_id UUID NOT NULL REFERENCES cohorts(id) ON DELETE CASCADE,
  type assessment_type NOT NULL,
  score_data JSONB NOT NULL DEFAULT '{}'::jsonb,
  qualitative_data JSONB NOT NULL DEFAULT '{}'::jsonb,
  submitted_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS performance_checks (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  cohort_id UUID NOT NULL REFERENCES cohorts(id) ON DELETE CASCADE,
  week_number INTEGER NOT NULL CHECK (week_number BETWEEN 1 AND 10),
  profile_id UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  responses JSONB NOT NULL DEFAULT '{}'::jsonb,
  status TEXT NOT NULL DEFAULT 'complete',
  submitted_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS weekly_reflections (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  cohort_id UUID NOT NULL REFERENCES cohorts(id) ON DELETE CASCADE,
  week_number INTEGER NOT NULL CHECK (week_number BETWEEN 1 AND 10),
  profile_id UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  prompt_question TEXT NOT NULL,
  response_text TEXT NOT NULL,
  what_noticed TEXT,
  what_worked TEXT,
  what_repeat TEXT,
  submitted_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS performance_plans (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  profile_id UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  cohort_id UUID NOT NULL REFERENCES cohorts(id) ON DELETE CASCADE,
  pressure_signal TEXT,
  reset_protocol TEXT,
  pre_shot_cadence JSONB DEFAULT '[]'::jsonb,
  anchor_cue TEXT,
  goals_30_day JSONB DEFAULT '[]'::jsonb,
  submitted_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE(profile_id, cohort_id)
);

CREATE TABLE IF NOT EXISTS mentor_reviews (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  plan_id UUID NOT NULL REFERENCES performance_plans(id) ON DELETE CASCADE,
  reviewer_id UUID NOT NULL REFERENCES profiles(id) ON DELETE RESTRICT,
  review_notes TEXT NOT NULL,
  review_media_url TEXT,
  reviewed_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS case_study_permissions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  profile_id UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  assessment_id UUID REFERENCES assessments(id) ON DELETE SET NULL,
  consent_given BOOLEAN NOT NULL DEFAULT false,
  approved_quote TEXT,
  signed_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS registrations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  cohort_id UUID NOT NULL REFERENCES cohorts(id) ON DELETE RESTRICT,
  full_name TEXT NOT NULL,
  email TEXT NOT NULL,
  registration_type registration_type NOT NULL DEFAULT 'individual_paid',
  status TEXT NOT NULL DEFAULT 'pending',
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ----------------------------------------------------------------------------

CREATE TABLE IF NOT EXISTS inquiries (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  profile_id UUID REFERENCES profiles(id) ON DELETE CASCADE,
  subject TEXT,
  message TEXT NOT NULL,
  status TEXT DEFAULT 'pending',
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS resource_entitlements (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  profile_id UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  resource_id UUID NOT NULL REFERENCES resources(id) ON DELETE CASCADE,
  granted_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE(profile_id, resource_id)
);

CREATE TABLE IF NOT EXISTS participant_progress (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  profile_id UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  cohort_id UUID NOT NULL REFERENCES cohorts(id) ON DELETE CASCADE,
  activity_id UUID NOT NULL REFERENCES curriculum_activities(id) ON DELETE CASCADE,
  completed_at TIMESTAMPTZ NOT NULL DEFAULT now(),
  UNIQUE(profile_id, cohort_id, activity_id)
);

-- 6. INDEXES FOR HIGH-TRAFFIC QUERY PATTERNS
-- ----------------------------------------------------------------------------
CREATE INDEX idx_cohort_members_profile ON cohort_members(profile_id);
CREATE INDEX idx_cohort_members_cohort ON cohort_members(cohort_id);
CREATE INDEX idx_weekly_reflections_profile_week ON weekly_reflections(profile_id, week_number);
CREATE INDEX idx_performance_plans_profile ON performance_plans(profile_id);
CREATE INDEX idx_curriculum_foundation_week ON curriculum_activities(foundation_id, week_number);
CREATE INDEX idx_resources_foundation ON resources(foundation_id);

-- ----------------------------------------------------------------------------
-- 7. ROW LEVEL SECURITY (RLS) POLICIES
-- ----------------------------------------------------------------------------
ALTER TABLE sports ENABLE ROW LEVEL SECURITY;
ALTER TABLE programs ENABLE ROW LEVEL SECURITY;
ALTER TABLE program_versions ENABLE ROW LEVEL SECURITY;
ALTER TABLE program_foundations ENABLE ROW LEVEL SECURITY;
ALTER TABLE performance_edge_tools ENABLE ROW LEVEL SECURITY;
ALTER TABLE foundation_tool_mappings ENABLE ROW LEVEL SECURITY;
ALTER TABLE profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE organizations ENABLE ROW LEVEL SECURITY;
ALTER TABLE organization_memberships ENABLE ROW LEVEL SECURITY;
ALTER TABLE cohorts ENABLE ROW LEVEL SECURITY;
ALTER TABLE cohort_members ENABLE ROW LEVEL SECURITY;
ALTER TABLE curriculum_activities ENABLE ROW LEVEL SECURITY;
ALTER TABLE resources ENABLE ROW LEVEL SECURITY;
ALTER TABLE activity_resources ENABLE ROW LEVEL SECURITY;
ALTER TABLE assessments ENABLE ROW LEVEL SECURITY;
ALTER TABLE performance_checks ENABLE ROW LEVEL SECURITY;
ALTER TABLE weekly_reflections ENABLE ROW LEVEL SECURITY;
ALTER TABLE performance_plans ENABLE ROW LEVEL SECURITY;
ALTER TABLE mentor_reviews ENABLE ROW LEVEL SECURITY;
ALTER TABLE case_study_permissions ENABLE ROW LEVEL SECURITY;
ALTER TABLE registrations ENABLE ROW LEVEL SECURITY;

-- Public taxonomy read access
CREATE POLICY "Public can view active sports" ON sports FOR SELECT USING (is_active = true);
CREATE POLICY "Public can view programs" ON programs FOR SELECT USING (true);
CREATE POLICY "Public can view active versions" ON program_versions FOR SELECT USING (is_active = true);
CREATE POLICY "Public can view foundations" ON program_foundations FOR SELECT USING (true);
CREATE POLICY "Public can view tools" ON performance_edge_tools FOR SELECT USING (true);
CREATE POLICY "Public can view tool mappings" ON foundation_tool_mappings FOR SELECT USING (true);
CREATE POLICY "Public can view non-internal resources" ON resources FOR SELECT USING (is_internal = false);

-- Profiles: users read and edit only their own
CREATE POLICY "Users view own profile" ON profiles FOR SELECT USING (auth.uid() = id);
CREATE POLICY "Users update own profile" ON profiles FOR UPDATE USING (auth.uid() = id);

-- Cohorts: members can view their enrolled cohort
CREATE POLICY "Members view their cohorts" ON cohorts FOR SELECT
  USING (EXISTS (SELECT 1 FROM cohort_members WHERE cohort_members.cohort_id = cohorts.id AND cohort_members.profile_id = auth.uid()));

-- Activities: members of active cohorts can view curriculum activities
CREATE POLICY "Enrolled athletes view activities" ON curriculum_activities FOR SELECT
  USING (EXISTS (
    SELECT 1 FROM cohort_members cm
    JOIN cohorts c ON cm.cohort_id = c.id
    WHERE cm.profile_id = auth.uid()
  ));

-- Athlete submissions: users can read/insert/update only their own reflections, plans & assessments
CREATE POLICY "Athletes view own reflections" ON weekly_reflections FOR SELECT USING (auth.uid() = profile_id);
CREATE POLICY "Athletes insert own reflections" ON weekly_reflections FOR INSERT WITH CHECK (auth.uid() = profile_id);
CREATE POLICY "Athletes update own reflections" ON weekly_reflections FOR UPDATE USING (auth.uid() = profile_id);

CREATE POLICY "Athletes view own plans" ON performance_plans FOR SELECT USING (auth.uid() = profile_id);
CREATE POLICY "Athletes insert own plans" ON performance_plans FOR INSERT WITH CHECK (auth.uid() = profile_id);
CREATE POLICY "Athletes update own plans" ON performance_plans FOR UPDATE USING (auth.uid() = profile_id);

CREATE POLICY "Athletes view own assessments" ON assessments FOR SELECT USING (auth.uid() = profile_id);
CREATE POLICY "Athletes insert own assessments" ON assessments FOR INSERT WITH CHECK (auth.uid() = profile_id);

CREATE POLICY "Athletes view own reviews" ON mentor_reviews FOR SELECT
  USING (EXISTS (SELECT 1 FROM performance_plans p WHERE p.id = mentor_reviews.plan_id AND p.profile_id = auth.uid()));

-- Admin bypass: Lornette / platform admin has full oversight
CREATE OR REPLACE FUNCTION is_admin_user() RETURNS BOOLEAN AS $$
  SELECT is_admin FROM public.profiles WHERE id = auth.uid();
$$ LANGUAGE sql SECURITY DEFINER;

CREATE POLICY "Admin full access profiles" ON profiles FOR ALL USING (is_admin_user() = true);
CREATE POLICY "Admin full access reflections" ON weekly_reflections FOR ALL USING (is_admin_user() = true);
CREATE POLICY "Admin full access plans" ON performance_plans FOR ALL USING (is_admin_user() = true);
CREATE POLICY "Admin full access reviews" ON mentor_reviews FOR ALL USING (is_admin_user() = true);

-- ----------------------------------------------------------------------------

ALTER TABLE inquiries ENABLE ROW LEVEL SECURITY;
ALTER TABLE resource_entitlements ENABLE ROW LEVEL SECURITY;
ALTER TABLE participant_progress ENABLE ROW LEVEL SECURITY;

-- Additional policies
CREATE POLICY "Users view own inquiries" ON inquiries FOR SELECT USING (auth.uid() = profile_id);
CREATE POLICY "Users insert own inquiries" ON inquiries FOR INSERT WITH CHECK (auth.uid() = profile_id);

CREATE POLICY "Users view own resource entitlements" ON resource_entitlements FOR SELECT USING (auth.uid() = profile_id);

CREATE POLICY "Users view own progress" ON participant_progress FOR SELECT USING (auth.uid() = profile_id);
CREATE POLICY "Users insert own progress" ON participant_progress FOR INSERT WITH CHECK (auth.uid() = profile_id);

-- Club Admin Policies
CREATE POLICY "Club Admin view organization" ON organizations FOR SELECT USING (
  EXISTS (SELECT 1 FROM organization_memberships WHERE organization_memberships.organization_id = organizations.id AND organization_memberships.profile_id = auth.uid() AND organization_memberships.role = 'admin')
);

CREATE POLICY "Club Admin view organization memberships" ON organization_memberships FOR SELECT USING (
  EXISTS (SELECT 1 FROM organization_memberships om WHERE om.organization_id = organization_memberships.organization_id AND om.profile_id = auth.uid() AND om.role = 'admin')
);

CREATE POLICY "Club Admin view cohorts" ON cohorts FOR SELECT USING (
  EXISTS (SELECT 1 FROM organization_memberships WHERE organization_memberships.organization_id = cohorts.organization_id AND organization_memberships.profile_id = auth.uid() AND organization_memberships.role = 'admin')
);

CREATE POLICY "Club Admin view cohort members" ON cohort_members FOR SELECT USING (
  EXISTS (
    SELECT 1 FROM cohorts c 
    JOIN organization_memberships om ON c.organization_id = om.organization_id
    WHERE c.id = cohort_members.cohort_id AND om.profile_id = auth.uid() AND om.role = 'admin'
  )
);

CREATE POLICY "Users view own cohort membership" ON cohort_members FOR SELECT USING (
  profile_id = auth.uid()
);

-- Registrations policies
CREATE POLICY "Users view own registrations" ON registrations FOR SELECT USING (email = (SELECT email FROM profiles WHERE id = auth.uid()));
CREATE POLICY "Users insert own registrations" ON registrations FOR INSERT WITH CHECK (email = (SELECT email FROM profiles WHERE id = auth.uid()));

-- Case study permissions
CREATE POLICY "Users view own case study permissions" ON case_study_permissions FOR SELECT USING (auth.uid() = profile_id);
CREATE POLICY "Users insert own case study permissions" ON case_study_permissions FOR INSERT WITH CHECK (auth.uid() = profile_id);

-- Performance checks
CREATE POLICY "Users view own performance checks" ON performance_checks FOR SELECT USING (auth.uid() = profile_id);
CREATE POLICY "Users insert own performance checks" ON performance_checks FOR INSERT WITH CHECK (auth.uid() = profile_id);

-- Activity resources
CREATE POLICY "Users view activity resources" ON activity_resources FOR SELECT USING (
  EXISTS (
    SELECT 1 FROM curriculum_activities ca
    JOIN cohort_members cm ON cm.current_week >= ca.week_number
    WHERE ca.id = activity_resources.activity_id AND cm.profile_id = auth.uid()
  )
);

-- 8. CANONICAL SEED DATA (GOLF V1 ONLY - NO OTHER SPORTS)
-- ----------------------------------------------------------------------------
DO $$
DECLARE
  v_sport_id UUID;
  v_program_id UUID;
  v_version_id UUID;
  v_f1 UUID; v_f2 UUID; v_f3 UUID; v_f4 UUID; v_f5 UUID;
  v_f6 UUID; v_f7 UUID; v_f8 UUID; v_f9 UUID; v_f10 UUID;
  v_t_focus UUID; v_t_routine UUID; v_t_pressure UUID; v_t_vis UUID;
  v_t_reset UUID; v_t_decide UUID; v_t_prep UUID; v_t_conf UUID;
BEGIN
  -- 1. Sport
  INSERT INTO sports (slug, name, is_active)
  VALUES ('golf', 'Golf', true)
  RETURNING id INTO v_sport_id;

  -- 2. Program
  INSERT INTO programs (sport_id, slug, title, tagline, format)
  VALUES (
    v_sport_id,
    'lornettes-foundation-golf',
    'Lornette’s Foundation — Golf',
    'Play Your Best When It Matters.',
    '10-Week Guided Athlete Development Program'
  )
  RETURNING id INTO v_program_id;

  -- 3. Version
  INSERT INTO program_versions (program_id, version_semver, duration_weeks, is_active)
  VALUES (v_program_id, '1.0.0', 10, true)
  RETURNING id INTO v_version_id;

  -- 4. 10 Canonical Foundations
  INSERT INTO program_foundations (program_id, foundation_number, week_number, name, subtitle, description)
  VALUES
    (v_program_id, 1, 1, 'Identity Beyond Sport', 'Ground your worth beyond the score', 'Build resilience and emotional steadiness by detaching personal worth from scoreboard fluctuations.'),
    (v_program_id, 2, 2, 'Champion Mindset', 'Train attention and internal clarity', 'Develop elite focus, confidence, and sensory visualization for tournament preparation.'),
    (v_program_id, 3, 3, 'Discipline Systems', 'Consistency through repeatable routines', 'Codify your 6-step pre-shot routine and deliberate tournament preparation habits.'),
    (v_program_id, 4, 4, 'Resilience After Setback', 'The Next Shot Principle', 'Master Lornette’s 5-second physical reset to instantly clear bogeys and unhook from frustration.'),
    (v_program_id, 5, 5, 'Pressure, Emotional Regulation & Recovery', 'Composure under fire', 'Regulate autonomic nervous arousal, heart rate spikes, and high-stakes tournament tension.'),
    (v_program_id, 6, 6, 'Communication & Presence', 'Internal dialogue & coach alignment', 'Command executive presence on the fairways and align clear expectations with swing coaches.'),
    (v_program_id, 7, 7, 'Family & Community Support', 'Surround yourself for longevity', 'Establish healthy emotional boundaries and cultivate an inner circle that sustains your career.'),
    (v_program_id, 8, 8, 'Career & Money Readiness', 'Athletic longevity & financial stability', 'Develop long-term financial wisdom, sponsorship literacy, and post-competition readiness.'),
    (v_program_id, 9, 9, 'Personal Brand & Story', 'Reputation and authentic leadership', 'Articulate your core values and lead by example across golf clubs and civic communities.'),
    (v_program_id, 10, 10, 'Legacy & Community Impact', 'Mentoring the next generation', 'Channel competitive achievements into enduring community impact and youth mentorship.')
  RETURNING id INTO v_f10;

  -- 5. 8 Performance Edge Tools
  INSERT INTO performance_edge_tools (slug, name, description, tool_order) VALUES
    ('focus', 'Focus', 'Selective attention and distraction elimination', 1) RETURNING id INTO v_t_focus;
  INSERT INTO performance_edge_tools (slug, name, description, tool_order) VALUES
    ('pre-shot-routine', 'Pre-Shot Routine', '6-step repeatable physical and sensory cadence', 2) RETURNING id INTO v_t_routine;
  INSERT INTO performance_edge_tools (slug, name, description, tool_order) VALUES
    ('pressure-response', 'Pressure Response', 'Physiological sigh and down-regulation', 3) RETURNING id INTO v_t_pressure;
  INSERT INTO performance_edge_tools (slug, name, description, tool_order) VALUES
    ('visualization', 'Visualization', 'Sensory mental rehearsal of ball flight apex', 4) RETURNING id INTO v_t_vis;
  INSERT INTO performance_edge_tools (slug, name, description, tool_order) VALUES
    ('mistake-reset', 'Mistake Reset', '5-second physical unhooking protocol', 5) RETURNING id INTO v_t_reset;
  INSERT INTO performance_edge_tools (slug, name, description, tool_order) VALUES
    ('decision-making', 'Decision-Making', 'Course management and conservative target lines', 6) RETURNING id INTO v_t_decide;
  INSERT INTO performance_edge_tools (slug, name, description, tool_order) VALUES
    ('competition-prep', 'Competition Preparation', '36-hour pre-tournament mental checklist', 7) RETURNING id INTO v_t_prep;
  INSERT INTO performance_edge_tools (slug, name, description, tool_order) VALUES
    ('confidence', 'Confidence', 'Evidence-based audit of preparation and composure', 8) RETURNING id INTO v_t_conf;

  -- 6. Demo Cohort
  INSERT INTO cohorts (program_id, program_version_id, title, cohort_code, start_date, status)
  VALUES (
    v_program_id,
    v_version_id,
    'Fall 2026 Championship Cohort',
    'GOLF-FALL-2026',
    CURRENT_DATE,
    'active'
  );
END $$;


-- ----------------------------------------------------------------------------
-- 9. EXPLICIT GRANTS
-- ----------------------------------------------------------------------------
GRANT SELECT ON sports TO authenticated, anon;
GRANT SELECT ON programs TO authenticated, anon;
GRANT SELECT ON program_versions TO authenticated, anon;
GRANT SELECT ON program_foundations TO authenticated, anon;
GRANT SELECT ON performance_edge_tools TO authenticated, anon;
GRANT SELECT ON foundation_tool_mappings TO authenticated, anon;

GRANT SELECT, INSERT, UPDATE ON profiles TO authenticated;
GRANT SELECT ON organizations TO authenticated;
GRANT SELECT ON organization_memberships TO authenticated;
GRANT SELECT ON cohorts TO authenticated;
GRANT SELECT ON cohort_members TO authenticated;
GRANT SELECT ON curriculum_activities TO authenticated;
GRANT SELECT ON resources TO authenticated;
GRANT SELECT ON activity_resources TO authenticated;

GRANT SELECT, INSERT, UPDATE ON assessments TO authenticated;
GRANT SELECT, INSERT ON performance_checks TO authenticated;
GRANT SELECT, INSERT, UPDATE ON weekly_reflections TO authenticated;
GRANT SELECT, INSERT, UPDATE ON performance_plans TO authenticated;
GRANT SELECT ON mentor_reviews TO authenticated;
GRANT SELECT, INSERT ON case_study_permissions TO authenticated;
GRANT SELECT, INSERT ON registrations TO authenticated;

GRANT SELECT, INSERT ON inquiries TO authenticated;
GRANT SELECT ON resource_entitlements TO authenticated;
GRANT SELECT, INSERT ON participant_progress TO authenticated;

GRANT USAGE ON SCHEMA public TO authenticated, anon;

-- Club Admin view participant progress
CREATE POLICY "Club Admin view participant progress" ON participant_progress FOR SELECT USING (
  EXISTS (
    SELECT 1 FROM cohorts c
    JOIN organization_memberships om ON c.organization_id = om.organization_id
    WHERE c.id = participant_progress.cohort_id AND om.profile_id = auth.uid() AND om.role = 'admin'
  )
);

