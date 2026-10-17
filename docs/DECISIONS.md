# 决策记录

> 总控维护。每条：日期 · 来源 · 决定 · 依据。任务卡与 skill 与此冲突时以此为准，并修正那一方。

## 2026-10-16 · T10 批 1 / T11 审查

| # | 来源 | 决定 | 依据 |
|:--|:--|:--|:--|
| D1 | T11 | **保留 `9618_s26_*`（12 份）给 4–5 月限时整卷模考**；专项刷题与复测跳过。题型卡代表题/变式若来自 s26 照常使用。T20–T23 选代表题与变式时**优先避开 s26**。 | 学生选择 |
| D2 | T11、T10 | P2 要求 pseudocode 时，混入编程语言语法或插页以外的语言函数（`def`、`len()`、切片、`FOR x IN file` 等）**该得分点不给**；非指南但非语言特有的写法（如考官范答中的 `ELSIF`、`INPUT a, b, c`）只有该题 MS 原文显示接受时才给，否则按不给并给出指南写法。阶梯与手册只教指南写法。 | s24 ER：“if the question asks for pseudocode, then variations with their studied programming language will be unacceptable”；`FOR Line IN InputFile` 列为常见错误；s23 ER 同义 |
| D3 | T11 | 编程题型**没有练习文件夹时不能标「已掌握」**：伪代码按 MS 批，Python 按样例手动核对，标「学习中」，解释证据写「无 pytest，待练习建成后补测」。 | 学生规则：编程题以测试过关 |
| D4 | T11 | 错误分类增加「手算与单位」。 | 禁用计算器（考纲 p.11） |
| D5 | T11 | 学习会话只 `git add ledger handoff attempts` 并 commit，不 push/pull/切分支；**总控负责推送**（合并 PR 后 `git pull --rebase` 再 `git push`）。 | 主 checkout 由总控与学习会话共用 |
| D6 | T11 | 草稿图片放 `work/tmp/figures/`（已 gitignore）。辅助脚本留在 `skill/cie-9618-cs-tutor/scripts/`，总控以后补冒烟测试。 | — |
| D7 | T10 | `tools/testkit.py` 新增 `output_lines(text)`（规则同 `ScriptResult.lines`），供 `io`/`trace` 型测试配 `capsys`。 | 避免每个测试各写一份 |
| D8 | T10 | **技能标签只有一份词表**：T21 以 `ladder/design.md` §7.8 为种子合并进 `papers/p2/skill_tags.json`（不做映射）；之后阶梯与 P2/P4 练习的 `meta.skills`、行的 `markpoints[].skills` 都取自它（P4 用 `extends`）。 | 失分技能要跨阶梯与真题统计 |
| D9 | T10 | `ledger/ladder.csv` 的「优先级」列一律 `★★★`（全部必修）。 | 阶梯无构建统计 |

## 2026-10-16 · T10 批 2 审查

| # | 来源 | 决定 | 依据 |
|:--|:--|:--|:--|
| D10 | T10 | P4 批改与教学口径：①数组要建出真实 list 并注释大小与类型（只写注释或空 list 不给声明分）；②题目给了指针初值就照题目用；③题目要求写算法时不用 `in`、`sort()`、`index()`、`max()` 等内置函数代劳。已写进 skill `references/programming.md` §8。 | ER s23 9618/41 Q3 p.39；ECR P4 2021 p.39 |
| D11 | T10 | T14 照抄规格里的数据文件：规格中的 `·` 表示普通空格；规格注明「最后一行不换行」的文件（如 L07 `trailing.txt`）必须不以换行结尾。 | 文件内容决定测试结果 |

## 2026-10-16 · T12 P1 / T14 批 1 审查

| # | 来源 | 决定 | 依据 |
|:--|:--|:--|:--|
| D12 | T14 审计 | 调用无参过程统一写 `CALL Beep()`（指南 p.22 正式语法、p.23 示例）；p.19 原例省略括号，卡片注明即可。T10 在批 3 PR 里顺手改 L02 card:130。 | 指南内部不一致，取正式语法 |
| D13 | T14 | io 型练习的提示语必须写在 `input("…")` 里；先 `print` 提示再 `input()` 会多出输出行导致测试失败。学习时遇到这种失败，导师先解释此规则，不算逻辑错误、不记错误类别。 | `feed_input` 不打印提示语；design.md §7 |

## 2026-10-16 · T20 / T12 P2 / T14 批 2 / T10 批 3 审查

| # | 来源 | 决定 | 依据 |
|:--|:--|:--|:--|
| D14 | T20 | 行的 `types.cross` 是「副题型」：同章、跨章都可以（构建器不区分）。 | 位运算表里混 LSL 等同章组合真实存在 |
| D15 | T20 | **逻辑门独立成章 `LG`**（原 HW-10…HW-15 → LG-01…LG-06），T24 开工前改完。 | 每卷必考、套路与硬件描述题不同，单独成章便于学与统计 |
| D16 | T12 | `9618_w22_22:1(c)`：MS 复述表达式时误印 `Count >= 99`，QP 为 `Count >= 29`；以 QP 为准讲解，给分按 MS 的答案（FALSE，两种写法结果相同）。 | QP p.3 / MS p.3 原页 |
| D17 | T12 | `9618_w25_23:3`：QP 与 MS 都把类型名 `PopData` 当变量用（应为 `ThisPop.Exists`/`ThisPop.Data`），按官方笔误处理：教学用 `ThisPop.<字段>`，并向学生说明原卷的笔误；按 MS 其余得分点给分。 | QP p.6 / MS p.7 原页 |
| D18 | T14 审计 | L06 card.md:182 的 E02 目录描述与规格不符，改为「找到就停；并行数组里返回分数（找不到返回 -1）」，由 T10 在批 3 PR 一并修改。 | 规格为准 |

## 2026-10-16 · 云端额度

| # | 来源 | 决定 | 依据 |
|:--|:--|:--|:--|
| D19 | 学生 | 云端会话额度（$100，11 月 5 日过期）用于只靠仓库内容就能完成的任务，模型 **Opus 5.5、effort high**；**预留一部分给最后一轮 Fable 5.1 的最终审查与优化，不要用完**。云端会话看不到 `sources/`。首个云端任务：T22。 | 学生选择；Fable 5.1 单价约为 Opus 5.5 的 2.5 倍 |

## 2026-10-16 · T21 / T14 批 3 审查

| # | 来源 | 决定 | 依据 |
|:--|:--|:--|:--|
| D20 | T21 | 技能标签 `declare-constant` **改名为 `declare-variables`**（含义：声明局部变量与常量），在 P2 打标签开始前由总控一次性改完：`papers/p2/skill_tags.json`、`papers/p2/pilot_markpoints.jsonl`、`papers/p2/tagging-guide.md`、`ladder/design.md` §7.8、阶梯各 `meta.json`。 | P2 MS 最常见的是 “Declare local variables”，旧名误导打标签 |
| D21 | T21 | `9618_s21_23`、`9618_w21_23` 与同季 `_21` 卷逐题相同的 37 行补 `equivalent_of`，由 codex-1 在 T12 的后续 PR 用 `overrides.json` 补齐；补齐前 P2 打标签照抄 `_21` 卷。 | 只有 5 行已标 |
| D22 | T21 | `ladder/design.md` §6 回填 P2 题型码（T21 PR 描述第 3 项的对照）——由 T10 跟进。 | 阶梯与题型衔接 |
| D23 | T21 | `skill/cie-9618-cs-tutor/scripts/rows.py` 用系统 python3 运行时，缺 PyMuPDF 就自动改用 `~/.venvs/alevel-cs/bin/python` 重新执行（总控改）。 | `render` 依赖 PyMuPDF |
| D24 | T14 审计 | 伪代码里的数组一律用**带上下界的全局声明**（真题写法，如 `ARRAY[1:200] OF Node`），不用无界的 `ARRAY OF INTEGER` 参数。L11/E03 的规格与模板由 T10 改成全局数组，`answer.pseudo` 由总控同步。 | 真题 P2 全部是带界全局数组；指南无无界参数写法 |
| D25 | T14 审计 | 不依赖 `AND` 短路：链表遍历等写成标志变量或分层判断。L10/E03、E04 的人工核对清单由 T10 改，与 L11 card:115 一致。 | 指南未保证短路求值 |

## 2026-10-17 · 抽取乱码（T22 批 B 发现）

| # | 来源 | 决定 | 依据 |
|:--|:--|:--|:--|
| D26 | T22 批 B | PDF 抽取把 Symbol/Wingdings 字形留成私用区字符（P2 的伪代码赋值箭头 812 处、项目符号、打勾等）。对照表：U+F0AC/U+F0DF→`←`，U+F0B7/U+F09F→`•`，U+F0FC/U+F050→`✓`，U+F0B1→`±`，U+F0B4→`×`，U+F0A1→`○`，U+F03C→`<`，U+F03E→`>`，U+F02D→`−`，U+F020→空格。①`tools/check.py` 的引文比对已按此表归一（新旧文本都能核对）；②codex-1 的 T12c 在抽取环节按此表改写 `stem`/`stem_ctx`/`ms_text`，**在 T28 合并之后**做，并用 T24/T28 的 apply 脚本重新套上标签与得分点（得分点 `text` 同样按表改写）。表外的私用区字符必须看原页确定后再加入，不得猜。 | 逐个渲染原页核对：w24/23 MS p.8、w22/12 MS p.9、s22/21 QP p.14、s25/23 QP p.14 |

## 2026-10-17 · T28 审查

| # | 来源 | 决定 | 依据 |
|:--|:--|:--|:--|
| D27 | T28 | 技能词表缺「普通变量赋值」「滚动缓存/数组移位」：由 T23 设计工位提出新标签，总控合并后由 codex 回填 `skill_tags.json` 与相关 markpoints。`9618_w21_22:2(a)`（MS 按流程图框给分、框内文字未抽取）按 §8.2.9 例外不拆。 | T28 报告 |
| D28 | 学生 | 云端额度余 $70（2026-10-17）：P2 题型卡分 2 批在云端做（预计约 $20），其余保留给最终的 Fable 5.1 审查。 | D19 |

## 2026-10-17 · T23 批 A / T12 P3 审查

| # | 来源 | 决定 | 依据 |
|:--|:--|:--|:--|
| D29 | T12 P3（#22） | 扩充 D26 对照表：U+F0F0（Wingdings）→`⇨`，U+F0A5（Symbol）→`∞`。`tools/check.py` 已加入；codex-1 在抽取归一步骤里同样加入，并重跑 P3（P1/P2 无这两个字符）。 | 渲染原页核对：s24/31 MS p.4（补码换算步骤之间的箭头）、w25/33 MS p.12（Dijkstra「其余结点设为 ∞」） |
| D30 | T23 批 A（#23） | 采纳 D27 的两个新技能标签，已写入 `papers/p2/skill_tags.json`（v1.1）：`assign-value`（data，普通赋值）、`shift-values`（algorithm，滚动缓存 / 数组移位）。回填由 codex-1 在 `pipeline/tag/p2/p2_markpoints.jsonl` 做后重新套用：`9618_w21_22:6(d)` MP6、`9618_w23_21:6(a)` MP5 → `assign-value`；`9618_s22_22:4(a)` MP5、MP6 → `shift-values`（均替换现在暂用的 `initialise-variables`）。其他疑似行只列进 PR 由总控裁决，不自行改。 | T23 PR #23 提议；逐条看过四个得分点原文 |

## 2026-10-17 · T25 批 1 审查

| # | 来源 | 决定 | 依据 |
|:--|:--|:--|:--|
| D31 | T25 批 1（#24） | 真题练习里 QP 要求与 MS 范例代码在边界情况上不一致时：**Python 自动测试按 QP 的要求判**（参考解、边界测试都按 QP）；**伪代码人工批改按该题 MS 的得分点给分**（范例代码不是得分点，学生写成范例那样不扣分）；`task.md` 的「Python 接口」写明差异与原因。另：测试不得替学生在 QP 未定义的地方做选择（如“同月”是否要求同年、输出是否带说明文字）——QP 未定义的边界不测，或在 `task.md` 写明约定后再测。 | 渲染原页核对：s24/22 MS p.9（6(a) 范例在剩余 13 字符时多删一词、首词 13 字符时删空越界）、s24/22 MS p.11（8(b) 范例对全空格行原样返回）、s25/23 MS p.12（7(a)(i) 只比 MONTH） |

## 2026-10-17 · T23 批 B 审查

| # | 来源 | 决定 | 依据 |
|:--|:--|:--|:--|
| D32 | T23 批 B（#25） | 补充 D2：考官报告（ER）说某种非指南写法“也拿了分”、但该题 MS 没有显示接受的（如 `IF … ELSEIF`），仍按 D2 不教、批改时不默认给分；可以在卡的“易错与失分”里提一句 ER 的说法并注明出处。给分只认该题 MS（AGENTS.md §5）。 | ER s22 9618/21 Q6(b) p.13 与 9618_s22_21:6(b) 的 MS 对照 |

## 2026-10-17 · T27 / T30 审查

| # | 来源 | 决定 | 依据 |
|:--|:--|:--|:--|
| D33 | T27（#26） | 考官报告摘录的挂行规则：①ER 印错按修正表处理并在条目里保留原印标签——w23 第一个 `Paper 9618/33` 块当作 31（`HEADING_FIXUPS`），s24_22 Q1 第二个 `(b)` 当作 1(c)（`LABEL_FIXUPS`，`er_label_printed`）；②行没有子行、且 ER 在该行下只有唯一一个更细标签时挂上，正文前加范围前缀 `[ER 6(a)]`；③上级总评与每卷 Key messages / General comments 只留在 `corpus/er/`，不挂到已有本级评论的行，skill 需要时自己读；④s25_42 Q3 重复的 (d)(ii) 等 P4 行入库后再定。`pipeline/extract` 与 `pipeline/tag` 的改动必须保留行的 `er` 字段。 | ER 原页核对：w23 p.25 / p.31 两块都印 33、无 31 标题；s24 p.17 第二个 (b) 内容为“怎样记录变量”（1(c)） |
| D34 | T30（#27） | P3 题型体系定为 **9 章 79 型**：考纲 15.2 布尔代数与逻辑电路单独成 `BL` 章（同 D15）；卡诺图分 BL-05 填写、BL-06 圈组与化简两型；FP-01 编程范式、SY-05 解释器因考纲独立要求保留；RISC/CISC 中断并入 HV-02，内核与低级调度并入 SY-03；得分点只拆指南 §8 所列写代码 / 类图题型，汇编、Prolog、BNF、语法图、电路不拆。新建 `papers/p3/skill_tags.json`（`extends` P2 词表，D8），收入 `random-file`、`user-defined-type` 两个新标签。 | T30 试标 3 卷 81 行全有主题型、低信心 0；2027–29 考纲 13–20 节与 2026 版逐行相同 |
| D35 | T30（#27） | P3 有 **119 行**与同季 `_31` 卷同题号逐字相同（题干与 MS 压缩空白后相同）却没有 `equivalent_of`：多为带图行（抽取器对图形行保守不判重）。由 codex-1 在 T12 后续 PR 里核对 QP 图形也相同（渲染原页比对）后，用 `pipeline/extract/overrides.json` 补 `equivalent_of`（同 D21）；图形不同的行不补并列出。补齐前 T31 打标签对这些行照抄 `_31` 卷的标签。 | 总控复核：s21_32 14、s21_33 14、w21_32 15、s22_33 9、s23_33 15、s24_33 12、w22_33 14、w23_33 10、w24_33 16 |
| D36 | 总控（#29 合并后） | P4 行入库后重跑 `apply_er.py`：P4 新挂 653 行，全语料 2938 / 3302 行带 `er`。D33 ④ 定案：s25 ER Paper 42 Q3 第二个 `(d)(ii)`（p.46，“generate the correct outputs … showing the updated values”）即 3(d)(iii) 测试截图，加入 `LABEL_FIXUPS`。T12d 回填的其余关键词候选（52 条）不扩大回填：现有标签抓的是各点主要技能。 | ER 原页 p.46；`9618_s25_42:3(d)(iii)` 题干为 Test your program / screenshot |

## 2026-10-17 · T25 批 2 / T12e 审查

| # | 来源 | 决定 | 依据 |
|:--|:--|:--|:--|
| D37 | T25 批 2（#30） | ①`9618_s23_21:8(b)` MP5「… OR when ThisItemNum < NewItemNum」指范例 WHILE 的第三个条件：Stock.txt 按 ItemNum 升序，读到的编号越过新编号即可提前结束；人工批改时循环含这层判断就给分，写成继续条件 `<` 或结束条件 `>` 均可。②`markpoints[].n` 是语料拆分顺序，可能与 MS 印的 MP 编号不同（如 `9618_w25_21:8(a)`：语料 MP5/MP6 拆自 MS MP5，语料 MP7 = MS MP6）；练习与题型卡在不一致处列出对照，语料不改。③LastLines 的 `shift-values` 已由 T12d（#28）回填，无需处理。 | s23/21 MS p.10；T12e（#31）119 行 equivalent_of 已合并（D35 完成） |
| D38 | 总控 | P2-AD-06（用文字描述算法、不写伪代码）的真题练习：`meta.pseudocode = false`，作答模板为 `answer.steps.md`（编号步骤，英文一句一步），人工清单逐点按 MS；同时写同一算法的 Python 并自动测试（`starter.py` / `test_task.py` 照常）。AD-05（流程图 → 伪代码）照常用 `answer.pseudo`。原题算法无法自动测时（只问“怎样用某数组”这类）不硬造测试，列进 PR「需要总控决定」。 | T25 批 3 规划；`schemas/exercise-format.md` 已加 `answer.steps.md` |
