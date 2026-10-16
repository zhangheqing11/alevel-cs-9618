# 线性查找（格式示例）

> 这是 `schemas/exercise-format.md` 的示例练习，演示函数型 + 伪代码题的文件组织。

写函数 `linear_search(items, target)`：从下标 0 开始逐个比较，返回 `target` 第一次出现的下标；找不到返回 `-1`。

1. 先在 `answer.pseudo` 里用剑桥伪代码写 `FUNCTION LinearSearch(Items : ARRAY OF INTEGER, Target : INTEGER) RETURNS INTEGER`。
2. 再在 `solution.py` 里写 Python 版。

## 人工核对清单
- 伪代码函数头、`RETURNS` 类型、`ENDFUNCTION`
- 循环变量范围覆盖到最后一个元素
