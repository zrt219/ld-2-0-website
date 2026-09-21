-- ============================================================================
-- SUPABASE POSTGRES MIGRATION: STORAGE BUCKETS & RLS
-- ============================================================================

-- 1. Create buckets if they don't exist
INSERT INTO storage.buckets (id, name, public) VALUES 
('marketing_public', 'marketing_public', true),
('participant_resources', 'participant_resources', false),
('participant_private', 'participant_private', false),
('internal_assets', 'internal_assets', false)
ON CONFLICT (id) DO NOTHING;

-- 2. Bucket RLS Policies (Storage objects)
-- RLS must be enabled on storage.objects
ALTER TABLE storage.objects ENABLE ROW LEVEL SECURITY;

-- 2a. Marketing Public: Anyone can read
CREATE POLICY "Public read access for marketing" ON storage.objects FOR SELECT 
USING (bucket_id = 'marketing_public');

-- 2b. Participant Resources: Only enrolled members can read their curriculum resources
-- This implies checking if the resource is linked to an activity the user has access to.
CREATE POLICY "Participant read access for resources" ON storage.objects FOR SELECT 
USING (
  bucket_id = 'participant_resources' 
  AND EXISTS (
    SELECT 1 FROM resources r
    JOIN activity_resources ar ON r.id = ar.resource_id
    JOIN curriculum_activities ca ON ar.activity_id = ca.id
    JOIN cohort_members cm ON cm.current_week >= ca.week_number
    WHERE r.storage_path = storage.objects.name
    AND cm.profile_id = auth.uid()
  )
);

-- 2c. Participant Private: Only the participant themselves or Admin/Lornette
CREATE POLICY "Private read access for participant" ON storage.objects FOR SELECT 
USING (
  bucket_id = 'participant_private' 
  AND (
    (auth.uid()::text = (storage.foldername(name))[1]) OR 
    ((SELECT is_admin FROM profiles WHERE id = auth.uid()) = true)
  )
);
CREATE POLICY "Private insert access for participant" ON storage.objects FOR INSERT 
WITH CHECK (
  bucket_id = 'participant_private' 
  AND (
    (auth.uid()::text = (storage.foldername(name))[1]) OR 
    ((SELECT is_admin FROM profiles WHERE id = auth.uid()) = true)
  )
);

-- 2d. Internal Assets: Only Admin/Lornette can read/write
CREATE POLICY "Admin read access for internal" ON storage.objects FOR SELECT 
USING (
  bucket_id = 'internal_assets' 
  AND ((SELECT is_admin FROM profiles WHERE id = auth.uid()) = true)
);
CREATE POLICY "Admin insert access for internal" ON storage.objects FOR INSERT 
WITH CHECK (
  bucket_id = 'internal_assets' 
  AND ((SELECT is_admin FROM profiles WHERE id = auth.uid()) = true)
);
CREATE POLICY "Admin update access for internal" ON storage.objects FOR UPDATE 
USING (
  bucket_id = 'internal_assets' 
  AND ((SELECT is_admin FROM profiles WHERE id = auth.uid()) = true)
);

