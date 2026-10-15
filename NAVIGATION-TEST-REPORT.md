# Secondary subject-first navigation — release checks

## Result

**130 structural, navigation and integration checks passed.**  
**971 activity-completion flows passed** (191 Trial; 780 Full).

The navigation matrix exercised **all 88 subject/year combinations**: 11 subjects × 4 years × 2 editions. Every topic view was checked against its subject/year and grouped topic count.

## What was checked

- Subject-only starting screens; separate History tracks; no mixed lesson wall before subject/year selection.
- Subject-group filtering and subject search; topic search and empty states restricted to the chosen subject/year.
- All retained topics reachable. Paired world contexts grouped without changing original pack records; custom copies remain separate.
- Activity selection, permitted mode categories, launch, completion and return. Existing sensitive-history activity restrictions retained.
- Lesson overview, milestone guide and source tabs; keyboard tab controls.
- Lesson-queue mode selection; custom History copy preserves timeline and source metadata; customised HTML retains the new UI and excludes result records by default.
- Existing model controls render; model selection and breadcrumbs match the tool subject; return from a model retains the original topic.
- Same-document Back/Forward state restoration in the test fixture; explicit Back keeps subject, year and search.
- Mobile navigation drawer, Escape, focus return, and sticky Start controls.
- No horizontal overflow in subject, topic and activity views at 320, 390 and 768 CSS pixels in both editions.
- Existing Primary and Secondary codes unchanged. The Primary code and an incorrect Secondary code are rejected in the Secondary form. The existing Secondary code decrypts the updated package.
- Remembered-code restoration with simulated browser storage; switching back to Trial does not erase Full access.
- Primary opens from the same combined platform.

## Content integrity

Primary Complete and Trial inputs are **byte-identical** to the supplied History owner kit.

Secondary Complete and Trial **world-data JSON blocks are unchanged**, including subjects, questions, places, references, histories and tool-reference metadata:

| Edition | Subjects | Lesson packs | Question records |
|---|---:|---:|---:|
| Full | 11 | 96 | 576 |
| Trial | 11 | 44 | 132 |

Paired location variants share their learning questions; these counts do not claim unique independent question sets. The new browser groups Full into 60 topic cards across all subject/year combinations, but never displays that complete topic collection together.

The gateway app script, gateway styles and gateway template are unchanged. Encryption is rebuilt with the original codes; workspace storage keys and the app identifier are preserved. Public-output scans found neither plaintext access codes nor the test-only adapter.

## Environment and limits

The test environment uses headless managed Chromium. Direct localhost navigation was attempted and blocked by the environment (ERR_BLOCKED_BY_ADMINISTRATOR).

The browser fixtures therefore use **an explicit in-memory localStorage adapter**. Browser decryption calls are forwarded to actual **Node Web Crypto** using the existing private test bridge. These tests cover runtime UI behaviour, API parameters, decryption, state restoration logic and content preservation—not native browser-origin persistence or native-browser cryptographic execution.

**Test adapters are not included in the public HTML.** The site has not been published to GitHub here. Check activation and remembered access on the live HTTPS site in the intended browser. Physical webcam tracking, device voices, iOS/Safari-specific behaviour, and browser persistence across real restarts were not tested.

This is a navigation/interface release. It does not independently revalidate historical interpretations or scientific/mathematical teaching content; the supplied data is deliberately preserved.

## Reproducible records

The private Owner Kit includes navigation-tests/results.json, the two 44-row navigation matrices, extra-ui-results.json and browser test scripts. Older tests are retained as historical build references, not as evidence that they were rerun for this release.
