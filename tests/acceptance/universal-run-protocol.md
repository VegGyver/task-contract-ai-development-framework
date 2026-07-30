# Acceptance Test — Universal Run Protocol

## Scenarios

Run the installed release against:

1. a planned greenfield directory with project-analysis input;
2. an existing local project;
3. a bounded daily task in an adopted project;
4. one direct future-agent invocation fixture;
5. a compatible host-resource target.

## Required behavior

- all scenarios use the same installed runner and one-target protocol;
- the operation resolves through the central registry;
- the agent loads only its exact machine manifest;
- target roles resolve from approved project mappings, then canonical paths;
- the host or environment selects one registered adapter;
- the envelope declares adapter transport and whether native invocation is verified;
- framework modules and target evidence are labelled separately;
- no project receives framework runtime files;
- no scenario requires multi-root, aliases, temporary bundles or reconstructed prompts;
- missing modules, invalid selectors, target overlap and registry mismatches fail before execution;
- every output stops at the declared developer review gate.

For Cline, run the registered `manual-envelope` transport: copy the generated envelope unchanged, append one declared step marker, allow at most one write confirmation, and start a new task after developer review. A `Pending` UI state must not trigger a repeated write.

## Failure rule

Correct the runner, manifest, adapter or procedure without substituting another workspace topology or run method.
