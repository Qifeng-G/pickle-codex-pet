# Bilingual Collaboration

Use English as the default language for reusable skill files, repository README files, package metadata, script output keys, and release artifacts. Use the user's language for conversation. If the user writes in Chinese, reply in Chinese while keeping code, filenames, state ids, JSON keys, and GitHub-facing docs in English unless asked otherwise.

## Chinese Input Handling

- Treat Chinese filenames as semantic labels, not noise. Examples:
  - `向右跑.mov` -> `running-right`
  - `失败.HEIC` -> `failed`
  - `任务执行中.MOV` -> `running`, meaning task-in-progress, not literal running
- Preserve English state ids in output files: `idle`, `running-right`, `running-left`, `waving`, `jumping`, `failed`, `waiting`, `running`, `review`.
- Translate user corrections into English implementation constraints before editing prompts or scripts, then explain the result back in Chinese if the user is using Chinese.
- Do not translate user intent too literally when the state label is ambiguous. Confirm semantics for words like `waving`, `running`, `review`, and `waiting`.

## Confirmation Language

When asking for approval in Chinese, keep it short and concrete:

- `这张代表帧请重点看：脸像不像、身体比例、动作语义、尾巴/爪子、白底是否干净。通过后我再做 MP4。`
- `这版 MP4 请重点看：动作顺序、身体是否抖、大小是否跳、边缘是否有色边。通过后我再更新 Codex pet。`

When recording approved constraints, write them in English for reusable artifacts:

- `Approved: standing tail-wag interpretation for waving; body and mouth must remain fixed; tail-only motion.`
- `Approved: jumping contact frame has the ball directly above the nose; sequence is one-way 1-2-3-4-5.`

## Documentation Tone

- Keep public README files English-first and copy-paste friendly.
- Avoid burying installation under long manual sections when the user wants one-command or one-prompt Codex install.
- Chinese explanations can live in conversation, issues, or optional notes, but do not mix Chinese and English randomly inside package manifests or scripts.
