# Installation

```bash
git clone <your-repo-url>
cd local-code-memory
./install.sh
```

Verify:

```bash
command -v code-memory
```

If `~/.local/bin` is not in your PATH, add it.

Bash/Zsh:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Fish:

```fish
fish_add_path -m $HOME/.local/bin
```
