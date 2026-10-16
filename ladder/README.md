# Python 阶梯 · 使用说明

12 级「剑桥伪代码 ↔ Python」阶梯：L01–L08 服务 AS Paper 2（伪代码），L09–L12 服务 A2 Paper 4（Python 上机）。总设计见 `design.md`。

## 每一级怎么学

1. 读 `levels/L<nn>-<slug>/card.md`：先看「伪代码 ↔ Python 对照」，再看「常见坑」。
2. 按 `## 练习` 的顺序做练习：
   ```bash
   make try EX=ladder/levels/L01-variables-io/exercises/E01-trace-basics
   ```
   第一次运行会在 `attempts/` 下生成 `solution.py`（以及需要先写伪代码的题的 `answer.pseudo`）；写好后再运行同一条命令自测。
3. `answer.pseudo` 先写，`solution.py` 后写。伪代码由导师按指南批改，测试测不到。
4. 不要先看练习里的 `ref/`（参考解与故意写错的版本）。

## 写 Python 时的三条规矩

- 代码写在 `starter.py` 给出的 `def` 里面，不要删掉文件末尾的 `if __name__ == "__main__":`。
- 提示语写进 `input("…")` 的括号里，不要另起一行 `print` 提示语；除了题目规定的输出，不要 `print` 别的东西。
- 函数型题目用 `return` 交答案，不要 `print`。

## 过关

全绿 + 伪代码批改通过 + 能讲出卡片里的坑 + 现场小测通过，导师才会在 `ledger/ladder.csv` 里标「已掌握」（细则见 `design.md` §4）。
