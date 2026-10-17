# T40 分数线原页抽查

核查日期：2026-10-17（UTC）。所有页码为 PDF 文件页码，从 1 起计。

已渲染并目视检查十份原件的全部 19 页；逐行按表头定位以下 20 格，分别覆盖每季一个 component 格和一个 option 格（包括续页）。PDF 位于只读 `sources/pastpapers/`。下列为目视读值与 CSV 的比较，不以抽取器输出代替人工读值。

| # | PDF | 页 | 表 / 行 | 列 | PDF 读值 | CSV 值 | 结果 |
|--:|:--|--:|:--|:--|--:|--:|:--|
| 1 | 9618_s21_gt.pdf | 1 | component 12 | A | 46 | 46 | 一致 |
| 2 | 9618_s21_gt.pdf | 1 | option AY | A* | 219 | 219 | 一致 |
| 3 | 9618_w21_gt.pdf | 1 | component 31 | A | 49 | 49 | 一致 |
| 4 | 9618_w21_gt.pdf | 2 | option SY | A | 90 | 90 | 一致 |
| 5 | 9618_s22_gt.pdf | 1 | component 22 | A | 38 | 38 | 一致 |
| 6 | 9618_s22_gt.pdf | 2 | option P2 | A* | 120 | 120 | 一致 |
| 7 | 9618_w22_gt.pdf | 1 | component 13 | D | 27 | 27 | 一致 |
| 8 | 9618_w22_gt.pdf | 2 | option CXN | A* | 121 | 121 | 一致 |
| 9 | 9618_s23_gt.pdf | 1 | component 50（补充表） | A | 58 | 58 | 一致 |
| 10 | 9618_s23_gt.pdf | 2 | option WF | A* | 230 | 230 | 一致 |
| 11 | 9618_w23_gt.pdf | 1 | component 42 | E | 19 | 19 | 一致 |
| 12 | 9618_w23_gt.pdf | 2 | option WA | A* | 231 | 231 | 一致 |
| 13 | 9618_s24_gt.pdf | 1 | component 12 | C | 34 | 34 | 一致 |
| 14 | 9618_s24_gt.pdf | 2 | option SY | A | 94 | 94 | 一致 |
| 15 | 9618_w24_gt.pdf | 1 | component 42 | A | 42 | 42 | 一致 |
| 16 | 9618_w24_gt.pdf | 1 | option 3W | A* | 219 | 219 | 一致 |
| 17 | 9618_s25_gt.pdf | 1 | component 23 | A | 62 | 62 | 一致 |
| 18 | 9618_s25_gt.pdf | 2 | option SZ | B | 106 | 106 | 一致 |
| 19 | 9618_w25_gt.pdf | 1 | component 33 | D | 32 | 32 | 一致 |
| 20 | 9618_w25_gt.pdf | 2 | option WC | A* | 226 | 226 | 一致 |

另外目视确认：w21 p.1 没有 component 33/43，两个占位行的数值字段均空；w21 p.1 的 BQJ/BRJ/BYJ 未列最大分，不回填；w24 p.1 的 2W/3W 是独立印出的两行；s22 p.2 的 P1 行 A* 为 `–`；考纲 `9618_syllabus_2027-2029.pdf` p.11 的四卷均为 75 分、各占 A Level 25%。

自动核对用独立的 PyMuPDF 文字读取，与生产抽取器 Poppler 的结果逐值比较，覆盖 component 主表有值的 118 行、补充表 8 行，以及 option 156 行所有等级格；每份另固定随机种子抽 3 格。27 项测试通过，无跳过。PyMuPDF 的 SWIG 在当前 Python 环境发出 5 条第三方 DeprecationWarning，不影响结果。

结论：20 格均一致。全部特殊行、原印横线和缺失值的处理见 README；未修改原件或借其他考季补数。
