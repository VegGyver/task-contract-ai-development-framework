# Execution Profiles

Profiles define preferred order, not permission. The task contract remains authoritative.

## Common profiles

- `FULLSTACK_CONTRACT_SLICE`: shared contract → minimal backend → frontend integration → verification.
- `BACKEND_CONTRACT_FIRST`: contract/schema → service/data → route → verification.
- `BACKEND_API_FIRST`: route shape → validation → service/data → verification.
- `FRONTEND_API_FIRST`: API client/data → state → UI → verification.
- `FRONTEND_UI_FIRST`: static UI → local behavior → integration → verification.
- `FIX_REPRO_FIRST`: evidence/reproduction → minimal cause fix → targeted verification.
- `FIX_LOG_FIRST`: evidence/logging task before modifying uncertain behavior.
- `DOCS_STATUS_LINE_ONLY`: change only allowed status/progress fields.
- `DOCS_SECTION_UPDATE`: update only the named section.
- `EXISTING_LOCAL_PATTERN`: follow nearest working pattern and integrate minimally.
- `LEGACY_CHARACTERIZATION_FIRST`: understand current behavior before a risky legacy change.
- `CONFIG_TARGETED_FIX`: change only the necessary configuration.

Skip layers not present in the project. Do not introduce missing layers to satisfy a profile.
