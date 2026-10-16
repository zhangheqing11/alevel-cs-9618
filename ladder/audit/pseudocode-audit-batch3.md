# 伪代码审计 · T14 批 3

## 依据与范围

依据为主 checkout 的只读资料：`sources/official/9618_pseudocode_guide_2027-2029.pdf`（尤其 p.10、p.13、p.15–24、p.26–30）及 `sources/pastpapers/9618_w25_in_21.pdf` p.2–4。本报告页码均为原 PDF 的 1 起页码；没有使用保留的 s26 资料，不审定 ER/ECR 的给分主张。

逐张读取并核对四张完整卡片、14 个伪代码围栏及行内说明：

| 卡片 | 围栏数 | 范围 |
|:--|--:|:--|
| `ladder/levels/L09-exceptions-validation/card.md` | 1 | 条件校验、IS_NUM/STR_TO_NUM/INT、无 TRY/EXCEPT 的指南边界、随机文件关键字 |
| `ladder/levels/L10-linked-lists-trees/card.md` | 6 | 记录/并行数组、0 起下标、空指针、空闲表、遍历、插入、删除、树声明 |
| `ladder/levels/L11-recursion-algorithms/card.md` | 4 | 递归函数与过程、二分查找、DIV、插入排序的标志循环、中序遍历 |
| `ladder/levels/L12-oop/card.md` | 3 | CLASS/ENDCLASS、PRIVATE/PUBLIC、构造 NEW、INHERITS/SUPER、对象方法调用 |

全部 10 份 `answer.pseudo` 已逐字与 spec 接口模板比对：L09/E04（1）、L10/E03–E05（3）、L11/E02–E05（4）、L12/E01 和 E03（2）。空白算法/类体是学生作答区域，本报告不把留空模板当成已经完成的算法。

## 需要总控决定

### 1. L11/E03 数组参数是已注明的仓库扩展，不能称为指南原文

| 位置 | 原写法 | 指南对照与建议 |
|:--|:--|:--|
| `ladder/levels/L11-recursion-algorithms/exercises/E03-binary-search/answer.pseudo:1`、`:8`；来源为同目录 spec.md:50、:57 | `SearchArray : ARRAY OF INTEGER` | 指南 p.10 的数组声明为 `DECLARE … : ARRAY[下界:上界] OF 类型`；p.22–23 的参数格式只有 `<param> : <data type>`，没有定义不带边界的数组参数语法。不能把 `ARRAY OF INTEGER` 宣称为指南逐字写法。若要完全避免扩展，可沿用 L11 card §3：全局声明有上下界的 SearchArray 和 NumberItems，函数参数只保留 SearchItem（递归版另保留 Low、High）。这是用指南既有语法组合出的建议，不是指南提供了二分查找原例。 |

spec.md:63 已明确承认该约定来自 `schemas/examples`；实际 `schemas/examples/function-style/answer.pseudo:1` 也使用同一形式。因此这是**来源已经说明的本地约定**，不是模板误抄或指南明确禁止的语法。T14 按任务卡要求原样复制，未自行修改。

需要总控决定：保留并正式记录这项本地约定，还是由 T10/总控将该 spec、模板及共享示例统一为全局数组方案。涉及 T10 spec 和共享 schema 示例，T14 不修改。

### 2. L10 两份人工清单与 L11 卡片的短路口径需要统一

| 位置 | 原写法 | 指南对照与建议 |
|:--|:--|:--|
| `ladder/levels/L10-linked-lists-trees/exercises/E03-ordered-insert/spec.md:94`，已按规格复制到 task.md 人工清单 | `WHILE Current <> -1 AND ListData[Current] <= Item` | 指南 p.16 定义 AND 的逻辑含义，没有保证短路求值；p.10 要求数组下标有效。Current 为 -1 时，不能仅据该说明保证第二个操作数不访问越界。建议用 p.18、p.21 的 IF/WHILE 结构：循环中先独立判断空指针，非空时才比较数据，再用标志结束循环。 |
| `ladder/levels/L10-linked-lists-trees/exercises/E04-delete-node/spec.md:93`，已按规格复制到 task.md 人工清单 | `WHILE Current <> -1 AND ListData[Current] <> Item` | 同上；与 `ladder/levels/L11-recursion-algorithms/card.md:115` 明确避免依赖短路的指导不一致。 |

这不是断言指南要求非短路求值，也不推断考试扣分；问题在于现有材料依赖了指南未定义的求值规则，并且本批教学口径不一致。Python 参考解中的 `and` 有短路语义，不受这个伪代码不确定性影响。

需要总控决定：由 T10 统一这两份 spec 的人工清单为标志/分层判断写法，或明确项目的伪代码求值约定。T14 保留规格原文，在此报告，不绕过任务范围。

## 其余语法核对结果

| 检查项 | 原页 | 结果 |
|:--|:--|:--|
| 关键字大小写、DECLARE、`←`、CHAR/STRING/BOOLEAN、数组冒号范围、记录 TYPE/ENDTYPE | 指南 p.5–10、p.13 | 卡片与模板未发现额外差异；0 起下标是题目明确约定，不擅自改为 1 起 |
| INPUT/OUTPUT、关系与逻辑运算、DIV/MOD、字符串函数、`&`、INT | 指南 p.15–17；插页 p.2–4 | 函数名、参数顺序及类型一致；L09 明确区分 IS_NUM 与整数转换，L11 用 DIV 计算中点 |
| IF/THEN/ELSE/ENDIF、FOR/TO/NEXT、REPEAT/UNTIL、WHILE/ENDWHILE | 指南 p.18–21 | 卡片的闭合结构及边界一致；L11 插入排序先判断 Position，再访问数组，用标志结束循环 |
| PROCEDURE/ENDPROCEDURE、CALL、FUNCTION/RETURNS/ENDFUNCTION、RETURN | 指南 p.22–24 | 普通过程递归使用 CALL，函数递归在表达式中使用；没有把函数结果误当 OUTPUT |
| 随机文件 OPENFILE/FOR RANDOM、SEEK、GETRECORD、PUTRECORD | 指南 p.26–27 | L09 的选学说明与指南一致，本批不实现随机文件练习 |
| CLASS/ENDCLASS、PRIVATE/PUBLIC、构造 NEW、INHERITS/SUPER、`对象.方法()` | 指南 p.28–29 | 卡片和两个类模板一致；对象方法调用沿用 p.28 的点号形式，不擅自添加普通过程的 CALL |
| `PRIVATE Breed : STRING` 的空格 | 指南 p.28 原页 | 卡片已注明原例 `Breed: STRING` 的空格差别；已查看 p.28 原页确认。这是显式说明的排版归一，不是关键字/参数差异 |
| 指南没有 TRY/EXCEPT | 指南 p.30 索引及正文 | L09 在 Python 区展示异常处理，在伪代码区使用条件检查，没有把 Python 异常结构混入伪代码 |

L11 card §7 已明确把考官范答的 `CALL RecursiveInsertion(…)` 作为与指南不符的例子说明；不是该卡推荐学生照写的正确形式。指南 p.23 的函数调用规则已在卡片说明。

D12、D18 的历史事项已核实解决：L02 card:130 为 `CALL Beep()`，附 p.19 原例省略括号的说明；L06 card:182 已写「并行数组里返回分数（找不到返回 -1）」。本批没有再改这两张卡片。

## 实现与验证边界

- 20 道练习、71 个规格指定 mutant（L09 17、L10 18、L11 17、L12 19）、10 份模板、2 个数据文件；starter 与模板逐字取自规格，数据文件按 D11 核对内容和尾换行。
- 每份测试覆盖全部 B 行为；额外覆盖规格要求的首次重复项删除/查找及 E03 继承自 E02 的初始化契约。
- 只在 design.md §7.5 和具体规格明确要求时检查递归/模块调用次数、数组读取次数、属性名字改写和继承关系。包装在上下文结束时恢复，不影响后续测试；`in`、`index` 等无法由读取计数可靠识别的写法仍交人工核对。
- 可能造环的链表 mutant 在输出过程设有限步数保护；测试遍历时验证路径有限，避免错误样例把检查拖成死循环。保护不影响合法链表的行为。
- 5 份正确替代实现的 51 项测试全部通过：ConvertMark 的 try/else、按序插入的分层判断、二分查找的另一种中点/比较顺序、标志循环插入排序、sum 累加面积。
- 本报告记录语法、规格一致性与测试证据；不声称自动测试能够代替导师审阅学生的伪代码、注释和考试证据文档。
