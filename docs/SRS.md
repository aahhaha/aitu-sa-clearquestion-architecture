# Software requirements specification

## Purpose and boundary

ClearQuestion is a classroom question board. Students can ask in writing while their names are
hidden from classmates; an authorized teacher can inspect authorship, answer or hide questions.
The application serves one demonstration room R1. Names are self-declared in this prototype;
institutional identity verification and internet deployment are separate integration concerns.
Student input is rendered as text, never inserted as HTML.

## Stakeholders

| Stakeholder | Need | Concern | Decision |
|---|---|---|---|
| Student asking a question | Clarification without public attribution | Peer judgment, privacy | Separate public and teacher projections |
| Other students | Useful shared questions | Spam and interruption | Deduplicated votes and moderation |
| Lecturer | Manage the queue and give explanations | Time and abuse | Teacher queue, answer/hide/reopen |
| University administrator | Accountability and maintainability | Data retention and integration | Explicit scope, audit records, SSO integration boundary |
| Maintainer | Predictable evolution | Data loss and regressions | SQLite transactions, versioned migration, CI |

Exploratory research from the earlier student team question-board project motivates these
needs. It suggests several barriers to asking; it does not establish that the software improves learning.

## Functional requirements

| ID | Requirement | Acceptance condition |
|---|---|---|
| FR-01 | Submit to an existing room | Valid author, 1-500 character question and 8-64 character request ID produce HTTP 201 |
| FR-02 | Protect public authorship | Public JSON and public UI exclude author fields |
| FR-03 | Teacher access | Moderation listing and mutations reject missing/incorrect bearer keys with 403 |
| FR-04 | Retry safely | Same key and same content return the same ID; different content returns 409 |
| FR-05 | Vote | One vote per provided voter ID and question, including concurrent requests |
| FR-06 | Moderate | Hidden items disappear publicly and cannot be voted or answered; reopening clears an old answer |
| FR-07 | Answer | A valid teacher answer changes open to answered and appears in the public queue |
| FR-08 | Persist and migrate | Version 1 question data survives conversion to version 2 |
| FR-09 | Limit abuse | More than ten new submissions per self-declared author/room/minute return 429 |
| FR-10 | Recover data | Reopening the SQLite file preserves questions and votes |

## Non-functional requirements and constraints

- NFR-P: p95 health latency below 500 ms for 100 loopback requests with four clients; measure the actual environment.
- NFR-A: committed data survives application restart; 503 responses conceal database internals on storage errors.
- NFR-S: parameterized SQL, constant-time teacher-key comparison, no-store responses, public identity separation.
- NFR-U: labelled fields, explicit identity notice, keyboard-operable submission and an announced status message.
- NFR-M: domain/storage behavior can be tested without a browser; schema changes have a regression test.

## API and data model

GET /health; GET /api/questions?room=R1; GET /api/moderation?room=R1.
POST /api/questions, /api/votes, /api/answer, /api/moderate.
See app.py and tests for complete request examples. Teacher operations require Authorization: Bearer <key>.

Rooms have questions; questions have votes. UNIQUE(room, author, request_id) enforces retry identity.
PRIMARY KEY(question_id, voter) prevents repeated votes from the same supplied identity.
Questions transition between open, answered and hidden. Audit records contain role/action/ID/time,
without copying the question text or author. Classroom deployments must replace self-declared
identities with authenticated identities and apply an institutional retention policy.
