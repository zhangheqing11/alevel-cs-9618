## CM　通信 {#ch-CM}

<!-- auto:chapter-stats -->

### 核心思想

这一章讲**数据怎样从一台设备到达另一台设备**，从小到大一层一层展开：

1. **网有多大、谁当家**（CM-01、CM-02）：LAN / WAN 看地理范围与基础设施归谁；客户端-服务器、对等网、瘦/胖客户端看“谁存数据、谁做处理”。
2. **怎么连**（CM-03 至 CM-07）：拓扑决定线怎么拉（CM-03），数据包在线上怎么走（CM-04），靠哪些硬件转发（CM-05），走铜线、光纤还是无线电（CM-06），总线上同时发送撞车了怎么办（CM-07，以太网与 CSMA/CD）。
3. **出了局域网之后**（CM-08 至 CM-11）：云（CM-08）；互联网的物理设施与 URL → DNS → IP 的寻址链（CM-09）；IP 地址的格式与类型（CM-10）；把一个网切成子网（CM-11）。
4. **连续的媒体流**（CM-12）：位流——边传边播，靠缓冲区抹平速度差。

这一章几乎没有计算（子网求网络 ID/主机 ID 除外），分值都在 describe / explain 里。得分的关键是用**设备名 + 动作**写短句：“The switch checks the destination address of each packet”，而不是“the network sends it to the right place”。

**心智模型**　一句话：**每个设备有地址，每一跳按地址转发**。数据包 = 报头（源地址、目的地址、序号）+ 数据；网络里的每样硬件只做一件事——看地址决定往哪送：集线器不看地址（转发给所有端口），交换机看 MAC 地址（只送到目的端口），路由器看 IP 地址（在网络之间选路），DNS 把域名翻成 IP 地址，子网掩码告诉你地址的哪一段是“网络”、哪一段是“主机”（CM-10、CM-11）。拓扑（CM-03、CM-04）决定一跳能到哪些设备、会不会撞车（总线上要 CSMA/CD，CM-07；交换机星型不会）；LAN / WAN、客户端-服务器 / 对等网（CM-01、CM-02）问的是“地址空间多大、谁存数据谁处理”；云和位流（CM-08、CM-12）是把存储与处理放到远端地址、再把数据连续送回来。描述题的每一句都应该是“某个设备看某个地址做某个动作”——这就是卷首第 10 条规则在本章的样子。

### 题型树
<!-- auto:type-tree -->

### P1-CM-01　局域网与广域网　{#P1-CM-01}

<!-- auto:stats P1-CM-01 -->

**考法**　①LAN 或 WAN 的特征（各 2 分）；②两者的区别；③联网（LAN）的好处；④判断情境中的网络是 LAN 还是 WAN 并论证（判断本身可能有分，也可能没有）。

**识别信号**　Give / Describe the characteristics of a LAN / WAN；Identify / State two differences between a WAN and a LAN；Give two benefits of connecting computers to a LAN；State whether the network will be a LAN or a WAN. Justify。

**解题思路**
1. 区别从三根轴找：**地理范围**（小 vs 大）；**基础设施归谁**（LAN 自有、专用；WAN 用外部/公共、租用的线路与设备）；**传输介质与速度、安全**（LAN 传输率高、更易保护）。
2. 区别题每点都写成**一对**：“A WAN covers a large geographical area whereas a LAN covers a small geographical area”。
3. 联网好处：共享文件/数据与通信；共享硬件与软件资源；集中管理（备份、安全）。
4. 判断题：一栋楼、一个校区 → LAN；多个城市、多个校区之间 → WAN。理由扣题目给的地点。

**得分表述**（引自对应 MS）
- 「Covers a small geographical area」⟦9618_s23_12:1(b)⟧
- 「The infrastructure is privately owned // not controlled by external organisations」⟦9618_s23_12:1(b)⟧
- 「A WAN covers a large geographical area」⟦9618_w24_13:9(a)⟧
- 「External/public infrastructure is used」⟦9618_w24_13:9(a)⟧
- 「Allows the sharing of resources e.g. hardware / software (applications)」⟦9618_s23_12:1(a)⟧
- 「LAN is usually more secure than a WAN because protection is easier to implement」⟦9618_s23_13:2(a)⟧

**易错与失分**
- 用“WAN is bigger”代替地理范围：要写 geographical area。
- 把“WAN = 互联网”写进答案：互联网是一个 WAN 的例子，不是定义。
- 区别题只写一边（“LAN is fast”）常常不给分，要和 WAN 对着写。
- “benefits of a LAN”写成 LAN 的特征（small area）——那是特征不是好处。

#### 代表题精讲　⟦9618_s23_13:2(a)⟧

**在考什么**　一所大学两个校区组成 WAN。Identify two differences between a WAN and a LAN. 2 分，每点 1 分。

**完整作答**
1. 范围：WAN 覆盖大的地理区域（这里是两个校区之间），LAN 只覆盖小的区域（一栋楼）。
2. 所有权：LAN 由机构自己拥有，WAN 可以是私有也可以是公共的（租用外部线路）。

（MS 还接受：LAN 的连接通常是物理连接，WAN 常是虚拟连接；LAN 传输率高，WAN 低；LAN 更容易保护所以更安全。）

**与 MS 对齐**　①“WAN covers a large geographical area and LAN covers a small geographical area”；②“The ownership of a LAN is private; the ownership of a WAN can be private or public”。

**英文作答句**　1. A WAN covers a large geographical area, whereas a LAN covers a small geographical area. 2. The ownership of a LAN is private, whereas the ownership of a WAN can be private or public.

**下一道变式**　⟦9618_w24_13:9(a)⟧　（只描述 WAN 的特征。）

<!-- auto:drills P1-CM-01 -->

### P1-CM-02　网络模型：客户端-服务器、对等网、瘦/胖客户端　{#P1-CM-02}

<!-- auto:stats P1-CM-02 -->

**考法**　①在情境中描述客户端与服务器各自的角色（银行 App、网页游戏）；②解释“这个系统用的是客户端-服务器模型”为什么成立；③瘦客户端 / 胖客户端的含义与特征，常配“特征 + 在本情境中的体现”两栏表；④对等网的特征与缺点（2021 扩展卷）。

**识别信号**　client-server model … Describe the roles of the different devices；thin-client / thick-client；peer-to-peer network … key features / drawbacks；Explain the reasons why the statement ‘… uses a client-server model’ is correct。

**解题思路**
1. 先**点名**情境里谁是服务器、谁是客户端（MS 常把“identification”单列 1 分）。
2. 再写**动作链**：客户端发送请求 → 服务器接收并处理请求、存储数据 → 服务器把结果发回 → 客户端显示结果。
3. 瘦客户端：数据不存在客户端、处理几乎全在服务器；客户端依赖服务器与网络连接；只需很少本地资源。胖客户端：客户端自己完成大部分处理，资源装在本地，服务器只做少量处理。
4. 对等网：所有计算机地位平等，每台既提供也使用资源，各自负责安全——所以缺点是没有集中的安全、备份与文件管理。
5. 两栏表的第二栏必须扣情境（“the exam papers are stored on the server, not on the examiner's computer”）。

**得分表述**（引自对应 MS）
- 「that sends requests over the internet to the web server」⟦9618_s25_13:3(c)⟧
- 「the server sends the results to the player」⟦9618_s25_13:3(c)⟧
- 「Server performs all processes required by the task and/or data storage」⟦9618_s23_13:2(c)⟧
- 「Clients only sends requests to the server and displays the returned results」⟦9618_s23_13:2(c)⟧
- 「The clients also do most of their own processing/work independently」⟦9618_s23_12:1(e)⟧
- 「All computers are of equal status」⟦9618_s21_11:4(a)⟧

**易错与失分**
- 只写“server stores data, client uses it”：没有“发送请求 / 处理请求 / 返回结果”的动作链，最多 1 分。
- 情境题不点名设备：MS 的 identification 分要求说出“the bank's server”“the customer's smartphone app”。
- 瘦客户端写成“cheap computer”：要写“few local resources / reliant on the server and network connection”。
- 把云存储题答成客户端-服务器（云在 CM-08）。

#### 代表题精讲　⟦9618_s25_13:3(c)⟧

**在考什么**　网页游戏：玩家用浏览器在任何联网电脑上玩，与其他玩家互动。Explain the reasons why the statement ‘This computer game uses a client-server model’ is correct. 4 分。

**完整作答**　游戏的数据（每个玩家的进度、位置）都存放在网络服务器上。每个玩家的电脑——准确说是玩家的浏览器——是客户端。玩家操作时，客户端通过互联网向服务器发送请求；服务器执行游戏里相应的动作、更新游戏数据，再把结果发回给玩家，浏览器显示出来。

**与 MS 对齐**　“A webserver stores all the data for each player”→“Each player is on a client computer // The player's web browser is the client”→“that sends requests over the internet to the web server”→“the server performs the required action in the game”/“the server updates the data in the game”→“the server sends the results to the player”，六点取四。

**英文作答句**　A web server stores all the data for each player. Each player's web browser is a client that sends requests over the internet to the web server. The server performs the required action in the game and updates the game data. The server then sends the results back to the player.

**下一道变式**　⟦9618_s24_11:5(a)⟧　（银行 App 情境：描述客户端与服务器各自的角色，含“点名”分。）

<!-- auto:drills P1-CM-02 -->

### P1-CM-03　网络拓扑　{#P1-CM-03}

<!-- auto:stats P1-CM-03 -->

**考法**　①画出或补全星型网络连接图（交换机/服务器在中间，2–4 分）；②描述网状（mesh）拓扑；③比较：星型相对总线、网状相对总线的优点，总线的缺点；④勾选表：每句话描述的是总线、星型还是网状（可多选）；⑤判断一个家庭网络的拓扑并论证。

**识别信号**　bus / star / mesh / hybrid topology；Draw a diagram to show the layout of … star topology；Complete the diagram to show how the hardware is connected；advantage(s) of … instead of a bus topology；Tick one or more boxes … to identify the topology。

**解题思路**
1. 三种结构一句话：**总线**——所有设备接在一条主干电缆上；**星型**——每台设备单独直连一个中心设备（交换机）；**网状**——设备之间多条连接，任意两点有多条路径。
2. 画星型：中心设备（题目说是 switch 就画 switch；只有 server 时以 server 为中心）；每台计算机**单独一条线**连到中心，计算机之间**没有**其他连线；所有设备都要**标注**；需要上网时把路由器/调制解调器接到交换机或服务器。
3. 优缺点按“结构 → 后果”写：
   - 星型 vs 总线：一条线坏了只影响一台设备（没有单根共享电缆）；冲突更少、性能更高；加新节点只需接到交换机；故障易定位。
   - 网状 vs 总线：一条线断了还有别的路径；没有一根共享主线，冲突更少、更安全。
   - 总线的缺点：节点多时效率低（同一时刻线上只能有一个传输）；主干断了整个网络瘫痪；广播给所有节点，有隐私问题。
4. 勾选表逐行对照结构特点；“most likely to lose data through collisions”→ 总线。

**得分表述**（引自对应 MS）
- 「All computers directly connected to switch and no other connections」⟦9618_w25_12:5(b)⟧
- 「Four labelled computers all connected directly to the switch」⟦9618_s25_12:6(d)⟧
- 「There are multiple routes between devices」⟦9618_s23_13:2(b)(i)⟧
- 「If one line goes down there are more routes available」⟦9618_s23_13:2(b)(ii)⟧
- 「Star topology is more resilient to faults」⟦9618_w23_11:2(d)⟧
- 「Higher performance as fewer collisions」⟦9618_w23_11:2(d)⟧

**易错与失分**
- 画图时计算机之间多连了线，或交换机和服务器的关系画反：MS 写明“no other connections”。
- 漏标设备名：⟦9618_s23_12:1(c)⟧ 的第二分就是“all components correctly labelled”。
- “Explain one advantage”只写优点不写原因：MS 是“优点 1 分 + 对应展开 1 分”。
- 网状拓扑写成“all computers connected to all others”：MS 的说法是“connected to at least one other device”+“multiple routes”。

#### 代表题精讲　⟦9618_s25_12:6(d)⟧

**在考什么**　总部办公室：4 台有线计算机、1 台服务器、2 台打印机、1 台中心交换机、1 台提供互联网接入点的设备，组成星型网络。Draw the topology. Label all devices. 4 分（讲解时请对照原卷 QP p.12 的作图区与 MS p.11 的示例图）。

**完整作答**　交换机放在中心，其余每台设备各用一条线直连交换机：

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 300" role="img" aria-labelledby="cm03-star-title" style="width:100%;max-width:680px;height:auto">
  <title id="cm03-star-title">星型网络：四台计算机、两台打印机、服务器及路由器分别直连中心交换机</title>
  <g stroke="#333" stroke-width="2">
    <line x1="85" y1="55" x2="340" y2="150" />
    <line x1="255" y1="55" x2="340" y2="150" />
    <line x1="425" y1="55" x2="340" y2="150" />
    <line x1="595" y1="55" x2="340" y2="150" />
    <line x1="85" y1="245" x2="340" y2="150" />
    <line x1="255" y1="245" x2="340" y2="150" />
    <line x1="425" y1="245" x2="340" y2="150" />
    <line x1="595" y1="245" x2="340" y2="150" />
  </g>
  <g fill="white" stroke="#333" stroke-width="2">
    <rect x="15" y="10" width="140" height="45" />
    <rect x="185" y="10" width="140" height="45" />
    <rect x="355" y="10" width="140" height="45" />
    <rect x="525" y="10" width="140" height="45" />
    <rect x="280" y="125" width="120" height="50" />
    <rect x="15" y="245" width="140" height="45" />
    <rect x="185" y="245" width="140" height="45" />
    <rect x="355" y="245" width="140" height="45" />
    <rect x="525" y="245" width="140" height="45" />
  </g>
  <g fill="#111">
    <text x="85" y="38" text-anchor="middle" font-family="Helvetica" font-size="15">Computer 1</text>
    <text x="255" y="38" text-anchor="middle" font-family="Helvetica" font-size="15">Computer 2</text>
    <text x="425" y="38" text-anchor="middle" font-family="Helvetica" font-size="15">Computer 3</text>
    <text x="595" y="38" text-anchor="middle" font-family="Helvetica" font-size="15">Computer 4</text>
    <text x="340" y="156" text-anchor="middle" font-family="Helvetica" font-size="15">SWITCH</text>
    <text x="85" y="273" text-anchor="middle" font-family="Helvetica" font-size="15">Printer 1</text>
    <text x="255" y="273" text-anchor="middle" font-family="Helvetica" font-size="15">Printer 2</text>
    <text x="425" y="273" text-anchor="middle" font-family="Helvetica" font-size="15">Server</text>
    <text x="595" y="273" text-anchor="middle" font-family="Helvetica" font-size="15">Router (internet)</text>
  </g>
</svg>

（打印机也可以接在服务器或某台计算机上；路由器/调制解调器可以接在交换机或服务器上——MS 都接受。）

**与 MS 对齐**　①“Server directly connected to the switch”；②“Four labelled computers all connected directly to the switch”；③“Two printers each directly connected to the switch / server / a computer”；④“Router / modem directly connected to the switch / server for internet access”。四个设备组各 1 分，标注是②的一部分。

**英文作答句**　（作图题无需文字；口头说明可写）Each device is connected directly to the central switch by its own cable, and the router is connected to the switch to provide internet access.

**下一道变式**　⟦9618_w23_11:2(d)⟧　（不画图，解释星型相对总线的一个优点，“优点 + 展开”。）

<!-- auto:drills P1-CM-03 -->

### P1-CM-04　拓扑中的数据包传输　{#P1-CM-04}

<!-- auto:stats P1-CM-04 -->

**考法**　按步骤描述数据包怎样在两台主机之间传输：星型网络经交换机（或路由器）按目的地址转发；总线网络在电缆上广播、只有目的节点接收（常和以太网/CSMA/CD 合考，此时主题型归 CM-07）。2–3 分。

**识别信号**　Explain / Describe how packets are transmitted between two devices / hosts in a star topology；Explain how data is transmitted between the two laptops in the LAN；… between two nodes in a bus topology。

**解题思路**
1. 星型三步：发送设备把数据包发给**中心设备**（交换机/路由器）→ 中心设备**读取每个包的目的地址**（必要时查路由表/MAC 表）→ **只**转发给目的设备。
2. 总线三步：两台设备都接在同一条总线上 → 数据在电缆上**广播**给所有节点 → 只有地址匹配的目的节点**接收**，其余忽略。
3. 题目里中心设备叫什么就写什么（switch、router、central device）。

**得分表述**（引自对应 MS）
- 「The sending device sends the packets to the switch」⟦9618_w25_12:5(c)⟧
- 「The switch checks the destination address on each packet」⟦9618_w25_12:5(c)⟧
- 「and sends them only to the intended receiver」⟦9618_w25_12:5(c)⟧
- 「Switch/router/central device checks destination address of packet and forwards directly to that device」⟦9618_s24_13:5(b)⟧
- 「The router transmits data directly / only to recipient」⟦9618_w23_12:7(b)(ii)⟧

**易错与失分**
- 星型写成“the switch sends the packet to all devices”：那是总线/集线器的行为，星型交换机只发给目的设备（MS 用 only / directly）。
- 漏掉“检查目的地址”这一步：这是三步里最核心的得分点。
- 把数据包传输写成路由器在互联网上选路（CM-05 的内容），偏离“局域网内两台主机”的情境。

#### 代表题精讲　⟦9618_w25_12:5(c)⟧

**在考什么**　LAN 有 5 台计算机、1 台交换机、1 台服务器。Describe how packets are transmitted between two hosts using a star topology. 3 分。

**完整作答**　发送主机把数据包发到交换机；交换机检查每个数据包上的目的地址；然后只把数据包发给目的主机，而不发给网络上的其他设备。

**与 MS 对齐**　三句依次对应“The sending device sends the packets to the switch”“The switch checks the destination address on each packet”“… and sends them only to the intended receiver”。

**英文作答句**　The sending host sends the packets to the switch. The switch checks the destination address on each packet and sends the packets only to the intended receiver.

**下一道变式**　⟦9618_w23_12:7(b)(ii)⟧　（中心设备换成路由器，MS 多了“routing table”一点。）

<!-- auto:drills P1-CM-04 -->

### P1-CM-05　网络硬件与路由器　{#P1-CM-05}

<!-- auto:stats P1-CM-05 -->

**考法**　①路由器的作用/功能（2–3 分，最常考）；②交换机的作用；③硬件用途填表：switch、WAP、bridge、repeater、WNIC，或按描述写设备名；④选设备连接 30 台计算机；⑤勾选“哪些任务由路由器完成”。

**识别信号**　Describe the role / function of a router / switch；Complete the table by writing the purpose of each hardware device；Identify two possible devices that can be used to physically connect；Describe the functions of a Wireless Network Interface Card (WNIC)；Tick … whether the task is performed by the router。

**解题思路**
1. **路由器**（连接不同网络、接入互联网）：接收数据包 → 读取目的 **IP 地址** → 查**路由表** → 选最有效路径转发；维护/更新路由表；给局域网设备分配私有 IP；为局域网提供公有 IP（网关）；可作防火墙、做协议转换。
2. **交换机**（局域网中心）：存储所连设备的 **MAC 地址**；接收数据包并**只**转发给目的设备；提供中心连接点。
3. **WAP**：让无线设备通过无线电信号接入有线网络。**Bridge**：连接两个使用相同协议的 LAN/网段。**Repeater**：再生信号，延长传输距离。**WNIC**：设备接入无线网络的接口，收发无线电波并与数字信号互换，检查地址。
4. 写功能时用“动词 + 对象”：receives packets、analyses the destination IP address、forwards …、maintains the routing table。

**得分表述**（引自对应 MS）
- 「Analyses the destination IP address of each packet」⟦9618_w23_11:2(a)⟧
- 「Forwards the packet towards its destination」⟦9618_s24_12:3(c)(i)⟧
- 「using the routing table」⟦9618_s24_12:3(c)(i)⟧
- 「assign private IP addresses to devices on LAN」⟦9618_w22_12:10(b)(ii)⟧
- 「To store the MAC addresses of devices connected to it」⟦9618_s25_12:6(e)⟧
- 「To connect two LANs / segments with the same protocol」⟦9618_w23_11:2(b)⟧

**易错与失分**
- 路由器与交换机混用：路由器看 **IP 地址**、跨网络；交换机看 **MAC 地址**、局域网内。
- “Finds the IP address of a URL”不是路由器的任务（那是 DNS，⟦9618_s21_11:4(c)(i)⟧ 勾选题的陷阱），“directs each packet to all devices”也不是。
- 同一描述在不同卷 MS 给的设备名可能不同：⟦9618_s22_12:9(a)⟧ 的 MS 把“两个使用相同协议的网络之间收发数据”填为 Router，而 ⟦9618_w23_11:2(b)⟧ 的 MS 把“连接两个相同协议的 LAN”作为 bridge 的用途。批改时只按该题自己的 MS（讲解时请对照原卷 QP p.13）。

#### 代表题精讲　⟦9618_w22_12:10(b)(ii)⟧

**在考什么**　路由器把星型 LAN 接入互联网。Describe the role and function of the router in the network. 3 分，MS 列了 11 个可得分点。

**完整作答**　路由器接收来自局域网设备或互联网的数据包；读取每个包的目的 IP 地址，用路由表找到通往目的地的最有效路径并转发；它还为局域网里的设备分配私有 IP 地址，并以自己的公有 IP 地址作为局域网通往互联网的网关。

**与 MS 对齐**　“receive packets from devices / internet”“find destination of packets using the IP address”“forward packets to the destination”“store/update/maintain a routing table”“find most efficient path to destination”“assign private IP addresses to devices on LAN”“provides the LAN with a public IP address”“acts as a gateway”——写清任意三点即满分。

**英文作答句**　The router receives packets from devices or the internet and finds the destination of each packet using its IP address. It forwards the packets to the destination using a routing table, choosing the most efficient path. It also assigns private IP addresses to devices on the LAN.

**下一道变式**　⟦9618_w23_11:2(b)⟧　（换成填表：switch、WAP、bridge 各自的用途；讲解时请对照原卷 QP p.4。）

<!-- auto:drills P1-CM-05 -->

### P1-CM-06　有线与无线、传输介质　{#P1-CM-06}

<!-- auto:stats P1-CM-06 -->

**考法**　①无线相对有线的优点、无线的缺点；②为情境选择有线或无线并论证（选择不给分）；③同时提供有线和无线的好处；④光纤与铜缆的区别；⑤卫星相对铜缆的优缺点；⑥除铜缆外再说出并描述两种传输介质。

**识别信号**　wired or wireless … Justify；advantages of a wireless network compared to a wired network；differences between fibre-optic cables and copper cables；transmitting data using satellites instead of copper cables；identifying and describing two other transmission media。

**解题思路**
1. 无线的好处：设备可移动、不需物理连接；无需布线、易于安装；易于增加设备；可接多种设备。无线的缺点：安全性较低；速度可能较慢；有干扰；信号随距离衰减。
2. 有线的好处（反过来）：更快、带宽更高、延迟低；更稳定、受距离与墙体干扰小；更安全。
3. 传输介质：铜缆——电信号；光纤——光脉冲，带宽更高、干扰更小、传得更远、更难窃听，但更易损坏；无线电波/微波——不同频率的电磁波；卫星——覆盖偏远地区，但延迟高、受天气影响、需视距。
4. 论证题每点“特性 → 在情境中意味着什么”（“wired is faster, which is needed as she is streaming large files”）。

**得分表述**（引自对应 MS）
- 「Devices can be more mobile as no physical connection is required」⟦9618_w25_13:4(a)⟧
- 「No cabling is needed so easier to set up」⟦9618_w25_13:4(a)⟧
- 「Interference is possible」⟦9618_w25_13:4(b)⟧
- 「Wired provides better performance for the student's device」⟦9618_s23_13:2(d)⟧
- 「Fibre optic data is transmitted using light, copper cable through electrical signals」⟦9618_s22_12:9(b)⟧
- 「Fibre optic has higher bandwidth than copper cable」⟦9618_s22_12:9(b)⟧

**易错与失分**
- 区别题只写光纤一边（“fibre is faster”）：要对着铜缆写 than copper cable。
- 写品牌或技术名（Wi-Fi 6、5G）代替原理：MS 要 radio waves / microwaves 与描述。
- “同时允许有线和无线的好处”要从**学生**角度写（只有一种接口的设备也能接入；需要高速时用有线；需要移动时用无线），不能只罗列两者各自的特点。

#### 代表题精讲　⟦9618_s23_13:2(d)⟧

**在考什么**　学生可以用网线或无线连接大学网络。Explain the benefits to the students of allowing them to use both wired and wireless connections. 4 分。

**完整作答**　有的学生的设备只有一种连接方式，两种都允许保证人人都能接入。需要高性能时学生可以接网线：有线连接速度更快，比如访问大学数据库更快；干扰更少；传输私密作业（如毕业论文）更安全。需要移动时用无线：学生可以在不同教室、校区甚至户外自由使用设备，也可以带多台、自带或更换设备。

**与 MS 对齐**　“Some students might only have one sort of connection on their device”“Wired provides better performance for the student's device”“... for example, enabling faster access to university databases”“There will be less interference if students connect via a cable”“Students can transmit private/confidential data/work securely”“Wireless connection means that the students can use their devices in different rooms/sites/outside/anywhere more freely”——任取四点。

**英文作答句**　Some students might only have one sort of connection on their device. A wired connection provides better performance for the student's device, for example faster access to university databases, with less interference. A wireless connection means students can use their devices in different rooms or sites more freely.

**下一道变式**　⟦9618_s22_12:9(b)⟧　（三个光纤与铜缆的区别，要成对写。）

<!-- auto:drills P1-CM-06 -->

### P1-CM-07　以太网与 CSMA/CD　{#P1-CM-07}

<!-- auto:stats P1-CM-07 -->

**考法**　①描述以太网是什么；②描述 CSMA/CD 怎样检测、处理冲突（3–4 分，最常考）；③碰到冲突后设备做的几件事；④CSMA/CD 的缺点；⑤综合：用以太网在总线拓扑中两节点间传数据。

**识别信号**　Describe what is meant by Ethernet；Carrier Sense Multiple Access / Collision Detection (CSMA/CD)；Describe how collisions are detected and managed；State three tasks performed by devices to deal with collisions；Identify two drawbacks of using CSMA/CD。

**解题思路**
1. **为什么会冲突**：多台设备共用同一传输介质（总线）→ 两台可能同时开始发送 → 冲突。
2. **CSMA/CD 的步骤**（按顺序写）：发送前**侦听**信道（carrier sense）→ 信道空闲才发送，忙则等待 → 发送中**检测**到冲突 → 中止发送并发出**阻塞信号**（jamming signal）→ 各自等待一个**随机**时间后重发 → 反复冲突时随机等待时间增加。
3. **以太网**：一种（有线网络的）协议；使用 CSMA/CD；数据以**帧**传输，每帧有源/目的 MAC 地址和差错校验数据。
4. **缺点**：等待时间可能无限增长、节点无法设优先级、只适合短距离、节点多时等待时间急剧变长（不易扩展）。

**得分表述**（引自对应 MS）
- 「A workstation / node (wishing to transmit) listens to the communication channel」⟦9618_s22_12:9(c)⟧
- 「before transmitting, a device checks if the channel is busy」⟦9618_w22_11:8⟧
- 「two workstations can start to transmit at the same time, causing a collision」⟦9618_w22_11:8⟧
- 「If a collision is detected by the device, transmission is aborted / a jamming signal is transmitted」⟦9618_w22_11:8⟧
- 「both devices wait a (different) random time and then try again」⟦9618_w22_11:8⟧
- 「Data is transmitted in frames」⟦9618_s23_12:1(d)⟧

**易错与失分**
- 等待时间写成“waits for a set time / a few seconds”：必须是 **random**，否则两台设备会同时重发再次冲突。
- 漏掉“发送前先侦听、空闲才发”：只写冲突后的处理，丢掉最前面的 1–2 分。
- 把 CSMA/CD 说成“prevents collisions”：它主要是**检测**并**处理**冲突（个别 MS 写“detect and prevent”，但步骤分都在检测与重发）。

#### 代表题精讲　⟦9618_w22_11:8⟧

**在考什么**　总线拓扑的 LAN。Describe how CSMA/CD is used in a bus network. 4 分，MS 7 点取 4。

**完整作答**　CSMA/CD 是总线网络中用来处理冲突的协议。因为多台计算机连在同一传输介质上，两台工作站可能同时开始发送，造成冲突。所以设备发送前先检查信道是否忙：忙就等待，空闲才发送。如果设备检测到冲突，就中止发送并发出阻塞信号；冲突双方各自等待一个（不同的）随机时间后再重试。

**与 MS 对齐**　“CSMA/CD is a protocol used to detect and prevent collisions in a bus topology”→“because there is more than one computer connected to the same transmission medium”→“two workstations can start to transmit at the same time, causing a collision”→“before transmitting, a device checks if the channel is busy”→“If the channel is busy the device waits // if the channel is free the data is sent”→“If a collision is detected by the device, transmission is aborted / a jamming signal is transmitted”→“both devices wait a (different) random time and then try again”。

**英文作答句**　Before transmitting, a device checks if the channel is busy. If the channel is busy the device waits; if it is free the data is sent. Because more than one computer is connected to the same transmission medium, two workstations can start to transmit at the same time, causing a collision. If a collision is detected, transmission is aborted and a jamming signal is sent. Both devices wait a different random time and then try again.

**下一道变式**　⟦9618_s24_13:5(c)(ii)⟧　（换成 CSMA/CD 的两个缺点。）

<!-- auto:drills P1-CM-07 -->

### P1-CM-08　云计算　{#P1-CM-08}

<!-- auto:stats P1-CM-08 -->

**考法**　①定义云计算、公有云、私有云；②结合情境说使用云（存储）的好处、缺点，或“讨论”好处与缺点；③私有云相对公有云的好处；④为什么某公司用公有云；⑤看图写出连接设备、云类型与云应用。

**识别信号**　Define cloud computing；State what is meant by a public cloud / private cloud；benefits / drawbacks of (storing data using) cloud computing；private cloud storage instead of public cloud storage；Discuss the benefits and drawbacks。

**解题思路**
1. 定义：云计算 = 通过网络访问**远程服务器**上的服务、文件或软件。公有云 = 第三方提供、任何人都能注册使用；私有云 = 专为某机构定制、只供该机构使用。
2. 好处：任何有网络的地方/设备都能访问；方便共享与协作；不需要本地大容量存储；服务商负责备份与恢复；容量可随时扩充；少量免费。
3. 缺点：没有网络就无法访问；对备份与安全没有控制权、依赖第三方；上传下载可能很慢；服务商故障导致无法访问；额外容量要付费、长期可能更贵。
4. 私有云 vs 公有云：不依赖第三方 → 对安全/隐私、备份有更大控制；存储可按公司需求定制。
5. “Discuss”题好处与缺点都要写，否则封顶（⟦9618_s26_12:6(d)⟧ 的 MS：只写一边最多 3 分）。

**得分表述**（引自对应 MS）
- 「Accessing a service/files/software on a remote server」⟦9618_s22_13:8(a)⟧
- 「Dedicated/bespoke services/storage on a remote server only available to company」⟦9618_s24_13:5(a)(i)⟧
- 「Public is open/available to anyone with the appropriate equipment/software/credentials」⟦9618_s22_13:8(b)⟧
- 「Not reliant on a third party」⟦9618_s24_13:5(a)(ii)⟧
- 「The data can be accessed from any computer with an internet connection」⟦9618_w25_12:8(a)(i)⟧
- 「The storage/cloud can only be accessed with an internet connection」⟦9618_w25_12:8(a)(ii)⟧

**易错与失分**
- 定义漏掉 **remote**：“storing files online”太含糊。
- 私有云写成“on the company's own computer”：MS 的私有云仍是**远程服务器**上的专用服务，区别在“只供本公司”。
- 好处与缺点不扣情境：情境给了“动画师”“餐厅”“学生”，就写他们能做什么、怕什么。
- “security is better”和“security is worse”都可能出现在 MS 里：看题问的是好处还是缺点，并说明原因（服务商有专业安全措施 / 自己无法控制安全）。

#### 代表题精讲　⟦9618_s24_13:5(a)(ii)⟧

**在考什么**　多媒体设计公司为员工建了私有云。Describe the benefits to the company of using private cloud storage instead of public cloud storage. 3 分。

**完整作答**　私有云不依赖第三方提供商，所以公司对数据的安全与隐私有更大的控制，对备份也有更大的控制；而且存储可以按公司的需要定制，比如可访问的存储量、员工之间怎样共享文件。

**与 MS 对齐**　“Not reliant on a third party”→“… gives greater control over security/privacy”→“… gives greater control over backup”→“Storage can be tailored/scalable to company requirements”，四点取三。

**英文作答句**　The company is not reliant on a third party, which gives it greater control over the security and privacy of its work and greater control over backup. The storage can also be tailored to the company's requirements, for example the amount of storage each employee can access.

**迁移与卡点**
- **卡点**：“相对于什么”。私有云对公有云的好处是“不依赖第三方 → 对安全、备份、定制有更大控制”；公有云对本地服务器的缺点是“依赖网络与第三方”。先圈出题目 instead of / compared to 后面的那个对象，每一点都写成“比它多了 / 少了什么”。
- **考官在换什么**：定义（remote 不能漏）、公有 / 私有的对比方向、好处还是缺点、是否 discuss（两面都写）；情境（动画师、餐厅、学生）决定展开句里的例子。
- **从代表题到变式**：代表题是三个独立的好处；变式是“两个缺点，每个点 + 展开”——不是三个点，而是两组“缺点 + because”。搬过去的是同一张好处 / 缺点清单；要换的是答案的形状。
- **反例**：私有云写成“公司自己的电脑上”——私有云仍在远程服务器上，区别只是“只供本公司”。

**下一道变式**　⟦9618_w23_13:3(a)(ii)⟧　（反方向：公有云相对 LAN 服务器的两个缺点，每个缺点“点 + 展开”。）

<!-- auto:drills P1-CM-08 -->

### P1-CM-09　互联网与万维网基础设施　{#P1-CM-09}

<!-- auto:stats P1-CM-09 -->

**考法**　①浏览器怎样用 URL 访问网页（经 DNS 得到 IP，4 分）；②调制解调器、专线在互联网传输中的作用；③PSTN 的作用；④蜂窝网络怎样传数据；⑤判断某个活动用的是互联网、万维网还是两者（2021 扩展卷）。

**识别信号**　Uniform Resource Locator (URL) … web browser … Domain Name Service (DNS)；modems / dedicated lines / PSTN；Explain how data is transmitted using the cell phone network；internet … World Wide Web (WWW) … or both。

**解题思路**
1. **URL → 网页**的顺序：浏览器先查缓存 → 解析 URL，拆出域名 → 向 **DNS 服务器**查询域名对应的 **IP 地址** → 收到 IP → 与该 IP 的网络服务器建立连接并发送资源请求 → 收到后渲染显示 → IP 存入缓存备用。
2. **调制解调器**：数字信号 ↔ 模拟信号，以便在电话线上传输。**专线**：直接、私有的连接，因而更快。**PSTN**：由多种通信线路组成，数据可能要转成模拟信号，双向同时传输，经过不同的交换中心/ISP。
3. **蜂窝网络**：地面分成蜂窝小区；每个小区有带天线的基站收发数据；手机与基站之间用低功率无线电信号传输；多台设备可同时与同一基站通信。
4. **互联网 vs 万维网**：互联网是网络的基础设施（硬件与线路）；万维网是通过互联网访问的网站与网页的集合。

**得分表述**（引自对应 MS）
- 「The browser finds the IP address for the domain name by querying a DNS server」⟦9618_w25_11:7(c)⟧
- 「The browser receives the matching IP address from the DNS server」⟦9618_w25_11:7(c)⟧
- 「A request for the resource is sent to the web server with that IP address」⟦9618_w25_11:7(c)⟧
- 「Converts digital data into analogue for transmission down phone lines」⟦9618_s25_11:2(c)⟧
- 「Used to provide a direct / private connection which therefore provides faster transmission」⟦9618_s25_11:2(c)⟧
- 「Each cell has a tower with an antenna which receives and transmits data」⟦9618_s25_12:6(b)⟧

**易错与失分**
- URL 题跳过 DNS：没有“查询 DNS 服务器得到 IP 地址”，核心两分就丢了。
- 写“DNS finds the website”：DNS 返回的是 **IP 地址**，网页是向那个 IP 的网络服务器请求来的。
- 把互联网和万维网当同义词。

#### 代表题精讲　⟦9618_w25_11:7(c)⟧

**在考什么**　用户在地址栏输入 URL。Explain how the web browser uses the URL to access the web page. 4 分，MS 8 点取 4。

**完整作答**　浏览器先检查自己的缓存里有没有这个 URL。没有的话，浏览器解析 URL，取出域名，向 DNS 服务器查询该域名对应的 IP 地址；DNS 服务器返回匹配的 IP 地址。浏览器与这个 IP 地址的网络服务器建立连接，发送对该网页资源的请求；收到响应后渲染并显示网页，并把 IP 地址存入缓存供以后使用。

**与 MS 对齐**　“The browser checks its cache for the URL”“The browser parses the URL and splits it into its component parts”“The browser finds the IP address for the domain name by querying a DNS server”“The browser receives the matching IP address from the DNS server”“The browser creates connection with the web server with the matching IP address”“A request for the resource is sent to the web server with that IP address”“The browser renders and displays the result”“The IP address is stored in the browser cache for future use”。

**英文作答句**　The browser parses the URL and finds the IP address for the domain name by querying a DNS server. The browser receives the matching IP address from the DNS server. A request for the resource is sent to the web server with that IP address, and the browser renders and displays the result.

**下一道变式**　⟦9618_s25_12:6(b)⟧　（换成蜂窝网络怎样传数据。）

<!-- auto:drills P1-CM-09 -->

### P1-CM-10　IP 地址　{#P1-CM-10}

<!-- auto:stats P1-CM-10 -->

**考法**　①IPv4 / IPv6 的格式（组数、每组位数、分隔符、进制、总位数）——常做成填空；②两者的区别；③判断一个地址是 IPv4、IPv6 还是不合法并说明理由（选择不给分）；④公有/私有、静态/动态 IP 的含义、用途（填表、连线、“static private IP 是什么意思”）。

**识别信号**　IPv4 / IPv6 … groups / bits / full stops / colons / hexadecimal；Explain why this is not an IPv6 address；Circle whether this IP address is IPv4, IPv6 or invalid；public / private / static / dynamic IP address；Complete the description of IP addresses。

**解题思路**
1. 背一张对照表：

| | IPv4 | IPv6 |
|:--|:--|:--|
| 组数 | 4 组 | 8 组 |
| 每组 | 8 位，十进制 0–255 | 16 位，十六进制 0–FFFF |
| 分隔符 | 句点（full stop） | 冒号（colon） |
| 总位数 | 32 位 | 128 位 |
| 简写 | — | 连续的全 0 组可用 `::` 代替（只能一次） |

2. 判断合法性：逐条对表——IPv4 每组 ≤ 255、只有数字；IPv6 用冒号、8 组、十六进制。说理由时两种都要排除。
3. 四种类型：**public**——在互联网上可见、可被访问；**private**——只在本 LAN 内可见，由 LAN 内的路由器分配；**static**——每次连接都不变；**dynamic**——每次连接可能重新分配。“static private”= 两个含义都写。

**得分表述**（引自对应 MS）
- 「IPv4 is 32 bits whilst IPv6 is 128 bits」⟦9618_s24_11:8(b)(ii)⟧
- 「IPv4 is usually represented in denary whilst IPv6 is usually represented in hexadecimal」⟦9618_s24_11:8(b)(ii)⟧
- 「Multiple consecutive groups of zeros can be replaced with a double colon」⟦9618_s25_12:6(c)⟧
- 「to be visible to and accessible by other devices on the internet」⟦9618_s24_11:8(b)(i)⟧
- 「Static means the IP for that device does not change and Private means it can only be accessed/seen/used within the LAN」⟦9618_s24_13:5(d)⟧
- 「It is not IPv4 because the maximum denary value should be 255, this uses 256」⟦9618_w25_11:7(b)⟧

**易错与失分**
- 题干已经给出的区别（如⟦9618_s24_11:8(b)(ii)⟧ 已说“句点 vs 冒号”）不能再写。
- IPv6 每组是 **16 位**（4 个十六进制数字），不是 8 位。
- “static private IP”只解释了一半：MS 要求一句话里两个含义都说（⟦9618_s26_11:7(c)(i)⟧ 写明 1 mark for a complete answer）。
- 判断不合法时只排除一种格式：要同时说明为什么不是 IPv4、为什么不是 IPv6。

#### 代表题精讲　⟦9618_s25_12:6(c)⟧

**在考什么**　IP 地址描述填空，6 空各 1 分。

**完整作答**　依次填：**full stops**（IPv4 分隔符）；**hexadecimal**（IPv6 每组 4 个十六进制数字）；**zeros**（连续全 0 组可用双冒号代替）；**128**（IPv6 位数）；**dynamic**（每次连接可能改变）；**private**（只能被同一 LAN 的设备访问、由 LAN 内路由器分配）。

**与 MS 对齐**　MS 的六个词：full stops、hexadecimal、zeros、128、dynamic、private。最后两空要从描述反推类型：“can change each time”→ dynamic；“only be accessed by other devices in the same LAN … assigned by the router”→ private。

**英文作答句**　IPv4 is made of four groups of 8-bit numbers separated by full stops. IPv6 is made of eight groups of 4 hexadecimal numbers separated by colons; multiple consecutive groups of zeros can be replaced with a double colon, and each IPv6 address is 128 bits. A dynamic IP address can change each time the computer connects to a network; a private IP address can only be accessed by devices in the same LAN.

**迁移与卡点**
- **卡点**：IPv6 每组 16 位（4 个十六进制数字），不是 8 位；static / dynamic 和 public / private 是两组互不相关的属性，“static private”要两个含义都说。
- **考官在换什么**：问格式（填空、区别）、问合法性（圈出并说理由）、问四种类型的含义——全都来自那张 IPv4 / IPv6 对照表。
- **从代表题到变式**：代表题是按描述填词；变式是判断一个地址——用对照表逐条对：有字母就不是十进制的 IPv4，某一组超过 255 也不是；用句点、只有 4 组又不是 IPv6。理由要**两种格式都排除**。搬过去的是对照表；要换的是用法（从填表变成逐条核对）。
- **反例**：题干已给的区别（句点 vs 冒号）再写一遍；判断题只排除一种格式。

**下一道变式**　⟦9618_w25_11:7(b)⟧　（判断 256.0.0.A 是 IPv4、IPv6 还是不合法，并说两条理由。）

<!-- auto:drills P1-CM-10 -->

### P1-CM-11　子网划分　{#P1-CM-11}

<!-- auto:stats P1-CM-11 -->

**考法**　①子网划分的目的/好处（常是“好处 + 展开”成对给分）；②子网中 IP 地址的两部分：network ID 与 host ID；③给出 IP 地址与子网掩码，写出网络 ID 或主机 ID。

**识别信号**　subnetting / subnetworks / subnet mask；Describe two benefits of subnetting a network；Describe the purpose of subnetting；network ID / host ID。

**解题思路**
1. 目的：把一个大网络分成**更小的网络**。
2. 好处四个方向，每个都要带“因为/所以”：
   - **流量与性能**：同一子网内的数据只在子网内走 → 减少其他部分的流量与拥塞。
   - **安全**：不是所有设备都能访问所有网段；一台设备被攻破不会暴露整个网络。
   - **管理与维护**：故障能被隔离；维护一个子网时其他子网照常工作。
   - **扩展**：更容易扩展网络、可用的 IP 地址范围更大。
3. 两部分：同一子网内所有设备 **network ID 相同**；每台设备的 **host ID 不同**，在子网内唯一标识它。
4. 用子网掩码求 ID：掩码为 255 的组属于网络 ID，为 0 的组属于主机 ID。例：172.16.5.9，掩码 255.255.0.0 → 网络 ID 172.16，主机 ID 5.9。
5. “just faster”不够（MS 标 NE）：要写“reduces congestion / traffic stays within the subnet”。

**得分表述**（引自对应 MS）
- 「It allows the network to be divided into smaller networks」⟦9618_w24_13:9(d)(ii)⟧
- 「which reduces traffic in some parts of the network // reduces congestion」⟦9618_w24_13:9(d)(ii)⟧
- 「To improve the security of the LAN」⟦9618_w23_12:7(b)(iii)⟧
- 「so that a compromised device does not expose the whole network」⟦9618_w23_12:7(b)(iii)⟧
- 「IP address is made up of a network ID and a host ID」⟦9618_s23_13:2(e)⟧
- 「the host ID uniquely identifies the device within the subnetwork」⟦9618_s23_13:2(e)⟧

**易错与失分**
- 只写“faster”或“more efficient”：⟦9618_s26_11:7(c)(ii)⟧ 的 MS 明写“just faster is NE”。
- 题干已给的理由不能重复（⟦9618_w23_12:7(b)(iii)⟧ 已给“separate a network into logical segments”，要写**其他**理由）。
- network ID 与 host ID 的描述没说“相同 / 不同”：这是描述分的关键词。

#### 代表题精讲　⟦9618_w23_12:7(b)(iii)⟧

**在考什么**　Describe two other reasons why subnetting is used in a network. 4 分：每个理由 1 + 对应展开 1。

**完整作答**
1. 提高 LAN 的安全：一台设备被攻破时，攻击不会暴露整个网络；而且不是所有设备都能访问所有网段。
2. 减少网络拥塞：通信被限制在本地——同一子网内设备之间的数据只留在该子网内，其他设备不会被大量无关数据淹没。

**与 MS 对齐**　理由 1 ←“To improve the security of the LAN”，展开 ←“… so that a compromised device does not expose the whole network”（或“… so not all devices can access all segments”）；理由 2 ←“To reduce network congestion”，展开 ←“… because data sent between devices on the same subnet stays within the subnet”。

**英文作答句**　1. To improve the security of the LAN, so that a compromised device does not expose the whole network. 2. To reduce network congestion, because data sent between devices on the same subnet stays within the subnet.

**下一道变式**　⟦9618_w22_13:7(c)(ii)⟧　（给 IP 地址和子网掩码，写出网络 ID 与主机 ID。）

<!-- auto:drills P1-CM-11 -->

### P1-CM-12　位流传输　{#P1-CM-12}

<!-- auto:stats P1-CM-12 -->

**考法**　①位流是什么；②实时与点播位流的区别；③解释实时位流（如视频会议）怎样传输数据（4 分）。另有一批压缩题以它为副题型：实时流媒体为什么要压缩、为什么选有损——那些题的主题型在 IR-13 / IR-14，得分点里的“缓冲、实时、流畅播放”属于本型知识（判定规则见 `adjudication.csv`）。

**识别信号**　State what is meant by bit streaming；real-time and on-demand bit streaming；Explain how data is transferred using real-time bit streaming；Explain how bit streaming is used in a real-time video conference。

**解题思路**
1. 定义：在通信路径上连续、有序的位流。
2. 传输过程（按顺序）：（先压缩）→ 视频/音频作为一串位**连续**传输 → 上传到**媒体服务器** → 用户下载时，媒体服务器把数据送入用户设备的**缓冲区** → 缓冲区暂存数据，直到接收方能够处理（抹平发送与接收的速度差）→ 接收方从缓冲区读取并播放。
3. 实时 vs 点播：实时直接来自源头，不能回看，连续播放；点播是预先录好、存在服务器上，可暂停、回看，按段下载。
4. 带宽/比特率：带宽不足 → 缓冲区被取空 → 卡顿。

**得分表述**（引自对应 MS）
- 「Continuous ordered flow of bits over a communication path」⟦9618_s24_11:2(e)(i)⟧
- 「Video is transmitted continuously」⟦9618_s25_11:2(a)⟧
- 「The video is uploaded to a media server」⟦9618_s25_11:2(a)⟧
- 「On download, the media server sends the data to a buffer on the user's device」⟦9618_s25_11:2(a)⟧
- 「Buffer stores data from server until recipient can receive it」⟦9618_s25_11:2(a)⟧
- 「Real-time cannot be re-watched, on-demand can be paused, re-watched」⟦9618_s24_11:2(e)(ii)⟧

**易错与失分**
- 不提**缓冲区**：位流题一半的得分点围绕 buffer。
- 把实时位流说成“下载完再播放”：那恰恰是点播按段下载、或普通下载的特征。
- 区别题只写一边：“real-time is live”要配“on-demand is pre-recorded”。

#### 代表题精讲　⟦9618_s25_11:2(a)⟧

**在考什么**　程序员开实时视频会议。Explain how data is transferred using real-time bit streaming. 4 分，MS 8 点取 4。

**完整作答**　视频被编码成一串位，连续不断地传输。发送方把视频上传到媒体服务器，参会者从媒体服务器下载。下载时，媒体服务器把数据送进用户设备上的缓冲区；当传输速度和接收速度不一致时，缓冲区先把服务器发来的数据存起来，直到接收方能处理；接收方从缓冲区读取位流来观看。

**与 MS 对齐**　“Video is transmitted continuously”“as a series of bits”“The video is uploaded to a media server”“The users download from the media server”“On download, the media server sends the data to a buffer on the user's device”“buffer is used when there is a difference in speed between transmission and receipt”“Buffer stores data from server until recipient can receive it”“Recipient views bit stream from the buffer”。

**英文作答句**　The video is transmitted continuously as a series of bits. The video is uploaded to a media server, and on download the media server sends the data to a buffer on the user's device. The buffer stores data from the server until the recipient can receive it, and the recipient views the bit stream from the buffer.

**下一道变式**　⟦9618_s24_11:2(e)(ii)⟧　（实时与点播位流的两个区别。）

<!-- auto:drills P1-CM-12 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| CM-01 vs CM-03 | LAN/WAN 看范围与归属；拓扑看线怎么连 | geographical area / infrastructure vs bus / star / mesh |
| CM-02 vs CM-08 | 客户端-服务器写谁发请求、谁处理；云写远程服务、公有/私有与利弊 | roles of devices / thin-client vs cloud / public / private |
| CM-03 vs CM-04 | 拓扑的结构与优缺点 vs 数据包一步步怎么走 | advantage / draw vs how packets are transmitted |
| CM-04 vs CM-07 | 只说数据怎么走 → CM-04；涉及冲突、侦听、阻塞信号 → CM-07 | collision / CSMA/CD / Ethernet |
| CM-05 vs CM-09 | 路由器、交换机、WAP、网桥 → CM-05；调制解调器、PSTN、专线、蜂窝网络、DNS → CM-09 | 设备名 |
| CM-10 vs CM-11 | IP 的格式与类型 → CM-10；网络 ID、主机 ID、子网掩码、子网的好处 → CM-11 | subnet |
| 交换机 vs 路由器 | 交换机按 MAC 地址在 LAN 内转发；路由器按 IP 地址在网络之间选路 | MAC address vs IP address / routing table |
| CM-12 vs IR-13/IR-14 | 位流怎么传、实时与点播 → CM-12；流媒体为什么压缩、选有损还是无损 → IR-13/IR-14（副题型 CM-12） | compress / lossy 出现在题干 |
| CM-12 vs HW-06 | 位流整体过程 → CM-12；只问缓冲区的作用 → HW-06 | purpose of the buffer |
