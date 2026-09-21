-- ============================================================================
-- SUPABASE MIGRATION: DYNAMIC COHORT CAPACITY & OPERATIONAL CLUB ROSTER
-- ============================================================================

-- 1. Add capacity column to cohorts if not exists (default 20, nullable for unlimited)
ALTER TABLE cohorts ADD COLUMN IF NOT EXISTS capacity INTEGER DEFAULT 20 CHECK (capacity IS NULL OR capacity > 0);

-- Ensure existing cohorts have an explicit capacity set
UPDATE cohorts SET capacity = 20 WHERE capacity IS NULL;

-- 2. Allow Club Admin to view registrations for cohorts belonging to their organization
DROP POLICY IF EXISTS "Club Admin view cohort registrations" ON registrations;
CREATE POLICY "Club Admin view cohort registrations" ON registrations FOR SELECT USING (
  EXISTS (
    SELECT 1 FROM cohorts c
    JOIN organization_memberships om ON c.organization_id = om.organization_id
    WHERE c.id = registrations.cohort_id AND om.profile_id = auth.uid() AND om.role = 'admin'
  )
);

-- Allow Club Admin to view member profiles (name, email) for operational cohort administration
DROP POLICY IF EXISTS "Club Admin view cohort member profiles" ON profiles;
CREATE POLICY "Club Admin view cohort member profiles" ON profiles FOR SELECT USING (
  EXISTS (
    SELECT 1 FROM cohort_members cm
    JOIN cohorts c ON cm.cohort_id = c.id
    JOIN organization_memberships om ON c.organization_id = om.organization_id
    WHERE cm.profile_id = profiles.id AND om.profile_id = auth.uid() AND om.role = 'admin'
  )
);

-- 3. Atomic, race-condition-safe registration function enforcing capacity
CREATE OR REPLACE FUNCTION register_cohort_athlete(
  p_cohort_id UUID,
  p_full_name TEXT,
  p_email TEXT,
  p_registration_type registration_type DEFAULT 'club_sponsored'
) RETURNS JSONB AS $$
DECLARE
  v_cohort RECORD;
  v_current_count INTEGER;
  v_new_reg_id UUID;
BEGIN
  -- Lock the cohort record to prevent simultaneous over-subscription
  SELECT id, capacity, status INTO v_cohort
  FROM cohorts
  WHERE id = p_cohort_id
  FOR UPDATE;

  IF NOT FOUND THEN
    RETURN jsonb_build_object('success', false, 'error', 'Cohort not found');
  END IF;

  IF v_cohort.status NOT IN ('active', 'upcoming') THEN
    RETURN jsonb_build_object('success', false, 'error', 'This cohort is closed or no longer accepting registrations');
  END IF;

  -- Count enrolled cohort members
  SELECT count(*) INTO v_current_count
  FROM cohort_members
  WHERE cohort_id = p_cohort_id;

  -- Verify capacity limit
  IF v_cohort.capacity IS NOT NULL AND v_current_count >= v_cohort.capacity THEN
    RETURN jsonb_build_object(
      'success', false,
      'error', 'Cohort capacity has been reached',
      'capacity', v_cohort.capacity,
      'enrolled', v_current_count
    );
  END IF;

  -- Insert pending registration record
  INSERT INTO registrations (
    cohort_id,
    full_name,
    email,
    registration_type,
    status
  ) VALUES (
    p_cohort_id,
    p_full_name,
    p_email,
    p_registration_type,
    'pending'
  ) RETURNING id INTO v_new_reg_id;

  RETURN jsonb_build_object(
    'success', true,
    'registration_id', v_new_reg_id,
    'capacity', v_cohort.capacity,
    'enrolled', v_current_count + 1
  );
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- 4. Operational roster function: returns operational identity only.
-- Strictly excludes reflection text, performance plan notes, and assessment answers.
CREATE OR REPLACE FUNCTION get_club_operational_roster(p_cohort_id UUID)
RETURNS TABLE (
  member_id UUID,
  profile_id UUID,
  full_name TEXT,
  email TEXT,
  status TEXT,
  current_week INTEGER,
  joined_at TIMESTAMPTZ,
  completed_foundations_count BIGINT
) AS $$
BEGIN
  -- Authorization check: caller must be admin of the organization that owns this cohort, or platform admin
  IF NOT EXISTS (
    SELECT 1 FROM cohorts c
    JOIN organization_memberships om ON c.organization_id = om.organization_id
    WHERE c.id = p_cohort_id AND om.profile_id = auth.uid() AND om.role = 'admin'
  ) AND NOT is_admin_user() THEN
    RAISE EXCEPTION 'Unauthorized to view this cohort roster';
  END IF;

  RETURN QUERY
  SELECT
    cm.id AS member_id,
    p.id AS profile_id,
    p.full_name,
    p.email,
    cm.status::TEXT,
    cm.current_week,
    cm.joined_at,
    (
      SELECT count(DISTINCT ca.week_number)
      FROM participant_progress pp
      JOIN curriculum_activities ca ON pp.activity_id = ca.id
      WHERE pp.profile_id = p.id AND pp.cohort_id = p_cohort_id
    ) AS completed_foundations_count
  FROM cohort_members cm
  JOIN profiles p ON cm.profile_id = p.id
  WHERE cm.cohort_id = p_cohort_id
  ORDER BY cm.joined_at ASC;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;
