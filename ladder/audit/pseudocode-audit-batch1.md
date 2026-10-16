# 伪代码审计 · T14 批 1

## 依据与范围

主要依据：主 checkout 的 `sources/official/9618_pseudocode_guide_2027-2029.pdf`。页码为原 PDF 的 1 起页码。本报告记录语法和格式差异，不判断任何真题的得分。

已核对三张完整卡片，包括 20 个 `pseudocode` 围栏及行内语法说明：

- `ladder/levels/L01-variables-io/card.md`：4 个围栏。
- `ladder/levels/L02-selection/card.md`：6 个围栏。
- `ladder/levels/L03-iteration/card.md`：10 个围栏。

已核对全部 13 份 `answer.pseudo`，并逐份与规格接口中的模板比对：L01/E02–E05（4 份）、L02/E01–E04（4 份）、L03/E02–E06（5 份）。L01/E01、L02/E05、L03/E01 为 trace 题，没有该文件。

辅助来源：`sources/pastpapers/9618_s26_in_21.pdf` p.2、p.4，核对指南没有列出的 `NUM_TO_STR` / `STR_TO_NUM` 与 CHAR/STRING 拼接、比较规则。使用插页函数表不涉及分发保留卷 QP 的专项刷题。

## 差异 / 需要总控决定

| 位置 | 原写法 | 指南正式语法 / 建议写法 | 页码与说明 |
|:--|:--|:--|:--|
| `ladder/levels/L02-selection/card.md:130`，CASE 示例最后一个子句 | `OTHERWISE : CALL Beep` | 按过程调用正式语法：`OTHERWISE : CALL Beep()` | 指南 p.22 §8.1 明确给出 `CALL <identifier>()`，p.23 的无参数调用示例也带括号；但指南 p.19 的 CASE 原例恰好写成 `CALL Beep`。已查看 p.19、p.22、p.23 原页确认，这不是抽取丢失括号。卡片忠实复制了 p.19 原例，属于指南内部不一致。 |

需要总控决定：是否在卡片将该行统一为 p.22 的 `CALL Beep()`，并说明 p.19 原例省略括号。本任务不修改 T10 卡片；也不据此推断考试是否给分。

## 其余检查结果

| 检查项 | 对照页 | 结果 |
|:--|:--|:--|
| 关键字大写、混合大小写标识符、`//` 注释、类型与字面量 | 指南 p.5–7 | 未发现额外差异 |
| `DECLARE <identifier> : <data type>`、`CONSTANT <identifier> = <literal>`、`←` | 指南 p.8–9 | 未发现差异 |
| INPUT/OUTPUT、`/`/`DIV`/`MOD`、完整比较、`AND`/`OR`/`NOT`、`INT`/`RAND` | 指南 p.15–17 | 未发现差异 |
| `&` 与数字转换函数、CHAR/STRING 拼接/比较 | 指南 p.17；插页 p.2、p.4 | 函数名、参数顺序和类型与注明的来源相符；未把插页函数误称为指南函数 |
| IF/ELSE/ENDIF、CASE OF/TO/OTHERWISE/ENDCASE | 指南 p.18–19 | 除上述 CALL 行外未发现差异 |
| FOR/STEP/NEXT、WHILE/ENDWHILE、REPEAT/UNTIL | 指南 p.20–21 | 未发现差异；没有 DO、BREAK 或遍历式 FOR 混入伪代码 |
| PROCEDURE/ENDPROCEDURE、FUNCTION/RETURNS/ENDFUNCTION、RETURN | 指南 p.22–24 | 13 份模板的模块头、参数、类型、结束关键字和注释均与规格模板一致，未发现差异 |
| 数组声明和文件操作 | — | 本批模板不含数组或文件操作；L03 卡片仅引用已有数组元素，未声称展示完整数组声明。OPENFILE/READFILE/EOF/CLOSEFILE 留待对应后续批次审计。 |

L01/E04 题面特意提供四处错误供学生改正，已按规格保留；这些错误不作为正确写法教授，也不属于 `answer.pseudo` 模板的缺陷。模板为留空作答外壳，本报告不宣称已完成的学生算法审计。
