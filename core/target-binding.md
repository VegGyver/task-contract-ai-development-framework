# Target Binding

A run has exactly one target descriptor:

```txt
locator
kind
existence
access mode
```

## Target kinds

- `planned-directory` — greenfield path that does not yet exist;
- `directory` — local project directory;
- `file` — one project or documentation file;
- `archive` — project snapshot or documentation archive;
- `host-resource` — attachment or resource exposed by a compatible host.

## Rules

- The normalized target cannot be the installed framework or contain it.
- A local adapter defaults to the current directory only when no target is explicitly provided.
- A host adapter binds the selected attachment/resource without asking the user for an internal path.
- The runner does not modify the target while assembling a run envelope.
- Bootstrap may bind a `planned-directory`; adoption and daily tasks may not.
- Repository presence is optional. Target existence and access are the relevant conditions.

## Target modules

When a manifest declares target document roles, the runner:

1. reads approved mappings from `docs/method/project-manifest.md` when present;
2. otherwise uses `registry/project-schema.json` default paths;
3. loads an existing mapped file;
4. uses a declared framework fallback when the target role is absent;
5. records unresolved optional roles without inventing files.

Target modules remain target evidence and are labelled separately in the run envelope.
