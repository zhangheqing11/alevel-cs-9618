## DB　数据库：核心概念 {#core-DB}

英文列带 ⟦⟧ 的是该题 MS 原文；标“非 MS 原句”的是标准定义，作答时以所答那题的 MS 为准。

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| File-based approach | 「There is program-data dependence with flat-files」⟦9618_s21_11:7(a)⟧ | 每个应用程序用自己的文件存数据，文件之间不链接 | 每个部门各记一本账 | P1-DB-01 |
| Data redundancy | 「Reduced data redundancy // less repeated data」⟦9618_s22_11:4(a)⟧ | 同一数据被重复存储在多处 | 每张单子都抄一遍顾客地址 | P1-DB-01 |
| Data inconsistency | 「because duplicated data might be stored differently」⟦9618_s21_11:7(a)⟧ | 重复存储的数据在不同地方不一致（一处改了别处没改） | 两本账对不上 | P1-DB-01 |
| Program-data independence | 「changes to the data do not require programs to be re-written」⟦9618_s22_11:4(a)⟧ | 数据结构由 DBMS 管理，改数据或结构不必重写程序 | 换了货架摆法，收银系统照常用 | P1-DB-01 |
| Relational database | Data is stored in linked tables, with each data item stored only once.（非 MS 原句） | 数据存放在多张通过主键—外键相互链接的表中 | 用编号互相引用的几本名册 | P1-DB-01 |
| Entity | 「An object about which data can be stored」⟦9618_w23_12:2(a)⟧ | 需要存储数据的现实对象（人、物、事件），表示为一张表 | 名册的主题：学生、课程 | P1-DB-02 |
| Table | Data about one entity organised in rows and columns.（非 MS 原句） | 关于一个实体的数据，按行（记录）和列（字段）组织 | 一张花名册 | P1-DB-02 |
| Record / tuple | 「a single row in a table」⟦9618_w22_11:4(c)(i)⟧ | 表中的一行，即实体的一个实例 | 名册上的一个人 | P1-DB-02 |
| Field | 「A column/attribute in a table」⟦9618_s21_12:1(a)⟧ | 表中的一列 | 名册的一栏：姓名、生日 | P1-DB-02 |
| Attribute | 「An item of data about an entity」⟦9618_w24_13:4(d)⟧ | 描述实体的一项数据，对应表中的一列 | 一个人的某项信息 | P1-DB-02 |
| Primary key | 「The unique attribute / combination of attributes used to identify the record / tuple」⟦9618_w23_12:2(a)⟧ | 唯一标识表中每条记录的属性或属性组合 | 学号 | P1-DB-02 |
| Candidate key | 「An attribute / field (or set of attributes / fields) that could be a primary key」⟦9618_w22_12:5(c)⟧ | 值唯一、可以当主键的属性或属性组合 | 身份证号也能当学号用 | P1-DB-02 |
| Secondary key | 「An additional/alternative key used as well as the primary key to locate specific data」⟦9618_s23_13:4(b)⟧ | 没被选为主键的候选键，或主键之外另用来查找数据的键 | 用手机号也能查到人 | P1-DB-02 |
| Foreign key | 「A field in one table that is linked to a primary key in another table」⟦9618_s23_13:4(b)⟧ | 一张表中引用另一张表主键的字段，用来实现关系 | 订单上写的顾客编号 | P1-DB-02、P1-DB-03 |
| Composite key | 「Neither key uniquely identifies each tuple by itself」⟦9618_s22_12:5(b)⟧ | 由两个或以上属性共同组成的主键，单个属性不唯一、合起来才唯一 | “学号 + 考试编号”才确定一个分数 | P1-DB-02 |
| One-to-many (1:M) | 「One staff member can have many devices」⟦9618_s22_13:6(a)⟧ | A 表一条记录对应 B 表多条记录，B 表每条只对应 A 表一条；A 的主键在 B 中作外键 | 一位顾客多张订单 | P1-DB-03、P1-DB-04 |
| One-to-one (1:1) | 「EMPLOYEE to LOGIN_DATA is 1 to 1」⟦9618_w24_12:6(b)(i)⟧ | 两表的记录一一对应 | 一人一个登录账号 | P1-DB-03 |
| Many-to-many (M:N) | 「To allow each character to have many items // to allow each item to be purchased for many characters」⟦9618_s25_12:5(a)⟧ | 两边都能对应多条；关系数据库不能直接实现，要用连接表 | 学生选课 | P1-DB-03 |
| Linking table | 「To remove the many-to-many relationship」⟦9618_s25_12:5(a)⟧ | 存放两张表的主键作外键的表，把 M:N 拆成两个 1:M | 选课登记表 | P1-DB-03、P1-DB-06 |
| E-R diagram | A diagram showing the entities and the degree of the relationships between them.（非 MS 原句） | 用方框表示实体、连线和鸦爪表示关系度数的图 | 表与表的关系地图 | P1-DB-04 |
| Normalisation | The process of organising data into tables so that each data item is stored once and depends only on the primary key.（非 MS 原句） | 把数据拆进合适的表，消除重复组、部分依赖与非键依赖 | 一件事只记一次、记在该在的地方 | P1-DB-05、P1-DB-06 |
| First Normal Form (1NF) | 「No repeating groups or repeating attributes」⟦9618_s22_13:6(c)⟧ | 没有重复的属性组，每个字段只存一个值 | 一格一个值 | P1-DB-05 |
| Atomic data | 「Ensure each field is atomic」⟦9618_w23_12:2(c)⟧ | 字段的值不可再分（姓与名分开存） | 不把一串课程挤进一格 | P1-DB-05、P1-DB-06 |
| Second Normal Form (2NF) | 「no partial key dependencies」⟦9618_w22_11:4(b)⟧ | 在 1NF 基础上，每个非键属性依赖整个主键 | 不能只看复合键的一半 | P1-DB-05 |
| Partial dependency | 「Each field is fully dependent on the corresponding primary key // no partial dependencies」⟦9618_s22_11:4(b)⟧ | 非键属性只依赖复合主键的一部分（违反 2NF） | 学生名只由学号决定，与考试无关 | P1-DB-05 |
| Third Normal Form (3NF) | 「All attributes must be fully dependent on the primary key and no other attributes」⟦9618_s22_13:6(c)⟧ | 在 2NF 基础上，非键属性只依赖主键，不依赖其他非键属性 | the key, the whole key, nothing but the key | P1-DB-05 |
| Non-key (transitive) dependency | 「no non-key dependencies // no transitive dependencies」⟦9618_w22_11:4(b)⟧ | 非键属性由另一个非键属性决定（违反 3NF） | 售价由品种决定，不由批次决定 | P1-DB-05、P1-DB-06 |
| DBMS | Software that creates, manages and controls access to a database.（非 MS 原句） | 建立、管理数据库并控制对它的访问的软件 | 数据库的管家 | P1-DB-07 |
| Data dictionary | 「Stores metadata about the database」⟦9618_w21_12:6(b)⟧ | 存放数据库元数据的地方：表名、字段名、类型、校验规则、键、关系 | 图书馆目录卡 | P1-DB-07 |
| Metadata | 「Data about the data in the database // data about the structure of the database // metadata for a database」⟦9618_s23_11:2(a)(i)⟧ | 关于数据的数据，描述数据的结构与特征 | 照片的拍摄时间、尺寸信息 | P1-DB-07 |
| Logical schema | 「independent of any particular DBMS」⟦9618_w22_12:5(d)(ii)⟧ | 与具体 DBMS 无关的数据库整体结构模型（如 E-R 图） | 房子的设计图 | P1-DB-07 |
| Data modelling | 「models the problem / situation」⟦9618_w22_12:5(d)(ii)⟧ | 用 E-R 图等方法为情境建立数据库结构模型 | 先画图再盖房 | P1-DB-07 |
| Developer interface | 「A software tool that allows the user to create items such as tables, forms and reports」⟦9618_s23_12:2(a)⟧ | 让设计者建表、设关系、做输入表单与报表的工具 | 搭积木的工具箱 | P1-DB-07 |
| Query processor | 「allows the user to enter criteria」⟦9618_w22_13:2(f)⟧ | 接收查询条件、执行 SQL、找出并整理结果的软件 | 图书馆的检索台 | P1-DB-07 |
| Access rights | 「some users are given different access permissions to different tables」⟦9618_w23_12:2(b)⟧ | 给不同用户设置对不同表的只读、读写或无权访问 | 门禁卡分楼层 | P1-DB-08 |
| Views | 「different users are able to see different parts of the database」⟦9618_w23_12:2(b)⟧ | 不同用户只看到数据库中自己需要的部分 | 各看各的报表 | P1-DB-08、P1-DB-01 |
| Backup | 「so that a second copy of the customer’s data is available in case of loss/damage」⟦9618_w25_13:5(d)⟧ | 定期复制数据库并存放在别处，丢失后可以恢复 | 每晚复印档案存进别处的保险库 | P1-DB-08 |
| Record locking | 「prevents simultaneous access to data」⟦9618_w23_12:2(b)⟧ | 一个用户修改某记录时锁住它，防止同时修改导致更新丢失 | 试衣间有人时挂“使用中” | P1-DB-08、P1-DB-01 |
| Referential integrity | 「Referential integrity ensures that every foreign key has a corresponding primary key」⟦9618_w25_11:2(d)⟧ | 每个外键都必须对应一个存在的主键，不能引用不存在的记录 | 订单上的顾客编号必须查得到这位顾客 | P1-DB-09、P1-DB-02 |
| Cascading update / delete | 「If data in one table is deleted/edited all tables are updated // cascading update/delete」⟦9618_s23_11:2(a)(ii)⟧ | 主键被修改或删除时，引用它的外键记录一起修改或删除 | 搬家后所有登记的地址一起改 | P1-DB-09 |
| Data integrity (in a database) | 「Methods of making sure the data is consistent」⟦9618_s23_11:2(a)(ii)⟧ | 用参照完整性、校验规则、规范化等保证数据一致、准确 | 账目处处对得上 | P1-DB-09 |
| DDL | Data Definition Language: SQL statements that create and modify the structure of a database.（非 MS 原句） | 定义数据库结构的 SQL：CREATE DATABASE、CREATE TABLE、ALTER TABLE | 设计空白表格 | P1-DB-10 |
| CREATE TABLE | 「CREATE TABLE start and end bracket」⟦9618_s23_11:2(b)(iii)⟧ | 建表语句：括号内逐行写“字段 类型”，再写主键、外键 | 画表头 | P1-DB-10 |
| ALTER TABLE | 「ALTER TABLE statement」⟦9618_w25_12:4(b)⟧ | 修改已有表的结构：加字段、加外键 | 给表格加一栏 | P1-DB-10 |
| Constraint | 「At least 1 appropriate constraint」⟦9618_w24_11:2(b)(ii)⟧ | 对字段可输入数据的限制，如 NOT NULL、VARCHAR 长度、主键 | 这一栏必须填 | P1-DB-10 |
| DML | Data Manipulation Language: SQL statements that query and change the data in a database.（非 MS 原句） | 查询与修改数据的 SQL：SELECT、INSERT、UPDATE、DELETE | 往表格里填、改、查 | P1-DB-11 至 P1-DB-13 |
| Aggregate function | 「Select SUM of AmountDue」⟦9618_w24_11:2(b)(iii)⟧ | 对多行计算出一个值：COUNT（条数）、SUM（总和）、AVG（平均） | 统计一栏 | P1-DB-11、P1-DB-12 |
| AS (alias) | 「AS and an appropriate name」⟦9618_w25_11:2(c)(ii)⟧ | 给计算出的结果列起名字 | 给统计结果加标题 | P1-DB-11、P1-DB-12 |
| LIKE | 「WHERE CompanyID LIKE 'HW%'」⟦9618_w22_13:2(c)⟧ | 模糊匹配，`%`（或 `*`）代表任意字符 | 以 HW 开头的都算 | P1-DB-11 |
| Join | 「FROM clause with suitable join of tables (ON or WHERE)」⟦9618_s25_11:5(e)⟧ | 让两张表中主键与外键相等，把对应的行拼在一起 | 按编号把两张名单对齐 | P1-DB-12 |
| GROUP BY | 「Grouping by the title and selecting the title」⟦9618_s24_13:4(c)⟧ | 按某字段分组，对每组分别做聚合 | 按班级各数人数 | P1-DB-11、P1-DB-12 |
| ORDER BY | 「Correct ORDER BY clause」⟦9618_w25_13:5(c)⟧ | 按某字段升序（ASC）或降序（DESC）排列结果 | 排名次 | P1-DB-11、P1-DB-12 |
| INSERT INTO | 「INSERT INTO TREE」⟦9618_w22_12:5(b)⟧ | 向表中添加一条新记录 | 在表格末尾加一行 | P1-DB-13 |
| UPDATE … SET | 「SET level and money」⟦9618_s25_12:5(d)(ii)⟧ | 修改满足 WHERE 条件的记录中的字段值 | 改某一行的几格 | P1-DB-13 |
| DELETE FROM | 「DELETE FROM and correct table」⟦9618_w25_11:2(c)(i)⟧ | 删除满足条件的整条记录 | 划掉整行 | P1-DB-13 |
