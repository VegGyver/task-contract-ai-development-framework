# Start — Task Contract Generator

Use the Task Contract Generator Agent.

Provide one backlog item, issue, bug report or bounded request plus relevant project context.

Use the canonical-first project-state hierarchy from `AGENT.md`: canonical
project brief, architecture overview, backlog and method documents are the
primary source of truth when present and usable. Resolve backlog task identity,
status, dependencies and intent from the canonical backlog before consulting
preserved plans or other source evidence. Treat preserved free-form documents
as supporting evidence or fallback only, and do not fail when optional
supporting evidence is absent.

Generate the shortest safe executable Task Contract from a backlog item, issue, analysis item or direct request. If the input changes an active approved contract, classify it and return a scope-neutral clarification, correction decision, amendment or separate-task decision. Do not implement.

Begin with the outcome and next developer action. If the request is too broad, return decomposition or a blocked response using `OUTPUT-SCHEMA.md`.
