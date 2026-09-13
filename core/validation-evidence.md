# Validation and Check Evidence

Validation and verification reports are evidence records, not predictions.
Use the authoritative command for the scope being reported and preserve its
result verbatim enough for a developer to identify what ran.

## Canonical project state

The runtime validator is authoritative for canonical TCAF project state:

```txt
tcaf validate --target <target>
```

Here `<target>` means the bound TCAF Run Envelope Target `locator`. Never
substitute the envelope file path, an input-resource path, another inspected
file, or the current working directory unless that exact path is the bound
target. This binding rule is general and applies regardless of adapter or
host. When validation is `PENDING` or `NOT RUN`, emit the exact command using
that bound target locator.

Report `Validation: PASS` only when that command (or the equivalent invocation
through the current runtime working copy) was executed for the current target
and returned success. If it was not executed, report `Validation: PENDING` or
`Validation: NOT RUN` and include the exact command. If it returned a failure,
report `Validation: FAILED`, include the validator issues, and do not soften it
to partial success. Schema inspection, generated-file presence, self-review,
or an agent's belief that the task is complete cannot establish PASS.

In inspect-only or developer-run workflows, validation normally remains
pending/not run unless the workflow explicitly permits a read-only validation.
Do not perform writes merely to satisfy validation. After approved canonical
writes, run the command when permitted; otherwise report the exact pending
command.

## Task checks

For every required check, record one evidence state:

```txt
PASS       — executed and succeeded
FAILED     — executed and failed; retain the observed error
NOT RUN    — not executed; retain the exact command
PENDING    — awaiting an allowed execution or developer-reported result
```

Aggregate task verification is `passed` only when every required check for the
approved Task Contract is recorded as `PASS`. A failed aggregate command stays
`FAILED` even if lower-level commands run separately and pass. Lower-level
successes are diagnostic evidence, not a replacement for the failed required
check. After approved remediation, rerun the failed check and affected checks.

Do not duplicate the runtime validator or let bundle heuristics override its
result. Schemas and templates may guide generation and inspection only.

## Lifecycle evidence

Keep canonical task status separate from lifecycle evidence. `Status:
Completed` does not imply implementation completion, review approval, executed
verification, or a commit. Record `Review: approved` only after explicit
developer approval, `Verification: passed` only from executed successful
required checks, and `Commit: committed` only from repository evidence.
