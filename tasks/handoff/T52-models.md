# 交接 · T52 P3 DR、P4 LT 心智模型

任务卡：`tasks/T52-chapter-models.md`。小任务，一个会话、两次提交。

## 1. 先读（范本与素材）

- 范本：`papers/p1/cards/HW.md` 第 15 行（速度阶梯 + 感知—判断—执行环）、`SS.md`、`CM.md`、`EO.md` 里 T50b 新加的「**心智模型**」段（`grep -n '心智模型' papers/p1/cards/*.md`）。共同点：一两幅“图”（可以是文字描述的阶梯、环、表格），每个部件都落到题型码上，结尾一句“看到一道 X 题，先问……”。
- `docs/guide/concept-threads.md`：主线一（数据组织）第 3–7 步、主线三（同一算法三种写法）——LT 的模型要和它衔接（P2 DT-15 / DT-16 → P3 CT-08 / CT-09 → P4 LT）。
- 两章全文：`python3 skill/cie-9618-cs-tutor/scripts/rows.py card DR`、`rows.py card LT`（或直接读 `papers/p3/cards/DR.md`、`papers/p4/cards/LT.md`），尤其「核心思想」「本章易混辨析」和各卡「迁移与卡点」。

## 2. 写什么（方向，具体由你判断）

**DR**：先给“路由”——看到题先判断它属于三块里的哪一块（关键词：TYPE / record / set / pointer / enumerated → 类型；serial / sequential / random / direct access / hash / collision → 文件；mantissa / exponent / normalised / precision / range → 浮点），再给每块各自的一幅图：

- 类型：`TYPE` 造模板、`DECLARE` 用模板造变量；组合 / 非组合两大类各有哪些成员，每种类型“大类一句 + 独有特征两句”（DR-01–05）。
- 文件：“记录在盘上怎么排”（串行 / 顺序 / 随机）×“怎么找到它”（顺序存取 / 直接存取），散列就是“用键算出地址”，冲突就是“两个键算出同一地址”的几种处理（DR-06–08）。
- 浮点：一组固定的位分成尾数与阶码，**位数怎么分就是精度与范围的取舍**；规格化 = 尾数前两位不同；换算两个方向是同一个式子的正反用（DR-09–12）。

**LT**：在已有“指针就是下一个去哪”之上加一幅**流程定位图**：一道 LT 大题几乎总是 声明与初始化（含空闲链）→ 插入（拿空结点 → 存数据 → 改指针）/ 删除 → 查找或遍历（从起点沿指针走到空指针；二叉树按大小选左右）→ 输出与截图。再加一个判断：数组实现还是对象实现（题目决定，不要换），两种实现里“指针”分别是什么、空是什么。结尾：“看到一道 LT 小问，先问它在流程的哪一步、用的是哪种实现，模板就定了。”

## 3. 执行方案

1. 建 worktree（交接 README §1，新分支 `task/T52-chapter-models`）。
2. 写 DR 段 → `make check` → `python3 build/build.py p3` → 提交 `T52: add DR mental model`。
3. 写 LT 段 → `make check` → `python3 build/build.py p4` → 提交 `T52: add LT mental model`。
4. 自查：段里出现的每个题型码都存在（`grep '### P3-DR-' papers/p3/cards/DR.md`）；没有「」；术语与本章一致（浮点用「阶码（exponent）」，T50 S8）。
5. 交付：rebase → `make check` → `make check-scope TASK=T52` → push → `gh pr create --base main --title "T52: mental models for P3 DR and P4 LT"`。PR 贴两段全文。

## 4. 坑

- 段长控制在 HW 那段的长度左右（一段，最多再带一张小表）；不要把题型卡的内容再抄一遍。
- AS 伪代码常用 1 起数组、0 作空指针，P4 几乎都是 0 起、−1 作空指针——模型里写“以本题题干为准”，不要写死。
- 若读的时候发现别的章也缺模型，写进 PR「需要总控决定」，不要顺手改（范围外）。
