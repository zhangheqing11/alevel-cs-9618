# Codex 启动提示词

在 worktree 里打开 codex 后，整段粘贴对应提示词。worktree 命令见各任务卡「工作方式」。

## codex-2 · T13（现在可开）

```
你是执行工位 codex-2，负责任务 T13（手册构建器）。
先读 AGENTS.md，再读 tasks/T13-builder.md；若 tasks/progress/T13.md 存在，从它记录的下一步继续。
只改任务卡允许的路径（tasks/scope.json 的 T13）。共享文件需要改动时，不要绕过，在 PR 描述写「需要总控决定：…」。
完成标准见任务卡。交付：git fetch origin && git rebase origin/main → make check → make check-scope TASK=T13 → git push -u origin HEAD → gh pr create --base main。不要合并 PR。
中途停下或上下文将满时，把已完成/进行中/下一步/坑写进 tasks/progress/T13.md 并提交。
```

## codex-1 · T12（现在可开：语料已就绪）

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

## codex-1 · T24（现在：手上那卷 T12 开出 PR 后就转这个）

```
你是执行工位 codex-1，负责任务 T24（P1 全量打标签）。它优先于 T12 剩余的 P3/P4。
先读 AGENTS.md、docs/DECISIONS.md，再读 tasks/T24-p1-tagging.md、papers/p1/taxonomy.json、papers/p1/tagging-guide.md（唯一打标签规则）。若 tasks/progress/T24.md 存在，从它记录的下一步继续。
从最新 origin/main 开分支 task/T24-p1-tagging。先盲标全部 979 行，再与 papers/p1/pilot_tags.csv 比对一致率。标签真源放 pipeline/tag/p1_tags.jsonl，用脚本合并进 corpus/rows/p1/。
只改 tasks/scope.json 里 T24 允许的路径。交付：rebase origin/main → make check → make check-scope TASK=T24 → push → gh pr create --base main。不要合并 PR。停下前更新 tasks/progress/T24.md 并提交。
```

## codex-2 · T14 批 3（现在可开：T10 批 3 已合并）

```
继续 T14：实现 T10 批 3（L09–L12）的练习与伪代码审计，同批 1、批 2 的做法。先读 docs/DECISIONS.md（D10–D13、D18）。从最新 origin/main 开分支 task/T14-ladder-batch3。交付：rebase → make check-all → make check-scope TASK=T14 → push → gh pr create --base main --title "T14 batch 3: L09–L12"。不要合并 PR。
```

## codex-1 · T12 补 equivalent_of（D21，可在 T24 之后或手头那卷之后做）

```
T12 后续：按 docs/DECISIONS.md D21，用 pipeline/extract/overrides.json 给 9618_s21_23、9618_w21_23 中与同季 _21 卷逐题相同、但还没标 equivalent_of 的 37 行补上 equivalent_of（指向 _21 卷对应行），重跑抽取确认其余字段不变。从最新 origin/main 开分支 task/T12-p2-equivalents。交付：make check → make check-scope TASK=T12 → push → gh pr create --base main。不要合并。
```

## codex-2 · T28（现在可开：P2 全量打标签 + 拆得分点）

```
你是执行工位 codex-2，负责任务 T28（P2 全量打标签 + 拆得分点）。它与 codex-1 的 T24（P1）并行，不要碰 P1 的文件。
先读 AGENTS.md、docs/DECISIONS.md，再读 tasks/T28-p2-tagging.md、papers/p2/taxonomy.json、papers/p2/skill_tags.json、papers/p2/tagging-guide.md（唯一规则，§8 是得分点拆分）。若 tasks/progress/T28.md 存在，从它记录的下一步继续。
从最新 origin/main 开分支 task/T28-p2-tagging。先盲标全部 721 行并拆得分点，再与 papers/p2/pilot_tags.csv、pilot_markpoints.jsonl 比对。真源放 pipeline/tag/p2/，用脚本合并进 corpus/rows/p2/。
只改 tasks/scope.json 里 T28 允许的路径。交付：rebase origin/main → make check → make check-scope TASK=T28 → push → gh pr create --base main。不要合并 PR。停下前更新 tasks/progress/T28.md 并提交。
```
