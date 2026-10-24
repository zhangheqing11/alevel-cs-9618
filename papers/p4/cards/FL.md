## FL　文本文件与异常处理 {#ch-FL}

<!-- auto:chapter-stats -->

### 核心思想

文件题是一条数据通道：打开 → 读一项 → 转成需要的类型或对象 → 存进结构 → 关闭。先确定“一项”是一行、几个字段还是连续几行；再选择 FL-01、FL-02。写出文件是 FL-03：模式和每行格式要单独确认。

`with open(...) as File:` 会在离开代码块时关闭文件，包括块内抛出异常时；把它放在 `try` 内，打开失败也能进入 `except`。Python 文件迭代到 EOF 自动停止，不能因为样例有 72 行就把未知行数写死成 72。固定大小数组要实际创建；题目明说行数未知的动态数组才从 `[]` 开始。

### 题型树
<!-- auto:type-tree -->

### P4-FL-01　读文本文件到数组或 ADT　{#P4-FL-01}

<!-- auto:stats P4-FL-01 -->

**考法**　从文本逐行读进一维数组，或把每项交给 Push / Enqueue；题目可要求返回数组、提示文件名、处理缺文件。

**识别信号**　unknown number of lines；until EOF；read each line；returns the populated 1D array。

**解题思路**
1. 先圈定文件名来源：固定名字、参数或用户输入，不能互相替换。
2. 读一行立即去换行；数字在进入整数数组或 ADT 前转换。
3. 未知行数用文件循环，不按源文件的当前行数写固定循环。
4. 送进 ADT 时只调用一次插入操作，保存并检查成功标志；关闭和异常处理覆盖文件访问。
5. 函数最后返回数组；主程序接住返回值，交给后续模块。

**Python 模板**

```python
def ReadData():
    DataList = []  # STRING, unknown size
    FileName = input("Enter the filename: ")
    try:
        with open(FileName, "r") as File:
            for Line in File:
                DataList.append(Line.rstrip("\n"))
    except OSError:
        print("Cannot open or read the file")
    return DataList
```

**得分表述**（引自对应 MS）
- 「Prompt to enter filename and reading input」⟦9618_s25_41:2(a)⟧
- 「Opening the file (to read) and closing the file in an appropriate place」⟦9618_s25_41:2(a)⟧
- 「Looping until EOF …」⟦9618_s25_41:2(a)⟧
- 「… (removing line break and) inserting in array」⟦9618_s25_41:2(a)⟧
- 「Returning populated array」⟦9618_s25_41:2(a)⟧
- 「Exception handling try catch with appropriate output」⟦9618_s25_41:2(a)⟧

**得分点地图**（核验语料 2022–2026s、主题型行、去掉 `equivalent_of`；同一行同一标签计一次；s26 只进计数。本型 14 行，均已拆点。下表列出现行数最多的 8 个标签；同次数按标签名排序，不把行数当分值。）

| 技能标签 | 行数 |
|:--|--:|
| `exception-handling` | 14 |
| `file-open-read` | 14 |
| `loop-to-eof` | 14 |
| `file-close` | 13 |
| `output-format` | 13 |
| `module-header` | 11 |
| `procedure-call` | 8 |
| `array-index` | 5 |

地图用于安排复习：先练覆盖行数较多的技能，再按当前题自己的 MS 检查每一点。多个标签可以属于同一个得分点，不能相加算分。

**易错与失分**
- 把未知行数写成固定次数。考官报告指出这会遗漏“文件长度未知”的要求（⟦9618_s25_41:2(a)⟧）。
- 在异常处理外面关闭一个可能从未打开的变量，会引入另一次异常。`with` 的打开、读取、关闭都位于 `try` 范围内。
- 对 `Enqueue()` 调用两次，一次判断、一次存入，会重复入队；变式要接住一次调用的返回值。

#### 代表题精讲　⟦9618_s25_41:2(a)⟧

**在考什么**　2(a) 的 ReadData() 提示文件名、逐行读入并返回字符串数组。QP p.4；同题 2(c)–(e) 在 p.5。MS p.18 的 8 点是 1 mark each to max 7；Python 范例在 p.19。下面连同分类、追加和主程序构成 2(a)–(e) 整题。

**完整作答**（整道大题的最终程序；分格提交时按小问截取代码，早期截图在后续修改前另存）

```python
# Question2_J25: 2(a)-(e)
def ReadData():
    DataList = []  # STRING, unknown number of lines
    FileName = input("Enter the filename: ")
    try:
        with open(FileName, "r") as File:
            for Line in File:
                DataList.append(Line.rstrip("\n"))
    except OSError:
        print("Cannot open or read the file")
    return DataList


def StoreData(DataToStore, FileName):
    try:
        with open(FileName, "a") as File:  # MP1 append and automatic close
            for Item in DataToStore:  # MP2
                File.write(str(Item))  # MP3
                File.write("\n")  # MP4
    except OSError:
        print("Cannot create or write to file")  # MP5


def SplitData(DataArray):
    Red = []  # INTEGER arrays, unknown size, one per colour
    Green = []
    Blue = []
    Orange = []
    Yellow = []
    Pink = []
    for Index in range(len(DataArray)):
        Parts = DataArray[Index].split(",")
        Number = int(Parts[0])
        Colour = Parts[1]
        if Colour == "red":
            Red.append(Number)
        elif Colour == "green":
            Green.append(Number)
        elif Colour == "blue":
            Blue.append(Number)
        elif Colour == "orange":
            Orange.append(Number)
        elif Colour == "yellow":
            Yellow.append(Number)
        elif Colour == "pink":
            Pink.append(Number)
    StoreData(Red, "Red.txt")
    StoreData(Green, "Green.txt")
    StoreData(Blue, "Blue.txt")
    StoreData(Orange, "Orange.txt")
    StoreData(Yellow, "Yellow.txt")
    StoreData(Pink, "Pink.txt")


if __name__ == "__main__":
    DataFromFile = ReadData()
    SplitData(DataFromFile)
```

**运行核对**　在官方源文件的临时副本中输入 TheData.txt，退出码 0；读取 72 行，Red.txt 写出 10、9、1、76、19、38、34、46、14、45、37、43，各占一行。红色文件按 QP 数据分类结果核对；该截图 MS 只规定文件内容和文件名可见，没有另印红色数列。缺文件路径另测，输出提示而不抛异常。

**与 MS 逐点对齐**　MS 未印逐点号码；下表 MP 按语料 `markpoints[].n` 顺序。

| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Function header (and end) | `def ReadData():` | `module-header` |
| 2 | Prompt to enter filename and reading input | `input("Enter the filename: ")` | `input-prompt` |
| 3 | Opening the file (to read) and closing the file in an appropriate place | `with open(FileName, "r")`，退出块关闭 | `file-open-read`、`file-close` |
| 4 | Looping until EOF … | `for Line in File` | `loop-to-eof` |
| 5 | … reading each line in the file … | 每次迭代得到一行 | `file-open-read` |
| 6 | … (removing line break and) inserting in array | `rstrip("\n")` 后 `append` | `strip-newline`、`array-index` |
| 7 | Returning populated array | `return DataList` | `return-value` |
| 8 | Exception handling try catch with appropriate output | `except OSError` 与提示 | `exception-handling`、`output-format` |

**分值边界**　该小问 7 分；语料 `ms_max=7`。`//` 是同一点的替代说法，接续句是否独立成点以本表与原页为准。

**证据格怎么交**　2(a) 格贴 ReadData()。2(b) 格贴 SplitData() 的分类部分；2(c) 格贴 StoreData()；2(d) 格贴增加六次调用后的 SplitData()；2(e)(i) 贴主程序。2(e)(ii) 截图要显示 TheData.txt 的提示与输入，以及 Red.txt 的内容和同图可见的文件名；控制台列表不能替代文件截图（MS p.29）。

**直观**　像把到站的一车包裹逐件收进仓库：车上还有就继续收，不预先猜一共有几件。

**对应练习与阶梯**　practice/p4/9618_s25_41_q2/（T35 并行生成，按目录命名规则定位）；前置阶梯 **L07 E03**（读词表）、**L09 E03**（读分数与异常）。

**下一道变式**　⟦9618_s25_43:1(d)⟧　QP p.3、MS p.14。CreateQueue() 改为读 QueueData.txt，每项调用 Enqueue()，满时输出 Queue full；仍须读到 EOF，所有文件访问放在 try 内。

<!-- auto:drills P4-FL-01 -->

### P4-FL-02　读文件拆字段并建记录或对象　{#P4-FL-02}

<!-- auto:stats P4-FL-02 -->

**考法**　每行拆成多个字段，或每几行读成一组，转换类型后创建记录 / 对象，存入数组。

**识别信号**　five comma-separated fields；creates a new object；sets of 2 lines；array of type Tree。

**解题思路**
1. 先把文件格式画成字段顺序：TreeName、HeightGrowth、MaxHeight、MaxWidth、Evergreen。
2. 一轮读取完整的一条记录；多行格式要连续读够一组，不能每行都建对象。
3. 先去换行再拆逗号，只把数值字段转 int。
4. 构造方法参数顺序照类图；每轮创建一个新对象，放到下一个数组位置。
5. 成功后返回数组；打开、读取与关闭都在异常处理范围内。

**Python 模板**

```python
def ReadPairs(FileName):
    Pairs = []  # dynamic array of (INTEGER, STRING) records
    try:
        with open(FileName, "r") as File:
            NumberLine = File.readline()
            while NumberLine != "":
                Colour = File.readline().rstrip("\n")
                Pairs.append((int(NumberLine), Colour))
                NumberLine = File.readline()
    except OSError:
        print("Cannot read file")
    return Pairs
```

**得分表述**（引自对应 MS）
- 「appropriate use of exception handling, with catch and output」⟦9618_s24_41:2(b)⟧
- 「Function header (and end where appropriate) and declaration of array (of type Tree with min 9 elements)」⟦9618_s24_41:2(b)⟧
- 「Reading each line of text (until EOF, or 9 times)」⟦9618_s24_41:2(b)⟧
- 「Splitting each line into the 5 elements …」⟦9618_s24_41:2(b)⟧
- 「… casting height growth, max height and max width to integers」⟦9618_s24_41:2(b)⟧
- 「… creating a new object of type Tree with the 5 values」⟦9618_s24_41:2(b)⟧

**得分点地图**（核验语料 2022–2026s、主题型行、去掉 `equivalent_of`；同一行同一标签计一次；s26 只进计数。本型 11 行，均已拆点。下表列出现行数最多的 8 个标签；同次数按标签名排序，不把行数当分值。）

| 技能标签 | 行数 |
|:--|--:|
| `exception-handling` | 11 |
| `file-close` | 11 |
| `file-open-read` | 11 |
| `loop-to-eof` | 11 |
| `output-format` | 11 |
| `object-instantiation` | 9 |
| `module-header` | 8 |
| `type-conversion` | 8 |

地图用于安排复习：先练覆盖行数较多的技能，再按当前题自己的 MS 检查每一点。多个标签可以属于同一个得分点，不能相加算分。

**易错与失分**
- 把五个字段都当字符串存进对象，后续高度比较或计算会出错。
- 忘记关文件，或把关闭放在 try 外。考官报告指出文件未打开时在外部关闭不可行（⟦9618_s24_41:2(b)⟧）。
- 复用同一个对象并不断改它的属性，数组就会保存同一对象的多个引用；每轮都要调用构造方法。

#### 代表题精讲　⟦9618_s24_41:2(b)⟧

**在考什么**　QP p.6 类图、p.7 文件格式与 2(b)、p.8 输出格式、p.9–10 筛选与测试。MS p.18–20 是本问（Python p.20）；p.22、28 是两轮测试的输出。注意本问是“异常处理必有 1 分 + 其余清单最多 6 分”，总分 7，不能把所有点简单按 Max 7 任取。

**完整作答**（整道大题的最终程序；分格提交时按小问截取代码，早期截图在后续修改前另存）

```python
# Question2_J24: 2(a)-(e)
class Tree:
    def __init__(self, Name, HGrowth, MaxH, MaxW, PEvergreen):
        self.__TreeName = Name  # STRING
        self.__HeightGrowth = HGrowth  # INTEGER
        self.__MaxHeight = MaxH  # INTEGER
        self.__MaxWidth = MaxW  # INTEGER
        self.__Evergreen = PEvergreen  # STRING

    def GetTreeName(self):
        return self.__TreeName

    def GetGrowth(self):
        return self.__HeightGrowth

    def GetMaxHeight(self):
        return self.__MaxHeight

    def GetMaxWidth(self):
        return self.__MaxWidth

    def GetEvergreen(self):
        return self.__Evergreen


def ReadData():
    TreeObjects = [None] * 9  # Tree, 9 elements
    Next = 0
    try:
        with open("Trees.txt", "r") as File:
            for Line in File:
                Parts = Line.rstrip("\n").split(",")
                TreeObjects[Next] = Tree(Parts[0], int(Parts[1]), int(Parts[2]),
                                         int(Parts[3]), Parts[4])
                Next = Next + 1
    except OSError:
        print("File not found or cannot be read")
    return TreeObjects


def PrintTrees(Item):
    Final = "does not lose its leaves."
    if Item.GetEvergreen() == "No":
        Final = "loses its leaves each year."
    print(Item.GetTreeName(), "has a maximum height", Item.GetMaxHeight(),
          "a maximum width", Item.GetMaxWidth(), "and grows", Item.GetGrowth(),
          "cm a year. It", Final)


def ChooseTree(Trees):
    Evergreen = input("Evergreen (keep/lose): ")
    MaxHeight = int(input("Maximum height in cm: "))
    MaxWidth = int(input("Maximum width in cm: "))
    Keep = "No"
    if Evergreen.lower() == "keep":
        Keep = "Yes"
    Options = []  # Tree, unknown number of matches
    for Item in Trees:
        if Item is not None:
            if (Item.GetMaxHeight() <= MaxHeight and Item.GetMaxWidth() <= MaxWidth
                    and Item.GetEvergreen() == Keep):
                Options.append(Item)
                PrintTrees(Item)
    if len(Options) == 0:
        print("No suitable trees")
    else:
        Choice = input("Enter the name of the tree to buy: ")
        Start = int(input("Starting height in cm: "))
        for Item in Options:
            if Item.GetTreeName() == Choice:
                Years = (Item.GetMaxHeight() - Start) / Item.GetGrowth()
                print("Your tree should be full height in approximately", Years, "years")


if __name__ == "__main__":
    TreeObjects = ReadData()
    if TreeObjects[0] is not None:
        PrintTrees(TreeObjects[0])
        ChooseTree(TreeObjects)
```

**运行核对**　官方 Trees.txt 副本读出 9 个 Tree；先输出 Beech 的 400、200、30，再输入 keep、400、200、Blue Conifer、100，输出 Blue Conifer 与 Green Conifer，最后 3.75 年，符合 MS p.22、28。缺文件另测仅输出错误提示，主程序防止对 None 调 getter。

**与 MS 逐点对齐**　MS 未印逐点号码；下表 MP 按语料 `markpoints[].n` 顺序。

| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | appropriate use of exception handling, with catch and output | `except OSError` 与输出 | `exception-handling`、`output-format` |
| 2 | Function header (and end where appropriate) and declaration of array (of type Tree with min 9 elements) | 无参函数；9 个位置的 TreeObjects | `module-header`、`array-of-objects`、`declare-array` |
| 3 | Opening text file Trees.txt to read and closing the file | `with open("Trees.txt", "r")` | `file-open-read`、`file-close` |
| 4 | Reading each line of text (until EOF, or 9 times) | `for Line in File` | `loop-to-eof` |
| 5 | Splitting each line into the 5 elements … | `split(",")` | `field-extract` |
| 6 | … casting height growth, max height and max width to integers | 三个 `int(...)` | `type-conversion` |
| 7 | … creating a new object of type Tree with the 5 values | 每轮 `Tree(...)` | `object-instantiation` |
| 8 | … storing each object in the array and returning the array | 下标 Next 存入；最后返回 | `array-of-objects`、`return-value` |

**分值边界**　该小问 7 分；语料 `ms_max=7`。`//` 是同一点的替代说法，接续句是否独立成点以本表与原页为准。

**证据格怎么交**　2(b) 格贴完整 ReadData()；类与 getter 分别进 2(a)(i)/(ii)，PrintTrees 进 2(c)，首次主程序进 2(d)(i)，首次 Beech 输出截图进 2(d)(ii)。保留首次截图后再加 ChooseTree；最终 2(e)(iii) 截图显示 keep、400、200、两棵 conifer，以及 Blue Conifer、100 和 3.75 年（MS p.28）。QP p.10 的 ChooseTrees() 多了 s；前文与 MS 用 ChooseTree()，程序统一用后者。

**直观**　像把一行报名表的五栏装进一个人的档案：先按栏拆开，再按类型填，整份档案放进数组一格。

**对应练习与阶梯**　practice/p4/9618_s24_41_q2/（T35 并行生成，按目录命名规则定位）；前置阶梯 **L07 E05**（拆字段）、**L08 E01**（记录）、**L12 E01**（类）。

**下一道变式**　⟦9618_s22_42:3(c)⟧　QP p.8、MS p.28–29。CardValues.txt 变为每张卡两行：数字、颜色；循环 30 组，创建 30 个 Card 对象。两行是一条记录，不能把 60 行当 60 张卡。

<!-- auto:drills P4-FL-02 -->

### P4-FL-03　写入或追加文本文件　{#P4-FL-03}

<!-- auto:stats P4-FL-03 -->

**考法**　把数组或结构中的数据逐项写入文件；题目可能要求覆盖、新建或追加，且每项一行或多字段按顺序写出。

**识别信号**　appends each item；new line；takes array and filename as parameters；exception handling when opening and writing。

**解题思路**
1. 先确定模式：WRITE 对应 w，APPEND 对应 a。a 会保留旧内容。
2. 文件名来自参数时直接使用参数，不重新输入，不写死红色文件。
3. 循环每个元素，把整数转 str 后写出，再补换行。
4. 整个 with 放在 try 中，文件操作失败时输出提示。
5. 运行前复制官方空文件；追加题重复运行会重复写入，不能把两轮结果误作首轮结果。

**Python 模板**

```python
def StoreData(DataToStore, FileName):
    try:
        with open(FileName, "a") as File:
            for Item in DataToStore:
                File.write(str(Item) + "\n")
    except OSError:
        print("Cannot create or write to file")
```

**得分表述**（引自对应 MS）
- 「Procedure header taking (1D) array and filename as parameters, opening file to append and closing file (in appropriate place)」⟦9618_s25_41:2(c)⟧
- 「Looping through each item in array parameter …」⟦9618_s25_41:2(c)⟧
- 「… writing to the file」⟦9618_s25_41:2(c)⟧
- 「… with new line break between each line」⟦9618_s25_41:2(c)⟧
- 「Using exception handling try and catch with suitable output」⟦9618_s25_41:2(c)⟧

**得分点地图**（核验语料 2022–2026s、主题型行、去掉 `equivalent_of`；同一行同一标签计一次；s26 只进计数。本型 4 行，均已拆点。下表列出现行数最多的 8 个标签；同次数按标签名排序，不把行数当分值。）

| 技能标签 | 行数 |
|:--|--:|
| `count-loop` | 4 |
| `exception-handling` | 4 |
| `file-close` | 4 |
| `file-write` | 4 |
| `module-header` | 4 |
| `output-format` | 4 |
| `string-concat` | 3 |
| `type-conversion` | 2 |

地图用于安排复习：先练覆盖行数较多的技能，再按当前题自己的 MS 检查每一点。多个标签可以属于同一个得分点，不能相加算分。

**易错与失分**
- 用 w 代替 a 会覆盖已有数据；本题明确要求追加。
- 文件名参数收下后却不用，导致六种颜色写进同一文件。考官报告指出了这个问题（⟦9618_s25_41:2(c)⟧）。
- 不补换行，多个数黏在一起；只把数组 print 到控制台也不是写文件。

#### 代表题精讲　⟦9618_s25_41:2(c)⟧

**在考什么**　QP p.5，MS p.26–27（Python p.26）。5 个独立点各 1 分；模块头、追加模式、适当位置关闭合在 MP1，不能拆成三分。与 FL-01 共用本题的整题程序，下面是相同的最终版本。

**完整作答**（整道大题的最终程序；分格提交时按小问截取代码，早期截图在后续修改前另存）

```python
# Question2_J25: 2(a)-(e)
def ReadData():
    DataList = []  # STRING, unknown number of lines
    FileName = input("Enter the filename: ")
    try:
        with open(FileName, "r") as File:
            for Line in File:
                DataList.append(Line.rstrip("\n"))
    except OSError:
        print("Cannot open or read the file")
    return DataList


def StoreData(DataToStore, FileName):
    try:
        with open(FileName, "a") as File:  # MP1 append and automatic close
            for Item in DataToStore:  # MP2
                File.write(str(Item))  # MP3
                File.write("\n")  # MP4
    except OSError:
        print("Cannot create or write to file")  # MP5


def SplitData(DataArray):
    Red = []  # INTEGER arrays, unknown size, one per colour
    Green = []
    Blue = []
    Orange = []
    Yellow = []
    Pink = []
    for Index in range(len(DataArray)):
        Parts = DataArray[Index].split(",")
        Number = int(Parts[0])
        Colour = Parts[1]
        if Colour == "red":
            Red.append(Number)
        elif Colour == "green":
            Green.append(Number)
        elif Colour == "blue":
            Blue.append(Number)
        elif Colour == "orange":
            Orange.append(Number)
        elif Colour == "yellow":
            Yellow.append(Number)
        elif Colour == "pink":
            Pink.append(Number)
    StoreData(Red, "Red.txt")
    StoreData(Green, "Green.txt")
    StoreData(Blue, "Blue.txt")
    StoreData(Orange, "Orange.txt")
    StoreData(Yellow, "Yellow.txt")
    StoreData(Pink, "Pink.txt")


if __name__ == "__main__":
    DataFromFile = ReadData()
    SplitData(DataFromFile)
```

**运行核对**　在官方空颜色文件副本上输入 TheData.txt，退出码 0；Red.txt 首轮有 12 行且顺序为 10、9、1、76、19、38、34、46、14、45、37、43。对同一临时副本再跑一次变为 24 行，两段相同，确认使用追加而非覆盖；写入失败路径输出提示。

**与 MS 逐点对齐**　MS 未印逐点号码；下表 MP 按语料 `markpoints[].n` 顺序。

| MP | MS 要求（原文） | 作答中对应 | 技能标签 |
|:--|:--|:--|:--|
| 1 | Procedure header taking (1D) array and filename as parameters, opening file to append and closing file (in appropriate place) | `def StoreData(DataToStore, FileName)`；a 模式；with 关闭 | `module-header`、`file-append`、`file-close` |
| 2 | Looping through each item in array parameter … | `for Item in DataToStore` | `count-loop` |
| 3 | … writing to the file | `File.write(str(Item))` | `file-append` |
| 4 | … with new line break between each line | `File.write("\n")` | `file-write`、`string-concat` |
| 5 | Using exception handling try and catch with suitable output | `except OSError` 与错误输出 | `exception-handling`、`output-format` |

**分值边界**　该小问 5 分；全部列点按该题 MS 计分。`//` 是同一点的替代说法，接续句是否独立成点以本表与原页为准。

**证据格怎么交**　2(c) 格贴 StoreData()，2(d) 格贴带六次调用的 SplitData()。2(e)(ii) 除输入文件名截图外，还要打开实际 Red.txt 截图，同张图看得到 Red.txt 文件名与内容（MS p.29）。

**直观**　写文件像在账本末尾逐行记账：a 翻到最后接着写，w 是先换一本空账本。

**对应练习与阶梯**　practice/p4/9618_s25_41_q2/（T35 并行生成，按目录命名规则定位）；前置阶梯 **L07 E04**（覆盖与追加）、**L07 E05**（按条件写文件）。

**下一道变式**　⟦9618_s22_41:1(f)⟧　QP p.4、MS p.17–18。WriteTopTen() 改为 NewHighScore.txt 的覆盖写，按名字、分数各一行写 10 人；MS 清单 5 点 Max 4。模板里改 w，同时保留异常处理，不照抄示例中 `Filename.close` 缺括号的写法（p.17）。

<!-- auto:drills P4-FL-03 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| FL-01 / FL-02 | 一行直接成为一项，或交给 ADT → FL-01；拆字段或几行组成记录 / 对象 → FL-02 | 有没有构造对象和字段分组 |
| FL-02 / AR-05 | 文件读入建对象 → FL-02；已有数组再分类或筛选 → AR-05 | 数据来自文件还是参数数组 |
| w / a | w 覆盖；a 追加 | write / append |
| EOF / 空白行 | readline() 的空串才是 EOF；只有换行的行仍是一行 | 去换行前先判断 EOF |
| return / print / write | 返回给调用者 / 控制台显示 / 文件保存 | 题目要求的数据去向 |
