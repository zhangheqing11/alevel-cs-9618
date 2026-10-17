## SP　安全、隐私与数据完整性 {#ch-SP}

<!-- auto:chapter-stats -->

### 核心思想

这一章回答一个问题：**数据怎样才不会丢、不会被偷看、不会出错？** 三个词各管一件事，先分清（SP-01）：

| 目标 | 管什么 | 对应措施 |
|:--|:--|:--|
| Security 安全 | 数据和系统不丢失、不被破坏、不被篡改，丢了能恢复 | 防火墙、杀毒、密码、备份、加密（SP-03 至 SP-05） |
| Privacy 隐私 | 只有被授权的人才能看到、拿到数据 | 用户账户与密码、访问权限、加密 |
| Integrity 完整性 | 数据准确、完整、一致、最新 | 校验 validation（SP-06）、验证 verification（SP-07） |

章内顺序是一条“攻—防—查”的链：

1. **攻**：有哪些威胁——病毒、间谍软件、黑客、网络钓鱼、域名欺骗（SP-02）。
2. **防**：一般措施（防火墙、杀毒、反间谍、密码、生物识别、访问权限、代理服务器）怎样工作（SP-03）；传输中被截获怎么办——加密（SP-04）；怎样证明“确实是他发的、途中没被改过”——数字签名（SP-05）。
3. **查**：录入时数据合不合理——校验（SP-06）；录入或传输后和原来的一不一样——验证（SP-07）；两者的区别、合用与局限（SP-08）。

本章几乎全是文字题，MS 的结构非常固定：**“名称 1 分 + 怎样起作用 1–2 分”**，或“威胁—描述—防范”三格一组。名称写对只拿一份分，“怎样起作用”一定要写出机制（比较什么、和什么比、比完做什么）。

### 题型树
<!-- auto:type-tree -->

### P1-SP-01　安全、隐私与完整性的概念　{#P1-SP-01}

<!-- auto:stats P1-SP-01 -->

**考法**　①说出 privacy / integrity of data 的含义（各 1 分）；②说出 security 与 privacy、security 与 integrity 的区别；③为什么数据要保持安全；④为什么数据**和**计算机系统都要防止未授权访问（两边各 1 分）；⑤连线：每个措施是保护安全还是保护完整性（2021 扩展题）。

**识别信号**　security of data；privacy of data；integrity of data；the difference between；State why data needs to be kept secure；keep both its data and its computer system secure。

**解题思路**
1. 背死三句话：security = 防止丢失、损坏、被改（并能恢复）；privacy = 只有授权的人能访问；integrity = 准确、完整、一致、最新。
2. 区别题成对写：“Security protects …, whereas privacy …”。
3. “数据和系统都要保护”分两边：数据——防止被人修改、删除、拿走；系统——防止有人装恶意软件、破坏系统。
4. 连线题的分法：防火墙、访问权限、密码 → 安全；两次录入（double entry）、存在检查（presence check）→ 完整性。凡是“查数据对不对”的都是完整性。

**得分表述**（引自对应 MS）
- 「Ensuring data can only be accessed by / disclosed to authorised persons」⟦9618_w23_12:5(a)⟧
- 「Ensuring the accuracy / completeness / consistency of data」⟦9618_w23_12:5(b)⟧
- 「Security prevents against loss while privacy prevents unauthorised access」⟦9618_s22_11:3(a)⟧
- 「integrity is ensuring the consistency / accuracy of the data」⟦9618_w21_11:2(a)⟧
- 「To stop the data being lost / corrupted / amended」⟦9618_s22_13:5(a)(i)⟧
- 「Data needs protecting from someone amending / deleting or taking it」⟦9618_s22_12:4(a)⟧

**易错与失分**
- 把 privacy 写成 “keeping data safe”：那是 security。privacy 的关键词是 **authorised / unauthorised persons**。
- 把 integrity 写成 “data is protected”：integrity 说的是数据**本身对不对**（accurate、consistent、up to date），与有没有人偷看无关。
- “数据和系统”两问写成一个意思：系统那一边要写“装恶意软件 / 破坏系统”，不是再写一遍“数据被偷”。

#### 代表题精讲　⟦9618_s22_12:4(a)⟧

**在考什么**　学校存有师生个人数据。Explain why the school needs to keep both its data and its computer system secure from unauthorised access. 2 分，数据 1 分、系统 1 分。

**完整作答**
- 数据：要防止有人修改、删除或拿走这些个人数据。
- 计算机系统：要防止有人（例如）安装恶意软件或破坏系统。

**与 MS 对齐**　Data ←“Data needs protecting from someone amending / deleting or taking it”；Computer System ←“Computer system need protecting to stop people for example, installing malware or damaging the system”。两边各写一句即满分，两句不能是同一个意思。

**英文作答句**　Data: the personal data needs protecting from someone amending, deleting or taking it. Computer system: the system needs protecting to stop people installing malware on it or damaging the system.

**直观**　数据是保险柜里的文件，系统是保险柜本身：文件怕被拿走或涂改，柜子怕被人撬开、装上窃听器。

**下一道变式**　⟦9618_s22_11:3(a)⟧　（换成区别题：security 与 privacy 的区别，1 分，一句话里两边都要有。）

<!-- auto:drills P1-SP-01 -->

### P1-SP-02　安全威胁　{#P1-SP-02}

<!-- auto:stats P1-SP-02 -->

**考法**　①“威胁—描述—防范”表格（每组 3 分，常两组共 6 分）；②描述指定威胁（phishing email、spyware、virus、pharming，各 2 分）；③两种威胁的异同（pharming vs phishing、spyware vs virus）；④网络与互联网带来的威胁举名。

**识别信号**　threat(s) to the data / to computer and data security；malware；virus；spyware；hacker / hacking；phishing；pharming；Identify and describe … Give a different prevention method for each threat。

**解题思路**
1. 五种威胁各背“是什么 + 干什么”：

| 威胁 | 是什么 | 干什么（危害） | 防范 |
|:--|:--|:--|:--|
| Virus | 会自我复制的恶意程序 | 删除、损坏、改动文件，占满存储 | Anti-virus / anti-malware，防火墙 |
| Spyware | 用户不知情时下载安装的恶意软件 | 偷偷记录键盘与操作，把记录发给第三方 | Anti-spyware，防火墙，屏幕虚拟键盘 |
| Hacker / hacking | 未经授权访问系统的人 / 行为 | 删除、损坏、窃取数据 | 防火墙，强密码，认证，访问权限 |
| Phishing | 冒充正规机构的电子邮件 | 诱导用户点链接、交出个人信息（银行账号） | 垃圾邮件过滤，不打开陌生来源邮件 |
| Pharming | 装在电脑上的恶意代码 | 把用户**自动重定向**到假网站，骗取个人信息 | Anti-malware，不打开陌生链接与附件 |

2. 表格题三格必须**配套**：防范方法要能防住你写的那个威胁；“每个方法不同”时两组不要都写 firewall。
3. 描述题写两截：先“是什么”，再用 “…” 接“它会做什么”。
4. Pharming 与 phishing：相同——都冒充正规机构、都想骗取个人或财务信息、都用到假网站；不同——pharming 是恶意代码自动重定向，phishing 靠邮件诱导用户自己行动。

**得分表述**（引自对应 MS）
- 「Malicious program/software that replicates/copies itself and deletes/alters files/data stored on a computer」⟦9618_w25_11:8(a)⟧
- 「Malware downloaded without the user’s knowledge」⟦9618_w23_12:5(c)⟧
- 「which secretly records the user’s actions / keystrokes on the computer」⟦9618_w23_12:5(c)⟧
- 「The email pretends to be from an official body」⟦9618_w23_12:5(c)⟧
- 「Malicious code/software installed on a computer which redirects user to a fake website to obtain personal data」⟦9618_w25_11:8(a)⟧
- 「Pharming is automatic. Phishing requires user action.」⟦9618_w23_13:8(b)⟧

**易错与失分**
- 病毒只写 “cause harm / damages the computer”：MS 会注明 cause harm is NE，要写“复制自己 + 删除/损坏数据”。
- 间谍软件漏了“发给第三方”：只说“记录按键”只拿一半。
- 把 phishing 写成“黑客入侵”：phishing 的载体是**邮件**，靠的是骗用户自己交出信息。
- 防范方法和威胁不配套（用 anti-virus 防 phishing），或两组写同一个方法。
- 防火墙、杀毒怎样**工作**属于 SP-03；本型的防范格只要写出名称（必要时加半句）。

#### 代表题精讲　⟦9618_s22_11:3(b)⟧

**在考什么**　老师在联网的笔记本上写试卷。Identify and describe two threats to the data. Identify one security measure to protect against each threat. Each security measure must be different. 6 分 = 2 ×（威胁 1 + 描述 1 + 措施 1）。

**完整作答**
- 威胁 1：Malware（恶意软件，如病毒）。描述：会自我复制的恶意软件，可以删除或损坏试卷文件。措施：安装并运行防恶意软件（anti-malware）。
- 威胁 2：Hacker（未授权访问）。描述：非法访问电脑，以删除、损坏或窃取试卷。措施：使用防火墙（或强密码）。

**与 MS 对齐**　MS 每组三点：“Malware / Malicious software that replicates and can delete/damage the examination papers / Install and run anti-malware”；“Hacker/unauthorised access / Illegal access in order to delete/damage the examination papers / Use a firewall // strong passwords”。也可以写 spyware（“Software installed on the computer without the teacher’s knowledge which records keystrokes and sends the data … to a third party”，措施 anti-spyware 或虚拟键盘）。两组措施不同才拿满 6 分。

**英文作答句**　Threat 1: malware. Malicious software that replicates itself and can delete or damage the examination papers. Measure: install and run anti-malware software. Threat 2: a hacker. A person who gains illegal access to the computer in order to delete, damage or steal the examination papers. Measure: use a firewall.

**直观**　威胁表就像“病名—症状—药”：药必须对症，两种病不能开同一种药。

**下一道变式**　⟦9618_w23_12:5(c)⟧　（不写防范，只描述 phishing email 与 spyware，各 2 分；看清两者各自的“…”展开点。）

<!-- auto:drills P1-SP-02 -->

### P1-SP-03　安全措施　{#P1-SP-03}

<!-- auto:stats P1-SP-03 -->

**考法**　①描述/解释防火墙怎样保护数据（3 分，最常考）；②给出“另一种”措施并描述怎样工作（防火墙、代理服务器）；③说出给定措施（firewall、encryption、passwords）各怎样保护系统；④两种防范网络威胁的软件（anti-virus、anti-spyware、firewall）；⑤怎样限制恶意软件的风险（3 分，“措施 + …so that”）；⑥给出保护存储数据的其他方法（列名）。

**识别信号**　security measure；protect … from hackers / unauthorised access；firewall；proxy server；anti-virus / anti-spyware / anti-malware；passwords；biometric；access rights；Explain how the data security risks of malware can be restricted。

**解题思路**
1. **防火墙**三步：监控所有进出的数据（流量/数据包）→ 与设定的规则比较（允许名单/拒绝名单、IP 地址、端口）→ 不符合规则的拦下，符合的放行。还可以加：阻止内部未授权软件向外发送数据（例如间谍软件外传）。
2. **代理服务器**：拦截请求 → 用自己的 IP 地址转发 → 设备不直接访问服务器 → 返回的数据先经它过滤再交给用户。
3. **杀毒 / 反间谍**：扫描文件与下载 → 与已知病毒/间谍软件的数据库比对（数据库要定期更新）→ 发现后隔离或删除。
4. **密码 / 生物识别 / 双因素认证**：只有凭证正确的用户才能访问。**访问权限**：不同用户只读、读写或无权访问。
5. “限制恶意软件风险”每点写“做法 + …so that”：只从可信来源下载（不容易带恶意软件）；定期备份（中毒后可恢复）；安装并运行防恶意软件、定期更新特征库；防火墙封掉不用的端口；不给普通用户管理员权限；禁用移动存储设备。

**得分表述**（引自对应 MS）
- 「Compares all incoming and outgoing transmissions」⟦9618_s24_11:5(c)(i)⟧
- 「against set criteria/whitelist/blacklist」⟦9618_s24_11:5(c)(i)⟧
- 「Blocks all transmissions that do not meet rules」⟦9618_s24_11:5(c)(i)⟧
- 「Forwards the request using its own IP address」⟦9618_s24_12:3(a)(i)⟧
- 「Ensures only users with the correct password can access the resources」⟦9618_w23_13:3(a)(iii)⟧
- 「Deny administrator privileges to everyday users」⟦9618_w23_13:8(c)⟧

**易错与失分**
- 防火墙只写 “blocks hackers / viruses”：要写**比较规则**这个机制。防火墙不扫描病毒，“scans for viruses”是杀毒软件。
- “另一种措施”又写题干已给的 authentication / password。
- 把加密写成“防止数据被截获”：加密不能阻止截获，只是截获了也读不懂（SP-04）。
- “限制恶意软件”只列措施名而不写 …so that 的理由：MS 的展开点要求写出为什么有用。
- 题干问的是 DBMS 怎样保护数据库（访问权限、视图、备份）→ 那是 DB-08。

#### 代表题精讲　⟦9618_s24_11:5(c)(i)⟧

**在考什么**　银行网络有防火墙。Explain how a firewall can help protect the customers’ data. 3 分，写防火墙的工作机制。

**完整作答**
1. 防火墙比较所有进出网络的数据传输；
2. 依据设定的规则（允许名单/拒绝名单）；
3. 拦截所有不符合规则的传输，例如阻止数据从特定端口进入；
4. 还能阻止内部未经授权或未知的软件向外发送数据（客户数据不会被偷偷传出）。

**与 MS 对齐**　1 ←“Compares all incoming and outgoing transmissions”；2 ←“... against set criteria/whitelist/blacklist”；3 ←“Blocks all transmissions that do not meet rules”“Blocks data entering from specific ports”；4 ←“Blocks unauthorised/unknown internal software transmitting data”。写满 3 点即满分。

**英文作答句**　The firewall compares all incoming and outgoing transmissions against a set of criteria, such as a whitelist or blacklist of IP addresses. It blocks all transmissions that do not meet the rules, for example data entering from specific ports, and it blocks unknown internal software from transmitting customer data out of the network.

**直观**　防火墙是小区门卫拿着一张名单：每个进出的人都要对名单，不在名单上的拦下，连从里面往外偷运东西的也拦。

**下一道变式**　⟦9618_w23_13:8(c)⟧　（换成“怎样限制恶意软件的风险”：措施不止一种，每个措施要配一个 …so that。）

<!-- auto:drills P1-SP-03 -->

### P1-SP-04　加密　{#P1-SP-04}

<!-- auto:stats P1-SP-04 -->

**考法**　①识别保护传输中数据的方法并描述（方法 1 分 + 描述 2 分）；②解释加密怎样保护传输中的数据（2 分）；③描述加密是什么、为什么用（2 分）；④在表格或连线里作为措施之一出现（副题型）。

**识别信号**　encryption；cipher text；key；protect the data when it is being transmitted；intercepting the data whilst it is being transferred；during email transfer。

**解题思路**
1. 题目问“传输中”“被截获”“发邮件时”保护数据，而 MS 只接受加密 → 方法就写 **Encryption**。
2. 描述三连：①用算法和密钥把数据编码/打乱成**密文**（cipher text）；②即使被截获也读不懂；③没有解密密钥就无法还原。
3. 用途一句话：传输的数据可能被截获，加密让截获者拿到的东西没有用。

**得分表述**（引自对应 MS）
- 「Data is encoded/scrambled using a key to create cipher text」⟦9618_s25_11:7(a)⟧
- 「if intercepted it cannot be understood」⟦9618_s25_11:7(a)⟧
- 「without being decrypted using a key」⟦9618_s25_11:7(a)⟧
- 「Algorithm/key is required to decode the data」⟦9618_s24_13:7(f)(ii)⟧
- 「File contents are converted to cipher text」⟦9618_w24_12:4(c)⟧
- 「Used so that it cannot be understood if intercepted without the decryption key」⟦9618_s22_12:4(c)⟧

**易错与失分**
- 写“加密防止数据被截获 / 被访问”：错。加密**不阻止**截获，阻止的是**看懂**。
- 漏了“密钥”：没有 key / decryption key 的描述常常少一分。
- 把加密和数字签名混在一起：签名证明来源与未被篡改（SP-05），加密保证别人看不懂。
- “传输中”的保护写成防火墙、杀毒：那是保护电脑上的数据，不是保护在路上的数据。

#### 代表题精讲　⟦9618_s25_11:7(a)⟧

**在考什么**　银行职员要通过互联网传输机密数据。Identify and describe one method of restricting the risks posed by an unauthorised person intercepting the data whilst it is being transferred. 3 分 = 方法 1 + 描述 2。

**完整作答**　方法：加密。描述：用密钥把数据编码（打乱）成密文；如果被截获，截获者看不懂；没有用密钥解密就无法理解。

**与 MS 对齐**　方法 ←“Encryption”；描述 ←“Data is encoded/scrambled using a key to create cipher text”“if intercepted it cannot be understood”“without being decrypted using a key”，任两点得 2 分。

**英文作答句**　Method: encryption. The data is encoded or scrambled using a key to create cipher text, so if it is intercepted it cannot be understood without being decrypted using the key.

**直观**　加密是把信写成只有你和收信人懂的暗号：信照样可能被人半路拆开，但拆开的人只看到一堆乱码。

**下一道变式**　⟦9618_w24_12:4(c)⟧　（情境换成邮件发送程序代码：先自己说出方法，再写两点解释。）

<!-- auto:drills P1-SP-04 -->

### P1-SP-05　数字签名　{#P1-SP-05}

<!-- auto:stats P1-SP-05 -->

**考法**　①解释数字签名怎样认证文档 / 保证数据在传输中未被改动（5 分，按步骤给分）；②解释数字签名怎样保证邮件真实（2 分，私钥/公钥）；③下载程序时应附带什么来证明程序真实（1 分：digital signature）。

**识别信号**　digital signature；authenticate a digital document；the email is authentic；the data has not been changed during transmission；hash；digest；private key；public key。

**解题思路**（发送方 4 步 + 接收方 4 步，按顺序写）
1. 发送方用哈希算法处理文档，得到**摘要**（digest）。
2. 发送方用自己的**私钥**加密摘要，得到数字签名。
3. 文档和签名一起发给接收方。
4. 接收方用发送方的**公钥**解密签名，还原出摘要。
5. 接收方用**同一个**哈希算法处理收到的文档，得到第二个摘要。
6. 比较两个摘要：相同 → 文档未被改动，且确实来自持有私钥的发送方。

为什么能证明：只有发送方有私钥，所以能用他的公钥解开的签名一定是他做的（来源真实）；文档改了一个字，重新算出的摘要就不同（内容未改）。

**得分表述**（引自对应 MS）
- 「The sender hashes the document / message」⟦9618_s25_11:7(b)⟧
- 「The sender encrypts the digest to create the digital signature」⟦9618_s25_11:7(b)⟧
- 「The receiver decrypts the signature to reproduce the digest」⟦9618_s25_11:7(b)⟧
- 「The receiver uses the same hashing algorithm on the document received to produce a second digest」⟦9618_s25_11:7(b)⟧
- 「Digest encrypted with sender’s private key」⟦9618_w22_12:6(a)(i)⟧
- 「the (digital) signature can only be decrypted with matching sender’s public key」⟦9618_w22_12:6(a)(i)⟧

**易错与失分**
- 把整个文档加密当成签名：签名加密的是**摘要**，文档本身可以是明文。
- 私钥、公钥用反：签名用**发送方私钥**加密，接收方用**发送方公钥**解密。
- 接收方漏了“用同一个哈希算法重新算摘要”这一步，或漏了最后的“比较”：5 分题这两步各值一分。
- 写成“加密让别人看不懂”：那是 SP-04 的答案，不能证明真实性。

#### 代表题精讲　⟦9618_s25_11:7(b)⟧

**在考什么**　银行职员收到带数字签名的机密数据。Explain how a digital signature can make sure the data has not been changed during transmission. 5 分，8 个步骤点任 5 个。

**完整作答**
1. 发送方用哈希算法处理文档，产生摘要；
2. 发送方加密摘要，生成数字签名；
3. 文档和签名一起发给银行职员；
4. 职员解密签名，还原出原摘要；
5. 职员对收到的文档用同一个哈希算法，得到第二个摘要；
6. 比较两个摘要；
7. 如果相同，说明文档在传输中没有被改动。

**与 MS 对齐**　1 ←“The sender hashes the document / message”+“to produce a digest”；2 ←“The sender encrypts the digest to create the digital signature”；3 ←“The message and the signature are sent to the banker / receiver”；4 ←“The receiver decrypts the signature to reproduce the digest”；5 ←“The receiver uses the same hashing algorithm on the document received to produce a second digest”；6 ←“The receiver compares this digest with the one from the digital signature”；7 ←“If both of the receiver’s digests are the same the document has not changed”。共 8 点，写全 7 句稳拿 5 分。

**英文作答句**　The sender hashes the document to produce a digest, then encrypts the digest with the sender’s private key to create the digital signature. The message and the signature are sent to the receiver. The receiver decrypts the signature with the sender’s public key to reproduce the digest, and uses the same hashing algorithm on the document received to produce a second digest. The receiver compares the two digests: if they are the same, the document has not been changed.

**直观**　摘要像文件的“指纹”，签名是用只有你有的印章盖在指纹上的封条。收件人用公开的验章工具看封条里的指纹，再自己给文件按一次指纹，两枚指纹一样才说明文件没被换过。

**下一道变式**　⟦9618_w22_12:6(a)(i)⟧　（只有 2 分、问“真实性”：重点是私钥加密、公钥解密这两件事。）

<!-- auto:drills P1-SP-05 -->

### P1-SP-06　数据校验　{#P1-SP-06}

<!-- auto:stats P1-SP-06 -->

**考法**　①对给定字段（出生日期、车牌号、骑手等级）描述两种校验方法（每种“名称 + 在本字段上怎么用”）；②给定校验名称，各举一例怎样用在该字段；③从伪代码算法判断是哪种校验；④描述校验怎样保护数据完整性；⑤填空：根据描述写出校验名称。

**识别信号**　validation；validate；validation check / rule；range / format / length / presence / existence (look-up) / type / limit check；check digit；“Describe two other ways … can be validated”。

**解题思路**
1. 校验 = 由计算机按规则检查数据**是否合理、在允许范围内**；它不检查数据是不是“真的”。
2. 各种校验与在字段上的写法：

| 校验 | 检查什么 | 写法示例（出生日期 / 编号） |
|:--|:--|:--|
| Range check | 在上下两个界限之间（两端都要有） | DoB 在 01/01/1900 与今天之间；月份 1–12 |
| Limit check | 只检查一端 | DoB 必须早于今天 |
| Presence check | 字段不能留空 | DoB 必须填写 |
| Length check | 字符个数正确 | 车牌号必须正好 6 个字符 |
| Format check | 字符的组合模式正确 | 1 个字母 + 3 个数字 + 2 个字母 |
| Type check | 数据类型正确 | 分数必须是整数；字段为 DATE |
| Existence / look-up check | 值在允许列表中 | 等级只能是 Beginner、Intermediate、Advanced |
| Check digit | 由其余数字算出的末位与输入的末位一致 | 条码、ISBN |

3. 每种校验都要**落到题目的字段上**：写出具体界限、长度、格式或列表，不要只写定义。
4. 伪代码识别：`IF x < 1 OR x > 26` → 范围；`IF x <> 'R' AND x <> 'G' AND x <> 'B'` → 存在（列表）；逐字符找某个符号（如 `@`）→ 格式；`IF x = ""` → 存在性（presence）；`LENGTH(x) <> 6` → 长度。
5. “题干已给 presence check，再给两种”：别再写 presence。

**得分表述**（引自对应 MS）
- 「Presence check to make sure that the (rider level) is entered」⟦9618_s23_12:2(c)(i)⟧
- 「Look-up / Existence check to make sure the rider level is only Beginner, Intermediate or Advanced」⟦9618_s23_12:2(c)(i)⟧
- 「Length check: the registration number must be 6 characters long」⟦9618_s23_13:4(d)(i)⟧
- 「Make sure the date of birth has been entered」⟦9618_s22_13:5(b)(ii)⟧
- 「protects the data by ensuring that the data is reasonable / sensible and within specified bounds」⟦9618_w23_13:8(a)⟧

**易错与失分**
- 只写校验名称，不写在本字段上怎么用：大多数题“名称 + 用法”才给分。
- Range check 只写一端（“must be before today”）：两端都写才是 range，只有一端的是 limit check。
- 格式与长度混淆：长度只管“几个字符”，格式管“什么字符在什么位置”。
- 把 double entry、visual check 写成校验：它们是**验证**（SP-07）。
- 长度检查的数字要和你说的格式一致：dd/mm/yyyy 是 10 个字符，ddmmyyyy 是 8 个。

#### 代表题精讲　⟦9618_s22_13:5(b)(ii)⟧

**在考什么**　员工资料从纸质录入电脑。Give one example of how each of the following data validation rules can be used to validate the date of birth: range check, presence check, length check. 3 分，每种一个具体用法。

**完整作答**
- Range check：出生日期必须在两个日期之间，例如 1900 年与今天之间（也可写月份在 1 至 12 之间、日在 1 至该月最后一天之间）。
- Presence check：确保出生日期已经输入，不能留空。
- Length check：日期必须是 8 个字符（如 ddmmyyyy）。

**与 MS 对齐**　Range ←“Make sure it is after and before a specific date // e.g. between 1900 and today's date // check month is between 1 and 12 …”；Presence ←“Make sure the date of birth has been entered”；Length ←“must be 8 characters”（或“at least 1 for day, 1 for month, 2/4 for year”）。

**英文作答句**　Range check: make sure the date of birth is between 01/01/1900 and today’s date. Presence check: make sure the date of birth has been entered and the field is not left blank. Length check: make sure the date of birth is 8 characters long, for example in the format DDMMYYYY.

**直观**　校验像门口的安检机：只看你带的东西形状、大小合不合规定，不管东西是不是你自己的。

**下一道变式**　⟦9618_w25_13:7(e)⟧　（反过来：给三段伪代码，判断各是哪种校验，三种必须不同。）

<!-- auto:drills P1-SP-06 -->

### P1-SP-07　数据验证　{#P1-SP-07}

<!-- auto:stats P1-SP-07 -->

**考法**　①录入时的验证：visual check、double entry（各“名称 + 描述”）；②传输时的验证：parity byte / parity block / checksum（名称 1 + 描述 1–2）；③解释 checksum 怎样工作（3 分）；④奇偶校验填空；⑤补写奇偶位、在奇偶块里圈出出错的位；⑥连线：验证方法 ↔ 用于录入还是传输。

**识别信号**　verification；verify；visual check；double entry；parity check / bit / byte / block；even / odd parity；checksum；during data entry / data transfer。

**解题思路**
1. 验证 = 检查数据和**原来的**（原始文件、发送端）是否一致。先看是“录入”还是“传输”：

| 场合 | 方法 | 怎样做 |
|:--|:--|:--|
| 录入 | Visual check | 录入后由人把输入的数据与原始文件逐项对照 |
| 录入 | Double entry | 输入两次，计算机比较两次是否一致，不一致就提示 |
| 传输 | Parity byte (parity bit) | 每个字节加一个奇偶位，使 1 的个数符合约定的奇/偶；收到后检查每个字节 |
| 传输 | Parity block | 每个字节有奇偶位，再对每一列（位位置）算出一个奇偶字节随数据一起发；可定位出错的位 |
| 传输 | Checksum | 发送前由数据算出一个值随数据发送；接收方用同样算法重算并比较，不同就有错（要求重发） |

2. **补奇偶位**：数出已有 7 位里 1 的个数；偶校验时让总数为偶，奇校验时让总数为奇。
3. **在奇偶块里找错位**：①逐行（每个字节）数 1，找出奇偶不对的那一行；②逐列数 1（含奇偶字节那一行），找出奇偶不对的那一列；③行列交叉处就是被改的位，把它取反即可恢复。

自编例（偶校验，最右一位是奇偶位）：

```
Byte A    1 0 1 1 0 0 1 0   four 1s  ✓
Byte B    0 1 0 0 1 0 1 0   three 1s ✗  ← row error
Byte C    1 1 0 0 0 1 0 1   four 1s  ✓
Parity    0 0 0 1 1 1 0 1
              ↑ column 3: 1+0+0+0 = one 1 ✗
```

第 3 列与 Byte B 交叉的那一位（0）出错，原值应为 1。

4. 奇偶校验的局限：**同一字节内偶数个位翻转**，该字节的奇偶性不变，可能绕过单字节奇偶检查。块校验还检查各列：同一行的两列各翻转一位时，行奇偶虽不变，两列的奇偶都会改变，仍能发现错误；不能把“两位必漏检”套到块校验。

**得分表述**（引自对应 MS）
- 「Double entry: Enter the registration number twice and the computer compares to check they are the same」⟦9618_s23_13:4(d)(ii)⟧
- 「Manually compare the data entered with the original (document)」⟦9618_s22_13:5(b)(i)⟧
- 「A calculation is made from the data and the result transmitted with the data」⟦9618_s24_13:7(f)(i)⟧
- 「The receiver repeats the calculation and compares the result with the value received」⟦9618_s24_13:7(f)(i)⟧
- 「Parity is calculated horizontally and vertically」⟦9618_s24_13:7(f)(i)⟧
- 「the location of an error can be found using vertical and horizontal parity」⟦9618_w25_13:7(c)⟧

**易错与失分**
- 录入与传输的方法用错场合：visual check / double entry 只用于录入，parity / checksum 只用于传输。
- Checksum 只写“检查数据有没有错”：要写出“发送前算 → 随数据发 → 接收方重算 → 比较”四步。
- 奇校验填空的反直觉：约定奇校验、而这组已有偶数个 1 时，奇偶位填 **1**（凑成奇数）。
- 奇偶位位置看清：题目会说明是最高位还是最低位（最右）是奇偶位。
- 把 range check 等写成验证：那是校验（SP-06）。

#### 代表题精讲　⟦9618_s24_13:7(f)(i)⟧

**在考什么**　餐厅机器人通过无线把数据传到中央计算机。Complete the table by identifying and describing two methods of data verification that can be used during data transfer. 4 分 = 2 ×（方法 1 + 描述 1）。

**完整作答**
- 方法 1：Parity byte（奇偶校验位）。描述：每个字节加一个额外的位，使字节中 1 的个数为奇或偶以符合约定；若使用偶校验却收到含奇数个 1 的字节，就说明出错。
- 方法 2：Checksum。描述：发送前由数据计算出一个值，随数据一起发送；接收方重复同样的计算，与收到的值比较，两者不同就说明出错。

**与 MS 对齐**　MS 三组任选两组：Parity byte ←“An additional bit is added to make the number of 1s in the byte odd or even to match the parity …”；Parity block ←“Parity is calculated horizontally and vertically. A parity byte is created from the bits produced by the vertical parity check …”；Checksum ←“A calculation is made from the data and the result transmitted with the data. The receiver repeats the calculation and compares the result with the value received. If the two are different, there is an error.”

**英文作答句**　Parity byte: an additional bit is added to each byte to make the number of 1s odd or even to match the agreed parity; if a byte with an odd number of 1s is received when even parity is used, there is an error. Checksum: a calculation is made from the data and the result is transmitted with the data; the receiver repeats the calculation and compares the result with the value received, and if the two are different there is an error.

**直观**　Checksum 像快递单上写的“共 12 件”：收件人自己点一遍，件数不对就知道路上丢了或多了。

**下一道变式**　⟦9618_w25_12:6(c)(ii)⟧　（换成动手题：偶校验的奇偶块里有一位出错，圈出它。先找行、再找列。讲解时请对照原卷 QP p.11 与 MS p.9 看圈的位置。）

<!-- auto:drills P1-SP-07 -->

### P1-SP-08　校验与验证的区别与局限　{#P1-SP-08}

<!-- auto:stats P1-SP-08 -->

**考法**　①说出验证与校验的区别（1 分，一句两边）；②解释在录入某字段时怎样同时使用校验和验证（校验最多 3 分 + 验证最多 2 分）；③为什么数据通过校验和验证后仍可能不正确（1–2 分）；④校验与验证怎样共同支持数据完整性。

**识别信号**　the difference between data verification and data validation；Explain how data validation and data verification can be used when …；why … might be incorrect / may not be correct even after it has been validated and verified。

**解题思路**
1. 区别一句话：verification 检查输入的数据**与原件一致**；validation 检查数据**合理、在范围内**。
2. “两者怎样用”分两栏写，各自扣题目的字段：校验写 2–3 种（range、presence、type…带具体界限），验证写 2 种（double entry、visual check）。
3. “通过后仍不正确”的原因：校验只看合理不合理，不看是否准确；验证只看与原件是否一致，不看原件本身对不对。所以原件本身就错、或错的值恰好也在合理范围内，两道检查都发现不了。

**得分表述**（引自对应 MS）
- 「data verification is checking if input data is the same as the original whereas data validation is checking that the data is reasonable / sensible」⟦9618_w22_12:4(a)⟧
- 「range check to make sure it is between 0 and max marks」⟦9618_s22_11:4(d)⟧
- 「double entry - enter the mark twice and the computer compares them」⟦9618_s22_11:4(d)⟧
- 「Validation checks data is reasonable/within bounds it does not check that accurate data has been entered」⟦9618_s22_13:5(b)(iii)⟧
- 「Verification checks if the data matches the data given it does not check if the original data is accurate」⟦9618_s22_13:5(b)(iii)⟧

**易错与失分**
- 区别题只写一边。
- “两者怎样用”只写一种，或校验写成 3 个都是定义而没落到字段上（0 至该测验满分、必须是整数）。
- “仍不正确”写成“computer error / typo”：错字会被验证查出来；要说的是**原件错**或**错值也合理**。

#### 代表题精讲　⟦9618_s22_11:4(d)⟧

**在考什么**　老师把学生测验分数录入数据库，分数必须是 0 到该测验满分之间的整数。Explain how data validation and data verification can be used when a mark is entered. 4 分（校验最多 3，验证最多 2）。

**完整作答**
- 校验：范围检查——分数在 0 与该测验满分之间；存在性检查——分数必须输入；类型检查——必须是整数。
- 验证：两次录入——分数输入两次，计算机比较两次是否一致；目视检查——把录入的分数与输入单据上的分数人工对照。

**与 MS 对齐**　Validation ←“range check to make sure it is between 0 and max marks”“presence check to make sure a mark is entered”“type check to make sure an integer value is entered”；Verification ←“double entry - enter the mark twice and the computer compares them”“visual check – manually compare the mark entered with the mark on the input document”。校验写 2、验证写 2 已够 4 分；各多写一个更稳。

**英文作答句**　Validation: a range check makes sure the mark is between 0 and the maximum mark for that test, a presence check makes sure a mark is entered, and a type check makes sure an integer value is entered. Verification: double entry, where the mark is entered twice and the computer compares them, or a visual check, where the mark entered is manually compared with the mark on the input document.

**直观**　校验问“这个数像不像分数？”，验证问“这个数是不是卷面上那个数？”——两个问题都答“是”，卷面上的分数本身也可能批错。

**下一道变式**　⟦9618_s22_13:5(b)(iii)⟧　（只问局限：为什么校验加验证之后数据仍可能不对，两边各一句。）

<!-- auto:drills P1-SP-08 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| Security vs privacy vs integrity | 不丢不坏 / 只有授权者能看 / 准确一致 | loss · unauthorised access · accurate |
| SP-01 vs DB-09 | 一般意义的完整性 → SP-01；数据库中怎样保证完整性（参照完整性、级联）→ DB-09 | 有没有 DBMS、外键 |
| SP-02 vs SP-03 | 描述威胁本身（+ 列防范名称）→ SP-02；描述措施怎样工作 → SP-03 | describe the threat 还是 how the measure works |
| Phishing vs pharming | 邮件诱导用户行动 / 恶意代码自动重定向到假网站 | email 还是 redirect |
| Virus vs spyware | 复制自己、破坏数据 / 不复制、偷记录并外传 | replicates · sends to third party |
| SP-03 vs SP-04 | 问一般措施、MS 接受多种 → SP-03；问传输中保护、MS 只接受加密 → SP-04 | during transmission / intercepted |
| 防火墙 vs 杀毒软件 | 按规则过滤进出流量 / 扫描文件与特征库比对 | traffic / rules 还是 scan / database of viruses |
| 加密 vs 数字签名 | 截获了也看不懂 / 证明来源真实、内容未被改 | understood 还是 authentic / not changed |
| SP-06 校验 vs SP-07 验证 | 合理吗（计算机按规则查）/ 与原件一致吗（比对） | reasonable · same as original |
| Range check vs limit check | 两端 / 一端 | between 还是 before / after |
| 录入验证 vs 传输验证 | visual check、double entry / parity、checksum | data entry 还是 data transfer |
| SP-06 / SP-07 vs SP-08 | 只问一种 → SP-06 或 SP-07；比较、合用、局限 → SP-08 | difference · both · still incorrect |
| SP-03 vs DB-08 | 一般计算机系统的措施 → SP-03；DBMS 的访问权限、视图、备份 → DB-08 | 题干有没有 DBMS / database |
