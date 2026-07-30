# Adapter Contract

Adapters connect the Universal Run Protocol to one tool or host. They are not part of the methodological core.

## Required responsibilities

An adapter must:

1. provide its registered adapter ID to the runner or allow deterministic environment detection;
2. bind exactly one target through the host's native file/resource access;
3. invoke the selected public operation;
4. pass the assembled run envelope to the model unchanged;
5. expose only the permissions actually available;
6. preserve instruction and target surfaces;
7. return the agent output using its declared schema;
8. stop at the developer review gate.

A registered manual transport may require the developer to copy the machine-generated envelope unchanged and append one adapter-defined step marker. It may segment writes, but it must not reconstruct or alter the envelope.

## Forbidden behavior

An adapter must not:

- alter core rules, manifests, task permissions, or output schemas;
- require the framework as another target workspace root;
- ask the user to select framework files;
- invent replacement prompts;
- treat framework modules as project evidence;
- silently continue after a failed validation or missing module;
- claim direct inspection, command, or edit access that the host does not provide.

## Compatibility

A host is compatible only if it can make the installed framework available persistently and bind target material without reconstructing the framework for each run.

A generic chat with persistent assistant knowledge or a native package/resource integration can be compatible. A chat with neither persistent instructions nor attachment/resource access is incompatible and must say so instead of introducing a temporary manual procedure.

An adapter must not claim native invocation until that bridge has passed its acceptance test.
