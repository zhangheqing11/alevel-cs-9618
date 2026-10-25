# 交接文档（总控 → Codex 执行工位）

从 2026-10-24 起：总控（Claude）写任务卡、交接文档与提示词并验收；**执行工作由 Codex 会话完成**（每个任务新开一个 Codex 会话，粘贴 `tasks/PROMPTS.md` 里对应的提示词）。交接文档 = 任务卡之外的「怎么做」：现状、逐步执行方案、坑、自检与交付。规则仍以 `AGENTS.md`、`docs/DECISIONS.md`、任务卡为准；交接文档与它们冲突时以它们为准，并在 PR 里指出。

| 文档 | 任务 | 状态 |
|:--|:--|:--|
| [T35-practice.md](T35-practice.md) | T35a–f P4 真题练习（54 道大题） | ✅ 已合并（#48、#49、#52–#55） |
| [T37-cards.md](T37-cards.md) | T37A / T37B P4 题型卡 | ✅ 已合并（#50、#51） |
| [T38-audit.md](T38-audit.md) | T38 审计 P4 手册 + 抽查 6 道练习 | ✅ 已合并 #57 |
| [T38-fixes.md](T38-fixes.md) | T38b 改 P4 卡（含 OP 换题）；T38c1–3 排查 54 道 P4 练习 | ✅ 已合并（#58、#60、#61、#59；D48） |
| [T39-skill.md](T39-skill.md) | T39 教学 skill 重构到全四卷 + P3 / P4 记录表 | ✅ 已合并 #56（D47） |
| [T51-retrieval.md](T51-retrieval.md) · [T51-rework.md](T51-rework.md) | T51 开场检索题库 + 抽题脚本 | 🔨 #66 题库内容打回返工（脚本与挂钩保留） |
| [T52-models.md](T52-models.md) | T52 P3 DR、P4 LT 心智模型 | 👀 #64 验收通过，待合并 |
| [T53-guide-build.md](T53-guide-build.md) | T53 指南进构建 + 引文正则（M1） | 👀 #65 验收通过，待合并 |

## 通用约定（所有交接任务）

1. **工作区**：不在主 checkout `/Users/zhangheqing/Desktop/alevel cs` 里改文件或切分支。在 Codex 自己的 worktree 里做：
   - 续做已有分支：`cd ~/Desktop/"alevel cs" && git fetch origin && git worktree add ~/.codex/worktrees/<任务>/"alevel cs" task/<分支>`（本地分支已存在且与 origin 同步；若本地没有就 `-b task/<分支> origin/task/<分支>`）。
   - 新任务：`git worktree add ~/.codex/worktrees/<任务>/"alevel cs" -b task/<分支> origin/main`。
2. **原件**只读：`/Users/zhangheqing/Desktop/alevel cs/sources/`（环境变量 `ALEVEL_CS_SOURCES`）。看原页：`python3 skill/cie-9618-cs-tutor/scripts/rows.py render <行 id> [--ms] [--pages N] --out <临时目录>`，再看图片。
3. **环境**：`~/.venvs/alevel-cs/bin/python`（pytest、pymupdf）；命令走 Makefile：`make check`、`make check-all`、`make check-scope TASK=<任务>`、`python3 build/build.py p<N>`。
4. **范围**：只写 `tasks/scope.json` 里本任务允许的路径与 `tasks/progress/<任务>.md`；共享文件（`tools/`、`schemas/`、`docs/`、`AGENTS.md`、`Makefile`、其他任务的目录）不改，需要时写进 PR「需要总控决定」。
5. **提交**：小步提交，信息 `<任务>: <英文祈使句>`；每完成一个单元（一道大题 / 一章）就提交并更新进度日志，**随时可能被中断，进度必须在提交里**。
6. **交付**：`git fetch origin && git rebase origin/main` → 本任务的校验命令全绿 → `git push -u origin HEAD` → `gh pr create --base main --title "…"`（普通 PR）。**不合并、不推 main、不 force-push 别人的分支**（续做的分支归你，rebase 后可 `--force-with-lease`）。shell 连不上 GitHub 时可以用 GitHub 连接器发布，PR 里写明并确认远端树与本地校验树一致。
7. **PR 描述**：做了什么、校验结果（贴命令与结果）、对照原页情况、已知问题、「需要总控决定」。
