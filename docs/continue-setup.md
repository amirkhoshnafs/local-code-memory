# Continue Setup

1. Install Ollama.
2. Pull Qwen:

```bash
ollama pull qwen2.5-coder:7b
```

3. Create the coding-agent wrapper:

```bash
ollama create local-code-agent -f configs/ollama/Modelfile
```

4. Copy `configs/continue/config.yaml` into your Continue config, or merge the model blocks into your existing config.

5. In a project:

```bash
code-memory .
code .
```

Attach `@AI_MEMORY.md` in Continue.
