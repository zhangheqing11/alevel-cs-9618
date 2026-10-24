## FL　文本文件：伪代码 ↔ Python 对照与模板 {#core-FL}

文件不是一次读完才有数据的数组。读指针每读取一行就前进，EOF 表示没有下一行；写模式决定保留还是清空原有内容。伪代码按 2027–29 指南 §9（p.25–27），本章只用文本文件。

### 1. 文件通道

| 伪代码 | Python | 需要留意 |
|:--|:--|:--|
| `OPENFILE FileName FOR READ` | `with open(FileName, "r") as File:` | 缩进块内读取，退出块自动关闭 |
| `READFILE FileName, Line` | `Line = File.readline()` | Python 保留换行；EOF 时返回空串 |
| `WHILE NOT EOF(FileName)` | `for Line in File:` | Python 文件可迭代；伪代码不用这个语言特有写法 |
| `CLOSEFILE FileName` | `File.close()`，或 with 自动关闭 | 只写 close 没括号不会调用 |
| `OPENFILE FileName FOR WRITE` | `open(FileName, "w")` | 覆盖已有文件 |
| `OPENFILE FileName FOR APPEND` | `open(FileName, "a")` | 保留原有内容，末尾追加 |
| `WRITEFILE FileName, Text` | `File.write(Text + "\n")` | write 不自动换行；数字先转 str |

「Opening the file (to read) and closing the file in an appropriate place」⟦9618_s25_41:2(a)⟧ 把打开与关闭放在同一个得分点；不能因为写了两句代码就算两分。题目要求未知行数时用 EOF 控制，不能按某次源文件的长度循环。

### 2. 完整的读到 EOF 模式

```pseudocode
DECLARE FileName : STRING
DECLARE Line : STRING
FileName ← "Words.txt"
OPENFILE FileName FOR READ
WHILE NOT EOF(FileName)
   READFILE FileName, Line
   OUTPUT Line
ENDWHILE
CLOSEFILE FileName
```

```python
def ReadLines(FileName):
    Lines = []  # STRING, unknown number of elements
    try:
        with open(FileName, "r") as File:
            for Line in File:
                Lines.append(Line.rstrip("\n"))
    except OSError:
        print("Cannot open or read file")
    return Lines
```

`rstrip("\n")` 只去行尾换行，保留有意义的空格；文本模式会把常见 CRLF 读成 `\n`。`strip()` 会同时删掉两端空白，只有题目不需要这些空白时才用。空白行不是 EOF：用 `readline()` 时先判断原始返回值 `!= ""`，再去换行。

### 3. 一行多字段与多行一组

| 文件格式 | 每轮读取 | 转换与存储 |
|:--|:--|:--|
| `Beech,30,400,200,No` | 读一行，去换行，`.split(",")` | 1、2、3 号字段 int；按类图参数顺序建 Tree |
| 数字一行、颜色一行 | 同一轮连续读两行 | 第一行 int，第二行去换行，再建 Card |
| 单个整数一行 | 读一行，int | 调一次 Enqueue / Push；检查返回值 |

「Reading in all sets of 2 lines (number then colour)」⟦9618_s22_42:3(c)⟧ 的单位是“一组两行”。每次只取一行并创建 Card 会把颜色当作下一张卡的数字。

```python
def ReadPairs(FileName):
    Pairs = []  # records: INTEGER number, STRING colour; unknown count
    try:
        with open(FileName, "r") as File:
            NumberLine = File.readline()
            while NumberLine != "":
                ColourLine = File.readline()
                Pairs.append((int(NumberLine), ColourLine.rstrip("\n")))
                NumberLine = File.readline()
    except OSError:
        print("Cannot read file")
    return Pairs
```

这个模板假设文件每条记录完整，正如题给有效源文件；若题目另要求验证损坏格式，再增加相应检查。创建记录 / 对象时每轮都调用构造方法，避免整个数组指向同一个实例。

### 4. 追加与异常

```python
def StoreData(DataToStore, FileName):
    try:
        with open(FileName, "a") as File:
            for Item in DataToStore:
                File.write(str(Item) + "\n")
    except OSError:
        print("Cannot create or write to file")
```

「Using exception handling try and catch with suitable output」⟦9618_s25_41:2(c)⟧ 在 Python 对应 `try` / `except`。`OSError` 可覆盖打开、读写等文件操作错误；只有题目要求处理非法数值时再处理 `ValueError`。不是所有异常都意味着“文件不存在”，提示文字用 cannot open or read 比较准确。

重复运行追加程序会再次写入，所以测试先复制官方空文件，在副本里检查首轮结果。要验证追加，保留副本再跑第二轮；不要清空真实源文件。截图需要的内容以该行 MS 为准；⟦9618_s25_41:2(e)(ii)⟧ 明确要求红色文件内容与文件名同图可见，终端里打印一个列表不能替代它。

### 5. 考前自检

| 检查 | 为什么 |
|:--|:--|
| 文件名来自题目指定位置 | 参数不能换成 input；固定名不能拼错大小写 |
| 循环单位与 EOF | 一行 / 一条记录 / 固定组数决定循环结构 |
| 去换行、转数值 | 避免 `"red\n" != "red"` 与字符串数值比较 |
| 真实数组、元素类型与个数注释 | 有指定大小就创建固定长度 list（D10） |
| 文件访问在 try 内，关闭位置可靠 | 打开失败时不会再访问不存在的文件变量 |
| w / a 与换行 | 覆盖、追加、每行一项是不同要求 |
