# T36b · P3 题型手册按审计修正记录

执行：Claude 子智能体（代 codex 担任执行工位）；日期：2026-10-19；基线：main `7690a83`（含 D44）。
依据：`docs/DECISIONS.md` D44（优先于 findings 的 suggestion）、D41 ②、D1；F01–F12 = `T36-findings.jsonl` 的第 1–12 行。
动笔前重读的原页（渲染图）：s24/31 MS p.6、w25/33 MS p.8、w24/31 MS p.10、s21/31 QP p.9 与 MS p.8、s23/32 QP p.12 与 MS p.11、s24/31 QP p.10 与 MS p.12、w25/33 MS p.13；w22/31 6(a)、w25/31 9(a)(i)、s22/31 2(c)(ii)、s22/32 2(c) 与各 ER 用语料文字核对。

行号是改后文件的行号。

## 逐条

| F | 级别 | 文件与行 | 改动摘要 |
|:--|:--|:--|:--|
| F01 | nit | `cards/DR.md:212`、`:216`、`:268` | “2024 年以后 / 2024 年后”改为“2024 年 11 月（w24）起”，并列出有 DECLARE 专分的四道（w24_32、s25_31、s25_33、w25_33）；212 行补一句 s24_31:3(b) 没有这一分但范答照样每行写 DECLARE；变式说明（268 行）同样提示。s24/31 MS p.6 原页只有 “TYPE FootballClub and ENDTYPE correct / every two correct declarations” 两条。 |
| F02 | nit | `cards/DR.md:577` | 考法里的位数改为“10 + 6、12 + 4、11 + 5 位；8 + 8 位见 DR-10 / DR-11”。语料核对：主题型 DR-09 的行只有这三种位数，8 + 8 只在 DR-10 / DR-11（w22_31、w22_33、s25_33）。 |
| F03 | nit | `cards/DR.md:316` | “考官报告指出这是赋值题最常见的错”改为“考官报告指出的常见错误”（ER 原文 “A common error seen …”）。 |
| F04 | nit | `core/CI.md:21` | BitTorrent 英文得分句去掉计分标记，改为「a communication protocol used for peer-to-peer file sharing」⟦9618_w25_33:4⟧（MS p.8 原页核对，仍是 ms_text 子串）。全手册再无 “[1]” 进引文。 |
| F05 | warn | `cards/BL.md:407` | 按 D41 ② / D44 改写，删去“已报总控裁决”。见下方原文。 |
| F06 | nit | — | **不改**（D44 ①：s26 的 MS 原句可以出现在得分表述与概念表；BL.md:277–278、core/BL.md:17 保留）。 |
| F07 | nit | `cards/BL.md:282` | “最常见的错是把第三列当成 10”改为“另一种常见的错是按二进制顺序把第三列当成 10（第三列是 11；这条是教学经验，考官报告没有提）”。 |
| F08 | warn | `cards/SC.md:66` | 改正理由：MS 按私钥的常见定义给分，而题干背景其实是“用私钥加密”。见下方原文。 |
| F09 | nit | `cards/AI.md:247` | “为什么这样选”补一句：扩展 F 时 E 经 F 的 g = 18、f = 26，远大于 End 的 12，MS 没写这一行，照模板写上也不扣分（F 的邻点 G 已有更小的 g，不写）。按 s23/32 QP p.12 原图重算，与 MS p.11 一致。 |
| F10 | warn | `cards/CT.md:254` | 代表题“规范代码要点”后新增一段“题给框架的边界缺陷”（D44 ④ 措辞）。见下方原文。 |
| F11 | warn | `cards/CT.md:526`、`core/CT.md:40` | 按任务卡措辞改写，core 同步。见下方原文。 |
| F12 | nit | `cards/FP.md:613` | 删去“（或 AND）”，只教逗号；注明目标里写 AND 的写法 MS 未见、不保证给分，“allow , for AND” 是规则题 FP-09 的口径。FP.md:672（FP-09 规则）的“用 AND（或逗号）”有 MS 依据，不动。 |

### warn 改后原文

**F05** `cards/BL.md:407`

> - 提醒：⟦9618_w24_31:7(d)(ii)⟧ 的 MS 把最简形式印成 D.(A.B̅)，这是官方笔误（决策 D41 ②）：由同题 (d)(i) 的 A.D + B̅.D 提公因式应得 D.(A + B̅)（按 7(a) 的真值表验算：T = 1 的六行都满足 D = 1 且 A = 1 或 B = 0）。教学按 D.(A + B̅)；给分仍按 MS，该点是「One mark for simplest form (Max 1)」⟦9618_w24_31:7(d)(ii)⟧，批改时按“最简形式”给这 1 分。

（back.md 没有勘误表，无需同步。）

**F08** `cards/SC.md:66`

> - 把“私钥用来解密”当成私钥在任何场合的用途：⟦9618_w22_31:6(a)⟧ 的 MS 把私钥写成「used to decrypt data that was encrypted with its matching public key」⟦9618_w22_31:6(a)⟧，这是私密消息的用法；但该题题干背景其实是“用私钥加密”（已验证消息），可见 MS 只是按私钥的常见定义给分。定义题照 MS 写；过程题按场合选钥匙——在已验证消息和数字签名里，私钥是用来**加密**的（见 SC-02、SC-06）。

**F10** `cards/CT.md:254`

> **题给框架的边界缺陷**　照 MS 填空得分；自己写时按模板处理边界（目标小于 Names[1] 时原代码会读 Names[0]）。原因：范围收缩到 TopOfList = 1、EndOfList = 2 时，CurrentItem = 1；目标比 Names[1] 小，`TopOfList >= EndOfList` 为假，走 `EndOfList ← CurrentItem – 1` 得 0；下一轮 CurrentItem = (1 + 0) DIV 2 = 0，读 Names[0]，越出 `ARRAY[1:100000]`。所以这段只当填空题用，不要当作可照抄的二分查找；自己写二分查找用上面 `WHILE Low <= High` 的模板。

**F11** `cards/CT.md:526`

> 1. **先定约定**：本型语料里空栈时 Top 的取值各题不同（如 w25/33 MS 接受 –1、0、1），按该题题干约定。多数题（w23 两卷、w25_31 / w25_32、2021 扩展卷）Top 指向**栈顶那个值**（最后放进去的），空栈时 Top = Base − 1（Base 为 1 → Top 为 0；Base 为 0 → Top 为 −1）；⟦9618_w25_33:10(b)⟧ 的 MS 对初值写的是「Top pointer with appropriate value (–1, 0, 1)」，范例用 `Base ← 0`、`Top ← 0`。题目没有约定时，自己选一种，并在 Push / Pop 里保持一致（下面的模板用 Top = Base − 1）。P2-DT-16 ……（后文不变）

`core/CT.md:40`（Top pointer 的中文定义）

> 存栈顶下标的整数变量；本型语料里空栈时 Top 的取值各题不同（如 w25/33 MS 接受 –1、0、1），按该题题干约定；多数题让它指向最后放入的值，空栈时比底指针小 1

## 同类表述（审计未点名，顺手按 F03 口径改）

考官报告原文只说 “common error(s)”，卡里写成“最常见”的另两处，按 F03 同样改掉：

| 文件与行 | 改前 → 改后 | ER 原文 |
|:--|:--|:--|
| `cards/CT.md:339` | “这是最常见的错误之一” → “这是一种常见错误” | s25_33:12(b)：“One common error that was seen was candidates reverting to a bubble sort.” |
| `cards/FP.md:377` | “继承图最常见的失分” → “继承图的常见失分” | s22_31:7(a)：“common errors included missing lines, missing arrows or incorrect arrows.” |

SY.md:64 的“最常见的得分答案”有 ER 原文 “The most common answers seen …” 支持，不改。

## D44 ③ · BL-02 变式

- `cards/BL.md:156`：删去“核验语料 2022–25 没有第二道……可作练习”，改为正式变式 ⟦9618_s21_31:7(c)⟧（2021 扩展题；电路 P = A XOR B、Y = P XOR C、Q = A AND B、R = P AND C、Z = Q OR R；写 Y、Z 的积之和并各说用途，4 分，MS “One mark for each point”；先做 7(a) 真值表、7(b) 电路名称）。电路按 s21/31 QP p.9 渲染图转录，积之和与 MS p.8 原页一致（卡第 5 步的式子不变，`truth_tables.py` 已验）。
- 该行主题型是 P3-BL-02，与代表题（s22_32）不同卷，非 s26，无 `equivalent_of`；按 D41 ① 的替代顺序（2021 扩展卷优先）合规。
- front.md、back.md、core/BL.md 与其他卡没有关于 BL-02“无第二道”的说法，无需改。HV-04、BL-03 的“无第二道”不在 D44 ③ 范围内，未动。
- `papers/p3/audit/check_handbook.py`：`D41_EXCEPTIONS` 里 BL-02 变式由 `'none'` 改为 `'extension'`（注 D44 ③）；另加 `ACCEPTED_PRIMARY_MISMATCH = {('P3-AI-07', 'variation')}`（D44 ② 维持 AI-07 变式），使选题检查对已裁决的情况不再报错。

## 审计脚本复跑（2026-10-19，改后）

| 命令 | 结果 |
|:--|:--|
| `check_handbook.py`（默认机检） | 79 张卡；选题规则失败 0（改前 AI-07 一条，现按 D44 ② 放行；BL-02 现有变式且合规）；伪代码 lint 0；Python 围栏 1 个（DR.md:256）`ast` 通过 |
| `check_handbook.py --verify-pages` | 156 行（79 代表题 + 77 变式，比审计时多 BL-02 变式一行）；未匹配 28 行，与审计时相同，全是表格 / 图的版面行；新增的 s21_31:7(c) QP p.9 / MS p.8 为 ok |
| `check_handbook.py --cross-quotes` | 跨章引文 0 |
| `check_handbook.py --stats` | 21 份卷；DR + SY + FP + CT 合计 62.5%（与审计时相同，本次未改统计） |
| `check_handbook.py --validate` | **按设计失败**：`Changed input since audit: papers/p3/cards/AI.md`。逐个比对 `T36-coverage.json` 记录的 20 个输入哈希，变了的正好是本次改的 8 个文件（cards/AI、BL、CT、DR、FP、SC，core/CI、CT），其余 12 个不变。`T36-coverage.json` 是 T36 审计时的快照，本次不重算 |
| `recompute.py` | 33/33 通过（含 CT-02 “item below Names[1] 读 index 0” 一条，即 F10 所述缺陷仍存在于官方框架，卡已提示） |
| `truth_tables.py` | 32/32 通过（含 BL-02 全加器积之和、BL-07 w24/31 D.(A + B̅)） |
| `check_front_back.py` | back.md 例题行越界 0；18 份卷，第 1 题 DR 17 / CI 1，最后一题 CT 8 / FP 7 / AI 2 / HV 1（与审计时相同） |

另：`make check` 全绿（2037 条 MS 引文全部是对应行 ms_text 的子串，含本次新加的三条引文）；`make build` 后 `output/p3/` 正常生成。
