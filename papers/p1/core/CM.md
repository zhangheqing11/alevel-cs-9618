## CM　通信：核心概念 {#core-CM}

英文列带 ⟦⟧ 的是该题 MS 原文；标“非 MS 原句”的是标准定义，作答时以所答那题的 MS 为准。

| 术语 | 英文得分句 | 中文定义 | 直观理解 | 相关题型 |
|:--|:--|:--|:--|:--|
| LAN | 「Covers a small geographical area」⟦9618_s23_12:1(b)⟧；「The infrastructure is privately owned // not controlled by external organisations」⟦9618_s23_12:1(b)⟧ | 覆盖小地理范围、基础设施由机构自己拥有的网络 | 一栋楼里自己拉的线 | P1-CM-01 |
| WAN | 「A WAN covers a large geographical area」⟦9618_w24_13:9(a)⟧；「External/public infrastructure is used」⟦9618_w24_13:9(a)⟧ | 覆盖大地理范围、使用外部/公共基础设施的网络 | 跨城市，只能租别人的线路 | P1-CM-01 |
| Client-server model | Clients send requests to a server; the server processes the requests, stores the data and sends the results back.（非 MS 原句） | 客户端发请求，服务器处理请求、集中存储数据并返回结果 | 餐厅：客人点单（请求），厨房做菜（处理），服务员上菜（返回） | P1-CM-02 |
| Thin client | 「Clients only sends requests to the server and displays the returned results」⟦9618_s23_13:2(c)⟧ | 客户端只发请求、显示结果，处理与数据都在服务器上 | 只有屏幕和键盘的“遥控器”，离了服务器和网络就不能用 | P1-CM-02 |
| Thick client | 「The clients also do most of their own processing/work independently」⟦9618_s23_12:1(e)⟧ | 客户端自己完成大部分处理，资源装在本地，服务器只做少量处理 | 自带厨房的客人，只偶尔向餐厅要食材 | P1-CM-02 |
| Peer-to-peer network | 「All computers are of equal status」⟦9618_s21_11:4(a)⟧ | 各计算机地位平等，每台既提供也使用资源，没有中心服务器 | 同学之间互相借笔记，没有图书馆 | P1-CM-02 |
| Bus topology | All devices are connected to a single shared backbone cable.（非 MS 原句） | 所有设备接在同一条主干电缆上 | 一条走廊两边的房间，喊一声所有人都听得见 | P1-CM-03、P1-CM-07 |
| Star topology | Each device is connected directly to one central device (switch).（非 MS 原句） | 每台设备用独立线路直连一个中心设备 | 车轮的辐条，一根断了只影响一台 | P1-CM-03、P1-CM-04 |
| Mesh topology | 「There are multiple routes between devices」⟦9618_s23_13:2(b)(i)⟧ | 设备之间多条连接，任意两点间有多条路径，设备可作中继 | 城市路网：一条路堵了还能绕 | P1-CM-03 |
| Switch | 「To forward packets directly to the intended recipient」⟦9618_s25_12:6(e)⟧；「To store the MAC addresses of devices connected to it」⟦9618_s25_12:6(e)⟧ | 局域网中心设备，记录所连设备的 MAC 地址，把数据包只转发给目的设备 | 楼里的收发室，按门牌号把信送到那一户 | P1-CM-04、P1-CM-05 |
| Router | 「Analyses the destination IP address of each packet」⟦9618_w23_11:2(a)⟧；「Forwards the packet towards its destination」⟦9618_s24_12:3(c)(i)⟧ | 连接不同网络，读取目的 IP 地址、用路由表选路转发；为 LAN 分配私有 IP | 邮局分拣中心，按城市和街道把信发往下一站 | P1-CM-05 |
| Wireless access point (WAP) | 「To allow wireless enabled devices to connect to a wired network」⟦9618_w23_11:2(b)⟧ | 让无线设备通过无线电信号接入有线网络的设备 | 有线网络伸出的一只“无线耳朵” | P1-CM-05 |
| Bridge | 「To connect two LANs / segments with the same protocol」⟦9618_w23_11:2(b)⟧ | 连接两个使用相同协议的 LAN 或网段 | 两个说同一种语言的社区之间的一座桥 | P1-CM-05 |
| Repeater | Restores the digital signal so it can be transmitted over greater distances.（非 MS 原句） | 再生信号，使其能传得更远 | 接力赛中途换一个精力充沛的人 | P1-CM-05 |
| WNIC | 「Provide interface to wireless network」⟦9618_w21_11:8(c)⟧ | 设备接入无线网络的接口：收发无线电波，并与数字数据互相转换 | 设备自己的“无线电台” | P1-CM-05 |
| Ethernet | 「Data is transmitted in frames」⟦9618_s23_12:1(d)⟧ | 有线局域网的协议（族）：数据按帧传输，帧含源/目的地址与差错校验数据，用 CSMA/CD 处理冲突 | 局域网里大家约定的“说话规矩” | P1-CM-07 |
| CSMA/CD | 「CSMA/CD is a protocol used to detect and prevent collisions in a bus topology」⟦9618_w22_11:8⟧ | 载波侦听多路访问/冲突检测：发送前侦听，空闲才发，检测到冲突就停止并发阻塞信号，随机等待后重发 | 会议上先听有没有人在说；两人同时开口就都停下，各自等一会儿再说 | P1-CM-07 |
| Collision | 「two workstations can start to transmit at the same time, causing a collision」⟦9618_w22_11:8⟧ | 两个节点同时在共享介质上发送，信号互相干扰 | 走廊里两个人同时喊 | P1-CM-07 |
| Cloud computing | 「Accessing a service/files/software on a remote server」⟦9618_s22_13:8(a)⟧ | 通过网络访问远程服务器上的服务、文件或软件 | 东西放在别人的仓库里，随用随取 | P1-CM-08 |
| Public cloud | 「Computing services offered by 3rd party provider over the public Internet」⟦9618_s22_13:8(b)⟧ | 第三方通过公共互联网提供、任何人都能注册使用的云服务 | 公共储物柜，谁都能租 | P1-CM-08 |
| Private cloud | 「Dedicated/bespoke services/storage on a remote server only available to company」⟦9618_s24_13:5(a)(i)⟧ | 远程服务器上为某机构专门定制、只供该机构使用的云服务 | 包下一整间仓库，钥匙只在自己手里 | P1-CM-08 |
| Internet vs WWW | 「using internet because sending data on the infrastructure」⟦9618_s21_11:4(d)⟧ | 互联网是全球网络的基础设施；万维网是通过互联网访问的网站与网页集合 | 互联网是公路网，万维网是路边的商店 | P1-CM-09 |
| Modem | 「Converts digital data into analogue for transmission down phone lines」⟦9618_s25_11:2(c)⟧ | 在数字信号与模拟信号之间转换，使数据能在电话线上传输 | 翻译官：计算机说“数字语”，电话线听“模拟语” | P1-CM-09 |
| Dedicated line | 「Used to provide a direct / private connection which therefore provides faster transmission」⟦9618_s25_11:2(c)⟧ | 两点之间专用、私有的直接连接，因而传输更快 | 自家专用车道 | P1-CM-09 |
| PSTN | 「The PSTN consists of many different types of communication lines」⟦9618_s24_12:3(c)(ii)⟧ | 公共交换电话网：由多种通信线路组成，经交换中心转接，可双向同时传输 | 老电话网络被拿来顺带传数据 | P1-CM-09 |
| Cell phone network | 「Land is split into cells designed for maximum line of sight」⟦9618_s25_12:6(b)⟧ | 地面分成蜂窝小区，每个小区的基站用低功率无线电与手机收发数据 | 每个小区一座“信号塔”，人走到哪就由哪座塔服务 | P1-CM-09 |
| DNS | 「The browser finds the IP address for the domain name by querying a DNS server」⟦9618_w25_11:7(c)⟧ | 域名系统：把域名转换成对应的 IP 地址 | 互联网的通讯录：查名字得到号码 | P1-CM-09 |
| URL | The text address of a web resource, made up of the protocol, domain name and path.（非 MS 原句） | 网页资源的文本地址，含协议、域名、路径 | 写在信封上的完整地址 | P1-CM-09 |
| IPv4 vs IPv6 | 「IPv4 is 32 bits whilst IPv6 is 128 bits」⟦9618_s24_11:8(b)(ii)⟧；「IPv4 is usually represented in denary whilst IPv6 is usually represented in hexadecimal」⟦9618_s24_11:8(b)(ii)⟧ | IPv4：4 组 × 8 位、十进制、句点分隔；IPv6：8 组 × 16 位、十六进制、冒号分隔 | IPv4 的号码用完了，IPv6 把号码加长到 128 位 | P1-CM-10 |
| Public IP address | 「to be visible to and accessible by other devices on the internet」⟦9618_s24_11:8(b)(i)⟧ | 在互联网上可见、可被访问的 IP 地址 | 对外公开的门牌号 | P1-CM-10 |
| Private IP address | 「Private means it can only be accessed/seen/used within the LAN」⟦9618_s24_13:5(d)⟧ | 只在本 LAN 内可见、由 LAN 内路由器分配的 IP 地址 | 楼里的房间号，出了楼没人认识 | P1-CM-10 |
| Static IP address | 「Static means the IP for that device does not change」⟦9618_s24_13:5(d)⟧ | 每次连接都不变的 IP 地址 | 固定车位 | P1-CM-10 |
| Dynamic IP address | 「A dynamic IP address can change each time the computer connects to a network」⟦9618_s25_12:6(c)⟧ | 每次连接时可能重新分配的 IP 地址 | 停车场随到随停 | P1-CM-10 |
| Subnetting | 「It allows the network to be divided into smaller networks」⟦9618_w24_13:9(d)(ii)⟧ | 把一个网络划分成多个更小的子网络 | 把一个大开间办公室隔成几个部门 | P1-CM-11 |
| Network ID / host ID | 「IP address is made up of a network ID and a host ID」⟦9618_s23_13:2(e)⟧；「the host ID uniquely identifies the device within the subnetwork」⟦9618_s23_13:2(e)⟧ | 子网中的 IP 地址分两部分：同一子网共享网络 ID，主机 ID 在子网内唯一标识设备 | 楼号 + 房间号 | P1-CM-11 |
| Subnet mask | A mask that shows which part of an IP address is the network ID and which part is the host ID.（非 MS 原句） | 标明 IP 地址中哪些位属于网络 ID、哪些属于主机 ID 的掩码（255 对应网络部分，0 对应主机部分） | 一把遮住房间号、只露出楼号的尺子 | P1-CM-11 |
| Bit streaming | 「Continuous ordered flow of bits over a communication path」⟦9618_s24_11:2(e)(i)⟧ | 在通信路径上连续、有序地传输的位流，边传边播 | 自来水：打开就流，不用等整桶接满 | P1-CM-12 |
| Real-time vs on-demand | 「Real-time cannot be re-watched, on-demand can be paused, re-watched」⟦9618_s24_11:2(e)(ii)⟧ | 实时流直接来自源头、不能回看；点播是预先录制存放在服务器上，可暂停、回看 | 直播对回放 | P1-CM-12 |
| Media server buffer | 「Buffer stores data from server until recipient can receive it」⟦9618_s25_11:2(a)⟧ | 接收端缓冲区暂存服务器发来的数据，直到接收方能处理 | 水箱：进水忽快忽慢，出水保持平稳 | P1-CM-12、P1-HW-06 |
