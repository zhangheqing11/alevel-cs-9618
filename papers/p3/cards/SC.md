## SC　安全 {#ch-SC}

<!-- auto:chapter-stats -->

### 核心思想

这一章是 P1「安全」里加密、数字签名（P1-SP-04、P1-SP-05）的 A2 加深版，考纲只有 17.1 一节，题目全是文字题。整章只有一个核心问题：**用谁的哪把钥匙？**

非对称加密里每一方都有自己的一对钥匙：公钥（public key）可以给任何人，私钥（private key）只有主人自己有。一把加密的，只有同一对里的另一把能解密。按“想达到什么目的”选钥匙：

| 目的 | 加密用 | 解密用 | 题型 |
|:--|:--|:--|:--|
| 私密：只有接收方能读 | **接收方**的公钥 | **接收方**的私钥 | SC-02 |
| 已验证：证明是发送方发的 | **发送方**的私钥 | **发送方**的公钥 | SC-02 |
| 数字签名：证明发送方 + 证明没被改 | 消息先散列成摘要，摘要用**发送方**私钥加密 | 用**发送方**公钥解出摘要，再与重新散列的摘要比较 | SC-06 |

所以“私钥用来解密”“公钥用来加密”都只在**私密消息**这个场合成立；在已验证消息和数字签名里正好反过来。答题时每提到一把钥匙，都写清楚是**谁的**（Sheila’s public key、the sender’s private key），考官报告反复指出只写 “public key” 不写归属会丢分。

其余三型围绕“公钥从哪里来、可不可信”：

1. **数字证书**（SC-05）：由证书机构 CA 签发、证明“这把公钥确实属于这个组织”的电子文档。
2. **SSL/TLS**（SC-04）：浏览器连网站时，先用证书拿到服务器的公钥、商定算法、生成会话密钥，再加密通信。
3. **量子密码**（SC-03）：不靠数学难题，靠物理规律分发密钥，有人窃听就会被发现。

本章文字题的规律与 SY 相同：MS 列出的点比满分多（“Max n”），带 “…” 的点是前一点的展开。过程题（SC-02、SC-04、SC-05、SC-06）**按时间顺序**一句一步写，每句点名主体（谁的计算机）和钥匙（谁的哪把）。

### 题型树
<!-- auto:type-tree -->

### P3-SC-01　加密术语与对称、非对称加密　{#P3-SC-01}

<!-- auto:stats P3-SC-01 -->

**考法**　①说明私钥 / 公钥 / 密文等术语（1–2 分）；②给出使用密钥加密的两个理由，或说出两种密钥加密方法（各 2 分）；③描述非对称加密的目的（2 分）；④说明或描述对称与非对称加密的区别（2–3 分）；⑤已给出非对称，再说出另一种密码类型（1 分）。

**识别信号**　private key；public key；cipher text；reasons for using key cryptography；methods of key cryptography；purpose of asymmetric key cryptography；differences between symmetric and asymmetric；one other type of cryptography。

**解题思路**
1. **术语**：明文（plain text）是加密前可读的数据；密文（cipher text）是用加密算法和密钥处理后的结果；私钥不公开、不传输，和一把公钥配对；公钥任何人都能拿到。
2. **为什么要用密钥加密**：从“通信安全”的角度写——只有指定接收方能读懂、消息来源可信（真实性）、传输中没被改、双方不能否认发过 / 收过（non-repudiation）。只写“防黑客”太空泛。
3. **方法 / 类型**：对称（symmetric）、非对称（asymmetric）；题目已给出其中一种时，答另一种或量子（quantum）。
4. **区别题**：每一句都要**两边都写**（“对称……，而非对称……”），从下面几个角度挑：

| 角度 | 对称 | 非对称 |
|:--|:--|:--|
| 钥匙数量 | 一把，加密解密用同一把 | 两把（公钥 + 私钥），一把加密、配对的另一把解密 |
| 分发 | 那一把要共享给对方，被截获就泄露 | 只公开公钥，私钥不传输，更安全 |
| 速度 | 过程简单、快 | 复杂、慢 |
| 密钥长度 | （通常）较短，如 128 / 256 位 | 较长，如 2048 位 |

5. **非对称的目的**：提供更好的安全性 → 用两把不同的钥匙（公钥、私钥）→ 一把加密 → 配对的另一把解密。

**得分表述**（引自对应 MS）
- 「Symmetric cryptography uses a single key to encrypt and decrypt messages, Asymmetric cryptography uses two」⟦9618_s23_32:5(b)⟧
- 「The symmetric key is shared, whereas with asymmetric, only the public key is shared (and the private key isn’t)」⟦9618_s23_32:5(b)⟧
- 「Symmetric cryptography is a simple process that can be carried out quickly, but asymmetric is much more complex, so slower」⟦9618_s23_32:5(b)⟧
- 「A private key is the unpublished/secret key/never transmitted anywhere」⟦9618_w22_31:6(a)⟧
- 「To ensure that only the intended receiver is able to understand the message」⟦9618_s22_31:8(a)(i)⟧
- 「by using two different keys / a public key and a private key」⟦9618_s23_31:9(a)⟧

**易错与失分**
- 区别题只写一边（“symmetric uses one key”）：考官报告指出，很多答案只详细写了一个区别，而不是写出几个区别（⟦9618_s23_32:5(b)⟧）。每句都要“对称……而非对称……”。
- 理由写得太空泛：考官报告指出 “prevents hacking”“others cannot read the message” 这类答案不给分，要写成“只有指定接收方能读懂”（⟦9618_s22_31:8(a)(i)⟧）。
- “目的”写成了“怎样用”：考官报告指出，有的答案写了非对称加密的特征或使用过程，没有写目的（⟦9618_s23_31:9(a)⟧）。目的的第一句是 “to provide better security”。
- “另一种类型”又写 asymmetric：题目已经给出，不给分（考官报告，⟦9618_w25_32:7(a)⟧）。
- 把“私钥用来解密”当成私钥在任何场合的用途：⟦9618_w22_31:6(a)⟧ 的 MS 把私钥写成「used to decrypt data that was encrypted with its matching public key」⟦9618_w22_31:6(a)⟧，这是私密消息的用法；但该题题干背景其实是“用私钥加密”（已验证消息），可见 MS 只是按私钥的常见定义给分。定义题照 MS 写；过程题按场合选钥匙——在已验证消息和数字签名里，私钥是用来**加密**的（见 SC-02、SC-06）。

#### 代表题精讲　⟦9618_s23_32:5(b)⟧

**在考什么**　Explain the differences between symmetric and asymmetric cryptography when encrypting and decrypting data. 3 分。MS “One mark per mark point (Max 3)”，列了 5 点，其中 MP3 以 “…” 开头，是 MP2 的展开。

**完整作答**
1. 对称加密用一把钥匙加密和解密，非对称加密用两把（一把加密，配对的另一把解密）。
2. 对称加密的那把钥匙要共享给对方，非对称只共享公钥，私钥不共享；
3. ……所以对称加密被攻破的风险更高，非对称更安全。
4. 对称加密过程简单、速度快；非对称复杂得多，所以更慢。

**与 MS 对齐**　1 ← MP1；2 ← MP2；3 ← MP3（必须接在 2 后面写才成立）；4 ← MP4。写出 4 个独立得分点，满分 3 分，多写一点是保险。也可以把 4 换成 MP5 “密钥长度：对称通常比非对称短（128/256 位 对 2048 位）”。

**英文作答句**　Symmetric cryptography uses a single key to encrypt and decrypt messages, whereas asymmetric cryptography uses two keys. The symmetric key is shared, whereas with asymmetric only the public key is shared and the private key is not, so the risk of compromise is higher with symmetric encryption and asymmetric encryption is more secure. Symmetric cryptography is a simple process that can be carried out quickly, but asymmetric is much more complex, so slower.

**直观**　对称加密像一把家门钥匙，要配一把给朋友，路上丢了谁都能开门。非对称像一个只能投不能取的信箱：投信口（公钥）谁都能用，开箱的钥匙（私钥）只在主人手里。

**下一道变式**　⟦9618_w22_31:6(a)⟧　（State what is meant by a private key，2 分：不公开、不传输 + 有配对的公钥 + 用来解密用配对公钥加密的数据，三点写两点。）

<!-- auto:drills P3-SC-01 -->

### P3-SC-02　用密钥对发送私密消息与已验证消息　{#P3-SC-02}

<!-- auto:stats P3-SC-02 -->

**考法**　给一个场景（Fred 给 Sheila 发机密文件；一个组织要接收加密传输；描述非对称加密的过程），按步骤说明两把钥匙怎样用（2–4 分）。场景多数是**私密消息**；也可能问**已验证消息**（发送方用自己的私钥加密，让任何人用其公钥解密来确认发送方）。

**识别信号**　Describe the process of asymmetric encryption；Explain how … uses asymmetric encryption to send … securely；makes use of the two keys to receive a secure transmission；send a private message；send a verified message。

**解题思路（逐步作答模板：私密消息）**
1. **接收方**用算法生成一对配对的钥匙：公钥与私钥。
2. 接收方把**公钥**发给发送方 / 公开给任何想给它发消息的人；私钥自己保留。
3. 发送方用**接收方的公钥**把消息（明文）加密成密文。
4. 发送方把密文发给接收方。
5. 接收方用**自己的私钥**解密；只有这把私钥能解开，所以只有接收方能读。

**已验证消息**把钥匙换成**发送方**的：发送方生成钥匙对、公开公钥 → 用自己的私钥加密 → 发出 → 任何人用发送方的公钥解密，能解开就证明是发送方发的。

每一步写清楚**谁的计算机**做、用**谁的哪把**钥匙。场景里有人名就用人名（Sheila’s public key）。

**得分表述**（引自对应 MS）
- 「Sheila’s computer uses an algorithm to generate a matching pair of keys private and public」⟦9618_s24_32:4⟧
- 「Fred’s computer encrypts the document/plain text using Sheila’s public key to create cipher text」⟦9618_s24_32:4⟧
- 「The organisation makes the public key available to anyone who wishes to send them secure transmissions」⟦9618_w25_32:7(b)⟧
- 「The organisation uses its private key to decrypt the message」⟦9618_w25_32:7(b)⟧
- 「The message to be sent is encrypted using the recipient’s public key」⟦9618_w22_31:6(b)⟧
- 「The message to be sent is encrypted using the sender’s private key」⟦9618_w22_31:6(b)⟧

**易错与失分**
- 钥匙不写归属：考官报告指出，有的答案没说清楚用哪把钥匙加密 / 解密，或没说明两把钥匙是配对的；好的答案是“用接收方的公钥加密、再用接收方的私钥解密”（⟦9618_w22_31:6(b)⟧）。
- 钥匙用反、把私钥发出去：考官报告指出，常见错误包括没说清两把钥匙是配对的、属于该组织，把钥匙用反导致私钥被共享，以及把本题和消息摘要、数字签名的题混在一起（⟦9618_w25_32:7(b)⟧）。
- 漏掉最后一步：考官报告指出，能拿第四分的考生相对较少（⟦9618_s24_32:4⟧）。第四分要写出“把密文发给 Sheila，Sheila 用她自己的私钥解密”。
- 一个题里混用两种场景：私密消息全程用**接收方**的钥匙；已验证消息全程用**发送方**的钥匙。

#### 代表题精讲　⟦9618_s24_32:4⟧

**在考什么**　Sheila has a customer called Fred. Fred wants to send Sheila a confidential document as part of a transaction. Explain how Fred uses asymmetric encryption to send his document securely. 4 分，MS 正好 4 个点（Max 4），每步 1 分，一步都不能漏。confidential（机密）说明是**私密消息**：用接收方 Sheila 的钥匙。

**完整作答**
1. Sheila 的计算机用算法生成一对配对的钥匙：私钥和公钥。
2. Sheila 的计算机把 Sheila 的公钥发给 Fred 的计算机（Fred 取得 Sheila 的公钥）。
3. Fred 的计算机用 Sheila 的公钥把文件（明文）加密成密文。
4. Fred 的计算机把密文发给 Sheila 的计算机，Sheila 的计算机用 Sheila 的私钥解密。

**与 MS 对齐**　1 ← MP1；2 ← MP2（“sends Fred’s computer Sheila’s public key // Fred’s computer acquires Sheila’s public key” 两种说法任写一种）；3 ← MP3；4 ← MP4（“sends the cipher text … can only be decrypted using Sheila’s private key // Sheila’s computer uses Sheila’s private key to decrypt the cipher text”）。

**英文作答句**　1: Sheila’s computer uses an algorithm to generate a matching pair of keys, private and public. 2: Sheila’s computer sends Sheila’s public key to Fred’s computer. 3: Fred’s computer encrypts the document (plain text) using Sheila’s public key to create cipher text. 4: Fred’s computer sends the cipher text to Sheila’s computer, and Sheila’s computer uses Sheila’s private key to decrypt the cipher text.

**直观**　Sheila 发给每个客户一把打开的挂锁（公钥），钥匙（私钥）留在自己口袋。Fred 把文件放进箱子、扣上 Sheila 的挂锁寄回去；路上谁拿到箱子都打不开，只有 Sheila 的钥匙能开。

**下一道变式**　⟦9618_w25_32:7(b)⟧　（组织持有两把钥匙、要接收加密传输：同样四步，主角换成“组织”和“发送方”，第一句要点明两把钥匙是私钥和公钥。）

<!-- auto:drills P3-SC-02 -->

### P3-SC-03　量子密码　{#P3-SC-03}

<!-- auto:stats P3-SC-03 -->

**考法**　①描述量子密码的目的（2 分）；②给出两个好处、两个缺点（各 2 分，或合成一道 4 分）。

**识别信号**　quantum cryptography；purpose；benefits；drawbacks；secure exchange (of keys)。

**解题思路**
1. **它是什么**：用光子（photon）的量子性质来分发密钥，安全性来自物理定律，而不是“数学题很难算”。窃听者一测量光子，光子的状态就会改变，通信双方能发现。
2. **目的**（写 2 句，前一句“做什么”，后一句“靠什么”）：产生几乎不可破解的加密系统 / 发送几乎不可能被黑的安全消息 → 利用量子力学原理 / 光子的性质；或者：能发现窃听 → 因为光子的性质会改变。
3. **好处与缺点**，每条写成具体的一句：

| 好处 | 缺点 |
|:--|:--|
| 能发现窃听（状态会改变） | 目前只能在相对短的距离内使用 |
| 安全性基于物理定律而不是数学算法，几乎不可破解 | 需要专用光纤线路和专门硬件，购买 / 维护成本高 |
| 可以用更长的密钥 | 光在光纤里传输时偏振可能改变 |
| 密钥传过去后完整性有保证（不能被复制、以后再解密） | 技术仍在发展，错误率较高；缺少数字签名等功能 |

**得分表述**（引自对应 MS）
- 「Provides security based on laws of physics rather than mathematical algorithms, so more secure」⟦9618_s23_31:9(b)⟧
- 「Eavesdropping can be detected」⟦9618_s23_31:9(b)⟧
- 「Currently only works over relatively short distances」⟦9618_s23_31:9(b)⟧
- 「High cost of purchasing / maintaining equipment required」⟦9618_s23_31:9(b)⟧
- 「to produce a virtually unbreakable encryption system」⟦9618_s23_32:5(a)⟧
- 「polarisation of light may be altered whilst travelling down fibre optic cables」⟦9618_s22_31:8(b)(ii)⟧

**易错与失分**
- 写“能防止窃听”：考官报告指出 “prevents eavesdropping” 不准确，正确的是“能**发现**窃听，因为状态会改变”（⟦9618_s22_31:8(b)(i)⟧）。量子密码挡不住别人去测，只是测了会被发现。
- 只写“太贵”：考官报告指出 “too expensive” 太空泛，不给分（⟦9618_s22_31:8(b)(ii)⟧）。要写贵在哪：专用光纤线路和专门硬件。
- 拿别的加密方法作比较、或只列特征：考官报告指出，有的答案把量子密码和其他加密方式比较，或只罗列特征，没有说清是好处还是缺点（⟦9618_s23_31:9(b)⟧）。
- 目的写成工作原理：考官报告指出，得分的是写“目的”的答案，如“产生几乎不可破解的加密系统”，而不是只描述量子密码是什么或怎样工作（⟦9618_s23_32:5(a)⟧）。

#### 代表题精讲　⟦9618_s23_31:9(b)⟧

**在考什么**　Identify two benefits and two drawbacks of quantum cryptography. 4 分：“One mark per benefit (Max 2)” + “One mark per drawback (Max 2)”，两边各列 6 点。

**完整作答**
- 好处 1：能发现窃听。
- 好处 2：安全性基于物理定律而不是数学算法，所以更安全。
- 缺点 1：目前只能在相对短的距离内使用。
- 缺点 2：需要的设备购买和维护成本高。

**与 MS 对齐**　好处 1 ← benefit MP6；好处 2 ← benefit MP1；缺点 1 ← drawback MP3；缺点 2 ← drawback MP2。好处和缺点分开计分，各最多 2 分；写了三个好处、一个缺点只能得 3 分。

**英文作答句**　Benefit 1: Eavesdropping can be detected. Benefit 2: It provides security based on the laws of physics rather than mathematical algorithms, so it is more secure. Drawback 1: It currently only works over relatively short distances. Drawback 2: There is a high cost of purchasing and maintaining the equipment required.

**直观**　量子密钥像肥皂泡：谁伸手去碰，它就破了，收件人一看就知道有人碰过。代价是泡泡飞不远，吹泡泡的设备还很贵。

**下一道变式**　⟦9618_s23_32:5(a)⟧　（Describe the purpose of quantum cryptography，2 分：“几乎不可破解的加密 → 利用量子力学 / 光子性质”或“发现窃听 → 光子性质会变”，每对是“点 + 展开”。）

<!-- auto:drills P3-SC-03 -->

### P3-SC-04　SSL/TLS　{#P3-SC-04}

<!-- auto:stats P3-SC-04 -->

**考法**　①说出 SSL/TLS 的两个功能，或描述它的目的（2 分）；②给出两个适合使用 SSL/TLS 的场合（2 分）；③说出组成 TLS 的两个主要协议并各说明作用（4 分）；④解释客户端—服务器通信开始时 SSL/TLS 怎样使用（握手过程，4 分）。

**识别信号**　Secure Sockets Layer；Transport Layer Security；functions；situations where … appropriate；two main protocols that form TLS；client-server communication is initiated。

**解题思路**
1. **目的 / 功能**：在互联网 / 网络上提供通信安全 → 加密数据 → 让双方识别、认证对方 → 保密性与完整性。
2. **适用场合**：传输认证数据（密码、会话 cookie）；传输不能被篡改的数据（用户输入、服务器返回结果）；传输非公开数据。网购付款、网银登录都属于这些。
3. **TLS 的两个协议**：

| 协议 | 作用 |
|:--|:--|
| Handshake protocol（握手协议） | 在两台设备之间建立安全可靠的连接：服务器与客户端互相认证、商定加密算法 |
| Record protocol（记录协议） | 在连接上安全可靠地收发数据：加密并认证交换的数据，保证完整性 |

4. **握手过程（逐步作答模板）**，按顺序一句一步：
   1. 应用（客户端）发起 SSL/TLS 连接，接收连接的一方是服务器。
   2. 每个新会话都从握手开始。
   3. 客户端向服务器请求数字证书（服务器把证书发给客户端）。
   4. 客户端验证服务器的数字证书，
   5. ……并从中取得服务器的公钥。
   6. 商定加密算法；生成对称的会话密钥。
   7. 客户端与服务器之间建立起安全会话。

**得分表述**（引自对应 MS）
- 「An SSL/TLS connection is initiated by an application/client」⟦9618_s25_33:7⟧
- 「Every new session begins with a handshake as defined by the SSL/TLS protocols」⟦9618_s25_33:7⟧
- 「The client verifies the server’s digital certificate」⟦9618_s25_33:7⟧
- 「Identification / authentication of client and server」⟦9618_s25_31:9(a)⟧
- 「When transmitting authentication data e.g. passwords, session cookies」⟦9618_s25_31:9(b)⟧
- 「Encrypts and authenticates data exchanged between a client and a server」⟦9618_s25_32:10⟧

**易错与失分**
- 步骤顺序错：考官报告指出，有的答案把各阶段的顺序写错（⟦9618_w21_31:8(b)⟧）；用正确术语、按正确顺序写的考生得分最高（⟦9618_s25_33:7⟧）。证书在前、会话密钥在后。
- 两个协议写成 HTTP、SMTP：考官报告指出这是常见错误，它们是应用层协议，不是组成 TLS 的协议（⟦9618_s25_32:10⟧）。
- 把握手写成“加密数据”一句带过：握手的得分点在“请求证书 → 验证证书 → 取得公钥 → 商定算法 / 会话密钥”，每步一分。

#### 代表题精讲　⟦9618_s25_33:7⟧

**在考什么**　Secure Socket Layer (SSL) and Transport Layer Security (TLS) are two protocols. Explain how SSL/TLS is used when client-server communication is initiated. 4 分，MS 列 7 点（Max 4），MP5 以 “…” 开头，是 MP4 的展开。

**完整作答**
1. 应用（客户端）发起 SSL/TLS 连接。
2. 每个新会话都以 SSL/TLS 协议规定的握手开始。
3. 客户端向服务器请求数字证书。
4. 客户端验证服务器的数字证书，
5. ……并取得服务器的公钥。
6. 双方商定加密算法，生成对称的会话密钥。

**与 MS 对齐**　1 ← MP1；2 ← MP2；3 ← MP3（“The client requests the digital certificate from the server // The server sends the digital certificate to the client” 任写一种）；4 ← MP4；5 ← MP5；6 ← MP6（“The encryption algorithms are agreed. // The symmetric session keys are generated/defined.” 是同一点的两种说法，两句都写也只算 1 分）。共 6 个独立得分点，满分 4 分；还可补 MP7 “建立安全会话”。

**英文作答句**　An SSL/TLS connection is initiated by an application/client. Every new session begins with a handshake as defined by the SSL/TLS protocols. The client requests the digital certificate from the server. The client verifies the server’s digital certificate and obtains the server’s public key. The encryption algorithms are agreed and the symmetric session keys are generated. A secure session is established between client and server.

**直观**　握手像去银行办业务：先看柜员的工牌（证书）是不是银行发的、是不是本人，确认后再约定这次谈话用的暗号（会话密钥），之后说的话都用暗号。

**下一道变式**　⟦9618_s25_32:10⟧　（说出组成 TLS 的两个协议并各说作用，4 分：握手协议 + 建立安全连接；记录协议 + 安全收发数据。）

<!-- auto:drills P3-SC-04 -->

### P3-SC-05　数字证书　{#P3-SC-05}

<!-- auto:stats P3-SC-05 -->

**考法**　①描述数字证书是什么（3 分）；②说出证书里常见的两个项目（2 分）；③说明组织怎样获取数字证书（3–4 分）。

**识别信号**　digital certificate；Describe what is meant by；items commonly found within；how a digital certificate is obtained；acquire its digital certificate。

**解题思路**
1. **是什么**（按“形式 → 用途 → 谁发 → 含什么”写）：电子 / 在线文档 → 用来认证 / 证明网站、个人或组织的在线身份 → 通常由证书机构（CA）签发 → 含有标识持有者的信息和持有者的公钥。
2. **证书里的项目**：持有者名称（subject）、序列号、版本号、有效期（起止日期）、**持有者的**公钥、签发者（CA）/ CA 的数字签名。写公钥、签名时要说明是**谁的**。
3. **获取过程（逐步作答模板）**：
   1. 组织生成一对公钥 / 私钥。
   2. 组织向证书机构（CA）申请证书。
   3. 组织收集 CA 要求的信息（包括证明身份的信息），连同自己的公钥发给 CA。
   4. CA 核实组织的身份。
   5. CA 生成 / 签发证书，证书里包含该组织的公钥（和其他信息）。

**得分表述**（引自对应 MS）
- 「A digital certificate is an electronic/online document」⟦9618_s24_31:7(a)⟧
- 「used to authenticate/prove the identity of a website/the online identity of an individual/organisation」⟦9618_s24_31:7(a)⟧
- 「The organisation requests a certificate from a Certificate Authority (CA)」⟦9618_w22_32:6(b)⟧
- 「The CA verifies the organisation’s identity」⟦9618_w22_32:6(b)⟧
- 「The CA generates / issues the certificate including the organisation’s public key (and other information)」⟦9618_w22_32:6(b)⟧
- 「Certificate holder’s public key // Subject public key」⟦9618_w25_31:5(a)⟧

**易错与失分**
- 项目写 “public key”“digital signature” 不写是谁的、或只写 “Certificate Authority” 不加说明：考官报告指出这些是常见的缺漏（⟦9618_w25_31:5(a)⟧）。写成 certificate holder’s public key、certificate issuer。
- 把获取证书写成 SSL 认证过程：考官报告指出这是常见错误（⟦9618_s22_32:7(a)⟧）。获取证书是“组织 ↔ CA”，SSL 握手是“客户端 ↔ 服务器”。
- 步骤不全或顺序乱：考官报告指出满分答案很少，得满分的是按正确顺序写出“向 CA 申请 → 发送认证信息 → CA 核实后签发”并适当展开的考生（⟦9618_w25_33:9⟧）。

#### 代表题精讲　⟦9618_w22_32:6(b)⟧

**在考什么**　Explain the process by which an organisation may acquire its digital certificate. 4 分，MS 列 5 点（“One mark for each point (Max 4)”）。

**完整作答**
1. 组织向证书机构（CA）申请证书。
2. 组织把自己的公钥发给 CA。
3. 组织收集 CA 要求的全部信息，包括证明自己身份的信息。
4. CA 核实组织的身份。
5. CA 生成并签发证书，证书里包括该组织的公钥（和其他信息）。

**与 MS 对齐**　1–5 依次对应 MS 的 5 个点，每点 1 分，满分 4。写 5 句多一点保险；3 和 4 是最容易漏的“核实身份”两步。

**英文作答句**　The organisation requests a certificate from a Certificate Authority (CA). The organisation sends its public key to the CA. The organisation gathers all the information required by the CA, including information to prove its identity. The CA verifies the organisation’s identity. The CA generates and issues the certificate including the organisation’s public key and other information.

**直观**　数字证书像护照：你去出入境管理处（CA）申请，交上身份证明和照片（公钥），他们核实是你本人后，签发一本盖了章的护照，别人看到章就信得过照片是你。

**下一道变式**　⟦9618_w25_33:9⟧　（同一过程的详细版，4 分：多了“在本地用 RSA 工具生成密钥对”“CA 回传它的公钥和证书、并用私钥签名”“公司发送的信息用自己的私钥签名、用 CA 的公钥加密”。）

<!-- auto:drills P3-SC-05 -->

### P3-SC-06　数字签名的产生与验证　{#P3-SC-06}

<!-- auto:stats P3-SC-06 -->

**考法**　①说明发送前数字签名怎样产生（3 分）；②说明接收后怎样用数字签名验证消息没被改（4 分）；③说明数字证书在产生 / 验证数字签名中的作用、为什么需要（2–3 分）。

**识别信号**　digital signature is produced before the message is sent；checked on receipt；verify a message when it is received；role of a digital certificate in creating a digital signature；why a digital certificate is required to validate a digital signature。

**解题思路（逐步作答模板）**

**产生（发送方）**：
1. 用（双方约定的）散列算法对消息做散列，
2. ……得到消息摘要（message digest）。
3. 用**发送方的私钥**加密消息摘要，得到数字签名，附在消息上发送。

**验证（接收方）**：
1. （若整个消息连同签名还用接收方的公钥加密过）先用**接收方的私钥**解密，得到消息和签名。
2. 用**发送方的公钥**解密数字签名，得到发送方算出的消息摘要。
3. 用同一个散列算法对收到的消息重新散列，得到第二个消息摘要。
4. 比较两个摘要。
5. 相同 → 消息没被改动（而且确实是发送方签的）；不同 → 消息被改过。

**证书的作用**：数字证书提供发送方的公钥 → 这把公钥用来验证产生签名的私钥确实属于该组织 → 所以签名几乎无法伪造 / 发送方不能否认（non-repudiation）。

第 1 步只在“消息本身也被加密”的场景出现（⟦9618_w22_31:6(c)⟧ 背景是用非对称加密发送的消息）。如果题目的消息是明文发送、只附签名，就从第 2 步开始。

**得分表述**（引自对应 MS）
- 「The message is hashed with (the agreed hashing algorithm)」⟦9618_s22_32:7(b)(i)⟧
- 「The message digest is then encrypted with the sender’s private key to form the digital signature」⟦9618_s22_32:7(b)(i)⟧
- 「The digital signature received is decrypted with the sender’s public key to recover the message digest sent」⟦9618_w22_31:6(c)⟧
- 「The two message digests are compared」⟦9618_w22_31:6(c)⟧
- 「The digital certificate provides the public key」⟦9618_s24_31:7(b)⟧
- 「which validates the private key used to create the digital signature」⟦9618_w25_31:5(b)⟧

**易错与失分**
- 把数字签名和数字证书混用：考官报告指出这是产生签名题里的常见错误（⟦9618_s22_32:7(b)(i)⟧）。签名是发送方每条消息自己算的；证书是 CA 签发的、装着公钥的身份文件。
- 说不清两个摘要从哪来：考官报告指出，考生大多知道要比较两个摘要，但说不清一个来自签名、另一个是接收方用同一散列算法重新算的（⟦9618_w22_31:6(c)⟧）。
- 钥匙不点名：考官报告指出，过程中用到的每把钥匙都要准确指明（⟦9618_s22_32:7(b)(ii)⟧）。
- 证书题只写一半：考官报告指出，很多考生写了“证书提供公钥”，但很少再写“这把公钥用来验证该组织的私钥”（⟦9618_s24_31:7(b)⟧）；能写到“使签名几乎无法伪造”的更少（⟦9618_w25_31:5(b)⟧）。

#### 代表题精讲　⟦9618_w22_31:6(c)⟧

**在考什么**　背景：A message is encrypted using a private key and sent to an individual using asymmetric encryption. 问：Explain how a digital signature is used to verify a message when it is received. 4 分，MS 列 5 点（Max 4），第 5 点以 “…” 开头，是第 4 点的展开。

**完整作答**
1. 收到的消息连同数字签名，用接收方的私钥解密。
2. 收到的数字签名用发送方的公钥解密，恢复出发送方发来的消息摘要。
3. 对解密后的消息用约定的散列算法重新散列，得到所收消息的消息摘要。
4. 比较这两个消息摘要，
5. ……相同则消息没有被改动；不同则消息被改动过。

**与 MS 对齐**　1–5 依次对应 MS 的 5 个点，满分 4。第 5 点必须接在第 4 点后才成立；只写第 1 步之外的 2–5 也能满分。

**英文作答句**　The message together with the digital signature is decrypted using the receiver’s private key. The digital signature received is decrypted with the sender’s public key to recover the message digest sent. The decrypted message received is hashed with the agreed hashing algorithm to reproduce the message digest of the message received. The two message digests are compared; if both digests are the same the message has not been altered, and if they are different the message has been altered.

**直观**　数字签名像快递封条上的“指纹 + 火漆印”：发件人把包裹内容压成一枚指纹（摘要），再用只有自己有的印章（私钥）盖住。收件人用公开的印模（公钥）认出印章，取出指纹，再自己给包裹按一次指纹，两枚一样就说明路上没被拆过。

**下一道变式**　⟦9618_s22_32:7(b)(i)⟧　（反方向：签名怎样产生，3 分：散列 → 得到摘要 → 用发送方私钥加密摘要。）

<!-- auto:drills P3-SC-06 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| SC-01 vs SC-02 | 定义术语、比较对称与非对称 → SC-01；按步骤说两把钥匙怎样用 → SC-02 | define · differences 还是 process · explain how … uses |
| 私密消息 vs 已验证消息 | 用接收方的公钥加密、接收方私钥解密 / 用发送方的私钥加密、发送方公钥解密 | confidential · private · secure 还是 verified · prove the sender |
| SC-02 已验证消息 vs SC-06 数字签名 | 整条消息用发送方私钥加密 / 先散列成摘要，只加密摘要，接收方比较两个摘要 | message digest · hash 是否出现 |
| SC-05 vs SC-06 | 证书是什么、怎样获取、含什么 / 证书在签名中的作用（提供公钥以验证私钥） | obtain · acquire · items 还是 role · validate a digital signature |
| 数字证书 vs 数字签名 | CA 签发的身份文件，装持有者公钥 / 发送方对每条消息用私钥加密摘要得到的数据 | Certificate Authority 还是 message digest |
| 获取证书 vs SSL/TLS 握手 | 组织 ↔ CA：申请、核实、签发 / 客户端 ↔ 服务器：请求并验证证书、取公钥、商定会话密钥 | CA · acquire 还是 client-server · initiated |
| SC-04 vs CI-03 | 组成 TLS 的握手协议、记录协议 / HTTP、FTP、SMTP 等应用层协议 | TLS 是否出现 |
| 量子密码“发现”vs“防止”窃听 | 窃听会改变光子状态而被发现；不能阻止别人去测 | eavesdropping can be identified |
| SC-01 / SC-06 vs P1-SP-04 / P1-SP-05 | A2 问过程、比较、量子与证书 / AS 问加密与签名的基本概念 | P3 卷还是 P1 卷 |
