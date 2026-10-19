## CI　通信与互联网技术：核心概念 {#core-CI}

英文列带 ⟦⟧ 的是该题 MS 原文；标“非 MS 原句”的是标准定义，作答时以所答那题的 MS 为准。

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| Protocol | 「Protocols provide a standard set of rules that enables successful data transfer between devices」⟦9618_s24_32:2(a)⟧ | 设备之间通信所遵守的一套标准规则；使不同厂商 / 平台的设备能够兼容 | 两国人约定用同一种语言和格式写信 | P3-CI-01 |
| Protocol stack / suite | 「The TCP/IP suite can be viewed as layers within a stack」⟦9618_s25_32:3(b)⟧ | 把协议按功能分成若干层叠起来实现；每层有自己的功能 | 一栋楼，每层办一类事 | P3-CI-01、P3-CI-02 |
| Adjacent layers | 「Each layer can only accept input from the next higher layer or the next lower layer」⟦9618_w24_31:4⟧ | 每层只与上下相邻的层交换数据，层间通过接口交互 | 只能和楼上楼下的邻居递东西 | P3-CI-01 |
| Header (encapsulation) | 「Data is added to the headers as the frames/packets pass through the layers」⟦9618_w24_31:4⟧ | 数据逐层向下传时，每层在前面加上自己的报头；接收方逐层去掉 | 每经一道手续贴一张标签 | P3-CI-01、P3-CI-02 |
| TCP/IP layers (order) | 「Application Transport Internet Link」⟦9618_s24_31:2(a)⟧ | 自上而下：应用层、传输层、网际层、链路层 | 用户在顶楼、网线在地下室 | P3-CI-02 |
| Application layer | 「The application layer provides access to all the programs that exchange data // Interacts directly with user」⟦9618_w24_32:5(b)⟧ | 与用户交互，为应用提供服务并定义应用交换数据所用的协议 | 前台接待 | P3-CI-02、P3-CI-03 |
| Transport layer | 「The transport layer is responsible for delivery of data from the source host to the destination host」⟦9618_s24_31:2(b)⟧ | 端到端交付：分段 / 分包、加序号、流量控制、保证无差错、丢包重传 | 打包员：拆箱、编号、保证一箱不少 | P3-CI-02 |
| Internet layer | 「It addresses packets with their source and destination IP addresses」⟦9618_w22_31:2⟧ | 确定目标网络与主机，给包加源 / 目的 IP 地址，为每个包选路 | 调度员：贴地址、选路线 | P3-CI-02 |
| Link layer | 「To format the data into frames for transmission」⟦9618_w23_31:2(b)⟧ | 在直接相连的设备之间传送：成帧、IP 地址映射到 MAC 地址、接入物理介质 | 司机：只管开到下一站 | P3-CI-02 |
| HTTP / HTTPS | 「HTTP to send and receive / transfer web pages / hypertext / images / videos」⟦9618_w25_32:3(a)⟧ | 传输网页 / 超文本的应用层协议；HTTPS 为安全版本 | 网页窗口 | P3-CI-03 |
| FTP | 「a protocol to download, upload and transfer files from one location to another on a network」⟦9618_w25_33:4⟧ | 在网络上传输文件的应用层协议 | 文件窗口 | P3-CI-03 |
| SMTP | 「Push protocol / for sending / uploading emails」⟦9618_w24_32:5(a)⟧ | 发送电子邮件的协议（电脑 → 邮件服务器、服务器 → 服务器） | 寄信窗口 | P3-CI-03 |
| POP3 | 「a protocol used to retrieve/receive emails from a mail server to a computer」⟦9618_w25_33:4⟧ | 从邮件服务器取回邮件到电脑的协议（pull） | 取信：信拿回家 | P3-CI-03 |
| IMAP | 「allows users to access/read their emails from any device without removing the message from the mail server // synchronises emails on any device」⟦9618_w25_32:3(a)⟧ | 在任何设备上访问邮件、邮件留在服务器上、各设备同步的接收协议 | 取信：只在邮局里看，信不拿走 | P3-CI-03 |
| BitTorrent | 「a communication protocol used for peer-to-peer file sharing」⟦9618_w25_33:4⟧ | 点对点文件共享协议：文件分块，各 peer 互相下载、上传 | 大家互相复印一本书的不同页 | P3-CI-04、P3-CI-03 |
| Torrent file | 「The torrent (descriptor file) contains metadata about the file to be shared」⟦9618_w25_32:3(b)⟧ | 描述要共享文件的元数据的小文件，下载者先取得它 | 书的目录卡 | P3-CI-04 |
| Tracker | 「A tracker acts like a server that holds all the data about all the computers connected to it / the swarm」⟦9618_w25_32:3(b)⟧ | 记录哪些计算机（swarm）参与共享的服务器式角色，不传文件本身 | 名单管理员 | P3-CI-04 |
| Seed | 「A peer who has a complete file and is sharing it is a seed」⟦9618_w25_32:3(b)⟧ | 拥有完整文件并在共享的 peer | 有整本书、愿意借给别人的人 | P3-CI-04 |
| Circuit switching | 「A dedicated circuit / channel is required」⟦9618_w24_31:3(a)⟧ | 传输前先建立一条专用线路，整个传输期间独占，数据沿同一路线按序连续传送，结束后释放 | 包下一整节车厢 | P3-CI-05、P3-CI-07 |
| Packet switching | 「The data to be transmitted is divided into equal sized packets」⟦9618_w24_32:1(a)⟧ | 消息分成带报头的包，各包独立选路，到达后按序号重组，丢失的包重发 | 拆成编号明信片各自寄 | P3-CI-06、P3-CI-07 |
| Packet header | 「A packet header is attached to each packet containing key information」⟦9618_w24_32:1(a)⟧ | 包前面附带的控制信息：源 / 目的 IP 地址、包序号等 | 明信片上的收发地址和编号 | P3-CI-06 |
| Router | 「The router reads the IP address of the destination from the packet header」⟦9618_s25_33:4(b)⟧ | 读包的目的 IP、查路由表、决定下一跳并转发包的设备 | 路口的指路员 | P3-CI-06 |
| Routing table | 「A router uses a routing table to find information …」⟦9618_s25_33:4(b)⟧ | 路由器保存的可用跳、网关、相邻路由器、线路状态等信息，用来选下一跳 | 指路员手里的地图 | P3-CI-06 |
| Hop counter | 「The router manages the hop counter // The hop counter is reduced by 1 every time the packet passes a router」⟦9618_s25_33:4(b)⟧ | 包报头里的计数，每经过一个路由器减 1，用完则丢弃该包 | 车票上剩余的站数 | P3-CI-06 |
