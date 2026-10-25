## CI　通信与互联网技术 {#ch-CI}

<!-- auto:chapter-stats -->

### 核心思想

CI 对应考纲 14.1 协议、14.2 电路交换与分组交换，全是文字题，几乎每卷一道 4–8 分。两块：

1. **协议与 TCP/IP 栈**（CI-01 至 CI-04）：先懂“为什么要协议”（统一规则，不同厂商 / 平台的设备才能通信），再懂“栈”（四层，每层只和相邻层打交道；发送时自上而下逐层加报头，接收时自下而上），然后才是“每层干什么”（CI-02）和“应用层有哪些协议”（CI-03、CI-04 BitTorrent）。**CI-01 与 CI-02 的分界最常考**：题目写“Do not describe the function of individual layers”时只讲层与层的关系。
2. **交换方式**（CI-05 至 CI-07）：电路交换 = 先建一条专用线路、独占整个带宽、按序到达；分组交换 = 拆包、每包带报头独立选路、到达后重组、丢了重发。只问一种时不要拿另一种来比（考官报告反复提醒）；两种都问时每句话都要“circuit … whereas packet …”成对写。

**TCP/IP 四层速查**（自上而下，顺序必考）

| 层 | 一句话功能 | 关键词 |
|:--|:--|:--|
| Application | 与用户交互，提供应用使用的协议 | HTTP(S)、FTP、POP3、IMAP、SMTP、BitTorrent |
| Transport | 端到端：把数据分成段 / 包、加序号、流量控制、出错重传 | segmentation、sequence number、end-to-end、error-free |
| Internet | 加源 / 目的 IP 地址，选路，把包交给链路层 | IP address、route、datagram |
| Link | 在直接相连的设备之间传送：成帧、MAC 地址、接入物理介质 | frame、MAC address、next hop |

### 题型树
<!-- auto:type-tree -->

### P3-CI-01　协议的必要性与协议栈　{#P3-CI-01}

<!-- auto:stats P3-CI-01 -->

**考法**　①解释为什么计算机通信需要协议（2 分）；②描述 TCP/IP 栈的各层怎样互相作用（4 分）；③描述一条消息经互联网从一台主机发到另一台时 TCP/IP 怎样被应用，题目明说不要描述单层功能（4 分）；④用给定词表补全关于协议栈的段落（3–4 分）。

**识别信号**　Explain why a protocol is used / Outline why protocols are essential for communication between computers；Describe how the layers of the TCP/IP protocol stack interact with each other；Describe how the TCP/IP protocol suite is applied when a message is sent through the internet from one host to another；Do not describe the function of individual layers；Complete the following paragraph … Some words are not used。

**解题思路**
1. **为什么要协议**：协议定下通信的**标准规则**；有了统一规则，**不同厂商 / 平台**的设备才能兼容、通信；双方用的协议不同就无法正常通信。
2. **栈的结构**：协议的实现可以看成分层的栈（TCP/IP 四层）；每层有自己的功能，**只能与上下相邻的层**交换数据（层与层之间有接口）；层间的交互由已安装的软件完成。
3. **一条消息怎样走**：发送方用户在最高层（应用层）交互 → 消息从应用层**逐层向下**传到链路层，每经过一层加上该层的报头 → 链路层直接与网络（硬件）交互，把数据发出去 → 接收方从链路层**逐层向上**传到应用层，交给用户。
4. 题目写了“Do not describe the function of individual layers”：只写第 2、3 条，不要写“传输层负责分包”之类。
5. 选词填空：先读完整段，再按“协议 → 栈 → 层 → 相邻 → 最高层是应用层、最低层是链路层”这条主线填；词表里有干扰词（seven、BitTorrent、circuit switching）。

**得分表述**（引自对应 MS）
- 「Protocols set a standard for communication」⟦9618_w22_32:3(a)⟧
- 「Protocols enable communication/compatibility between devices from different manufacturers/platforms」⟦9618_w22_32:3(a)⟧
- 「Each layer can only accept input from the next higher layer or the next lower layer」⟦9618_w24_31:4⟧
- 「Data is added to the headers as the frames/packets pass through the layers」⟦9618_w24_31:4⟧
- 「The message when sent passes from the top layer/application layer to the bottom layer/link layer」⟦9618_s25_32:3(b)⟧
- 「The link layer interfaces directly with the network and sends/receives the message」⟦9618_s25_32:3(b)⟧

**易错与失分**
- 题目要求描述层与层的交互，却逐层写功能：考官报告指出很多考生这样误读题目（⟦9618_w24_31:4⟧、⟦9618_s25_32:3(b)⟧ 的考官报告），这些句子不得分。
- “为什么要协议”只写一句“so computers can communicate”：考官报告指出很少有人展开（⟦9618_w22_32:3(a)⟧ 的考官报告）；第二分要写出“不同厂商 / 平台的设备之间”。
- 把栈的方向写反：发送是从应用层到链路层（自上而下），接收是从链路层到应用层。
- 选词填空写了词表以外的词，或把 layer 与 protocol 填反。考官报告指出这类段落题考生普遍觉得难（⟦9618_w23_32:4⟧ 的考官报告）。

#### 代表题精讲　⟦9618_s25_32:3(b)⟧

**在考什么**　Describe how the TCP/IP protocol suite is applied when a message is sent through the internet from one host to another. Do not describe the function of individual layers of the TCP/IP protocol suite. 4 分，MS 六点 Max 4。

**完整作答**
1. TCP/IP 协议族可以看成一个栈里的若干层。
2. 每一层只能从紧邻的上一层或下一层接收输入。
3. 发送方的用户在最高层（应用层）与之交互，发送消息。
4. 发送时，消息从最高层（应用层）逐层向下传到最低层（链路层）。
5. 链路层直接与网络交互，把消息发出去；在接收方由链路层收到。
6. 接收时，消息从最低层（链路层）逐层向上传到最高层（应用层），交给接收方用户。

**与 MS 对齐**　1 → MP1，2 → MP2，3 → MP3，4 → MP4，5 → MP6，6 → MP5。六点都是独立得分点，任 4 点满分；全写出来是保险。注意每句都没有讲某一层的具体功能——这正是题目的限制。

**英文作答句**　The TCP/IP suite can be viewed as layers within a stack. Each layer can only accept input from the next higher or the next lower layer. The sender interfaces with the top layer, the Application layer, to send the message. When sent, the message passes from the Application layer down to the bottom layer, the Link layer, which interfaces directly with the network and sends the message. When received, the message passes from the Link layer up to the Application layer.

**直观**　像寄快递：你只和最上面的前台打交道（应用层）；包裹一层层往下交接，每一层贴一张自己的标签（报头）；最底层的车队真正上路（链路层）；到了对方城市再一层层往上拆标签，最后送到收件人手里。

**迁移与卡点**
- **卡点**：题目写了 Do not describe the function of individual layers，一个层的功能都不能写——写了不得分还浪费时间。答案全是“栈、相邻层、报头、自上而下 / 自下而上、链路层接硬件、应用层接用户”。
- **考官在换什么**：问为什么要协议（标准 + 不同厂商）、问层怎样交互、问一条消息怎样走、选词填空。都是同一幅“栈”图。
- **从代表题到变式**：代表题按消息的路径写；变式问层与层怎样交互——同一组句子换个组织方式：只和相邻层交换、每层加报头、交互由软件完成、用户在应用层、硬件在链路层。搬过去的是整套句子；要换的是组织顺序（从“路径”变成“关系”）。
- **反例**：逐层写功能；发送与接收的方向写反。

**下一道变式**　⟦9618_w24_31:4⟧　（问“层与层怎样交互”：除了相邻层、报头，还可写交互由软件完成、用户在应用层、硬件在链路层。）

<!-- auto:drills P3-CI-01 -->

### P3-CI-02　TCP/IP 四层的顺序与功能　{#P3-CI-02}

<!-- auto:stats P3-CI-02 -->

**考法**　①把四层排成正确顺序或补全栈图（2 分）；②描述某一层的功能 / 目的（2–3 分）；③描述两层（各 Max 3、合计 5 分，最常见：传输层 + 网际层、应用层 + 传输层、网际层 + 链路层）；④说出另外两层并各描述功能（4 分）；⑤层与描述连线（4 分）。

**识别信号**　Complete the diagram to show the correct order for these layers；Describe the function / purpose of the Transport / Internet / Link / Application layer；Outline the functions of the Transport and Internet layers；Identify two (other) layers of the TCP/IP protocol suite；Draw one line to connect each TCP/IP layer to its most appropriate description。

**解题思路**
1. **顺序**：自上而下 Application → Transport → Internet → Link。记法：“用户在上、网线在下”。
2. **每层按“它对数据做了什么”写**，不要只写“把数据交给下一层”：
   - **Application**：与用户交互 / 为应用提供服务；定义应用交换数据所用的协议（HTTP、FTP、SMTP …）；可提供加密、认证等安全机制。
   - **Transport**：负责从源主机到目的主机的端到端交付；把数据分成包 / 段；在报头加序号；流量控制；保证无差错按序到达、丢包重传。
   - **Internet**：确定目标网络与主机；给每个包加上源 / 目的 IP 地址；为每个包独立选最佳路由；把包交给链路层。
   - **Link**：在直接相连的两台设备之间传送（下一跳）；把数据报封装成帧；把 IP 地址映射到 MAC 地址；保证遵守正确的网络协议；差错检查与重发。
3. 两层一起问、每层 Max 3、总分 5：每层写 3 点（多写一点保险），不要一边写 5 点另一边空着。
4. “Identify two **other** layers”：题干已给的那层不能再写。

**得分表述**（引自对应 MS）
- 「The Transport Layer breaks data into manageable packets / performs segmentation」⟦9618_w22_31:2⟧
- 「It sequences the packets // adds data to the packet header // adds a packet header」⟦9618_w22_31:2⟧
- 「It routes the packets independently through the optimum route」⟦9618_w22_31:2⟧
- 「It addresses packets with their source and destination IP addresses」⟦9618_w22_31:2⟧
- 「To format datagrams into frames for transmission」⟦9618_s25_33:4(a)⟧
- 「It ensures data arrives error free // It retransmits packets if lost」⟦9618_s24_31:2(b)⟧

**易错与失分**
- 说得不具体：考官报告举例，网际层写“it uses IP addresses”不够，要写“source and destination IP addresses are added to the packet header”（⟦9618_w22_31:2⟧ 的考官报告）。
- 只写“它把数据传给哪一层”：考官报告指出得分高的答案讲的是该层为发送 / 接收**准备数据**的作用，而不是它把数据传给哪一层（⟦9618_s25_31:3(a)⟧、⟦9618_s25_33:4(a)⟧ 的考官报告）。
- 应用层功能写不满三点：考官报告指出很少有人写到三分（⟦9618_w24_32:5(b)⟧ 的考官报告）——除了“与用户交互”，还要写“提供所有交换数据的程序的接入”“定义应用使用的协议”“与传输层传递数据”。
- 把 Internet 层叫成 Network 层：MS 常写 Internet / Network 都接受（⟦9618_w22_32:3(b)⟧），但 Link 层不能与 Internet 层混淆。

#### 代表题精讲　⟦9618_w22_31:2⟧

**在考什么**　Outline the functions of the Transport and Internet layers of the TCP/IP protocol suite. 5 分：传输层 MP1–MP5 Max 3，网际层 MP6–MP10 Max 3。

**完整作答**
- Transport layer：
  1. 把数据分成便于处理的包（分段）。
  2. 给包编序号（在包的报头里加入数据）。
  3. 控制包的流量；处理丢包或损坏的包，对完整无误的包发确认。
  4. 从应用层接收数据，把包送到网际层。
- Internet layer：
  1. 确定目标网络与主机。
  2. 给每个包加上源 IP 地址和目的 IP 地址。
  3. 为每个包独立地选择最佳路由。
  4. 把包送到链路层。

**与 MS 对齐**　传输层 1 → MP1，2 → MP2，3 → MP4、MP5，4 → MP3（取 3）；网际层 1 → MP6，2 → MP9，3 → MP8，4 → MP7（取 3）。两边合计封顶 5 分，所以每边至少写 3 个不同的点。

**英文作答句**　Transport layer: it breaks data into manageable packets; it sequences the packets by adding a packet header; it controls the flow of packets and handles packet loss or corruption; it sends the packets to the Internet layer. Internet layer: it identifies the intended network and host; it addresses packets with their source and destination IP addresses; it routes the packets independently through the optimum route; it transmits the packets to the Link layer.

**直观**　传输层是“打包员”：把货拆成小箱、编号、负责最终一箱不少地送到；网际层是“调度员”：给每箱贴上收发地址、决定走哪条路；链路层是“司机”：只管开到下一站。

**迁移与卡点**
- **卡点**：每层要写“它对数据做了什么”，不是“把数据交给下一层”——传输层分段、编号、流控、重传；网际层加源 / 目的 IP、独立选路；链路层成帧、MAC 地址、直连设备之间。两层一起问、各 Max 3、共 5，每边至少三点。
- **考官在换什么**：问哪两层（传输 + 网际、应用 + 传输、网际 + 链路）、顺序题、连线题、“另外两层”。四层各有三四句固定的话。
- **从代表题到变式**：代表题是传输 + 网际；变式是网际 + 链路——网际层那三句照搬，链路层换成帧、MAC 地址、下一跳、差错检查。搬过去的是“每层三句动作”；要换的是哪两层。
- **反例**：网际层只写 it uses IP addresses（不够具体）；把 Internet 层和 Link 层混淆。

**下一道变式**　⟦9618_s25_33:4(a)⟧　（换成网际层 + 链路层，各 Max 3、共 5 分；链路层要写成帧、MAC 地址、直连设备之间。）

<!-- auto:drills P3-CI-02 -->

### P3-CI-03　应用层协议：HTTP、FTP、POP3、IMAP、SMTP　{#P3-CI-03}

<!-- auto:stats P3-CI-03 -->

**考法**　①说出并描述应用层的两三个协议（每个“名称 1 分 + 描述 1 分”，4 或 6 分）；②收发电子邮件各用什么协议（2 分）；③描述 IMAP 或说出 HTTP、IMAP 的用途（2 分）；④协议与用途连线（4 分）。

**识别信号**　Identify two protocols used by this layer. Describe the use of each protocol；Name and describe two protocols used by the Application Layer；Identify and describe three protocols；State the names of two different protocols associated with the sending and receiving of emails；Describe the purpose of the IMAP protocol；Draw one line to connect each protocol to its most appropriate use。

**解题思路**
1. 选自己最有把握的协议，每个写成“**名称 + 做什么 + 在哪里之间**”：
   - **HTTP / HTTPS**：在联网设备之间传输网页 / 超文本文档（HTTPS 为安全版本）。
   - **FTP**：在网络上从一处向另一处上传、下载、传输文件。
   - **SMTP**：发送电子邮件（从电脑到邮件服务器、在邮件服务器之间）；push 协议。
   - **POP3**：从邮件服务器把邮件取回 / 下载到电脑；pull 协议。
   - **IMAP**：在任何设备上访问 / 阅读邮件而**不把邮件从服务器上删除**，各设备同步；pull 协议。
   - **BitTorrent**：点对点（peer-to-peer）文件共享。
2. 收邮件写 POP3 或 IMAP，发邮件写 SMTP，别弄反。
3. IMAP 与 POP3 都是“收邮件”，区分 IMAP 要写出“邮件留在服务器上、多设备同步”。
4. 连线题：先连有把握的（HTTP ↔ hypertext；SMTP ↔ sending；IMAP ↔ retrieving from a mail server；BitTorrent ↔ peer-to-peer），剩下的是干扰项（如 map MAC addresses onto IP addresses，那是链路层的事）。

**得分表述**（引自对应 MS）
- 「a protocol/secure protocol used to transfer hypermedia documents / web pages / (data) files between networked devices」⟦9618_w25_33:4⟧
- 「a protocol to download, upload and transfer files from one location to another on a network」⟦9618_w25_33:4⟧
- 「a protocol used to send emails between mail servers // a protocol used to send emails from a computer to a mail server」⟦9618_w25_33:4⟧
- 「allows users to access/read their emails from any device without removing the message from the mail server // synchronises emails on any device」⟦9618_w25_32:3(a)⟧
- 「Push protocol / for sending / uploading emails」⟦9618_w24_32:5(a)⟧

**易错与失分**
- 描述只是把缩写展开：考官报告指出“FTP 是用来传文件的协议”几乎只是复述 F T P 三个字母，要加上“… from one location to another on a network”（⟦9618_w25_33:4⟧ 的考官报告）；“SMTP is used to send emails”同样不够（⟦9618_w25_31:3(b)⟧ 的考官报告）。
- IMAP 的描述写得太泛、对 POP3 也成立：考官报告指出这样不给分，要写“synchronises emails on any device”之类 IMAP 独有的特点（⟦9618_w25_32:3(a)⟧ 的考官报告）。
- 把 IMAP 说成发送邮件的协议（⟦9618_w22_32:3(c)⟧ 的考官报告点名）。
- 题干已给 POP3（“two **other** protocols”）还写 POP3。

#### 代表题精讲　⟦9618_w25_33:4⟧

**在考什么**　Identify and describe three protocols that are used in the Application Layer of the TCP/IP protocol suite. 6 分：每个协议名称 1 分 + 对应描述 1 分，MS 列了六个协议任选三个。

**完整作答**
1. HTTPS：一种安全协议，在联网设备之间传输超媒体文档 / 网页。
2. FTP：在网络上把文件从一处下载、上传、传输到另一处。
3. SMTP：把电子邮件从电脑发送到邮件服务器，以及在邮件服务器之间发送。

**与 MS 对齐**　三个名称各 1 分（HTTP/S、FTP、SMTP 都在 MS 的 Three from 列表里）；三条描述分别对应「a protocol/secure protocol used to transfer hypermedia documents / web pages / (data) files between networked devices」⟦9618_w25_33:4⟧、「a protocol to download, upload and transfer files from one location to another on a network」⟦9618_w25_33:4⟧、「a protocol used to send emails between mail servers // a protocol used to send emails from a computer to a mail server」⟦9618_w25_33:4⟧。描述必须与名称对应，写错名称时描述分也拿不到。

**英文作答句**　HTTPS: a secure protocol used to transfer hypermedia documents / web pages between networked devices. FTP: a protocol to download, upload and transfer files from one location to another on a network. SMTP: a protocol used to send emails from a computer to a mail server and between mail servers.

**直观**　应用层协议是各种“窗口”的办事规则：网页窗口（HTTP）、文件窗口（FTP）、寄信窗口（SMTP）、取信窗口（POP3 取走、IMAP 只看不拿走）。

**迁移与卡点**
- **卡点**：描述不能只是把缩写展开（“FTP 用来传文件”不够）——要写“在哪里之间、做什么”：from one location to another on a network；SMTP 从电脑到邮件服务器、服务器之间；IMAP 的独有点是“邮件留在服务器、多设备同步”。
- **考官在换什么**：问几个协议、指定还是自选、连线、只问某一个（IMAP、HTTP）。每个都是“名称 1 分 + 描述 1 分”。
- **从代表题到变式**：代表题三选三自选；变式只问 IMAP 的用途——取邮件（pull）、从邮件服务器、保持服务器与设备同步，三点取二。搬过去的是“名称 + 做什么 + 在哪之间”；要换的是把 IMAP 和 POP3 区分开的那一句。
- **反例**：IMAP 写成发送邮件；题干已给 POP3 还写 POP3。

**下一道变式**　⟦9618_w22_32:3(c)⟧　（只问 IMAP 的用途，2 分：取邮件 / pull、从邮件服务器、保持服务器与客户端同步，三点取二。）

<!-- auto:drills P3-CI-03 -->

### P3-CI-04　BitTorrent 点对点文件共享　{#P3-CI-04}

<!-- auto:stats P3-CI-04 -->

**考法**　①描述用 BitTorrent 共享文件的过程（4 分，MS 十点 Max 4）；②解释“BitTorrent 提供点对点文件共享”这句话（3 分）。核验语料 2 次，过程固定，按步骤背。

**识别信号**　Describe how files are shared using the BitTorrent protocol；Explain the meaning of the phrase: BitTorrent protocol provides peer-to-peer file sharing。

**解题思路**　按时间顺序写，一步一句：
1. 文件在**点对点**网络上共享：用户直接互相共享，计算机都是 peer，没有中央服务器，地位平等。
2. 一个 peer 先做一个很小的 **torrent 文件**（描述文件），里面是要共享文件的元数据；最初整个文件至少在一个 peer 上。
3. 文件被分成大小相等的**块**（pieces）。
4. 想下载的 peer 先拿到 torrent 文件，连接 **tracker**；tracker 像服务器一样，掌握所有已连接计算机（**swarm**）的信息。
5. 每个 peer 同时从多个 peer 下载不同的块，直到整个文件下载完；每收到一块，它就成为这一块的来源（边下边传）。
6. 拥有完整文件并继续共享的 peer 叫 **seed**。

**得分表述**（引自对应 MS）
- 「Files are shared over a peer-to-peer network」⟦9618_w25_32:3(b)⟧
- 「The file is broken into equal sized pieces」⟦9618_w25_32:3(b)⟧
- 「Other peers who wish to download the file first obtain the torrent (descriptor file) and connect to a tracker」⟦9618_w25_32:3(b)⟧
- 「As each peer receives a piece of the file, they become a source for that piece of the file」⟦9618_w25_32:3(b)⟧
- 「Users share files directly with each other // the users’ computers are acting as peers」⟦9618_s24_32:2(c)⟧

**易错与失分**
- 把 seed 说成“下载了一部分并在共享的 peer”：考官报告指出 seed 是已下载**完整**文件并在共享的 peer（⟦9618_w25_32:3(b)⟧ 的考官报告）。
- 大谈 leech：考官报告指出 leech 与“文件怎样共享”无关（⟦9618_w25_32:3(b)⟧ 的考官报告）。
- 只写“peer-to-peer”一个词：考官报告指出拿高分的考生按步骤系统地写出了“先让文件可共享，再怎样共享”（⟦9618_w25_32:3(b)⟧ 的考官报告）。

#### 代表题精讲　⟦9618_w25_32:3(b)⟧

**在考什么**　Describe how files are shared using the BitTorrent protocol. 4 分，MS 十点 Max 4。

**完整作答**
1. 文件在点对点网络上共享。
2. 一个 peer 先创建一个小文件——torrent（描述文件），里面是要共享文件的元数据；最初整个文件至少放在一个 peer 上。
3. 文件被分成大小相等的块。
4. 想下载的 peer 先取得 torrent 文件并连接 tracker；tracker 像服务器，保存着连接到它的所有计算机（swarm）的信息。
5. 每个 peer 从其他 peer 下载文件的各个块，直到整个文件下载完；每收到一块，它就成为这一块的来源。
6. 已有完整文件并继续共享的 peer 是 seed。

**与 MS 对齐**　1 → MP1；2 → MP2、MP3、MP4；3 → MP5；4 → MP6、MP7；5 → MP8、MP9；6 → MP10。远超 4 个独立点，挑任意四步写清楚即可满分；按顺序写不容易漏。

**英文作答句**　Files are shared over a peer-to-peer network. A peer first creates a small torrent descriptor file, which contains metadata about the file to be shared; the whole file must initially be on at least one peer. The file is broken into equal sized pieces. Peers who wish to download the file obtain the torrent file and connect to a tracker, which holds data about all the computers in the swarm. Each peer downloads pieces of the file from other peers until it has the entire file, and as it receives each piece it becomes a source for that piece. A peer with the complete file that is sharing it is a seed.

**直观**　一大本书拆成很多页，大家互相复印：你从张三那里拿第 3 页、从李四那里拿第 7 页，同时把已有的页借给别人；名单管理员（tracker）只告诉你谁手里有书，不负责传书。

**下一道变式**　⟦9618_s24_32:2(c)⟧　（解释“peer-to-peer file sharing”这句话：成千上万用户经互联网直接互传、不用中央服务器、地位平等。）

<!-- auto:drills P3-CI-04 -->

### P3-CI-05　电路交换　{#P3-CI-05}

<!-- auto:stats P3-CI-05 -->

**考法**　①描述电路交换（3 分）；②给出好处与缺点（各 1 或各 2，2–4 分）；③说出在什么场合适用并给理由（2 分）。只问电路交换一种。

**识别信号**　Describe circuit switching as a method of data transmission；Give / State two benefits and two drawbacks of circuit switching；State, with a reason, where it would be appropriate to use circuit switching。

**解题思路**
1. **描述**按时间顺序：需要一条**专用**线路 / 信道 → 传输开始**前**先建立好 → 整个传输期间一直保持，结束后拆除 → 数据沿**同一路线**连续流动（通常双向）。
2. **好处**（写成“好处”，不是“特点”）：整个带宽可用 → 传输速率稳定、高；数据按发送顺序到达 → 不需要重组；适合长时间连续传输、实时通信；数据都走同一条路 → 不易丢失。
3. **缺点**：建立连接要时间；专用线路被占着时别的数据不能用（即使空闲）→ 带宽浪费；线路出故障没有备用路线；只走一条路 → 易被截获，安全性较低。
4. **适用场合**：需要整段带宽、需要一直保持专用通路的实时通信——普通语音电话、视频流、专用数据网络。理由与场合各一分。
5. 只问电路交换时**不要**写“比分组交换更 …”。

**得分表述**（引自对应 MS）
- 「A dedicated circuit / channel is required」⟦9618_w24_31:3(a)⟧
- 「The circuit is established before the transmission begins」⟦9618_w24_31:3(a)⟧
- 「The circuit lasts for the whole of the transmission // The circuit is closed at the end of the transmission」⟦9618_w24_31:3(a)⟧
- 「Steady/high rate of transmission because the whole of the bandwidth is available」⟦9618_s25_32:4⟧
- 「Delays due to dedicated connection required to be set up/established before transmission can begin」⟦9618_s25_32:4⟧
- 「There are no alternative routes if there is a failure or fault on the line」⟦9618_s25_32:4⟧

**易错与失分**
- 拿分组交换来比较：考官报告指出只问电路交换时，不去和其他传输方式比较的考生得分最高（⟦9618_s25_32:4⟧、⟦9618_s23_31:5(b)⟧ 的考官报告）。
- 描述只写“dedicated channel set up before transmission”：考官报告指出再加上“线路在整个传输期间保持”才拿满三分（⟦9618_w24_31:3(a)⟧ 的考官报告）。
- 好处与缺点写成同一件事的正反面（“whole bandwidth is available” 与 “bandwidth cannot be shared”）——两条都可能在 MS 里，但写之前确认它们是 MS 列出的两个不同点。

#### 代表题精讲　⟦9618_w24_31:3(a)⟧

**在考什么**　Describe circuit switching as a method of data transmission. 3 分，MS 五点 Max 3。

**完整作答**
1. 需要一条专用的电路 / 信道。
2. 在传输开始之前先建立这条电路。
3. 电路在整个传输期间保持，传输结束时关闭。
4. 数据以连续的流沿同一条路线传送。
5. 传输通常是双向的。

**与 MS 对齐**　1–5 分别对应 MP1–MP5，任 3 点满分。第 3 句 MS 用 `//` 给了两种说法（lasts for the whole of the transmission // closed at the end），是同一点，只算一分。

**英文作答句**　A dedicated circuit / channel is required. The circuit is established before the transmission begins and lasts for the whole of the transmission; it is closed at the end. Data travels in a continuous stream along the same route, and transmission is usually bidirectional.

**直观**　像老式电话：先拨号接通一条线，通话期间这条线只归你俩，挂断才释放；说的话按顺序原样到达。

**下一道变式**　⟦9618_s25_32:4⟧　（两个好处、两个缺点，各 Max 2；只写电路交换本身，不比较。）

<!-- auto:drills P3-CI-05 -->

### P3-CI-06　分组交换与路由器　{#P3-CI-06}

<!-- auto:stats P3-CI-06 -->

**考法**　①描述分组交换怎样在网络 / 互联网上传消息（3–4 分，有时说明不要写检查与重发）；②给出好处与缺点（4 分）；③两个适用场合（2 分）；④分组交换怎样保证收到完整的消息（2 × 2 分）；⑤路由器在分组交换中的作用（3–4 分）。

**识别信号**　Describe / Explain how packet switching is used to transmit / pass messages across a network / the internet；State two benefits and two drawbacks of packet switching；State two examples of where it would be appropriate to use packet switching；Describe two ways in which packet switching ensures a complete message is received；Describe the function of a router in packet switching。

**解题思路**
1. **过程**（按顺序）：消息被分成大小相等的小块——包 → 每个包加报头，含源 / 目的 IP 地址、包序号 → 每个包**独立**发送，可走不同路线 → 路由由路由表 / 拥塞情况决定，走最佳路线 → 包通常乱序到达 → 在目的地按序号重组成完整消息 → 缺失或损坏的包请求重发。
2. **保证完整**（每种方法 2 分 = 做法 + 结果）：到达时检查 → 损坏或没到就发重发请求；包可走不同路线 → 一条路堵了就改走别的路；跳数超限的包被丢弃 → 引发重发请求。
3. **好处**：可绕开故障线路重新选路、丢包可单独重发 → 更可能完整到达；带宽可被多条消息共享；包走不同路线 → 较安全；传输速率可以很高。**缺点**：重组 / 重发 / 共享带宽带来时间延迟；需要复杂的算法与协议；需要大量内存处理大量数据；不适合实时传输。
4. **路由器**：读包报头里的**目的 IP 地址** → 查**路由表**（可用跳、网关、相邻路由器、线路状态）→ 决定**下一跳** / 最佳路线并把包发出 → 管理跳数计数器（每过一个路由器减 1）。
5. **适用场合**：互联网上不需要实时的大文件、邮件、短信、文档、VoIP；需要绕开故障线路时；不需要占用整个带宽时。

**得分表述**（引自对应 MS）
- 「The data to be transmitted is divided into equal sized packets」⟦9618_w24_32:1(a)⟧
- 「… such as source/destination IP addresses, packet number, etc」⟦9618_w24_32:1(a)⟧
- 「The packets are reassembled in the correct order at the destination // The packets are re-ordered using the sequence number/the header」⟦9618_w24_32:1(a)⟧
- 「The router reads the IP address of the destination from the packet header」⟦9618_s25_33:4(b)⟧
- 「The router determines the next hop / optimum route. // The router sends the packet on its next hop」⟦9618_s25_33:4(b)⟧
- 「Bandwidth can be shared allowing packets from different messages to share the same path」⟦9618_w24_32:1(b)⟧

**易错与失分**
- 好处 / 缺点写成单纯的事实：考官报告指出“packets travel by different routes”只是能回答 1(a) 的事实，要写成“packets are more likely to arrive because if one is lost it can be retransmitted”这样的好处（⟦9618_w24_32:1(b)⟧ 的考官报告）。
- 描述题里写好处与缺点，或和电路交换混淆：考官报告点名这两种错误（⟦9618_s25_31:3(b)⟧ 的考官报告）。
- 题目说“Do not include checking for completeness and resending packets”时还写重发——那一分没有。
- 路由器只写“connects to the internet / helps packets find the destination”：考官报告指出这种泛泛的说法不够具体（⟦9618_w21_31:6(b)⟧ 的考官报告），要写读目的 IP、查路由表、定下一跳。
- “保证完整”每种方法只写了做法、没写结果（或反之）：MS 是 2 × 2，每种方法两分。

#### 代表题精讲　⟦9618_w24_32:1(a)⟧

**在考什么**　Describe how packet switching is used to transmit messages across a network. 3 分，MS 九点 Max 3。

**完整作答**
1. 要传输的数据被分成大小相等的包。
2. 每个包加上报头，报头里有关键信息，如源 / 目的 IP 地址、包序号。
3. 各个包独立传送，可能经不同路线到达目的地。
4. 路线由路由表决定，按拥塞情况选最佳路线。
5. 包通常乱序到达，在目的地按序号重新排好、组装成原消息；缺失或损坏的包会被要求重发。

**与 MS 对齐**　1 → MP1；2 → MP2 + MP3（报头 + 报头内容，是两个点）；3 → MP4 + MP5；4 → MP6；5 → MP7、MP8、MP9。只要 3 点，前两句就已经有 MP1、MP2、MP3，后面是保险。

**英文作答句**　The data to be transmitted is divided into equal sized packets. A packet header is attached to each packet containing key information such as the source and destination IP addresses and the packet number. Packets are transmitted independently and may travel through different routes, determined using routing tables. The packets usually arrive out of order and are reassembled in the correct order at the destination using the sequence numbers; missing or corrupted packets are re-sent.

**直观**　把一封长信拆成编了号的明信片，每张都写上收发地址，各自投进邮筒、各走各的路；收件人按编号排好再读，少了哪张就请对方再寄。

**下一道变式**　⟦9618_s25_33:4(b)⟧　（路由器在分组交换中的作用：读目的 IP → 查路由表 → 定下一跳 → 跳数减 1。）

<!-- auto:drills P3-CI-06 -->

### P3-CI-07　电路交换与分组交换的比较　{#P3-CI-07}

<!-- auto:stats P3-CI-07 -->

**考法**　同一小问里两种交换都考：①分别描述并各给一个不同的优点和缺点（8 分）；②写出两者的区别（2 或 4 个）；③各给一个好处（2 分）。

**识别信号**　Describe both methods of data transmission. Include a different advantage and disadvantage for each method；Give four differences / Identify two differences between circuit switching and packet switching；Identify one benefit of circuit switching and one benefit of packet switching。

**解题思路**
1. **区别要成对写**：一句话里同时说两边——“In circuit switching …, whereas in packet switching …”。常用的区别维度：

   | 维度 | 电路交换 | 分组交换 |
   |:--|:--|:--|
   | 连接 | 先建立专用线路才能传 | 不需要专用线路，直接开始传 |
   | 数据形式 | 消息完整、连续的流 | 分成包 |
   | 路线 | 全部走同一路线 | 各包可走不同路线 |
   | 到达顺序 | 按发送顺序到达 | 可能乱序，到达后重组 |
   | 带宽 | 占用整个带宽 | 与其他用户共享带宽 |
   | 出错 | 出错则通信中止 / 整个重传 | 单个包可以重发 |

2. **“各给一个不同的优点和缺点”**：同一种方式的优点和缺点要是两件不同的事，不要把优点倒过来当缺点写（例如电路交换优点写“独占带宽、速率稳定”，缺点又写“带宽不能与人共享”，读起来是同一件事的两面）。拿不准时用该题 MS 列出的那几条。
3. **“一个好处”**要写成好处（带“所以 / 因此”），不要写成事实（“data is sent as a continuous stream”是事实，加上“so no time is wasted reordering”才是好处）。

**得分表述**（引自对应 MS）
- 「Circuit switching requires a dedicated line to be connected before the data transfer takes place, in packet switching, data transfer commences directly/ straight away」⟦9618_w25_32:4(b)⟧
- 「In circuit switching each data unit follows the same route, but in packet switching, packets can follow any route」⟦9618_w25_32:4(b)⟧
- 「Circuit switching uses the whole bandwidth of the channel used, packet switching can share bandwidth」⟦9618_s23_32:7(b)⟧
- 「Advantage – data /frames arrive in order and do not need to be reassembled」⟦9618_s22_31:3⟧
- 「Disadvantage – time taken to reassemble packets at the destination」⟦9618_s22_31:3⟧

**易错与失分**
- 区别只写一边：考官报告举例，“circuit switching uses the whole bandwidth and packet switching does not”不够，要写“bandwidth can be shared in packet switching”（⟦9618_w25_32:4(b)⟧ 的考官报告）。
- 四个区别里有两个是同一区别的换说法：考官报告指出写出清楚、互不重复的区别才得高分（⟦9618_s23_32:7(b)⟧ 的考官报告）。
- 把优点倒过来当缺点写：考官报告点名这一常见错误（⟦9618_s22_31:3⟧ 的考官报告）。
- 好处写成事实：考官报告指出只陈述特点不给分（⟦9618_w25_32:4(a)⟧ 的考官报告）。

#### 代表题精讲　⟦9618_s22_31:3⟧

**在考什么**　Data can be sent over networks using either circuit switching or packet switching. Describe both methods of data transmission. Include a different advantage and disadvantage for each method. 8 分：电路交换 Max 4（描述两点 + 优点 + 缺点），分组交换 Max 4（同样结构）。讲解时请对照原卷 QP p.6 的作答格式（每种方式下分描述、Advantage、Disadvantage 三栏）。

**完整作答**
- Circuit switching
  - 描述：使用一条专用电路；传输开始前先建立电路，传输结束后释放；数据使用整个带宽，全部走同一路线。
  - Advantage：数据 / 帧按顺序到达，不需要重组。
  - Disadvantage：电路空闲时别人也不能使用这条电路。
- Packet switching
  - 描述：数据被分成包；每个包有自己的路由；包的路由取决于网络拥塞情况；包可能不按发送顺序到达。
  - Advantage：线路出问题时包可以改走别的路线。
  - Disadvantage：在目的地重组包需要时间。

**与 MS 对齐**　电路交换：描述 MS 列四点 Any two（dedicated circuit / established before … released after / whole bandwidth / same route），再加优点 1 分、缺点 1 分，合计 Max 4；分组交换：描述同样 Any two（split into packets / own route / routing depends on congestion / may not arrive in order），优点、缺点各 1 分，Max 4。作答里的优缺点都取自该题 MS：电路交换「Advantage – data /frames arrive in order and do not need to be reassembled」⟦9618_s22_31:3⟧、“Disadvantage – nobody else can use the same circuit even if it is idle”；分组交换 “Advantage – packets can be rerouted if there are problems”、「Disadvantage – time taken to reassemble packets at the destination」⟦9618_s22_31:3⟧。描述部分每边写三点，比 Any two 多一点作保险。

**英文作答句**　Circuit switching: a dedicated circuit is established before transmission starts and released after it ends; all data is transferred over the same route using the whole bandwidth. Advantage: data arrives in order and does not need to be reassembled. Disadvantage: nobody else can use the circuit even if it is idle. Packet switching: data is split into packets and each packet is given its own route, depending on congestion; packets may not arrive in the order sent. Advantage: packets can be rerouted if there are problems. Disadvantage: time is taken to reassemble the packets at the destination.

**直观**　电路交换像包下一整节车厢从头坐到尾；分组交换像把一群人拆开、各自坐不同的公交，到终点再集合。

**下一道变式**　⟦9618_w25_32:4(b)⟧　（只写两个区别，每个都要“电路交换怎样 … 分组交换怎样 …”成对写。）

<!-- auto:drills P3-CI-07 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| CI-01 vs CI-02 | 层与层怎样交互、消息怎样穿过整个栈、为什么要协议 → CI-01；各层名称、顺序、某层功能 → CI-02 | 题干有没有 “Do not describe the function of individual layers” / “interact with each other” |
| CI-02 vs CI-03 | 问应用层**这一层**的目的与功能 → CI-02；问应用层上的**具体协议** → CI-03 | “purpose of the Application Layer” 还是 “protocols used by the Application Layer” |
| CI-03 vs CI-04 | 多个协议一起问（含连线里 BitTorrent 一条）→ CI-03；单独问 BitTorrent 怎样共享 → CI-04 | 题干是否只提 BitTorrent |
| POP3 vs IMAP | 都是收邮件；POP3 把邮件取回到电脑，IMAP 把邮件留在服务器、多设备同步 | 题目要“IMAP 的特点”时必须写同步 / 不删除 |
| SMTP vs POP3 / IMAP | SMTP 发送（push）；POP3 / IMAP 接收（pull） | Sending … / Receiving … |
| Internet 层 vs Link 层 | Internet：IP 地址、选路、跨网络；Link：帧、MAC 地址、直连设备之间的下一跳 | 说的是 IP 还是 MAC、跨网络还是本地段 |
| CI-05 / CI-06 vs CI-07 | 只问一种交换 → 不比较；同一小问两种都问 → CI-07，成对写 | 题干出现几种交换方式 |
| 好处 vs 特点 | 特点是事实（“continuous stream”）；好处要说出因此带来什么（“so no time is wasted reordering”） | benefit / advantage 题检查每句有没有“所以” |
