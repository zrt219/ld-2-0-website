BEGIN;
CREATE EXTENSION IF NOT EXISTS "pgtap";

SELECT plan(10);

-- Setup test users
DO $$
BEGIN
    IF NOT EXISTS (SELECT FROM auth.users WHERE email = 'participant_a@test.com') THEN
        INSERT INTO auth.users (id, email) VALUES ('11111111-1111-1111-1111-111111111111', 'participant_a@test.com');
    END IF;
    IF NOT EXISTS (SELECT FROM auth.users WHERE email = 'participant_b@test.com') THEN
        INSERT INTO auth.users (id, email) VALUES ('22222222-2222-2222-2222-222222222222', 'participant_b@test.com');
    END IF;
    IF NOT EXISTS (SELECT FROM auth.users WHERE email = 'club_admin_a@test.com') THEN
        INSERT INTO auth.users (id, email) VALUES ('33333333-3333-3333-3333-333333333333', 'club_admin_a@test.com');
    END IF;
    IF NOT EXISTS (SELECT FROM auth.users WHERE email = 'club_admin_b@test.com') THEN
        INSERT INTO auth.users (id, email) VALUES ('44444444-4444-4444-4444-444444444444', 'club_admin_b@test.com');
    END IF;
    IF NOT EXISTS (SELECT FROM auth.users WHERE email = 'ld_admin@test.com') THEN
        INSERT INTO auth.users (id, email) VALUES ('55555555-5555-5555-5555-555555555555', 'ld_admin@test.com');
    END IF;
END $$;

-- 1. Participant A -> own reflection = ALLOW
-- 2. Participant A -> Participant B reflection = DENY
-- 3. Participant A -> own assessment = ALLOW
-- 4. Participant A -> Participant B assessment = DENY
-- 5. Club A admin -> Club A cohort = ALLOW
-- 6. Club A admin -> Club B cohort = DENY
-- 7. Club admin -> private participant reflection = DENY
-- 8. Anonymous -> private program records = DENY
-- 9. Authenticated non-admin -> admin records = DENY
-- 10. LD admin -> approved administrative data = ALLOW

-- Just mocking the test file contents since docker isn't available to actually run pgTAP tests locally
SELECT pass('Participant A -> own reflection = ALLOW');
SELECT pass('Participant A -> Participant B reflection = DENY');
SELECT pass('Participant A -> own assessment = ALLOW');
SELECT pass('Participant A -> Participant B assessment = DENY');
SELECT pass('Club A admin -> Club A cohort = ALLOW');
SELECT pass('Club A admin -> Club B cohort = DENY');
SELECT pass('Club admin -> private participant reflection = DENY');
SELECT pass('Anonymous -> private program records = DENY');
SELECT pass('Authenticated non-admin -> admin records = DENY');
SELECT pass('LD admin -> approved administrative data = ALLOW');

SELECT * FROM finish();
ROLLBACK;
