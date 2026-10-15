# History update — validation report

## Results

- **54 structural, access and teacher-workflow checks passed.**
- **324 automated activity-completion flows passed.** These consist of Full history activity modes, Trial history activity modes (with sensitive-mode fallbacks), and the ordinary quiz flow for all 72 retained secondary world-context packs. This is not a claim to have re-run every original Primary game or every old Secondary tool.
- No browser page errors were recorded in these tests.

## Preservation and access

Both Primary input HTML files were byte-compared with the previous owner package and are unchanged. All 72 original Full Secondary packs and all 36 original Trial Secondary packs were deep-compared and retained exactly. Both access codes match the prior private code JSON. They are absent in plaintext and normalised form from the new public HTML.

The builder performed actual cryptographic round trips for both encrypted payloads. The UI tests checked rejection of a Primary code in the Secondary form, rejection of an invalid well-formed code, and successful decryption with the original Secondary code. Secondary activation leaves Primary in Trial. Stored-code restoration logic was checked using a simulated reload.

## History and teacher workflows

The checks cover the two history tracks at every Secondary level, 24 Full lessons with 144 questions, eight Trial lessons with 24 questions, reference-ID resolution, track/level/search filters, timeline reordering/checks/hints, teacher source rubric, empty-response validation, ungraded reflections, source-activity queueing, copied-lesson metadata, printing provenance, and mobile horizontal layout.

The test responses and rubric scores were entered programmatically. A passing UI test does not prove a learner understands history or independently validate every historical interpretation. Historical content was developed with the sources linked in the lessons; teacher review remains appropriate.

## Test environment and limits

Managed Chromium in this environment blocks file/HTTP navigation. Browser interaction used **about:blank/srcdoc with an explicit test-only in-memory localStorage adapter**. Cryptographic calls were forwarded to **Node Web Crypto** through the existing test adapter. The actual AES-GCM/PBKDF2 operations ran, but **native browser-origin cryptography and persistence across browser restarts on a hosted site were not verified here**.

No adapter, sample learner responses, remembered codes, or test storage is included in the public website. Physical webcam hand tracking, device voices and iOS/Safari behaviour were not tested. The website has not been deployed to GitHub from this conversation.

## Checks passed

1. All 72 old Full secondary packs preserved exactly
2. All 36 old Trial secondary packs preserved exactly
3. History Full has 24 packs and 144 questions
4. History Trial has 8 packs and 24 questions
5. full history-ph S1 coverage
6. full history-ph S2 coverage
7. full history-ph S3 coverage
8. full history-ph S4 coverage
9. full history-world S1 coverage
10. full history-world S2 coverage
11. full history-world S3 coverage
12. full history-world S4 coverage
13. trial history-ph S1 coverage
14. trial history-ph S2 coverage
15. trial history-ph S3 coverage
16. trial history-ph S4 coverage
17. trial history-world S1 coverage
18. trial history-world S2 coverage
19. trial history-world S3 coverage
20. trial history-world S4 coverage
21. Every history source ID resolves in both editions
22. Primary Complete input byte-identical
23. Primary Teacher-Trial input byte-identical
24. Both original access codes retained
25. primary plaintext code absent in public HTML
26. secondary plaintext code absent in public HTML
27. Starts Trial for both levels
28. Trial loads 44 packs
29. Trial history hub visible
30. Track filter 4 sample lessons
31. Level filter 1 sample lesson
32. History search handles no matches
33. Primary code rejected in Secondary form
34. Wrong well-formed Secondary code does not unlock
35. Existing Secondary code decrypts new history package
36. Full loads 96 packs
37. Unlocking Secondary leaves Primary Trial
38. Sensitive history cannot start competitive teams
39. Wrong first response stays recorded as incorrect
40. Wrong timeline does not finish
41. Timeline hint recorded
42. Empty source responses cannot be saved
43. Ungraded source reflection not given automatic marks
44. Edited history copy retains source and timeline
45. Printed history is not labelled fictional
46. Source Detective queues with correct mode
47. Queued source activity starts
48. Secondary code record saved in harness
49. Stored code revalidates on simulated reload
50. Stored code opens history Full on simulated reload
51. Mobile history hub has no horizontal overflow
52. Mobile timeline has no horizontal overflow
53. Mobile source activity has no horizontal overflow
54. No browser page errors in executed flows
