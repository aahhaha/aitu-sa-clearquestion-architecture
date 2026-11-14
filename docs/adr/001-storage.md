# ADR 001-storage: SQLite transactions

Status: accepted for this demonstration. Date: 14 November 2026.

## Context
The prototype must be reproducible and preserve classroom privacy and storage invariants.

## Decision
Use SQLite with uniqueness constraints and short BEGIN IMMEDIATE writes.

## Alternatives
An in-memory list loses data and cannot enforce uniqueness across workers; PostgreSQL adds administration.

## Consequences and risks
Persistence and atomic constraints support FR-04/05/08. A single writer limits throughput. Database backup and file permissions are operational responsibilities.

## Evidence
See tests/test_board.py and reports/execution.json.
