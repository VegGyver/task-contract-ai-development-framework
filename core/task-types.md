# Task Types

Use one primary type per task.

| Type | Purpose | Main boundary |
|---|---|---|
| `INSPECT` | Read and report | No edits |
| `PROJECT_ANALYSIS` | Define project scope, architecture or plan | No application code edits |
| `CODE_FEATURE` | Add new behavior | No implicit refactor/tooling |
| `CODE_CHANGE` | Change existing behavior | Preserve working code; minimal integration |
| `CODE_FIX` | Correct demonstrated faulty behavior | Modify only the identified cause |
| `TEST_ONLY` | Add or update tests | Existing test capability only |
| `REFACTOR` | Change structure without intended behavior change | Must be explicit and independently verified |
| `DOCS_STATUS_UPDATE` | Update status/progress fields | Preserve document structure and history |
| `DOCS_CONTENT_UPDATE` | Update an explicitly named section | No unrelated editorial rewrite |
| `CONFIG_TOOLING` | Change configuration, scripts or dependencies | Separate explicit approval |
| `BACKLOG_REPLAN` | Reorder or add future work | Do not rewrite completed history |
| `FRAMEWORK_ADOPTION` | Add framework files to an existing project | Additive-only by default |

A task that contains more than one primary purpose should normally be split.
