# Quality scenarios and architecture evaluation

This is a documented scenario-based evaluation following ATAM concepts, not a claim of an
externally facilitated stakeholder workshop. The utility tree groups priorities by PASUM.

| Attribute | Stimulus / environment | Response and measure | Tactic | Evidence |
|---|---|---|---|---|
| Performance | Four clients issue 100 loopback health requests | p95 < 500 ms in the recorded run | Short requests and per-operation connections | reports/load.json |
| Availability | Application stops after commit | Restart preserves question/vote data | Durable transaction and integrity check | persistence and migration tests |
| Security | Unauthenticated actor requests authorship or changes an answer | 403; no author field in public API | Authorization at server, least-data projection | HTTP privacy test and browser XSS test in SQAT |
| Usability | New student opens submission page | Visible name notice, labels, keyboard submission, status message | Explicit disclosure and semantic HTML | UI source and browser workflow; no user-task timing claimed |
| Modifiability | Answer field is added to schema | Existing rows and integrity retained | Versioned migration; isolated Board service | migration regression test |

## Evaluation steps

1. Business driver: enable written questions while preserving teacher moderation.
2. Present architecture: browser, HTTP adapter, Board and transactional database.
3. Identify approaches: projections, idempotency, constraints, bearer authorization and refresh.
4. Build utility tree: prioritize security/availability, then performance, usability and change cost.
5. Analyze scenarios above using executable checks and explicitly identified design review.
6. Record risks, sensitivities and trade-offs below; retain scenarios for future review.

| Item | Type | Consequence | Response |
|---|---|---|---|
| Database lock contention | Sensitivity | Long transactions increase p95 | Keep transactions short; benchmark before scaling |
| Peer anonymity vs teacher accountability | Trade-off | A teacher can still judge authors | Explain the boundary and restrict teacher access |
| Polling vs immediacy | Trade-off | Questions are not pushed live | Refresh UI; consider push after a measured need |
| Self-declared identity | Risk | A user can impersonate another name / voter | Institutional authentication before real classroom use |
| Single host | Risk | Host failure interrupts service | Backups/restart procedure; do not claim multi-host high availability |

The measured latency is a local result, not a production capacity guarantee. Usability and
organizational benefits require a classroom study; the current evidence proves functional behavior.
