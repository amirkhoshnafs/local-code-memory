# Local Code Memory

A lightweight, file-based project-memory workflow for coding assistants.

Local Code Memory gives any coding assistant a stable project briefing through `AI_MEMORY.md`, generated from editable files in `.project-memory/`.

It works especially well with local models through **Ollama + Qwen + Continue**, but the workflow is model-agnostic. You can use the memory file with Continue, Cursor, Claude Code, Cline, Aider, OpenHands, or any chat-based coding assistant that can read project files.

## Why this exists

Coding assistants often fail because they do not know:

- what your project does
- how to run your tests
- which commands are safe
- your style preferences
- what happened last session
- known errors and previous fixes
- what not to invent

Local Code Memory makes that context explicit, editable, and versionable.

## What you get

- `code-memory` command
- `.project-memory/` editable memory folder
- generated `AI_MEMORY.md` bridge file
- optional `QWEN_MEMORY.md` alias for Qwen/Continue workflows
- Ollama Modelfile example for a local coding-agent model
- Continue config example with separate chat/edit and autocomplete roles
- test-driven coding-agent workflow docs
- example projects showing the loop

## Quick start

```bash
# clone this repo
cd local-code-memory
./install.sh

# inside any project
cd /path/to/your/project
code-memory .
code .
```

Then attach `@AI_MEMORY.md` in your coding assistant and ask it to use that as project memory.

For Qwen/Continue users, you can also generate a compatibility alias:

```bash
code-memory . --qwen-alias
```

Then attach `@QWEN_MEMORY.md` in Continue.

## Recommended assistant loop

1. Attach `AI_MEMORY.md`.
2. Ask the assistant to inspect relevant files before editing.
3. Ask for the smallest targeted change.
4. Run tests.
5. Paste exact failing output.
6. Ask for a targeted fix.
7. Re-run tests.
8. Update memory.

The main rule:

> Do not trust vague review-only answers. Prefer tests, tracebacks, and targeted fixes.

## Example prompt

```text
Use @AI_MEMORY.md as project memory.

The tests are failing. Inspect the relevant file and the failing test output.
Suggest the smallest targeted fix.
Do not modify unrelated files.
```

## Ollama + Qwen setup

Create a local coding-agent wrapper model:

```bash
ollama pull qwen2.5-coder:7b
ollama create local-code-agent -f configs/ollama/Modelfile
```

Then use `configs/continue/config.yaml` as a starting point for Continue.

## Repository layout

```text
local-code-memory/
├── scripts/                 # code-memory command and helpers
├── templates/               # memory file templates
├── configs/                 # Continue and Ollama examples
├── prompts/                 # reusable agent prompts
├── docs/                    # setup and workflow docs
└── examples/                # small example projects
```

## What this is not

Local Code Memory is not a full agent framework, model server, vector database, or Claude Code replacement.

It is a small project-memory layer that makes coding assistants less forgetful and more test-driven.

## Privacy and safety

The memory files are plain text in your project. Do not store secrets in them.

Do not store:

- API keys
- tokens
- passwords
- SSH keys
- private credentials
- huge logs
- sensitive personal data

## License

MIT. See `LICENSE`.
