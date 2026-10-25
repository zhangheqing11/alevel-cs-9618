# 交接 · T51 开场检索题库

任务卡：`tasks/T51-retrieval-bank.md`。读者是 **Claude 学习会话（导师）**：它开场跑 `retrieval.py pick` 抽 2–3 道题给学生 Richard 做，学生用英文答，导师用 `show` 看答案批。题库的质量标准只有一条：**一道题测一环，30 秒答完，答案有 MS 证据。**

## 1. 先读

- `skill/cie-9618-cs-tutor/references/few-shots.md`：「先找缺的那一环：六种探针」「把错误转成下一道题」两节与示例 6–8（尤其示例 8：开场检索的样子——三道题的问法、✓ / ✗ 怎样处理）。
- `skill/cie-9618-cs-tutor/references/theory.md`「开场检索」段、`references/handoff-template.md` 的「下次开场检索」行。
- 一张 ★★★ 卡的「迁移与卡点」块（T50b 加的，四条：卡点、考官在换什么、从代表题到变式、反例）：`python3 skill/cie-9618-cs-tutor/scripts/rows.py card P1-IR-05`。卡点就是检索题最好的来源。
- `skill/cie-9618-cs-tutor/scripts/ledger.py`（`find_root`、`read_ledger` 可直接 import）、`init_ledger.py`（星级从 `output/p<N>/index.json` 读的写法）。

## 2. 题库格式（`references/retrieval/P<N>.md`，脚本按这个解析）

```markdown
# P1 开场检索题库

## IR　信息表示

### P1-IR-05　溢出

- **P1-IR-05-R1**　〔原情境〕
  - Q: Give the MS wording for what an overflow is.
  - A: 「The answer cannot be represented in the number of bits available」⟦9618_w24_11:1(d)⟧
  - 测：溢出定义的关键词是 number of bits available，不是 too big
- **P1-IR-05-R2**　〔换情境〕
  - Q: An 8-bit register holds 11111111. One is added. State what happens and why.
  - A: 「…」⟦…⟧
  - 测：同一个定义用到具体的位数上
```

规则：

- 卷首一行 `# P<N> 开场检索题库`；章用 `## <章码>　<章名>`；题型用 `### <题型码>　<名称>`（名称照 taxonomy 的 `name_zh`）；顺序照 taxonomy。
- 题号 `<题型码>-R<n>`，全库唯一；标签只有 `〔原情境〕`（代表题 / 变式的原场景，换个问法）和 `〔换情境〕`（同一模型换到另一个设备 / 结构 / 场景）。
- 三个字段固定顺序：`Q:`（英文，题面，学生会看到）、`A:`（答案）、`测：`（中文一句，这题测的是哪一环——导师批 ✗ 时就讲这一句）。
- **A 的证据**：
  - 是 MS 原句就写 `「…」⟦行 id⟧`，逐字从该行 `ms_text` 复制（省略号 `…` 与 `...` 不能换，校验器逐字核对）。
  - 代码 / 伪代码 / 自己组织的句子：A 行写 `（非 MS 原文）`，代码放在 A 下面缩进 4 格的围栏块里（```` ```pseudocode ```` 或 ```` ```python ````），不超过 3 行；若有支撑它的 MS 句，再加一行 `依据：「…」⟦行 id⟧`。
- 引 MS 的行只能是**该题型卡里已经出现的行**（代表题、变式、得分表述里的 ⟦⟧）或该章 `core/` 概念表已引用的行——学生首学时都见过，不会提前泄露复测要用的题。**不用 s26 行**（D1）。
- 不写不带 ⟦⟧ 的「」（构建器的正则会吞文本，T50 M1）；中文引号用 “ ”。

## 3. 脚本 `scripts/retrieval.py`（只用标准库，风格照 `ledger.py`）

```text
retrieval.py pick P1 [--n 3] [--types P1-HW-06,P1-IR-05] [--avoid P1-IR-05-R1,...] [--ledger PATH] [--seed N]
retrieval.py show P1-IR-05-R1 [P1-HW-06-R2 ...]
retrieval.py check [P1|P2|P3|P4]
```

- `pick`：不给 `--types` 时从记录表（默认 `ledger/P<N>.csv`，`--ledger` 可指定副本）取 `状态=学习中` 的题型，按 `复测日期` 由近到远（已过期的最先）；不足 `--n` 时用 `已掌握` 里 `日期` 最早的补（间隔复习）。每个题型最多出一道；同一题型优先没在 `--avoid` 里的、`〔换情境〕` 优先于 `〔原情境〕`。**只打印题号与 Q**，不打印答案。没有可抽的题型时说清楚并以 0 退出。
- `show`：打印题号、Q、A（原样，含 ⟦⟧）、测。
- `check`：解析四个文件（或指定一卷）；报错项：格式不可解析、题号重复或与所在题型不符、题型码不在 taxonomy、缺字段、A 既没有 ⟦⟧ 也没有「非 MS 原文」、引了 s26 行、★★★ 少于 2 道或没有〔换情境〕、★★☆ 少于 1 道（星级读 `output/p<N>/index.json`，缺文件时提示先 `python3 build/build.py all`）。全过打印每卷题数与换情境比例，以 0 退出。

## 4. 执行方案

1. 建 worktree（交接 README §1，新分支 `task/T51-retrieval-bank`）；`python3 build/build.py all`。
2. **先写脚本和 README**，再用 P1 IR 章的 2–3 个题型写样题，跑 `check P1`（覆盖不足的报错是预期的）、`pick --types …`、`show …`，确认格式与脚本互相吻合。提交。
3. **逐卷逐章写题**（P1 → P2 → P3 → P4）。每章：
   1. `rows.py card <章码>` 读整章；每个 ★★★ / ★★☆ 题型看「迁移与卡点」「易错」「得分表述」和概念表。
   2. ★★★ 两道：R1 测「卡点」那一环（多为〔原情境〕），R2 把同一模型换情境（参照各卡「反例」「考官在换什么」）；★★☆ 一道，测「易错」里最常丢的那一分。
   3. 问法照示例 8：短、具体、只有一个答案；不要把原题整题再问一遍；P2 / P4 的代码题只要关键的 1–3 行（循环头、判满条件、指针移动、文件模式），不要整模块。
   4. 跑 `make check` 与 `retrieval.py check <卷>`，提交 `T51: add P1 IR retrieval items`，更新进度日志。
4. 改 skill 挂钩（任务卡产出 4）：few-shots「把错误转成下一道题」第 1 步、theory.md「开场检索」段、handoff-template 检索行——先 `retrieval.py pick`，题库没有的再现编，现编的好题记进交接文档。只改说法，不动协议本身。
5. 实测：把 `ledger/P1.csv` 复制到 `work/tmp/`，用 `ledger.py` 或手改副本把 3–4 个题型改成学习中（含一个复测日期已过期），跑 `pick P1 --ledger work/tmp/P1.csv`、`show`，输出贴进 PR。**不改 `ledger/` 下的真实记录表。**
6. 交付：rebase → `retrieval.py check` → `make check` → `make check-scope TASK=T51` → push → `gh pr create --base main --title "T51: opening retrieval bank and picker"`。

## 5. 坑

- 记录表 `ledger/P1.csv` 的「优先级」列有一处过时（P1-PF-09），覆盖与星级一律以 `index.json` 为准。
- 行 id 含括号，shell 里加引号：`rows.py get '9618_w24_11:1(d)'`。
- `make check` 扫 `skill/` 下全部 `.md`：所有 ⟦⟧ 行号必须存在，所有「」⟦⟧ 必须逐字。
- 题目只测理解，不要出“背 MS 原句”的题太多（每卷不超过三成）；示例 8 的第 2 题那种“Give the MS wording”只用于措辞本身就是得分关键的题型。
- 学生 Python 弱：P4 的题测“这一行为什么这样写”，不测语法冷知识。
