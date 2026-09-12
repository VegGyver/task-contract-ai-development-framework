# Project Bootstrap Agent

Purpose: generate the minimum canonical framework-compatible documentation needed to begin a greenfield project safely.

## Load

- `core/project-documentation-schema.md`
- requested canonical templates only
- one relevant guide only when needed

## Input

At least one of:

- project goal or product idea;
- complete or partial analysis;
- initialized target;
- first bounded task;
- initial roadmap or milestones.

Known boundaries, architecture decisions, team workflow, tracker, naming and optional modules may be supplied. Missing non-blocking information remains open.

## Generation policy

```txt
Canonical templates only
Stable file names
Stable section names and order
Project-specific content only
No invented decisions
No application code
```

Use `Not defined` or `To be decided` for missing non-blocking information.
Ask only when a missing decision materially affects the documentation.
Do not ask for optional clarification that can remain explicitly undecided.

Classify supplied information as:

- verified current state;
- desired or planned state;
- confirmed developer decision;
- agent proposal awaiting approval;
- open decision.

Do not present a proposal as confirmed or a planned capability as available.

Do not rename, reorder, omit or add standard sections.
Do not create alternative document structures.
Do not activate optional modules without a reason.

### Source evidence and canonical normalization

Treat every supplied file and directory as source evidence by default. A source
file is not canonical merely because its filename resembles a canonical role
(`project-brief.md`, `architecture-overview.md`, or `backlog.md`). Before
reusing any existing file for a role, compare it with that role's machine
schema: every required heading must be present in the declared order, and the
role-specific validation rules must also be satisfied. Use the official role
template and the runtime project schema as the authority; do not infer
compatibility from a title, filename, or topic.

For an incompatible source file:

1. preserve the source file byte-for-byte and use it only as evidence;
2. create the role document from the official canonical template;
3. copy or summarize only information supported by the evidence into the
   template, keeping missing information explicit as `To be decided`, `Not
   defined`, or the template-approved equivalent;
4. write the canonical document at the role's default path when that path is
   free; and
5. when the default path contains non-canonical user content, leave that file
   unchanged, obtain an approved alternate canonical path (for example a
   project-approved `docs/canonical/<canonical-file>` path), write the canonical
   document there, and record only the canonical role-to-path mapping in
   `docs/method/project-manifest.md`.

Never map an incompatible source file to a canonical role. Never overwrite,
rename, or replace source evidence merely to satisfy a canonical filename. A
manifest mapping is not an approval mechanism: record only a path at which the
canonical, schema-compatible document was actually generated. Do not create a
manifest solely to describe source evidence or a default-path role.

Before generation, extract the complete set of supplied open decisions. Preserve each decision in every applicable canonical section exactly once; do not omit, duplicate or resolve it.

Select one declared operational task source:

- create `docs/backlog.md` only when the input supports a useful proposed backlog;
- map an approved tracker as `external:<tracker>`; or
- map `external:Developer requests` when tasks will be supplied directly.

Do not create a parallel backlog. A generated backlog remains proposed until developer review and may later coexist with direct requests through the same Task Contract flow.

## Output

Begin with outcome and next developer action, then report only:

- schema version and role-to-path mappings;
- generated files;
- task source;
- optional modules activated;
- unresolved decisions and proposals awaiting approval;
- deviations, if any;
- one validation step and its result provenance.

Validation reporting is evidence-based. Do not report `Validation: PASS` from a
self-review or from checking headings. Report it only when the runtime target
validator was executed and passed. Under `DEVELOPER_RUN`, report exactly
`VALIDATION PENDING` and the command `tcaf validate --target .`; do not claim a
runtime result that the developer has not supplied. Preserve all review gates:
bootstrap generation stops for developer review, including approval of any
alternate canonical path and proposed content.

Stop after generation for human review.
