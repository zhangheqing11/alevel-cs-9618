# T25 · P2 真题练习文件夹（执行工位 codex-2）

## 目标

把 P2 的写代码真题做成练习文件夹：学生先用**伪代码**作答（按 MS 得分点人工批改），再把同一算法写成 **Python** 跑 pytest。这是「伪代码按 MS 判 + 同题 Python 版自动测」决策的落地，也是 P2「失分技能」统计的来源。

## 选题范围

`corpus/rows/p2/*.jsonl` 中有 `markpoints` 的行，**2022–25 核验语料**（不含 `extension: true` 的 2021，不含 `9618_s26_*`——D1 保留给模考），且主题型**不是** `P2-AD-04`（画流程图，没法自动测）。约 126 行。一道大题下若有几个相关的写代码小问（例如 (a) 写函数、(b) 写调用它的过程），可以合成一个练习，`meta.source.rows` 列全。

## 分批（每批一个 PR）

1. 批 1：主题型 `P2-PG-*`（字符串、数值、输入-处理-输出、日期、IF/CASE）。
2. 批 2：主题型 `P2-DT-*`（一维/二维数组、记录数组、冒泡、读写文件、ADT）。
3. 批 3：主题型 `P2-AD-05`、`P2-AD-06`（流程图 → 伪代码、按文字描述写算法）。

## 每个练习

目录 `practice/p2/<卷>_<题号去括号>/`（如 `practice/p2/9618_s24_22_6a/`），文件按 `schemas/exercise-format.md`：

- `task.md`：中文导读 + **英文原题**（从 QP 原页转写：题干、给定的模块描述表、全局变量与数组声明、示例数据；保留标识符与格式）+ 「先写伪代码，再写 Python」+ 人工核对清单（来自该行 `markpoints` 中测试测不到的点：模块头、声明、注释、伪代码写法、D2 规则提醒）。
- `meta.json`：`kind: "past-paper"`、`id` 为主行 id、`source: {paper, rows}`、`marks`、`types`（主 + 副）、`skills`（这些行 `markpoints` 的技能并集）、`pseudocode: true`、`ms_verified: true`、`entry`。
- `answer.pseudo`：伪代码作答模板——**只给题目要求的模块头与结束行**（照 QP 写的标识符与参数），内部留空；全局变量/数组按题目给的声明写成注释行。
- `starter.py`：Python 骨架。**标识符照抄题目**（CamelCase，如 `CountVowels`），参数顺序照题目；题目给的全局数组/变量在模块顶层建出来（真实 list，注释写明大小与类型，D10）。下标约定：伪代码 1 起的数组，Python 用同样大小的 list 并在注释里写明「Python 下标 = 伪代码下标 − 1」，或按题目给定的下界换算；同一练习内保持一致。
- `test_task.py`：每个测试的 docstring 写对应行 id 与得分点编号（如 `"""9618_s24_22:6(a) MP3–MP5"""`）。行为来自 MS：MS 给了示例输入输出就用它们，再补边界情况；MS 只描述步骤时，从题目给的描述推出行为。写文件的题检查生成的文件内容；读文件的题把题目描述的数据格式做成 `files/` 里的样例文件。
- `ref/solution.py`：参考解，尽量贴近 MS 的范例算法（照 MS 范例伪代码翻译），不用题目禁止的内置函数（D10）。
- `ref/mutant_*.py`：**至少 2 个**，从该行 `markpoints` 里挑真实易错点各做一个（如漏关文件 `file-close`、循环边界差一 `loop-bounds`、返回类型错 `boolean-return`），文件头注释写明对应的得分点与技能标签。

## 规则

- 伪代码批改不靠测试：测试只验证 Python 版的行为。task.md 的人工核对清单要覆盖测试测不到的得分点。
- 只用标准库；确定性（随机数题注入或固定种子）；单个练习 < 5 秒。
- 正确但写法不同的 Python 必须能通过（不测内部实现）；题目规定的标识符与返回类型必须测。
- 不改 `corpus/`、`papers/`、`ladder/`、共享文件；发现 MS/行数据问题写进 PR「需要总控决定」。
- 读 QP 原页确认题干与示例：PDF 在 `/Users/zhangheqing/Desktop/alevel cs/sources/pastpapers/`（只读），`python3 skill/cie-9618-cs-tutor/scripts/rows.py render <行 id> [--ms]`。

## 允许写的路径

`practice/p2/**`、`tasks/progress/T25.md`。

## 完成标准（每批）

- `make check-all` 全绿：参考解全过、每个 mutant 至少挂一个测试、meta 合法（`types` 在 taxonomy 中、`skills` 在词表中、`source.rows` 存在）。
- `make check-scope TASK=T25` 全绿。
- PR 描述：练习数与覆盖的行、合并成一个练习的小问、跳过的行及原因、需要总控决定的事项。

## 工作方式

从最新 origin/main 开分支 `task/T25-p2-practice-b<批号>`；进度写 `tasks/progress/T25.md`；交付 rebase → make check-all → make check-scope TASK=T25 → push → `gh pr create --base main --title "T25 batch N: P2 practice …"`。不要合并。
