# T38b · P4 手册审计修正记录

依据：D46、T38 F01–F04 与 OP 换题裁决；开工基线 `5effaee`，提交前已 rebase 到 `705e1b354d4df28bf90686022422988d2c1ebd42`（包含 #57 合并提交 `92d0ac389876044037c897c24439059d782c089a` 与 D47）。本任务修正 4 条手册发现，重写 3 张代表题，保留 36 型体系。没有修改语料、练习测试、共享文件或原始资料。

## 逐项修正

下列行号指本分支最终手写文件；完整整题程序均在相应卡片内。

| 项目 | 文件与行 | 改动 | 原页 / 运行核验 |
|:--|:--|:--|:--|
| F01 AR-03 | `papers/p4/cards/AR.md:534` | 明确统一用 MS 的 HeadPointer / TailPointer，并说明 QP 大小写差异 | w24/42 QP p.8、MS p.18–19 原页；未改变运行代码 |
| F02 LT-04 | `papers/p4/cards/LT.md:535` | “语法错误”改为运行时 TypeError；tuple 下标与两层 list 下标分清 | w22/41 QP p.9、MS p.19–20 原页；`ast.parse("ArrayNodes[Root, 1]")` 成功，list 实际求值 TypeError；`ArrayNodes[Root][1]` 正确返回 10 |
| F03 SQ-04 | `papers/p4/core/SQ.md:111`、`:113` | 先声明 Stored 为 BOOLEAN，再 `Stored ← PushAnimal(AnimalReturned)`；不 CALL 函数 | s23/41 QP p.8（RETURNS BOOLEAN）；2027–29 伪代码指南 p.23 §8.2 原页；Python 直接调用可保留 |
| F04 OP-03 | `papers/p4/cards/OP.md:424`、`:517` | 明确该题 MS 接受撤销本次增量或赋最大值，ER 不覆盖 MS；原题移为变式 | s23/41 QP p.5、MS p.17 原页；当前速度 95、增量 20、上限 100：推荐封顶得 speed/position=100/100，临时撤销增量等价版本得 95/95；两者均每条路径更新位置 |
| OP-02 换题 | `papers/p4/cards/OP.md:238`（MP 表 `:337`；证据 `:345`） | 代表题换为 `9618_s24_42:2(a)(iii)`；Node 三 setter，整题 Node + TreeClass；原代表题 `9618_s23_41:2(a)(ii)` 改作变式 | QP p.6–9、MS p.15–27 全题原页；7 行输出与 MS p.27 完全一致；setter 三字段读回、空树、20 个独立结点均通过 |
| OP-03 换题 | `papers/p4/cards/OP.md:426`（MP 表 `:501`；证据 `:511`） | 代表题换为 `9618_w25_42:1(a)(iv)`；整题 Bird、四方向、REAL 距离、main 输入验证；原代表题 `9618_s23_41:2(a)(iv)` 改作变式 | QP p.2–5、MS p.6–17 全题原页；四次 QP 测试、无效输入重试、0/500 分钟通过；第 4 次截图鸟名差异见下文 |
| OP-07 换题 | `papers/p4/cards/OP.md:1147`（MP 表 `:1218`；证据 `:1226`） | 代表题换为 `9618_s25_42:3(d)(ii)`；整题 Animal / Parrot / Wolf；原代表题 `9618_s23_41:2(d)(i)` 改作变式 | QP p.9–12、MS p.33–45 全题原页；3 条描述与 MS p.45 全字段一致；实际调用与返回值输出另经运行追踪核对 |

三张新卡均补齐：Python 模板、3–5 条同题 MS 引文、原有口径的得分点地图、MP 对齐、代码格/截图格说明、练习路径与存在的前置阶梯。三组代表题/变式均为 2022–25、本型 primary、非 equivalent_of、不同卷；未用 s26。对应练习分别为 `practice/p4/9618_s24_42_q2/`、`practice/p4/9618_w25_42_q1/`、`practice/p4/9618_s25_42_q3/`，均已存在。

变式原页再次核对：s23/41 QP p.4–7，MS p.14–17、24–25；Vehicle 原整题仍在 OP-01、OP-04、OP-05，运行得到 60/40、120/80/6。

## Python 运行证据

解释器一律 `/Users/zhangheqing/.venvs/alevel-cs/bin/python`；三道新题都只使用 QP 给定的数据，不读源文件（w25/42 的 TreeData.txt 属于 Q3）。程序和运行日志只放临时目录 `/tmp/T38b/`，未提交临时材料。卡内三个完整作答与实际运行文件逐字相同（包括换行），SHA-256：

| 卡 | 临时运行文件 | SHA-256 |
|:--|:--|:--|
| OP-02 | `/tmp/T38b/op02.py` | `67d84760658024fb82148ff7f6e0d7c9dca68b9caba1c9a3a5372780663881ef` |
| OP-03 | `/tmp/T38b/op03.py` | `ca7d10fa80f13859117a2d6a42217e73b556e284ae4caa31e4dcf7682b17b3fa` |
| OP-07 | `/tmp/T38b/op07.py` | `f3288de3144e3d8c1f3854d247b8777d70ca3f6135cc5cd43b17257bc262860c` |

OP-02 输入顺序 10、11、5、1、20、7、15，实际输出：

```text
2 10 1
-1 11 4
3 5 5
-1 1 -1
6 20 -1
-1 7 -1
-1 15 -1
```

三个 setter 另依次写入左指针 2、右指针 1、数据 12，getter 返回 `(2, 12, 1)`；空树输出 `No nodes`；20 格 Node 的对象身份互异。追踪 main 确认 InsertNode 调用 7 次、OutputTree 调用 1 次。

OP-03 四次独立启动（stdin 顺序为鸟号、分钟、方向）：

| stdin | Cockatiel 最终 X/Y | Macaw 最终 X/Y |
|:--|:--|:--|
| `1\n60\nN\n` | 500.0 / 571.0 | 500.0 / 500.0 |
| `2\n30\nS\n` | 500.0 / 500.0 | 500.0 / 472.0 |
| `1\n30\nW\n` | 464.5 / 500.0 | 500.0 / 500.0 |
| `2\n60\nE\n` | 500.0 / 500.0 | 556.0 / 500.0 |

另跑 `0\n1\n-1\n501\nabc\n60\nQ\nN\n`，三类无效输入都重新读取，最终得到第一测试正确结果；0 分钟位置不变，500 分钟按公式更新。每次 main 只调用所选对象 Move 一次；GetPosition 返回值实际被输出。

OP-07 实际输出：

```text
The animal's name is Chewie, it makes a Squawk, its size is 1 and its intelligence level is 10. It has a wingspan of 30cm and can say 31 words.
The animal's name is Nighteyes, it makes a Howl, its size is 8 and its intelligence level is 7. Its territory is 80 square miles.
The animal's name is Copper, it makes a Neigh, its size is 10 and its intelligence level is 6
```

`run_script_traced` 记录 Wolf.SetTerritorySize(Change=−20)、Parrot.ChangeNumberWords(Change=2)，均在描述调用之前；三个 main Description 调用，加上两个子类内部复用父类的 Description 调用，共 5 条记录，返回字符串全部包含在输出中。没有用打印固定结果代替调用。

整章 OP 的 **14 个 Python 代码块全部单独解析并运行成功**（Bird main 输入第一测试）；新三卡程序相等性、三组选题规则、F02 的 TypeError 与 F04 的两种速度限制行为另用临时断言核对。运行命令：

```sh
/Users/zhangheqing/.venvs/alevel-cs/bin/python /tmp/T38b/verify_cards.py
```

如临时目录被清理，可从每张卡 `代表题精讲` 后的第一个 python 围栏原样抽出完整作答；OP-02/07 无 stdin，OP-03 用上表输入。测试源码没有入库，也没有扩大到 T38c 的练习修改范围。

## 原件差异与需要总控决定

1. **w25/42 Q1 第 4 次截图错配鸟名**：QP p.5 明确 Macaw 向东 60 分钟；MS p.17 截图却把 X=556.0 写在 Cockatiel 行，Macaw 留 500.0。MS p.12 的调用点、p.16 的 E 分支按所选对象调用 Move，56 km/h × 1h 对应 Macaw 的 556.0。本卡按 QP / 语言无关得分点与 MS 程序逻辑写，明确标注该截图差异（D31），未宣称第 4 次与错误截图完全一致。需要总控决定：是否把此原件差异加入共享 D45 缺陷清单；本任务不改 docs/。
2. s25/42 MS p.40 的 Territory / SetTerritory 简写与 QP p.11、MS p.41 代码不同；p.42 Python 范例的 `it's territory is` 与 QP 指定 `. Its territory is ` 不同。本卡说明并按 QP 完整名称/格式实现；实际输出与 MS p.45 截图一致。无需改变 schema 或语料。
3. F05–F09 属于 T38c 范围；本任务未修练习测试，卡片明确代码调用与截图结果须分别核对。

## 验收

发布前按交接要求 fetch/rebase 最新 origin/main，再实际运行：

```sh
make check
PATH="/Users/zhangheqing/.venvs/alevel-cs/bin:$PATH" python3 build/build.py p4
make check-scope TASK=T38b
```

本轮三条命令均已通过：`make check` 核验 130 卷 / 3302 行 / 249 型 / 3558 引用 / 2280 MS 引文，244 道练习发现、0 道执行（未修改练习）；P4 两份手册构建成功，36 型保留；scope 全绿。发布前还会在最新 main 上重跑。最终命令结果、基线与发布状态记录在 `tasks/progress/T38b.md` 和 PR 描述。构建 output/ 为 gitignore 生成物，不手改、不提交。PR 按协调主会话与最新交接索引要求创建 draft，保持开放待总控验收。
