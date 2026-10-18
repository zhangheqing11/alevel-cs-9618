## SC　安全：核心概念 {#core-SC}

英文列带 ⟦⟧ 的是该题 MS 原文；标“非 MS 原句”的是标准定义（核验语料里没有可直接引用的 MS 句子），作答时以所答那题的 MS 为准。

### 加密与密钥（17.1）

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Plain text | Plain text is the original, readable data before it is encrypted.（非 MS 原句） | 加密前可以直接读懂的原始数据 | 没装进保险箱的信 | P3-SC-01 |
| Cipher text | 「Fred’s computer encrypts the document/plain text using Sheila’s public key to create cipher text」⟦9618_s24_32:4⟧ | 明文经加密算法和密钥处理后得到的、不能直接读懂的数据 | 锁进保险箱后的信 | P3-SC-01、P3-SC-02 |
| Symmetric encryption | 「Symmetric cryptography uses a single key to encrypt and decrypt messages, Asymmetric cryptography uses two」⟦9618_s23_32:5(b)⟧ | 加密和解密用同一把钥匙；这把钥匙要共享给对方 | 一把家门钥匙配给朋友 | P3-SC-01 |
| Asymmetric encryption | 「by using two different keys / a public key and a private key」⟦9618_s23_31:9(a)⟧ | 用一对配对的钥匙：一把加密，只有配对的另一把能解密 | 只能投不能取的信箱 | P3-SC-01、P3-SC-02 |
| Public key | 「The organisation makes the public key available to anyone who wishes to send them secure transmissions」⟦9618_w25_32:7(b)⟧ | 钥匙对中公开给任何人的那把 | 摆在门口谁都能拿的挂锁 | P3-SC-01、P3-SC-02 |
| Private key | 「A private key is the unpublished/secret key/never transmitted anywhere」⟦9618_w22_31:6(a)⟧ | 钥匙对中只有主人持有、从不传输的那把；与一把公钥配对 | 只在主人口袋里的钥匙 | P3-SC-01、P3-SC-02、P3-SC-06 |
| Private message（confidentiality） | 「The message to be sent is encrypted using the recipient’s public key」⟦9618_w22_31:6(b)⟧ | 用接收方的公钥加密、接收方的私钥解密，只有接收方能读 | 用对方的挂锁锁箱子 | P3-SC-02 |
| Verified message | 「The message to be sent is encrypted using the sender’s private key」⟦9618_w22_31:6(b)⟧ | 用发送方的私钥加密，任何人用发送方公钥能解开，就证明是发送方发的 | 盖了只有你有的私章 | P3-SC-02 |
| Non-repudiation | 「Non-repudiation, neither the sender or receiver can deny the transmission occurred」⟦9618_s22_31:8(a)(i)⟧ | 发送方和接收方都不能否认传输发生过 | 签收单签了名就赖不掉 | P3-SC-01、P3-SC-06 |
| Quantum cryptography | 「to produce a virtually unbreakable encryption system」⟦9618_s23_32:5(a)⟧ | 利用光子的量子性质分发密钥，安全性基于物理定律；窃听会改变光子状态而被发现 | 一碰就破的肥皂泡 | P3-SC-03 |
| Eavesdropping detection | 「Any eavesdropping can be identified (as the state will be changed)」⟦9618_s22_31:8(b)(i)⟧ | 量子密码的主要好处：有人测量光子会改变其状态，因而能发现窃听（不是阻止） | 封条被动过一眼就能看出 | P3-SC-03 |

### 协议、证书与签名（17.1）

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| SSL / TLS | 「The SSL and TLS protocols provide communications security over the internet / network」⟦9618_w21_31:8(a)⟧ | 为网络通信提供安全的协议：加密数据、认证双方、保证保密性与完整性 | 给网络对话加一层防窃听的隔音罩 | P3-SC-04 |
| Handshake | 「Every new session begins with a handshake as defined by the SSL/TLS protocols」⟦9618_s25_33:7⟧ | 会话开始时客户端与服务器交换并验证证书、取得公钥、商定算法、生成会话密钥的过程 | 先看工牌，再约暗号 | P3-SC-04 |
| Handshake protocol | 「To establish a secure and reliable connection between two devices, systems or networks」⟦9618_s25_32:10⟧ | TLS 中负责建立安全连接（相互认证、商定加密算法）的协议 | 见面时的验证与约定 | P3-SC-04 |
| Record protocol | 「Encrypts and authenticates data exchanged between a client and a server」⟦9618_s25_32:10⟧ | TLS 中负责在已建立的连接上加密、认证并传输数据的协议 | 约好暗号后的正式对话 | P3-SC-04 |
| Session key | 「The symmetric session keys are generated/defined」⟦9618_s25_33:7⟧ | 握手时为本次会话生成的对称密钥，之后的数据用它加密 | 只在这次通话里有效的暗号 | P3-SC-04 |
| Certificate Authority (CA) | 「The CA verifies the organisation’s identity」⟦9618_w22_32:6(b)⟧ | 核实申请者身份并签发数字证书的可信机构 | 签发护照的出入境管理处 | P3-SC-05 |
| Digital certificate | 「A digital certificate is an electronic/online document」⟦9618_s24_31:7(a)⟧ | 由 CA 签发、用来证明网站 / 个人 / 组织在线身份的电子文档，含持有者信息与公钥 | 盖了章的护照 | P3-SC-05、P3-SC-06 |
| Hashing algorithm | 「The message is hashed with (the agreed hashing algorithm)」⟦9618_s22_32:7(b)(i)⟧ | 把任意长度的消息算成固定长度摘要的算法；双方要用同一个 | 给包裹按指纹的方法 | P3-SC-06 |
| Message digest | 「The two message digests are compared」⟦9618_w22_31:6(c)⟧ | 消息经散列算法得到的固定长度结果；消息改动一点摘要就不同 | 包裹的指纹 | P3-SC-06 |
| Digital signature | 「The message digest is then encrypted with the sender’s private key to form the digital signature」⟦9618_s22_32:7(b)(i)⟧ | 用发送方私钥加密的消息摘要；接收方用发送方公钥解出并比较摘要，以验证发送方和消息未被改动 | 指纹 + 火漆印 | P3-SC-06 |
| Certificate’s role in signatures | 「The digital certificate provides the public key」⟦9618_s24_31:7(b)⟧ | 证书提供发送方可信的公钥，用来验证产生签名的私钥确实属于该组织 | 护照证明这枚印章是本人的 | P3-SC-06 |
