## DB　数据库 {#ch-DB}

<!-- auto:chapter-stats -->

### 核心思想

数据库是 P1 分值最多的一章，而且**几乎每卷都有一整道数据库大题**：给一个情境和几张表的定义，从概念、关系、范式一路问到 SQL。按大题里的出场顺序，13 个题型分四块：

1. **为什么用关系数据库、它由什么组成**（DB-01、DB-02）：文件方式会重复存储、数据不一致、程序依赖数据结构；关系数据库用相互链接的表解决。术语：entity、table、record / tuple、field / attribute，以及主键、候选键、次键、外键、复合键。
2. **表与表怎样连起来、表该怎样拆**（DB-03 至 DB-06）：1:1、1:M、M:N 关系，用“主键—外键”实现，M:N 用连接表拆掉（DB-03）；画成 E-R 图（DB-04）；判断 1NF / 2NF / 3NF（DB-05）；动手把表规范化到 3NF（DB-06）。
3. **DBMS 帮你做什么**（DB-07 至 DB-09）：数据字典、逻辑模式、开发者界面、查询处理器（DB-07）；安全——访问权限、视图、备份、加密、记录锁（DB-08）；完整性——参照完整性、级联更新与删除、校验（DB-09）。
4. **SQL**（DB-10 至 DB-13）：DDL 建库、建表、改表（DB-10）；单表查询（DB-11）；两表连接查询（DB-12）；插入、修改、删除记录（DB-13）。

整章有一条主线：**主键唯一标识一条记录 → 外键引用另一张表的主键 → 关系就靠这对键实现 → 规范化就是把每个事实放到“它只依赖主键”的那张表里 → 参照完整性保证外键总能找到主键 → SQL 连接查询就是让两张表的这对键相等。** 弄懂这条线，DB 的大部分题都是同一件事的不同问法。

### 表定义的记号

题目把表写成 `TableName(Field1, Field2, …)`，原卷里**主键加实线下划线**，有时**外键加虚线下划线**；抽取的文字里下划线丢了，所以本章讲解时用**粗体表示主键**、*斜体表示外键*。例如 SALE(**SaleID**, *BatchID*, *CustomerID*, Quantity, Date)。自己作答时照题目要求画下划线。

### SQL 速查（9618 考的全部写法）

**DDL（定义结构）**

```sql
CREATE DATABASE SHOP;

CREATE TABLE STUDENT_TEST(
  StudentID INTEGER NOT NULL,
  TestID VARCHAR(5) NOT NULL,
  Mark INTEGER,
  PRIMARY KEY (StudentID, TestID),
  FOREIGN KEY (StudentID) REFERENCES STUDENT(StudentID),
  FOREIGN KEY (TestID) REFERENCES TEST(TestID)
);

ALTER TABLE PURCHASE
ADD OrderDate DATE;

ALTER TABLE EXAM_QUESTION
ADD FOREIGN KEY (ExamID) REFERENCES EXAM(ExamID);
```

数据类型用考纲给的这七种（⟦9618_s23_11:2(b)(iii)⟧ 的题干照抄了这张表）：`CHARACTER`、`VARCHAR(n)`、`BOOLEAN`、`INTEGER`、`REAL`、`DATE`、`TIME`。MS 也接受 `INT`、`CHAR`、不写长度的 `VARCHAR` 等常见写法。

**DML（查询与维护数据）**

```sql
SELECT Field1, COUNT(Field2) AS NewName      -- or SUM(...) / AVG(...)
FROM TABLE1 INNER JOIN TABLE2
ON TABLE1.KeyField = TABLE2.KeyField
WHERE Condition1 AND Condition2
GROUP BY Field1
ORDER BY Field1 DESC;                        -- ASC is the default

INSERT INTO PRODUCT (ProductID, ProductName, Cost)
VALUES ("002323", "Blue pen", 5.00);

UPDATE CHARACTER
SET Level = 3, Money = 10000.00
WHERE CharacterID = "0002";

DELETE FROM PLACEMENT
WHERE Complete = TRUE;
```

**值的写法**：字符串加引号（`"Caledonia"` 或 `'Caledonia'` 都行）；数字不加引号；布尔值写 `TRUE` / `FALSE`；日期写 `#31/12/2023#`；模糊匹配 `LIKE 'HW%'`（MS 也接受 `*`）。

**MS 怎样给 SQL 分**：一个子句或一个要素一分——“SELECT 了正确的字段 / 聚合”“AS 起了合适的名字”“FROM 正确的表”“两表连接条件”“每个 WHERE 条件”“GROUP BY”“ORDER BY”。所以：题目每说一个要求（“给合适的名字”“按降序”“只要已付款的”），答案里就要有一个对应的子句；表名、字段名一律照题目抄。

### 题型树
<!-- auto:type-tree -->

### P1-DB-01　文件方式的局限与关系数据库　{#P1-DB-01}

<!-- auto:stats P1-DB-01 -->

**考法**　①给出文件方式的一个局限，并解释关系数据库怎样解决（局限 1 + 解释 2）；②描述关系数据库怎样解决文件方式的局限（两点，每点成对给分）；③解释 / 说出关系数据库相对文件方式的好处（3–4 分）；④（2021 扩展）解释“文件方式更好”的说法为什么错。

**识别信号**　file-based approach；limitation(s)；advantages / benefits of a relational database compared to / instead of a file-based approach；how a relational database addresses。

**解题思路**　三对“局限 ↔ 解决”，每对写成“好处 + …because”：

| 文件方式的局限 | 关系数据库怎样解决 |
|:--|:--|
| 数据冗余：同一数据在多个文件里重复存储 | 用相互链接的表，每个数据项只存一次 → 冗余减少 |
| 数据不一致、完整性差：一处改了别处没改 | 数据只存一次，改一次处处生效；链接的数据不能在两张表里写成不同的样子；可强制参照完整性 |
| 程序—数据依赖：改数据结构就得重写程序 | 数据结构由 DBMS 管理，与程序分离；改数据不必重写程序，查询不依赖数据结构 |

再加两条只拿 1 分的好处：复杂查询更容易执行；可以提供不同的视图（用户只看到数据库的特定部分，隐私更好）；（还有：通过记录锁支持多人同时访问。）

**得分表述**（引自对应 MS）
- 「Data items are stored once so reduces data duplication / data redundancy」⟦9618_w24_11:2(a)⟧
- 「Data changed once in one place will automatically update elsewhere」⟦9618_w24_11:2(a)⟧
- 「linked data cannot be entered differently in two tables」⟦9618_w24_12:6(a)⟧
- 「Program-data independence is ensured」⟦9618_w24_12:6(a)⟧
- 「Complex queries are easier to run」⟦9618_w24_12:6(a)⟧
- 「so users can only see specific aspects of the database」⟦9618_w24_12:6(a)⟧

**易错与失分**
- 只写“less redundancy”而不写“因为每个数据项只存一次 / 表相互链接”：成对给分的题丢一半。
- 把“冗余”与“不一致”写成一个点：冗余是**重复存**，不一致是**重复存导致的不同步**，是两个点。
- 写“数据库更安全、更快”这类空话：MS 没有这些点。
- 题目要“一个局限 + 解释”，解释必须对应你写的那个局限。

#### 代表题精讲　⟦9618_w24_11:2(a)⟧

**在考什么**　修理店老板用文件方式存修理记录。Give one limitation of using a file-based approach to store the data and explain how a relational database addresses this limitation. 3 分 = 局限 1 + 对应解释 2。

**完整作答**　局限：数据冗余——同一位顾客的资料在每次修理的文件里都要重复存一遍。解释：关系数据库使用相互链接的独立表（顾客表、修理表）；每个数据项只存一次（顾客资料只存在顾客表里，修理表用顾客编号引用），从而减少数据重复。

**与 MS 对齐**　局限 ←“Data redundancy // data duplication”；解释 ←“Separate linked tables are used”“Data items are stored once so reduces data duplication / data redundancy”。也可选“数据不一致”（解释：改一处处处更新、强制参照完整性）或“程序依赖数据结构”（解释：结构由 DBMS 管理、改数据不必重写程序）。

**英文作答句**　Limitation: data redundancy, because the same customer details are stored again for every repair. A relational database uses separate linked tables, so each data item is stored only once, which reduces data duplication.

**直观**　文件方式像每张修理单都手抄一遍顾客地址；关系数据库是把地址记在通讯录里，修理单上只写顾客编号。

**下一道变式**　⟦9618_s23_13:4(a)⟧　（两点描述、每点成对给分：每点都要写“好处 + because”。）

<!-- auto:drills P1-DB-01 -->

### P1-DB-02　关系模型术语与键　{#P1-DB-02}

<!-- auto:stats P1-DB-02 -->

**考法**　①术语表：写出定义或由描述写出术语（entity、tuple、attribute、field、secondary key、foreign key、candidate key、referential integrity）；②在给定表里找外键及其引用的表；③找候选键；④在表定义里给主键（含复合键）画下划线；⑤解释某表为什么用复合主键；⑥给出术语的定义并用本数据库举例。

**识别信号**　Define / State what is meant by；entity；tuple；attribute；field；primary / candidate / secondary / foreign / composite key；Identify two foreign keys … and the table each references；Underline the attribute(s) that form the primary key。

**解题思路**
1. 术语定义（按 MS 原词背）：

| 术语 | 定义 |
|:--|:--|
| Entity | 关于它要存数据的对象（现实中的人或事物），表示为一张表 |
| Table | 关于一个实体的数据，按行和列组织 |
| Record / tuple | 表中的一行：实体的一个实例 |
| Field / attribute | 表中的一列：关于实体的一项数据 |
| Primary key | 唯一标识每条记录的属性或属性组合 |
| Candidate key | 可以当主键（值唯一）但不一定被选中的属性或属性组合 |
| Secondary key | 没被选为主键的候选键，或主键之外另用来查找数据的键 |
| Foreign key | 一张表中链接到另一张表主键的字段 |
| Composite key | 由两个或以上属性共同组成的主键 |

2. **找外键**：在一张表里找“名字和另一张表主键相同”的字段，例如 SALE 里的 BatchID → BATCH，CustomerID → CUSTOMER。答题写“外键名 + 它所在 / 引用的表”，看清题目问的是哪一个。
3. **找候选键**：除主键外，哪个字段的值对每条记录都不同？（卡号、序列号、邮箱。）
4. **复合主键**：连接表（如 FILM_ACTOR(ActorID, FilmID)）中，单独一个字段会重复出现，两个字段合起来才唯一。

**得分表述**（引自对应 MS）
- 「The unique attribute / combination of attributes used to identify the record / tuple」⟦9618_w23_12:2(a)⟧
- 「An attribute / field (or set of attributes / fields) that could be a primary key」⟦9618_w22_12:5(c)⟧
- 「A field in one table that is linked to a primary key in another table」⟦9618_s23_13:4(b)⟧
- 「An item of data about an entity」⟦9618_w24_13:4(d)⟧
- 「a single row in a table」⟦9618_w22_11:4(c)(i)⟧
- 「Ensures that every foreign key has a corresponding primary key」⟦9618_w23_12:2(a)⟧

**易错与失分**
- 主键定义漏 **unique**：只写“identifies a record”不给分。
- 外键写成“another table’s primary key”而没说“在本表中、链接到另一表”：要写清楚两张表的关系。
- 候选键答成主键本身：题目要的是“could be a primary key”的**另一个**字段。
- 下划线题：连接表的复合键两个字段都要画，单键表只画一个。
- 外键题把“外键所在的表”和“外键引用的表”弄反。

#### 代表题精讲　⟦9618_s23_13:4(b)⟧

**在考什么**　租车店的关系数据库。Complete the table by writing the missing term or description for each database feature. 4 格各 1 分：给描述写术语（2 格），给术语写描述（2 格）。

**完整作答**

| Term | Description |
|:--|:--|
| Entity | An object that data is stored about. |
| Tuple | 表中关于一个对象实例的一行数据 |
| Secondary key | 除主键外另用来查找特定数据的键；或没有被选为主键的候选键 |
| Foreign key | A field in one table that is linked to a primary key in another table. |

**与 MS 对齐**　Entity ←“Entity”；Tuple ←“A row of data in a table about one instance of an object”；Secondary key ←“An additional/alternative key used as well as the primary key to locate specific data // a candidate key that has not been chosen as a primary key”；Foreign key ←“Foreign key”。

**英文作答句**　Entity. Tuple: a row of data in a table about one instance of an object. Secondary key: an alternative key used as well as the primary key to locate specific data, or a candidate key that has not been chosen as the primary key. Foreign key.

**直观**　表像花名册：每一行（tuple）是一个人，每一列（attribute）是一项信息；学号是主键，身份证号是候选键，班级表里引用的“班主任工号”是外键。

**下一道变式**　⟦9618_s22_12:5(b)⟧　（换成解释：连接表 FILM_ACTOR 为什么要用复合主键，2 分。）

<!-- auto:drills P1-DB-02 -->

### P1-DB-03　关系类型及其实现　{#P1-DB-03}

<!-- auto:stats P1-DB-03 -->

**考法**　①说出两表之间的关系（1:M、M:1，1 分）；②描述两表之间的关系，并提到主键与外键（2–4 分）；③识别数据库中每个关系并解释怎样实现（6 分）；④解释连接表的作用（消除 M:N）；⑤（2021 扩展）给出 1:1、1:M、M:N 的例子；哪种关系不能直接实现。

**识别信号**　Identify / Describe the relationship between …；Refer to the primary and foreign keys in your answer；one-to-many / 1:M；many-to-many；Explain the purpose of the table …（连接表）。

**解题思路**
1. **判断度数**：看外键在哪边。B 表里有 A 表的主键作外键 → A 对 B 是 **1:M**（一个 A 对应多个 B，每个 B 只属于一个 A）。题目问“B 和 A”时顺序反过来写成 **M:1**。
2. **1:1**：外键在一边且每个值只出现一次（员工 ↔ 登录数据）。
3. **M:N**：两边都能对应多个（角色 ↔ 物品、学生 ↔ 课程）。关系数据库**不能直接实现**，要建**连接表**：连接表里放两张表的主键作外键，把一个 M:N 拆成两个 1:M。
4. 描述题写满四件事：①度数；②主键在哪张表；③它在另一张表里作外键；④用情境话解释（“一位员工可以有多台设备，每台设备只属于一位员工”）。

**得分表述**（引自对应 MS）
- 「implemented by Primary Key in CUSTOMER is Foreign Key in JOB」⟦9618_w24_12:6(b)(i)⟧
- 「EMPLOYEE to LOGIN_DATA is 1 to 1」⟦9618_w24_12:6(b)(i)⟧
- 「The primary key ShipID in the SHIP table is linked to the foreign key ShipID in the CONTAINER table」⟦9618_w25_12:4(a)⟧
- 「One staff member can have many devices」⟦9618_s22_13:6(a)⟧
- 「Each device can only be with one member of staff」⟦9618_s22_13:6(a)⟧
- 「many to 1 // there are many performances of each show」⟦9618_s24_13:4(a)⟧

**易错与失分**
- 度数方向写反：问 “PERFORMANCE and SHOW” 时答 many-to-one，不是 one-to-many。
- 描述题只写 “1:M”，不提主键、外键：题目明说 Refer to the primary and foreign keys 时，键的那两分就丢了。
- 漏掉连接表与两边的关系：连接表与两张主表各有一个 1:M。
- 把 M:N 当成可以直接用外键实现。

#### 代表题精讲　⟦9618_w24_12:6(b)(i)⟧

**在考什么**　修理公司的规范化数据库：CUSTOMER、EMPLOYEE、LOGIN_DATA（每位员工的用户名和密码）、JOB（每个修理工作）、JOB_EMPLOYEE（每个工作由哪些员工负责）。Identify each relationship between the database tables and explain how each relationship can be implemented in the normalised database. 6 分，每个关系“度数 1 + 实现 1”。

**完整作答**
1. CUSTOMER 对 JOB 是 1 对多：CUSTOMER 的主键作为外键放在 JOB 中。
2. EMPLOYEE 对 LOGIN_DATA 是 1 对 1：EMPLOYEE 的主键作为外键放在 LOGIN_DATA 中。
3. JOB 对 JOB_EMPLOYEE 是 1 对多：JOB 的主键作为外键放在 JOB_EMPLOYEE 中。
4. EMPLOYEE 对 JOB_EMPLOYEE 是 1 对多：EMPLOYEE 的主键作为外键放在 JOB_EMPLOYEE 中。

（JOB 与 EMPLOYEE 本来是多对多——一个工作可由多名员工做、一名员工可做多个工作——JOB_EMPLOYEE 就是拆掉它的连接表。）

**与 MS 对齐**　1 ←“CUSTOMER to JOB is 1 to many”+“… implemented by Primary Key in CUSTOMER is Foreign Key in JOB”；2 ←“EMPLOYEE to LOGIN_DATA is 1 to 1”+“… implemented by Primary Key in EMPLOYEE is Foreign Key in LOGIN_DATA”；3、4 同理。四个关系 8 点，写满 3 个关系即 6 分，写全 4 个更稳。

**英文作答句**　CUSTOMER to JOB is one-to-many, implemented by the primary key of CUSTOMER being a foreign key in JOB. EMPLOYEE to LOGIN_DATA is one-to-one, implemented by the primary key of EMPLOYEE being a foreign key in LOGIN_DATA. JOB to JOB_EMPLOYEE is one-to-many, implemented by the primary key of JOB being a foreign key in JOB_EMPLOYEE. EMPLOYEE to JOB_EMPLOYEE is one-to-many, implemented by the primary key of EMPLOYEE being a foreign key in JOB_EMPLOYEE.

**直观**　外键像“挂号单上写的病人编号”：病人表是“1”，挂号单表是“多”；一个病人可以挂很多次号，每张挂号单只属于一个病人。

**下一道变式**　⟦9618_s25_12:5(a)⟧　（解释连接表 CHARACTER_ITEM 的作用：它拆掉的是哪两张表之间的哪种关系。）

<!-- auto:drills P1-DB-03 -->

### P1-DB-04　E-R 图　{#P1-DB-04}

<!-- auto:stats P1-DB-04 -->

**考法**　给出表定义和画好的实体方框，补全 E-R 图：在方框之间连线并标出每个关系的度数（2–4 分，每个关系 1 分；多画会被扣）。

**识别信号**　Complete / Draw the entity-relationship (E-R) diagram；页面上已有 CUSTOMER、ORDER… 等方框。

**解题思路**
1. 逐张表找外键：每个外键对应**一条**连线，连到它引用的那张表。
2. 外键所在的表是“多”端，被引用的表是“一”端。
3. 用鸦爪记号画：一端是单线，多端是三叉（鸦爪）。本手册用文字写成 `A ──< B`，表示 A 对 B 是 1:M，`<` 是 B 端的鸦爪。
4. 连接表（含两个外键）连两条线，两条都是“鸦爪在连接表一端”。
5. 只画外键所表示的关系：两张表之间没有外键就**不要**连线。

**得分表述**（引自对应 MS）
- 「1:M between CUSTOMER and PARTY」⟦9618_w22_11:4(a)⟧
- 「1:M between PARTY and PHOTO_DATA」⟦9618_w22_11:4(a)⟧
- 「1:M between CAMERA_DATA and PHOTO_DATA」⟦9618_w22_11:4(a)⟧
- 「1 mark for both 1:M relationships as follows」⟦9618_w23_13:3(b)(i)⟧
- 「Max 2 if any extra」⟦9618_s25_11:5(a)⟧

**易错与失分**
- 鸦爪画在错的一端：多端是**有外键的那张表**。
- 多画连线（例如把 CUSTOMER 直接连到 PHOTO_DATA）：MS 写明有多余连线就封顶。
- 只连线不标度数，或画成 M:N：规范化的数据库里不会有 M:N 连线。
- 讲解时请对照原卷：E-R 图的方框位置和 MS 的标准答案只在原页图上。

#### 代表题精讲　⟦9618_w22_11:4(a)⟧

**在考什么**　摄影师的数据库 PHOTOGRAPHS：CUSTOMER(**CustomerID**, FirstName, LastName, Telephone)、PARTY(**PartyID**, *CustomerID*, PartyDate, StartTime)、PHOTO_DATA(**PhotoID**, *PartyID*, TimeTaken, *CameraID*)、CAMERA_DATA(**CameraID**, LensType, LightingType)。Complete the E-R diagram. 3 分，每个关系 1 分。讲解时请对照原卷 QP p.6（方框布局）与 MS p.5（标准图）。

**完整作答**　逐张找外键：PARTY 里的 CustomerID → CUSTOMER；PHOTO_DATA 里的 PartyID → PARTY，CameraID → CAMERA_DATA。共三条线：

```
CUSTOMER ──< PARTY ──< PHOTO_DATA >── CAMERA_DATA
```

即 CUSTOMER 对 PARTY 1:M；PARTY 对 PHOTO_DATA 1:M；CAMERA_DATA 对 PHOTO_DATA 1:M（鸦爪都在有外键的那一端）。

**与 MS 对齐**　“1:M between CUSTOMER and PARTY”“1:M between PARTY and PHOTO_DATA”“1:M between CAMERA_DATA and PHOTO_DATA”，三条线各 1 分。

**英文作答句**　(Diagram) CUSTOMER one-to-many PARTY; PARTY one-to-many PHOTO_DATA; CAMERA_DATA one-to-many PHOTO_DATA, with the crow’s foot at the PARTY end and at both PHOTO_DATA ends.

**直观**　一位顾客办很多场派对，一场派对拍很多张照片，一台相机拍很多张照片——“很多”的那一边长出鸦爪。

**下一道变式**　⟦9618_w23_11:3(a)⟧　（五张表，其中有连接表 ORDER_ITEM：它要连两条线。讲解时请对照原卷 QP p.6 与 MS p.5。）

<!-- auto:drills P1-DB-04 -->

### P1-DB-05　范式　{#P1-DB-05}

<!-- auto:stats P1-DB-05 -->

**考法**　①描述处于 3NF 的数据库的特征（3 分）；②给出数据库所处的最高范式并论证（范式 1 + 理由 2）；③解释某数据库为什么处于 3NF；④填表：描述 1NF、2NF、3NF；⑤连线：范式 ↔ 定义；⑥解释为什么某表的数据不能并入另一张表（会出现重复组、不在 1NF）。

**识别信号**　First / Second / Third Normal Form (1NF / 2NF / 3NF)；characteristics of a database that is in 3NF；the highest level of Normal Form … justify；repeating groups；partial dependencies；non-key / transitive dependencies。

**解题思路**　三级范式一级一级加条件：

| 范式 | 条件（在前一级的基础上） | 判断时问自己 |
|:--|:--|:--|
| 1NF | 没有重复的属性组；每个字段是原子的（一格只放一个值）；有主键 | 有没有一格里放了一串值，或 Subject1、Subject2… 这样重复的列？ |
| 2NF | 没有部分依赖：每个非键属性依赖**整个**主键 | 主键是复合键吗？如果是，有没有字段只依赖其中一部分？（单字段主键的 1NF 表自动是 2NF） |
| 3NF | 没有非键依赖（传递依赖）：非键属性只依赖主键，不依赖别的非键属性 | 有没有字段其实是由另一个非键字段决定的？ |

判断一个数据库的步骤：
1. 逐张表查 1NF：有重复组或一格多值 → 0NF（未规范化）。
2. 有复合主键的表查 2NF：比如 STUDENT_TEST(StudentID, TestID, Mark)，Mark 依赖“哪个学生 + 哪次测验”两者 → 无部分依赖。
3. 逐张表查 3NF：比如 BATCH(BatchID, Type, Flavour, Size, SellingPrice, EndDate)，售价由冰淇淋的品种决定而不是由批次决定 → 有非键依赖 → 不在 3NF。
4. 还要看有没有未拆开的 M:N 关系（例如 OWNER 表里塞了 TreeID）。
5. 论证题写“范式名 + 2 条理由”，理由最好举本数据库里的字段。

**得分表述**（引自对应 MS）
- 「no repeating groups of attributes // data is atomic」⟦9618_w22_11:4(b)⟧
- 「no partial key dependencies」⟦9618_w22_11:4(b)⟧
- 「no non-key dependencies // no transitive dependencies」⟦9618_w22_11:4(b)⟧
- 「All attributes must be fully dependent on the primary key and no other attributes」⟦9618_s22_13:6(c)⟧
- 「There are no many-to-many relationships」⟦9618_w25_11:2(b)⟧
- 「Each order would only be able to have one item」⟦9618_s25_11:5(d)⟧

**易错与失分**
- 3NF 只写“no transitive dependencies”：3 分题要把 1NF、2NF 的条件也写上（3NF 包含前两级）。
- 把“部分依赖”与“非键依赖”说反：部分依赖是依赖**主键的一部分**（只在复合键里出现）；非键依赖是依赖**另一个非键字段**。
- 只说“normalised”不说到哪一级。
- 范式 ↔ 定义的连线题（⟦9618_s23_11:2(b)(ii)⟧，三条全对才给 1 分）：原题三句话的排列顺序故意与范式错开，按定义连——“no repeating groups of attributes”→ 1NF，“no partial dependencies”→ 2NF，“All fields are fully dependent on the primary key”→ 3NF。抽取的 MS 文字只是原题排版，连线结果讲解时请对照原卷 MS p.4。

#### 代表题精讲　⟦9618_w22_11:4(b)⟧

**在考什么**　摄影师的数据库已规范化到 3NF。Describe the characteristics of a database that is in Third Normal Form (3NF). 3 分。

**完整作答**
1. 没有重复的属性组，所有数据都是原子的（1NF）；
2. 没有部分键依赖：每个非键属性都依赖整个主键（2NF）；
3. 没有非键依赖（传递依赖）：非键属性只依赖主键，不依赖其他非键属性（3NF）。

**与 MS 对齐**　1 ←“no repeating groups of attributes // data is atomic”；2 ←“no partial key dependencies”；3 ←“no non-key dependencies // no transitive dependencies”。

**英文作答句**　There are no repeating groups of attributes and the data is atomic. There are no partial key dependencies, so every non-key attribute depends on the whole primary key. There are no non-key (transitive) dependencies, so every non-key attribute depends only on the primary key.

**直观**　3NF 的口诀：每个字段都要依赖“the key（1NF）, the whole key（2NF）, and nothing but the key（3NF）”。

**下一道变式**　⟦9618_s22_11:4(b)⟧　（给出 MARKS 数据库所处的最高范式并论证：先判断，再用三张表举理由。）

<!-- auto:drills P1-DB-05 -->

### P1-DB-06　规范化设计　{#P1-DB-06}

<!-- auto:stats P1-DB-06 -->

**考法**　①按情境描述设计一个 3 表 3NF 数据库，按 TableName(Field1, …) 格式写出并标主键、外键（6 分）；②把给定的未规范化表规范化，写出新表定义（4 分）；③解释怎样把表改成 1NF / 3NF（3–4 分）；④描述还需要哪些表、各表怎样链接（5 分）。

**识别信号**　Create a 3-table design … normalised to 3NF；Normalise the database table …；Write the table definitions for your new tables；Explain how the database can be normalised；Describe the additional tables that will need to be included；The following database table is not normalised。

**解题思路**（规范化设计五步）
1. **找实体**：情境里每一类“要存数据的东西”一张表（学生、书、借阅；顾客、车、预订）。
2. **每张表定主键**：已有唯一字段就用（车牌号、用户名），否则新建 ID 字段。不要用名字当主键（会重名）。
3. **把每个字段放到它只依赖主键的那张表**：车型、颜色属于车，不属于预订；顾客的姓、邮箱属于顾客。
4. **按关系放外键**：1:M → 把“1”端的主键放进“多”端作外键；M:N → 建连接表，放两边的主键作外键，再放只属于这对关系的字段（分数、数量、借书日期）。
5. **检查**：原来的字段一个不少、每个只出现一次（外键除外）；表名合适；主键、外键按题目要求标出。

改成 1NF 的写法：找出重复组（如 Subject 与 SubjectCode 一格多个值）→ 拆成单独的行或单独的表；把非原子字段拆开（StudentName → FirstName、LastName）；确定主键。

**得分表述**（引自对应 MS）
- 「Booking table includes Primary key from car and Primary key from customer as Foreign keys」⟦9618_s23_13:4(c)⟧
- 「All original fields are in correct tables」⟦9618_s23_13:4(c)⟧
- 「Identify repeating groups of attributes」⟦9618_w23_12:2(c)⟧
- 「Ensure each field is atomic」⟦9618_w23_12:2(c)⟧
- 「removing the many-to-many relationship between Owner and Tree」⟦9618_w22_12:5(a)⟧
- 「that stores the Primary Key of the CUSTOMER table as a Foreign Key to join with CUSTOMER table」⟦9618_s24_13:4(d)⟧

**易错与失分**
- 连接表忘了放两边的外键，或忘了放“属于关系本身”的字段（分数、日期）。
- 用 FirstName 当主键：会重名。MS 的标准答案都新建了 ID。
- 题目说“只要 3 张表”却设计出 4 张，或说“不要改 CUSTOMER 和 SALE”却改了。
- 字段丢失：原表里的每个字段都要出现在新设计里。
- 只写表名不写字段，或主键 / 外键没有按要求标出。

#### 代表题精讲　⟦9618_s23_13:4(c)⟧

**在考什么**　租车数据库未规范化：BOOKING(CarRegistration, StartDate, EndDate, CarModel, CarColour, CustomerFirstName)、CUSTOMER(CustomerFirstName, CustomerLastName, EmailAddress, TelephoneNumber)。Write a normalised database design … All tables must be in 3NF. Use the field names given and underline the primary key fields. 4 分。讲解时请对照原卷 MS p.6 看下划线。

**先找问题**
- CarModel、CarColour 由车（CarRegistration）决定，不由一次预订决定 → 车的信息应单独成表。
- 用 CustomerFirstName 当顾客主键不唯一（会重名）→ 需要 CustomerID。
- BOOKING 需要自己的主键（同一辆车会被多次预订）。

**完整作答**（粗体为主键，斜体为外键）
- BOOKING(**BookingID**, *CarRegistration*, *CustomerID*, StartDate, EndDate)
- CAR(**CarRegistration**, CarModel, CarColour)
- CUSTOMER(**CustomerID**, CustomerFirstName, CustomerLastName, EmailAddress, TelephoneNumber)

**与 MS 对齐**　“Only 3 tables with appropriate identifiers (i.e. one table for customer, one for booking and one for car)”；“Appropriate Primary key in each table underlined”；“Booking table includes Primary key from car and Primary key from customer as Foreign keys”；“All original fields are in correct tables”。四点各 1 分，与 MS 的 Example answer 完全一致。

**英文作答句**　BOOKING(BookingID, CarRegistration, CustomerID, StartDate, EndDate); CAR(CarRegistration, CarModel, CarColour); CUSTOMER(CustomerID, CustomerFirstName, CustomerLastName, EmailAddress, TelephoneNumber) — with BookingID, CarRegistration and CustomerID underlined as the primary keys of the three tables.

**直观**　规范化就是“一件事只记一次、记在它该在的地方”：车的颜色写在车的档案里，预订单上只写车牌号。

**下一道变式**　⟦9618_s24_11:6(a)⟧　（从一段文字情境出发设计 3 张表：用户、测验和中间的成绩表，6 分。）

<!-- auto:drills P1-DB-06 -->

### P1-DB-07　DBMS 的功能与工具　{#P1-DB-07}

<!-- auto:stats P1-DB-07 -->

**考法**　①描述数据字典（含义 + 例子）、逻辑模式；②数据字典里还存什么（另外三项）；③开发者界面的用途；④查询处理器的作用；⑤DBMS 功能填空 / 名称与描述配对；⑥说出“描述数据与其结构关系”的功能（logical schema）。

**识别信号**　Database Management System (DBMS)；data dictionary；metadata；logical schema；data modelling；developer interface；query processor。

**解题思路**　四个工具各背“是什么 + 例子 / 用途”：

| 工具 | 是什么 | 例子 / 用途 |
|:--|:--|:--|
| Data dictionary | 关于数据的数据（metadata），描述数据库的结构 | 表名、字段名、数据类型、校验规则、主键 / 外键、关系、视图 |
| Logical schema | 数据库的概念设计：与具体 DBMS 无关的整体结构模型 | 用 E-R 图表示实体与关系；用来设计物理结构 |
| Developer interface | 让设计者建立数据库对象和界面的工具 | 建表、改表、设关系；做输入表单（加下拉框、按钮）；设计报表；加菜单 |
| Query processor | 接收查询条件、找出并返回结果的软件 | 处理并执行 SQL 查询，整理结果显示给用户 |

“另外三项”时，看清题干已经列了哪些（如已给属性名、表名、主外键），只写剩下的：关系、视图、数据类型、校验规则。

**得分表述**（引自对应 MS）
- 「Data about the data in the database // metadata」⟦9618_s24_11:6(b)⟧
- 「Platform/database independent overview of the database」⟦9618_s24_11:6(b)⟧
- 「Is used to design the physical structure」⟦9618_s24_11:6(b)⟧
- 「To allow the user to create a form for data input」⟦9618_w25_12:4(d)⟧
- 「software that processes and executes queries written in SQL」⟦9618_s23_12:2(a)⟧
- 「searches for the data that meets the entered criteria」⟦9618_w22_13:2(f)⟧

**易错与失分**
- 数据字典写成“存储数据库里的数据”：它存的是**关于数据的数据**，不是数据本身。
- 举的例子是数据值（“顾客名字 John”），而不是元数据（“字段名 CustomerName、类型 VARCHAR”）。
- 逻辑模式漏了“independent of any DBMS”这个关键限定。
- 题干已给的项目再写一遍（Identify three **other** items）。

#### 代表题精讲　⟦9618_s24_11:6(b)⟧

**在考什么**　Describe what is meant by the following DBMS features: data dictionary, logical schema. 4 分，每项最多 2。

**完整作答**
- 数据字典：关于数据库中数据的数据，即元数据；说明将要存储的数据有哪些特征，例如字段名、表名、校验规则、数据类型、主键与外键、关系。
- 逻辑模式：数据库的概念设计，是与平台 / 具体数据库软件无关的整体结构；用来设计物理结构，例如实体设计或 E-R 图。

**与 MS 对齐**　Data dictionary ←“Data about the data in the database // metadata”“Identifies the characteristics of the data that will be stored”“Appropriate example e.g. field names, table name, validation rules, data types, primary / foreign keys, relationships etc.”；Logical schema ←“Conceptual design”“Platform/database independent overview of the database”“Is used to design the physical structure”“Appropriate example e.g. Design of entities / E-R diagram / views”。每项写“定义 + 例子”即 2 分。

**英文作答句**　Data dictionary: data about the data in the database (metadata), for example the field names, table names, data types, validation rules and primary and foreign keys. Logical schema: a conceptual design of the database that is a platform-independent overview of its structure, such as an E-R diagram, and is used to design the physical structure.

**直观**　数据字典是图书馆的目录卡（记录每本书的编号、分类、位置，而不是书的内容）；逻辑模式是房子的设计图，还没决定用什么牌子的砖。

**下一道变式**　⟦9618_s25_13:6(d)(ii)⟧　（换成开发者界面：数据库设计者怎样使用它，3 分。）

<!-- auto:drills P1-DB-07 -->

### P1-DB-08　DBMS 数据安全　{#P1-DB-08}

<!-- auto:stats P1-DB-08 -->

**考法**　①除认证外，DBMS 还能用哪些方法提高数据库安全（描述，4 分）；②识别保护某张表免受未授权访问的两种方法并解释（方法 1 + 解释 1，各两组）；③描述 DBMS 怎样保证顾客数据安全（两种方法 + 描述）；④（2021 扩展）访问权限怎样保护数据。

**识别信号**　methods the DBMS can use to protect the data / improve the security of a database；access rights；views；backup；protect the data in the table … from unauthorised access。

**解题思路**　每种方法写“名称 + 怎样保护”：

| 方法 | 怎样保护 |
|:--|:--|
| Access rights（访问权限） | 不同用户 / 用户组对不同表有不同权限：只读、读写、完全访问、无权访问 |
| Views（视图） | 不同用户只看到数据库中自己需要的那部分（例如经理只看自己店的数据） |
| Backup / recovery | 定期自动复制数据库并存放在异地，数据丢失时可以恢复 |
| Encryption | 数据变成密文，没有解密密钥看不懂 |
| Record / table locking | 防止多人同时修改同一记录，更新不会丢失、数据不会被覆盖 |
| Authentication / passwords | 用户名与密码、生物识别、双因素认证，阻止未授权访问 |

题干已给“authentication”时不要再写它。MS 常注明只写名称不写描述最多 2 分。

**得分表述**（引自对应 MS）
- 「Max 2 if no descriptions」⟦9618_w23_12:2(b)⟧
- 「some users are given different access permissions to different tables」⟦9618_w23_12:2(b)⟧
- 「different users are able to see different parts of the database」⟦9618_w23_12:2(b)⟧
- 「so that the data can be recovered if lost」⟦9618_w23_12:2(b)⟧
- 「prevents simultaneous access to data」⟦9618_w23_12:2(b)⟧
- 「so that only those with correct permissions can read / edit customer’s data」⟦9618_w25_13:5(d)⟧

**易错与失分**
- 只列方法名：描述那一半分数丢掉。
- 写防火墙、杀毒软件：那是保护计算机系统的一般措施（SP-03），不是 DBMS 提供的功能。
- 视图与访问权限说成一回事：访问权限管“能不能读 / 写”，视图管“看得到哪部分”。
- 备份只写“make a copy”：要说定期、存在别处、丢失后能恢复。

#### 代表题精讲　⟦9618_w23_12:2(b)⟧

**在考什么**　Authentication is one method a DBMS can use to improve the security of a database. Describe other methods that a DBMS can use to improve the security of a database. 4 分；只写名称最多 2 分。

**完整作答**
1. 备份与恢复：定期自动复制数据库并存放在异地，这样数据丢失后可以恢复。
2. 访问权限：给不同用户设置对不同表的不同权限，如只读、读写、完全访问。
3. 视图：不同用户只能看到数据库的不同部分，只看到自己需要看的。
4. （也可写）加密：数据变成密文，没有解密密钥就看不懂；记录锁：防止同时访问，更新不会丢失。

**与 MS 对齐**　1 ←“Backup / recovery procedures”“… automatically takes copies of the database and store off site on a regular basis”“... so that the data can be recovered if lost”；2 ←“Use of access rights”“… some users are given different access permissions to different tables”“... read/write, read only, full access, etc.”；3 ←“Views”“… different users are able to see different parts of the database”。两种方法各写“名称 + 描述”即可满分，写三种更稳。

**英文作答句**　Backup procedures: the DBMS automatically takes copies of the database and stores them off site on a regular basis, so that the data can be recovered if lost. Access rights: some users are given different access permissions to different tables, such as read only or read/write. Views: different users are able to see different parts of the database, so they only see what they need to see.

**直观**　数据库像一栋办公楼：门禁卡决定你能进哪层（访问权限），玻璃墙决定你看得到哪些办公室（视图），每晚把档案复印一份锁进别处的保险库（备份）。

**下一道变式**　⟦9618_s25_12:5(c)(i)⟧　（只保护一张表 USER：两种方法，每种要解释它怎样保护**这张表**。）

<!-- auto:drills P1-DB-08 -->

### P1-DB-09　数据库中的数据完整性　{#P1-DB-09}

<!-- auto:stats P1-DB-09 -->

**考法**　①解释参照完整性是什么、怎样应用于给定数据库（通用点 + 本库举例）；②解释参照完整性为什么重要（3 分）；③解释 DBMS 怎样支持数据完整性；④给出 DBMS 支持完整性的两种方式；⑤说出数据完整性的含义并举数据库中的实现例子。

**识别信号**　referential integrity；important；enforce；cascade(ing) update / delete；Explain how a DBMS supports data integrity；State what is meant by data integrity and give one example of how this is implemented in a database。

**解题思路**
1. 参照完整性的核心句：**每个外键都必须有对应的主键**——不能引用不存在的记录。
2. 由此推出三件事：
   - 不能在“多”端表里插入一个引用不存在主键的记录（不能给不存在的公司加实习记录）；
   - **级联更新**：主键改了，所有引用它的外键一起改；
   - **级联删除**：主键记录删了，引用它的记录一起删，不留下“孤儿记录”。
3. 为什么重要：数据保持一致、最新；不会有无效的引用；查询结果准确、完整。
4. DBMS 支持完整性的其他方式：校验规则（validation）、强制参照完整性、级联更新 / 删除、规范化。
5. “应用于本数据库”要点名具体的表和键：CompanyID 是 PLACEMENT 的外键，依赖 COMPANY 的主键 CompanyID。

**得分表述**（引自对应 MS）
- 「Referential integrity ensures that every foreign key has a corresponding primary key」⟦9618_w25_11:2(d)⟧
- 「Referential integrity provides for cascading update / delete」⟦9618_w25_11:2(d)⟧
- 「Referential integrity is enforced」⟦9618_w24_13:4(e)⟧
- 「Methods of making sure the data is consistent」⟦9618_s23_11:2(a)(ii)⟧
- 「Ensuring the database is normalised」⟦9618_s25_12:5(c)(ii)⟧
- 「Makes sure any queries return accurate and complete results」⟦9618_w23_12:2(a)⟧

**易错与失分**
- 参照完整性写成“数据准确”：太泛，要写“外键必须对应存在的主键”。
- 级联删除方向写反：删除的是“1”端（主键所在）的记录，连带删掉“多”端（外键所在）的记录。
- “应用于本数据库”只写通用定义：举例那两分要点名表和字段。
- 把一般的完整性定义（SP-01）当成答案，没提 DBMS 怎样做。

#### 代表题精讲　⟦9618_w25_11:2(d)⟧

**在考什么**　WORKEXPERIENCE 数据库：STUDENT(**StudentID**, …)、PLACEMENT(**PlacementID**, *StudentID*, *CompanyID*, StartDate, EndDate, Complete)、COMPANY(**CompanyID**, …)。Explain what is meant by referential integrity, and how it applies to this database. 3 分（通用最多 2、举例最多 2）。

**完整作答**
- 通用：参照完整性确保每个外键都有对应的主键；它提供级联更新与级联删除。
- 本库：CompanyID 是 PLACEMENT 表的外键，依赖 COMPANY 表的主键 CompanyID（不能为不存在的公司添加实习记录）；如果从 STUDENT 表删除一条记录，PLACEMENT 表中所有相同 StudentID 的记录也会被删除。

**与 MS 对齐**　通用 ←“Referential integrity ensures that every foreign key has a corresponding primary key”“Referential integrity provides for cascading update / delete”；举例 ←“CompanyID is a foreign key in PLACEMENT table and is dependent on the primary key CompanyID in COMPANY table”“If a record is deleted from the STUDENT table, then all records with the same StudentID will be deleted from the PLACEMENT table”。通用 1–2 点 + 举例 1–2 点，凑满 3 分。

**英文作答句**　Referential integrity ensures that every foreign key has a corresponding primary key, and it provides for cascading update and delete. In this database, CompanyID is a foreign key in the PLACEMENT table and is dependent on the primary key CompanyID in the COMPANY table. If a record is deleted from the STUDENT table, all records with the same StudentID will be deleted from the PLACEMENT table.

**直观**　外键像通讯录里的“紧急联系人编号”：编号必须对应一个真实存在的人；那个人被删了，引用他的条目要么一起删，要么更新。

**下一道变式**　⟦9618_s23_12:2(b)⟧　（只问为什么重要，3 分：写一致、最新、外键对应主键、查询准确这类“好处”。）

<!-- auto:drills P1-DB-09 -->

### P1-DB-10　SQL DDL：建库、建表与改表　{#P1-DB-10}

<!-- auto:stats P1-DB-10 -->

**考法**　①按样本数据写 CREATE TABLE（含数据类型、NOT NULL、主键、外键，3–5 分，最常考）；②CREATE DATABASE（1 分）；③ALTER TABLE 加一个或两个字段（2–3 分）；④ALTER TABLE 补上外键链接（2 分）；⑤补全 CREATE TABLE 的空格；⑥找出 DDL 脚本里的错误并写出改正后的行。

**识别信号**　Write a Structured Query Language (SQL) script to define / create the table / database；Data Definition Language (DDL)；include an additional field；add one field；link the foreign key；Include constraints (restrictions)；identify the errors in the SQL script。

**解题思路**（CREATE TABLE 五步，每步对一个得分点）
1. 骨架：`CREATE TABLE 表名(` … `);`，括号要成对，所有语句都在括号里。
2. 每个字段一行：`字段名 数据类型,`，字段之间用逗号分隔（最后一行之后不要多逗号）。
3. **按样本数据选类型**：
   - 带前导零或含字母的编号（`0001`、`MK12`、`00956124`）→ `VARCHAR(n)` / `CHARACTER`，不能用 INTEGER（会丢掉前导零）；
   - 计数、整数分值 → `INTEGER`；带小数的价格、尺寸 → `REAL`；
   - 日期 → `DATE`，时刻 → `TIME`；是 / 否 → `BOOLEAN`。
4. 约束：主键字段加 `NOT NULL`；题目要求“constraints”时至少写一个（`NOT NULL`、`VARCHAR` 长度）。
5. 键：`PRIMARY KEY (字段)`；复合键 `PRIMARY KEY (字段1, 字段2)`；外键 `FOREIGN KEY (字段) REFERENCES 表(字段)`。

改表：加字段 `ALTER TABLE 表 ADD 字段 类型;`（两个字段用逗号接着写）；加外键 `ALTER TABLE 表 ADD FOREIGN KEY (字段) REFERENCES 表(字段);`。改错题常见错误：`DATA BASE` 应为 `DATABASE`；`NONULL` 应为 `NOT NULL`；行末漏逗号；`PRIMARY KEY` 后漏括号；`REFERENCES` 后漏表名；字段名与表定义不一致。

**得分表述**（引自对应 MS）
- 「Creating table PERFORMANCE with opening and closing brackets」⟦9618_s24_13:4(b)⟧
- 「Setting all four attributes with appropriate data types」⟦9618_s24_13:4(b)⟧
- 「Setting ShowID as foreign key referencing SHOW table」⟦9618_s24_13:4(b)⟧
- 「Create table with opening and closing brackets and commas separating the attributes」⟦9618_w25_13:5(b)⟧
- 「ADD FOREIGN KEY (ExamID) REFERENCES EXAM(ExamID)」⟦9618_s24_12:4(c)⟧
- 「Including the additional field with a suitable field name and suitable field type」⟦9618_w25_12:4(b)⟧

**易错与失分**
- 编号用 INTEGER：样本里 `0001` 这种前导零是在提示你用 VARCHAR / CHAR。
- 外键只写 `FOREIGN KEY (ShowID)`，漏了 `REFERENCES SHOW(ShowID)`。
- 加字段用了 `UPDATE` 或 `INSERT`：改结构是 DDL 的 `ALTER TABLE … ADD`；`UPDATE` 改的是数据（DB-13）。
- 复合键写成两个 PRIMARY KEY 语句：应写在一个括号里。
- 漏 `CREATE TABLE` 的右括号或分号，或括号外还写了字段。

#### 代表题精讲　⟦9618_s24_13:4(b)⟧

**在考什么**　剧院数据库：SHOW(**ShowID**, Title, Duration)、PERFORMANCE(**PerformanceID**, *ShowID*, ShowDate, StartTime)。样本数据：PerformanceID `0001`…，ShowID `MK12`、`OP3`，ShowDate `5/5/2025`，StartTime `13:00`。Write an SQL script to define the table PERFORMANCE. 4 分。

**完整作答**

```sql
CREATE TABLE PERFORMANCE(
  PerformanceID VARCHAR(4) NOT NULL,
  ShowID VARCHAR(4),
  ShowDate DATE,
  StartTime TIME,
  PRIMARY KEY (PerformanceID),
  FOREIGN KEY (ShowID) REFERENCES SHOW(ShowID)
);
```

类型理由：`0001` 有前导零、`MK12` 含字母 → VARCHAR；日期 → DATE；`13:00` 是时刻 → TIME。

**与 MS 对齐**　“Creating table PERFORMANCE with opening and closing brackets”；“Setting all four attributes with appropriate data types”；“Setting PerformanceID as primary key”；“Setting ShowID as foreign key referencing SHOW table”。四行要素各 1 分，与 MS 的 Example 一致。

**英文作答句**　（本题答案即上面的脚本。）

**直观**　CREATE TABLE 像设计一张空白表格：先写表头（字段名和每格能填什么类型），再规定哪一列是身份证号（主键）、哪一列要去别的表里查得到（外键）。

**下一道变式**　⟦9618_w24_11:2(b)(ii)⟧　（连接表 REPAIR_PART：复合主键 + 题目要求写约束。）

<!-- auto:drills P1-DB-10 -->

### P1-DB-11　SQL 单表查询　{#P1-DB-11}

<!-- auto:stats P1-DB-11 -->

**考法**　在一张表上写或补全查询：①带两三个条件的计数 / 求和 / 平均（COUNT、SUM、AVG），常要求“给结果一个合适的名字”（AS）；②按日期范围筛选；③用 OR 取两个值之一；④用 LIKE 找以某字符串开头的值；⑤GROUP BY 求每组的计数；⑥补全 SELECT … FROM … WHERE 的空格。

**识别信号**　Write an SQL script to return / find / count …；Complete the SQL script；the total number of …；the total amount；the average；appropriate (field) name；begins with；in the year 2023；for each …（但只用一张表）。

**解题思路**
1. 先确定**要返回什么**：一列值（`SELECT Name`）、个数（`COUNT(字段)`）、总和（`SUM(字段)`）、平均（`AVG(字段)`）。
2. 题目要“合适的名字”→ 紧跟 `AS 名字`（不加空格的一个词，如 `TotalPlacements`）。
3. `FROM` 那一张表（照抄表名）。
4. 把题干里**每个限定词**都变成一个条件，用 `AND` 连接：
   - 指定 ID、名字 → `CustomerID = "0034E"`（字符串加引号）；
   - “已完成 / 未付款” → `Complete = TRUE`、`Paid = FALSE`（布尔值不加引号）；
   - “在 2023 年” → `Date >= #01/01/2023# AND Date <= #31/12/2023#`；
   - “等级是 A 或 B” → `HorseLevel = "Intermediate" OR HorseLevel = "Beginner"`；
   - “以 HW 开头” → `CompanyID LIKE 'HW%'`。
5. “每个 … 的个数”→ `SELECT 分组字段, COUNT(…) … GROUP BY 分组字段`。
6. 结尾加分号。

**得分表述**（引自对应 MS）
- 「SELECT COUNT any appropriate field」⟦9618_w25_11:2(c)(ii)⟧
- 「AS and an appropriate name」⟦9618_w25_11:2(c)(ii)⟧
- 「Two AND clauses with the other two correct conditions」⟦9618_w25_11:2(c)(ii)⟧
- 「From the correct table and one correct condition」⟦9618_w24_11:2(b)(iii)⟧
- 「AND Date >= #01/01/2023# AND Date <= #31/12/2023#」⟦9618_w24_13:4(b)⟧
- 「WHERE CompanyID LIKE 'HW%'」⟦9618_w22_13:2(c)⟧

**易错与失分**
- “总数量”用了 COUNT：数**记录条数**用 COUNT，把某字段的值**加起来**用 SUM。
- 漏掉藏在题干里的条件：“completed placements”“invoices that have not been paid”各自是一个条件。
- 字符串不加引号，或布尔值加了引号（`"TRUE"`）。
- 日期范围只写一端，或写成 `Date = 2023`。
- 两个值之一写成 `HorseLevel = "Intermediate" OR "Beginner"`：OR 两边都要写完整的条件。

#### 代表题精讲　⟦9618_w25_11:2(c)(ii)⟧

**在考什么**　PLACEMENT(**PlacementID**, *StudentID*, *CompanyID*, StartDate, EndDate, Complete)。Write an SQL script to return the total number of placements completed by the student with ID LDEA01 at the company with ID NEAM. The total should be given an appropriate name. 4 分。

**完整作答**

```sql
SELECT COUNT(PlacementID) AS TotalPlacements
FROM PLACEMENT
WHERE StudentID = "LDEA01"
AND CompanyID = "NEAM"
AND Complete = TRUE;
```

三个条件分别来自题干的“student with ID LDEA01”“company with ID NEAM”“completed”。

**与 MS 对齐**　“SELECT COUNT any appropriate field”；“AS and an appropriate name”；“FROM and correct table and WHERE and one correct condition”；“Two AND clauses with the other two correct conditions”。最容易丢的是第四分：漏掉 `Complete = TRUE`。

**英文作答句**　（本题答案即上面的脚本。）

**直观**　写查询像在 Excel 里筛选：先选要统计哪一列、怎么统计（计数），再把每个筛选条件一个个勾上。

**下一道变式**　⟦9618_s24_11:6(c)(ii)⟧　（换成“每个玩家各完成了多少个活动”：需要 GROUP BY。）

<!-- auto:drills P1-DB-11 -->

### P1-DB-12　SQL 两表连接查询　{#P1-DB-12}

<!-- auto:stats P1-DB-12 -->

**考法**　要返回的字段或条件分属两张表：①按名字（在另一张表）统计个数或总和；②返回一张表的名字 + 另一张表的计数，按顾客 / 节目分组；③连接后加条件并排序（ORDER BY … DESC）；④补全 INNER JOIN … ON 的空格；⑤找出两表查询里的四个错误并改正。

**识别信号**　返回的字段（顾客名、节目名）与条件（未领取、评分 ≤ 5）或计数对象不在同一张表；INNER JOIN … ON；WHERE TABLE1.Key = TABLE2.Key；for each customer / each show；There are … errors in the script。

**解题思路**
1. **找要用的两张表**：返回字段在哪张表？条件字段在哪张表？两者不同就要连接。
2. **找连接键**：一张表的主键 = 另一张表的外键（`CUSTOMER.CustomerID = ORDER.CustomerID`）。两张表都有的字段名前**必须加表名**。
3. **两种连接写法，MS 都接受**：

```sql
-- Method 1: join in FROM ... ON
FROM CUSTOMER INNER JOIN ORDER
ON CUSTOMER.CustomerID = ORDER.CustomerID
WHERE ORDER.Collected = FALSE

-- Method 2: list both tables, join in WHERE
FROM CUSTOMER, ORDER
WHERE CUSTOMER.CustomerID = ORDER.CustomerID
AND ORDER.Collected = FALSE
```

4. 有“每个 …”就 `GROUP BY`（按 ID 或名字）；有“排序”就 `ORDER BY 字段 ASC / DESC`，写在最后。
5. 子句顺序固定：`SELECT → FROM → (ON) → WHERE → GROUP BY → ORDER BY`。
6. 改错题逐项查：聚合函数对不对（数人数用 COUNT 不用 SUM）；连接条件两边有没有表名；AND / OR 用对没有；字符串有没有引号；日期有没有 `#`。

**得分表述**（引自对应 MS）
- 「Joining tables ORDER and CUSTOMER」⟦9618_s25_13:6(c)⟧
- 「Grouping by customer ID or customer name」⟦9618_s25_13:6(c)⟧
- 「FROM clause with suitable join of tables (ON or WHERE)」⟦9618_s25_11:5(e)⟧
- 「The WHERE statement needs the table names before each field name」⟦9618_s23_12:2(c)(iii)⟧
- 「The OR should be AND」⟦9618_s23_12:2(c)(iii)⟧
- 「Beginner is missing the speech marks」⟦9618_s23_12:2(c)(iii)⟧

**易错与失分**
- 只 `FROM` 两张表却不写连接条件：会得到两表所有行的组合，连接那一分丢掉。
- 连接条件写成 `WHERE StudentID = StudentID`：没有表名，等于什么都没连。
- 用了计数却忘 GROUP BY：题目说“for each customer”“the number of times each show is scheduled”就要分组。
- 把连接条件和筛选条件用 OR 连：两者必须同时成立，用 AND。
- 排序方向：“descending”→ `DESC`；“ascending”可写 `ASC` 或不写。

#### 代表题精讲　⟦9618_s25_13:6(c)⟧

**在考什么**　CUSTOMER(**CustomerID**, CustomerName, Email)、ORDER(**OrderID**, *CustomerID*, Date, Collected)，Collected 为 TRUE 表示已领取。Write an SQL script to return the customer name for each customer that has orders they have not collected. Include the number of orders each customer has not collected with an appropriate title. 4 分。

**完整作答**

```sql
SELECT CUSTOMER.CustomerName, COUNT(ORDER.OrderID) AS NotCollected
FROM CUSTOMER INNER JOIN ORDER
ON CUSTOMER.CustomerID = ORDER.CustomerID
WHERE ORDER.Collected = FALSE
GROUP BY CUSTOMER.CustomerID;
```

为什么要连接：顾客名在 CUSTOMER，是否领取在 ORDER。为什么要分组：要的是**每个**顾客的未领取订单数。

**与 MS 对齐**　“Selection of customer name and counting any field from ORDER as an appropriate identifier”（SELECT 行 + AS）；“Joining tables ORDER and CUSTOMER”（INNER JOIN … ON，或 FROM 两表 + WHERE 连接）；“AND (or WHERE) clause: Collected = FALSE”；“Grouping by customer ID or customer name”。

**英文作答句**　（本题答案即上面的脚本。）

**直观**　两表连接像把“顾客名单”和“订单记录”按顾客编号对齐拼成一张大表，再从大表里筛出没领取的，最后按顾客数一数。

**下一道变式**　⟦9618_w25_13:5(c)⟧　（PRODUCT 与 COMPLAINT 连接，筛评分 ≤ 5，并按评分降序排列，5 分。）

<!-- auto:drills P1-DB-12 -->

### P1-DB-13　SQL 数据维护：INSERT、UPDATE、DELETE　{#P1-DB-13}

<!-- auto:stats P1-DB-13 -->

**考法**　①INSERT INTO … VALUES 添加一条新记录（3–4 分）；②UPDATE … SET … WHERE 修改某条记录的一个或多个字段（3 分）；③DELETE FROM … WHERE 删除满足条件的记录（2 分）；④补全 INSERT 语句。

**识别信号**　add a new record；enter the new product into the table；change the character’s data；amend the record；delete all … that have been completed。

**解题思路**
1. **INSERT**：`INSERT INTO 表 (字段1, 字段2, …) VALUES (值1, 值2, …);`
   - 字段列表可省略，但省略时值必须**按表定义的字段顺序**全部给出；
   - 字符串（含带前导零的编号 `"002323"`）加引号，数字不加，布尔写 TRUE / FALSE。
2. **UPDATE**：`UPDATE 表 SET 字段1 = 值1, 字段2 = 值2 WHERE 主键 = 值;`
   - 多个字段在一个 SET 里用逗号分开；**一定要有 WHERE**，否则整张表都被改。
3. **DELETE**：`DELETE FROM 表 WHERE 条件;`——删的是整条记录，不写字段名。
4. 与 DDL 区分：改**数据**用 INSERT / UPDATE / DELETE（DML）；改**结构**（加字段）用 ALTER TABLE（DDL，DB-10）。

**得分表述**（引自对应 MS）
- 「VALUES with opening and closing brackets」⟦9618_s25_13:6(b)⟧
- 「Inserting ProductID, ProductName and SupplierID correctly as strings including quotation marks into correct fields」⟦9618_s25_13:6(b)⟧
- 「Inserting quantity and cost correctly into correct fields」⟦9618_s25_13:6(b)⟧
- 「Values in correct order」⟦9618_w22_12:5(b)⟧
- 「DELETE FROM and correct table」⟦9618_w25_11:2(c)(i)⟧

**易错与失分**
- 数字加了引号（`"50"`），或编号 `002323` 没加引号（会变成数字 2323）。
- 省略字段列表时值的顺序与表定义不一致。
- UPDATE 漏 WHERE，或用两个 SET。
- 写成 `DELETE * FROM`，或 `DELETE 字段名 FROM`。
- 把“加一个新字段”写成 INSERT：那是 ALTER TABLE。

#### 代表题精讲　⟦9618_s25_13:6(b)⟧

**在考什么**　PRODUCT(**ProductID**, ProductName, QuantityInBox, Cost, *SupplierID*)。新产品：ID 002323，名称 ‘Blue ball point 2mm’，每盒 50 支，价格 $5.00，供应商 SFX223。Write an SQL script to enter the new product into the table PRODUCT. 4 分。

**完整作答**

```sql
INSERT INTO PRODUCT (ProductID, ProductName, QuantityInBox, Cost, SupplierID)
VALUES ("002323", "Blue ball point 2mm", 50, 5.00, "SFX223");
```

ProductID 有前导零、SupplierID 含字母，都是字符串，要加引号；50 和 5.00 是数字，不加引号；值的顺序与字段列表一一对应。

**与 MS 对齐**　“INSERT INTO PRODUCT”；“VALUES with opening and closing brackets”；“Inserting ProductID, ProductName and SupplierID correctly as strings including quotation marks into correct fields”；“Inserting quantity and cost correctly into correct fields”。MS 两个例子：带字段列表与不带字段列表都给分。

**英文作答句**　（本题答案即上面的脚本。）

**直观**　INSERT 是在表格末尾新添一行，每一格按表头顺序填；UPDATE 是找到那一行改几格；DELETE 是把整行划掉。

**下一道变式**　⟦9618_s25_12:5(d)(ii)⟧　（换成 UPDATE：一次改同一条记录的两个字段。）

<!-- auto:drills P1-DB-13 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| DB-01 vs DB-07 | 关系数据库相对文件方式的好处 → DB-01；DBMS 提供的工具（数据字典等）→ DB-07 | file-based approach 还是 DBMS feature |
| 主键 vs 候选键 vs 次键 | 被选中的唯一标识 / 能当主键的 / 没被选中或另外用于查找的 | chosen · could be · alternative |
| 外键所在表 vs 外键引用的表 | 外键所在的表是“多”端；被引用的表是“一”端，主键在那里 | the table each is found in 还是 references |
| DB-02 vs DB-03 | 识别或定义键 → DB-02；描述表间关系、连接表的作用 → DB-03 | key 还是 relationship |
| DB-03 vs DB-04 | 文字描述关系 → DB-03；画或补全 E-R 图 → DB-04 | describe 还是 complete the diagram |
| DB-05 vs DB-06 | 判断、描述范式 → DB-05；动手拆表、写新表定义 → DB-06 | which NF / describe 还是 normalise / create a design |
| 部分依赖 vs 非键依赖 | 依赖复合主键的一部分（违反 2NF）/ 依赖另一个非键字段（违反 3NF） | 有没有复合键 |
| DB-08 vs SP-03 | DBMS 的访问权限、视图、备份、记录锁 → DB-08；一般系统的防火墙、杀毒 → SP-03 | 题干有没有 DBMS |
| DB-09 vs DB-02 | 解释参照完整性为什么重要、怎样实现 → DB-09；术语表里给它下定义 → DB-02 | explain why / how 还是 definition |
| DB-09 vs SP-06 | DBMS 怎样保证完整性（参照完整性、级联）→ DB-09；某个字段怎样校验 → SP-06 | referential integrity 还是 validate the field |
| DB-10 vs DB-13 | 改结构（CREATE / ALTER TABLE）→ DB-10；改数据（INSERT / UPDATE / DELETE）→ DB-13 | add a field 还是 add a record |
| DB-11 vs DB-12 | 一张表就够 → DB-11；字段或条件分属两张表 → DB-12 | 返回字段与条件在不在同一张表 |
| COUNT vs SUM | 数记录条数 / 把某字段的值加起来 | number of 还是total quantity / amount |
| WHERE vs GROUP BY | 筛选哪些行 / 按什么分组统计 | only those … 还是 for each … |
