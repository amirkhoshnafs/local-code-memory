# Review With Memory Prompt

Use `@AI_MEMORY.md` as project memory.

Review the attached file against the project commands, style, and known errors.

Do not give a generic review. Look for:
- mismatches with project style
- likely test failures
- missing edge cases
- known errors listed in memory
- commands that should be run next

Return:
1. concrete issues
2. smallest targeted fixes
3. exact verification command
