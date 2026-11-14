# ADR 003-delivery: Modular monolith and refresh

Status: accepted for this demonstration. Date: 14 November 2026.

## Context
The prototype must be reproducible and preserve classroom privacy and storage invariants.

## Decision
Serve a small same-origin HTTP API and static UI, with a Board service for transactions.

## Alternatives
Microservices and an event broker add deployment and consistency costs; WebSockets add connection management.

## Consequences and risks
A single component is easy to run and test. Explicit refresh has a latency trade-off. Review after measured classroom usage.

## Evidence
See tests/test_board.py and reports/execution.json.
