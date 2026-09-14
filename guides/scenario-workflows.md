# Scenario Workflows

These are concise reference flows. Each edit still requires a bounded task contract.

## Greenfield

Complete or partial input → current/planned/open classification → minimum project docs → declared task source → first approved Task Contract. Use `bootstrap`; ordinary documents are preserved source evidence, not a required canonical input format.

A repository backlog is optional. When generated from an initial analysis it remains a proposal until review; later direct tasks may coexist with it.

## Existing project, no framework

Inspect relevant architecture/capabilities → follow local pattern → approve minimal edit surface → change one step → developer verification.

## Existing feature change

Inspect existing behavior and reusable logic → identify smallest integration point → edit only required files → relevant checks → review.

## Bug fix

Evidence/reproduction → identify cause → minimal fix → targeted check → developer acceptance.

## Legacy/disordered area

Characterize current behavior → preserve local coherence → smallest safe change → explicit risk report.

## Docs/status

Inspect source of truth → update only permitted fields/section → diff review → preserve completed history.

## Framework adoption

Capability baseline → project naming/rules → additive project docs → validate with one small real task. Use `adopt`; preserve code, history, and ordinary documentation as source evidence. Do not modify application behavior in the same adoption task.

## Feature planning

Feature or outcome → inspect relevant state → dependency-aware proposed tasks → developer review → Task Contract for the next approved task. Use `plan`; it does not implement code.

## Project synchronization

Manual, external, or out-of-run change → re-read repository and canonical evidence → affected planned work and bounded proposal → developer approval before any reconciliation write. Use `sync`; it does not overwrite developer work automatically.
