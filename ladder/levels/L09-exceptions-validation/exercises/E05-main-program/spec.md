# L09/E05 · 完整的 P4 式程序：全局数组 + 读文件 + 主程序

| 属性 | 值 |
|:--|:--|
| id | `L09/E05` |
| 目录 | `ladder/levels/L09-exceptions-validation/exercises/E05-main-program/` |
| 形态 | `script`（用 `tools/testkit.run_script` 运行整个文件；另用 `sol` 直接测 `ReadProducts`） |
| entry | `main` |
| pseudocode | `false` |
| files | `["Products.txt"]` |
| skills | `exception-handling`, `file-open-read`, `global-scope`, `output-format`, `p4-identifiers`, `parallel-arrays` |
| difficulty | 3 |
| title | `A complete Paper 4 style program: global arrays, file input, main program` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L09 card §3、§5；L07 card §3；L06 card §6 |

## 练习目标

第一次写「完整程序」：模块顶层的全局数组（真实建出并注释大小与类型），一个读文件的过程（放在 `try` 里），以及主程序。运行整个文件得到的输出就是 P4 证据文档里的「截图」。

## 题面

### 中文导读

文件 `Products.txt` 每行是 `名称,价格`。程序有三个全局变量：`ProductName`（10 个字符串）、`ProductPrice`（10 个实数）、`NumberProducts`（已读入的个数）。写过程 `ReadProducts(FileName)`：读文件存进两个数组；文件不存在时输出 `File not found`。主程序：调用 `ReadProducts("Products.txt")`；没有产品时输出 `No products`；否则每个产品输出一行 `名称: 价格`（价格两位小数），最后输出 `Total: 总价`（两位小数）。

### English task

Each line of the text file `Products.txt` holds a product name and its price, separated by a comma, for example `Pen,1.20`.

The program uses three global variables:

- `ProductName`, a 1D array of 10 strings, each initialised to `""`
- `ProductPrice`, a 1D array of 10 real numbers, each initialised to `0.0`
- `NumberProducts`, an integer initialised to 0.

1. Write a procedure `ReadProducts()` that takes a file name as a parameter, reads each line of the file and stores the name and the price (as a real number) in the next elements of the two arrays, adding 1 to `NumberProducts` each time. If the file does not exist, it outputs `File not found`. Use exception handling.
2. Write the main program. It calls `ReadProducts()` with `"Products.txt"`. If `NumberProducts` is 0, it outputs `No products`. Otherwise it outputs one line for each product in the form `Pen: 1.20` and then a final line in the form `Total: 4.50`. Prices and the total are output to two decimal places.

You may assume the file holds at most 10 lines, each in the correct format.

## 接口

```python
ProductName = [""] * 10      # STRING, 10 elements
ProductPrice = [0.0] * 10    # REAL, 10 elements
NumberProducts = 0           # INTEGER


def ReadProducts(FileName: str) -> None:
    """Read 'name,price' lines into ProductName and ProductPrice; output 'File not found' if missing."""
    raise NotImplementedError


def main() -> None:
    """Main program: call ReadProducts("Products.txt") and output the product list and total."""
    raise NotImplementedError


if __name__ == "__main__":
    main()
```

（`starter.py` 里三个全局变量与末尾的守卫照上面给出。）

## 数据文件

`files/Products.txt`（3 行，以换行结束）：

```text
Pen,1.20
Notebook,2.50
Ruler,0.80
```

## 必测行为

B1–B3 用 `run_script(candidate_path, files_dir=…)` 运行整个文件，比对 `result.lines`；B4–B5 用 `sol` 直接调用。T10 已核对：`1.20 + 2.50 + 0.80` 的浮点和格式化后是 `4.50`。

| # | 运行方式 | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | `run_script`，`files_dir = exercise_dir / "files"` | 返回码 0；`lines == ["Pen: 1.20", "Notebook: 2.50", "Ruler: 0.80", "Total: 4.50"]` | 正常运行（证据输出） |
| B2 | `run_script`，不给 `files_dir`（临时目录里没有文件） | 返回码 0；`lines == ["File not found", "No products"]` | 文件不存在时不崩溃 |
| B3 | `run_script`，`files_dir` 是测试自建的临时目录，里面只有一个空的 `Products.txt` | 返回码 0；`lines == ["No products"]` | 空文件 |
| B4 | `sol.ReadProducts("Products.txt")` | `sol.NumberProducts == 3`；`sol.ProductName[:3] == ["Pen", "Notebook", "Ruler"]`；`sol.ProductPrice[:3]` 约等于 `[1.2, 2.5, 0.8]` 且元素是 `float`；其余元素保持初值 | 数组内容与类型 |
| B5 | 刚加载（不调用任何函数） | `sol.ProductName == [""] * 10`、`sol.ProductPrice == [0.0] * 10`、`sol.NumberProducts == 0`；没有任何输出 | 全局数组真实建出；导入时不运行主程序 |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 打开文件没有异常处理：文件不存在时抛 `FileNotFoundError`，返回码非 0 | B2 |
| M2 | 价格没有格式化：输出 `Pen: 1.2`、`Total: 4.5` | B1 |
| M3 | 价格按字符串存入数组（没有 `float()`）：求总价时 `0 + "1.20"` 抛 `TypeError` | B1、B4 |

## 人工核对清单

- [ ] 全局数组按 D10 真实建出并注释类型与大小；`ReadProducts` 里写了 `global NumberProducts`。
- [ ] 文件的打开与关闭都在 `try` 里（推荐 `with`）；`except FileNotFoundError:`。
- [ ] 主程序在 `main()` 里，并且由 `if __name__ == "__main__":` 调用（本阶梯的约定，P4 本身不要求）。
- [ ] 能说出：在 P4 考试中，B1 的这四行输出就是要截图贴进证据文档的内容，截图要能看清全部输出（ER s22 9618/41 p.35）。

## 出处

自编。依据：考纲 p.40（P4 提交证据文档、源文件不含二进制文件）；D10（P4 数组声明口径）；ER s23 9618/41 Q3 p.39（文件与异常）。
