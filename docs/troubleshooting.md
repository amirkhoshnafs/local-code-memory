# Troubleshooting

## `code-memory: command not found`

Add `~/.local/bin` to PATH.

Fish:

```fish
fish_add_path -m $HOME/.local/bin
```

Bash/Zsh:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

## Assistant ignores hidden memory folder

Attach `AI_MEMORY.md`, not `.project-memory/*`. The bridge file exists to make memory visible and reliable.

## Assistant gives vague review

Give it failing tests and exact traceback output. The workflow is strongest when test-driven.
