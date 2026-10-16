# L09/E05 · 完整的 P4 式程序：全局数组 + 读文件 + 主程序


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

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

## 数据文件

`files/Products.txt`（3 行，以换行结束）：

```text
Pen,1.20
Notebook,2.50
Ruler,0.80
```

## 人工核对清单

- [ ] 全局数组按 D10 真实建出并注释类型与大小；`ReadProducts` 里写了 `global NumberProducts`。
- [ ] 文件的打开与关闭都在 `try` 里（推荐 `with`）；`except FileNotFoundError:`。
- [ ] 主程序在 `main()` 里，并且由 `if __name__ == "__main__":` 调用（本阶梯的约定，P4 本身不要求）。
- [ ] 能说出：在 P4 考试中，B1 的这四行输出就是要截图贴进证据文档的内容，截图要能看清全部输出（ER s22 9618/41 p.35）。

## 出处

自编。依据：考纲 p.40（P4 提交证据文档、源文件不含二进制文件）；D10（P4 数组声明口径）；ER s23 9618/41 Q3 p.39（文件与异常）。
