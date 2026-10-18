# P4 上机练习约定草案（供 T35；总控定稿）

> 本文件只是提议。目的：把 P4 真题做成可以自动测的 Python 练习文件夹，同时让「证据文档」里每一格的要求都对得上该题自己的 MS 得分点。通用格式仍以 `schemas/exercise-format.md` 为准，下面只写 P4 不同或需要补充的地方。凡需要改共享文件（`schemas/`、`tools/`、`Makefile`）的，标「需要总控决定」。
>
> 引用行一律写纯文本行 id。

## 1. P4 与 P2 练习的区别

| 方面 | P2 练习（T25） | P4 练习（提议） |
|:--|:--|:--|
| 作答语言 | 先写伪代码（人工按 MS 批）再写同一算法的 Python | **只写 Python**（考试本来就是上机写 Python）；`meta.pseudocode = false`，没有 `answer.pseudo` |
| 一个练习的范围 | 一个写代码小问（有时合并相关小问） | **一道大题**（如 9618_s25_43 第 1 题的 1(a)–1(e)(ii)）：各小问前后依赖（声明 → 操作 → 读文件 → 主程序 → 截图），拆开反而不能运行 |
| 数据文件 | 按题目描述自造样例 | **照搬官方源文件**（`sf` 目录的 `.txt`），逐字节复制 |
| 骨架 | 给好函数签名与全局数组 | **接近考场的空白程序**：只给各小问的分节注释与主程序入口（见 §4），声明与模块头本身就是得分点 |
| 截图题 | 无 | 截图格换成对程序输出的自动测试（§5） |

## 2. 选题与分批

- 范围：2022–25 核验语料，不含 2021 扩展、不含 s26（D1 保留给模考）。去掉 `equivalent_of` 与逐字重复后，P4 实有 **18 份卷、54 道大题、426 行、1350 分**：9618_s22_43、9618_s23_43、9618_s24_43、9618_w22_43、9618_w23_43、9618_w24_43 六份与同季 _41 **整卷相同**（行逐字相同，源文件也相同），不另做练习，`task.md` 注明「同 _41」。
- 每道大题一个练习，目录 `practice/p4/<卷>_q<题号>/`（如 `practice/p4/9618_s25_43_q1/`）。大题 14–34 分、5–13 行。
- 分批建议：T34 打完标签后，按每道大题得分最多的章分三批，顺序与学习顺序一致——批 1：PR / AR / FL / SR / RC 为主的大题；批 2：SQ / LT；批 3：OP。每批一个 PR。

## 3. 官方源文件怎样用

- 源文件在 `$ALEVEL_CS_SOURCES/pastpapers/9618_<季><yy>_sf_<卷号>/`（目录嵌套层数各卷不同，`pipeline/extract/source_files_p4.json` 有每个文件的相对路径、字节数与 sha256）。练习只复制数据 `.txt`，放进 `files/`，`meta.files` 列出文件名。不复制 `evidence.doc` 与 2021–22、s26 包里附带的「Conducting … practical test」说明 PDF / 文档（不是题目内容）。
- **逐字节复制，不得「整理」**：47 个 `.txt` 都是 ASCII；38 个是 CRLF 行尾且**最后一行不换行**，2 个 CRLF 但以换行结尾，6 个只有一行，1 个 LF。这些细节决定 MS 的「removing new line」（`strip-newline`）与「loop until EOF」点能不能测出来（同 D11 的精神）。T35 在 PR 里列出每个复制文件的 sha256，与 `source_files_p4.json` 一致。
- 题目说「文件 X 不提供」或要程序新建的文件（如 9618_w25_42:3(d) 的 Tree.txt），不放进 `files/`；测试检查程序写出的文件。
- 练习不依赖 `sources/` 存在：worktree 与云端会话看不到 `sources/`，`files/` 是练习自带的副本。

## 4. 文件夹内容（与 `schemas/exercise-format.md` 的差异）

- `task.md`：中文导读 + **英文原题**（从 QP 原页转写全部小问：题干、类图、给定的伪代码、数据格式、测试数据表；伪代码照 QP 原样，含 `←` 与带界数组，D24）+ **证据文档对照表**（§6）+ 人工核对清单。导读里提醒：标识符、文件名照抄题目（`p4-identifiers`）；数组要建出真实 list 并注释大小与类型（D10 ①）；指针初值照题目（D10 ②）；写算法时不用 `in`、`sort()`、`index()`、`max()` 代劳（D10 ③）。
- `meta.json`：`kind: "past-paper"`；`id` 取该大题第一行（如 `9618_s25_43:1(a)`）；`source.rows` 列出大题全部行；`marks` = 各行分值之和；`types` = 各行主题型与副题型的并集；`skills` = 各行 `markpoints` 技能的并集；`pseudocode: false`；`files` 列数据文件；`entry: "main"`；`ms_verified: true`。
- `starter.py`：**不预写声明、类与模块头**（这些是得分点，预写就白送了分，也练不到考场上从空文件写起）。只给：各小问的分节注释（`# ---- 1(a) ----`，后跟一句英文要求摘要）、`import` 行留空、末尾主程序入口：

  ```python
  # ---- main program ----
  if __name__ == "__main__":
      pass
  ```

  主程序必须写在 `if __name__ == "__main__":` 下：测试用 `sol` fixture 导入模块时主程序不运行（不会卡在 `input()`），`run_script` 以脚本方式运行时才运行。MS 的 Python 范例把主程序写在顶层，这一点在 `task.md` 导读里说明，不算偏离 MS（主程序的得分点看调用与输出，不看入口写法）。**需要总控决定**：这与 `exercise-format.md`「骨架给函数 / 类签名 + `raise NotImplementedError`」不同。
- `test_task.py`：按小问分组，测试名带小问号（`test_1b_enqueue_full_returns_false`），docstring 写行 id 与得分点编号（`"""9618_s25_43:1(b) MP2–MP3"""`，编号用语料 `markpoints[].n`，与 MS 印的不同时在 `task.md` 列对照，D37 ②）。
- `ref/solution.py`：参考解贴近 MS 的 **Python** 范例（`ms_text` 里范例丢了缩进，要渲染 MS 原页读），修掉范例里的笔误（如多余的 `;`）。QP 与 MS 范例在边界上不一致时按 QP（D31）。
- `ref/mutant_*.py`：至少 2 个，从该题 `markpoints` 的真实易错点挑（文件头注释写对应得分点与技能），P4 常用的见 §7。

## 5. 截图格怎样换成自动测试

P4 的截图格（MP-03）在 2022–25 去重后有 75 行、94 分，约占 7%。MS 给分看的是截图里的**内容**，正好可以变成对程序输出的断言：

1. **怎样运行**：测试用 `tools/testkit.run_script(candidate_path, stdin=…, files_dir=exercise_dir / "files")` 以脚本方式运行整个程序，输入照 QP 给的测试数据与顺序（含应被拒绝的无效输入），得到 stdout 与写出的文件。
2. **期望值从哪来**：只从**该行自己的 MS**——清单文字列出的值（9618_s25_43:1(e)(ii)「showing 3059」、9618_s24_41:1(c)(ii)「Array output 3 9 4 1 2」），或 MS 截图样例（「e.g.」后的图，要渲染原页看；2022–25 有 9 行 MS 只有图没有文字）。再用参考解在官方源文件上跑一遍核对；图与按 QP 正确运行的结果不一致时按 QP（D31），`task.md` 写明差异。
3. **断言写法**：
   - MS 列出的数值与顺序 → 在 `output_lines(stdout)` 里按顺序找到这些值（子序列匹配），不比对整行文字；
   - QP 只说「appropriate message」的提示与说明文字 → 不测文字内容（D31），只测有输出、且关键值在；
   - 有 `input()` 时，提示语与下一次 `print` 的内容会接在同一行（`input("Enter: ")` 不换行，D13），所以按「行内包含」而不是「整行相等」找；
   - 「无效输入被拒」（`test-input-sequence`）→ 喂入 QP 给的整串输入，断言程序读完全部输入、没有多问也没有少问（输入用尽时 `run_script` 的子进程会 EOFError 退出，测试据此判定），并断言只有有效值进入结果；
   - 文件内容截图（`screenshot-file`，9618_s25_41:2(e)(ii)）→ 用 `ScriptResult.read(文件名)` 检查写出的文件；「文件名在同一截图可见」无法测，进人工清单。
4. 每个截图格至少一个测试，docstring 写 `9618_…:…(ii) MP-03 MP1` 这样的行 id 与点号。截图格的测试同时是对前面各小问代码的端到端检查。

## 6. 证据文档对照表（`task.md` 必有）

证据文档（`evidence.doc`）就是一张按小问排列的表：每一格要么「Copy and paste program code listing for question 1(a) here」，要么「Copy and paste screenshot for question 1(e)(ii) here」。`task.md` 把它换成下表，一格一行，说明这一格的每个 MS 得分点怎样判：

| 证据格 | 行 id | 分 | 交什么 | 自动测（测试名 · 得分点） | 人工核对（得分点） |
|:--|:--|:--|:--|:--|:--|
| Part 1(a) | 9618_s25_43:1(a) | 3 | 代码 | `test_1a_queue_declared` · MP1–MP3（长度 50、初值 –1、两个指针 –1） | 注释写明类型与大小（D10 ①） |
| Part 1(b) | 9618_s25_43:1(b) | 6 | 代码 | `test_1b_*` · MP2–MP6（满时返回 False、首个元素把 HeadPointer 设为 0、尾指针后移） | MP1 函数头 |
| Part 1(c) | 9618_s25_43:1(c) | 5 | 代码 | `test_1c_*` · MP2–MP5 | MP1 函数头 |
| Part 1(d) | 9618_s25_43:1(d) | 6 | 代码 | `test_1d_*` · MP2–MP5（官方 QueueData.txt 全部入队；造一个超过 50 行的文件测「Queue full」）、MP6（文件缺失时不抛异常且有输出） | MP1 打开与关闭的位置；MP6 「所有文件操作在 try 里」 |
| Part 1(e)(i) | 9618_s25_43:1(e)(i) | 5 | 代码 | 由 1(e)(ii) 的端到端测试覆盖 MP1–MP5 | — |
| Part 1(e)(ii) | 9618_s25_43:1(e)(ii) | 1 | 截图 | `test_1e_screenshot_total` · 输出含 3059 | — |

（上表是格式示例；得分点编号以语料 `markpoints` 为准。）

## 7. 哪些能自动测，哪些只能人工核对

按试标 3 卷（9618_s23_42、9618_w24_41、9618_s25_43）的 218 条得分点粗算：约 78%（按分值）落在可由行为测出的技能上，约 14% 部分可测，约 8% 只能人工核对（只打了 `module-header`、`data-types`、`class-definition`、`encapsulation`、`translate-pseudocode`、`global-scope` 的点）。

| 题型 | 自动测什么 | 留给人工核对 |
|:--|:--|:--|
| PR-01 | 用 `feed_input` 喂无效再有效的输入，断言返回 / 存下的是有效值、`input()` 被调用的次数正确 | 提示语是否「appropriate」 |
| PR-02、PR-03、AR-05、SR-01 | 函数返回值与输出；边界（空串、找不到返回 –1、计数为 0） | 不用 `in` / `count()` / `max()` 代劳（D10 ③） |
| AR-01、AR-02、AR-03 | 数组长度、维度、初值、存入的数据与顺序；记录的字段名与值（类当记录时用属性） | 类型注释；「全局」还是「局部于主程序」 |
| AR-04、LT-01、LT-04 | 捕获输出，按 QP 给的格式与顺序比对（QP 给了样例格式时才比对分隔方式） | — |
| FL-01、FL-02 | 用官方源文件跑，检查数组 / ADT / 对象数组的内容；删掉数据文件再跑，断言不抛异常且有输出 | 打开与关闭的位置；异常提示的措辞 |
| FL-03 | 检查写出的文件内容与行格式；追加模式跑两次 | 截图里文件名可见 |
| SR-02、SR-03、SR-04 | 结果正确；递归版用包装函数数调用次数，断言确实递归（递归调用经模块全局名查找，替换 `sol.函数名` 即可数到） | 不用 `sort()` / `index()`（D10 ③）；「efficient」版本的提前结束可用比较次数测时才测 |
| RC-01、RC-02 | 返回值；改写成递归的断言有递归调用，改写成迭代的断言调用次数为 1 | 基本情况的写法 |
| SQ-01 ～ SQ-03、LT-02、LT-03、LT-05 | 每次操作后的数组与指针值（照 QP 给的指针约定与初值，D10 ②）、满 / 空时的返回值、回绕、空闲表、溢出区 | — |
| SQ-04 | 用题给数据跑，检查结果；可包装 Pop / Dequeue 断言确实调用了 ADT 操作 | — |
| OP-01、OP-04 | 用构造方法建对象，经 getter 检查属性值；`issubclass(子类, 父类)`；私有属性按 QP 类图的名字检查改名后的 `_类名__属性` 存在 | 属性类型注释（「If you are writing in Python, include attribute declarations using comments」） |
| OP-02、OP-03、OP-05、OP-06、OP-07 | 方法的返回值与对属性的影响；重写后子类与父类对象行为不同；容器方法的存取 | — |
| MP-01、MP-02 | `run_script` 跑主程序，检查调用顺序产生的输出 | — |
| MP-03 | 见 §5 | 截图是否清晰、文件名是否可见 |

**只能人工核对、所有题型共有的**：模块头「(and end where appropriate)」、声明的类型注释、「following the pseudocode / remainder correct」这类整体结构点、补全伪代码时是否照题目伪代码的结构（`translate-pseudocode`）。这些进 `task.md` 末尾的人工核对清单，学习时由导师按 MS 核对。

**常见 mutant**（每个练习挑 2 个以上，注释写对应得分点）：读行不去换行 / 不转 int（`strip-newline`、`type-conversion`）；循环队列尾指针不回绕或回绕差一（`queue-array`）；满时不返回失败值（`boolean-return`）；指针约定换成自己的（D10 ②）；删掉 try / except 导致缺文件时崩溃（`exception-handling`）；链表删除不把结点还给空闲表（`linked-list`）；二叉树插入左右走反（`binary-tree`）；递归改写成循环（`recursion`，靠调用计数挂掉）；构造方法参数顺序错（`constructor`）；用 `self.Name` 公有属性（`encapsulation`，靠改名属性检查挂掉）。

## 8. 与已定决策的关系

- **D10**：①数组要建出真实 list → 测长度与初值，类型注释人工核对；②指针初值照题目 → 测指针状态时用 QP 的约定，不接受「等价但不同」的约定；③写算法不用内置函数代劳 → 人工核对。可选：`tools/testkit.py` 加一个用 `ast` 检查候选文件是否调用了 `sort` / `sorted` / `index` / `count` / `max` / `min`、或在比较里用了 `in` 的辅助函数，让 ③ 也能自动挂（**需要总控决定**）。
- **D24**：只管伪代码（带上下界的全局数组）。P4 练习里伪代码只出现在 `task.md` 转写的题干中，照 QP 原样；Python 一律用固定长度的 list，下标照 QP。
- **D31**：QP 与 MS 范例在边界上不一致时，自动测试按 QP；QP 没定义的地方（提示语、说明文字、是否带空格）不测，或在 `task.md` 写明约定后再测。P4 的人工核对按该题 MS 的得分点。
- **D13**：提示语写在 `input("…")` 里；P4 截图测试按行内包含查找（§5）。
- **D3**：P4 题型有了练习文件夹后，「已掌握」以 `make try` 全过 + 人工清单通过为准。
- **D37 ②**：测试 docstring 用语料 `markpoints[].n`。

## 9. 需要总控决定

1. P4 骨架不预写声明与签名（§4），与 `exercise-format.md` 的骨架规则不同；是否在 `exercise-format.md` 加一条 P4 例外。
2. 一道大题一个练习、`meta.id` 取大题第一行（§2、§4）；或改 schema 允许 `9618_s25_43:1` 这样的大题 id。
3. `tools/try.py` 首次运行时把练习的 `files/` 复制进 `attempts/<练习>/`，学生自己 `python solution.py` 也能读到数据文件（现在只有测试的临时目录里有）。
4. `make try` 支持 `K=1b` 透传给 `pytest -k`，让学生一个小问一个小问地测。
5. `tools/testkit.py` 增加：`use_files(monkeypatch, tmp_path, files_dir)`（函数型测试切到数据文件副本目录，读相对路径的文件）；可选的 D10 ③ 内置函数检查（§8）。在总控加之前，T35 在各 `test_task.py` 里就地写同样的 fixture。
6. 六份与 _41 整卷相同的 _43 卷不做练习、只在 `task.md` 注明（§2）；它们的行 `equivalent_of` 由总控按 D35 的办法补（见 `papers/p4/tagging-guide.md` §6）。
