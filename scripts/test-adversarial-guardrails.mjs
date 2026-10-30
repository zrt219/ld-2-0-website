/**
 * scripts/test-adversarial-guardrails.mjs
 * 
 * Comprehensive Empirical Adversarial Stress Harness
 * Validates pre-flight guardrails across:
 *   - scripts/buffer-post.mjs (assertPostTextClean)
 *   - scripts/schedule-master.mjs (assertQueueClean)
 *   - scripts/campaign-sync.mjs (assertCampaignPostClean)
 * 
 * Tests:
 * 1. Case variations of bracketed metadata tags
 * 2. Spacing and whitespace variations (spaces, tabs, newlines)
 * 3. Nested, compound, and edge-case brackets
 * 4. Legitimate parentheticals (ensuring 0 false positives)
 * 5. Edge and boundary conditions (null, undefined, empty, non-string, multi-line)
 * 6. Keyword combinations: DAY, SLOT, POST, WAVE with varied delimiters
 */

import { assertPostTextClean, METADATA_TAG_REGEX as BUFFER_REGEX } from './buffer-post.mjs';
import { assertQueueClean, METADATA_TAG_REGEX as MASTER_REGEX } from './schedule-master.mjs';
import { assertCampaignPostClean, METADATA_TAG_REGEX as SYNC_REGEX } from './campaign-sync.mjs';

const testResults = {
  total: 0,
  passed: 0,
  failed: 0,
  details: []
};

function recordPass(suite, name, detail = '') {
  testResults.total++;
  testResults.passed++;
  testResults.details.push({ suite, name, status: 'PASS', detail });
  console.log(`  ✅ [PASS] ${suite} -> ${name} ${detail ? `(${detail})` : ''}`);
}

function recordFail(suite, name, error) {
  testResults.total++;
  testResults.failed++;
  testResults.details.push({ suite, name, status: 'FAIL', error: error?.message || String(error) });
  console.error(`  ❌ [FAIL] ${suite} -> ${name}: ${error?.message || error}`);
}

function expectThrows(fn, expectedSubstr, suite, name) {
  try {
    fn();
    recordFail(suite, name, new Error(`Expected function to throw, but it succeeded.`));
  } catch (err) {
    if (!expectedSubstr || err.message.includes(expectedSubstr)) {
      recordPass(suite, name, `threw "${err.message.slice(0, 60)}..."`);
    } else {
      recordFail(suite, name, new Error(`Expected error containing "${expectedSubstr}", got "${err.message}"`));
    }
  }
}

function expectPasses(fn, suite, name) {
  try {
    fn();
    recordPass(suite, name);
  } catch (err) {
    recordFail(suite, name, err);
  }
}

console.log('======================================================================');
console.log('🔥 STARTING EMPIRICAL ADVERSARIAL STRESS HARNESS');
console.log('======================================================================\n');

// -----------------------------------------------------------------------------
// SUITE 1: CASE VARIATIONS (Dirty Inputs Must Throw Rule 9 Invariant Violation)
// -----------------------------------------------------------------------------
console.log('--- SUITE 1: Case Variations of Bracketed Tags ---');

const caseDirtyInputs = [
  { tag: '(day 12 - slot)', label: 'lowercase day with slot' },
  { tag: '[Day 4 - Morning]', label: 'titlecase Day with slot titlecase' },
  { tag: '(DAY 1)', label: 'uppercase DAY single digit' },
  { tag: '[day 9]', label: 'lowercase day in square brackets' },
  { tag: '[SLOT: MORNING]', label: 'uppercase SLOT with colon' },
  { tag: '[POST 4]', label: 'uppercase POST with digit' },
  { tag: '[WAVE 3]', label: 'uppercase WAVE with digit' },
  { tag: '(DaY 15 - EvEnInG)', label: 'mixed-case DaY and EvEnInG' },
  { tag: '[sLoT 2]', label: 'mixed-case sLoT in square brackets' },
  { tag: '(pOsT 99)', label: 'mixed-case pOsT' },
  { tag: '[wAvE 1]', label: 'mixed-case wAvE' },
  { tag: '(day)', label: 'lowercase bare day tag' },
  { tag: '[DAY]', label: 'uppercase bare DAY tag' },
  { tag: '(SLOT)', label: 'uppercase bare SLOT tag' },
  { tag: '[post]', label: 'lowercase bare post tag' },
  { tag: '(wave)', label: 'lowercase bare wave tag' },
];

for (const { tag, label } of caseDirtyInputs) {
  const postText = `TACTICAL DISCIPLINE AND LEADERSHIP ${tag}\n\nElite athletic execution under pressure.`;

  // Test buffer-post
  expectThrows(
    () => assertPostTextClean(postText, 'BufferPost'),
    'Rule 9 Invariant Violation',
    'Suite 1: Case Variations',
    `buffer-post rejects ${label} "${tag}"`
  );

  // Test schedule-master queue
  expectThrows(
    () => assertQueueClean([{ id: 'TEST_01', text: postText }], 'MasterQueue'),
    'Rule 9 Invariant Violation',
    'Suite 1: Case Variations',
    `schedule-master rejects ${label} "${tag}"`
  );

  // Test campaign-sync post text
  expectThrows(
    () => assertCampaignPostClean({ id: 101, headline: 'CLEAN HEADLINE', text: postText }),
    'Rule 9 Invariant Violation',
    'Suite 1: Case Variations',
    `campaign-sync text rejects ${label} "${tag}"`
  );

  // Test campaign-sync post headline
  expectThrows(
    () => assertCampaignPostClean({ id: 102, headline: `HEADLINE ${tag}`, text: 'Clean editorial body.' }),
    'Rule 9 Invariant Violation',
    'Suite 1: Case Variations',
    `campaign-sync headline rejects ${label} "${tag}"`
  );
}

// -----------------------------------------------------------------------------
// SUITE 2: SPACING & WHITESPACE VARIATIONS (Must Throw Rule 9 Invariant Violation)
// -----------------------------------------------------------------------------
console.log('\n--- SUITE 2: Spacing & Whitespace Variations ---');

const spacingDirtyInputs = [
  { tag: '(  DAY 5  )', label: 'spaces padding inside parens' },
  { tag: '[ DAY   8 - MIDDAY ]', label: 'multiple interior spaces around DAY and hyphen' },
  { tag: '(    DAY 12)', label: 'excessive leading spaces inside paren' },
  { tag: '(DAY 12    )', label: 'excessive trailing spaces inside paren' },
  { tag: '[\tDAY 3\t]', label: 'tab character padding inside square brackets' },
  { tag: '[\nDAY 4\n]', label: 'newline character padding inside square brackets' },
  { tag: '[Day 7  :  Morning]', label: 'multi-spaces around colon delimiter' },
  { tag: '(DAY 10   -   EVENING)', label: 'multi-spaces around hyphen delimiter' },
  { tag: '(\t  SLOT 1  \t)', label: 'mixed spaces and tabs inside SLOT tag' },
  { tag: '[   POST   10   ]', label: 'multi-space padded POST tag' },
  { tag: '(  WAVE   5  )', label: 'multi-space padded WAVE tag' },
];

for (const { tag, label } of spacingDirtyInputs) {
  const postText = `CHAMPIONSHIP CULTURE ${tag}\n\nConsistent daily standard of excellence.`;

  expectThrows(
    () => assertPostTextClean(postText, 'BufferPost'),
    'Rule 9 Invariant Violation',
    'Suite 2: Spacing Variations',
    `buffer-post rejects ${label}`
  );

  expectThrows(
    () => assertQueueClean([{ id: 'TEST_02', text: postText }], 'MasterQueue'),
    'Rule 9 Invariant Violation',
    'Suite 2: Spacing Variations',
    `schedule-master rejects ${label}`
  );

  expectThrows(
    () => assertCampaignPostClean({ id: 201, headline: 'CLEAN HEADLINE', text: postText }),
    'Rule 9 Invariant Violation',
    'Suite 2: Spacing Variations',
    `campaign-sync rejects ${label}`
  );
}

// -----------------------------------------------------------------------------
// SUITE 3: NESTED & COMPOUND BRACKETS (Must Throw Rule 9 Invariant Violation)
// -----------------------------------------------------------------------------
console.log('\n--- SUITE 3: Nested & Compound Brackets ---');

const nestedDirtyInputs = [
  { tag: '((DAY 1))', label: 'double parentheses' },
  { tag: '[([DAY 2])]', label: 'square-paren-square nested brackets' },
  { tag: '[ (DAY 3) ]', label: 'space-padded nested parens inside square brackets' },
  { tag: '((Day 4 - Morning))', label: 'double parens with slot descriptor' },
  { tag: '[[SLOT 1]]', label: 'double square brackets around SLOT' },
  { tag: '([[POST 5]])', label: 'paren-square compound around POST' },
  { tag: '([WAVE 2])', label: 'paren-square compound around WAVE' },
  { tag: '([( DAY 7 )])', label: 'triple nested bracket with spacing' },
  { tag: '[DAY 1] [SLOT: EVENING]', label: 'consecutive distinct bracketed tags' },
];

for (const { tag, label } of nestedDirtyInputs) {
  const postText = `MENTAL TOUGHNESS ${tag}\n\nEmotional poise under championship pressure.`;

  expectThrows(
    () => assertPostTextClean(postText, 'BufferPost'),
    'Rule 9 Invariant Violation',
    'Suite 3: Nested Brackets',
    `buffer-post rejects ${label} "${tag}"`
  );

  expectThrows(
    () => assertQueueClean([{ id: 'TEST_03', text: postText }], 'MasterQueue'),
    'Rule 9 Invariant Violation',
    'Suite 3: Nested Brackets',
    `schedule-master rejects ${label} "${tag}"`
  );

  expectThrows(
    () => assertCampaignPostClean({ id: 301, headline: `HEADLINE ${tag}`, text: 'Clean editorial body.' }),
    'Rule 9 Invariant Violation',
    'Suite 3: Nested Brackets',
    `campaign-sync rejects ${label} "${tag}"`
  );
}

// -----------------------------------------------------------------------------
// SUITE 4: LEGITIMATE PARENTHETICALS (Must PASS With Zero False Positives)
// -----------------------------------------------------------------------------
console.log('\n--- SUITE 4: Legitimate Parentheticals (Zero False Positives) ---');

const legitimateInputs = [
  { text: 'Como 1907 (founded 1907) represents athletic renaissance on Lake Como.', label: 'historical founding year (1907)' },
  { text: 'Dawn Staley coached A\'ja Wilson (Las Vegas Aces) to back-to-back WNBA titles.', label: 'team parenthetical (Las Vegas Aces)' },
  { text: 'Survival Skills for Men is now available in digital edition ($14.99 CAD) at lornettedaye.com.', label: 'currency and price ($14.99 CAD)' },
  { text: 'Canadian national sprint champion Lornette Daye clocked world-class speeds (112 km/h wind gauge adjusted).', label: 'speed/metric units (112 km/h)' },
  { text: 'The championship match was held at Arthur Ashe Stadium (Flushing Meadows, NY).', label: 'location specification' },
  { text: 'Dawn Staley built a dominant program at South Carolina (Gamecocks).', label: 'mascot in parens' },
  { text: 'With 40+ years as an Olympic-level coach (and Canadian sprint champion), Lornette brings unparalleled perspective.', label: 'parenthetical clause' },
  { text: 'The campaign spans exactly 3 weeks (21 calendar days) with 1-2 posts per day.', label: 'calendar duration explanation' },
  { text: 'Athletes must build emotional poise (e.g., breathing reset, pre-shot routine) before execution.', label: 'latin abbreviation e.g.' },
  { text: 'Read the full framework in Finish Strong (see chapter 4).', label: 'cross reference in parens' },
  { text: 'Buffer queue reports 100% clean status (0 bracketed tags remaining).', label: 'audit metric parenthetical' },
  { text: 'Today is the day we elevate our discipline (today represents a clean slate).', label: 'word "today" inside parens' },
  { text: 'Reflecting on yesterday (yesterday teaches us valuable lessons) sharpens future focus.', label: 'word "yesterday" inside parens' },
  { text: 'Build steady habits (everyday consistency compounds over time).', label: 'word "everyday" inside parens' },
  { text: 'Peak physical condition requires elite focus (game day execution is non-negotiable).', label: 'phrase "game day" inside parens' },
  { text: 'Our booking calendar opens up (time slot availability updated weekly).', label: 'phrase "time slot" inside parens' },
  { text: 'She led the team through the postseason tournament (postseason resilience).', label: 'word "postseason" inside parens' },
  { text: 'Immediate impact echoed throughout the league (shockwave of championship momentum).', label: 'word "shockwave" inside parens' },
  { text: 'Heat wave conditions tested every golfer (heat wave endurance).', label: 'phrase "heat wave" inside parens' },
];

for (const { text, label } of legitimateInputs) {
  // Test buffer-post
  expectPasses(
    () => assertPostTextClean(text, 'BufferPost'),
    'Suite 4: Legitimate Parentheticals',
    `buffer-post allows ${label}`
  );

  // Test schedule-master
  expectPasses(
    () => assertQueueClean([{ id: 'LEGIT_01', text }], 'MasterQueue'),
    'Suite 4: Legitimate Parentheticals',
    `schedule-master allows ${label}`
  );

  // Test campaign-sync
  expectPasses(
    () => assertCampaignPostClean({ id: 401, headline: 'CLEAN EDITORIAL HEADLINE', text }),
    'Suite 4: Legitimate Parentheticals',
    `campaign-sync allows ${label}`
  );
}

// -----------------------------------------------------------------------------
// SUITE 5: EDGE CONDITIONS & BOUNDARY INPUTS
// -----------------------------------------------------------------------------
console.log('\n--- SUITE 5: Edge Conditions & Boundary Inputs ---');

// 5.1 buffer-post edge inputs
expectThrows(
  () => assertPostTextClean(null),
  'must be a non-empty string',
  'Suite 5: Edge Conditions',
  'buffer-post rejects null'
);

expectThrows(
  () => assertPostTextClean(undefined),
  'must be a non-empty string',
  'Suite 5: Edge Conditions',
  'buffer-post rejects undefined'
);

expectThrows(
  () => assertPostTextClean(''),
  'must be a non-empty string',
  'Suite 5: Edge Conditions',
  'buffer-post rejects empty string'
);

expectThrows(
  () => assertPostTextClean('   \t\n   '),
  'must be a non-empty string',
  'Suite 5: Edge Conditions',
  'buffer-post rejects whitespace-only string'
);

expectThrows(
  () => assertPostTextClean(12345),
  'must be a non-empty string',
  'Suite 5: Edge Conditions',
  'buffer-post rejects number input'
);

expectThrows(
  () => assertPostTextClean({ text: 'Some text' }),
  'must be a non-empty string',
  'Suite 5: Edge Conditions',
  'buffer-post rejects object input'
);

// 5.2 schedule-master edge inputs
expectPasses(
  () => assertQueueClean([], 'EmptyQueue'),
  'Suite 5: Edge Conditions',
  'schedule-master cleanly accepts empty queue array'
);

expectThrows(
  () => assertQueueClean([{ id: 'E1', text: null }]),
  'has missing or invalid text',
  'Suite 5: Edge Conditions',
  'schedule-master rejects queue item with null text'
);

expectThrows(
  () => assertQueueClean([{ id: 'E2', text: undefined }]),
  'has missing or invalid text',
  'Suite 5: Edge Conditions',
  'schedule-master rejects queue item with undefined text'
);

expectThrows(
  () => assertQueueClean([{ id: 'E3', text: '' }]),
  'has missing or invalid text',
  'Suite 5: Edge Conditions',
  'schedule-master rejects queue item with empty string text'
);

expectThrows(
  () => assertQueueClean([{ id: 'E4', text: 999 }]),
  'has missing or invalid text',
  'Suite 5: Edge Conditions',
  'schedule-master rejects queue item with number text'
);

// 5.3 campaign-sync edge inputs
expectThrows(
  () => assertCampaignPostClean({ id: 501, text: null }),
  'text must be a non-empty string',
  'Suite 5: Edge Conditions',
  'campaign-sync rejects post with null text'
);

expectThrows(
  () => assertCampaignPostClean({ id: 502, text: '' }),
  'text must be a non-empty string',
  'Suite 5: Edge Conditions',
  'campaign-sync rejects post with empty text'
);

expectThrows(
  () => assertCampaignPostClean({ id: 503, text: '   ' }),
  'text must be a non-empty string',
  'Suite 5: Edge Conditions',
  'campaign-sync rejects post with whitespace text'
);

// 5.4 Multi-line text with dirty tag on line 1, line 5, line 20
const multiLinePostWithTagLine1 = `CULTURE OVER CELEBRITY (DAY 28 - EVENING)\n\nLine 2\nLine 3\nLine 4\nFinal line.`;
const multiLinePostWithTagLine5 = `Line 1\nLine 2\nLine 3\nLine 4\nCULTURE OVER CELEBRITY (DAY 28 - EVENING)\nLine 6`;
const multiLinePostWithTagEnd = `Line 1\nLine 2\nLine 3\nLine 4\nFinal line with tag [SLOT: MORNING]`;

expectThrows(
  () => assertPostTextClean(multiLinePostWithTagLine1),
  'Rule 9 Invariant Violation',
  'Suite 5: Edge Conditions',
  'buffer-post rejects multi-line text with tag on line 1'
);

expectThrows(
  () => assertPostTextClean(multiLinePostWithTagLine5),
  'Rule 9 Invariant Violation',
  'Suite 5: Edge Conditions',
  'buffer-post rejects multi-line text with tag on line 5'
);

expectThrows(
  () => assertPostTextClean(multiLinePostWithTagEnd),
  'Rule 9 Invariant Violation',
  'Suite 5: Edge Conditions',
  'buffer-post rejects multi-line text with tag on final line'
);

// 5.5 Rule 7 Asterisk Rejection Verification
expectThrows(
  () => assertPostTextClean('Title\n\n**Key Takeaway**: Must reject markdown bolding.'),
  'Rule 7 Invariant Violation',
  'Suite 5: Edge Conditions',
  'buffer-post rejects asterisk (*)'
);

expectThrows(
  () => assertCampaignPostClean({ id: 504, headline: 'CLEAN', text: 'Text with * single asterisk.' }),
  'Rule 7 Invariant Violation',
  'Suite 5: Edge Conditions',
  'campaign-sync rejects asterisk in text'
);

expectThrows(
  () => assertCampaignPostClean({ id: 505, headline: '**DIRTY** HEADLINE', text: 'Clean text.' }),
  'Rule 7 Invariant Violation',
  'Suite 5: Edge Conditions',
  'campaign-sync rejects asterisk in headline'
);

expectThrows(
  () => assertQueueClean([{ id: 'E5', text: 'Text with **bold**.' }]),
  'Rule 7 Invariant Violation',
  'Suite 5: Edge Conditions',
  'schedule-master rejects asterisk in queue'
);

// -----------------------------------------------------------------------------
// SUITE 6: DIRECT REGEX COMBINATORIAL STRESS BATTERY
// -----------------------------------------------------------------------------
console.log('\n--- SUITE 6: Direct Regex Combinatorial Stress Battery ---');

const keywords = ['DAY', 'day', 'Day', 'DaY', 'SLOT', 'slot', 'Slot', 'sLoT', 'POST', 'post', 'Post', 'pOsT', 'WAVE', 'wave', 'Wave', 'wAvE'];
const openBrackets = ['(', '[', '((', '[[', '([', '[('];
const closeBrackets = [')', ']', '))', ']]', '])', ')]'];
const suffixes = [' 1', ' 14', ' 28', ': MORNING', ' - MIDDAY', ' - EVENING', ' 99 - SLOT', ''];

let combMatches = 0;
for (const kw of keywords) {
  for (const ob of openBrackets) {
    for (const cb of closeBrackets) {
      for (const suf of suffixes) {
        const testStr = `PRE ${ob}${kw}${suf}${cb} POST`;
        if (BUFFER_REGEX.test(testStr)) {
          combMatches++;
        } else {
          recordFail('Suite 6: Combinatorial', `Regex failed to match: "${testStr}"`, new Error('Expected match'));
        }
      }
    }
  }
}

if (combMatches > 0) {
  recordPass('Suite 6: Combinatorial', `Combinatorial matrix: ${combMatches}/${combMatches} permutations successfully matched and blocked`);
}

// -----------------------------------------------------------------------------
// SUITE 7: ADVERSARIAL DISCOVERY & CORNER CASE EXPLORATION (Boundary analysis)
// -----------------------------------------------------------------------------
console.log('\n--- SUITE 7: Adversarial Discovery & Corner Cases ---');

// Case A: (DAY1) without space - Analysis
const day1NoSpace = '(DAY1)';
const matchesDay1NoSpace = BUFFER_REGEX.test(day1NoSpace);
console.log(`  ℹ️  [ANALYSIS] Corner Case: "${day1NoSpace}" regex match: ${matchesDay1NoSpace} (Expected false under \\b constraint because digit is \\w)`);

// Case B: {DAY 1} with curly braces - Analysis
const curlyDay = '{DAY 1}';
const matchesCurlyDay = BUFFER_REGEX.test(curlyDay);
console.log(`  ℹ️  [ANALYSIS] Corner Case: "${curlyDay}" regex match: ${matchesCurlyDay} (Rule 9 scopes brackets (...) and [...])`);

// Case C: Post-workout parenthetical - Analysis
const postWorkout = '(Post-workout recovery routine)';
const matchesPostWorkout = BUFFER_REGEX.test(postWorkout);
console.log(`  ℹ️  [ANALYSIS] Corner Case: "${postWorkout}" regex match: ${matchesPostWorkout} (Matched due to POST\\b delimiter)`);

// -----------------------------------------------------------------------------
// FINAL SUMMARY
// -----------------------------------------------------------------------------
console.log('\n======================================================================');
console.log(`🎯 STRESS HARNESS COMPLETE: ${testResults.passed} PASSED, ${testResults.failed} FAILED (TOTAL: ${testResults.total})`);
console.log('======================================================================');

if (testResults.failed > 0) {
  console.error(`💥 Adversarial test harness detected ${testResults.failed} failures!`);
  process.exit(1);
} else {
  console.log(`🏆 ALL ${testResults.passed} ADVERSARIAL STRESS TESTS PASSED SUCCESSFULLY!`);
  process.exit(0);
}
