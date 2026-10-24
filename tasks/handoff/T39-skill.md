# 交接 · T39 教学 skill 更新到全四卷

任务卡：`tasks/T39-skill-update.md`（现状、9 项改动、允许路径、完成标准）。skill 是给 **Claude 学习会话**看的说明书：写法保持现有口吻（中文说明，命令与路径用代码格式），**不改教学协议本身**（掌握门槛、讲解结构、批改纪律、写入边界）。

## 执行方案

1. **建 worktree**（交接 README §1，新分支 `task/T39-skill-update`）；`python3 build/build.py p1 p2 p3 p4` 生成 `output/`（ledger 星级要用 `index.json`）。
2. **通读现有 skill**：`SKILL.md` 全文与 `references/*.md`，列出所有只提 P1 / P2、或与现状不符的句子（任务卡第 9 项），写进进度日志当清单。
3. **核对事实来源**（改 skill 之前先读这些，命令以它们为准）：`pipeline/mock/README.md`（模考包用法）、`corpus/thresholds/README.md`（学生对应的 option、加权）、`papers/p4/practice-notes.md` 与 `schemas/exercise-format.md` 末节（P4 练习约定）、`tools/try.py`（`K=`）、`docs/DECISIONS.md` D1、D2、D31、D32、D33、D37、D38、D44、D45。
4. **改 `SKILL.md`**（任务卡第 1–5 项）：资源表、P3 流程、P4 流程、批改纪律补充、整卷模考小节。新增内容尽量放进已有小节，或在相应位置加小节；不重排原有结构。
5. **改 references**：`syllabus-map.md` 用脚本从 `papers/p3|p4/taxonomy.json` 的 `syllabus` 字段生成 13–20 节对照表；`few-shots.md` 加两个短示范（P3 写代码题按 MP 批改、P4 小问“自动测 + 人工清单”），行与 MS 原文取自真实语料；`programming.md` 补 P4 相关处（与 SKILL.md 不重复，互相指向）。
6. **学习记录表**：写 `skill/cie-9618-cs-tutor/scripts/init_ledger.py <P3|P4> [--force]`：从 taxonomy 与 `output/p<N>/index.json` 生成 13 列 `utf-8-sig` 表（格式照 `schemas/ledger-format.md` 与 `ledger/P2.csv`）；生成 `ledger/P3.csv`、`ledger/P4.csv`；`python3 skill/cie-9618-cs-tutor/scripts/ledger.py summary` 能读出。
7. **实测 skill 里的每条命令**（任务卡完成标准）：`rows.py get|find|drills|ex|render` 各跑一次 P3 / P4 行（行 id 含括号，shell 里加引号）；`make_mock.py` 生成一份 s26 卷的批改包；在 `--out` 的临时目录里给 `score.csv` 填假数据，跑 `score_mock.py`；用一道 P4 练习的参考解跑 `make try EX=… K=1b`（复制到 `attempts/` 后跑，跑完删掉）。命令与输出摘要写进 PR。
8. 交付：rebase → `make check` → `make check-scope TASK=T39` → push → `gh pr create --base main --title "T39: update tutor skill for P3/P4, mocks and thresholds"`。

## 提醒

- `ledger/P1.csv`、`P2.csv`、`ladder.csv` 是学生的真实记录，**不要改**。
- skill 已软链到 `~/.claude/skills/`：合并后立即生效，所以改动里不能留半成品或占位符。
- 不确定的教学协议问题（例如模考后多久复测、P4 截图格是否计入掌握门槛）写进 PR「需要总控决定」，不要自行定规则。
