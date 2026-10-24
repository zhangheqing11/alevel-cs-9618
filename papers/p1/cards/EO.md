## EO　伦理与所有权 {#ch-EO}

<!-- auto:chapter-stats -->

### 核心思想

这一章讲**写软件、用软件的人要守什么规矩，软件归谁**，再加上 AI 这个当下最大的伦理话题。三块：

1. **职业伦理**（EO-01、EO-02）：程序员为什么要加入 BCS、IEEE 这样的职业道德团体（有准则可依、客户信得过、有法律支持与培训），行为准则有什么用；在具体情境中怎样对同事、客户、公众合乎道德地做事。
2. **所有权**（EO-03）：版权保护作者的知识产权；软件许可规定别人能怎样用：商业软件、共享软件、开源（OSI）、自由软件（FSF）四种，要会认、会选、会论证。
3. **人工智能**（EO-04、EO-05）：AI 在给定系统里**怎样工作**（图像/人脸/字符/语音识别，与训练数据比对，按概率选最可能的结果，学习改进），以及它带来的**影响**（社会、经济、伦理、环境，好坏两面）。

本章题目短、分值不高，但 MS 的得分点很“松”：大多是 e.g. 列出的一串可接受答案。拿分的关键是**每个点写出“做什么 + 为什么 / 所以”**——MS 里大量以 `…` 开头的展开点，就是给“所以”的分。

**心智模型**　本章所有题都在一张**三方关系图**上：开发者（你）、雇主 / 客户、公众（用户、社会、环境）。约束来自三处——法律（版权、数据保护）、许可（软件归谁、别人能怎样用，EO-03）、职业道德团体的行为准则（EO-01）。“合乎道德地行事”（EO-02）就是在某个情境里对三方各尽一条义务：对雇主诚实与胜任，对客户保密与按约交付，对公众安全与不伤害；每条义务写成“做什么 + 对谁 + 所以避免了什么”。AI 两型（EO-04、EO-05）把公众这一角放大：先说清系统怎样做决定（和训练数据比较、按概率选最像的，还会学习改进），再分社会 / 经济 / 伦理 / 环境四类说它对谁有什么影响，好坏两面都写。看到一道 EO 题，先定位“问的是哪一方对哪一方、约束来自哪一处”，再按“做什么 + 所以”写。

### 题型树
<!-- auto:type-tree -->

### P1-EO-01　职业道德团体与行为准则　{#P1-EO-01}

<!-- auto:stats P1-EO-01 -->

**考法**　①解释程序员为什么要加入职业道德团体（3–4 分）；②描述不加入可能的后果（3 分，即好处的反面）；③描述行为准则（code of conduct）的目的（2 分）。

**识别信号**　professional ethical body；BCS；IEEE；join；benefits；consequences of … not joining；code of conduct。

**解题思路**　加入的好处背四条，每条都带一个 “…so” 展开：

| 好处 | 展开（…so） |
|:--|:--|
| 有成文的伦理准则可以遵循 | 客户与同事知道你按什么标准做事；不必自己判断什么算合乎道德 |
| 客户知道你可靠 | 入会可能有考试或门槛，等于认可了你的技能与知识 |
| 团体提供帮助与支持 | 例如需要法律咨询时 |
| 团体开办培训课程 | 让技能保持最新 |

- **不加入的后果**就是把四条反过来写：没有或很少有法律咨询（被起诉时）；人脉少（错过联系人与工作）；培训少；没有清楚的伦理准则、也没人可商量 → 可能做出不道德的事 → 可能惹上官司。
- **行为准则的目的**：营造安全、专业的工作环境；让员工明白期望和行为后果；给出什么是好做法的清楚规则；保护组织声誉、维持公众信任。

**得分表述**（引自对应 MS）
- 「The programmer has ethical guidelines to follow」⟦9618_w23_13:6(b)⟧
- 「so programmer does not have to decide what is ethical or not」⟦9618_w23_13:6(b)⟧
- 「Clients know programmer is reputable」⟦9618_w23_13:6(b)⟧
- 「Professional ethical body provides help and support」⟦9618_w23_13:6(b)⟧
- 「There is no / limited access to legal advice」⟦9618_s25_13:3(d)⟧
- 「so there are clear rules to follow in certain situations」⟦9618_w25_12:2(b)⟧

**易错与失分**
- 只写“to be ethical / to follow rules”而不写展开：一个点往往只值一分，展开那一分更容易拿。
- 写成“必须加入，否则不能工作 / 违法”：加入职业团体不是法律要求，MS 没有这类点。
- 后果题写成好处题：题目问 consequences of **not** joining，要写“缺少……所以……”。

#### 代表题精讲　⟦9618_w23_13:6(b)⟧

**在考什么**　Explain why it is important for a programmer to join a professional ethical body. 4 分，四个好处点各带展开。

**完整作答**
1. 程序员有成文的伦理准则可以遵循，所以买程序的人知道他按什么标准做事；
2. 程序员也不必自己去判断什么合乎道德、什么不合乎；
3. 客户知道这位程序员可靠——入会可能有考试，等于认可了他的技能和知识；
4. 团体提供帮助和支持，例如法律咨询；还可以参加团体的培训课程，让技能保持最新。

**与 MS 对齐**　1 ←“The programmer has ethical guidelines to follow”+“…so purchasers of programs know the standards being applied”；2 ←“…so programmer does not have to decide what is ethical or not”；3 ←“Clients know programmer is reputable”“There may be an entry requirement / exam”“… so clients know that the programmer is competent”；4 ←“Professional ethical body provides help and support”“Such as legal advice”“Enables programmer to attend the ethical body’s training courses”“…to keep skills up to date”。MS 共 11 点，写出 4 个独立点即满分。

**英文作答句**　The programmer has ethical guidelines to follow, so purchasers of programs know the standards being applied and the programmer does not have to decide what is ethical or not. Clients know the programmer is reputable because there may be an entry requirement or exam. The ethical body provides help and support, such as legal advice, and runs training courses to keep the programmer’s skills up to date.

**直观**　加入职业团体像律师加入律师协会：有统一的执业规范，客户看到会员资格就放心，遇到纠纷有人撑腰，还有继续教育。

**下一道变式**　⟦9618_s25_13:3(d)⟧　（反过来问：不加入会有什么后果，3 分；把每个好处改写成“缺少……所以……”。）

<!-- auto:drills P1-EO-01 -->

### P1-EO-02　合乎道德地行事　{#P1-EO-02}

<!-- auto:stats P1-EO-02 -->

**考法**　①解释程序员为什么要对同事和公众合乎道德地行事（两边各 2 分）；②给出学生用个人电脑连学校网络时的其他伦理考虑（3 分）；③（2021 扩展）给定情境中怎样做才合乎道德、为什么某人的做法不道德。

**识别信号**　act ethically；ethical considerations；towards colleagues / the public / the client；Explain the reasons why … did not act ethically。

**解题思路**
1. 先找出这个情境里**受影响的对象**：同事、客户（雇主）、公众、产品、职业本身、自己。
2. 对每个对象写“应该怎样做 + …so that 为什么”：
   - 同事：公平对待、不歧视；愿意接受和提出批评（…技术工作得以改进）；承认同事的贡献（…让他们感到被重视）；帮助、培训同事。
   - 公众：维护公众的健康、安全与福祉（…不危及任何人）；对软件的宣传诚实、实事求是（…维持公众信任）；保护公众数据的安全。
   - 客户 / 产品：发现错误要报告（否则产品可能失败、客户被辜负）；不懂的工具如实告诉经理并主动学习。
3. 学生连学校网络的伦理考虑：隐私；不滥用社交网络、不网络霸凌；不抄袭别人的作品；遵守学校的网络使用规定；只做正当用途；不入侵其他电脑。

**得分表述**（引自对应 MS）
- 「Treat colleagues fairly and avoid acts of discrimination」⟦9618_w24_12:5(a)⟧
- 「Credit the contributions of colleagues」⟦9618_w24_12:5(a)⟧
- 「Maintain the health, safety and welfare of the public」⟦9618_w24_12:5(a)⟧
- 「Be honest / realistic in making claims about the software」⟦9618_w24_12:5(a)⟧
- 「Students should not copy work that is not their own」⟦9618_w25_11:8(b)⟧
- 「He didn’t act in best interest of client」⟦9618_w21_11:4(c)⟧

**易错与失分**
- 同事、公众两栏写成同一件事（“be honest”写两遍）：MS 两栏分别封顶，各写各的。
- 只写“be ethical / be nice”：要写具体行为。
- 学校网络题又写题干已给的“传播恶意软件”。
- “为什么要合乎道德”只列行为不写理由：分值高的题常给 …so that 那一分。

#### 代表题精讲　⟦9618_w24_12:5(a)⟧

**在考什么**　Explain the reasons why the computer programmer needs to act ethically towards colleagues and the public. 4 分，同事最多 2、公众最多 2。

**完整作答**
- 同事：程序员应公平对待同事、避免歧视；应愿意接受和提出批评，这样技术工作才能改进；应承认同事的贡献，让他们感到被重视。
- 公众：程序员应维护公众的健康、安全与福祉，不危及任何人；对软件的宣传要诚实、实事求是，这样才能维持公众信任。

**与 MS 对齐**　Colleagues ←“Treat colleagues fairly and avoid acts of discrimination”“Be prepared to accept / offer critique”“… so that technical work can be improved”“Credit the contributions of colleagues”“… so that they feel valued / respected”；Public ←“Maintain the health, safety and welfare of the public”“… so as not to endanger anyone”“Be honest / realistic in making claims about the software”“… so that public trust is maintained”。两栏各写 2 点。

**英文作答句**　Colleagues: the programmer should treat colleagues fairly and avoid acts of discrimination, and should be prepared to accept and offer critique so that technical work can be improved. The public: the programmer should maintain the health, safety and welfare of the public so as not to endanger anyone, and should be honest and realistic in making claims about the software so that public trust is maintained.

**直观**　对内像好队友（公平、肯定别人、互相指正），对外像好医生（不害人、不夸大疗效）。

**下一道变式**　⟦9618_w25_11:8(b)⟧　（情境换成学生用个人电脑连学校网络：给出三条“其他”伦理考虑。）

<!-- auto:drills P1-EO-02 -->

### P1-EO-03　版权与软件许可　{#P1-EO-03}

<!-- auto:stats P1-EO-03 -->

**考法**　①按描述写出许可名称（表格 3–4 分）；②描述某种许可的特征（commercial、Free Software）；③给出用 shareware / commercial 许可发布的好处；④按情境选出最合适的许可并论证（licence 1 分 + 理由）；⑤允许别人修改并再发布时可用哪两种许可（OSI、FSF）；⑥为什么要给程序申请版权；为什么某程序不适合开源；⑦术语表：copyright、open source、shareware、software licence。

**识别信号**　copyright；intellectual property；software licence；commercial / proprietary；shareware；open source (initiative)；free software (foundation)；Identify the most appropriate type of software licence … justify；allow … to edit and redistribute。

**解题思路**
1. 四种许可对照（先背这张表）：

| | Commercial | Shareware | Open Source Initiative | Free Software Foundation |
|:--|:--|:--|:--|:--|
| 费用 | 购买才能用 | 先免费试用，之后可能要付费 | 通常免费（也可收费） | 不一定免费（free = 自由，不是免费） |
| 源代码 | 不给 | 不给 | 随程序提供 | 随程序提供 |
| 能否修改 | 不能（合法地） | 不能 | 能 | 能 |
| 能否再发布 | 不能 | 试用版可以传播 | 能，遵守具体许可证条款 | 能，遵守具体许可证条款 |
| 特点 | 受版权保护，常有支持与更新、测试充分 | 试用期或功能受限；受版权保护 | 鼓励协作、用户报告并修复错误 | 强调用户的自由：运行、研究、修改、分享 |

只有采用要求保留相同许可或自由的 copyleft 许可证时，修改版再发布才受相应要求约束；不能把这种要求推广到所有开源或自由软件许可证。

2. **按情境选**：要卖钱、不想被改 → commercial（或想先让人试玩 → shareware）；要让别人改、再发布 → OSI 或 FSF；情境说“源代码可被企业修改、企业付钱买维护”→ 开源（程序员靠维护和更新赚钱）。
3. **论证**每点写“许可的特征 → 对这个情境的好处”：用户必须付费 → 程序员有收入；受版权保护 → 用户不能合法修改 → 程序员掌控产品、可对盗版采取法律行动。
4. **版权**：给作者对知识产权的合法所有权；防止未经授权的复制；被侵权时可以依法追究。

**得分表述**（引自对应 MS）
- 「Gives the holder the legal right of ownership of intellectual property」⟦9618_w25_12:2(a)⟧
- 「Users have no access to source code」⟦9618_s25_12:3(c)(i)⟧
- 「The user can test/trial the program before purchasing to see whether it meets needs」⟦9618_w24_11:7(a)⟧
- 「The software is not necessarily free of charge」⟦9618_w25_12:10(b)⟧
- 「to allow errors to be reported / identified / fixed by users」⟦9618_w22_13:8(a)(i)⟧
- 「User has to pay for the product so the programmer can gain an income」⟦9618_s23_13:5(b)⟧

**易错与失分**
- 把 Free Software 理解成“免费软件”：FSF 的 free 指自由，MS 有“not necessarily free of charge”这一点。
- 把 shareware 写成“可以修改”：shareware 不给源代码。
- 选许可的题，许可名称本身通常只 1 分，理由必须扣情境（卖给公众、企业要改代码……）。
- 允许修改再发布的两种许可写成 open source 和 shareware：应是 Open Source Initiative 与 Free Software Foundation。
- 版权不是许可：版权是所有权，许可是作者允许别人怎样用的协议。

#### 代表题精讲　⟦9618_s23_13:5(b)⟧

**在考什么**　程序员开发一款要卖给公众的电脑游戏。Identify the most appropriate type of software licence for the game and justify your choice. 4 分 = 许可 1 + 理由最多 3。

**完整作答**　许可：商业软件许可（commercial）。理由：
1. 用户必须付费购买，程序员因此有收入；
2. 程序可以受版权保护；
3. 所以用户不能合法修改程序，程序员保有对产品的控制；
4. 并且可以对非法复制或转卖的人采取法律行动。

**与 MS 对齐**　Licence ←“Commercial software licence”；理由 ←“User has to pay for the product so the programmer can gain an income”“Enables the program to be copyrighted”“... so the user cannot legally edit the program // the programmer retains control over product”“… and can take legal action against people who attempt to illegally copy it /sell it on”。MS 也接受 shareware（理由：先免费试玩、更多人体验从而更可能购买），选哪种都要配那一种的理由。

**英文作答句**　Licence: commercial software licence. The user has to pay for the product so the programmer can gain an income. It enables the program to be copyrighted, so the user cannot legally edit the program and the programmer retains control over the product, and the programmer can take legal action against people who attempt to illegally copy it or sell it on.

**直观**　商业许可像卖书：读者买了能读，但不能改了再印出来卖；开源像菜谱公开分享：谁都能照着做、改良后再分享。

**下一道变式**　⟦9618_w24_12:5(b)(i)⟧　（情境换了：企业可以修改源代码、付钱买维护与安全更新——这次应选哪种许可？）

<!-- auto:drills P1-EO-03 -->

### P1-EO-04　人工智能的应用　{#P1-EO-04}

<!-- auto:stats P1-EO-04 -->

**考法**　解释或描述 AI 在给定系统里怎样工作（3–4 分）：①人脸识别（银行 App、商店识别顾客、相机自动对焦）；②图像识别与 OCR（停车场识别车牌、读取商品标签）；③语音识别与自然语言（点餐机器人、语音转命令）；④CCTV 识别并追踪人；⑤描述一种 AI 应用（应用 1 分 + 描述 2 分）；⑥（2021 扩展）AI 下棋。

**识别信号**　Artificial Intelligence (AI)；Explain / Describe how AI is used in …；facial / image / speech recognition；optical character recognition；natural language。

**解题思路**　写成一条“输入 → 识别 → 比对 → 决定 → 行动 / 学习”的链，每一环落到题目的系统上：
1. **输入**：摄像头拍下图像 / 麦克风录下声音。
2. **用什么识别**：点名技术——image recognition、facial recognition、optical character recognition (OCR)、speech recognition、natural language processing。
3. **怎样识别**：分析像素，找出图案、特征（人脸特征之间的距离、字符形状）；或分析声波。
4. **和什么比对**：与数据库或训练数据（大量图像、已知的字、单词、句子）比较。
5. **怎样决定**：按匹配概率选最可能的结果（最可能的字、词、句子、人）。
6. **之后做什么**：执行对应动作（开闸扣费、对焦、下单）；有的系统会从结果中学习、改进。

**得分表述**（引自对应 MS）
- 「It uses optical character recognition」⟦9618_w24_11:6⟧
- 「The pixels within the registration number area identified are analysed」⟦9618_w24_11:6⟧
- 「Trained to identify the features of a face in an image」⟦9618_s24_11:5(c)(ii)⟧
- 「Uses the probability of a match」⟦9618_s24_11:5(c)(ii)⟧
- 「The audio recordings are compared to a database of words/sound waves」⟦9618_s24_13:7(b)⟧
- 「and generates the most likely sentence / command / word」⟦9618_s23_12:7(d)⟧

**易错与失分**
- 只写“AI learns / AI thinks”：要写出识别技术的名称和比对过程。
- 讲成系统的硬件流程（传感器、执行器）：那是 HW-08 / HW-09，本型只给 AI 怎样识别、比对、决定的分。
- 题干提到生物认证，但问的是 AI 怎样做人脸识别：不要写成安全措施（SP-03）。
- 写影响（“方便顾客、省人工”）：那是 EO-05。

#### 代表题精讲　⟦9618_w24_11:6⟧

**在考什么**　停车场用摄像头记录进出车辆的车牌。Explain how artificial intelligence is used in the car park system to identify the car’s registration number. 4 分。

**完整作答**
1. 系统使用图像识别：存下摄像头拍到的每幅图像的像素；
2. 把像素与车牌应有的形状、大小、颜色比对，找出车牌所在的区域；
3. 系统使用光学字符识别（OCR）：分析车牌区域内的像素；
4. 与预期的字符（字母、数字）比对，得出车牌号。

**与 MS 对齐**　1 ←“It uses image recognition”“The pixels of each image from the camera are stored”；2 ←“… and matched to the expected shape/size/colour of registration number”；3 ←“It uses optical character recognition”“The pixels within the registration number area identified are analysed”；4 ←“… and compared to expected characters/letters/numbers”。MS 共 6 点，写满 4 点。

**英文作答句**　The system uses image recognition: the pixels of each image from the camera are stored and matched to the expected shape, size and colour of a registration plate. It then uses optical character recognition: the pixels within the registration number area are analysed and compared to the expected characters, letters and numbers to identify the registration number.

**直观**　像人看车牌：先在整张照片里找到那块长方形的牌子，再一个字一个字地认。

**下一道变式**　⟦9618_s24_13:7(b)⟧　（换成语音：顾客对机器人说话点餐，AI 怎样认出说的是什么。）

<!-- auto:drills P1-EO-04 -->

### P1-EO-05　人工智能的影响　{#P1-EO-05}

<!-- auto:stats P1-EO-05 -->

**考法**　描述 AI 应用带来的某一类影响：①社会影响（学生用 AI 做作业、机场人脸识别、读标签程序的社会好处）；②经济影响（汽车修理厂的 AI 诊断模块）；③伦理影响（课堂上用 AI 分析学生视频）。常 2 分（影响 1 + 展开 1），也有 4 分（两个影响各 2）。

**识别信号**　social / economic / ethical / environmental impact(s)；social benefits；Describe … impact(s) of … AI。

**解题思路**
1. 看清题目问哪一类影响，只写那一类：
   - **社会**：对人的生活、交流、能力、公平、安全感（技能退化、交流减少、数字鸿沟、错误信息；帮助视障或不懂语言的人、更安全、犯罪减少）。
   - **经济**：对成本、利润、价格、就业（诊断更快 → 成本降低；完成更多工作 → 利润增加；软件贵 → 利润率降低）。
   - **伦理**：对隐私、公平、心理健康（持续监控带来隐私顾虑、压力与焦虑；也可能及早发现需要帮助的学生）。
2. 每个影响写两截：**影响本身 + “…because / so” 的具体机制**，扣题目的情境。
3. 题目没限定好坏时，好坏都可以写；“benefits”只写好处。

**得分表述**（引自对应 MS）
- 「The AI answer might not be correct leading to mis-information」⟦9618_w25_11:8(c)⟧
- 「Emphasises the digital divide// some students may not have access to the technology」⟦9618_w25_11:8(c)⟧
- 「reduce costs to the garage」⟦9618_w22_13:8(b)⟧
- 「because less time taken for diagnosis」⟦9618_w22_13:8(b)⟧
- 「There could be privacy concerns」⟦9618_w25_13:7(a)⟧
- 「It can help people with visual impairment to identify which products to purchase」⟦9618_s25_12:3(b)⟧

**易错与失分**
- 问经济影响却写“更方便、更准确”：要落到钱上（成本、利润、价格、顾客数）。
- 只写“good / bad for society”：要写出具体的人受到什么影响。
- 把 AI 怎样工作写进来：那是 EO-04，不给分。
- 两个影响写成同一件事的两种说法（“学不到东西”和“技能下降”只算一个）。

#### 代表题精讲　⟦9618_w25_11:8(c)⟧

**在考什么**　Describe two social impacts of students using Artificial Intelligence (AI) to complete their homework. 4 分；按学习与人际交流两项影响组织答案，覆盖 4 个独立 MS bullet，同一 bullet 内的 `//` 是替代表述，不累计给分。

**完整作答**
- 影响 1（学习）：学生用 AI 走捷径，可能错过培养推理和解决问题能力的机会；AI 的答案也可能不正确，导致学生接触错误信息。
- 影响 2：过度依赖 AI 会减少协作、团队合作和面对面交流的机会，对学生的沟通能力不利；屏幕时间增加、更孤立，可能加重焦虑或孤独。
- （其他可选要点：凸显数字鸿沟——有的学生用不上这些技术；正面的：获得额外帮助的学生可能学得更好。）

**与 MS 对齐**　MS p.13 每个 bullet 1 分、封顶 4 分；上面的两项影响覆盖以下 4 个独立 bullet：

| 作答位置 | 对应 MS 原文 | 分值 |
|:--|:--|:-:|
| 影响 1：错过能力培养 | 「If students use AI to shortcut learning, they may miss out on developing reasoning and problem-solving skills」⟦9618_w25_11:8(c)⟧ | 1 |
| 影响 1：错误答案造成错误信息 | 「The AI answer might not be correct leading to mis-information」⟦9618_w25_11:8(c)⟧ | 1 |
| 影响 2：交流与协作减少 | 「heavy reliance on AI may limit opportunities for collaboration, teamwork, and face-to-face communication」⟦9618_w25_11:8(c)⟧ | 1 |
| 影响 2：焦虑或孤独 | 「Increased screen time and isolation could contribute to anxiety or loneliness」⟦9618_w25_11:8(c)⟧ | 1 |

第一行所在 bullet 中的 not learning / decline in skills 是替代表述，不能另计分。

**英文作答句**　1. If students use AI to shortcut their homework, they may miss out on developing reasoning and problem-solving skills. AI answers may also be incorrect, leading to misinformation. 2. Heavy reliance on AI may limit opportunities for collaboration, teamwork and face-to-face communication. Increased screen time and isolation could contribute to anxiety or loneliness.

**直观**　AI 写作业像请人代跑步：成绩单上看着不错，腿上的肌肉却没长出来。

**下一道变式**　⟦9618_w22_12:9⟧　（换成机场的人脸识别：社会影响，2 分，好坏都可以写。）

<!-- auto:drills P1-EO-05 -->

### 本章易混辨析

| 容易混 | 区别 | 判断信号 |
|:--|:--|:--|
| EO-01 vs EO-02 | 加入职业团体的好处、行为准则的目的 → EO-01；具体情境中怎样做才合乎道德 → EO-02 | professional ethical body / code of conduct 还是 act ethically |
| 版权 vs 许可 | 所有权本身 / 作者允许别人怎样使用的协议 | copyright 还是 licence |
| Open Source vs Free Software | 都给源代码、允许修改再发布；FSF 强调用户的自由（free ≠ 免费），OSI 强调开放协作 | Initiative 还是 Foundation |
| Shareware vs Commercial | 先试用再付费 / 直接购买 | trial |
| Shareware vs Open Source | 都可能免费拿到，但 shareware 不给源代码、不能改 | source code |
| EO-04 vs EO-05 | AI 怎样工作 → EO-04；带来什么影响 → EO-05 | how AI is used 还是 impact / benefit |
| EO-04 vs HW-08 / HW-09 | AI 怎样识别、比对、决定 → EO-04；传感器、执行器、反馈怎样控制 → HW | recognition / database 还是 sensor / actuator |
| 社会 vs 经济 vs 伦理影响 | 人的生活与能力 / 成本利润 / 隐私公平心理 | social · economic · ethical |
