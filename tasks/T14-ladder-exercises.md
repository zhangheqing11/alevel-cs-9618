# T14 · 阶梯练习实现 + 伪代码审计（执行工位 codex-2）

> **开工前提**：T10 批 1（`ladder/design.md` + L01–L03 规格）已合并进 main。总控会通知你。

## 目标

把设计工位（T10）写的每份练习规格 `ladder/levels/*/exercises/*/spec.md` 实现成可自动判分的练习文件夹；同时审计 T10 对照卡里的伪代码是否与官方伪代码指南逐字一致。

## 输入

- `ladder/levels/*/exercises/*/spec.md`（**唯一需求来源**；不要改它）、`ladder/levels/*/card.md`、`ladder/design.md`。
- `schemas/exercise-format.md`、`schemas/exercise.schema.json`、`schemas/examples/`（函数型与脚本型各一例，照着做）。
- `conftest.py`（`sol`、`candidate_path`、`exercise_dir` fixture）与 `tools/testkit.py`（`run_script`、`feed_input`、`output_lines`）。
- `ladder/design.md` §7（**给 T14 的规格约定**：四种练习形态、输出比对规则、浮点、mutant、技能标签）与 `docs/DECISIONS.md`。
- 伪代码指南：`$ALEVEL_CS_SOURCES/official/`（默认 `/Users/zhangheqing/Desktop/alevel cs/sources/official/`）。

## 每份规格要产出

在规格所在目录里：`task.md`（中文导读 + 英文题干 + 人工核对清单，取自规格）、`meta.json`（`kind: "ladder"`、`id: "L05/E03"`、`source: null`、`adapted_from` 照抄规格出处）、`starter.py`、`test_task.py`、`ref/solution.py`、`ref/mutant_*.py`（**按规格的 mutant 建议逐个实现，至少 2 个**）、`files/`（若需要）、`answer.pseudo`（规格要求先写伪代码时；含题目要求的过程/函数头）。

数据文件（D11）：逐字照抄规格「数据文件」小节；规格里的 `·` 是普通空格的可视标记；注明「最后一行不换行」的文件不得以换行结尾（写完用 `tail -c1 文件 | xxd` 自查）。

测试要求：
- 覆盖规格「必测行为」的每一条，docstring 注明对应条目；
- 只通过 fixture 访问被测代码，不 `import solution`；
- 不对实现细节过拟合：学生正确但写法不同（如用 `while` 代替 `for`、用 `str.find` 代替循环）必须能通过；
- 确定性、单个练习 < 5 秒、只用标准库。

## 伪代码审计（交叉审计职责）

逐张检查 `card.md` 与 `answer.pseudo` 模板里的伪代码：关键字拼写与大小写、`←`、`DECLARE`/`CONSTANT`/数组声明格式、`ENDIF`/`ENDWHILE`/`NEXT`、`OPENFILE … FOR READ`、`READFILE`、`EOF()`、内置函数名与参数顺序等。结果写入 `ladder/audit/pseudocode-audit-batch<N>.md`：每条问题给出卡片位置、原写法、指南写法、指南页码。**你只报告，不改卡片**（卡片归 T10）。

## 分批

跟随 T10 的批次：批 1 = L01–L03，批 2 = L04–L08，批 3 = L09–L12。每批一个 PR。

## 允许写的路径

见 `tasks/scope.json` 的 `T14`：各练习目录下的 `task.md`、`meta.json`、`starter.py`、`test_task.py`、`answer.pseudo`、`ref/**`、`files/**`，以及 `ladder/audit/**`、`tasks/progress/T14.md`。

## 完成标准（每批）

- `make check-all` 全绿：参考解全过、每个 mutant 至少挂一个测试、meta 合法。
- `make check-scope TASK=T14` 全绿。
- 审计报告已提交（没有问题也写「本批无差异」并列出检查过的卡）。
- PR 描述：练习数、每级 mutant 种类、规格中不清楚而你自行假设的地方（这些写成「需要总控决定」）。

## 工作方式

```bash
cd ~/Desktop/"alevel cs" && git fetch origin
git worktree add ~/Desktop/alevel-cs-wt/T14 -b task/T14-ladder-exercises origin/main
cd ~/Desktop/alevel-cs-wt/T14 && codex
```

进度写 `tasks/progress/T14.md`；交付：rebase → `make check-all` → `make check-scope TASK=T14` → `git push -u origin HEAD` → `gh pr create --base main --title "T14 batch N: …"`。不要合并。
