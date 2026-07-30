# Using the Agents

Install the framework once and invoke the Universal Runner. Do not reconstruct modules or invent a start prompt. A registered manual transport copies the generated envelope unchanged.

## Public operations

```txt
tcaf bootstrap --target <target> [--request <text> | --input <path>]
tcaf adopt --target <target>
tcaf task --target <target> --request <bounded request>
tcaf run <future-agent-id> --target <target>
```

The registry selects the bundle. Its machine manifest loads all required modules, project evidence and the host adapter.

## Stable procedure

1. Invoke one public operation.
2. Let the runner bind exactly one target and assemble the run envelope.
3. Use the transport declared in the envelope. Manual transports copy it unchanged and add only the adapter-defined step marker.
4. Review the agent output against its declared schema.
5. Approve only the next bounded write or execution step.

## Tool use

- Codex, Cline and other direct-access tools bind the current project through their adapter.
- Cline currently uses the `manual-envelope` transport in `adapters/cline.md`; use one Cline task per write.
- Compatible generic chat hosts bind attachments/resources through the same target contract.
- A chat without persistent framework availability and target-resource access is incompatible; do not replace the protocol with manual bundles.

One agent role per operation. Human review remains mandatory. Do not claim native invocation for an adapter whose envelope reports it as unverified.

The single-file profiles in this directory are legacy references. They are not registered or loaded by the runtime.
