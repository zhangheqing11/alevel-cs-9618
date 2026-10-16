# L07/E03 · 读单词进数组：去换行、跳过空行


### 中文导读

文件每行一个单词，中间可能有空行。伪代码：过程 `LoadWords(FileName)` 把非空的行依次存进全局数组 `WordArray`，个数存进全局变量 `NumberWords`；函数 `LongestWord()` 返回最长的单词（一样长时取先出现的；没有单词时返回空串）。Python：`load_words(file_name)` 返回单词 list；`longest_word(file_name)` 读文件后返回最长的单词。

### English task

Each line of a text file holds one word; some lines may be blank.

1. Write a procedure `LoadWords()` that takes a file name, reads the file, and stores each non-blank line in the next element of the global array `WordArray : ARRAY[1:100] OF STRING`. The global integer `NumberWords` must hold the number of words stored.
2. Write a function `LongestWord()` that returns the longest word in `WordArray`. If two words have the same length, return the one that appears first. If there are no words, return the empty string.

Then write the Python functions:

- `load_words(file_name)` returns the list of non-blank lines, without their newline characters, in file order
- `longest_word(file_name)` returns the longest word in the file, using the same rules.

## 作答文件

使用 `starter.py` 的接口，在学生作答目录的 `solution.py` 中实现。

先完成 `answer.pseudo`，再写 Python；伪代码写法由导师按下列清单核对。

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

## 人工核对清单

- [ ] 伪代码：`NumberWords ← 0` 在读文件之前；每读到一个非空行先 `NumberWords ← NumberWords + 1` 再存进 `WordArray[NumberWords]`（下标从 1 起）。
- [ ] 伪代码：`OPENFILE FileName FOR READ`、`WHILE NOT EOF(FileName)`、`READFILE FileName, LineOfText`、`CLOSEFILE FileName`；文件只打开、关闭各一次，不在循环里（ECR P4 2024 p.7）。
- [ ] 伪代码：`LongestWord` 用 `LENGTH(WordArray[Index])` 比较长度；循环上界是 `NumberWords`。
- [ ] Python：能说出若按 P4 的要求用全局 list `word_array` 和全局计数 `number_words`，`load_words` 里哪一行需要 `global`（卡片 §3 的例子）。

## 出处

自编。题型参考 9618_s24_42 Q1（ECR P4 2024 p.5–7：把单词文件读进全局数组 `WordArray`、个数存进 `NumberWords`）。语法依据：指南 p.25–26；插页 9618_w25_in_21 p.2（LENGTH）。
