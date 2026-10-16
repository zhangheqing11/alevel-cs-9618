# Codex 启动提示词

在 worktree 里打开 codex 后，整段粘贴对应提示词。worktree 命令见各任务卡「工作方式」。

## codex-1 · T13（现在可开）

```
你是执行工位 codex-1，负责任务 T13（手册构建器）。
先读 AGENTS.md，再读 tasks/T13-builder.md；若 tasks/progress/T13.md 存在，从它记录的下一步继续。
只改任务卡允许的路径（tasks/scope.json 的 T13）。共享文件需要改动时，不要绕过，在 PR 描述写「需要总控决定：…」。
完成标准见任务卡。交付：git fetch origin && git rebase origin/main → make check → make check-scope TASK=T13 → git push -u origin HEAD → gh pr create --base main。不要合并 PR。
中途停下或上下文将满时，把已完成/进行中/下一步/坑写进 tasks/progress/T13.md 并提交。
```

## codex-1 · T12（总控通知语料就绪后）

```
你是执行工位 codex-1，负责任务 T12（抽文本、拆最细小问）。
先读 AGENTS.md，再读 tasks/T12-extract-rows.md 与 schemas/corpus-format.md；若 tasks/progress/T12.md 存在，从它记录的下一步继续。
PDF 在 /Users/zhangheqing/Desktop/alevel cs/sources/pastpapers/（只读）。按 P1 → P2 → P3 → P4 分批，每批一个 PR。
只改 tasks/scope.json 里 T12 允许的路径。交付：rebase origin/main → make check → make check-scope TASK=T12 → push → gh pr create --base main。不要合并 PR。
停下前更新 tasks/progress/T12.md 并提交。
```

## codex-2 · T14（总控通知 T10 批 1 合并后）

```
你是执行工位 codex-2，负责任务 T14（阶梯练习实现 + 伪代码审计）。
先读 AGENTS.md，再读 tasks/T14-ladder-exercises.md、schemas/exercise-format.md 和 schemas/examples/；若 tasks/progress/T14.md 存在，从它记录的下一步继续。
需求只来自 ladder/levels/*/exercises/*/spec.md，不要改 spec.md 或 card.md。伪代码指南在 /Users/zhangheqing/Desktop/alevel cs/sources/official/。
只改 tasks/scope.json 里 T14 允许的路径。交付：rebase origin/main → make check-all → make check-scope TASK=T14 → push → gh pr create --base main。不要合并 PR。
停下前更新 tasks/progress/T14.md 并提交。
```
