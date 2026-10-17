## SP　安全、隐私与数据完整性：核心概念 {#core-SP}

英文列带 ⟦⟧ 的是该题 MS 原文；标“非 MS 原句”的是标准定义，作答时以所答那题的 MS 为准。

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Data security | 「Security prevents against loss while privacy prevents unauthorised access」⟦9618_s22_11:3(a)⟧ | 保护数据和系统不丢失、不被损坏或篡改，丢失后能恢复 | 保险柜别被撬、文件别被烧 | P1-SP-01 |
| Data privacy | 「Ensuring data can only be accessed by / disclosed to authorised persons」⟦9618_w23_12:5(a)⟧ | 只有获得授权的人才能访问或得知数据 | 病历只给医生看 | P1-SP-01 |
| Data integrity | 「Ensuring the accuracy / completeness / consistency of data」⟦9618_w23_12:5(b)⟧ | 数据准确、完整、一致、最新 | 账本上的数字和实际一致 | P1-SP-01、P1-SP-06、P1-SP-07 |
| Malware | 「Malicious software that replicates and can delete/damage the examination papers」⟦9618_s22_11:3(b)⟧ | 为破坏、窃取或干扰而编写的恶意软件的总称（病毒、间谍软件等） | 混进电脑的坏程序 | P1-SP-02 |
| Virus | 「Malicious program/software that replicates/copies itself and deletes/alters files/data stored on a computer」⟦9618_w25_11:8(a)⟧ | 会自我复制、删除或改动文件与数据的恶意程序 | 会传染的病 | P1-SP-02 |
| Spyware | 「Malware downloaded without the user’s knowledge」⟦9618_w23_12:5(c)⟧ | 用户不知情时安装、偷偷记录操作或按键并发给第三方的恶意软件 | 藏在屋里的窃听器 | P1-SP-02 |
| Hacking | 「Illegal access in order to delete/damage the examination papers」⟦9618_s22_11:3(b)⟧ | 未经授权访问计算机系统，以窃取、删除或破坏数据 | 撬锁进屋 | P1-SP-02 |
| Phishing | 「The email pretends to be from an official body」⟦9618_w23_12:5(c)⟧ | 冒充正规机构发邮件，诱导用户点链接或交出个人信息 | 假冒银行的诈骗短信 | P1-SP-02 |
| Pharming | 「Malicious code/software installed on a computer which redirects user to a fake website to obtain personal data」⟦9618_w25_11:8(a)⟧ | 恶意代码把用户自动重定向到假网站以骗取个人数据 | 路标被人偷偷换了方向 | P1-SP-02 |
| Firewall | 「Monitors incoming and outgoing traffic and rejects any traffic that does not meet the set rules」⟦9618_w23_13:3(a)(iii)⟧ | 按设定规则（名单、IP 地址、端口）检查进出的流量，拦截不符合规则的数据 | 拿着名单的门卫 | P1-SP-03 |
| Proxy server | 「Prevents devices accessing the web server directly」⟦9618_s24_12:3(a)(i)⟧ | 介于用户与服务器之间，拦截请求、用自己的 IP 转发并过滤返回数据 | 替你去取快递的代收点 | P1-SP-03 |
| Anti-virus software | 「scans the computer for viruses and checks against a stored database of viruses」⟦9618_s23_13:6(b)⟧ | 扫描文件并与已知病毒库比对，发现后隔离或删除；病毒库要定期更新 | 拿通缉照片逐个对脸 | P1-SP-03 |
| Anti-spyware software | 「compares downloaded files to a database of known spyware and prevents the download continuing」⟦9618_s23_13:6(b)⟧ | 检测并清除间谍软件，阻止其下载 | 专门找窃听器的探测仪 | P1-SP-03 |
| Password | 「Ensures only users with the correct password can access the resources」⟦9618_w23_13:3(a)(iii)⟧ | 只有输入正确密码的用户才能访问资源；强密码混合多种字符且足够长 | 门锁的钥匙 | P1-SP-03 |
| Two-factor / multi-factor authentication | 「Two factor authentication」⟦9618_s21_12:8(b)⟧ | 登录时除密码外还要第二种凭证（生物特征、验证器 App 等） | 钥匙加指纹两道锁 | P1-SP-03 |
| Biometrics | Uses a unique physical characteristic of the user, such as a fingerprint or face, to authenticate them.（非 MS 原句） | 用指纹、人脸等身体特征认证用户 | 刷脸开门 | P1-SP-03、P1-EO-04 |
| Access rights | 「appropriate permissions for the table USER are needed to read or edit the data」⟦9618_s25_12:5(c)(i)⟧ | 给不同用户设置不同权限：无权访问、只读、读写 | 员工卡只能刷开自己部门的门 | P1-SP-03、P1-DB-08 |
| Encryption | 「Data is turned into cipher text // Data is encoded」⟦9618_s22_12:4(c)⟧ | 用算法和密钥把明文变成密文，没有解密密钥就读不懂 | 写成暗号的信 | P1-SP-04 |
| Cipher text | 「File contents are converted to cipher text」⟦9618_w24_12:4(c)⟧ | 加密后得到的、看不懂的数据 | 暗号本身 | P1-SP-04 |
| Decryption key | 「Algorithm/key is required to decode the data」⟦9618_s24_13:7(f)(ii)⟧ | 把密文还原成明文所需的密钥 | 暗号本 | P1-SP-04 |
| Digital signature | 「The sender encrypts the digest to create the digital signature」⟦9618_s25_11:7(b)⟧ | 用发送方私钥加密文档摘要得到的数据，用来证明来源真实、内容未被改动 | 盖在指纹上的私人印章 | P1-SP-05 |
| Hashing / digest | 「(email) message put through hashing algorithm to produce a digest」⟦9618_w22_12:6(a)(i)⟧ | 哈希算法把文档算成固定长度的摘要；文档改一点，摘要就变 | 文件的指纹 | P1-SP-05 |
| Private key | 「Digest encrypted with sender’s private key」⟦9618_w22_12:6(a)(i)⟧ | 只有拥有者自己持有的密钥，签名时用来加密摘要 | 只有你有的印章 | P1-SP-05 |
| Public key | 「the (digital) signature can only be decrypted with matching sender’s public key」⟦9618_w22_12:6(a)(i)⟧ | 公开给所有人的密钥，用来解开对应私钥做的签名 | 人人可用的验章器 | P1-SP-05 |
| Validation | 「validation checks that data is reasonable / sensible」⟦9618_w21_11:2(b)(i)⟧ | 计算机按规则检查输入的数据是否合理、在允许范围内 | 安检机只看合不合规定 | P1-SP-06、P1-SP-08 |
| Range check | 「range check to make sure it is between 0 and max marks」⟦9618_s22_11:4(d)⟧ | 检查数据在上下两个界限之间 | 年龄 0–120 | P1-SP-06 |
| Limit check | Checks that data is above or below one specific limit only.（非 MS 原句） | 只检查一端的界限 | 必须早于今天 | P1-SP-06 |
| Presence check | 「presence check to make sure a mark is entered」⟦9618_s22_11:4(d)⟧ | 检查字段没有留空 | 必填项的红星号 | P1-SP-06 |
| Length check | 「to make sure the data contains the correct number of characters」⟦9618_w22_12:4(c)⟧ | 检查字符个数正确 | 手机号必须 11 位 | P1-SP-06 |
| Format check | 「to make sure data is in the required format」⟦9618_w22_12:4(c)⟧ | 检查字符的组合模式正确（哪一位是字母、哪一位是数字） | 车牌号格式 | P1-SP-06 |
| Type check | 「type check to make sure an integer value is entered」⟦9618_s22_11:4(d)⟧ | 检查数据类型正确 | 分数栏不能填字母 | P1-SP-06 |
| Existence / look-up check | 「to make sure the data is already present in the system」⟦9618_w22_12:4(c)⟧ | 检查值在允许的列表中或已存在于系统里 | 下拉框只能选给出的项 | P1-SP-06 |
| Check digit | An extra digit calculated from the other digits of a code and compared when the code is entered.（非 MS 原句） | 由编码其余各位算出的附加位，输入时重算比对 | 身份证号最后一位 | P1-SP-06 |
| Verification | 「verification checks that data is the same as the original」⟦9618_w21_11:2(b)(ii)⟧ | 检查输入或传输后的数据与原件 / 发送端的一致 | 抄完再对一遍原稿 | P1-SP-07、P1-SP-08 |
| Visual check | 「Manually compare the data entered with the original (document)」⟦9618_s22_13:5(b)(i)⟧ | 录入后由人把屏幕上的数据与原始文件逐项对照 | 用眼睛核对 | P1-SP-07 |
| Double entry | 「Enter the data twice and the system compares them to see if they are the same」⟦9618_s22_13:5(b)(i)⟧ | 数据输入两次，由计算机比较是否一致 | 设密码时“再输一次” | P1-SP-07 |
| Parity check | 「a parity bit is added to each byte to make the number of 1s match the parity, odd or even」⟦9618_w25_13:7(c)⟧ | 给每个字节加一位，使 1 的个数符合约定的奇或偶；收到后检查 | 每箱货都凑成双数 | P1-SP-07 |
| Odd / even parity | 「Computer A and Computer B agree on whether to use odd or even parity」⟦9618_s24_11:5(b)⟧ | 收发双方事先约定 1 的个数为奇数还是偶数 | 事先对好暗号规则 | P1-SP-07 |
| Parity block check | 「a bit is added to each byte, but a parity byte is also set for each block」⟦9618_w25_13:7(c)⟧ | 每个字节有奇偶位，每列再算出一个奇偶字节；行列交叉可定位出错的位 | 横竖两张对账表 | P1-SP-07 |
| Checksum | 「checksum value is calculated from the data before transmission」⟦9618_w22_12:4(b)⟧ | 发送前由数据算出一个值随数据发送，接收方重算比较，不同即出错 | 快递单上的“共 12 件” | P1-SP-07 |
