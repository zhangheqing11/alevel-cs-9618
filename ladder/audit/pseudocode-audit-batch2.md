# 伪代码审计 · T14 批 2

## 依据与范围

主要依据：`sources/official/9618_pseudocode_guide_2027-2029.pdf`，已读取 p.5–26；辅助依据：`sources/pastpapers/9618_w25_in_21.pdf` p.2–4 的函数和运算符表。页码均为原 PDF 的 1 起页码。资料来自主 checkout 的只读 sources，本批未读取保留的 s26 题卷。

逐张检查五张完整卡片，包括 14 个 `pseudocode` 围栏、行内语法说明和 Python 对照：

| 卡片 | 伪代码围栏数 | 核对重点 |
|:--|:--|:--|
| `ladder/levels/L04-subroutines/card.md` | 4 | 过程/函数头、CALL、RETURN、BYVAL/BYREF、局部与全局 |
| `ladder/levels/L05-strings/card.md` | 1 | 字符串函数签名与下标、字符循环、日期函数、数值转换与连接 |
| `ladder/levels/L06-arrays/card.md` | 4 | 一维/二维声明、整个数组赋值、查找、冒泡排序、循环边界 |
| `ladder/levels/L07-text-files/card.md` | 2 | READ/WRITE/APPEND、文件名变量、EOF 参数、读写与关闭顺序 |
| `ladder/levels/L08-records-stacks-queues/card.md` | 3 | TYPE/ENDTYPE、字段与记录数组、枚举/指针、栈与循环队列 |

逐份检查 20 份 `answer.pseudo` 并与 spec.md 接口模板逐字比对：L04/E02–E05、L05/E03–E06、L06/E02–E05、L07/E02–E05、L08/E01 与 E03–E05，每级 4 份。模板中的注释是作答提示，空白函数体留给学生完成，不作为已经实现的算法。

## 语法对照结果

本批无差异：未发现卡片作为正确示例教授的伪代码或本批模板，与所引指南/插页的语法存在差异。卡片中明确标为错误的反例不算正确示例。

| 检查项 | 对照原页 | 结果 |
|:--|:--|:--|
| 大写关键字、混合大小写标识符、`//`、CHAR/STRING/BOOLEAN/DATE、DECLARE、CONSTANT、`←` | 指南 p.5–9 | 关键字及字面量格式一致；常量值为字面量 |
| ARRAY 的冒号范围、二维逗号分隔、方括号访问、数组整体赋值、循环逐个初始化 | 指南 p.10–11 | 示例与指南一致；Python 对照区分真实复制与别名 |
| `TYPE Season = (…)`、`TYPE TIntPointer = ^INTEGER`、记录 TYPE/DECLARE/ENDTYPE、记录数组与点号 | 指南 p.12–14 | 定义及访问格式一致；栈/队列里的整数下标未冒充语言指针类型 |
| INPUT/OUTPUT、DIV/MOD、比较与 AND/OR/NOT、`&` | 指南 p.15–17；插页 p.4 | 没有把赋值写成 `=`；数字先转换再连接字符串 |
| RIGHT/LENGTH/MID、LEFT/TO_UPPER/TO_LOWER、NUM_TO_STR/STR_TO_NUM/IS_NUM、ASC/CHR | 指南 p.16–17；插页 p.2–3 | 函数名、参数顺序和类型一致；指南没有的函数明确依据插页，没有拿 Python 切片充当伪代码 |
| DAY/MONTH/YEAR/DAYINDEX/SETDATE/TODAY、DATE | 指南 p.7；插页 p.3 | 星期日为 1，SETDATE 是日/月/年；Python 对照正确转换星期编号和构造参数顺序 |
| IF/THEN/ELSE/ENDIF、CASE 的行内说明、FOR/TO/STEP/NEXT、REPEAT/UNTIL、WHILE/ENDWHILE | 指南 p.18–21 | 负步长、循环上下界和闭合关键字一致；未在伪代码中引入遍历式 FOR、BREAK 或 Python 方法 |
| PROCEDURE/CALL/ENDPROCEDURE、FUNCTION/RETURNS/RETURN/ENDFUNCTION、BYVAL/BYREF | 指南 p.22–24 | 无参过程带括号（D12）；BYREF 只用于过程，连续同传递方式参数可省略重复关键字；模板的头与结束成对 |
| OPENFILE/FOR READ、WRITE、APPEND、READFILE、EOF(文件名)、WRITEFILE、CLOSEFILE | 指南 p.25–26；插页 p.4 | L07 复制示例与指南 p.26 一致；变量文件名不加引号；EOF 明确用于 READ 模式 |

`AND` 是否短路未由指南定义；L05 卡片已经明确说明这一限制。该处没有被当作 Python 测试能证明的伪代码性质。人工清单仍需由导师核对学生的实际伪代码。

本报告核对语法和格式，不审定卡片引用的 ER/ECR 评分主张，不据此给任何真题打分。

## 卡片与规格的一处文字不一致 / 需要总控决定

| 位置 | 现有文字 | 对照与建议 |
|:--|:--|:--|
| `ladder/levels/L06-arrays/card.md:182`，E02 练习目录行 | `找到就停；返回 1 起位置` | E02 spec 的接口是 `look_up_mark`，返回首个匹配学生的**分数**或 `-1`；卡片 §4 的另一个示例 `FindPosition` 才返回 1 起位置或 0。建议目录行改为「找到就停；并行数组里返回分数」。这是卡片目录与规格的一致性问题，没有对应的指南错误页码。 |

需要总控决定：修正上述 L06 目录行。T14 按唯一需求来源 spec.md 实现查分练习，未修改归 T10 的卡片，也没有改变题目接口。

## 实现与校验补充

- 26 份 starter 均与 spec Python 接口逐字一致；20 份模板均与 spec 伪代码模板逐字一致。
- 测试覆盖每份规格的全部 B 行为，所有建议的 84 个 mutant 均已实现。算法/声明/注释等写法要求保留在人工清单，测试不检查源码结构。
- 另外用 5 份正确替代实现验证测试不过拟合：`strip()` 去空格（8 测试）、while 查找（7）、临时变量冒泡交换（6）、`read().splitlines()` 统计代码行（4）、逐对比较括号（11），全部通过。
- L07 共 12 个数据文件按规格逐字写出，`·` 转为普通空格；`trailing.txt` 末字节为 `0x32`，没有末尾换行；两个 `empty.txt` 均为 0 字节。
- `program1.txt` 第 9 行按规格必须是 4 个空格再换行，因此完整 `git diff --check` 会报告该数据行的 trailing whitespace/末尾空白行。不得为消除提示而改坏数据；排除该文件后，其余变更的空白检查通过。
