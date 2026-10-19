# 练习文件夹格式（真题 `practice/` 与阶梯 `ladder/` 通用）

```
<练习目录>/
  task.md          # 题面：中文导读 + 英文原题（真题从 QP 转写，保留标识符名、数据格式）
  meta.json        # schema: exercise.schema.json
  starter.py       # 给学生的骨架：函数/类签名 + docstring，函数体 `raise NotImplementedError`
  answer.pseudo    # 仅 meta.pseudocode=true：伪代码作答模板（含题目要求的过程/函数头）
  answer.steps.md  # 仅题目要求“用文字描述算法、不写伪代码”（P2-AD-06）：编号步骤作答模板，meta.pseudocode=false（D38）
  test_task.py     # pytest；只通过 `sol` fixture 访问被测代码
  files/           # 程序要读的数据文件（P4 从官方源文件复制）；测试在临时目录里运行
  ref/
    solution.py    # 参考解（学生请勿先看）
    mutant_1.py    # 故意写错的版本：每个至少让一个测试失败
    mutant_2.py    # 建议覆盖：边界差一、漏关文件/漏处理异常、返回类型错 等真实易错
```

## 规则

1. **被测代码的加载**：测试函数声明参数 `sol` 即可得到被测模块（根目录 `conftest.py` 提供）。被测文件按优先级取：环境变量 `CANDIDATE` → `attempts/<练习目录>/solution.py` → 跳过。不要在测试里 `import solution`。
2. **脚本型题**（`input()`/`print()`、读写文件）：用 `tools/testkit.py` 的 `run_script(path, stdin=..., files=...)`，它在临时目录里运行候选文件、复制 `files/`、返回 stdout 和生成的文件。函数型题直接调 `sol.<函数>`。
3. **测试来自 MS**：真题练习的每个测试在 docstring 里注明对应的行 id 和得分点，如 `"""9618_s24_42:1(b) MP3: closes file"""`。MS 只给样例输出时，测试至少覆盖样例 + 一个边界情况。
4. **不能测的得分点**（注释、变量命名、证据截图、伪代码写法）不写成测试；在 `task.md` 末尾列「人工核对清单」，学习时由 AI 按 MS 核对。
5. **mutant 必挂、参考解必过**：`make check` 对每个练习运行一次参考解（必须全过）和每个 mutant（至少一个失败）。
6. **确定性**：不依赖网络、时间、随机数（需要随机时固定种子或注入）。单个练习的测试总时长 < 5 秒。
7. **Python 版本**：标准库 only，兼容 Python 3.12+。
8. 阶梯练习 `meta.kind = "ladder"`、`id = "L05/E03"`、`source = null`；改编自公开课的写 `adapted_from`。

## P4 真题练习（D42 ④；细则见 `papers/p4/practice-notes.md`）

与上面的通用规则不同或补充的地方：

1. **一道大题一个练习**：目录 `practice/p4/<卷>_q<题号>/`；`meta.id` 取该大题第一行（如 `9618_s25_43:1(a)`），`source.rows` 列出大题全部行，`marks` = 各行分值之和；`pseudocode: false`；`entry: "main"`。与同季 `_41` 整卷相同的 `_43` 卷不另做练习。
2. **骨架例外**：`starter.py` 不预写声明、类与模块头（它们本身是得分点），只给各小问的分节注释（`# ---- 1(a) ----` + 一句英文要求摘要）和末尾的主程序入口 `if __name__ == "__main__":`。主程序必须写在这个入口下，`sol` 导入时才不会运行到 `input()`。
3. **数据文件**：`files/` 里的 `.txt` 从官方源文件**逐字节复制**（CRLF、末行不换行都保留），sha256 与 `pipeline/extract/source_files_p4.json` 一致；题目要求程序新建的文件不放进 `files/`。`make try` 首次运行会把 `files/` 复制到 `attempts/<练习>/`，学生可以直接 `python solution.py`。
4. **测试**：函数型测试读数据文件前调 `tools/testkit.use_files(monkeypatch, tmp_path, exercise_dir / "files")`；截图格换成 `run_script(..., files_dir=…)` 的输出断言（按 MS 列出的值做子序列 / 行内包含匹配，不测提示语，D13 / D31）。测试名带小问号（`test_1b_…`），学生可用 `make try EX=… K=1b` 一问一问地测。
5. **`task.md` 必有证据文档对照表**：每个证据格 → 行 id → 每个得分点是自动测（测试名）还是人工核对。
