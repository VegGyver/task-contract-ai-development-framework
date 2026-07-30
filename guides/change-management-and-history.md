# Change Management and History

Completed work is historical evidence; project status is operational data.

## Immutable completed content

Do not retroactively rewrite a completed task's original:

- title
- description
- scope
- acceptance criteria
- original dependencies
- implementation notes

## Operational status

A task status may be corrected by a separate approved `DOCS_STATUS_UPDATE` task after implementation evidence is verified.

For a status-only task:

- modify only explicitly approved status fields or lines
- do not rewrite historical content
- do not add a parallel status document by default
- do not mark a parent task done when only a sub-step is complete

Later functional work becomes a linked extension, fix, refactor or change request.

## Active task changes

Classify new information before editing:

- **Clarification:** understanding becomes more precise without changing contract fields; record it and continue.
- **Correction:** current implementation does not satisfy the approved contract; correct it within the same task.
- **Local adaptation:** an unplanned but necessary change remains inside the allowed surface and behavior; report it.
- **Extension:** behavior, acceptance criteria, surface, dependency, interface, risk or exclusion changes; stop and request approval for a Task Contract amendment.
- **Independent request:** not required for the current goal; preserve it as a separate task or pending note.
- **Blocker:** repository evidence invalidates the contract; report the evidence and wait.

An amendment identifies only changed and unchanged contract fields, work already completed, and checks to add or repeat. Do not rewrite unaffected content. If the primary goal changes, replace the contract or create a new task.

## Developer or concurrent changes

The current repository state is authoritative. Before resuming after a pause or reported manual edit:

- re-read relevant current files;
- distinguish compatible, overlapping and unrelated changes where possible;
- preserve unrelated changes;
- keep compatible work and complete only what remains;
- ask when an overlapping change contradicts the contract or cannot be interpreted safely;
- never discard, reset, delete or restore uncertain work automatically.

Git status and diff do not prove authorship. Report only changes whose origin is known, and describe uncertain changes without attributing them.

## Naming convention

The framework does not impose a universal ID format.

- use the existing team or tracker convention
- define one during greenfield analysis when absent
- do not rename historical IDs
- use linked suffixes or child tasks consistently for later work

## Principle

```txt
Plans evolve.
History is preserved.
Status may be verified and updated.
Changes are appended.
```
