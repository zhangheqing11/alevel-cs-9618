# P4 打标签与得分点拆分指南（T34 用）

> 题型体系：`papers/p4/taxonomy.json` v1.0，9 章 36 个题型；技能标签：`papers/p2/skill_tags.json`（唯一词表，D8）+ `papers/p4/skill_tags.json`（`extends` P2，11 个 P4 新标签，见 §8.4）。本指南告诉打标签的人（T34）怎样给 `corpus/rows/p4/*.jsonl` 的每一行写 `types`、`tag_confidence`、`tag_note`，以及怎样给写代码、测试截图的小问写 `markpoints` 与 `ms_max`。设计依据、试标结果与考纲核对见文末 §10–§11。
>
> 引用行一律写纯文本行 id（如 9618_s25_43:2(e)），不加任何括号标记。

## 1. 要写的字段

```json
"types": {"primary": "P4-SQ-02", "cross": []},
"tag_confidence": "high",
"tag_note": "…",
"markpoints": [
  {"n": 1, "text": "Function Enqueue() header (and end) taking one (integer) parameter", "marks": 1, "skills": ["module-header"]}
],
"ms_max": 6
```

- `primary`：**每一行必须有且只有一个**主题型，P4 不允许 null。
- `cross`：副题型，0–2 个，见 §4。没有就写 `[]`。
- `tag_confidence`：`high` 或 `low`，见 §5。`low` 时 `tag_note` 必写；`high` 时可写一句「按指南 §7 第 n 条」。
- `markpoints` / `ms_max`：只给 §8.1 规定要拆的行写；其余行不写这两个字段。
- 不新建题型码，不新建技能标签。找不到合适题型 → 选最接近的、标 `low`、`tag_note` 写「无合适题型：…」；找不到合适技能 → 选最接近的标签，`tag_note` 写「技能词表缺：…」，由设计工位裁决。

## 2. 定主题型的步骤

1. **先看这一格要考生交什么**（证据文档里这一格是程序代码还是截图），再看情境：

   | 考生要交 | 先看的题型 |
   |:--|:--|
   | 截图（Test your program … Take a screenshot …；MS 列的是输出内容） | P4-MP-03 |
   | 声明：全局数组与变量、记录、类、ADT 的数组与指针 | AR-01 ～ AR-03、OP-01、OP-04；ADT 的声明归 SQ / LT 对应题型 |
   | 一个过程、函数或方法的代码（Write program code for …；含补全题干给的伪代码） | 按 §3 |
   | 主程序（Write / Amend / Edit the main program …） | 按 §3；常落在 MP-01、MP-02、OP-07、PR-01、SQ-04 |

2. **对照 taxonomy 的 `cues`** 找候选题型，再用 `not` 排除近邻。情境（动物、马术、员工工资、火车站）只决定故事，不决定题型。
3. **看 MS 的得分点清单**确认。P4 的 MS 依次给出「语言无关的得分点清单」与 Java、VB.NET、Python 三份范例代码（部分题还先给伪代码）。**题型与得分点只按清单定**；范例只用来理解清单，而且只看 Python 版。`ms_text` 里的 Python 范例丢了缩进，要读范例时渲染原页。
4. `has_figure: true` 的行（584 行，绝大多数是 MS 末尾「e.g.」后的截图样例）**打题型时通常不必看图**：截图样例不影响题型，清单是文字。下列情况必须看原页：类图（判断 OP-01 / OP-04 / OP-06 要看属性与方法表）、题干给的二叉树或链表示意图、QP 里的数据表（判断 AR-02 的维度）、`ms_text` 清单本身看不清时。命令：`~/.venvs/alevel-cs/bin/python skill/cie-9618-cs-tutor/scripts/rows.py render <行 id>`（看 MS 加 `--ms`）。
5. 同一大题的各小问**各自**定题型，不随大题。例：9618_s25_43 第 1 题依次是 1(a)–1(c) 线性队列 SQ-02、1(d) 读文件入队 FL-01、1(e)(i) 出队求和 SQ-04、1(e)(ii) 截图 MP-03。

## 3. 写代码小问怎样归类

P4 一个模块常同时用到文件、数组、ADT 操作与输出。按下面的规则定，不凭整体印象：

1. **先认模块身份**。下表左列认出来就直接定主题型，后面第 2–4 条只用来定 `cross`：

   | 模块是什么 | 主题型 |
   |:--|:--|
   | 栈 / 队列的 Push、Pop、Enqueue、Dequeue 本身，或它们的数组与指针声明 | P4-SQ-01 / SQ-02 / SQ-03 |
   | 链表、二叉树、哈希表的声明、插入、删除、查找、遍历（含写成类的方法，如 InsertNode()、Traverse()） | P4-LT-01 ～ LT-05 |
   | 排序、二分查找（迭代或递归） | P4-SR-03、SR-04、SR-02 |
   | 迭代 ↔ 递归改写；按描述或伪代码写的其他递归函数 | P4-RC-02；P4-RC-01 |
   | 类的声明、子类、getter / setter、其他方法、重写、容器类（方法在实现 ADT、排序、查找时按上面几行） | P4-OP-01 ～ OP-06 |
   | 在循环里调用已写好的 Pop / Dequeue 取出数据再处理，或按条件 Push 进不同的栈 | P4-SQ-04 |
   | 测试截图 | P4-MP-03 |

2. **数得分点**：其余模块（普通过程函数、主程序）按得分点归属计数。依赖某种结构才能拿到的得分点算这个结构的分。**通用点不算任何结构**：模块头、局部变量声明、不带校验的输入、输出一个值或一条消息、调用一个已写好的模块并保存或使用返回值（含只调用一次 Enqueue / Push 并按返回值输出成败）、按顺序调用几个模块。
3. **主题型 = 承担得分点最多的结构**，但这个结构必须「在场」：承担 ≥ 2 个得分点，**或**承担该行除模块头以外得分点的至少一半（小分值行常见，如 9618_w24_41:1(b)(i) 2 分，一个模块头 + 一个「遍历数组拼成字符串」→ AR-04）。几个结构同分时按下表优先级取第一个：

   | 优先级 | 结构（判断信号） | 题型 |
   |:--|:--|:--|
   | 1 | 写或追加文件 | P4-FL-03 |
   | 2 | 读文件并拆字段 / 多行一组建记录或对象 | P4-FL-02 |
   | 3 | 读文件，每行一项存进数组或 ADT | P4-FL-01 |
   | 4 | 在数组里与一个目标值逐个比较（找位置、是否存在、计数） | P4-SR-01 |
   | 5 | 遍历数组求最值、合计、百分比，按条件筛选 | P4-AR-05 |
   | 6 | 实例化对象、调用对象方法 | P4-OP-07 |
   | 7 | 按下标顺序输出数组或拼成字符串 | P4-AR-04 |
   | 8 | 建记录并赋字段 | P4-AR-03 |
   | 9 | 二维数组的声明、赋初值、按行列访问 | P4-AR-02 |
   | 10 | 一维数组的声明与存数（含随机数、去重） | P4-AR-01 |
   | 11 | 字符串处理（逐字符、拆分、拼接、校验位） | P4-PR-02 |
   | 12 | 输入并校验到合法 | P4-PR-01 |
   | 13 | 按公式或规则计算、多分支 | P4-PR-03 |

4. **第二个在场（≥ 2 个得分点）的结构**写进 `cross`（最多 2 个，见 §4）。
5. **没有任何结构在场**（得分点全是通用点，或某结构只有 1 分且不到一半）：主程序或驱动过程归 **P4-MP-01**；循环把一串输入或题给数据逐个交给某模块并按返回值输出 → **P4-MP-02**。例：9618_s23_42:2(e) EnterRecord() 输入、建记录（1 分）、调用 Enqueue 并输出 Full / Stored → MP-01；9618_s25_43:2(f)(i) 题给 4 个值逐个调用 Search() 并各输出结果 → MP-02。
6. 「Amend / Edit / Extend the main program」「Amend the procedure …」与「Write program code」同样处理：按改动部分的得分点归类。
7. **补全题干给的伪代码**（There are n incomplete statements … Write program code for …）与写代码同样处理：按伪代码实现的算法定题型（9618_s23_42:1(c) 冒泡 → SR-03；9618_s22_41:3(b) 循环队列 Enqueue → SQ-03；9618_w22_41:3(c) 二叉树递归查找 → LT-04；9618_w23_42:2(b)(i) 递归函数 → RC-01）。得分点按 §8.2 第 7 条切。

例：9618_s23_42:3(d) EnterHours() 读文件逐行更新已有对象：文件 3 分（头与开关文件、异常、循环读行）、在对象数组里查员工号 2 分 → 主题型 FL-01，副题型 SR-01。9618_w24_41:2(c)(ii) 主程序输入四道栏的高度与风险：输入与两个范围校验 3 分、声明 Fence 数组与实例化存入 2 分 → 主题型 PR-01，副题型 OP-07。9618_w22_41:1(c) FindValues()：两个校验点 2 分、遍历比较计数 3 分 → 主题型 SR-01，副题型 PR-01。

## 4. 副题型（cross）

`cross` 列出**另外承担 ≥ 2 个得分点**的题型，最多 2 个，同章、跨章都可以（D14）。只有 1 分的输入、输出、调用、建记录、getter 不加（9618_s25_42:2(e) 读文件建记录后调用 InsertIntoHash() 只占 1 分 → 不加 LT-05）。唯一例外：迭代 ↔ 递归改写的对象是排序、查找或树时，RC-02 总进 `cross`（§7 第 9 条）。

- **不加**：主题型的 `summary` 已经覆盖的内容。例：9618_s25_43:2(e) 二分查找的 MS 把迭代与递归写在同一张清单（Looping/recursive calls …）→ 不加 RC-01；9618_s23_42:3(c) 按字段决定实例化 Manager 还是 Employee 属 FL-02 本身 → 不加 OP-07；9618_w24_41:2(c)(i) Fence 类的两个 getter 合成 1 分 → 不加 OP-02。
- **不加**：调用 Enqueue / Push 并按返回值输出属通用点（§3 第 2 条）。例：9618_s25_43:1(d) 读文件入队 → FL-01，不加 SQ-04。

常见组合：

| 主题型 | 常见副题型 | 典型行 | 何时加 |
|:--|:--|:--|:--|
| P4-FL-01 读文件 | P4-SR-01 线性查找 | 9618_s23_42:3(d) | 读一行就在数组里找对应元素，查找 ≥ 2 分 |
| P4-SQ-03 循环队列 | P4-AR-03 记录 | 9618_s23_42:2(b) | 建空记录、填满队列数组 2 分 |
| P4-SQ-04 用 ADT 操作 | P4-PR-02 字符串 | 9618_w25_43:2(e) | 出队后做游程压缩，比较、计数、拼接 ≥ 2 分 |
| P4-PR-01 输入校验 | P4-OP-07 实例化 | 9618_w24_41:2(c)(ii) | 校验后建对象存进对象数组 2 分 |
| P4-SR-01 线性查找 | P4-PR-01 输入校验 | 9618_w22_41:1(c) | 先校验要找的值 2 分 |
| P4-SR-04 插入排序 | P4-RC-02 改写 | 9618_s24_42:3(c)(i) | 题目要求把一种写法改成另一种：总是加（全部得分点都在做改写，§7 第 9 条） |
| P4-SR-02 二分查找 | P4-RC-01 递归 | 9618_w25_42:2(e) | 递归调用、基本情况在清单里自成 ≥ 2 点（「recursive call with middle –1 …」「… middle + 1 …」） |

## 5. 低信心（`tag_confidence: "low"`）

只在下列情况标 `low`，并在 `tag_note` 写清原因：

1. 两个题型各承担约一半得分点，§3 的计数、优先级与 §7 都不能裁决。
2. 看了原页仍无法确定这一格 MS 在考什么（例如抽取把相邻小问的 MS 混在一起、清单与题干对不上）。
3. 36 个题型里都找不到合适位置（写「无合适题型」）。
4. 看原页后发现题干与 `stem` 明显不符（`tag_note` 写「行数据疑误」，供总控转修正任务）。

不要因为「题目长」「代码多」「有图」「是 2021 扩展卷」就标 `low`。目标：低信心 < 10%。

## 6. 特殊行

- **`equivalent_of` 不为空**的行（43 行）：照抄原行的 `types`、`tag_confidence`、`markpoints`、`ms_max`。
- **逐字相同但没标 `equivalent_of` 的行（共 162 行）**：`stem` 与 `ms_text` 压缩连续空白后与同季更小 variant 的同题号行完全相同，全部是带图行（抽取器对图形行保守不判重，同 P3 的 D35）。分布：核验语料 108 行——9618_s22_43（14）、9618_s23_43（12）、9618_s24_43（22）、9618_w22_43（20）、9618_w23_43（20）、9618_w24_43（20），均与同季 _41 相同；2021 扩展 54 行——9618_s21_42（19）、9618_s21_43（19）与 9618_s21_41 相同，9618_w21_42（16）与 9618_w21_41 相同。总控补 `equivalent_of` 之前：先比对（压缩空白后 `stem` 与 `ms_text` 都相同），相同就照抄小 variant 同题号行的全部字段。
- **2021 扩展卷**（`extension: true`）与 **s26 各卷**：同样打标签、同样拆得分点（D1 只限制选代表题）。
- **截图行**：`Test your program …`、`Take a screenshot …` 一律 MP-03，哪怕题干同时说「Edit the main program to call …」——只要 MS 给分的是输出内容（9618_s21_41:1(c)(ii)「Screenshot showing: …」）。MS 给分的是代码时按代码归类。
- **MS 的语言限定点**：清单里写明只对某语言的点（「Removing carriage return from each line read in (Java, Python)」、「(Python 5)」）照常拆，`text` 保留括号。
- **看图行**：见 §2 第 4 条。

## 7. 边界判例（按出现频率排）

1. **ADT 四分**：写 Push / Pop / Enqueue / Dequeue 本身（含其数组与指针声明）→ SQ-01 ～ SQ-03（9618_s22_42:1(c)、9618_s25_43:1(a)）；在模块里循环调用 Pop / Dequeue 处理数据、按条件 Push 分类 → SQ-04（9618_s23_41:3(c)、9618_w25_41:1(e)）；主程序把一串值逐个 Enqueue / Push 并报告成败 → MP-02（9618_s25_41:1(c)）；读文件逐行入栈入队 → FL-01（9618_s25_43:1(d)）；只入一次并报告成败的驱动过程 → MP-01（9618_s23_42:2(e)）。
2. **出队之后再处理**：数据靠循环出队 / 出栈取得 → 主题型 SQ-04，处理部分 ≥ 2 分进 `cross`。9618_w25_43:2(e) 出队后游程压缩 → SQ-04，副题型 PR-02；9618_w23_41:2(c)(iii) 出队后统计到记录数组 → SQ-04。主程序里出队直到返回空值并累加 → 仍是 SQ-04（9618_s25_43:1(e)(i)）。
3. **线性队列与循环队列**：队尾到末尾回到 0、用 NumberOfItems 判满判空 → SQ-03（9618_s23_42:2(c)）；没有回绕 → SQ-02（9618_s25_43:1(b)、9618_w22_42:3(b)）。用记录结构包住数组与指针的队列按有无回绕定（9618_w24_42:2(c)）。
4. **读文件二分**：每行就是数组的一项 → FL-01（9618_w24_41:1(a)）；每行按逗号拆字段、或每 n 行合成一条记录 / 一个对象 → FL-02（9618_s24_41:2(b)、9618_s23_42:3(c)）。读文件更新已有对象（不新建）→ FL-01（9618_s23_42:3(d)）。异常处理是文件题的一部分，不单独成题型。
5. **主程序五分**：只按顺序调用几个模块、保存返回值、输出 → MP-01（9618_w24_41:1(b)(ii)、9618_s25_43:2(d)(i)）；循环逐个交给模块 → MP-02（9618_s22_42:1(d)(i)）；主要是实例化对象、调用对象方法 → OP-07（9618_w24_41:2(b)(i)）；主要是输入校验 → PR-01（9618_w24_41:2(c)(ii)）；主要是出队 / 出栈处理 → SQ-04（9618_s25_43:1(e)(i)）。这里的「主要是」指该结构的得分点**严格多于**其他任何结构；与其他结构同票时按 §3 优先级表取主题型，输入校验进 `cross`（D43 ③）。主程序「调用一次 + 逐个输出整个（返回）数组」各 1 分时，输出数组占一半、按 §3 第 3 条在场 → AR-04，§3 优先于本条（D43 ②；9618_s24_41:1(c)(i)、9618_s24_42:3(b)(ii)、9618_w25_43:3(b)(iii)）。
6. **类与记录**：题目说 record structure（「If your programming language does not support record structures, a class can be declared instead」）→ AR-03（9618_s23_42:2(a)、9618_w24_42:2(a)）；题目说 class、要求私有属性与构造方法 → OP-01（9618_w24_41:2(a)(i)）。
7. **OOP 内部分界**：有父类 → OP-04（9618_s23_42:3(b)(i)；同时写一个子类新方法也归 OP-04，9618_s25_42:3(b)(i)）；属性是另一类对象的数组 → OP-06（9618_w22_41:2(b)(i)），只有一个结点引用属性的链表类 → OP-01（9618_s25_43:3(b)(i)）；名叫 Set… 但要计算再存入 → OP-03（9618_s23_42:3(a)(iii)），把参数加到属性上再限制在范围内仍是 setter → OP-02（9618_w23_41:3(a)(iii)）；子类里同名方法 → OP-05（9618_s23_42:3(b)(ii)、9618_w23_42:3(c)(ii)）。
8. **类的方法在实现 ADT**：按操作归 LT，不归 OP-03。对象实现的链表表头插入 → LT-02（9618_s25_43:3(b)(ii)）；树类的 InsertNode() → LT-03（9618_s24_42:2(b)(ii)）；以结点对象为参数的递归中序遍历 → LT-04（9618_s25_41:3(d)）。
9. **递归四分**：给了迭代版要求改写成递归（或反过来）→ RC-02（9618_w23_41:1(b)(i)、9618_w22_42:3(d)）；按描述或伪代码写递归函数 → RC-01（9618_w25_43:3(a)(i)）；递归的对象是二分查找 / 插入排序 / 二叉树 → SR-02 / SR-04 / LT-04。改写题的 RC-02 总进 `cross`（9618_s24_42:3(c)(i) 插入排序递归改迭代 → SR-04 + RC-02）；写递归版时，递归调用与基本情况在清单里自成 ≥ 2 点才加 RC-01（9618_w25_42:2(e) 加；9618_s25_43:2(e) 清单把循环与递归写成同一点 → 不加）。
10. **查找按数据在哪里定**：数组里逐个比较一个目标值 → SR-01（9618_s23_41:1(c)）；多条件、范围、最值 → AR-05（9618_s24_41:2(e)(i)；D43 ⑥ 更正例子）；链表里找到再删 → LT-02（9618_w24_41:3(d)(i)）；树里找 → LT-04（9618_w22_41:3(c)）；按散列值找 → LT-05（9618_w25_41:3(f)）。
11. **输出三分**：按下标顺序输出数组（一维、二维网格、记录、按存储顺序输出每个结点的三项）→ AR-04（9618_s25_43:2(c)、9618_s22_42:2(b)(ii)、9618_s24_42:2(b)(iii)）；沿指针走 → LT-01（9618_w24_41:3(c)(i)）；中序 / 后序遍历 → LT-04（9618_w22_41:3(d)）。按下标顺序遍历对象数组、用 getter 取属性逐个输出 → AR-04，getter 只是取值手段；只有实例化对象、调用对象方法占主要得分点时才是 OP-07（D43 ①；9618_s23_42:3(e)(i)）。
12. **字符串归属**：把整个数组拼成一行 → AR-04（9618_w24_41:1(b)(i)）；类的方法把属性拼成字符串 → OP-03（重写父类的 → OP-05，9618_s25_42:3(b)(ii)）；其余逐字符处理、比较、拆分、校验位 → PR-02（9618_w24_41:1(c)、9618_s24_41:3(d)(i)）。
13. **计算归属**：计算写在类的方法里、用对象属性 → OP-03（9618_w24_41:2(d)）；独立模块或主程序里的公式与多分支 → PR-03（9618_w23_42:2(a)(i)、9618_w22_42:2(f)；后者输入校验 2 分 → 副题型 PR-01）。
14. **声明归属**：ADT 的数组与指针声明 → 对应 SQ / LT 题型（9618_s25_43:1(a) → SQ-02；9618_w24_41:3(a) → LT-01；9618_w25_42:3(a) → LT-03）；表格数据的二维数组 → AR-02（9618_w22_42:1(a)、9618_w24_42:3(a)）；其余一维数组 → AR-01（9618_s23_42:1(a)、9618_w25_42:2(a) 含 20 个不重复随机数）。
15. **排序二维数组或记录**：按排序算法定（9618_s22_42:2(b)(i) 二维数组冒泡 → SR-03；9618_w22_42:1(e) 按优先级插入排序 → SR-04），AR-02 / AR-03 只在另有 ≥ 2 个声明或存取得分点时进 `cross`。
16. **哈希表**：算散列值的函数（只有 MOD）、插入、按散列值查找 → LT-05（9618_s25_42:2(c)、9618_s25_42:2(d)、9618_w25_41:3(f)）；读文件后调用插入 → FL-02，插入部分 ≥ 2 分进 `cross`。
17. **截图**：见 §6。2 分以上的截图行按 MS 圆点拆（§8.2 第 10 条），主题型仍是 MP-03。

## 8. 得分点拆分规则

### 8.1 哪些行要拆

同时满足下面三条的行写 `markpoints`：

1. `component = 4`；
2. `marks >= 2`；
3. MS 有计分清单（圆点、编号、「1 mark for …」逐行，或「1 mark for each completed statement」这类计数句）。

所有题型都适用，包括 2 分以上的截图行（MP-03）。**不拆**：1 分的行（P4 共 162 行，多为截图与一句调用）；MS 只有范例代码或截图样例、没有任何清单文字的行（`tag_note` 写「MS 无计分清单，未拆」，不算低信心）。

**为什么门槛是 2 分而不是 P2 / P3 的 4 分**：P4 每一格都是代码或截图，MS 几乎每行都有逐点清单；2–3 分的行有 295 行（占全部 744 行的 40%），P4 特有的技能——构造方法、getter / setter、实例化、对象数组、全局数组声明、主程序调用、测试截图——主要落在这些小分值行上。门槛定在 4 分会丢掉大部分 OOP 与证据类的失分统计。（`docs/PLAN.md` 写「P2/P4 中 ≥4 分的写代码小问再拆」，此处偏离，列入 PR「需要总控决定」。）

### 8.2 怎样切

1. **只从语言无关的清单切**。清单在 MS 开头，到「Example program code」「Pseudocode」「Java」「VB.NET」「Python」或「e.g.」为止。范例代码**不拆**，只用来理解得分点。
2. **一个圆点或一个编号 = 一条 markpoint**，`n` 从 1 连续编号，是我们自己的顺序号（D37 ②）。
3. **`text` = MS 原文**：去掉行首的 `•`、编号；跨行的原文用一个空格接起来；其余逐字照抄，包括 `…`、`...`、`//`、`(and end where appropriate)`、语言限定「(Java, Python)」、错别字。圆点下面附了示例代码行的（如 9618_w23_41:2(c)(iii) 的圆点后跟着伪代码），`text` 只取圆点的文字句，不抄代码行。校验：`text` 与 `ms_text` 先按 D26 / D29 归一私用区字符、再压缩连续空白后，`text` 必须是子串。
4. **`marks`** 一般为 1。MS 明写一个点值 2 分时照写。
5. **得分点总分大于小问分值**（「1 mark each to max 6」「1 mark per point (Max 7)」，或没写 Max 但点数多）→ 写 `ms_max`（= 小问分值）；相等不写。例：9618_w24_41:1(a) 7 点、max 6 → `ms_max: 6`；9618_s23_42:3(c) 8 点、7 分 → `ms_max: 7`。
6. **MS 分两段计分**（9618_s24_41:2(b)：「1 mark for: • appropriate use of exception handling …」+「1 mark each to max 6 • …」）→ 两段按出现顺序拆成一张清单，总分大于分值时写 `ms_max`，`tag_note` 写「MS 分两段计分：…」。
7. **计数句作一条**：「1 mark for each completed statement (5)」「1 mark for each completed statement to MAX 4」「One mark for each gap (5)」「One mark for each test」→ 作**一条** markpoint，`text` 是这句原文，`marks` = 括号里的数或 MAX 后的数（没有数时 = 小问分值减去其他点）；清单里其余的圆点或「1 mark for …」行照常各成一条。例：9618_s23_42:1(c) 三条：计数句 4 分 + 两个圆点各 1 分。**不按 P3 §8.2 B 的办法按留空行拆**：P4 考生交的是 Python，MS 补全的伪代码行与三份范例写法各异，逐行对应没有意义；技能打 `translate-pseudocode` + 所补算法的标签。
8. **没有圆点、逐行「1 mark for …」的清单**（9618_s22_41:3(b)：「1 mark per complete statement (5)」「1 mark for function heading and end, dealing with ByRef」「1 mark for remainder of function correct …」）→ 每行一条，计数行按第 7 条。
9. **MS 给了两套各自独立的计分清单** → 只拆第一套，`tag_note` 写「MS 另有替代计分清单：…」。只有替代范例代码、没有第二套清单的按唯一清单拆。
10. **截图行**（MP-03，≥ 2 分）：每个圆点一条，通常是「输入了哪些数据、无效的被拒」与「输出了哪些值」。例：9618_s25_43:3(c)(ii) 两条「Output of linked list with 50 40 30 20 10」「Output of 2nd linked list with 50 40 20 10」；9618_s25_41:2(e)(ii) 两条，第二条要求文件名与内容在同一截图。只有「One mark for each test」一句（9618_w23_41:3(e)(ii)）→ 按第 7 条作一条 2 分。期望输出只在截图样例里时，拆分照样只取清单文字。
11. 同一得分点内的 `//` 或 `/` 并列写法属于同一条，不拆开。
12. **一个圆点里写了两个可独立得分的点**（用「…」接上第二个点，且这样点数才对得上分值），或**圆点下另起一行、没有圆点的续行自成一个得分点**，按原页拆成两条（D43 ④）。例：9618_s25_41:1(c)、9618_w25_41:1(d)、9618_w25_41:3(d)（同一圆点两点）；9618_s24_42:1(c)(i)（MS 写「Loops MPs 2–5」印证）、9618_s24_41:2(e)(i)（「to max 6」共 7 点）（无圆点续行）。

### 8.3 怎样打技能标签

每条 markpoint 打 **1–3 个**标签，取「拿不到这一分最可能是因为不会哪项技能」。只用 P2 词表与 `papers/p4/skill_tags.json` 的标签；P3 的 `random-file`、`user-defined-type` 不在 P4 词表里，不用。P2 指南 §8.3 的对照表（模块头、返回、循环、查找、排序、文件开关等）照样适用；P4 常见写法补充如下：

| MS 写法 | 标签 |
|:--|:--|
| Function / Procedure / Method header (and end where appropriate) taking n parameters | `module-header`；「returning … in all cases」再加 `return-value` 或 `boolean-return` |
| Class X header (and end) / Class declaration | `class-definition`（只管类头；P4 的构造方法另用 `constructor`） |
| (All n) attributes declared as private with (appropriate) data types (declaration or comment) | `encapsulation` + `data-types` |
| Constructor header … taking n parameters / assigning parameters to attributes / initialising … within constructor | `constructor`（赋初值加 `initialise-variables`） |
| get method header with no parameter / returning correct attribute (without overriding) / 2nd get method | `getter-setter`（返回加 `return-value`） |
| set method taking parameter / assigns parameter to the attribute | `getter-setter` |
| Class header inheriting from … / calling parent (class) constructor | `inheritance`（子类构造方法头用 `constructor`） |
| Method … overriding parent method / calling parent method | `polymorphism`（调用父类版本加 `inheritance`） |
| (private) attribute array of type Card / Declaration of array … of type Fence | `array-of-objects`（是类的属性时加 `containment`，或建数组加 `declare-array`） |
| Instantiating / creating (new) object of type X with correct parameters | `object-instantiation`（存进数组加 `array-of-objects`） |
| Calling method X() for the object / using GetName() | `method-call` |
| Global array named X / n string elements / initialised to … | `declare-array` + `global-scope`（类型加 `data-types`，初值加 `initialise-variables`；MS 特别点名标识符时加 `p4-identifiers`） |
| 2D array with n × m elements | `array-2d` + `declare-array` |
| Record declaration / record or class with fields | `record-type`（字段类型加 `data-types`） |
| Opening file X to read and closing … | `file-open-read` + `file-close`（写 / 追加用 `file-write` / `file-append`） |
| Looping until end of file / reading each line | `loop-to-eof`（读行用 `file-open-read`） |
| … converting to integer and removing new line / Removing carriage return | `type-conversion`、`strip-newline` |
| Splitting each line by commas into … | `field-extract` |
| Reading in all sets of n lines / reading all lines for each employee | `read-line-groups` |
| Exception handling with (appropriate) output / try, catch | `exception-handling` |
| Checking if stack / queue is full / empty; incrementing pointer (and resetting to 0) | `stack-array` / `queue-array` |
| FirstEmpty / following pointers until −1 / updating previous pointer | `linked-list` |
| Node objects: GetNextNode() / storing null / HeadNode replaced | `object-reference`（链表操作加 `linked-list`，树加 `binary-tree`） |
| left / right pointer, recursive traversal | `binary-tree`（递归加 `recursion`） |
| Calculation of parameter MOD n / overflow / next free space | `hash-table`（MOD 加 `div-mod`） |
| Base case … returning / recursive call(s) | `recursion` |
| Calling X() and storing / using return value | `procedure-call` |
| Output … in (appropriate / correct) format / message | `output-format` |
| Taking … as input until it is between a and b (inclusive) | `input-validation` + `relational-ops` |
| random integers between … / unique | `random-numbers`（去重另加 `linear-search` 或 `flag-variable`） |
| 1 mark for each completed statement / remainder … following the pseudocode | `translate-pseudocode` + 所补算法的标签 |
| Output showing … entered twice … with first being invalid | `test-input-sequence` |
| Output of … / screenshot showing (values) | `test-output` |
| Screenshot of data in … file. Filename must be shown | `screenshot-file` |

不要给 P4 得分点打 `flowchart-draw`、`flowchart-to-pseudocode`、`trace-dry-run`、`case-of`、`case-range`（P4 不画流程图、不填追踪表，Python 没有 CASE）。`byval-byref` 只在 MS 明写 ByRef 时用（9618_s22_41:3(b)）。

### 8.4 P4 新技能标签

以下 11 个标签已在 `papers/p4/skill_tags.json`（`extends` P2 词表，D8）。只收 P2 词表没有、而 P4 MS 反复单独给分的技能：

| tag | group | 收入理由 | MS 例 |
|:--|:--|:--|:--|
| `constructor` | oop | P4 几乎每个类都有 1–3 分落在构造方法（参数个数、赋属性、初值），P2 的 `class-definition` 把类头与构造混在一起，无法区分失分 | 9618_s24_41:2(a)(i) |
| `object-instantiation` | oop | 「Instantiating an object … with correct parameters」是主程序与读文件题的独立得分点 | 9618_s23_41:2(d)(i) |
| `method-call` | oop | 「Calling … method for the object」「using GetX()」：对对象调用方法、用 getter 而不是直接读属性，与普通 `procedure-call` 错因不同 | 9618_s22_41:2(f) |
| `array-of-objects` | oop | 「array … of type Card」：声明对象数组、存进下一个空位、遍历调用方法 | 9618_s22_42:3(c) |
| `object-reference` | adt | 结点对象链接（None / null、GetNextNode()）实现的链表与树，与数组 + 整数指针（`linked-list`、`binary-tree`）错因不同 | 9618_s25_43:3(b)(iii) |
| `strip-newline` | file | Python / Java 读行后去掉换行是单独得分点，源文件是 CRLF 行尾 | 9618_s24_42:1(a) |
| `read-line-groups` | file | 一条记录占连续 n 行，每轮连读 n 行 | 9618_s22_42:3(c) |
| `hash-table` | adt | P4 写散列函数、冲突放溢出区或下一空位、按散列值查找；P2 词表没有散列 | 9618_s25_42:2(c) |
| `test-input-sequence` | evidence | 截图分常要求「按给定顺序输入、无效输入被拒后重输」 | 9618_s24_41:1(c)(ii) |
| `test-output` | evidence | 截图分的主体：输出的值、顺序、提示与正确程序一致 | 9618_s24_41:1(c)(ii) |
| `screenshot-file` | evidence | 截图写出的文本文件内容且文件名可见 | 9618_s25_41:2(e)(ii) |

### 8.5 拆分判例

| 行 | 情况 | 处理 |
|:--|:--|:--|
| 9618_s25_43:1(b) | 6 个圆点、6 分 | 6 条，不写 `ms_max` |
| 9618_w24_41:1(a) | 7 个圆点、max 6 | 7 条，`ms_max: 6` |
| 9618_s23_42:3(c) | 8 个圆点、7 分（含异常处理、多行一组、按字段建子类对象） | 8 条，`ms_max: 7` |
| 9618_s24_41:2(b) | 两段计分：1 分异常 + max 6 的 7 个圆点 | 合成一张 8 条，`ms_max: 7`，`tag_note` 记两段（§8.2 第 6 条） |
| 9618_s23_42:1(c) | 补全伪代码：计数句「to MAX 4」+ 2 个圆点 | 3 条：4 分 + 1 分 + 1 分（§8.2 第 7 条） |
| 9618_s22_41:3(b) | 无圆点：计数句 (5) + 两行「1 mark for …」 | 3 条：5 分 + 1 分 + 1 分（§8.2 第 8 条） |
| 9618_w23_41:3(e)(ii) | 截图 2 分，只有「One mark for each test」 | 1 条 2 分 |
| 9618_s25_43:3(c)(ii) | 截图 2 分，两个圆点 | 2 条，`test-output` |
| 9618_w24_41:2(e)(iii) | 截图 2 分：输入值与每匹马每道栏的概率 / 平均与最高 | 2 条，第一条 `test-input-sequence` + `test-output` |
| 9618_s25_43:1(e)(ii) | 截图 1 分 | 不拆（1 分行） |
| 9618_w24_41:3(c)(ii) | 主程序调用 1 分 | 不拆（1 分行） |

## 9. 各题型样例行

样例取 2022–25 核验语料，不取 s26（D1）；同一考季的 _43 与 _41 相同时只列 _41。每行 id 可用 `rows.py get <id> --ms` 查看。

### PR　输入、字符串与计算

| 题型 | 名称 | 样例行 | 提醒 |
|:--|:--|:--|:--|
| P4-PR-01 | 键盘输入与输入校验 | 9618_w24_41:2(c)(ii)、9618_s24_41:1(b)、9618_s22_41:1(e)(i) | 校验 ≥ 2 分才在场 |
| P4-PR-02 | 字符串处理 | 9618_w24_41:1(c)、9618_w23_41:1(a)(i)、9618_s24_41:3(d)(i) | 数据靠出队取得 → SQ-04 |
| P4-PR-03 | 数值计算与分支逻辑 | 9618_w23_42:2(a)(i)、9618_w22_42:2(f) | 写在类里 → OP-03 |

### AR　数组与记录

| 题型 | 名称 | 样例行 | 提醒 |
|:--|:--|:--|:--|
| P4-AR-01 | 声明一维数组并存入数据 | 9618_s23_42:1(a)、9618_s23_42:1(b)、9618_w25_42:2(a) | ADT 的数组归 SQ / LT |
| P4-AR-02 | 二维数组 | 9618_s22_42:2(a)、9618_w22_42:1(a)、9618_w24_42:3(a) | 只输出网格 → AR-04 |
| P4-AR-03 | 记录结构 | 9618_s23_42:2(a)、9618_s25_42:2(a)、9618_w24_42:2(a) | 题目说 class 且要私有 → OP-01 |
| P4-AR-04 | 按格式输出数组内容 | 9618_s25_43:2(c)、9618_w24_41:1(b)(i)、9618_s22_42:2(b)(ii) | 不跟随指针 |
| P4-AR-05 | 数组的统计与筛选 | 9618_w24_41:2(e)(ii)、9618_s24_41:2(e)(ii)、9618_s24_42:1(c)(ii) | — |

### FL　文本文件与异常处理

| 题型 | 名称 | 样例行 | 提醒 |
|:--|:--|:--|:--|
| P4-FL-01 | 读文本文件到数组或 ADT | 9618_w24_41:1(a)、9618_s25_43:1(d)、9618_s24_42:1(a) | 入队入栈也在这里 |
| P4-FL-02 | 读文件拆字段并建记录或对象 | 9618_s23_42:3(c)、9618_s24_41:2(b)、9618_s25_42:2(e) | — |
| P4-FL-03 | 写入或追加文本文件 | 9618_s22_41:1(f)、9618_s25_41:2(c)、9618_w25_42:3(d) | — |

### SR　查找与排序

| 题型 | 名称 | 样例行 | 提醒 |
|:--|:--|:--|:--|
| P4-SR-01 | 线性查找与计数 | 9618_s23_41:1(c)、9618_w22_41:1(c) | 多条件或最值 → AR-05 |
| P4-SR-02 | 二分查找（迭代或递归） | 9618_s25_43:2(e)、9618_s24_41:1(e)(i)、9618_w25_42:2(e) | — |
| P4-SR-03 | 冒泡排序 | 9618_w24_41:1(d)(i)、9618_s22_42:2(b)(i)、9618_w25_42:2(c) | 补全伪代码按 §8.2 第 7 条 |
| P4-SR-04 | 插入排序 | 9618_s25_43:2(b)、9618_w22_42:1(e)、9618_s24_42:3(c)(i) | 递归 ↔ 迭代仍归此 |

### RC　递归

| 题型 | 名称 | 样例行 | 提醒 |
|:--|:--|:--|:--|
| P4-RC-01 | 按描述或伪代码写递归子程序 | 9618_w25_43:3(a)(i)、9618_w23_42:2(b)(i) | 核验语料较少 |
| P4-RC-02 | 迭代与递归互相改写 | 9618_w23_41:1(b)(i)、9618_w22_42:3(d) | — |

### SQ　栈与队列

| 题型 | 名称 | 样例行 | 提醒 |
|:--|:--|:--|:--|
| P4-SQ-01 | 数组实现栈 | 9618_s22_42:1(c)、9618_w25_41:1(b)、9618_s23_41:3(b)(i) | 照题目的指针约定 |
| P4-SQ-02 | 数组实现线性队列 | 9618_s25_43:1(b)、9618_s24_41:3(b)、9618_w22_42:3(b) | — |
| P4-SQ-03 | 数组实现循环队列 | 9618_s23_42:2(c)、9618_s23_42:2(d)、9618_s22_41:3(b) | — |
| P4-SQ-04 | 用栈或队列的操作完成处理 | 9618_s25_43:1(e)(i)、9618_s23_41:3(c)、9618_w25_41:1(e) | 单次调用报成败不算 |

### LT　链表、二叉树与哈希表

| 题型 | 名称 | 样例行 | 提醒 |
|:--|:--|:--|:--|
| P4-LT-01 | 链表：声明初始化与遍历 | 9618_w24_41:3(a)、9618_w24_41:3(c)(i)、9618_s25_43:3(b)(iii) | — |
| P4-LT-02 | 链表：插入与删除结点 | 9618_w24_41:3(b)、9618_w24_41:3(d)(i)、9618_s25_43:3(b)(iv) | 对象实现也在这里 |
| P4-LT-03 | 二叉树：声明初始化与插入 | 9618_w25_42:3(a)、9618_s24_42:2(b)(ii)、9618_s25_41:3(c)(iii) | — |
| P4-LT-04 | 二叉树：查找与遍历 | 9618_w22_41:3(d)、9618_s25_41:3(d)、9618_w22_41:3(c) | — |
| P4-LT-05 | 哈希表 | 9618_s25_42:2(c)、9618_s25_42:2(d)、9618_w25_41:3(f) | — |

### OP　面向对象编程

| 题型 | 名称 | 样例行 | 提醒 |
|:--|:--|:--|:--|
| P4-OP-01 | 声明类：私有属性与构造方法 | 9618_w24_41:2(a)(i)、9618_s25_43:3(a)(i)、9618_s23_41:2(a)(i) | — |
| P4-OP-02 | getter 与 setter | 9618_w24_41:2(a)(ii)、9618_s23_41:2(a)(iii)、9618_w23_41:3(a)(iii) | 名叫 Set 但要计算 → OP-03 |
| P4-OP-03 | 写类的其他方法 | 9618_w24_41:2(d)、9618_w23_42:3(a)(v)、9618_s22_41:2(c) | — |
| P4-OP-04 | 继承：声明子类 | 9618_s23_42:3(b)(i)、9618_s25_42:3(b)(i)、9618_w23_42:3(c)(i) | — |
| P4-OP-05 | 重写父类方法（多态） | 9618_s23_42:3(b)(ii)、9618_w23_42:3(c)(ii)、9618_s25_42:3(b)(ii) | — |
| P4-OP-06 | 包含：容器类 | 9618_w22_41:2(b)(i)、9618_w25_41:2(c)(ii)、9618_w25_43:1(b)(ii) | — |
| P4-OP-07 | 创建对象并调用方法 | 9618_w24_41:2(b)(i)、9618_w25_41:2(b)、9618_w23_42:3(b)(i) | — |

### MP　主程序与测试证据

| 题型 | 名称 | 样例行 | 提醒 |
|:--|:--|:--|:--|
| P4-MP-01 | 主程序：调用模块并输出结果 | 9618_w24_41:1(b)(ii)、9618_s25_43:2(d)(i)、9618_w24_42:3(e)(i) | 驱动过程也在这里 |
| P4-MP-02 | 主程序：循环输入并逐个调用 | 9618_s22_42:1(d)(i)、9618_s25_41:1(c)、9618_s25_43:2(f)(i) | — |
| P4-MP-03 | 运行测试并截图 | 9618_s24_41:1(c)(ii)、9618_w24_41:2(e)(iii)、9618_s25_41:2(e)(ii) | ≥ 2 分按圆点拆 |

## 10. 设计说明与试标

- **章节**：按 P4 实际考的程序任务分 9 章，章码 PR、AR、FL、SR、RC、SQ、LT、OP、MP，不与 P1–P3 冲突（P1 IR CM HW LG PF SS SP EO DB；P2 AD DT PG SD；P3 DR CI HV BL SY SC AI CT FP）。顺序即学习顺序：先 Python 基本功（输入、字符串、数组、文件），再算法（查找排序、递归），再数据结构（栈队列、链表树散列），再 OOP，最后主程序与测试证据。阶梯 L09–L12 是这条线的 Python 基础。
- **与 P2 / P3 同名算法的分界**：P2 写伪代码（DT、PG），P3 在纸上写、补全或追踪（CT、FP），P4 上机写 Python。每个 P4 题型的 `not` 都写了对应的 P2 / P3 题型。
- **粒度**：一个题型 = 识别信号、作答套路、MS 得分句模式都稳定的一种考法。ADT 按「写操作本身」与「用操作完成处理」分开（SQ-01 ～ SQ-03 与 SQ-04），因为两者的失分点不同（前者是指针与判满判空，后者是返回值检查与循环结束条件）；OOP 拆 7 型，因为 P4 每卷都有一道 OOP 大题，声明、getter / setter、子类、重写、容器、实例化各自有稳定的 MS 句式。
- **写代码题的归类**：P4 模块混用结构，比 P3 复杂，所以先认模块身份、再数得分点、同分按优先级（§3）。与 P2 §3 不同：P2 在场结构按优先级取第一，P4 取得分点最多的，因为 P4 的驱动过程与主程序常混着输入校验、实例化、查找，按优先级会把 3 分的校验让给 2 分的实例化。
- **试标**：`papers/p4/pilot_tags.csv`（列 `id,primary,cross,confidence,note`，多个副题型用 `;` 分隔），3 份不同考季、不同 variant 的卷全部小问（9618_s23_42、9618_w24_41、9618_s25_43，共 71 行，225 分）。每行都找到了主题型；低信心 0 行；带副题型 3 行；用到 25 个题型。`papers/p4/pilot_markpoints.jsonl`（每行 `{"id", "ms_max", "markpoints"}`，`ms_max` 为 null 表示不写该字段）：57 行拆出 218 条得分点（不拆的 14 行都是 1 分行），用到 59 个技能标签（含 P4 新标签 9 个）；每条 `text` 已核对为 MS 原文子串（D26 归一 + 压缩空白，不做大小写与标点放宽），每行得分点总分等于分值或带 `ms_max`。
- **试标中补充的规则**：① 9618_w24_41:2(c)(ii) 校验 3 分对实例化 2 分，定出「取得分点最多、同分才按优先级」；② 9618_w24_41:1(b)(i) 2 分行只有一个结构点，定出「在场 = ≥ 2 分或占非模块头得分点一半」；③ 9618_s23_42:2(e) 定出单次 Enqueue 报成败是通用点、驱动过程归 MP-01；④ 9618_s23_42:1(c) 补全伪代码的计数句作一条（§8.2 第 7 条）；⑤ 9618_s25_43:3(b)(ii) 对象链表的插入按操作归 LT-02；⑥ 9618_s25_43:2(e) 迭代 / 递归同一清单不加 RC-01。复核时另把二维数组网格输出从 AR-02 移到 AR-04、出队后压缩从 PR-02 移到 SQ-04（taxonomy 的 summary、cues、not 已同步）。
- 未在试标卷出现、只凭 cues 与样例行定义的 11 个题型：PR-03、AR-02、FL-03、SR-01、RC-01、RC-02、SQ-01、LT-03、LT-04、LT-05、OP-06。T34 打完后，若某题型核验语料不足 2 次、或低信心集中在某一对题型，交设计工位复核再定是否合并。

## 11. 考纲核对（2027–2029）

- **对照了什么**：`sources/official/9618_syllabus_2027-2029.pdf` 第 19–20 节与 P4 说明，和 2026 版考纲同节逐行比对：第 19–20 节内容完全相同（只有排版空白不同）。P4 说明两版一致：2 小时 30 分、75 分，考第 19–20 节（低级编程与声明式编程除外），用 Java / VB.NET / Python 控制台程序，提交程序代码与测试证据；「source files given will not contain binary files」是 2026 版起的说明（2026 考纲变更表）。
- **题型的 `syllabus` 字段**：P4 只直接考 19–20 节，但程序任务实际用到 AS 的 10.1–10.4（数据类型、数组、文件、ADT）、11.1–11.3（编程基础、构造、结构化编程）、12.3（测试）与 13.2（散列），题型按实际用到的节标注。
- **结论**：语料（2021–2026s）里的每一种考法都在 2027–29 考纲之内，没有题型需要标「不再考」。
- **考纲有、语料少见或未考**：从栈 / 队列删除以外的「从链表删除」已考（LT-02）；用其他 ADT 或内置类型实现字典 ADT（19.1）未在 P4 出现；随机文件（20.2 serial / sequential / random）在 P4 未出现，且源文件不含二进制文件，P4 实际只考文本文件（FL 章）；Big O（19.1）只在 P3 考。
