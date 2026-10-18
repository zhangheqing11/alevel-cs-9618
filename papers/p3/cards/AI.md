## AI　人工智能 {#ch-AI}

<!-- auto:chapter-stats -->

### 核心思想

考纲只有 18.1 一节，内容分成两半，答法完全不同：

| 半边 | 回答的问题 | 题型 | 答法 |
|:--|:--|:--|:--|
| **图与寻路** | 图怎样帮 AI 表示关系；怎样在图上找最短路径 | AI-01 ～ AI-04 | AI-01、AI-02 是文字题；AI-03、AI-04 是**计算题**（各 5 分），照逐步模板做 |
| **机器学习** | 机器怎样从数据中学；神经网络、深度学习怎样工作；怎样修正误差 | AI-05 ～ AI-07 | 全是文字题，MS 列的点比满分多 |

图与寻路这半边按顺序学：

1. **图**（AI-01）：结点（node / vertex）表示实体（地点、人），边（edge）表示关系或可走的路，边上的权（weight）表示距离、代价、时间。考纲注明：**不要求写建图或搜索图的算法代码**。
2. **两种寻路算法的目的与区别**（AI-02）：都是找两点间代价最小的路径；Dijkstra 不加引导地向外扩展所有可能路线，A* 多了启发值 h，优先扩展“看起来离终点更近”的结点。
3. **在图上手算**：Dijkstra（AI-03）求起点到**每个**结点的最短距离；A*（AI-04）在表里逐行算 g、h、f，求起点到**一个**终点的路径。

机器学习这半边是一条“学习方式 → 实现工具 → 修正方法”的链：

1. **学习类别**（AI-05）：监督学习用带标签的数据（输入配已知正确输出），学会预测；无监督学习用无标签数据，自己找模式、分组；强化学习在环境里试错，靠奖励 / 惩罚反馈学习。
2. **人工神经网络与深度学习**（AI-06）：神经网络模仿人脑，输入层 → 隐藏层 → 输出层，结点之间的连接带权；隐藏层很多就是深度学习，擅长从大量非结构化数据里找隐藏模式。
3. **反向传播与回归**（AI-07）：输出与期望比较得到误差，把误差从输出层往回传、调整各层权重，反复迭代；回归是从数据中找输入与（连续的）输出之间的关系，用来预测。

文字题的写法与前几章相同：按 MS 的“点 + …展开”结构，**一句一个得分点**，满分 n 就写 n 句以上；“描述 / 解释”某种学习时，要写**这一种**特有的东西（标签、奖惩、隐藏层），不要写放到哪种 AI 都成立的泛泛之谈。

### 题型树
<!-- auto:type-tree -->

### P3-AI-01　图的结构与在 AI 中的用途　{#P3-AI-01}

<!-- auto:stats P3-AI-01 -->

**考法**　①描述 AI 系统里图的结构（2 分）；②描述图在 AI 系统里的用途（2 分）；③解释图怎样帮助 AI（3 分，2021）。

**识别信号**　graph；Artificial Intelligence；Describe the structure of a graph；Describe the purpose of a graph；use of graphs to aid AI。

**解题思路**
1. **结构**（一句一个组成部分）：

| 组成 | 说法 |
|:--|:--|
| 结点 / 顶点 | 表示实体，如目的地、人 |
| 边 | 连接结点，表示可能的路径；路径 = 两结点之间由边相连的一串结点 |
| 权 / 标签 | 结点或边可以带标签或权，权的含义由应用决定（距离、时间、代价） |
| 环 | 回到同一结点的一串结点 |

2. **用途**（“做什么 → 用什么 → 举例”）：记录实体之间的关系 → 用结点和边 → 例如表示地图上的地点与它们之间的距离，用来找最短路线。
3. **帮助 AI 的方式**（2021 题）：人工神经网络可以用图表示；AI 问题可以表述成“在图里找路径”；图可以交给 A*、Dijkstra 等算法分析。

**得分表述**（引自对应 MS）
- 「A graph uses vertices/nodes to identify/represent entities such as destinations, people, etc」⟦9618_s25_32:6(a)⟧
- 「Edges are used to connect nodes and can represent possible paths between them」⟦9618_s25_32:6(a)⟧
- 「Nodes/edges can be labelled/weighted」⟦9618_s25_32:6(a)⟧
- 「A graph is used in AI to record relationships between entities」⟦9618_s25_31:10(a)⟧
- 「for example, to represent places on a map and the distances between them, in order to find the shortest route」⟦9618_s25_31:10(a)⟧
- 「AI problems can be defined/solved as finding a path in a graph」⟦9618_s21_31:5(b)⟧

**易错与失分**
- 只写“图由结点和边组成”一句：考官报告指出，考生一般知道图由结点和边组成、可以带权，**写出不止一点**的才拿到两分（⟦9618_s25_32:6(a)⟧）。结点、边、权各写一句。
- 结构和用途混写：问 structure 写组成部分；问 purpose 写“记录实体间关系 + 举例找最短路线”。
- 写成数据结构 ADT 的定义（“图是一种 ADT，有 add node 操作”）：那是 CT-05 的角度，这里要联系 AI。

#### 代表题精讲　⟦9618_s25_32:6(a)⟧

**在考什么**　Describe the structure of a graph as used in an Artificial Intelligence (AI) system. 2 分，MS 列 4 点（Max 2）。

**完整作答**
1. 图用结点（顶点）表示实体，例如目的地、人。
2. 边连接结点，可以表示结点之间可能的路径。
3. 结点或边可以带标签 / 权，权的含义按具体应用而定（如距离）。

**与 MS 对齐**　1 ← MP1；2 ← MP2；3 ← MP3。三个独立得分点，满分 2。MP4（环）也可以替换任何一句。

**英文作答句**　A graph uses vertices/nodes to represent entities such as destinations or people. Edges are used to connect nodes and can represent possible paths between them. Nodes/edges can be labelled/weighted, and the weighting is used in the context of the application, for example distance.

**直观**　地铁线路图就是一张图：站点是结点，两站之间的线路是边，线路旁标的分钟数就是权。

**下一道变式**　⟦9618_s25_31:10(a)⟧　（换问 purpose，2 分：记录实体之间的关系 → 用结点和边；或举例“表示地图上的地点和距离，用来找最短路线”。）

<!-- auto:drills P3-AI-01 -->

### P3-AI-02　A* 与 Dijkstra 算法：目的与区别　{#P3-AI-02}

<!-- auto:stats P3-AI-02 -->

**考法**　①描述 / 说出 A* 和 Dijkstra 两种算法的目的（1–2 分）；②说出一种在图上找两点最短距离的 AI 算法（1 分）；③概述 A* 与 Dijkstra 的区别（2 分）。

**识别信号**　purpose of (both) the A* algorithm and Dijkstra’s algorithm；Identify one AI algorithm to find the shortest distance；difference between the A* and Dijkstra’s algorithms。

**解题思路**
1. **目的**（两种算法相同，写成“找什么 → 在哪里 → 按什么衡量”三截）：找最优 / 最短 / 代价最小的路线 → 在图上两个结点之间 → 按距离 / 代价 / 时间衡量。
2. **算法名**：A* algorithm 或 Dijkstra’s algorithm（写全名）。
3. **区别**（每句两边对照）：

| | Dijkstra | A* |
|:--|:--|:--|
| 怎样选下一个结点 | 只看从起点走过来的代价，向外探索所有可能路线 | 另加启发函数 h（到终点的估计），用 f = g + h 优先扩展更有希望 / 代价更低的结点 |
| 结果 | 起点到**所有**结点的最短距离 | 起点到**一个**终点的路径，通常不必走遍所有结点 |

**得分表述**（引自对应 MS）
- 「to find the optimal / shortest / most cost-effective route」⟦9618_s23_31:2(b)⟧
- 「based on distance / cost / time」⟦9618_s23_31:2(b)⟧
- 「To find the path between two points on a graph using the algorithm」⟦9618_s25_33:10(a)⟧
- 「A* tries to find a better path (between two points) by using a heuristic function」⟦9618_s25_33:10(b)⟧
- 「Dijkstra’s just explores all possible routes」⟦9618_s25_33:10(b)⟧
- 「The heuristic function on the A* algorithm gives priority to nodes that are supposed to be better than others」⟦9618_s25_33:10(b)⟧

**易错与失分**
- 区别只写 A* 一边：考官报告指出，常见的得分答案是“A* 用启发函数找更好的路径”或“Dijkstra 只是探索所有可能路线”（⟦9618_s25_33:10(b)⟧）。两边各写一句最稳。
- 目的写成“找路径”而不说“最短 / 最优”和“两结点之间”：考官报告指出，大多数考生能写出“在图上找两结点之间的最优路径”这类答案（⟦9618_s23_31:2(b)⟧），三截都要有。
- ⟦9618_s25_33:10(b)⟧ 的 MS 还列了一点“Dijkstra 不能处理负权 // A* 可以处理负权”。这只是该题 MS 接受的一种说法，不是普遍规律（A* 一般也不处理负权），学习时不要把它当作两种算法的主要区别来背；作答优先写启发函数那两点。

#### 代表题精讲　⟦9618_s25_33:10(b)⟧

**在考什么**　Outline the difference between the A* and Dijkstra’s algorithms. 2 分，MS 列 4 点（Max 2），MP2 以 “…” 开头，接在 MP1 后面。

**完整作答**
1. A* 用启发函数，试图找到（两点之间）更好的路径；
2. ……Dijkstra 只是探索所有可能的路线。
3. A* 的启发函数让被认为更好 / 代价更低的结点优先。

**与 MS 对齐**　1 ← MP1；2 ← MP2（接在 1 后才完整）；3 ← MP3。三个独立得分点，满分 2。

**英文作答句**　A* tries to find a better path between two points by using a heuristic function, whereas Dijkstra’s just explores all possible routes. The heuristic function on the A* algorithm gives priority to nodes that are supposed to be better / less costly than others.

**直观**　Dijkstra 像往池塘里扔石子，水波向四面八方一圈圈扩开，直到碰到目标；A* 像带着指南针走路，每一步都优先往目标方向走。

**下一道变式**　⟦9618_s23_31:2(b)⟧　（描述两种算法共同的目的，2 分：最优 / 最短路线 → 两结点之间 → 按距离 / 代价 / 时间。）

<!-- auto:drills P3-AI-02 -->

### P3-AI-03　用 Dijkstra 算法求最短距离　{#P3-AI-03}

<!-- auto:stats P3-AI-03 -->

**考法**　给一张带权无向图，求起点到其余**每个**结点的最短距离，在图上或 working 区写过程，答案填进表格。5 分：过程（working）最多 3 分 + 答案最多 2 分（六个全对 2 分，四或五个对 1 分；2021 年口径是四个对 1 分、全对再 1 分）。

**识别信号**　Calculate the shortest distance between the Start and each of …；using Dijkstra’s algorithm；Show your working and write your answers in the table provided。

**解题思路（逐步作答模板）**
1. **初始化**：起点写 0，其余结点全部写 ∞。（这两句各是一个得分点，一定要在图上或 working 里**写出来**。）
2. **选结点**：从“未访问”的结点里选当前距离最小的一个，标记为**已访问**（visited，打勾或画圈）——它的距离从此确定。
3. **更新邻点**：对它每个未访问的邻点，算“它的距离 + 边权”；比邻点现有的值小就**改写**（旧值划掉，新值写旁边）。
4. 重复 2–3，直到所有结点都已访问。
5. 把每个结点最后的值填进答案表。

过程分来自：初始化（起点 0、其余 ∞）、更新值的痕迹、已访问标记、至少一条路线的正确计算、**至少一个结点算过不止一条路线**。所以 working 里写一张“每一步的距离表”最稳（见下）。这张表是教学用的写法，MS 不规定格式：在图上每个结点旁写值、划掉旧值、打勾标已访问，同样给分。

**得分表述**（引自对应 MS）
- 「Initialisation – setting Start to 0」⟦9618_w23_32:8⟧
- 「and the rest of the towns to ∞」⟦9618_w25_33:8⟧
- 「Evidence to show values at nodes being updated」⟦9618_w23_32:8⟧
- 「Evidence to show ‘visited node(s)’」⟦9618_w23_32:8⟧
- 「Evidence to show more than one route has been calculated for at least one town」⟦9618_w23_32:8⟧
- 「Two marks for all six correct values」⟦9618_w23_32:8⟧

**易错与失分**
- 只写答案不写过程：考官报告指出，考生的最短距离很少算错，但过程常常不够清楚、对不上得分点；初始化（起点 0、其余 ∞）、标出已访问结点、写清至少一条路线的计算、展示同一结点的不同路线比较，都是要写出来的过程分（⟦9618_w25_33:8⟧）。
- 考官报告指出，只有少数考生写出了“起点设 0、其余设 ∞、标出已访问结点”这些更完整的 Dijkstra 过程（⟦9618_s21_32:5(a)⟧）。
- 只沿一条路一直走（“贪心”）：Dijkstra 每轮都在**所有**未访问结点里选最小的，不是只看刚访问结点的邻居。
- 已访问的结点又被改小：边权都非负时（真题都是），一旦访问，距离就确定了；如果你发现还能改小，说明前面选错了结点。

#### 代表题精讲　⟦9618_w23_32:8⟧

**在考什么**　讲解时请对照原卷 QP p.7（图与答案表在同一页）与 MS p.6。Calculate the shortest distance between the Start and each of the destinations in the diagram using Dijkstra’s algorithm. 5 分。图的边（按原页）：Start–A 8，Start–F 10，A–B 4，B–C 8，B–D 2，D–E 2，C–E 3，C–F 9，E–F 7。

**完整作答**　working（教学格式，比 MS 多：每行是“访问一个结点之后”各结点的当前距离；粗体 = 本行确定的结点；括号里是比较过但没采用的值或被改掉的旧值）：

| 步 | 访问 | A | B | C | D | E | F |
|:--|:--|:--|:--|:--|:--|:--|:--|
| 初始 | Start = 0 | ∞ | ∞ | ∞ | ∞ | ∞ | ∞ |
| 1 | Start（0） | 8 | ∞ | ∞ | ∞ | ∞ | 10 |
| 2 | A（8） | **8** | 8 + 4 = 12 | ∞ | ∞ | ∞ | 10 |
| 3 | F（10） |  | 12 | 10 + 9 = 19 | ∞ | 10 + 7 = 17 | **10** |
| 4 | B（12） |  | **12** | 19（12 + 8 = 20，不改） | 12 + 2 = 14 | 17 |  |
| 5 | D（14） |  |  | 19 | **14** | 14 + 2 = 16（17 改为 16） |  |
| 6 | E（16） |  |  | 19（16 + 3 = 19，相等不改） |  | **16** |  |
| 7 | C（19） |  |  | **19** |  |  |  |

答案：A 8，B 12，C 19，D 14，E 16，F 10。

**与 MS 对齐**　过程分（Max 3）：“初始”一行 ← MP1（Start 0）与 MP2（其余 ∞）；每行改写的值 ← MP3；“访问”一列 ← MP4；任一条算式如 8 + 4 = 12 ← MP5；E 先得 17 后改 16、C 比较了 19 / 20 / 19 ← MP6。六个都有，过程满 3 分。答案（Max 2）：六个全对 2 分。

注意 MS 原页 MP2 印作 “…and the rest of the towns to”，∞ 符号漏印；同样的得分点在 ⟦9618_w25_33:8⟧ 的 MS 里印全了。

**英文作答句**　（答案表照填数字即可；working 里可用这样的短句标注）Initialise: Start = 0, all other nodes = ∞. Visit Start: A = 8, F = 10. Visit A: B = 8 + 4 = 12. Visit F: C = 10 + 9 = 19, E = 10 + 7 = 17. Visit B: D = 12 + 2 = 14; C via B = 20 > 19, no change. Visit D: E via D = 14 + 2 = 16 < 17, update E to 16. Visit E: C via E = 16 + 3 = 19, no change. Visit C.

**直观**　像墨水从起点慢慢渗开：每次都是“离起点最近、还没被墨染到”的那个点先被染上，染上的点就不会再变；墨水沿着每条边继续往外渗，遇到更短的渗法就改写邻居的数字。

**下一道变式**　⟦9618_w25_33:8⟧　（同样 5 分，结点 T、V、W、X、Y、Z；Start–Y 直连 22，但绕 T、V、W、X 走只要 21——专门考你会不会改写。）

<!-- auto:drills P3-AI-03 -->

### P3-AI-04　用 A* 算法求路径　{#P3-AI-04}

<!-- auto:stats P3-AI-04 -->

**考法**　给一张带权图，每个结点旁标了启发值 h，表格前两行已填好；用 A* 在表里逐行写出 g、h、f = g + h，最后写出起点到终点的路径。5 分：计算行最多 4 分（MS 按“某几行”给分）+ 最终路径 1 分。

**识别信号**　using the A* algorithm；Show your working in the table provided；The first two rows (in the table) have (already) been completed；表头 Cost from start node (g) / Heuristic (h) / Total (f = g + h)；Final path。

**解题思路（逐步作答模板）**
1. **读图**：边上的数字是两结点之间的代价；**结点旁边**的数字是该结点的 h（到终点的估计），终点的 h 为 0。题目通常在某一个结点旁写明 “h = …、g = …” 作示例。
2. **从起点扩展**：起点的每个邻点各写一行：g = 边权，h 照图抄，f = g + h。
3. **选下一个**：在所有**写过但还没扩展**的行里选 f 最小的结点扩展。
4. **扩展**：对它的每个邻点写一行，g = 当前结点的 g + 边权（写出加法，如 5 + 2 = 7），h 照抄，f = g + h。若某邻点已经有更小的 g，不必再写这一行。
5. 重复 3–4，直到**终点**成为 f 最小的那一行。
6. **写路径**：从终点那一行往回找“从哪个结点来”，写成 起点 ⇨ … ⇨ 终点。

**得分表述**（引自对应 MS）
- 「Node G (from C) (Line 6 in table)」⟦9618_s23_32:10(b)⟧
- 「Node F and Node End (from G) (Lines 7 and 8 in table)」⟦9618_s23_32:10(b)⟧
- 「Node End (from F) (Line 9 in table)」⟦9618_s23_32:10(b)⟧
- 「One mark for correct path (Max 1)」⟦9618_s23_32:10(b)⟧
- 「Begin ⇨ C ⇨ G ⇨ F ⇨ End」⟦9618_s23_32:10(b)⟧

**易错与失分**
- 只写路径不写表：考官报告指出，有的考生没有完整的过程也写出了最终路径，但得分最高的是既有正确路径、又有完整过程的答案（⟦9618_s23_32:10(b)⟧）。路径只值 1 分，表里的行值 4 分。
- g 只写边权：g 是**从起点累计**的代价（5 + 2 + 4 = 11），不是最后一条边。
- 把结点旁的 h 当成边权，或把边权当 h：先在图上分清“线上的数”和“圈旁的数”。
- 选了 g 最小或 h 最小的结点扩展：A* 每次比的是 **f**。

#### 代表题精讲　⟦9618_s23_32:10(b)⟧

**在考什么**　讲解时请对照原卷 QP p.12（图与表格在同一页）与 MS p.11。Calculate the path that takes the shortest time to travel from the Begin node to the End node, using the A* algorithm. 5 分。图（按原页）：边 Begin–A 5，Begin–B 6，Begin–C 5，Begin–D 4，A–E 6，A–End 8，B–End 7，C–G 2，D–G 6，E–F 7，F–End 1，F–G 4，G–End 7；h：Begin 12，A 8，B 7，C 7，D 11，E 8，F 1，G 5，End 0。

**完整作答**

| 行 | Start node | Destination node | g | h | f = g + h |
|:--|:--|:--|:--|:--|:--|
| 1 | Begin | Begin | 0 | 12 | 12 |
| 2 | Begin | A | 5 | 8 | 13 |
| 3 | Begin | B | 6 | 7 | 13 |
| 4 | Begin | C | 5 | 7 | 12 |
| 5 | Begin | D | 4 | 11 | 15 |
| 6 | C | G | 5 + 2 = 7 | 5 | 12 |
| 7 | G | F | 5 + 2 + 4 = 11 | 1 | 12 |
| 8 | G | End | 5 + 2 + 7 = 14 | 0 | 14 |
| 9 | F | End | 5 + 2 + 4 + 1 = 12 | 0 | 12 |

Final path：Begin ⇨ C ⇨ G ⇨ F ⇨ End（总时间 12）。

（“行”一列是教学加的编号，对应 MS 说的 Line 3、Line 6 等；答卷的表格没有这一列，从第 3 行起直接填。）

为什么这样选：第 2–5 行里 C 的 f = 12 最小 → 扩展 C 得 G（12）；G 的 f = 12 最小 → 扩展 G 得 F（12）与 End（14）；G 的另一邻点 D 经 G 的代价 7 + 6 = 13 比已有的 4 大，不写；F 的 f = 12 最小 → 扩展 F 得 End（12）；此时 End 的 f = 12 是最小的，结束。

**与 MS 对齐**　第 3、4、5 行各是一个点（Max 2）；第 6 行、第 7 和 8 行、第 9 行各是一个点（Max 2）；路径 1 分。表与 MS 的范答逐行相同（MS 的表留了最后一行空白）。

**英文作答句**　（本题是填表题，按上表填写；Final path 一栏写）Begin ⇨ C ⇨ G ⇨ F ⇨ End

**直观**　A* 每走一步都问两个问题：“我已经走了多远（g）？离终点估计还有多远（h）？”两者加起来最小的方向先走。Begin 到 A 虽然近，但 A 离终点还远（h = 8），所以先去 C。

**下一道变式**　⟦9618_w21_31:9(b)⟧　（2021 扩展题，核验语料除 s26 外没有第二道 A* 计算题。Home 到 School，前两行已给，共 9 行；注意第 5 行的 B（经 A）与第 7 行的 F，f 都是 11，MS 扩展的是 h 更小的 F。）

<!-- auto:drills P3-AI-04 -->

### P3-AI-05　机器学习的类别　{#P3-AI-05}

<!-- auto:stats P3-AI-05 -->

**考法**　①说出一个机器学习类别（1 分）；②连线：类别 → 最合适的描述（4 分）；③描述监督学习和无监督学习、解释两者怎样不同 / 怎样训练（3–4 分）；④解释无监督学习怎样进行（3 分）；⑤解释强化学习（3 分）。

**识别信号**　category of machine learning；supervised / unsupervised / reinforcement learning；Draw one line from each machine learning category；differ from each other；how … takes place；Reinforcement Learning in relation to AI。

**解题思路**
1. 三种学习方式，各记住一个关键词和一条“怎样学”：

| 类别 | 关键词 | 怎样学 |
|:--|:--|:--|
| 监督学习 supervised | **labelled** data | 用已知正确输出的样本（输入—输出对）训练，需要人先给数据贴标签；学会后根据过去的数据预测新输入的结果 |
| 无监督学习 unsupervised | **unlabelled** data | 只给输入、不给正确输出；算法自己分析数据、聚类，找出隐藏的模式、分组、相似与不同，不需要人工干预 |
| 强化学习 reinforcement | **reward / punishment** | 智能体（agent）在环境里执行动作、看结果；好动作得到正反馈（奖励），坏动作得到负反馈（惩罚）；不靠标签数据，靠反馈不断改进 |

2. **连线题**（⟦9618_s23_31:2(a)⟧ 的四个类别）：监督 → 用示例输入—输出对把输入映射到输出；强化 → 在交互环境里靠自身经验试错；深度学习 → 模拟人脑的数据处理能力来做决策；无监督 → 让过程自己发现以前没发现的模式。剩下“传递神经网络产生的误差信息”那一条是干扰项（它说的是反向传播）。
3. **区别 / 怎样训练题**：按“数据有没有标签 → 标签意味着什么 → 要不要人工 → 学到的是什么”写，每句两边对照。

**得分表述**（引自对应 MS）
- 「Supervised learning uses labelled data // Unsupervised learning makes use of unlabelled data」⟦9618_s25_32:6(b)⟧
- 「Labelled data means that known outcomes are applied to specific inputs to help the AI predict outcomes」⟦9618_s25_32:6(b)⟧
- 「Able to predict future outcomes based on past data」⟦9618_w22_32:7⟧
- 「They discover hidden patterns / data groupings / clusters without the need for human intervention」⟦9618_s25_33:10(c)⟧
- 「Reinforcement learning is a machine learning technique based on feedback / rewards / punishment」⟦9618_s24_32:11⟧
- 「enables learning in an interactive environment by trial and error using its own experiences」⟦9618_s23_31:2(a)⟧

**易错与失分**
- 只写“有标签 / 无标签”就停：考官报告指出，考生大多知道监督用有标签数据、无监督用无标签数据，再进一步说明“已知结果 / 未知结果”的才拿到更高分（⟦9618_s25_32:6(b)⟧）；描述题完全正确的答案很少（⟦9618_w22_32:7⟧）。
- 无监督少了“相似与不同”：考官报告指出很少有人拿到第三分，因为没有补上“能发现数据中的相似与不同”（⟦9618_s25_33:10(c)⟧）。
- 强化学习写成泛泛的 AI 描述：考官报告指出，得分最高的是专门针对强化学习、而不是放到许多 AI 领域都成立的答案；能在“奖励与惩罚”上展开的才拿到一分以上（⟦9618_s24_32:11⟧）。
- 把“`//` 两边”当两分：MP1 写“监督用有标签、无监督用无标签”两半，只算 1 分。

#### 代表题精讲　⟦9618_s25_32:6(b)⟧

**在考什么**　Explain how supervised learning and unsupervised learning differ from each other. 4 分，MS 列 6 点（Max 4）；MP1、MP3 内部的 `//` 是同一点的两种说法；MP5、MP6 以 “…” 开头，依次接在 MP4 后面。

**完整作答**
1. 监督学习使用有标签的数据，而无监督学习使用无标签的数据。
2. 有标签的数据是指给特定的输入配上已知的结果，帮助 AI 预测结果。
3. 监督学习需要先有人工输入 / 训练，无监督学习不需要。
4. 无监督学习用的是无标签数据，结果是未知的，
5. ……AI 必须自己寻找隐藏的模式、结构或聚类。

**与 MS 对齐**　1 ← MP1；2 ← MP2；3 ← MP3；4 ← MP4；5 ← MP5。五个独立得分点，满分 4。可以在 5 之后补“……在数据中寻找，以便预测结果”（MP6）。

**英文作答句**　Supervised learning uses labelled data, whereas unsupervised learning makes use of unlabelled data. Labelled data means that known outcomes are applied to specific inputs to help the AI predict outcomes. Supervised learning requires initial human input/training, but unsupervised learning does not. With unlabelled data in unsupervised learning, outcomes are not known, so the AI has to search for hidden patterns, structures or clusters within the data.

**直观**　监督学习像做带答案的练习册，做完对答案、改错；无监督学习像把一堆没写名字的照片自己分成几组；强化学习像学骑自行车，没人告诉你答案，摔了（惩罚）就调整，骑稳了（奖励）就记住。

**下一道变式**　⟦9618_s24_32:11⟧　（Explain what is meant by Reinforcement Learning，3 分：基于反馈 / 奖惩的技术 → 智能体在环境中执行动作、看结果 → 好动作正反馈、坏动作负反馈。）

<!-- auto:drills P3-AI-05 -->

### P3-AI-06　人工神经网络与深度学习　{#P3-AI-06}

<!-- auto:stats P3-AI-06 -->

**考法**　①解释什么是人工神经网络、它怎样让机器学习（4 分）；②描述 / 解释深度学习（2–5 分）；③深度学习的使用理由（2 分）；④深度学习的一个应用例子、怎样让它更有效（各 1 分）；⑤多个隐藏层的理由（1 分，2021）。

**识别信号**　artificial neural network；Deep Learning；hidden layers；Outline the reasons for using deep learning；State one example where Deep Learning is used；made more effective。

**解题思路**
1. **人工神经网络**（ANN），按“像什么 → 由什么组成 → 怎样学”写：
   - 模仿生物大脑的工作方式，是机器学习的关键组成部分；
   - 由大量相互连接的结点（神经元）组成，分层：输入层 → 一个或多个隐藏层 → 输出层；
   - 结点之间的连接带**权**；数据从输入层进入，在各隐藏层被分析、提取特征，输出层给出结果；
   - 通过训练**调整权重**，结果越来越准；数据越多效果越好。
2. **深度学习** = 机器学习的一个分支，使用**很多隐藏层**的人工神经网络：
   - 一层层分解、分析数据，找出人难以发现的隐藏模式（特征提取）；
   - 适合大数据量、非结构化数据（图像、语音、文本），可以包含不同的监督方式；
   - 用误差反向传播调整权重，提高准确度；隐藏层越多，能学的越复杂、结果越准。
3. **使用理由**（写“为什么用”，不是“它是什么”）：善于利用非结构化数据；数据量大时比其他方法表现好；能以非线性方式处理数据；善于找出人看不出或太复杂、太费时的模式；隐藏层越多结果越准。
4. **应用例子**写具体任务：图像 / 人脸识别、自动驾驶、自然语言处理、机器翻译、欺诈检测、聊天机器人等。**更有效**：增加隐藏层。

**得分表述**（引自对应 MS）
- 「An artificial neural network is the component of artificial intelligence that is meant to simulate the functioning of a biological brain」⟦9618_w23_31:12⟧
- 「Weights are adjusted through training to give a more accurate result」⟦9618_w23_31:12⟧
- 「Deep learning is a branch of machine learning」⟦9618_w25_31:7(b)⟧
- 「It is a structure consisting of many interconnected layers」⟦9618_w25_31:7(b)⟧
- 「Deep learning makes good use of unstructured data」⟦9618_w22_31:9(b)⟧
- 「Use / introduce more hidden layers」⟦9618_w25_32:9(a)(ii)⟧

**易错与失分**
- 写泛泛的 AI 描述：考官报告指出，得分最高的是专门针对深度学习、而不是放到许多 AI 领域都成立的答案（⟦9618_s24_31:9⟧）。要写出“很多隐藏层”“找隐藏模式”这类深度学习特有的点。
- “理由”写成“定义”：考官报告指出，有的考生在问使用理由的小问里写的是深度学习是什么，那属于上一小问（⟦9618_w22_31:9(b)⟧）。
- 应用例子写 “ANN”“AI” 或商品名：考官报告指出这些泛泛的答案和 ChatGPT 这类商品名都不给分（⟦9618_w25_32:9(a)(i)⟧）。写 “natural language processing”“image recognition”。
- 解释 ANN 怎样让机器学习时只描述监督 / 无监督学习：考官报告指出这样不够（⟦9618_w21_31:9(a)(ii)⟧），要写网络的层、权与训练过程。

#### 代表题精讲　⟦9618_w25_31:7(b)⟧

**在考什么**　Describe Deep Learning. 5 分，MS 列 10 点（Max 5）。带 “…” 的点要接在前一点后面：MP3 接 MP2，MP5、MP6 接 MP4，MP8 接 MP7。

**完整作答**
1. 深度学习是机器学习的一个分支。
2. 它使用人工神经网络，
3. ……以类似人脑的方式工作。
4. 它是由许多相互连接的层组成的结构，
5. ……包括输入层、隐藏层和输出层（输入层把数据送进第一个隐藏层，最后一个隐藏层送到输出层），
6. ……逐步分解、分析数据，找出隐藏的模式。
7. 它适合处理大数据集。
8. 深度学习用误差反向传播来调整参数 / 权重，改进结果、提高准确度。

**与 MS 对齐**　1 ← MP1；2 ← MP2；3 ← MP3；4 ← MP4；5 ← MP5；6 ← MP6；7 ← MP9；8 ← MP10。八个独立得分点，满分 5。

**英文作答句**　Deep learning is a branch of machine learning. It makes use of artificial neural networks to work in a similar manner to the human brain. It is a structure consisting of many interconnected layers: input, hidden and output, gradually breaking down and analysing the data to find hidden patterns. It works well with large data sets. Deep learning uses back propagation of errors to adjust the weightings to improve its accuracy.

**直观**　认一只猫：第一层隐藏层只看出边和线，下一层拼成耳朵、眼睛，再下一层拼成“猫脸”。层越多，能拼出的东西越复杂——这就是“深”。

**下一道变式**　⟦9618_w23_31:12⟧　（Explain what is meant by the term artificial neural network，4 分：模拟生物大脑 → 机器学习的关键部分 → 输入、隐藏、输出层 → 结点间有权、训练中调整权重。）

<!-- auto:drills P3-AI-06 -->

### P3-AI-07　反向传播与回归　{#P3-AI-07}

<!-- auto:stats P3-AI-07 -->

**考法**　①描述机器学习中的误差反向传播方法（4 分）；②解释机器学习中的回归方法（3 分）。考纲 18.1 把两者列为独立要求。核验语料里回归方法只出现在 s26 模考卷（D1 保留），本卡不引它的 MS。

**识别信号**　back propagation of errors；regression methods；in Machine Learning。

**解题思路**
1. **反向传播**（逐步作答模板，按一次训练循环的顺序写）：
   1. 把神经网络的初始输出与期望输出比较，得到误差；
   2. ……调整权重，使实际输出与期望输出的差距最小；
   3. 用微积分求出输出误差的梯度（error gradient）；
   4. ……把结果从输出层反馈回神经网络；
   5. ……按反馈调整每个结点 / 神经元的权重；
   6. ……重复这个过程，直到结果更准确。
2. **回归方法**（以下是标准说法，非 MS 原句，作答时以所答那题的 MS 为准）：一种**监督学习**技术；找出一个数学函数 / 拟合一条最合适的直线或曲线，描述自变量（原因）怎样影响因变量（结果）；用来预测趋势和结果；训练目标是让预测值与实际值的差最小。例：根据房屋面积预测房价。

**得分表述**（引自对应 MS）
- 「Initial outputs are compared to expected outputs」⟦9618_w25_32:9(b)⟧
- 「weightings are adjusted to minimise the difference between actual and expected outputs」⟦9618_w25_32:9(b)⟧
- 「Calculus is used to find the error gradient in the obtained outputs」⟦9618_w25_32:9(b)⟧
- 「weightings of each neuron / node are adjusted as a result of the feedback」⟦9618_w25_32:9(b)⟧
- 「the process repeats until results are more accurate」⟦9618_w25_32:9(b)⟧

**易错与失分**
- 步骤没有逻辑顺序：考官报告指出，最好的答案给出了方法的逻辑流程——输出与期望输出比较、调整权重缩小差距、用微积分求误差梯度、结果反馈回网络、按反馈重新调整结点权重、重复直到结果更准（⟦9618_w25_32:9(b)⟧）。
- 只写“把误差传回去”：要说清**比较什么**（实际输出与期望输出）、**调什么**（各结点的权重）、**做到什么时候**（反复直到更准确）。
- 把回归写成“回到上一步”：回归（regression）在这里是统计意义上“找变量之间的关系来预测”，和反向传播是两件事。

#### 代表题精讲　⟦9618_w25_32:9(b)⟧

**在考什么**　Describe the back propagation of errors method in Machine Learning. 4 分，MS 列 6 点（Max 4）；MP2 接 MP1，MP4–MP6 依次接在前一点后面，整体是一条流程。

**完整作答**
1. 把初始输出与期望输出比较，
2. ……调整权重，使实际输出与期望输出之间的差距最小。
3. 用微积分求出所得输出中的误差梯度，
4. ……把结果反馈回神经网络，
5. ……按反馈调整每个神经元 / 结点的权重，
6. ……重复这一过程，直到结果更准确。

**与 MS 对齐**　1–6 依次对应 MP1–MP6，满分 4。按顺序写满 6 句，即使有一两句说法不够准，也还能拿满分。

**英文作答句**　Initial outputs are compared to expected outputs, and the weightings are adjusted to minimise the difference between actual and expected outputs. Calculus is used to find the error gradient in the obtained outputs, and the results are fed back into the neural network. The weightings of each neuron / node are adjusted as a result of the feedback, and the process repeats until results are more accurate.

**直观**　投篮：投出去（输出），看偏了多少（与期望比较），判断是手腕还是手肘的问题、各该改多少（误差梯度，从结果往回找原因），调整动作（改权重），再投，直到命中率提高（迭代）。

**下一道变式**　⟦9618_w21_31:9(a)(ii)⟧　（2021 扩展题、AI-06 主题型：“ANN 怎样让机器学习”，MS 最后一点就是“用误差反向传播纠正错误”，练习把反向传播放进整个训练过程里讲。回归方法唯一一道 ⟦9618_s26_33:9(a)⟧ 在 s26 模考卷，模考前不做。）

<!-- auto:drills P3-AI-07 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| AI-01 vs CT-05 | 图在 AI 里表示什么、怎样帮 AI → AI-01；把图作为 ADT 与其他 ADT 比较 → CT-05 | Artificial Intelligence 是否出现 |
| AI-02 vs AI-03 / AI-04 | 用文字说目的、区别 / 在给定图上手算 | describe · outline 还是 calculate · show your working |
| AI-03 vs AI-04 | Dijkstra：到每个结点的最短距离，填一行答案 / A*：表里有 g、h、f 列，求到一个终点的路径 | each of the destinations 还是 heuristic · f = g + h · final path |
| Dijkstra vs A* 的选择规则 | 选当前距离（g）最小的未访问结点 / 选 f = g + h 最小的未扩展结点 | 题目有没有给 h |
| 边权 vs 启发值 h | 写在边上，两结点间的真实代价 / 写在结点旁，从该结点到终点的估计 | 数字在线上还是圈旁 |
| 监督 vs 无监督 | 有标签、已知结果、要人工训练、用来预测 / 无标签、结果未知、自己找隐藏模式与聚类 | labelled 还是 unlabelled |
| 强化学习 vs 监督学习 | 靠环境的奖惩反馈、试错，不用标签 / 靠标签数据的正确答案 | reward · punishment · trial and error |
| AI-05 vs AI-06 | 学习类别（连线题里深度学习只占一条线时仍归 AI-05）/ 神经网络、深度学习本身 | category 还是 neural network · hidden layers |
| AI-06 vs AI-07 | 整体描述深度学习或 ANN（可以顺带一句反向传播）/ 专门问反向传播或回归的过程 | Describe deep learning 还是 back propagation · regression |
| 反向传播 vs 回归 | 神经网络里把误差往回传、调整权重 / 找自变量与因变量之间的关系来预测 | neural network · weights 还是 best-fit · predict |
| AI-06 vs P1-EO-04 | ANN 与深度学习怎样工作 / AS 的 AI 应用与影响 | P3 卷还是 P1 卷 |
