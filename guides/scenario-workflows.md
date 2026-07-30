# Scenario Workflows

These are concise reference flows. Each edit still requires a bounded task contract.

## Greenfield

Analysis → naming and rules → project docs/backlog → capability choices → small implementation steps.

## Existing project, no framework

Inspect relevant architecture/capabilities → follow local pattern → approve minimal edit surface → change one step → developer verification.

## Existing feature change

Inspect existing behavior and reusable logic → identify smallest integration point → edit only required files → targeted checks → review.

## Bug fix

Evidence/reproduction → identify cause → minimal fix → targeted check → developer acceptance.

## Legacy/disordered area

Characterize current behavior → preserve local coherence → smallest safe change → explicit risk report.

## Docs/status

Inspect source of truth → update only permitted fields/section → diff review → preserve completed history.

## Framework adoption

Capability baseline → project naming/rules → additive project docs → validate with one small real task. Do not modify application behavior in the same adoption task.
