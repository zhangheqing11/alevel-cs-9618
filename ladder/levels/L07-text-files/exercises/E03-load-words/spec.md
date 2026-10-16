# L07/E03 · 读单词进数组：去换行、跳过空行

| 属性 | 值 |
|:--|:--|
| id | `L07/E03` |
| 目录 | `ladder/levels/L07-text-files/exercises/E03-load-words/` |
| 形态 | `function`（两个函数，参数是文件名） |
| entry | `load_words`（同一文件还有 `longest_word`） |
| pseudocode | `true` |
| files | `["game.txt", "tie.txt", "empty.txt"]` |
| skills | `file-open-read`, `loop-to-eof`, `file-close`, `array-index`, `return-value` |
| difficulty | 3 |
| title | `Load words from a file into an array` |
| adapted_from | 无（不写该字段） |
| 对应卡片小节 | L07 card §2、§3；L06 card §1 |

## 练习目标

P4 最常见的第一小题：把源文件里每行一个的数据读进全局数组并记下个数。去掉行尾换行、跳过空行；再在数组上做一次查找。

## 题面

### 中文导读

文件每行一个单词，中间可能有空行。伪代码：过程 `LoadWords(FileName)` 把非空的行依次存进全局数组 `WordArray`，个数存进全局变量 `NumberWords`；函数 `LongestWord()` 返回最长的单词（一样长时取先出现的；没有单词时返回空串）。Python：`load_words(file_name)` 返回单词 list；`longest_word(file_name)` 读文件后返回最长的单词。

### English task

Each line of a text file holds one word; some lines may be blank.

1. Write a procedure `LoadWords()` that takes a file name, reads the file, and stores each non-blank line in the next element of the global array `WordArray : ARRAY[1:100] OF STRING`. The global integer `NumberWords` must hold the number of words stored.
2. Write a function `LongestWord()` that returns the longest word in `WordArray`. If two words have the same length, return the one that appears first. If there are no words, return the empty string.

Then write the Python functions:

- `load_words(file_name)` returns the list of non-blank lines, without their newline characters, in file order
- `longest_word(file_name)` returns the longest word in the file, using the same rules.

## 接口

```python
def load_words(file_name: str) -> list[str]:
    """Return the non-blank lines of the file, without newline characters, in order."""
    raise NotImplementedError


def longest_word(file_name: str) -> str:
    """Return the longest word in the file (first one on a tie), or "" if there are none."""
    raise NotImplementedError
```

`answer.pseudo` 模板：

```pseudocode
// global: WordArray : ARRAY[1:100] OF STRING
// global: NumberWords : INTEGER
PROCEDURE LoadWords(FileName : STRING)

ENDPROCEDURE

FUNCTION LongestWord() RETURNS STRING
   // assume LoadWords() has already been called

ENDFUNCTION
```

## 数据文件

全部以换行结束。

`files/game.txt`（6 行，第 4 行是空行）：

```text
house
hose
shoe

houses
use
```

`files/tie.txt`（2 行）：

```text
ab
cd
```

`files/empty.txt`：空文件（0 字节）。

## 必测行为

| # | 调用 | 期望 | 说明 |
|:--|:--|:--|:--|
| B1 | `load_words("game.txt")` | `["house", "hose", "shoe", "houses", "use"]` | 去换行、跳过空行、保持顺序 |
| B2 | `load_words("empty.txt")` | `[]` | 空文件 |
| B3 | `longest_word("game.txt")` | `"houses"` | |
| B4 | `longest_word("tie.txt")` | `"ab"` | 一样长取先出现的 |
| B5 | `longest_word("empty.txt")` | `""` | 没有单词 |
| B6 | 返回类型 | `load_words` 返回元素为 `str` 的 `list`；`longest_word` 返回 `str` | |

## mutant 建议

| # | 错误 | 应失败于 |
|:--|:--|:--|
| M1 | 没去换行：B1 得 `["house\n", …]`，B3 得 `"houses\n"` | B1、B3、B4 |
| M2 | 没跳过空行：B1 里多了一个 `""`（若同时没去换行则是 `"\n"`） | B1 |
| M3 | 比较长度用 `>=`：一样长时取了后出现的，B4 得 `"cd"` | B4 |

## 人工核对清单

- [ ] 伪代码：`NumberWords ← 0` 在读文件之前；每读到一个非空行先 `NumberWords ← NumberWords + 1` 再存进 `WordArray[NumberWords]`（下标从 1 起）。
- [ ] 伪代码：`OPENFILE FileName FOR READ`、`WHILE NOT EOF(FileName)`、`READFILE FileName, LineOfText`、`CLOSEFILE FileName`；文件只打开、关闭各一次，不在循环里（ECR P4 2024 p.7）。
- [ ] 伪代码：`LongestWord` 用 `LENGTH(WordArray[Index])` 比较长度；循环上界是 `NumberWords`。
- [ ] Python：能说出若按 P4 的要求用全局 list `word_array` 和全局计数 `number_words`，`load_words` 里哪一行需要 `global`（卡片 §3 的例子）。

## 出处

自编。题型参考 9618_s24_42 Q1（ECR P4 2024 p.5–7：把单词文件读进全局数组 `WordArray`、个数存进 `NumberWords`）。语法依据：指南 p.25–26；插页 9618_w25_in_21 p.2（LENGTH）。
