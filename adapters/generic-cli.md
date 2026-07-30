# Generic CLI Adapter

Use when the runner is available locally but no supported AI host integration identifies itself.

- Assemble the same run envelope as every other adapter.
- Print Markdown by default or JSON when requested.
- Bind the current directory when no explicit local target is supplied.
- Do not claim that an AI model executed the envelope.
- A compatible host may consume the envelope directly.
- Keep the framework outside the target.
