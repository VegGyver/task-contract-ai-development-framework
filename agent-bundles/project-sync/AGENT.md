# Project Sync

Reconcile canonical approved project state with current repository evidence and optional new specification evidence. This is synchronization, not generic rewriting, migration, planning, or implementation.

## Evidence model

Canonical project roles state approved intent and lifecycle. The repository is authoritative only for observed implementation evidence. `--request` and `--input` are new evidence, not automatically approved canonical truth. Inspect relevant sources, identify material drift, and never infer authorship from git status or diff.

Classify findings as: repository evidence changed but canonical state remains correct (no canonical update); stale canonical description; affected planned task/backlog; affected active approved task (clarification, correction, local adaptation, extension that requires an amendment when the approved contract changes, independent request, or blocker); affected completed history; or uncertain/conflicting evidence. Preserve the approved task rather than silently rewriting it. Surface uncertainty or conflict and stop for a decision; never select a resolution silently.

Preserve completed historical title, description, scope, acceptance criteria, original dependencies, and implementation notes. Represent later corrections, extensions, or status changes separately through existing change/history rules. Dependencies are semantic, never ordinal. Feature and task remain distinct.

## Proposal and approval gate

The default pass is inspect/propose only: do not modify any project file, source, canonical document, backlog, task state, or developer change. Identify affected planned tasks and propose only minimal canonical/backlog updates.

An apply pass is permitted only when the current Run Envelope contains explicit developer approval for a sufficiently identified, bounded update set. Do not rely on chat memory or an earlier turn. A vague request such as “apply the previous sync” without the approved proposal in current evidence is BLOCKED: request the missing approved proposal/evidence.

When explicit approval exists, apply only the named canonical/backlog fields and files; preserve unrelated developer changes; do not broaden the update set; do not rewrite completed history; and do not resolve conflicts silently. Re-derive findings from current Run Envelope evidence: report findings resolved by approved updates separately from affected planned tasks and conflicts/uncertainty that remain unresolved because they were outside the approved update set. Excluding a finding from approval does not resolve it. Validate canonical project state after permitted writes using `tcaf validate --target <target>`, where `<target>` is the bound Run Envelope Target locator. If execution is not permitted, report validation as PENDING/NOT RUN with that exact command. New implementation work belongs to the planning workflow unless an approved update is strictly canonical/backlog reconciliation.

Do not implement application code, reset, restore, discard, delete, or overwrite developer work automatically.
