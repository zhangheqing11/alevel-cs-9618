## CT　计算思维与问题求解：核心概念 {#core-CT}

英文列带 ⟦⟧ 的是该题 MS 原文；标“非 MS 原句”的是标准定义，作答时以所答那题的 MS 为准。写代码的部分（查找、排序、栈、队列、链表、二叉树的伪代码模板）在对应题型卡里。

### 查找、排序与效率

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Linear search | 「Linear search sequentially checks each element of the array / list」⟦9618_s24_32:8(b)⟧ | 从第一个元素起逐个比较，直到找到或到达末尾；数据不必有序 | 一页一页翻书找 | P3-CT-01、P3-CT-02 |
| Binary search | 「Binary search finds the mid-point of an array/list and determines which side contains the item to be found」⟦9618_s24_32:8(b)⟧ | 取中间元素比较，舍去不可能含目标的一半，对剩下一半重复，直到找到或范围为空 | 翻字典：每次翻中间、扔掉一半 | P3-CT-01、P3-CT-02 |
| Binary search condition | 「The list to be searched must be ordered/sorted」⟦9618_s22_32:8(b)(i)⟧ | 二分查找的前提：数据已排序（升序或降序） | 字典要按字母排好 | P3-CT-01 |
| Insertion sort | Takes each item in turn and inserts it into its correct position in the already sorted part of the list.（非 MS 原句） | 依次取出下一个元素，把已排好部分里比它大的元素后移，再放回空位 | 理扑克牌 | P3-CT-03 |
| Bubble sort | Repeatedly compares adjacent items and swaps them if they are in the wrong order.（非 MS 原句） | 反复比较相邻两个元素，逆序就交换；一趟把最大值送到末尾 | 气泡一个个浮上来 | P3-CT-03（AS 版见 P2-DT-08） |
| Big O notation | 「Big O notation is used to indicate the time/space complexity of an algorithm」⟦9618_s24_31:10(c)⟧ | 描述算法所需时间（或空间）随数据量增长的方式，通常指最坏情况 | 数据翻倍时，要多花多少时间 | P3-CT-04 |
| O(n) | 「Big O for linear search is O (n)」⟦9618_s24_32:8(b)⟧ | 线性时间：时间与数据量成正比 | 名字多一倍，翻的页也多一倍 | P3-CT-04 |
| O(log n) | 「O(log n) is a time complexity that uses logarithmic time」⟦9618_w22_31:12(b)(ii)⟧ | 对数时间：数据量指数增长时，时间只线性增长 | 1000 个要 10 次，100 万个只要 20 次 | P3-CT-04 |
| O(n²) | Time grows with the square of the number of items; the worst case of insertion sort and bubble sort.（非 MS 原句） | 平方时间：数据量翻倍，时间约变 4 倍 | 每个人都要和其他每个人握手 | P3-CT-04 |
| Factors affecting sort performance | 「The sort may take longer if the number of items to be sorted is larger」⟦9618_s25_33:12(c)⟧ | 数据项的个数；数据开始时的有序程度（部分有序时插入排序更快） | 牌越多越慢；牌本来就差不多排好时很快 | P3-CT-04 |

### 抽象数据类型（ADT）

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Abstract data type (ADT) | A collection of data together with the operations on that data, defined without saying how it is implemented.（非 MS 原句） | 一组数据加上对它的操作（如入栈、出栈），只规定“能做什么”，不规定怎样实现 | 遥控器上的按钮：只管按哪个键，不管里面电路 | P3-CT-05 |
| Stack | 「a stack is a first in last out / FILO / LIFO data structure」⟦9618_w23_31:10(c)⟧ | 后进先出：只在栈顶一端压入、弹出；只有一个移动的指针 | 一摞盘子 | P3-CT-05、P3-CT-06 |
| Queue | 「A queue is a first in first out / FIFO data structure」⟦9618_w23_31:10(c)⟧ | 先进先出：从队尾加入、从队首取出；有两个移动的指针 | 排队买票 | P3-CT-05、P3-CT-07 |
| Stack vs queue: access | 「A stack has only one moveable pointer whereas a queue has two」⟦9618_w23_31:10(c)⟧ | 栈在同一端进出，队列在两端分别进出 | 一个门进出 vs 前门出后门进 | P3-CT-05 |
| Uses of a stack | 「interrupt handling (storing contents of registers etc)」⟦9618_s22_31:5(c)⟧ | 递归、过程调用（保存返回地址）、中断处理（保存寄存器）、实现其他 ADT、RPN 求值 | 记“回来的路” | P3-CT-05、P3-CT-11 |
| Linked list | 「A linked list is a dynamic data structure / not restricted in size」⟦9618_w23_32:9(b)⟧ | 结点各含数据和指向下一个结点的指针；顺序由指针决定，可按需增删结点 | 寻宝纸条：每张写着下一张在哪 | P3-CT-05、P3-CT-08 |
| Array (static structure) | 「An array is a static data structure」⟦9618_w23_32:9(b)⟧ | 大小在声明时固定；用数组实现的栈满了就不能再扩展 | 固定格数的鸡蛋盒 | P3-CT-05 |
| Binary tree (ordered) | Each node has a left pointer and a right pointer; values smaller than a node are in its left subtree and larger values in its right subtree.（非 MS 原句） | 每个结点有左右两个指针；比结点小的在左子树、大的在右子树 | 比大小的分岔路 | P3-CT-09 |
| Graph | A set of nodes (vertices) joined by edges, which may have weights.（非 MS 原句） | 由结点和连接结点的边组成的 ADT；考纲只要求描述（写代码不考），用法见 AI 章 | 地铁线路图 | P3-CT-05、P3-AI-01 |
| Dictionary | A collection of key–value pairs in which each key is used to look up its value.（非 MS 原句） | 键值对的集合，用键查值；考纲列出，语料尚未单独出题 | 字典：词条 → 解释 | P3-CT-05 |

### 用数组实现 ADT：指针

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Base pointer | 「Points to the bottom of the stack」⟦9618_w23_32:9(a)(i)⟧ | 存栈底那一格下标的整数变量 | 盘子摞的底座 | P3-CT-06 |
| Top pointer | 「Points to the top of the stack」⟦9618_w23_32:9(a)(i)⟧ | 存栈顶下标的整数变量；本型语料里空栈时 Top 的取值各题不同（如 w25/33 MS 接受 –1、0、1），按该题题干约定；多数题让它指向最后放入的值，空栈时比底指针小 1 | 插在最上面盘子上的小旗 | P3-CT-06 |
| Front pointer | 「Points to the first term of the queue」⟦9618_s23_32:11(a)(i)⟧ | 存队首（最早加入的那个值）下标的整数变量 | 队伍最前面的人 | P3-CT-07 |
| Rear pointer | 「Points to the last term of the queue」⟦9618_s23_32:11(a)(i)⟧ | 存队尾（最后加入的那个值）下标的整数变量 | 队伍最后面的人 | P3-CT-07 |
| Queue length | 「Indicates the number of items in the queue」⟦9618_s23_32:11(a)(i)⟧ | 队中元素个数；入队加 1、出队减 1，用来判满判空 | 场内车数 | P3-CT-07 |
| Circular queue (wrap round) | When a pointer passes the upper bound of the array it is reset to the lower bound.（非 MS 原句） | 指针越过数组上界就回到下界，空出的位置可以重复使用 | 环形停车场 | P3-CT-07 |
| Head pointer | Stores the index of the first node in the linked list.（非 MS 原句） | 存链表第一个结点下标的变量；链表的遍历从它开始 | 第一张纸条在哪个盒子 | P3-CT-08 |
| Null pointer | A pointer value (such as −1 or 0, as stated in the question) that does not point to any node.（非 MS 原句） | 表示“没有下一个 / 没有孩子”的约定值，照题目用 0 或 −1 | 纸条上写着“到此为止” | P3-CT-08、P3-CT-09 |
| Free list pointer | 「Include a free list pointer」⟦9618_w22_32:11(c)⟧ | 指向空闲链表第一个结点的指针；未用和删掉的位置串成空闲链表，插入时从这里取位置 | 空座位排队等人坐 | P3-CT-08 |
| Free list | 「as a linked list of free space」⟦9618_w22_32:11(c)⟧ | 由未用结点组成的链表，使空间可以重复使用 | 回收站 | P3-CT-08 |
| Root pointer | Stores the index of the root node of the tree.（非 MS 原句） | 存二叉树根结点下标的变量；查找、插入都从根开始；−1（或题目约定值）表示空树 | 分岔路的起点 | P3-CT-09 |

### 递归

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Recursion | 「A process using a function or procedure defined in terms of itself / calls itself」⟦9618_s23_31:12(a)⟧ | 子程序用自身来定义、在执行中调用自身，直到基本情况为止 | 俄罗斯套娃 | P3-CT-10 |
| Base case | 「A recursive process must have a base case (which is a way to return without making a recursive call)」⟦9618_s23_31:12(a)⟧ | 不再递归调用、直接给出结果的情况；递归的终止条件 | 最小那个实心的套娃 | P3-CT-10、P3-CT-12 |
| General case | 「There must (also) be a general case where the recursive call takes place」⟦9618_s23_31:12(a)⟧ | 用更小的问题调用自身的情况 | 打开一个，里面还有一个 | P3-CT-10、P3-CT-12 |
| Move towards the base case | 「It must change its state and move towards the base case」⟦9618_w25_31:9(b)⟧ | 每次递归调用都要改变参数（状态），越来越接近基本情况 | 套娃一个比一个小 | P3-CT-10 |
| When recursion is beneficial | 「Recursion is beneficial for problems that can be broken down into smaller, repetitive problems」⟦9618_w25_33:11⟧ | 问题能自然分解成同类的更小问题时（阶乘、数列、树的遍历、RPN 求值） | 大问题里藏着同样的小问题 | P3-CT-10 |
| Winding | 「with each recursive call // … to set up winding」⟦9618_w23_32:9(c)⟧ | 一层层深入调用的过程，每次调用把返回地址、局部变量压栈 | 一层层翻进脚注 | P3-CT-11、P3-CT-12 |
| Unwinding | 「after the base case is reached // … to implement unwinding」⟦9618_w23_32:9(c)⟧ | 到达基本情况后逐层返回，按相反顺序弹栈，把下层结果代回上层 | 一层层翻回正文 | P3-CT-11、P3-CT-12 |
| Stack in recursion | 「Each time a recursive algorithm calls itself data is pushed onto the stack」⟦9618_w25_32:12(b)⟧ | 栈后进先出，正好让最后的调用最先返回；每层调用的数据压栈、返回时弹栈 | 便签一张张叠上、再一张张撕掉 | P3-CT-11 |
