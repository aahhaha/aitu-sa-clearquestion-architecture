# ADR 002-privacy: Separate projections

Status: accepted for this demonstration. Date: 14 November 2026.

## Context
The prototype must be reproducible and preserve classroom privacy and storage invariants.

## Decision
Use a public query without author and a restricted query requiring a teacher key.

## Alternatives
Fully anonymous storage removes moderation accountability; sending names and hiding them in CSS leaks them.

## Consequences and risks
The API boundary enforces peer privacy. Teachers still see names, and self-declared identities are not SSO.

## Evidence
See tests/test_board.py and reports/execution.json.
