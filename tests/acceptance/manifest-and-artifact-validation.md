# Acceptance Test — Manifest and Artifact Validation

## Valid release

`tcaf validate` must pass only when:

- `VERSION`, README, changelog and central registry agree;
- every registered agent has one existing machine manifest;
- operation and agent IDs agree;
- bundle files and every declared module exist inside the installed framework;
- optional selectors are unique and bounded;
- target roles exist in the project schema;
- every registered adapter has an instruction file;
- every adapter declares transport and native-invocation verification state;
- canonical templates contain required headings in canonical order.

Target validation must also:

- accept `external:GitHub Issues` for the Backlog role;
- reject an external mapping for a role that does not allow it;
- reject a default backlog file beside an external Backlog mapping;
- reject empty or duplicate Project Brief open decisions;
- reject duplicate manifest role mappings.

## Mutation checks

On isolated copies, introduce one defect at a time:

- missing module;
- escaping module path;
- duplicate operation alias;
- unknown target role;
- missing adapter instructions;
- version mismatch;
- missing canonical template heading.
- invalid external role mapping;
- parallel external/default backlog sources;
- empty or duplicate open decisions;
- duplicate manifest role mapping.

Each defect must produce a non-zero validation result and identify the failed invariant without loading a fallback or changing procedure.
