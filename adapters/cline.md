# Cline Adapter

Current verified transport: `manual-envelope`. Native runner-to-Cline invocation is not verified.

1. Run `tcaf ... --adapter cline` outside Cline.
2. Start a new Cline task and paste the generated Run Envelope unchanged.
3. Append exactly one transport marker:

   ```txt
   TCAF CLINE STEP: INSPECT
   TCAF CLINE STEP: WRITE <repository-relative-path>
   TCAF CLINE STEP: VALIDATE
   ```

`INSPECT` and `VALIDATE` are read-only. `WRITE` authorizes at most one write operation to the named file and one write confirmation in that Cline task. The marker may only narrow the envelope; it cannot expand target, scope, permissions or output.

- Bind the active project as the single target; never add the framework as a workspace root.
- In `INSPECT`, use read-only listing or search before direct reads, including relevant dot-prefixed project config. Record absent paths without calling or retrying the read tool on them.
- Use a new Cline task for every write and review the actual file before the next task.
- Do not use Cline terminal commands by default. Record one to three `DEVELOPER_RUN` commands or manual checks.
- After the one write, report the changed file and stop at developer review.
- If Cline remains `Pending` after an approved write but the file changed, treat the write as performed and review the file; do not approve or repeat it.
- If the file did not change, start a fresh Cline task for the same bounded step; do not broaden the request.
- Never claim automatic or native Cline invocation until its bridge passes a dedicated acceptance test.
- Keep global rules short; canonical project rules remain project evidence.
