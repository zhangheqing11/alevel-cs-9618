## SD　软件开发 {#ch-SD}

<!-- auto:chapter-stats -->

### 核心思想

SD 章讲一个程序“从提出需求到交付以后”的一生，考纲 12.1–12.3。12 个题型分四块：

1. **开发生命周期**（SD-01、SD-02）：分析、设计、编码、测试、维护五个阶段各做什么、各产出什么文档；瀑布、迭代、RAD 三种模型的原理与优缺点。
2. **设计图**（SD-03、SD-04）：结构图（模块之间谁调用谁、传什么参数、选择与重复）；状态转换图（状态、事件、输出）。都是“按表格或说明画图”与“按图填表”两个方向。
3. **读代码、找错**（SD-05 至 SD-08）：错误的三种类型与 IDE 调试工具；在给定伪代码里找出错误并改正；按调用逐行干跑、填追踪表；解释一段代码的作用、某分支为何永远不执行、某初值为何这样选。
4. **测试与维护**（SD-09 至 SD-12）：测试方法（走查、白盒、黑盒、集成、桩、alpha、beta、验收）；选测试数据（正常、异常、边界）；三种维护；需求变化后怎样改程序。

整章有一条主线：**每个阶段都有固定的“动作 + 产出”，每种测试和维护都有固定的“谁做 + 什么时候 + 为了什么”。** SD 章的大多数题是 1–3 分的短答，MS 的得分句高度固定（stub、integration、adaptive 每次都是那几句），把本章“得分表述”默写下来，就能稳拿。只有两类题需要动手：画结构图 / 状态转换图（SD-03、SD-04），干跑填追踪表（SD-07），这三型分值高、套路也固定。

### 本章速查

| 阶段 | 做什么 | 产出（MS 常见） |
|:--|:--|:--|
| Analysis 分析 | 调查现有系统、访谈客户、可行性研究、明确问题 | requirements specification、problem definition、feasibility study |
| Design 设计 | 定数据结构、算法、模块结构、界面、测试计划 | identifier table、structure chart、flowchart / pseudocode、state-transition diagram、test plan |
| Coding 编码 | 用程序语言实现算法，在 IDE 里编写、编译 | 程序代码；可能出现 syntax errors |
| Testing 测试 | 干跑、走查、白盒 / 黑盒、集成、alpha、beta | trace table、测试结果 |
| Maintenance 维护 | 交付后改正、适应、完善 | 修改后的程序 |

| 测试 | 谁 / 何时 | 一句话 |
|:--|:--|:--|
| Dry run / walkthrough | 开发者，看代码 | 逐行执行、填追踪表，看变量值和路径是否符合预期 |
| White-box | 开发者，看得到代码 | 用测试数据走遍程序里的每条路径 |
| Black-box | 不看代码 | 只比较输入与预期输出 |
| Integration | 模块各自测过之后 | 把已测试的模块组合起来作为整体测试 |
| Stub | 有模块还没写好 / 有错 | 用只返回固定值或输出一句话的简单模块代替它 |
| Alpha | 开发方内部 | 发布前在公司内部测试 |
| Beta | 一小群真实用户 | 在真实环境中使用并反馈问题 |
| Acceptance | 客户 | 交付前由客户确认满足需求 |

| 维护 | 原因 |
|:--|:--|
| Corrective 纠正性 | 程序有错，不按预期工作 |
| Adaptive 适应性 | 需求、技术（新硬件、新库）或法规变了 |
| Perfective 完善性 | 程序没错，但要更快、更好用 |

### 题型树
<!-- auto:type-tree -->

### P2-SD-01　开发生命周期的阶段与活动　{#P2-SD-01}

<!-- auto:stats P2-SD-01 -->

**考法**　①表格：每行一个开发活动，写出它属于哪个阶段（每行 1 分，4–5 分）；②说出设计阶段要做的三件事（3 分）；③说出分析阶段产出的一份文档；④说出改正已发布程序的错误属于哪个阶段；⑤生命周期的一个好处；⑥选编程语言时要考虑什么。

**识别信号**　program development life cycle；Complete the table by writing the name of the life cycle stage for each activity；State three activities that will take place during the design stage；State one document that may be produced from the analysis stage；Identify the stage …；State one benefit of a development life cycle。

**解题思路**
1. **五个阶段的顺序**：Analysis → Design → Coding → Testing → Maintenance。阶段名用这五个词，不要写 planning、implementation 之外的自造词（Coding 也可写 Implementation）。
2. **按动词定阶段**：
   - 访谈客户、调查现有系统、可行性研究、写需求说明 → Analysis。
   - 定义数据结构 / 记录 / 文件结构、画结构图或流程图、写伪代码、做标识符表、设计界面、制定测试计划 → Design。
   - 用编程语言实现算法、用编译器、IDE 自动补全、出现语法错误 → Coding。
   - 走查、干跑、填追踪表、白盒 / 黑盒测试 → Testing。
   - 发布后改错、让程序适应新硬件 → Maintenance。
3. **设计阶段的活动**：选数据结构、写算法（流程图 / 伪代码）、定模块结构、设计界面、定测试方法与测试计划、选编程语言或开发环境——写三条，每条扣情境（网站 → 网页布局）。
4. **分析阶段的文档**：requirements specification（需求说明）、problem definition；也可以是可行性研究报告、访谈记录。
5. **生命周期的好处**：更容易管理、计划和估算成本；每个阶段结束都有明确的交付物。

**得分表述**（引自对应 MS）
- 「Easier to manage/plan/cost // Clear deliverables produced at (end of) each stage」⟦9618_w22_23:1(b)(i)⟧
- 「Requirements specification // Client requirements」⟦9618_w22_23:1(b)(ii)⟧
- 「Algorithms / flowcharts / pseudocode」⟦9618_w21_22:2(b)(ii)⟧
- 「Testing method / Test plan / Test data / Trace tables」⟦9618_w24_22:7(c)⟧
- 「(Corrective) Maintenance」⟦9618_w24_22:1(a)⟧
- 「Which programming language would best suit the problem being solved」⟦9618_s25_22:1(a)(ii)⟧

**易错与失分**
- 标识符表、记录结构、测试计划写成 Coding / Testing：它们是**设计**出来的，属于 Design（⟦9618_s22_22:1(b)⟧ 标识符表 → Design）。
- “程序改到能在新硬件上运行”写成 Coding：发布以后的修改都是 Maintenance。
- “用编译器”写成 Testing：编译是 Coding 的一部分。
- 设计阶段的活动写成“写代码”“测试程序”：那是后面的阶段。
- 分析阶段的文档写成“伪代码”“结构图”：那是设计阶段的产出。

#### 代表题精讲　⟦9618_w24_21:5(a)⟧

**在考什么**　五个开发活动，写出各自所属的生命周期阶段。每行 1 分，共 5 分。

**完整作答**
| 活动 | 阶段 |
|:--|:--|
| The walkthrough method is used. | Testing |
| An algorithm is implemented in a programming language. | Coding |
| The client is interviewed about problems with the current system. | Analysis |
| The program is modified to run on new hardware. | Maintenance |
| Records and file structures are defined. | Design |

**与 MS 对齐**　MS 五行依次是 Testing、Coding、Analysis、Maintenance、Design，「One mark per row」⟦9618_w24_21:5(a)⟧。

**英文作答句**　（本题答案即上表。）

**直观**　盖房子：先问业主要什么（分析），再画图纸（设计），然后施工（编码），验收检查（测试），住进去以后修修补补、改造升级（维护）。

**下一道变式**　⟦9618_w24_22:7(c)⟧　（设计阶段要做的三件事，结合给定情境：发邮件的新模块。）

<!-- auto:drills P2-SD-01 -->

### P2-SD-02　生命周期模型　{#P2-SD-02}

<!-- auto:stats P2-SD-02 -->

**考法**　①RAD 的一条原则（1 分）；②与瀑布模型相比，RAD 的两个好处和一个缺点（3 分）；③瀑布模型为什么不适合某情境（2 分）并说出更合适的模型（1 分）；④补全瀑布模型图（阶段名与上下箭头，3 分），解释向下、向上箭头的含义（2 分）；⑤说出另一种生命周期模型；⑥为什么需要不同的生命周期 / 选择时考虑什么。

**识别信号**　Rapid Application Development (RAD)；waterfall；iterative；State one principle of this life cycle；Give two benefits and one drawback … compared to the waterfall life cycle；Give two reasons why this may not be the most appropriate model；downward and upward arrows；Identify another type of model。

**解题思路**
1. **瀑布（waterfall）**：各阶段按顺序进行，一个阶段完成并交出结果才进入下一个；向下箭头 = 上一阶段的结果作为下一阶段的输入；向上箭头 = 发现问题时回到前一阶段补做。缺点：到后期才有能用的软件；需求变化难以应对。适合需求清楚、稳定的项目。
2. **迭代（iterative）**：先做一个简单版本，再一轮轮分析 → 设计 → 编码 → 测试，每轮增加功能；早期就有可用版本。
3. **RAD**：模块并行开发、做原型（prototype）、很少详细规划、客户全程参与反馈、小步发布。好处：开发快、早有原型、容易改需求、客户与开发者合作紧；缺点：难估计成本和时间、文档常被省略、需要客户随时有空。
4. **选模型**：需求可能变、要尽早给客户看原型、要快速上市 → RAD / 迭代；需求明确、项目稳定 → 瀑布。理由一定扣情境（网站要尽快上线、校长要先看原型）。

**得分表述**（引自对应 MS）
- 「Small incremental releases are made, each adding functionality」⟦9618_w22_23:1(c)(i)⟧
- 「Prototype produced (at early stage in process)」⟦9618_w22_23:1(c)(ii)⟧
- 「Difficult to estimate cost / time to complete project」⟦9618_w22_23:1(c)(ii)⟧
- 「No working software until late in the life cycle so slower to market than competitors」⟦9618_s23_21:5(a)(i)⟧
- 「Downward arrows: result from one stage is input / passed to the next」⟦9618_s22_23:8(b)⟧
- 「Upward arrows: more work is required at a previous stage to complete the current stage」⟦9618_s22_23:8(b)⟧

**易错与失分**
- 好处、缺点不“与瀑布比较”：题目说 compared to the waterfall life cycle，好处要是瀑布没有的（早有原型、易改需求）。
- RAD 的缺点写成“质量差”“不安全”：MS 要的是难估成本 / 时间、文档少、要求客户一直参与。
- 画瀑布模型时中间三个阶段顺序写错（Design → Coding → Testing），或每对阶段之间只画了一个方向的箭头。
- 向上箭头写成“返回上一步重新开始”：是“回到前一阶段补做工作，才能完成当前阶段”。

#### 代表题精讲　⟦9618_w22_23:1(c)(ii)⟧

**在考什么**　购物网站将用 RAD 生命周期开发。Give two benefits and one drawback of its use compared to the waterfall life cycle. 3 分（好处最多 2 分，缺点最多 1 分）。

**完整作答**
- Benefit 1: A prototype is produced at an early stage, so the client can review it early.
- Benefit 2: It is easier to change the requirements, because modules are developed in parallel and released in small increments.
- Drawback: It is difficult to estimate the cost and the time to complete the project.

**与 MS 对齐**　两个好处对应「Prototype produced (at early stage in process)」⟦9618_w22_23:1(c)(ii)⟧ 与「Easier to change requirements / quicker delivery of usable modules」⟦9618_w22_23:1(c)(ii)⟧；缺点对应「Difficult to estimate cost / time to complete project」⟦9618_w22_23:1(c)(ii)⟧。MS 另列了 Quicker development possible、Documentation often omitted 等，任选。

**英文作答句**　Compared with the waterfall model, RAD produces a prototype early and makes it easier to change the requirements, but it is harder to estimate the cost and time of the whole project.

**直观**　瀑布像按图纸一次盖完整栋楼，盖好才能看；RAD 像先搭样板间让业主看、边看边改，快是快，但很难事先算准要花多少钱。

**下一道变式**　⟦9618_s22_23:8(b)⟧　（瀑布模型图：解释向下与向上箭头的含义，讲解时请对照原卷 QP p.12 的图。）

<!-- auto:drills P2-SD-02 -->

### P2-SD-03　结构图　{#P2-SD-03}

<!-- auto:stats P2-SD-03 -->

**考法**　①按模块说明表（谁调用谁、带什么参数、返回什么、选择还是重复）画完整的结构图（5–6 分）；②补全已画一部分的结构图（3–5 分），或按模块头画结构图；③解释菱形符号、弧形箭头符号的含义（2 分）；④说出结构图的用途（2 分）；⑤解释图中几个模块之间的关系。

**识别信号**　Draw a structure chart / Complete the structure chart；Explain the meaning of the diamond symbol / curved arrow symbol；Describe the purpose of a structure chart；Module name | Description 表（calls … followed by …；calls either … or …；repeatedly calls …）；pseudocode module headers。

**解题思路**
1. **画框与连线**：每个模块一个矩形框，写上模块名；调用者在上、被调用者在下，用直线相连。同一个调用者的被调模块从左到右按调用顺序排。
2. **选择**：“calls either A or B (determined when the program runs)” → 在调用者框的下沿画一个**菱形**，从菱形引线到 A、B。
3. **重复**：“repeatedly calls A followed by B” → 在调用者下方画一个**弧形箭头**，跨过通往 A、B 的连线。
4. **参数箭头**画在连线旁：向下的箭头 = 传入的参数；向上的箭头 = 返回值或传回的值；**同一参数下去又回来（双头箭头）= BYREF**。箭尾空心圆 = 数据，实心圆 = 标志（BOOLEAN）。每个箭头旁写上参数名。
5. **从模块头读信息**：`FUNCTION X(…) RETURNS …` → 有向上的返回箭头；`BYREF P : …` → 这个参数画成双向；没有参数的模块不画箭头。
6. **解释符号题**：菱形 = 选择，A 调用 B、C 中的一个（运行时决定）；弧形箭头 = 重复，A 反复依次调用 B、C。**把相关模块名全部写出**，并说清顺序——这是第二分。

**得分表述**（引自对应 MS）
- 「module relationships / hierarchy / selection / repetition // how a problem is broken down」⟦9618_s22_23:3(a)⟧
- 「the parameters that are passed between the sub-tasks / modules」⟦9618_s22_23:3(a)⟧
- 「Diamond applied to Mod-B only」⟦9618_s24_23:7(b)⟧
- 「Iteration arrow applied to Mod-C only」⟦9618_s24_23:7(b)⟧
- 「Means that Sync repeatedly calls Reset and (then) Enable」⟦9618_w24_21:7(b)⟧
- 「BYREF parameter to Update」⟦9618_w25_21:7(b)⟧

**易错与失分**
- 解释菱形时只写“selection”，不写出四个模块名（ER s24 9618/21 Q7(b)(i) p.15：多数考生认出了选择，却没有写全模块名）。
- 菱形或弧形箭头画错了位置：画在被调模块上，或画在了没有选择 / 重复的模块下（MS 写明 applied to Mod-B only）。
- 返回值画成向下的箭头，或 BYREF 参数只画了一个方向。
- 把函数的返回值也当成参数画下去；没有参数的模块也画了箭头。
- 同一层的被调模块顺序与“followed by”的顺序不一致。

#### 代表题精讲　⟦9618_s24_23:7(b)⟧

**在考什么**　七个模块的说明（讲解时请对照原卷 QP p.16 的表）：Mod-A 先调用 Mod-B 再调用 Mod-C；Mod-B 带参数 Par1、Par2，调用 Mod-D 或 Mod-E 之一（运行时决定），返回一个 BOOLEAN；Mod-C 带参数 Par1、Par3（Par3 按引用），反复依次调用 Mod-F、Mod-G；Mod-D 带 Par2；Mod-E 带 Par3，返回一个整数；Mod-F 带 Par3；Mod-G 带 Par3（按引用）。Draw a structure chart to show the relationship between the seven modules and the parameters passed between them. 6 分。

**完整作答**（矩形写成 `[ ]`，菱形 `<>`，弧形重复箭头 `(loop)`；`↓` 传入，`↑` 返回，`⇅` BYREF；BOOLEAN 返回箭头的箭尾画实心圆 `●`，INTEGER 返回画空心圆 `○`）

```text
                                [ Mod-A ]
                    ____________/       \____________
                   |                                 |
     ↓ Par1, Par2  |  ↑● (BOOLEAN)      ↓ Par1  ⇅ Par3 |
                   |                                 |
               [ Mod-B ]                         [ Mod-C ]
                  <>                              (loop)
             _____/ \_____                    _____/ \_____
            |             |                  |             |
     ↓ Par2 |      ↓ Par3 | ↑○ (INTEGER)     | ↓ Par3      | ⇅ Par3
            |             |                  |             |
        [ Mod-D ]     [ Mod-E ]          [ Mod-F ]     [ Mod-G ]
```

| 连线 | 画法 | MS 点 |
|:--|:--|:--|
| Mod-A → Mod-B（左）、Mod-A → Mod-C（右） | 先 B 后 C，Mod-A 下面不画菱形，也不画重复箭头；所有下层模块也须正确命名、连接 | MP1 |
| Mod-A → Mod-B | 向下 Par1、Par2；向上返回 BOOLEAN，箭尾按该题 MS 画实心圆标志 | MP2 |
| Mod-A → Mod-C | 向下 Par1；Par3 双向（BYREF） | MP3 |
| Mod-B 下方 | 菱形，引出 Mod-D、Mod-E | MP4 |
| Mod-B → Mod-D / Mod-E | Mod-D：向下 Par2；Mod-E：向下 Par3、向上返回 INTEGER（空心圆数据箭头） | MP6（与下层另一行合看） |
| Mod-C 下方 | 弧形重复箭头跨过通往 Mod-F、Mod-G 的连线（先 F 后 G） | MP5 |
| Mod-C → Mod-F / Mod-G | Mod-F：向下 Par3；Mod-G：Par3 双向（BYREF） | MP6（与下层另一行合看） |

**与 MS 对齐**　MS 六点：「All modules correctly labelled and interconnected」⟦9618_s24_23:7(b)⟧；「Parameters between Mod-A and Mod-B and return value from Mod-B」⟦9618_s24_23:7(b)⟧；「Parameters between Mod-A and Mod-C」⟦9618_s24_23:7(b)⟧；「Diamond applied to Mod-B only」⟦9618_s24_23:7(b)⟧；「Iteration arrow applied to Mod-C only」⟦9618_s24_23:7(b)⟧；「All parameters at lower level and return value」⟦9618_s24_23:7(b)⟧。上表七行说明对应六个得分点；两行下层参数共同覆盖 MP6，须合起来完整才得这一分。

**英文作答句**　（本题答案即上图。）

**直观**　结构图是公司的组织图加快递单：框是部门，线是“谁给谁派活”，箭头是派活时递过去、交回来的材料；菱形表示“二选一派给谁”，弧形箭头表示“这几件活反复轮着做”。

**下一道变式**　⟦9618_w25_21:7(b)⟧　（由六个模块头画结构图：参数、返回值、BYREF 都从模块头里读出来；讲解时请对照原卷 QP p.13。）

<!-- auto:drills P2-SD-03 -->

### P2-SD-04　状态转换图　{#P2-SD-04}

<!-- auto:stats P2-SD-04 -->

**考法**　①按“当前状态 | 输入 | 输出 | 下一状态”表补全状态转换图：加状态圈、加带标签的箭头、自环（4–5 分）；②按图补全输入 / 输出 / 下一状态表，每行 1 分；③给一串输入，写出最后的状态和输出次数；④写出从 S1 到 S4 状态变化最少的输入序列；⑤数图里的转换个数、带输出的转换个数、终止状态；⑥按文字说明画控制系统的状态图（温度低于 10 开加热、高于 20 关）。

**识别信号**　state-transition diagram；Complete the state-transition diagram；Complete the table to show the inputs, outputs and next states；Current state | Input | Output | Next state；START；Input-A | Output-W；the minimum number of state changes。

**解题思路**
1. **符号**：圆圈 = 状态（写 S1、S2…）；带黑点的 START 箭头指向初始状态；箭头 = 转换，从当前状态指向下一状态；箭头上写 `输入 | 输出`（没有输出就只写输入）；当前状态与下一状态相同 → 画一个从圆圈出发又回到自己的**自环**。
2. **表 → 图**：表的每一行画一条箭头，画完逐行打勾，一条都不能漏；同一对状态之间两个方向的转换要画成两条箭头。
3. **图 → 表**：从初始状态出发，按给定的输入一步步沿箭头走；“下一状态”就是下一行的“当前状态”；没有输出写 none。
4. **最短序列**：从起点往终点找经过箭头最少的路径，写出路径上箭头的输入。
5. **数转换**：“导致状态改变的转换”不算自环；“带输出的转换”只数标了 `| 输出` 的箭头。

**得分表述**（引自对应 MS）
- 「Label A1 | X1 added on line from S1 to state labelled S2」⟦9618_w25_21:7(a)⟧
- 「Lines from S3 with correct event labels including 'loop' label」⟦9618_w25_21:7(a)⟧
- 「All three lines between S2 and S5 (including S5 to S5)」⟦9618_w23_21:7⟧
- 「One mark per row 3 to 7」⟦9618_s24_22:7(b)(i)⟧
- 「Input-B, Input-A」⟦9618_s24_22:7(b)(ii)⟧
- 「Temp < 10 (Heaters Off to Heaters On)」⟦9618_w21_21:4(b)⟧

**易错与失分**
- 自环漏画，或画成指向另一个状态。
- 箭头方向画反（从下一状态指回当前状态）。
- 标签只写输入、漏了输出，或把输出写在状态圈里。
- 图 → 表时，下一行的当前状态没有接上一行的下一状态。
- 控制系统题的条件写成 `Temp <= 10`、`Temp >= 20`：题目说 below 10、above 20，用 `<`、`>`。

#### 代表题精讲　⟦9618_w23_21:7⟧

**在考什么**　表（讲解时请对照原卷 QP p.12 的表与半成品图）：

| 当前状态 | 输入 | 输出 | 下一状态 |
|:--|:--|:--|:--|
| S1 | A1 | X1 | S2 |
| S2 | A3 | none | S1 |
| S2 | A2 | X4 | S5 |
| S5 | A1 | X1 | S5 |
| S5 | A4 | X2 | S2 |
| S5 | A3 | none | S3 |
| S1 | A9 | X9 | S3 |
| S3 | A9 | X9 | S4 |

图里已画：START → S1；S1 → 一个未标名的圆圈，标签 A1 | X1；该圆圈 → S1，标签 A3。Complete the state-transition diagram. 5 分。

**完整作答**
1. 给已有的空圆圈写上 S2。
2. 新画三个圆圈 S3、S4、S5。
3. S1 → S3，标 `A9 | X9`。
4. S2 → S5，标 `A2 | X4`；S5 → S2，标 `A4 | X2`；S5 上画自环，标 `A1 | X1`。
5. S5 → S3，标 `A3`；S3 → S4，标 `A9 | X9`。

**与 MS 对齐**　五步依次对应 MS 五点：「S2 labelled」⟦9618_w23_21:7⟧；「S3, S4 and S5 added」⟦9618_w23_21:7⟧；「Line from S1 to S3」⟦9618_w23_21:7⟧；「All three lines between S2 and S5 (including S5 to S5)」⟦9618_w23_21:7⟧；「Line from S5 to S3 AND from S3 to S4」⟦9618_w23_21:7⟧。注意第 4 点三条线（含自环）全对才给分。

**英文作答句**　（本题答案即上面的图。）

**直观**　状态图像地铁线路图：圆圈是车站，箭头是单向线路，箭头上写着“刷什么卡（输入）| 广播什么（输出）”；绕回本站的环线就是自环。

**下一道变式**　⟦9618_s24_22:7(b)(i)⟧　（方向相反：按图和一串输入补全输入 / 输出 / 下一状态表，讲解时请对照原卷 QP p.17 的图。）

<!-- auto:drills P2-SD-04 -->

### P2-SD-05　错误类型与 IDE 调试　{#P2-SD-05}

<!-- auto:stats P2-SD-05 -->

**考法**　①说出并描述另外两种错误类型（每种：名称 1 分 + 描述 1 分）；②程序运行中停止响应属于哪种错误，什么结构会导致它；③为什么编译器发现不了这个错误；④说明怎样用 IDE 的断点、单步、变量监视 / 报告窗口定位错误（3–4 分）；⑤说出编码时有用的两个 IDE 功能；⑥给出断点的术语；⑦单行看不出来的语法错误还有哪些。

**识别信号**　syntax error / logic error / run-time error；Identify and describe two other types of error；unexpectedly stops responding；Explain why the compiler does not identify this error；Integrated Development Environment (IDE)；breakpoint、single stepping、watch window、report window。

**解题思路**
1. **三种错误**：
   - Syntax error（语法错误）：违反了语言的规则 / 语法（拼错关键字、括号不配对、缺 ENDIF）；编译器会报出。
   - Logic error（逻辑错误）：算法本身错了，程序能运行但结果不对（用错运算符、循环次数错）；编译器发现不了。
   - Run-time error（运行时错误）：运行时执行了非法操作（除以 0、数组越界、把非数字串转成数字），或死循环导致程序停止响应。
2. **编译器为什么发现不了**：没有违反语言规则，没有语法错误——错的是逻辑。
3. **停止响应**：条件循环的结束条件永远不满足（死循环）→ run-time error。
4. **IDE 调试三件套，按顺序写**：先在可疑处（如函数开头）设 **breakpoint**，让程序运行到这一句就停；然后 **single stepping**，一次执行一句；同时在 **watch / report window** 里看变量的值，发现哪一步出现了意料之外的值。每个术语配一句作用。
5. **编码时的 IDE 功能**：编辑器、自动补全、动态语法检查、自动缩进 / 美化输出（prettyprint）、折叠代码块、上下文提示。

**得分表述**（引自对应 MS）
- 「Rules of programming language // the language grammar was not followed」⟦9618_s25_21:2(c)⟧
- 「The program performs an illegal operation」⟦9618_s25_21:2(c)⟧
- 「Where the program does not behave as expected / Does not give expected result / An error in the logic of the algorithm」⟦9618_s25_22:2(b)(iii)⟧
- 「The rules of the language have not been broken // there are no syntax errors」⟦9618_s23_22:5(b)⟧
- 「The terminating condition is never satisfied」⟦9618_w24_22:5(b)⟧
- 「Set a breakpoint to stop the program at a certain line / statement / point」⟦9618_s23_22:5(c)⟧
- 「Step through the program line by line / statement by statement」⟦9618_s23_22:5(c)⟧

**易错与失分**
- 只写出错误类型的名字不描述，或描述与类型对不上。
- 题目说“除了语法错误 / 逻辑错误之外的两种”时又写了它。
- IDE 题只列术语不解释，或说 IDE 能“自动发现并改正错误”（ER s23 9618/22 Q5(c) p.20 点名这类错误说法，以及答了与调试无关的 prettyprint、autocomplete）。
- 把 IDE 的单步写成“一次运行一个模块”：是一次执行一条语句。
- 停止响应的原因写成“语法错误”：程序已经在运行，语法没问题。

#### 代表题精讲　⟦9618_w24_22:1(b)⟧

**在考什么**　已发布的程序里，函数 Lookup() 有时返回错误的值。用 IDE 的 watch window、single stepping、breakpoint 三项功能定位错误。Explain these features including the order that they will be used in to locate the error in Lookup(). 3 分。

**完整作答**
1. First, set a breakpoint at the start of (or within) Lookup(), so that execution stops at that statement.
2. Then use single stepping to execute the function one statement at a time.
3. While stepping, use the watch window to display the values of the variables, so that the statement where a variable gets an unexpected value can be found.

**与 MS 对齐**　三句依次对应 MS 三点：「Order starting with a breakpoint and an explanation – ‘stop execution at this statement / line’」⟦9618_w24_22:1(b)⟧；「Explanation of single stepping – execute ‘line by line’ / statements」⟦9618_w24_22:1(b)⟧；「Explanation of watch window – displaying the value of variable(s)」⟦9618_w24_22:1(b)⟧。顺序本身就是第一分的一部分：从断点开始。

**英文作答句**　Set a breakpoint in Lookup() to stop execution there, then single-step through it one statement at a time while the watch window shows how the variables change.

**直观**　查一辆车哪里异响：先在可疑路段停车（断点），再一米一米地慢慢开（单步），同时盯着仪表盘（监视窗口）看哪个读数突然不对。

**下一道变式**　⟦9618_s25_21:2(c)⟧　（逻辑错误改完之后，还可能有哪两种错误：名称与描述各 1 分。）

<!-- auto:drills P2-SD-05 -->

### P2-SD-06　找出并改正伪代码错误　{#P2-SD-06}

<!-- auto:stats P2-SD-06 -->

**考法**　①表格：每条语句可能有错，说出错在哪或写 NO ERROR（每行 1 分，3–5 分）——函数参数类型不对、运算符用错、赋值号与比较号混用；②一段伪代码里有若干语法错误和一个其他错误（逻辑 / 越界），指出并给出改正（3 分）；③指出“运算符用错”的几处并改正；④指出会导致运行时错误的语句并说明原因；⑤描述算法里的逻辑错误并说明怎样改正；⑥流程图里判断框顺序错了：为什么错、怎么改。

**识别信号**　may contain errors. State the error in each case or write 'NO ERROR'；The pseudocode contains two syntax errors and one other error；Identify each error and state the correction required；contains a logical error. Identify the error and suggest a correction；statements that could generate a run-time error。

**解题思路**
1. **逐句对照插页**：函数名、参数个数、参数类型（`IS_NUM` 要字符串、`STR_TO_NUM` 要字符串、`NUM_TO_STR` 要数值）、返回类型能不能赋给左边的变量。
2. **运算符**：比较用 `=`，赋值用 `←`（`IF EMPTY ← "" THEN` 错）；`&` 只连接字符串（`2 & 4`、`"Done" & 数字` 错）；`+` 不能加字符串；`AND` / `OR` 两边必须是布尔值（`IF x = 3 OR 4` 错）。
3. **结构配对**：`WHILE` 配 `ENDWHILE`、`FOR` 配 `NEXT 变量`、`REPEAT` 配 `UNTIL`、`IF` 配 `ENDIF`、`CASE OF` 配 `ENDCASE`。配错是语法错误。
4. **其他错误**：下标越界（数组从 1 开始，代码却访问了 0）、比较方向反了（找最小值用了 `>`）、循环次数差一、计数器没初始化、除以 0。
5. **作答格式**：说出**哪一句 / 哪一行**、**错在哪**、**改成什么**。只说“这一行有错”不给分。

**得分表述**（引自对应 MS）
- 「NEXT Index (should be ENDWHILE)」⟦9618_s24_22:5(a)(i)⟧
- 「'&' used to concatenate an integer (in OUTPUT statement)」⟦9618_s24_22:5(a)(i)⟧
- 「Accesses element outside range // Accesses element 0」⟦9618_s24_22:5(a)(i)⟧
- 「Num > Min should be Num < Min」⟦9618_w23_21:5(a)⟧
- 「Count & 1 should be Count + 1」⟦9618_w23_21:5(a)⟧
- 「Should be "=" not ←」⟦9618_w22_21:1(c)⟧
- 「Parameter should be a string (or char) // should not be a real」⟦9618_w22_21:1(c)⟧

**易错与失分**
- 把正确的语句也说成错：表格题里常有一两行是 NO ERROR（`X ← STR_TO_NUM("37") + 5` 没错）。
- 只说错误不写改正：题目要求 state the correction 时，改正本身是得分的一半。
- 把逻辑错误当语法错误：`Num > Min` 应为 `Num < Min` 不违反语法，是逻辑错误。
- 改正时引入新的非指南写法（`!=`、`ENDFOR`）。
- 越界错误只说“循环错了”，没说出访问了 `Data[0]`、数组下界是 1。

#### 代表题精讲　⟦9618_s24_22:5(a)(i)⟧

**在考什么**　全局一维数组 Data 有 200 个 STRING 元素，第一个元素下标为 1。过程如下（原题代码，**含错误**，所以不按伪代码块标注；讲解时请对照原卷 QP p.10）：

```text
PROCEDURE Process(Label : STRING)
   DECLARE Index : INTEGER
   Index ← 0
   INPUT Data[Index]
   WHILE Index < 200
      Index ← Index + 1
      CASE OF (Index MOD 2)
         0 : Data[Index] ← TO_UPPER(Label)
         1 : Data[Index] ← TO_LOWER(Label)
         OTHERWISE : OUTPUT "Alarm 1201"
      ENDCASE
   NEXT Index
   OUTPUT "Completed " & Index & " times"
ENDPROCEDURE
```

The pseudocode contains two syntax errors and one other error. Identify the errors. 3 分。

**完整作答**
- Syntax error 1: `NEXT Index` is used to end a WHILE loop; it should be `ENDWHILE`.
- Syntax error 2: `&` is used to concatenate the integer `Index` in the final OUTPUT statement; it should be `OUTPUT "Completed ", Index, " times"` (or use `NUM_TO_STR(Index)`).
- Other error: `Index` is 0 when `INPUT Data[Index]` is executed, so it accesses `Data[0]`, which is outside the range of the array (the lower bound is 1).

**与 MS 对齐**　三点依次对应「NEXT Index (should be ENDWHILE)」⟦9618_s24_22:5(a)(i)⟧、「'&' used to concatenate an integer (in OUTPUT statement)」⟦9618_s24_22:5(a)(i)⟧、「Accesses element outside range // Accesses element 0」⟦9618_s24_22:5(a)(i)⟧，「One mark per error」⟦9618_s24_22:5(a)(i)⟧。

改正后的过程（供对照）：删去访问 `Data[0]` 的 `INPUT` 一句；`NEXT Index` 改成 `ENDWHILE`；输出用逗号分隔。CASE 只有 0、1 两种结果，这里顺手改成 IF … ELSE（多余的 OTHERWISE 正是 (a)(ii) 问的，见 SD-08）。

```pseudocode
PROCEDURE Process(Label : STRING)
   DECLARE Index : INTEGER
   Index ← 0
   WHILE Index < 200
      Index ← Index + 1
      IF Index MOD 2 = 0 THEN
         Data[Index] ← TO_UPPER(Label)
      ELSE
         Data[Index] ← TO_LOWER(Label)
      ENDIF
   ENDWHILE
   OUTPUT "Completed ", Index, " times"
ENDPROCEDURE
```

**英文作答句**　（本题答案即上面三句。）

**直观**　找错像校对作文：先查“格式”（括号、关键字配对、`&` 只接文字），再查“内容”（写到了不存在的第 0 格）。

**下一道变式**　⟦9618_w22_21:1(c)⟧　（表格题：四条语句各说出错误或写 NO ERROR——赋值号当比较号、`IS_NUM` 的参数是实数、两个字符串用 `+` 相加。）

<!-- auto:drills P2-SD-06 -->

### P2-SD-07　追踪表（干跑）　{#P2-SD-07}

<!-- auto:stats P2-SD-07 -->

**考法**　按给定的调用或输入，逐行执行一段伪代码（或流程图），按该题表格约定记录变量的赋值与输出（4–6 分，按列或按“圈出的区域”给分）；写出最后的返回值或输出；补全执行后数组的内容；数循环执行了几次；回答某个输入下某变量被赋了什么值。代码常含：逐字符处理字符串、按输入分支计数、数组元素互相引用（下标由上一步的值算出）、链表插入、插入排序。

**识别信号**　Complete the trace table (below) by dry running the function / procedure / algorithm；when it is called as follows: CALL …；when the following values are input；The first row has been completed；State the value returned；Complete the diagram showing the contents of the global arrays … after the procedure has run。

**解题思路**
1. **先读题头**：调用的参数是什么（`CALL Process(2)`）、表里有哪几列、第一行是否已给出。初值行（参数、计数器、数组初值）就是 MS 的第一分。
2. **一句一句走**，逐条执行赋值，按题目与该题 MS 的追踪表约定记录。语句没执行才不记录该次赋值；执行后赋得相同值也不能一概省略。本卡代表题第 4、5 轮的 Index 都要再次填 2；Value 与 Total 可按该题 MS 排在同一表行，不要求每次赋值另起一整行。
3. **循环条件每轮都重新判断**：先算条件，再决定进不进循环体；WHILE 在循环前判断，REPEAT 在循环后判断。
4. **下标由变量算出时**（`Mix[Index]`、`Index ← (Value MOD 4) + 1`），先在草稿上算出这一轮的下标，再去读、写那个元素；数组元素被改过后，后面读到的是**新值**。
5. **字符串**：每轮写出取到的字符（带单引号）和拼接后的完整串（带双引号）；空格用题目规定的符号（如 ∇）表示。
6. **最后一轮**：循环结束后的语句（`Mix[1] ← Total * Index`、RETURN）也要填；MS 常把“最后一行全对”单列一分。

**得分表述**（引自对应 MS）
- 「Row 1 (initialisation)」⟦9618_w23_23:5⟧
- 「5 – Total 28 and final Mix[1] = 56」⟦9618_w23_23:5⟧
- 「One mark for each of columns 2 to 5 (condone missing final 11)」⟦9618_s21_21:4(a)⟧
- 「If no marks per group then mark by columns (columns 3 to 6) for max 4」⟦9618_s22_22:5(b)⟧
- 「One mark per zone」⟦9618_s24_21:5(a)⟧
- 「Award 1 mark per region」⟦9618_s25_22:6(a)(i)⟧

**易错与失分**
- 用了数组的旧值：前一轮已经改过的元素，这一轮再读要用新值。
- 漏了循环结束后的那一句（`Mix[1] ← Total * Index`），或多走了一轮（条件已不满足还继续）。
- 没区分语句未执行与执行后赋得相同值，擅自省略后者；或没按本题表格约定记录，把一轮里的赋值写进了上一轮的行。
- 字符串列忘了引号、大小写，或空格没用规定的符号表示。
- REPEAT 循环忘了“先执行一次再判断”；FOR 循环的终值算错（终值包含在内）。
- ER w23 9618/23 Q5 p.23：很少有人拿满 6 分，多数人拿到初值那一分后就“很快迷路”——每一步都要在草稿上写清当前的下标。

#### 代表题精讲　⟦9618_w23_23:5⟧

**在考什么**　全局整数数组 Mix 的初值：`Mix[1]` = 4、`Mix[2]` = 2、`Mix[3]` = 3、`Mix[4]` = 5。过程（讲解时请对照原卷 QP p.10–11 的代码与空表）：

```pseudocode
PROCEDURE Process(Start : INTEGER)
   DECLARE Value : INTEGER
   DECLARE Index : INTEGER
   DECLARE Total : INTEGER
   Index ← Start
   Total ← 0
   WHILE Total < 20
      Value ← Mix[Index]
      Total ← Total + Value
      IF Index < 4 THEN
         Mix[Index] ← Mix[Index] + Mix[Index + 1]
      ELSE
         Mix[Index] ← Mix[Index] + Mix[1]
      ENDIF
      Index ← (Value MOD 4) + 1
   ENDWHILE
   Mix[1] ← Total * Index
ENDPROCEDURE
```

（原题把三个变量写在一句 DECLARE 里，这里按指南拆成三句，执行结果相同。）Complete the trace table by dry running the procedure when it is called as follows: `CALL Process(2)`. 6 分。

**完整作答**

| Index | Value | Total | Mix[1] | Mix[2] | Mix[3] | Mix[4] |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 2 | | 0 | 4 | 2 | 3 | 5 |
| | 2 | 2 | | | | |
| | | | | 5 | | |
| 3 | | | | | | |
| | 3 | 5 | | | | |
| | | | | | 8 | |
| 4 | | | | | | |
| | 5 | 10 | | | | |
| | | | | | | 9 |
| 2 | | | | | | |
| | 5 | 15 | | | | |
| | | | | 13 | | |
| 2 | | | | | | |
| | 13 | 28 | | | | |
| | | | | 21 | | |
| 2 | | | | | | |
| | | | 56 | | | |

草稿（每一轮）：
1. Total = 0 < 20：Value = Mix[2] = 2，Total = 2；Index 2 < 4，Mix[2] = 2 + Mix[3] = 5；Index = (2 MOD 4) + 1 = 3。
2. Total = 2：Value = Mix[3] = 3，Total = 5；Mix[3] = 3 + Mix[4] = 8；Index = (3 MOD 4) + 1 = 4。
3. Total = 5：Value = Mix[4] = 5，Total = 10；Index 不小于 4，Mix[4] = 5 + Mix[1] = 9；Index = (5 MOD 4) + 1 = 2。
4. Total = 10：Value = Mix[2] = 5（已是新值），Total = 15；Mix[2] = 5 + Mix[3] = 13；Index = 2。
5. Total = 15：Value = Mix[2] = 13，Total = 28；Mix[2] = 13 + 8 = 21；Index = (13 MOD 4) + 1 = 2。
6. Total = 28，不再小于 20，离开循环；Mix[1] = 28 × 2 = 56。

**与 MS 对齐**　MS 六点：「Row 1 (initialisation)」⟦9618_w23_23:5⟧，然后每一轮一分——Total 依次为 2、5、10、15、28，最后一分还要求「5 – Total 28 and final Mix[1] = 56」⟦9618_w23_23:5⟧。MS 的表正是上面这种“一次变化写一行”的格式。

**英文作答句**　（本题答案即上面的追踪表。）

**直观**　干跑就是“当一次电脑”：手里一张表，脑子里不许记任何东西，每做一步就把结果写到表上，下一步只看表上的最新值。

**下一道变式**　⟦9618_w22_21:6(b)(i)⟧　（字符串版：逐字符扫描 `"Liz.123@big@net"`，按字符类别给 Dots、Ats、Others 计数，最后 Valid 变成 FALSE；讲解时请对照原卷 QP p.10–11 的代码。）

<!-- auto:drills P2-SD-07 -->

### P2-SD-08　分析给定伪代码　{#P2-SD-08}

<!-- auto:stats P2-SD-08 -->

**考法**　读懂一段给定的代码（多半没有错）并解释：①四个赋值里哪一个永远不会执行、为什么；加上的 OTHERWISE 为什么永远不执行；②哪一句是多余的、为什么；③程序为什么给出意外的结果（参数按引用传递、初值选得不好）；④为什么选 −1 作初值；外层 / 内层条件的作用；⑤在什么条件下输出才正确；⑥某一段算法的目的是什么；⑦某个特殊字符串作结束标记可能带来什么问题。1–3 分。

**识别信号**　One of these assignments will never be performed. Identify … and explain why；State why this assignment is never performed；contains a statement that is not needed；Explain why the program gives unexpected results；Comment on why the programmer chose −1 as the initial value；Explain the purpose of the outer conditional clause；State the condition that results in the correct output；State the purpose of …。

**解题思路**
1. **先把代码在草稿上“翻译”成一句中文**：这段代码在做什么（找第一个匹配的下标、保留最后三行、统计…）。
2. **永远不执行的分支**：CASE 按顺序测试，前面的子句已经覆盖了后面子句的所有值（`< 30` 在 `< 20` 之前），后面的就测不到；OTHERWISE 永远不执行，是因为前面的子句已经覆盖了所有可能的值（`MOD 2` 只能是 0 或 1）。
3. **初值的作用**：−1 不是合法的数组下标，所以能表示“还没找到”；999 当最小值的初值时，如果所有输入都大于 999，结果就会错。
4. **意外结果**：参数按引用（BYREF）传递，模块里改了它，调用者的循环变量也跟着变；应按值传递。
5. **在什么条件下才对**：用三个变量轮流保存最后三行时，只有当行数是 3 的倍数时输出顺序才对。
6. 作答写成“**是哪一句 + 为什么**”两部分：MS 常把“指出”和“解释”分开给分。

**得分表述**（引自对应 MS）
- 「because CASE clauses are checked in sequence // because of the order of the clauses」⟦9618_w23_21:1(b)⟧
- 「a value < 30 satisfies the first clause // Clause '< 20' will never be tested」⟦9618_w23_21:1(b)⟧
- 「The result of MOD 2 can only be 0 or 1」⟦9618_s24_22:5(a)(ii)⟧
- 「It is a value that is invalid as an (array) index // not in the range of valid (index) values」⟦9618_w25_21:5(a)(i)⟧
- 「parameter / Num has been passed by reference // should have been passed by value」⟦9618_s23_22:5(a)⟧
- 「then the minimum will be given as 999 (and not one of the input values)」⟦9618_w23_21:5(b)(i)⟧
- 「If the number of lines in the text file is a multiple of three」⟦9618_s22_23:7(b)⟧

**易错与失分**
- 只指出哪一句、不解释原因（或反过来），3 分题只拿 1 分。
- 解释写成“这一句有错”：本型的代码通常没错，问的是“为什么执行不到 / 为什么多余”。
- BYREF 题只写“用了 BYREF”不说后果（ER s23 9618/22 Q5(a) p.20：三分题只提 ByRef 不解释拿不满；不少人误以为错在两处标识符不同）。
- 把目的写成逐行复述代码：要说出它整体完成什么（求最大公因数、按原顺序输出最后三行）。

#### 代表题精讲　⟦9618_w23_21:1(b)⟧

**在考什么**　一段 CASE（讲解时请对照原卷 QP p.2）：

```pseudocode
CASE OF ThisValue
   < 30 : Level ← "Low"
          Check ← 1
   < 20 : Level ← "Very Low"
          Check ← ThisValue / 2
   30 TO 40 : Level ← "Medium"
              Check ← ThisValue / 3
              Data[ThisValue] ← Data[ThisValue] + 1
   > 40 : Level ← "High"
ENDCASE
```

（`< 30 :` 这种关系式子句是本题原文的写法，指南的 CASE 只列了“值”与“值 TO 值”。）The pseudocode contains four assignments to variable Level. One of these assignments will never be performed. Identify this assignment and explain why this is the case. 3 分。

**完整作答**
- Assignment: `Level ← "Very Low"`.
- Why: the CASE clauses are checked in sequence and only the first clause that applies is executed. Any value less than 20 is also less than 30, so it satisfies the first clause `< 30` and the clause `< 20` is never tested.

**与 MS 对齐**　三点依次对应：「Level ← "Very Low" // the level is assigned value “very low”」⟦9618_w23_21:1(b)⟧；「because CASE clauses are checked in sequence // because of the order of the clauses」⟦9618_w23_21:1(b)⟧；「a value < 30 satisfies the first clause // Clause '< 20' will never be tested」⟦9618_w23_21:1(b)⟧。

**英文作答句**　`Level ← "Very Low"` is never performed, because the CASE clauses are tested in order: any value below 20 is also below 30, so the first clause is always chosen and the `< 20` clause is never reached.

**直观**　门口两个筛子，先过的是大孔（< 30），后面的小孔（< 20）根本接不到东西——能过小孔的早就被大孔接走了。

**下一道变式**　⟦9618_w25_21:5(a)(i)⟧　（FindFirst() 里 FoundAt 的初值为什么选 −1；同一题 (a)(ii)、(a)(iii) 继续问外层、内层条件的作用。）

<!-- auto:drills P2-SD-08 -->

### P2-SD-09　测试方法与测试策略　{#P2-SD-09}

<!-- auto:stats P2-SD-09 -->

**考法**　①某些模块还没写好或有错、集成测试停了：说出能继续测试的方法（stub testing）并描述（3 分）；②描述集成测试（2 分）；③发布前的最后测试阶段（beta）是什么、怎样做（3–4 分）；④描述走查（walkthrough）并说明它怎样发现错误；走查前还需要什么信息、为什么；⑤把测试描述对上测试方法（alpha、integration、black-box、acceptance）；⑥按描述填空：阶段名与测试名。

**识别信号**　Identify a method that can be used to continue testing the main program before the errors in these modules have been corrected；Describe integration testing；Identify and describe the additional / final test stage … before the program is sold / made available；walkthrough method；Complete the table by identifying the test method that matches the test description；Identify this method of testing。

**解题思路**
1. **Stub testing（桩测试）**：被调用的模块还没完成或有错时，写一个**简单的替身模块**代替它；替身只**返回一个已知的固定值**，或**输出一句“我被调用了”**——这样调用它的主程序可以继续测试。描述写两点：替身代替谁 + 替身做什么。
2. **Integration testing**：模块各自测试过之后，把它们**组合起来作为整体**测试。
3. **Alpha**：开发方内部、发布前；**Beta**：一小群（潜在）用户在真实环境中使用，反馈问题和建议，问题改正后再发布；**Acceptance**：客户在交付前确认满足需求。
4. **White-box**：看着代码设计测试数据，走遍每条路径；**Black-box**：不看代码，只比较输入与预期输出。
5. **Walkthrough / dry run**：逐行走一遍程序、填追踪表，记录变量的变化；变量出现意外的值或走了意外的路径，就说明有错。走查前需要：源代码（或说明）和测试计划（测试数据与预期结果），因为要知道程序的结构，才能测到所有路径。
6. 描述题按“**谁 + 什么时候 + 做什么 + 为了什么**”写，每一句扣一个得分点。

**得分表述**（引自对应 MS）
- 「Modules that have already been tested individually」⟦9618_s22_22:5(c)⟧
- 「are combined into a single (sub) program which is then tested as a whole」⟦9618_s22_22:5(c)⟧
- 「The dummy/simple module will return an expected value // will output a message to show it has been called」⟦9618_s23_21:8(c)(ii)⟧
- 「Testing carried out by a small group of (potential) users」⟦9618_w22_22:1(b)⟧
- 「The program is checked by creating a trace table / going through the program a line at a time」⟦9618_w22_23:5(d)⟧
- 「so that all paths through the program can be tested」⟦9618_s23_23:5(a)⟧
- 「Acceptance testing」⟦9618_w25_22:5(b)⟧

**易错与失分**
- 桩测试描述成“跳过这个模块”“先不测它”：要写出“写一个简单的替身模块，返回已知值或输出消息”。
- 集成测试只写“把模块放在一起”，漏了“各自已经测过”这一前提。
- beta 测试写成“开发者再测一遍”：beta 是**用户**在真实环境中测。
- alpha、beta、acceptance 三者混用：内部 → 外部少量用户 → 客户验收。
- 走查只写“检查代码”，没有写出“逐行 + 追踪表 + 变量出现意外值就说明有错”。

#### 代表题精讲　⟦9618_s23_22:8(c)⟧

**在考什么**　模块 SuppExists() 与 CheckSupplier() 已经写好但有错，它们在主程序的多处被调用，主程序的集成测试因此停了。Identify a method that can be used to continue testing the main program before the errors in these modules have been corrected and describe how this would work. 3 分（方法 1 分，描述 2 分）。

**完整作答**
- Method: stub testing.
- Description: SuppExists() and CheckSupplier() are replaced by dummy (simple) modules with the same names and parameters. Each dummy module just returns a known result, or outputs a message to show that it has been called, so the main program can still be tested.

**与 MS 对齐**　「Method: Stub testing」⟦9618_s23_22:8(c)⟧；描述两点：「The modules SuppExists() and CheckSupplier() are replaced by dummy modules」⟦9618_s23_22:8(c)⟧ 与「...which return a known result / contain an output statement to show they have been called」⟦9618_s23_22:8(c)⟧。描述里写出两个模块名，就是“扣情境”。

**英文作答句**　Use stub testing: replace SuppExists() and CheckSupplier() with simple dummy modules that return a known value or output a message saying they were called, so testing of the main program can continue.

**直观**　排练话剧时主角请假，就找个人拿着剧本站在那个位置念台词（替身），其他演员的戏照样能排。

**下一道变式**　⟦9618_w22_23:5(d)⟧　（描述走查方法，并说明它怎样发现错误，3 分。）

<!-- auto:drills P2-SD-09 -->

### P2-SD-10　测试数据与有效性检查　{#P2-SD-10}

<!-- auto:stats P2-SD-10 -->

**考法**　①补全测试计划：给出测试数据、数据类型（normal / abnormal / boundary / extreme）、预期结果，每行 1 分（4–5 分）；②为一个过程设计几组测试数据序列并说明各自的目的；③给出一个能暴露问题的输入（让最小值算错的四个值、格式正确但无法求值的表达式）；④说出对参数应做的有效性检查；⑤白盒测试：给出走不同路径的两组有效数据；⑥概述怎样全面测试一个函数。

**识别信号**　A test plan is needed … Complete the table. The first line has been completed for you；Type of test data | Test data value | Expected result / outcome；normal / abnormal / boundary / extreme；Give three test data sequences；Give a test string that could be used to show …；State two checks that could be applied to the values passed to the function；Outline a test plan。

**解题思路**
1. **先找边界**：从题目里找出合法范围（24 到 37、0 到 40、149 到 155 克），写下四个关键值：下界、上界、下界 − 1、上界 + 1。
2. **四类数据**：
   - normal：范围中间的值 → 接受 / TRUE。
   - boundary / extreme：恰好在边界上的合法值（24、37）→ 接受。
   - 边界外一步的非法值（23、38）：MS 多标为 abnormal（也接受 boundary）→ 拒绝 / FALSE。
   - abnormal：明显在范围外的值（12、99）→ 拒绝。
3. **一行写全三栏**：类型、值、预期结果都要和题意一致，一栏错整行没分。题目给了第一行（normal）就不要再写 normal。
4. **测试序列题**：每个序列写清“数据 + 目的”，并且**以结束值结尾**（如 99）：只有奇数、只有偶数、奇偶个数相等、只有结束值。
5. **暴露问题的输入**：先读懂 SD-08 式的问题（初值 999、除以 0），再造出恰好触发它的数据。
6. **参数检查**：范围（月份 1–12、起点 ≥ 1）、长度够不够、类型对不对、几个参数之间是否一致（日号与月份匹配）。

**得分表述**（引自对应 MS）
- 「One mark per row for rows 2 to 5」⟦9618_w21_21:4(a)⟧
- 「Abnormal / Boundary / Extreme 23 FALSE」⟦9618_w24_21:5(b)(i)⟧
- 「Boundary / Extreme 24 TRUE」⟦9618_w24_21:5(b)(i)⟧
- 「data set with (only) odd values, terminated with 99」⟦9618_w23_22:4(b)⟧
- 「Value for month is between 1 and 12 (inclusive)」⟦9618_s23_23:2(b)(i)⟧
- 「Start and/or Num are >= 1 // positive」⟦9618_s22_22:7(b)⟧
- 「Create a list of numbers that should generate all of the possible check digit values」⟦9618_w25_23:6(a)⟧

**易错与失分**
- 只测了一边的边界，或把边界外的值标成“接受”。
- 预期结果写成“works”“correct”：要写具体的结果（TRUE / FALSE、"PASS" / "FAIL"、data is rejected）。
- 测试序列没有结束值，或和题目给的例子几乎一样（ER w23 9618/22 Q4(b) p.18–19：多数答案漏了结尾的 99；常见错误是与题目示例太相似）。
- 有效性检查写成“检查数据是否正确”：要写出具体的范围或条件。
- 白盒测试的两组数据走的是同一条路径。

#### 代表题精讲　⟦9618_w24_21:5(b)(i)⟧

**在考什么**　函数：以一个整数为参数；值在 24 到 37（含两端）之间返回 TRUE，否则返回 FALSE。Complete the table to define a test plan to thoroughly test the operation of the function. 第一行已给（Normal、30、TRUE），4 分。

**完整作答**

| Type of test data | Test data value | Expected result |
|:--|:--|:--|
| Normal | 30 | TRUE |
| Boundary / Extreme | 24 | TRUE |
| Boundary / Extreme | 37 | TRUE |
| Abnormal (just outside the range) | 23 | FALSE |
| Abnormal (just outside the range) | 38 | FALSE |

**与 MS 对齐**　MS 列了 12、23、24、25、36、37、38、99 八行备选，「Max 4 marks」⟦9618_w24_21:5(b)(i)⟧，「One mark per row」⟦9618_w24_21:5(b)(i)⟧。QP 除已给的 Normal、30、TRUE 外只有四个空行；上表四个新行均在 MS 里：24、37 标 Boundary / Extreme → TRUE；23、38 MS 写作 Abnormal / Boundary / Extreme → FALSE。备选：Abnormal、99、FALSE，可替换一个新行，不要求另加第五行。

**英文作答句**　（本题答案即上表。）

**直观**　测一扇只让身高 24 到 37 的人进的门：正中（30）已给，再测恰好踩线（24、37）和刚好差一点（23、38），填满四个空行；差得远（99）是另一个可选测试。

**下一道变式**　⟦9618_w23_22:4(b)⟧　（给 Count() 过程设计三组测试数据序列并写出目的，每组都要以 99 结尾。）

<!-- auto:drills P2-SD-10 -->

### P2-SD-11　维护类型　{#P2-SD-11}

<!-- auto:stats P2-SD-11 -->

**考法**　①已知一种维护（perfective），说出另外两种并各给一个原因（4 分，名称与原因配对）；②给出适应性维护的两三个原因；③按情境判断是哪种维护（硬件换了、要提高响应速度）；④除了适应性维护，再说出一种。

**识别信号**　One type of maintenance is called perfective. Name two other types；Give two / three reasons why adaptive maintenance may be required；Identify the type of maintenance；changes are made to the program to improve the speed of response。

**解题思路**
1. **三种维护**：
   - Corrective（纠正性）：程序有错、不按预期工作 → 改错。
   - Adaptive（适应性）：外部变了——用户需求变了、有了新技术 / 新硬件、用到的库模块变了、法规变了 → 让程序适应。
   - Perfective（完善性）：程序没错，但要更好——更快、更好用、更易维护。
2. **按情境判断**：出错 → corrective；“新硬件”“新 HTML 版本”“法律变化”“新需求” → adaptive；“提高响应速度”“改进界面” → perfective。
3. **名称 + 原因要配对**（MS：dependent marks）：名称错了，原因写得再好也没有分。原因扣情境（浏览器程序 → 新版 HTML）。

**得分表述**（引自对应 MS）
- 「Type: Adaptive Reason: To accommodate a change in the requirement / technology / legislation」⟦9618_s22_23:2⟧
- 「Type: Corrective Reason: The program does not operate as expected / contains a bug」⟦9618_s22_23:2⟧
- 「Dependent marks」⟦9618_s22_23:2⟧
- 「New technologies available to host website // changes made to library modules used」⟦9618_w22_23:1(d)⟧
- 「Change in relevant legislation」⟦9618_w22_23:1(d)⟧
- 「Perfective」⟦9618_s23_23:5(b)⟧

**易错与失分**
- 题目已经给出的 perfective 又写一次。
- 名称写成 preventive、update 等 MS 没有的词。
- 把“提高速度”判成 adaptive：程序没出错、外部也没变，只是要更好 → perfective。
- 适应性维护的原因写成“程序有错”：那是 corrective。

#### 代表题精讲　⟦9618_s22_23:2⟧

**在考什么**　网页浏览器程序需要维护。One type of maintenance is called perfective. Name two other types of maintenance that the program may require and give a reason for each. 4 分（名称与原因配对给分）。

**完整作答**
- Type 1: Adaptive. Reason: to accommodate a change in the requirements, technology or legislation, for example a new version of HTML becomes available.
- Type 2: Corrective. Reason: the program does not operate as expected because it contains a bug, for example passwords are not hidden.

**与 MS 对齐**　「Type: Adaptive Reason: To accommodate a change in the requirement / technology / legislation」⟦9618_s22_23:2⟧（MS 举例 a new HTML version is available）；「Type: Corrective Reason: The program does not operate as expected / contains a bug」⟦9618_s22_23:2⟧（MS 举例 passwords are not hidden）。「Dependent marks」⟦9618_s22_23:2⟧：原因分依附于名称分。

**英文作答句**　Adaptive maintenance is needed when the requirements, technology or laws change (for example a new version of HTML); corrective maintenance is needed when the program contains a bug and does not work as expected.

**直观**　养一辆车：坏了修（纠正性）；搬到冬天下雪的城市要换雪地胎（适应性）；车没毛病，但想跑得更省油（完善性）。

**下一道变式**　⟦9618_w23_23:1(d)⟧　（硬件换了，程序要改：判断是哪种维护，再给出另一个需要这种维护的原因。）

<!-- auto:drills P2-SD-11 -->

### P2-SD-12　按新需求修改程序　{#P2-SD-12}

<!-- auto:stats P2-SD-12 -->

**考法**　需求变了，说明程序要怎样改（多为文字，1–4 分）：①写出要改的那一行、或在 CASE 里加的一个子句以及放在哪里；②写出要移动的行号和新位置；③概述或描述对算法要做的改动（加参数、变量换成数组、循环改到给定行号、读两遍文件改成只读一遍并存进数组）；④文件不存在或为空时怎样处理、改用什么文件模式；⑤记录结构要加哪些字段、新模块怎样用这些数据；⑥某种改动会带来什么问题（复杂度、实数比较的精度）并给出解决办法。

**识别信号**　The requirement(s) … are changed；Explain the changes that will need to be made；Describe the changes that need to be made to steps … of the algorithm；Outline the changes …；Write the modified line / the single line of pseudocode；State where this new line should be placed；Write the number of the line to be moved and state its new position；Describe how this might be achieved / how the design could be modified。

**解题思路**
1. **先说清旧程序在做什么**（一句话），再对照新需求找出**差别**：多了一个输入？结束条件变了？要多存一项数据？要返回结果？
2. **按得分链逐环检查要改的地方**：模块头（加参数、改成函数、加 BYREF）→ 数据（变量换成数组、记录加字段、文件换模式）→ 循环（结束条件、次数）→ 循环里的处理 → 输出 / 返回。每一处改动写成一句，一句一分。
3. **只写改动**：没变的部分不用复述；题目说 steps 2 to 8，就只针对这几步说。
4. **写一行代码的题**：照原代码的变量名写，并说清放在哪一行之后（after the 'Z' clause / before the ENDCASE）。
5. **有“返回 TRUE / FALSE”要求时**，写清每种失败情况返回 FALSE、成功之后返回 TRUE。
6. **问题 + 解决**两段式：先说问题（会出错 / 更复杂 / 精度不够），再给一个具体办法。

**伪代码模板**（把改动写成代码时的检查顺序；以“从给定行号起输出三行”为例）

```pseudocode
// 1 module header: a new parameter, and a function because a result is now returned
FUNCTION OutputThree(StartLine : INTEGER) RETURNS BOOLEAN
   DECLARE ThisLine : STRING
   DECLARE LineNum : INTEGER
   DECLARE Printed : INTEGER
   DECLARE Success : BOOLEAN
   // 2 data: the rolling variables LineX, LineY, LineZ are no longer needed
   LineNum ← 0
   Printed ← 0
   OPENFILE "Result.txt" FOR READ
   // 3 loop: the end condition now depends on the parameter
   WHILE NOT EOF("Result.txt") AND Printed < 3
      READFILE "Result.txt", ThisLine
      LineNum ← LineNum + 1
      // 4 processing inside the loop
      IF LineNum >= StartLine THEN
         OUTPUT ThisLine
         Printed ← Printed + 1
      ENDIF
   ENDWHILE
   CLOSEFILE "Result.txt"
   // 5 return: TRUE only if all three lines were output
   IF Printed = 3 THEN
      Success ← TRUE
   ELSE
      Success ← FALSE
   ENDIF
   RETURN Success
ENDFUNCTION
```

**得分表述**（引自对应 MS）
- 「Change the procedure header to include a (numeric) parameter (as well as the filename)」⟦9618_s22_22:4(b)⟧
- 「Replace LineX, Y and Z with an array」⟦9618_s22_22:4(b)⟧
- 「Loop until given line number (-1) / <parameter> (-1) (lines have been read)」⟦9618_w24_21:3(c)⟧
- 「After outputting the (required) lines return TRUE」⟦9618_w24_21:3(c)⟧
- 「The file will need to be opened in APPEND mode」⟦9618_w24_21:8(c)⟧
- 「OTHERWISE : CALL Error(C)」⟦9618_s24_21:5(b)(i)⟧
- 「Replace the old code / algorithm wherever it appears with a call to the module / function / procedure / subroutine」⟦9618_s24_23:1(a)(ii)⟧

**得分点地图**（核验语料 18 个小问；MS 不拆分，以下按改动的种类人工归纳，一个小问可属于几类）

| 改动种类（MS 常见写法） | 小问数 | 技能标签 |
|:--|--:|:--|
| 数据怎么存：变量换成数组、记录加字段 / 新记录、一行字符串里加分隔符或新字段 | 7 | `declare-array`、`record-type`、`field-extract` |
| 模块头：加参数、把重复的代码提成模块并传参调用 | 2 | `module-header`、`procedure-call` |
| 循环：结束条件或次数改变（到给定行号、读到文件尾、只读一遍） | 3 | `loop-bounds`、`loop-to-eof` |
| 判断方式：随机数的比例、实数比较的误差、等待超时 | 3 | `random-numbers`、`relational-ops` |
| 文件：改用 APPEND，文件不存在时以 WRITE 新建 | 2 | `file-append`、`file-write` |
| 说出改动带来的影响（更复杂、显示更精确） | 2 | — |
| 写出要加的一行代码并说明位置 | 1 | `case-of` |

**易错与失分**
- 复述旧程序而不写改动；或只写“改循环”“改输出”，不说改成什么。
- 漏了失败时返回 FALSE 的情况，或成功时没有返回 TRUE。
- 写一行代码时用了原题没有的变量名，或不说放在哪里。
- 文件改动只写“改文件”，不写出模式名（APPEND / WRITE）。
- 记录结构改动只写“加数据”，不写出具体加哪个字段（归还日期、借阅期限类别）。

#### 代表题精讲　⟦9618_w24_21:3(c)⟧

**在考什么**　原算法用 8 步输出文本文件 Result.txt 的最后三行：打开文件，循环到文件尾，每读一行就把 LineY 赋给 LineX、LineZ 赋给 LineY、新行赋给 LineZ，循环后关闭文件并输出三行。需求改成：实现为函数，参数是一个行号；从这一行开始输出三行；输出了三行返回 TRUE，做不到返回 FALSE。Describe the changes that need to be made to steps 2 to 8 of the algorithm given in part (a). 4 分（MS 列 7 点）。讲解时请对照原卷 QP p.6 的 8 个步骤。

**完整作答**
1. Step 2: loop, reading lines from the file, until the line before the given line number has been read.
2. If the end of the file is reached before the given line, return FALSE.
3. Replace steps 3 to 6: loop three times; each time read a line from the file and output it.
4. If the end of the file is reached before three lines have been output, return FALSE.
5. After the three lines have been output, close the file and return TRUE.
6. Steps 4 to 6 that re-order LineX, LineY and LineZ are no longer needed.

**与 MS 对齐**　MS 两套等价的计分清单，Max 4。按“两次循环”那一套：第 1 句对应「Loop until given line number (-1) / <parameter> (-1) (lines have been read)」⟦9618_w24_21:3(c)⟧；第 2 句对应 MP2（到文件尾返回 FALSE）；第 3 句对应 MP3、MP4（循环三次，读一行并输出）；第 4 句对应 MP5；第 5 句对应「After outputting the (required) lines return TRUE」⟦9618_w24_21:3(c)⟧；第 6 句对应「Ordering of lines no longer needed」⟦9618_w24_21:3(c)⟧。写满六句，余量充足。

**英文作答句**　Read and skip lines until the given line number is reached, returning FALSE if the end of the file comes first; then read and output the next three lines, again returning FALSE if the file ends early; finally return TRUE. The shuffling of LineX, LineY and LineZ is no longer needed.

**直观**　原来是“一直读到最后，手里只留最后三张牌”；现在是“数到第 n 张，从这张起连翻三张给人看，翻不够就说不行”。

**同题 Python 版要点**
- 逐行读文件 ↔ `for raw in file:`，每行去掉换行符；读到够数就可以直接 `return True`（`with` 会负责关闭文件）。
- 伪代码里“先关文件再 RETURN”的顺序，在 Python 的 `with` 里不需要操心。
- 先过阶梯 **L07 E02**（逐行读并计数）。

```python
def output_three(start_line: int) -> bool:
    line_num = 0
    printed = 0
    with open("Result.txt") as file:
        for raw in file:
            line_num = line_num + 1
            if line_num >= start_line:
                print(raw.rstrip("\n"))
                printed = printed + 1
                if printed == 3:
                    return True
    return False
```

**下一道变式**　⟦9618_s22_22:4(b)⟧　（输出最后 n 行，n 由参数给出：改模块头、三个变量换成数组、改移位方法、按参数决定从哪一行开始输出。）

<!-- auto:drills P2-SD-12 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| SD-01 vs SD-02 | 阶段名、各阶段做什么、产出什么文档 → SD-01；瀑布 / 迭代 / RAD 的原理与优缺点 → SD-02 | stage / activity / document 还是 model / RAD / waterfall |
| SD-03 vs AD-02 vs PG-07 | 画或解释结构图 → SD-03；只列模块名与用途 → AD-02；由结构图写模块头 → PG-07 | Draw / Complete the structure chart 还是 identify modules / write the header |
| SD-04 vs AD-04 | 状态转换图（状态圈、事件 \| 输出）→ SD-04；程序流程图（框、菱形）→ AD-04 | state-transition 还是 program flowchart |
| SD-05 vs SD-06 | 错误类型的概念、IDE 怎样定位 → SD-05；在给定代码里指出具体哪一句错、怎样改 → SD-06 | type of error / IDE 还是 State the error in each case |
| SD-06 vs SD-08 | 代码有错，要指出并改正 → SD-06；代码没错，问作用、为何执行不到、为何多余 → SD-08 | error / correction 还是explain why / purpose |
| SD-07 vs SD-08 | 逐行记录变量 → SD-07；不填表，只解释 → SD-08 | trace table 还是explain |
| SD-07 vs PG-02 | 执行一整段代码 → SD-07；只求单个表达式 → PG-02 | dry run 还是evaluate each expression |
| SD-09 vs SD-10 | 测试方法的名称、含义、何时用 → SD-09；具体的测试数据、测试计划 → SD-10 | method / stage 还是test data / test plan |
| SD-09 vs SD-05 | 测试（找出有没有错）→ SD-09；调试（定位错在哪，用 IDE）→ SD-05 | testing method 还是IDE / breakpoint |
| SD-11 vs SD-12 | 只问是哪种维护、为什么需要 → SD-11；问具体怎样改程序 → SD-12 | type of maintenance 还是describe the changes |
| SD-12 vs SD-06 | 原程序没错、需求变了 → SD-12；原程序有错 → SD-06 | requirements are changed 还是contains errors |
| alpha vs beta vs acceptance | 开发方内部 → alpha；一小群真实用户 → beta；客户交付前确认 → acceptance | in-house / users / customer |
| white-box vs black-box | 看代码，测每条路径 → white-box；不看代码，只比输入与预期输出 → black-box | paths through the program 还是without referring to the code |
| integration vs stub | 已测好的模块组合起来测 → integration；有模块没完成，用替身代替 → stub | combined 还是dummy / simple module |
| adaptive vs perfective vs corrective | 外部变了 → adaptive；要更好 → perfective；有错 → corrective | new hardware / legislation 还是improve speed 还是bug |
