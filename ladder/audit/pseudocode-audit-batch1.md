# 伪代码审计 · T14 批 1

审核依据：Cambridge `9618_pseudocode_guide_2027-2029.pdf`（唯一伪代码权威）。本报告只记录审计结果，不修改 T10 的卡片或本批规格。

## 审计范围

- `ladder/levels/L01-variables-io/card.md`
- `ladder/levels/L02-selection/card.md`
- `ladder/levels/L03-iteration/card.md`
- 本批 12 份带 `pseudocode: true` 的 `answer.pseudo`：L01/E02–E05、L02/E01–E04、L03/E02–E04、L03/E06。
- L01/E01、L02/E05、L03/E01 标为 `pseudocode: false`，没有 `answer.pseudo`，仍检查了对应卡片中的伪代码示例。

## 检查项目与结果

| 项目 | 对照页 | 结果 |
|:--|:--|:--|
| 关键字大写、标识符混合大小写、注释使用 `//` | p.5–7 | 本批无差异 |
| `DECLARE`、`CONSTANT <id> = <literal>`、`←` 赋值与数据类型 | p.7–9 | 本批无差异 |
| `INPUT <identifier>`、`OUTPUT <value(s)>`、`/`、`DIV`、`MOD`、比较与 `AND/OR/NOT` | p.15–17 | 本批无差异 |
| `IF … THEN … ELSE … ENDIF` 的嵌套闭合 | p.18 | 本批无差异 |
| `CASE OF`、值/`TO` 范围、最后的 `OTHERWISE`、`ENDCASE` | p.19 | 本批无差异 |
| `FOR … TO … [STEP …]`、包含终点、`NEXT <identifier>` | p.20 | 本批无差异 |
| `REPEAT … UNTIL` 后测条件与 `WHILE … ENDWHILE` 前测条件 | p.20–21 | 本批无差异 |
| `PROCEDURE … ENDPROCEDURE`、`FUNCTION … RETURNS … ENDFUNCTION`、`RETURN` | p.22–23 | 本批无差异 |
| `answer.pseudo` 模板的函数头/过程头、结束关键字和占位注释 | p.5–9、p.18–23 | 本批无差异 |

## 结论

本批检查过的卡片、规格模板和 `answer.pseudo` 与 2027–2029 指南逐字格式一致，**本批无差异**。未发现 `ELSIF`、`FOR … IN`、Python 专属函数、`%` 代替 `MOD`、`=` 代替 `←`、缺失 `ENDIF`/`NEXT`/`ENDWHILE`/`ENDCASE` 等问题。
