## AI　人工智能：核心概念 {#core-AI}

英文列带 ⟦⟧ 的是该题 MS 原文；标“非 MS 原句”的是标准定义（核验语料里没有可直接引用的 MS 句子，或唯一的 MS 在 s26 模考卷），作答时以所答那题的 MS 为准。

### 图与寻路（18.1）

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Graph（in AI） | 「A graph is used in AI to record relationships between entities」⟦9618_s25_31:10(a)⟧ | 由结点和边组成、用来记录实体之间关系的结构；AI 问题可以表述成在图上找路径 | 地铁线路图 | P3-AI-01 |
| Node / vertex | 「A graph uses vertices/nodes to identify/represent entities such as destinations, people, etc」⟦9618_s25_32:6(a)⟧ | 图中表示实体（地点、人等）的点 | 地铁站 | P3-AI-01 |
| Edge | 「Edges are used to connect nodes and can represent possible paths between them」⟦9618_s25_32:6(a)⟧ | 连接两个结点的线，表示关系或可走的路径 | 两站之间的轨道 | P3-AI-01 |
| Weight | 「Nodes/edges can be labelled/weighted」⟦9618_s25_32:6(a)⟧ | 结点或边上的数值，含义由应用决定（距离、时间、代价） | 线路旁标的分钟数 | P3-AI-01、P3-AI-03、P3-AI-04 |
| Purpose of A* / Dijkstra | 「to find the optimal / shortest / most cost-effective route」⟦9618_s23_31:2(b)⟧ | 在图上两个结点之间，按距离 / 代价 / 时间找最优路线 | 导航软件算路线 | P3-AI-02 |
| Dijkstra’s algorithm | 「Dijkstra’s just explores all possible routes」⟦9618_s25_33:10(b)⟧ | 起点设 0、其余设 ∞；每次访问未访问结点中距离最小的一个，更新其邻点的距离，直到全部确定；得到起点到每个结点的最短距离 | 墨水从起点一圈圈渗开 | P3-AI-02、P3-AI-03 |
| A* algorithm | 「A* tries to find a better path (between two points) by using a heuristic function」⟦9618_s25_33:10(b)⟧ | 每次扩展 f = g + h 最小的结点，用启发值引导搜索朝终点方向，求起点到一个终点的路径 | 带着指南针走路 | P3-AI-02、P3-AI-04 |
| Heuristic (h) | 「The heuristic function on the A* algorithm gives priority to nodes that are supposed to be better than others / less costly than others」⟦9618_s25_33:10(b)⟧ | 从某结点到终点代价的估计值，题图里写在结点旁，终点为 0 | “离终点大概还有多远” | P3-AI-02、P3-AI-04 |
| g and f = g + h | g is the actual cost of the path from the start node to this node; f = g + h is the estimated total cost of a route through this node.（非 MS 原句） | g：从起点到该结点已走路径的累计代价；f：经过该结点到终点的总估计代价，A* 按 f 选择 | 已走的路 + 还剩的估计 | P3-AI-04 |

### 机器学习（18.1）

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Machine learning | Machine learning is a branch of AI in which a system improves its performance at a task by learning from data, without being explicitly programmed for every case.（非 MS 原句） | 让计算机从数据中学习、改进表现，而不是为每种情况逐条编程 | 学生做题越多越会做 | P3-AI-05 |
| Supervised learning | 「Supervised learning uses labelled data」⟦9618_s25_32:6(b)⟧ | 用有标签数据（输入配已知正确输出）训练，需要人工准备；学会后根据过去的数据预测新结果 | 做带答案的练习册 | P3-AI-05 |
| Labelled data | 「Labelled data means that known outcomes are applied to specific inputs to help the AI predict outcomes」⟦9618_s25_32:6(b)⟧ | 每个输入都配有已知结果的数据 | 写了名字的照片 | P3-AI-05 |
| Unsupervised learning | 「They discover hidden patterns / data groupings / clusters without the need for human intervention」⟦9618_s25_33:10(c)⟧ | 用无标签数据，由算法自己分析、聚类，找出隐藏的模式、分组、相似与不同 | 把一堆没写名字的照片自己分组 | P3-AI-05 |
| Reinforcement learning | 「Reinforcement learning is a machine learning technique based on feedback / rewards / punishment」⟦9618_s24_32:11⟧ | 智能体在环境中执行动作、看结果，好动作得奖励、坏动作受惩罚，靠反馈不断改进 | 学骑自行车，摔了就调整 | P3-AI-05 |
| Artificial neural network | 「An artificial neural network is the component of artificial intelligence that is meant to simulate the functioning of a biological brain」⟦9618_w23_31:12⟧ | 模仿生物大脑的结构：大量相互连接的结点分成输入层、隐藏层、输出层，连接带权 | 一张由“神经元”连成的网 | P3-AI-06 |
| Layers | 「Artificial neural networks can be layered (input, hidden and output layers)」⟦9618_w23_31:12⟧ | 输入层接收数据，隐藏层逐层分析、提取特征，输出层给出结果 | 流水线上的一道道工序 | P3-AI-06 |
| Weights | 「Weights are adjusted through training to give a more accurate result」⟦9618_w23_31:12⟧ | 结点之间每条连接上的数值，决定信号的影响大小；训练就是调整权重 | 每个旋钮拧多大 | P3-AI-06、P3-AI-07 |
| Deep learning | 「Deep learning is a branch of machine learning」⟦9618_w25_31:7(b)⟧ | 使用很多隐藏层的人工神经网络的机器学习，逐层分析大量（非结构化）数据，找出隐藏模式 | 一层看线条，下一层看五官，再下一层认出猫 | P3-AI-06 |
| Reasons for deep learning | 「Deep learning makes good use of unstructured data」⟦9618_w22_31:9(b)⟧ | 善于处理非结构化、大量数据，能找出人难以发现的模式；隐藏层越多结果越准 | 照片、录音这类没填表格的数据也能用 | P3-AI-06 |
| Back propagation of errors | 「Initial outputs are compared to expected outputs」⟦9618_w25_32:9(b)⟧ | 把输出与期望比较得到误差，用误差梯度把结果从输出层反馈回网络，调整各结点权重，反复直到更准确 | 投篮偏了，往回找是哪个动作的问题再改 | P3-AI-07 |
| Error gradient | 「Calculus is used to find the error gradient in the obtained outputs」⟦9618_w25_32:9(b)⟧ | 误差随各权重变化的快慢与方向，用来决定每个权重该改多少、往哪边改 | 下山时脚下哪边最陡 | P3-AI-07 |
| Regression methods | Regression is a supervised learning technique that finds a mathematical function (a best-fit line or curve) describing how independent variables affect a dependent variable, so that outcomes can be predicted.（非 MS 原句） | 一种监督学习技术：找出自变量与因变量之间的函数关系（拟合直线或曲线），用来预测趋势和结果，目标是使预测值与实际值的差最小 | 根据房屋面积画一条线来估房价 | P3-AI-07 |
