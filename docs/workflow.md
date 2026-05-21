# Workflow

Recommended loop:

1. Initialize memory:

```bash
code-memory .
```

2. Fill `.project-memory/commands.md`, `summary.md`, and `style.md`.
3. Regenerate `AI_MEMORY.md`:

```bash
code-memory .
```

4. Attach `@AI_MEMORY.md` in your coding assistant.
5. Ask the assistant to inspect files before editing.
6. Run tests.
7. Paste failing output back to the assistant.
8. Ask for a targeted fix.
9. Update memory after the session.

Best prompt pattern:

```text
Use @AI_MEMORY.md as project memory.
Here is the failing test output.
Fix only the relevant file.
Do not modify tests.
Keep the change targeted.
```
