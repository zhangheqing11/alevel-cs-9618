# T26c · P1 手册审计修正记录

执行：codex-1；日期：2026-10-17；基线：`d73f9deac50890657c40a4f13c22059c3b993883`（D40）。

F01–F13 按 `T26-findings.jsonl` 行序，已处理 error 10、warn 3。下列行号为本次修正后源文件行号；路径均相对于 `papers/p1/`。

## 逐条处理

| 编号 | 级别 | 文件与行 | 改动摘要 |
|:--|:--|:--|:--|
| F01 | error | `cards/CM.md:145`；`cards/CM.md:179` | 用内嵌 SVG 重画星型图；4 台计算机、2 台打印机、服务器、路由器各有一条线直接接中心交换机。 |
| F02 | error | `cards/EO.md:261`；`cards/EO.md:279` | 在学习影响中补入错误答案导致错误信息；学习、人际交流两项影响各覆盖两个独立 bullet，新增逐点对齐表，明确 // 不累计给分。 |
| F03 | error | `core/PF.md:19` | ACC 改称专用寄存器，保留功能描述与 MS 引文。 |
| F04 | error | `core/DB.md:31` | 按 D40 改名为 No partial dependencies（2NF 条件），同步中文和直观；英文 MS 原句保留。 |
| F05 | error | `core/DB.md:33` | 按 D40 改名为 No non-key / transitive dependencies（3NF 条件），同步中文和直观；英文 MS 原句保留。 |
| F06 | error | `cards/SP.md:369` | 把偶数位翻转的局限限定到同一字节的单字节检查，另解释同一行两列出错仍会改变列奇偶，块校验能发现。 |
| F07 | error | `cards/DB.md:195`；`cards/DB.md:246`；`cards/DB.md:259`；`cards/DB.md:532`；`cards/DB.md:810` | 补外键可重复才据此判多端；唯一或兼主键时按约束判 1:1。同步 DB-03、DB-04、章末辨析及级联删除处同类表述。 |
| F08 | error | `cards/DB.md:145`；`cards/DB.md:159` | 明确主键从候选键中选择且仍属候选键；只在 another / other 或未选中限定下排除主键。 |
| F09 | error | `core/PF.md:43` | 先讲逐位移动与补零，再补无符号左移未丢有效位、右移除后向下取整条件。 |
| F10 | error | `cards/EO.md:135`；`cards/EO.md:138`；`core/EO.md:15` | 再发布按具体许可证条款；相同许可或自由要求仅限相应 copyleft 许可。同步对照表两个自由/开放许可栏及 core。 |
| F11 | warn | `cards/PF.md:463` | 指令表与程序改指 QP p.10，跟踪表 p.11，设问 p.12。 |
| F12 | warn | `cards/PF.md:597` | 按 D40 保留完整表，注明 MS 省略不改数据的 205、211 两行；按阴影分组核数，不称逐行一致。 |
| F13 | warn | `cards/IR.md:17` | 移除无统计口径的“一半”比例，改为定性说明。 |

F04/F05 在审计给出的两个选项中执行 D40 指定的词条改名方案，未改写英文得分句。F12 直接执行 D40；其余按 suggestion 修正。未改语料、题型体系、练习与原始资料；历史审计 findings、coverage 和脚本保留。

## error 改后原文片段

以下摘自修正后的源文件；F01 仅截取路由器连线、中心节点和标签，其余七条线同样终止于交换机中心 `(340, 150)`。

### F01

```xml
    <line x1="595" y1="245" x2="340" y2="150" />
    <rect x="280" y="125" width="120" height="50" />
    <text x="340" y="156" text-anchor="middle" font-family="Helvetica" font-size="15">SWITCH</text>
    <text x="595" y="273" text-anchor="middle" font-family="Helvetica" font-size="15">Router (internet)</text>
```

### F02

**完整作答**
- 影响 1（学习）：学生用 AI 走捷径，可能错过培养推理和解决问题能力的机会；AI 的答案也可能不正确，导致学生接触错误信息。
- 影响 2：过度依赖 AI 会减少协作、团队合作和面对面交流的机会，对学生的沟通能力不利；屏幕时间增加、更孤立，可能加重焦虑或孤独。
- （其他可选要点：凸显数字鸿沟——有的学生用不上这些技术；正面的：获得额外帮助的学生可能学得更好。）

**与 MS 对齐**　MS p.13 每个 bullet 1 分、封顶 4 分；上面的两项影响覆盖以下 4 个独立 bullet：

| 作答位置 | 对应 MS 原文 | 分值 |
|:--|:--|:-:|
| 影响 1：错过能力培养 | 「If students use AI to shortcut learning, they may miss out on developing reasoning and problem-solving skills」⟦9618_w25_11:8(c)⟧ | 1 |
| 影响 1：错误答案造成错误信息 | 「The AI answer might not be correct leading to mis-information」⟦9618_w25_11:8(c)⟧ | 1 |
| 影响 2：交流与协作减少 | 「heavy reliance on AI may limit opportunities for collaboration, teamwork, and face-to-face communication」⟦9618_w25_11:8(c)⟧ | 1 |
| 影响 2：焦虑或孤独 | 「Increased screen time and isolation could contribute to anxiety or loneliness」⟦9618_w25_11:8(c)⟧ | 1 |

第一行所在 bullet 中的 not learning / decline in skills 是替代表述，不能另计分。

**英文作答句**　1. If students use AI to shortcut their homework, they may miss out on developing reasoning and problem-solving skills. AI answers may also be incorrect, leading to misinformation. 2. Heavy reliance on AI may limit opportunities for collaboration, teamwork and face-to-face communication. Increased screen time and isolation could contribute to anxiety or loneliness.


### F03

```text
| Accumulator (ACC) | 「holds the result of a calculation」⟦9618_w25_11:6(a)⟧ | 存放算术与逻辑运算（中间）结果的专用寄存器 | 计算器的显示屏 | P1-PF-02、P1-PF-09 |
```


### F04

```text
| No partial dependencies（2NF 条件） | 「Each field is fully dependent on the corresponding primary key // no partial dependencies」⟦9618_s22_11:4(b)⟧ | 不存在部分依赖：每个非键属性依赖整个主键，而非复合主键的一部分 | 若复合主键是学号与考试号，就不能把只由学号决定的学生名留在这张表 | P1-DB-05 |
```


### F05

```text
| No non-key / transitive dependencies（3NF 条件） | 「no non-key dependencies // no transitive dependencies」⟦9618_w22_11:4(b)⟧ | 不存在非键（传递）依赖：非键属性不依赖其他非键属性 | 若售价只由品种决定，就把品种与售价另存一表，不留在以批次为主键的表中 | P1-DB-05、P1-DB-06 |
```


### F06

```text
4. 奇偶校验的局限：**同一字节内偶数个位翻转**，该字节的奇偶性不变，可能绕过单字节奇偶检查。块校验还检查各列：同一行的两列各翻转一位时，行奇偶虽不变，两列的奇偶都会改变，仍能发现错误；不能把“两位必漏检”套到块校验。
```


### F07

```text
1. **判断度数**：结合外键与题目约束。B 表里有 A 表的主键作外键，且该外键值允许重复 → A 对 B 是 **1:M**（一个 A 对应多个 B，每个 B 只属于一个 A）。题目问“B 和 A”时顺序反过来写成 **M:1**；若该外键唯一或同时为 B 的主键，则结合约束判断为 **1:1**，不能仅凭外键位置断定“多”端。
```

```text
2. 外键值允许重复时，外键所在的表是“多”端，被引用的表是“一”端；若外键唯一或同时为主键，结合题目约束判断为 **1:1**。
```

```text
- 鸦爪画在错的一端：**1:M 关系中**，鸦爪在外键可重复的表一端；外键唯一的 **1:1** 关系不画鸦爪。
```

```text
- 级联删除方向写反：删除被引用表中主键对应的记录，连带删除引用它的外键记录；在 1:M 关系中，即从“一”端删到“多”端。
```

```text
| 外键所在表 vs 外键引用的表 | 外键可重复时，所在表是“多”端、被引用表是“一”端；外键唯一或同时为主键时，结合约束判 1:1 | the table each is found in 还是 references；是否允许重复 |
```


### F08

```text
3. **找候选键**：找能唯一标识每条记录的属性或属性组合（如卡号、序列号、邮箱，须以题目约束为准）。主键从候选键中选择，已选主键仍是候选键；只有题目要求 another / other 或未被选为主键的键时，才排除已选主键。
```

```text
- 把主键排除出候选键：主键本身仍是候选键；只有题目明确要求 another / other 或未选中的键时，才须找主键以外的候选键。
```


### F09

```text
| Logical shift | 「A logical shift moves all bits to the right and inserts zeros in the appropriate leftmost bits」⟦9618_w24_13:8(c)⟧ | 所有位整体移动，移出的丢弃，空位补 0；对无符号数，左移 n 位仅在未丢失有效位时等于 ×2ⁿ，右移 n 位等于 ÷2ⁿ 后向下取整 | 队伍挪座位，空座坐“0” | P1-PF-11 |
```


### F10

```text
| 能否再发布 | 不能 | 试用版可以传播 | 能，遵守具体许可证条款 | 能，遵守具体许可证条款 |
```

```text
只有采用要求保留相同许可或自由的 copyleft 许可证时，修改版再发布才受相应要求约束；不能把这种要求推广到所有开源或自由软件许可证。
```

```text
| Open Source Initiative (OSI) | 「Allows program source code to be examined」⟦9618_w24_12:5(b)(i)⟧ | 随程序提供源代码，允许修改和再发布，须遵守具体许可证条款；要求保留相同许可的限制取决于所用的 copyleft 许可证 | 公开的菜谱 | P1-EO-03 |
```


## 证据与校验

- F02 动笔前重读并渲染 `9618_w25_qp_11.pdf` p.14 与同卷 MS p.13。QP 要求两项社会影响；MS 为每 bullet 1 分、max 4。改后学习影响对应“能力培养”和“错误信息”两点；人际交流影响对应“交流协作”和“焦虑孤独”两点。中文完整作答、英文作答与对齐表一致。
- F01 重读 QP `9618_s25_qp_12.pdf` p.12，渲染 MS p.11 确认路由器直连 switch/server。构建后从 `output/p1/P1题型手册.html` 提取实际 SVG：8 条线全部终止于交换机中心，9 个设备标签唯一；用 PyMuPDF 渲染该 SVG 并人工确认连线、居中标签和边界。浏览器验证工具超时，未取得浏览器页面截图；HTML 已确认保留原始 SVG、可访问标题和响应式尺寸。
- F11 重读 `9618_s25_qp_13.pdf` p.10–12；F12 重读 QP `9618_s25_qp_11.pdf` p.15 并渲染 MS p.12，确认省略 205/211、四段阴影及各数值。F03/F07 另复核 `9618_w23_qp_11.pdf` p.9、`9618_w24_ms_12.pdf` p.7。其他修正使用已成立的 T26a 证据和 D40 裁决，未把教材、ER 或其他题的 MS 当作本题给分依据。
- `~/.venvs/alevel-cs/bin/python papers/p1/audit/check_handbook.py`：88 张卡、176 个代表题/变式入口，`pick_failures = []`；Python 块 0。
- 同脚本 `--validate`：预期拒绝，首项 `AssertionError: Changed input: papers/p1/cards/CM.md`。此模式校验 T26a 历史输入哈希，不能代表修正后内容；20 个历史哈希均另以 `git show origin/main:<path>` 核验通过，没有更新 coverage 去冒充重新全审。
- `make check`：通过（语料 3302 行、213 题型；引用及 MS 原文核对通过；练习代码无改动，changed-only 模式执行练习 0）。
- `make build`：通过；生成 P1/P2 手册与概念/对照表、Python 阶梯；P3/P4 按当前已有内容跳过。
- `make check-scope TASK=T26c`：通过；`git diff --check`：通过。

## 交付环境

主 checkout 的 `.git` 为只读，本次在 `/tmp/alevel-cs-T26c-git` 的独立 worktree `/tmp/alevel-cs-T26c` 执行。终端访问 GitHub 失败（`Could not resolve host: github.com`）；通过 GitHub 连接器复核远端 main 仍为上述基线。终端 push 与 gh 均失败后，已用连接器发布同名分支并创建 PR #36（https://github.com/zhangheqing11/alevel-cs-9618/pull/36），未合并。前三次远端提交的 tree SHA 均与本地对应提交完全一致。

需要总控决定：无新增内容裁决；浏览器页面级视觉复核尚未完成，已以构建后 SVG 的直接渲染和结构检查代验。
