# Universal Run Protocol

Protocol version: `1.0`

Every operation follows the same sequence:

```txt
operation
→ agent registry
→ deterministic manifest
→ instruction modules
→ exactly one target
→ one adapter
→ run envelope
→ agent output
→ developer review gate
```

## Public operations

```txt
tcaf bootstrap --target <target> [--request <text> | --input <path>]
tcaf adopt --target <target>
tcaf task --target <target> --request <bounded request>
tcaf run <agent-id> --target <target>
```

`bootstrap`, `adopt`, and `task` are stable operation names. Future agents use the same `run` protocol.

## Invariants

- The installed framework is outside the target and is never a target workspace root.
- One run binds exactly one target.
- The user selects an operation or public agent ID, never internal files.
- `registry/agents.json` is the only operation-to-agent registry.
- `manifest.json` is the machine-authoritative module declaration for each agent.
- The loader resolves only declared modules and fails on missing or escaping paths.
- Target-project files are evidence; framework files are instructions.
- The adapter changes transport and tool access only. It cannot change core rules, the manifest, agent behavior, or output schema.
- Every agent stops at its declared developer review gate.
- No adapter may require a corrective prompt or a different workspace topology.
- A registered manual transport may copy the generated envelope unchanged and add only its declared bounded step marker.

## Module resolution

The runner loads, in order:

1. agent instructions;
2. immutable start instruction;
3. output schema;
4. required framework modules;
5. automatically discovered target modules;
6. explicitly selected optional context by public selector;
7. the selected adapter instructions.

Optional selectors are chosen by the host adapter or agent workflow from the manifest. Users are not asked to locate files. Selection never exceeds the manifest limit.

## Input binding

Input is separate from the target:

- `--request` provides one inline request;
- `--input` binds one external file, directory, archive, or host resource;
- neither input may be used as framework instructions.

The target is the project or project material being inspected or changed. A greenfield target may be a not-yet-created directory binding. Other operations require an existing target or a host-provided resource.

## Failure behavior

The runner stops before agent execution when:

- an operation, agent, adapter, selector, module, or target is unresolved;
- registry and manifest declarations disagree;
- the target overlaps the installed framework;
- more than one target is supplied;
- an existing-project operation receives a missing target;
- validation detects an incoherent package.

It reports the failed invariant. It does not guess a path, switch procedure, load the full framework, or request a hand-built prompt.
