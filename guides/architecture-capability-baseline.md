# Architecture Capability Baseline

Inspect only capabilities relevant to the current task or adoption decision.

Classify each capability:

```txt
Available
Available with limits
Not available
Unclear
```

Rules:

- `Available`: direct target-project evidence confirms usable support.
- `Available with limits`: support exists but scope or completeness is limited.
- `Not available`: authoritative project docs explicitly exclude it, or relevant expected target-project paths were directly inspected and support is absent.
- `Unclear`: evidence, path visibility or workspace coverage is incomplete.
- Never infer absence from a shallow tree, omitted hidden folders, uninspected paths or framework files.
- Before using `Not available`, confirm likely exact paths through read-only listing or search, including relevant dot-prefixed config. Never test absence through repeated failed reads.
- Framework files are instructions, not evidence about the target project.
- Use existing dependencies, scripts, tools and local patterns.
- Do not add a missing capability implicitly.
- If a required capability is absent, propose a separate `CONFIG_TOOLING` task.
- Select checks only from supported capabilities.
- Inspect the smallest relevant target-project file set; do not scan the whole repository by default.

## Evidence order

Use the strongest available target evidence:

1. active configuration, dependency declarations and executable scripts;
2. representative working source usage;
3. tests, CI and build configuration;
4. authoritative current project documentation;
5. historical or planning documents, labelled as non-current when applicable.

Documentation alone does not make planned functionality available. A dependency alone does not prove a project-wide usage pattern.

## Repository standard extraction

For each task-relevant area, record:

```txt
Area:
Observed pattern:
Evidence paths:
Scope / limits:
Classification: Established / Localized / Conflicting / Unclear
```

Extraction rules:

- inspect a representative working use, not every occurrence;
- prefer the nearest relevant feature or layer;
- distinguish an established repeated pattern from a one-off implementation;
- classify an isolated or explicitly legacy exception as `Localized`; reserve `Conflicting` for multiple active patterns that materially disagree;
- record exact target paths and relevant config keys or scripts;
- do not infer a convention from generated, vendored, build-output or framework files;
- do not convert inferred best practice into an existing-project rule;
- use `Conflicting` only when multiple active working patterns disagree materially;
- use `Unclear` when evidence is insufficient;
- propose standardization or cleanup only as a separate explicit task.

The extracted standards guide later integration. They do not authorize rewriting current code.
