-- ============================================================================
-- SUPABASE MIGRATION: MULTI-TRACK (GOLF, HOCKEY, CORPORATE) & EU GDPR COMPLIANCE
-- ============================================================================

-- 1. Ensure sports & programs exist for Hockey and Corporate
DO $$
DECLARE
  v_hockey_sport_id UUID;
  v_corporate_sport_id UUID;
  v_hockey_program_id UUID;
  v_corporate_program_id UUID;
  v_hockey_version_id UUID;
  v_corporate_version_id UUID;
BEGIN
  -- Insert Hockey Sport if not exists
  INSERT INTO sports (slug, name, is_active)
  VALUES ('hockey', 'Hockey', true)
  ON CONFLICT (slug) DO UPDATE SET is_active = true
  RETURNING id INTO v_hockey_sport_id;

  -- Insert Hockey Program
  INSERT INTO programs (sport_id, slug, title, tagline, format)
  VALUES (
    v_hockey_sport_id,
    'lornettes-foundation-hockey',
    'Lornette’s Foundation — Hockey',
    'High-Performance Team Composure & Mental Poise',
    '10-Week Guided Athlete Development Program'
  )
  ON CONFLICT (slug) DO NOTHING
  RETURNING id INTO v_hockey_program_id;

  IF v_hockey_program_id IS NOT NULL THEN
    INSERT INTO program_versions (program_id, version_semver, duration_weeks, is_active)
    VALUES (v_hockey_program_id, '1.0.0', 10, true)
    ON CONFLICT (program_id, version_semver) DO NOTHING;
  END IF;

  -- Insert Corporate Sport / Vertical if not exists
  INSERT INTO sports (slug, name, is_active)
  VALUES ('corporate', 'Corporate & Executive Leadership', true)
  ON CONFLICT (slug) DO UPDATE SET is_active = true
  RETURNING id INTO v_corporate_sport_id;

  -- Insert Corporate Program
  INSERT INTO programs (sport_id, slug, title, tagline, format)
  VALUES (
    v_corporate_sport_id,
    'lornettes-foundation-corporate',
    'Lornette’s Foundation — Corporate',
    'Executive Mental Performance & Team Composure',
    '10-Week Executive & Dealership Leadership Program'
  )
  ON CONFLICT (slug) DO NOTHING
  RETURNING id INTO v_corporate_program_id;

  IF v_corporate_program_id IS NOT NULL THEN
    INSERT INTO program_versions (program_id, version_semver, duration_weeks, is_active)
    VALUES (v_corporate_program_id, '1.0.0', 10, true)
    ON CONFLICT (program_id, version_semver) DO NOTHING;
  END IF;
END $$;

-- 2. Extend Profiles with Track, Region & GDPR Fields
ALTER TABLE profiles 
  ADD COLUMN IF NOT EXISTS active_track TEXT NOT NULL DEFAULT 'golf',
  ADD COLUMN IF NOT EXISTS region_focus TEXT NOT NULL DEFAULT 'north_america',
  ADD COLUMN IF NOT EXISTS gdpr_consent_date TIMESTAMPTZ,
  ADD COLUMN IF NOT EXISTS gdpr_analytics_consent BOOLEAN NOT NULL DEFAULT false,
  ADD COLUMN IF NOT EXISTS gdpr_coaching_recording_consent BOOLEAN NOT NULL DEFAULT false,
  ADD COLUMN IF NOT EXISTS gdpr_data_residency TEXT NOT NULL DEFAULT 'eu-west-1';

-- 3. Create GDPR Compliance & Data Rights Request Table
CREATE TABLE IF NOT EXISTS gdpr_compliance_requests (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  profile_id UUID NOT NULL REFERENCES profiles(id) ON DELETE CASCADE,
  request_type TEXT NOT NULL CHECK (request_type IN ('export', 'erasure', 'rectification', 'consent_update')),
  status TEXT NOT NULL DEFAULT 'completed',
  details JSONB DEFAULT '{}'::jsonb,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- 4. Enable Row Level Security
ALTER TABLE gdpr_compliance_requests ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Athletes can view their own GDPR requests"
  ON gdpr_compliance_requests FOR SELECT
  USING (auth.uid() = profile_id);

CREATE POLICY "Athletes can insert their own GDPR requests"
  ON gdpr_compliance_requests FOR INSERT
  WITH CHECK (auth.uid() = profile_id);

GRANT SELECT, INSERT ON gdpr_compliance_requests TO authenticated;
