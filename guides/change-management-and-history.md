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
