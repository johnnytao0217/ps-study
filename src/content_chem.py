"""Grade 11 化学（P2）每日内容。题目与答案为原创；N_A = 6,02 × 10²³，R = 8,31 J·K⁻¹·mol⁻¹，STP 下 V_m = 22,4 dm³·mol⁻¹。"""

M = lambda s: f'<span class="m">{s}</span>'
FR = lambda a, b: f'<span class="fr"><i>{a}</i><i>{b}</i></span>'
OK = '<span class="ok">✓</span>'

CHEM = [
# ------------------------------------------------------------------ C02
dict(code="c02", zh="化学键：Lewis 结构、电负性、配位键", en="Chemical bonding — Lewis structures, electronegativity, dative bonds",
 bridge="Grade 9：价电子、离子的形成",
 warm=[("写出 O、Na、Cl 的价电子数。", 1), ("Mg 原子形成什么离子？", 1)],
 learn="""
<p><b>化学键</b>：原子之间的相互吸引。<b>共价键</b>：非金属原子之间<b>共用</b>电子对；<b>离子键</b>：金属把电子<b>转移</b>给非金属，正负离子互相吸引；<b>金属键</b>：金属阳离子浸在“自由电子海”中。</p>
<p><b>Lewis 结构</b>用点和叉表示价电子；<b>Couper 结构</b>用短线表示共用电子对（一条线 = 一对）。</p>
<p><b>电负性 electronegativity</b>：原子吸引成键电子的能力。两原子电负性差 ΔEN = 0 → 非极性共价键；差越大，键越极性；差很大 → 离子键。</p>
<p><b>配位键 dative bond</b>：共用的两个电子<b>都来自同一个原子</b>（通常是孤对电子），例如 NH₄⁺、H₃O⁺。<b>键级越高</b>（单 → 双 → 三键）：键长越短，键能越大。</p>""",
 formulas=["ΔEN = |EN<sub>A</sub> − EN<sub>B</sub>|", "常用 EN：H 2,1　C 2,5　N 3,0　O 3,5　Cl 3,0　F 4,0"],
 pitfalls=["<b>Lewis 结构漏掉孤对电子</b>：H₂O 的 O 上有两对孤对电子，NH₃ 的 N 上有一对。",
           "<b>化合物的化学式写错</b>：先查离子电荷，再交叉配平。例如 Al³⁺ 和 Cr₂O₇²⁻ → Al₂(Cr₂O₇)₃。",
           "<b>配位键的箭头方向</b>：从提供电子对的原子指向接受者。"],
 defs=[("Covalent bond", "共价键", "The sharing of electrons between two atoms to form a molecule."),
       ("Electronegativity", "电负性", "A measure of the tendency of an atom in a molecule to attract bonding electrons."),
       ("Dative covalent bond", "配位键", "A covalent bond in which both shared electrons are provided by the same atom."),
       ("Bond length", "键长", "The average distance between the nuclei of two bonded atoms."),
       ("Bond energy", "键能", "The energy needed to break one mole of a particular bond (to separate the atoms).")],
 ex=[dict(n="2.1", lv=1, q="Name the type of bond in: (a) NaCl (b) Cl₂ (c) HCl (d) Cu.", mk=4, ln=2),
     dict(n="2.2", lv=1, q="Draw (a) the Lewis structure of NH₃ and (b) the Couper structure of CO₂.", mk=4, ln=0, box=22),
     dict(n="2.3", lv=2, q="Use electronegativities (H 2,1; C 2,5; O 3,5; Cl 3,0) to arrange the bonds H–Cl, O–H and C–H from MOST polar to LEAST polar. Show your working.", mk=3, ln=2),
     dict(n="2.4", lv=2, q="Use Lewis structures in a balanced equation to show how the hydronium ion (H₃O⁺) forms. Name the type of bond formed.", mk=4, ln=0, box=26),
     dict(n="2.5", lv=3, q="Compare the bond lengths and bond energies of C–C, C=C and C≡C. Explain the trend.", mk=4, ln=4)],
 ans_warm=["O：6；Na：1；Cl：7", "Mg²⁺（失去 2 个电子）"],
 ans=[("2.1", f"(a) 离子键 ionic {OK}　(b) 非极性共价键 non-polar covalent {OK}　(c) 极性共价键 polar covalent {OK}　(d) 金属键 metallic {OK}"),
      ("2.2", f"(a) N 周围 3 对共用电子 + 1 对孤对电子 {OK}{OK}　(b) O=C=O {OK}{OK}"),
      ("2.3", f"ΔEN：O–H = 1,4；H–Cl = 0,9；C–H = 0,4 {OK}{OK}；所以 O–H > H–Cl > C–H {OK}"),
      ("2.4", f"H₂O（O 上有孤对电子） + H⁺ → H₃O⁺ {OK}{OK}；O 的一对孤对电子与 H⁺ 共用 {OK}；配位共价键 dative covalent bond {OK}"),
      ("2.5", f"键长：C–C > C=C > C≡C {OK}；键能：C≡C > C=C > C–C {OK}；共用的电子对越多（键级越高） {OK}，原子核与电子之间的吸引越强，原子靠得越近 {OK}")]),

# ------------------------------------------------------------------ C04
dict(code="c04", zh="分子形状 VSEPR 与分子极性", en="Molecular shape (VSEPR) & molecular polarity",
 bridge="Day 2 的 Lewis 结构",
 warm=[("H₂O 的中心原子 O 周围有几对成键电子、几对孤对电子？", 1), ("CH₄ 中 C 有几个价电子？", 1)],
 learn="""
<p><b>VSEPR 理论</b>：中心原子周围的电子对（成键对 + 孤对）互相排斥，尽可能远离，从而决定分子形状。<b>孤对电子的排斥比成键电子对更强</b>，会把键角压小。</p>
<p><b>判断步骤</b>：① 画 Lewis 结构；② 数中心原子周围的成键对和孤对（双键、三键都只算一组）；③ 对照下面的形状表。</p>
<p><b>分子极性</b>：键有极性 ≠ 分子有极性。若分子<b>对称</b>（CO₂、BF₃、CH₄、SF₆），各键的极性互相抵消 → <b>非极性分子</b>；若<b>不对称</b>（H₂O、NH₃、HCl、HCN）→ <b>极性分子</b>。</p>
<p>答题模板（3–4 分）：键的极性（ΔEN）＋ 分子形状（对称/不对称）＋ 结论（分子极性/非极性）。</p>""",
 formulas=["2 键 0 孤对 → 直线形", "3 键 0 孤对 → 平面三角形", "4 键 0 孤对 → 正四面体", "3 键 1 孤对 → 三角锥", "2 键 2 孤对 → V 形", "6 键 0 孤对 → 八面体"],
 pitfalls=["<b>把双键算成两组</b>：CO₂ 中 C 只有 2 组电子 → 直线形。",
           "<b>只说“有极性键所以是极性分子”</b>：必须讨论分子形状是否对称。",
           "<b>NH₃ 写成平面三角形</b>：N 上有孤对电子 → 三角锥。"],
 defs=[("Molecular shape (VSEPR)", "分子形状", "The shape is determined by the repulsion between electron pairs (bonding and lone pairs) around the central atom, which arrange themselves as far apart as possible."),
       ("Polar molecule", "极性分子", "A molecule with an uneven distribution of charge, so that one end is slightly positive and the other slightly negative.")],
 ex=[dict(n="4.1", lv=1, q="Write down the molecular shape of: CH₄, NH₃, H₂O, CO₂, BF₃, SF₆.", mk=6, ln=3),
     dict(n="4.2", lv=2, q="The C=O bond is polar, yet the CO₂ molecule is non-polar. Explain.", mk=3, ln=3),
     dict(n="4.3", lv=2, q="Explain why NH₃ is a polar molecule while BF₃ is non-polar.", mk=4, ln=4),
     dict(n="4.4", lv=3, q="For HCN: (a) draw the Lewis structure (2); (b) write down its shape (1); (c) is it polar or non-polar? Explain. (2)", mk=5, ln=3, box=18)],
 ans_warm=["2 对成键电子，2 对孤对电子", "4 个"],
 ans=[("4.1", f"CH₄ 正四面体 {OK}；NH₃ 三角锥 {OK}；H₂O V 形 {OK}；CO₂ 直线形 {OK}；BF₃ 平面三角形 {OK}；SF₆ 八面体 {OK}"),
      ("4.2", f"C=O 键有极性（ΔEN = 1,0） {OK}；CO₂ 是直线形、对称的 {OK}；两个键的极性方向相反、互相抵消，所以分子非极性 {OK}"),
      ("4.3", f"N–H 和 B–F 键都有极性 {OK}；NH₃ 是三角锥（有孤对电子），不对称 → 极性分子 {OK}{OK}；BF₃ 是平面三角形，对称，极性抵消 → 非极性 {OK}"),
      ("4.4", f"(a) H–C≡N，N 上一对孤对电子 {OK}{OK}　(b) 直线形 {OK}　(c) 极性 {OK}：两端原子不同，C–H 与 C≡N 的极性不能抵消 {OK}")]),

# ------------------------------------------------------------------ C06
dict(code="c06", zh="分子间作用力的类型", en="Intermolecular forces — types",
 bridge="Day 4 的分子极性",
 warm=[("分子内的共价键和分子之间的作用力，哪个更强？", 1), ("HCl 是极性分子还是非极性分子？", 1)],
 learn="""
<p><b>分子间作用力 IMF</b>：分子之间（或分子与离子之间）的吸引力，比分子内的化学键弱得多。沸腾、熔化时被克服的是 IMF，<b>不是</b>化学键。</p>
<ul class="tight">
<li><b>London 力（色散力）</b>：所有分子都有。电子云瞬间偏移形成瞬时偶极。<b>电子越多（分子越大）越强</b>。非极性分子只有这一种。</li>
<li><b>偶极-偶极力</b>：极性分子之间，一个分子的 δ+ 吸引另一个分子的 δ−。</li>
<li><b>氢键</b>：H 直接连在 <b>N、O 或 F</b> 上，并被另一分子 N/O/F 上的孤对电子吸引。是最强的“分子之间”的力。</li>
<li><b>离子-偶极力</b>：离子溶解在极性溶剂中，例如 NaCl(aq)。</li></ul>""",
 formulas=["London < 偶极-偶极 < 氢键 < 离子-偶极（分子大小相近时）"],
 pitfalls=["<b>说“CH₄ 有氢键”</b>：H 必须连在 N、O、F 上，C–H 不行。",
           "<b>把“打断共价键”当作沸腾</b>：水沸腾时 O–H 键没有断。",
           "<b>CaCl₂(s) 与 CaCl₂(aq)</b>：固态是离子键，水溶液才有离子-偶极力。"],
 defs=[("Intermolecular forces", "分子间作用力", "Forces of attraction between molecules (or between molecules and ions)."),
       ("Hydrogen bond", "氢键", "A strong dipole-dipole force between a hydrogen atom bonded to a small, highly electronegative atom (N, O or F) and a lone pair on an N, O or F atom of another molecule."),
       ("London (dispersion) forces", "London 力", "Weak forces between molecules caused by temporary (induced) dipoles.")],
 ex=[dict(n="6.1", lv=1, q="Name the STRONGEST intermolecular force in: (a) CH₄ (b) HCl (c) NH₃ (d) KBr(aq) (e) I₂.", mk=5, ln=2),
     dict(n="6.2", lv=1, q="Give THREE requirements for hydrogen bonding between molecules.", mk=3, ln=3),
     dict(n="6.3", lv=2, q="Distinguish between an intramolecular force and an intermolecular force, using HCl as an example.", mk=3, ln=3),
     dict(n="6.4", lv=2, q="Which has stronger London forces, F₂ or Br₂? Explain.", mk=3, ln=2),
     dict(n="6.5", lv=3, q="CO₂ has only London forces between its molecules, but SO₂ has dipole-dipole forces. Explain this difference by referring to molecular shape.", mk=4, ln=4)],
 ans_warm=["分子内的共价键更强", "极性分子"],
 ans=[("6.1", f"(a) London {OK}　(b) 偶极-偶极 {OK}　(c) 氢键 {OK}　(d) 离子-偶极 {OK}　(e) London {OK}"),
      ("6.2", f"H 原子直接与 N、O 或 F 相连 {OK}；另一分子上有 N、O 或 F 的孤对电子 {OK}；N/O/F 原子小、电负性高 {OK}"),
      ("6.3", f"分子内力：同一个 HCl 分子中 H 与 Cl 之间的共价键 {OK}；分子间力：一个 HCl 分子与相邻 HCl 分子之间的偶极-偶极力 {OK}；分子内力强得多 {OK}"),
      ("6.4", f"Br₂ {OK}；Br₂ 的电子更多（分子更大），电子云更容易变形 {OK}，瞬时偶极更强 {OK}"),
      ("6.5", f"CO₂ 直线形、对称 {OK} → 非极性分子 → 只有 London 力 {OK}；SO₂ 是 V 形、不对称 {OK} → 极性分子 → 有偶极-偶极力 {OK}")]),

# ------------------------------------------------------------------ C08
dict(code="c08", zh="分子间作用力与物理性质", en="Intermolecular forces & physical properties",
 bridge="Grade 8：物质三态与状态变化",
 warm=[("25 °C 时水是什么状态？", 1), ("沸腾 boiling 和蒸发 evaporation 有什么区别？", 1)],
 learn="""
<p><b>IMF 越强</b> → 熔点、沸点越高，黏度和表面张力越大，<b>蒸气压越低</b>（分子越难逃离液面）。</p>
<p><b>沸点比较题（4 分模板）</b>：① 写出两种物质各自的 IMF 类型；② 比较强弱并说原因（氢键 vs 偶极；电子数多 → London 力强）；③ 克服较强的 IMF 需要更多能量；④ 所以沸点更高。</p>
<p><b>水的反常性质</b>来自氢键：沸点比同族的 H₂S、H₂Se、H₂Te 都高；冰的密度比水小；比热容大。</p>
<p><b>溶解性</b>：“相似相溶 like dissolves like”。溶质–溶剂之间的吸引力要能和原来的 IMF 相当。I₂（非极性）几乎不溶于水，但溶于己烷。</p>""",
 formulas=["IMF ↑ → 沸点 ↑、熔点 ↑、黏度 ↑、表面张力 ↑、蒸气压 ↓"],
 pitfalls=["<b>只写“氢键更强”就结束</b>：4 分题必须写满四步，尤其“需要更多能量克服 IMF”。",
           "<b>说“分子量大所以沸点高”</b>：要说“电子更多 → London 力更强”。",
           "<b>把“沸点”定义成“液体变成气体的温度”</b>：标准定义要提到蒸气压等于大气压。"],
 defs=[("Boiling point", "沸点", "The temperature at which the vapour pressure of a liquid equals the atmospheric (external) pressure."),
       ("Vapour pressure", "蒸气压", "The pressure exerted by a vapour in equilibrium with its liquid in a closed system."),
       ("Melting point", "熔点", "The temperature at which the solid and liquid phases of a substance are in equilibrium.")],
 ex=[dict(n="8.1", lv=1, q="Define boiling point.", mk=2, ln=2),
     dict(n="8.2", lv=1, q="At 25 °C, which has the higher vapour pressure: ethanol or water? Give a reason.", mk=3, ln=2),
     dict(n="8.3", lv=2, q="HF boils at about 20 °C and HCl at about −85 °C. Explain this difference.", mk=4, ln=4),
     dict(n="8.4", lv=2, q="The boiling points of Cl₂, Br₂ and I₂ are about −34 °C, 59 °C and 184 °C. Explain this trend.", mk=4, ln=4),
     dict(n="8.5", lv=3, q="Explain why cooking oil does not mix with water, but does dissolve in hexane.", mk=3, ln=3)],
 ans_warm=["液态", "沸腾在整个液体内部、在沸点发生；蒸发只在液面、任何温度都会发生"],
 ans=[("8.1", f"液体的蒸气压等于外界（大气）压强时的温度 {OK}{OK}"),
      ("8.2", f"乙醇 ethanol {OK}；乙醇分子间的 IMF（氢键）比水弱 {OK}，分子更容易逃离液面 {OK}"),
      ("8.3", f"HF 分子间有氢键 {OK}；HCl 分子间只有偶极-偶极力（和 London 力） {OK}；氢键更强，克服它需要更多能量 {OK}；所以 HF 沸点更高 {OK}"),
      ("8.4", f"三者都是非极性分子，只有 London 力 {OK}；Cl₂ → Br₂ → I₂ 电子数增多（分子更大） {OK}，London 力增强 {OK}；需要更多能量克服，沸点升高 {OK}"),
      ("8.5", f"油是非极性的，只有 London 力 {OK}；水分子之间是强的氢键，油不能和水形成足够强的吸引 {OK}；己烷也是非极性的，油与己烷之间的 London 力相当 → 相似相溶 {OK}")]),

# ------------------------------------------------------------------ C10
dict(code="c10", zh="气体定律与分子运动论", en="Gas laws & the kinetic molecular theory",
 bridge="Grade 8：粒子模型；Grade 10：温度单位",
 warm=[("27 °C 等于多少 K？", 1), ("1 dm³ 等于多少 cm³？", 1)],
 learn="""
<p><b>分子运动论 KMT</b>：气体由不停随机运动的微粒组成；微粒撞击器壁产生压强；温度越高，微粒平均动能越大。</p>
<ul class="tight"><li><b>Boyle</b>（T、n 不变）：p ∝ 1/V → p₁V₁ = p₂V₂。体积变小 → 单位时间撞墙次数增多 → 压强增大。</li>
<li><b>Charles</b>（p、n 不变）：V ∝ T → V₁/T₁ = V₂/T₂。</li>
<li><b>Gay-Lussac</b>（V、n 不变）：p ∝ T → p₁/T₁ = p₂/T₂。</li></ul>
<p>T <b>必须用开尔文</b>：T(K) = θ(°C) + 273。V-T(°C) 图外推后交于 −273 °C，即<b>绝对零度</b>。</p>
""",
 formulas=[M(FR("p₁V₁", "T₁") + " = " + FR("p₂V₂", "T₂")), M("T(K) = θ(°C) + 273")],
 pitfalls=["<b>温度用 °C 代入</b>：最常见的失分点，一定换成 K。",
           "<b>KMT 解释漏步骤</b>：要写“分子运动/碰撞频率 → 对器壁的力 → 压强”。",
           "<b>p 与 V 的单位</b>：组合气体定律两边单位一致即可，不必换成 SI。",
           "<b>实验题三种变量</b>：自变量 independent（改变的量）、因变量 dependent（测量的量）、控制变量 controlled（保持不变：温度或压强 + 气体的量）。"],
 defs=[("Boyle’s law", "波义耳定律", "The pressure of an enclosed gas is inversely proportional to its volume, provided the temperature and amount of gas remain constant."),
       ("Charles’ law", "查理定律", "The volume of an enclosed gas is directly proportional to its Kelvin temperature, provided the pressure and amount of gas remain constant."),
       ("Gay-Lussac’s law", "盖-吕萨克定律", "The pressure of an enclosed gas is directly proportional to its Kelvin temperature, provided the volume and amount of gas remain constant."),
       ("Absolute zero", "绝对零度", "The temperature (0 K = −273 °C) at which particles have minimum kinetic energy.")],
 ex=[dict(n="10.1", lv=1, q="A gas at 150 kPa occupies 2 dm³. It is compressed to 0,5 dm³ at constant temperature. Calculate the new pressure.", mk=3, ln=2),
     dict(n="10.2", lv=1, q="A gas occupies 3 dm³ at 27 °C. It is heated to 127 °C at constant pressure. Calculate the new volume.", mk=3, ln=2),
     dict(n="10.3", lv=2, q="Use the kinetic molecular theory to explain why the pressure of a gas increases when its volume is decreased at constant temperature.", mk=3, ln=3),
     dict(n="10.4", lv=2, q="A sealed can contains gas at 100 kPa and 20 °C. It is heated to 150 °C. Calculate the pressure inside the can.", mk=3, ln=2),
     dict(n="10.5", lv=3, q="A gas occupies 250 cm³ at 100 kPa and 15 °C. Calculate its volume at 80 kPa and 45 °C.", mk=4, ln=3),
     dict(n="10.6", lv=3, q="In an experiment to verify Boyle’s law, name the independent, dependent and controlled variables.", mk=3, ln=2)],
 ans_warm=["300 K", "1 000 cm³"],
 ans=[("10.1", f"p₁V₁ = p₂V₂ {OK}；150 × 2 = p₂ × 0,5 {OK} → p₂ = 600 kPa {OK}"),
      ("10.2", f"V₁/T₁ = V₂/T₂ {OK}；3/300 = V₂/400 {OK} → V₂ = 4 dm³ {OK}"),
      ("10.3", f"体积减小，分子之间、分子与器壁的距离变小 {OK}；单位时间内碰撞器壁的次数增多 {OK}；对器壁的作用力增大，所以压强增大 {OK}"),
      ("10.4", f"p₁/T₁ = p₂/T₂ {OK}；100/293 = p₂/423 {OK} → p₂ = 144,37 kPa {OK}"),
      ("10.5", f"p₁V₁/T₁ = p₂V₂/T₂ {OK}；(100)(250)/288 = (80)V₂/318 {OK}{OK} → V₂ = 345,05 cm³ {OK}"),
      ("10.6", f"自变量：体积（或压强） {OK}；因变量：压强（或体积） {OK}；控制变量：温度和气体的量 {OK}")]),

# ------------------------------------------------------------------ C12
dict(code="c12", zh="理想气体方程与真实气体", en="Ideal gas equation & real gases",
 bridge="Day 10 的气体定律 + 摩尔 n = m/M",
 warm=[("200 kPa = ? Pa；500 cm³ = ? m³", 1), ("8 g O₂ 是多少 mol？", 1)],
 learn="""
<p><b>pV = nRT</b>：必须全部用 <b>SI 单位</b>——p (Pa)、V (m³)、T (K)、R = 8,31 J·K⁻¹·mol⁻¹。kPa × 1 000 → Pa；dm³ ÷ 1 000 → m³；cm³ ÷ 10⁶ → m³。</p>
<p><b>理想气体</b>：假设分子本身没有体积、分子间没有作用力。<b>真实气体</b>在两种条件下偏离最明显：</p>
<ul class="tight"><li><b>高压</b>：分子挤得很近，分子本身的体积不能忽略；</li><li><b>低温</b>：分子运动变慢，分子间吸引力变得明显（接近液化）。</li></ul>
<p>同一温度下，所有气体分子的<b>平均动能相同</b>：E<sub>k</sub> = ½mv²，所以质量小的分子（如 H₂、He）平均速度更大。</p>""",
 formulas=[M("pV = nRT"), M("n = " + FR("m", "M")), M("R = 8,31 J·K⁻¹·mol⁻¹")],
 pitfalls=["<b>pV = nRT 用了 kPa 和 dm³</b>：答案会差 10⁶ 倍。（例外：kPa 搭配 dm³ 时两者的 10³ 恰好抵消，但不建议依赖。）",
           "<b>只写“高压低温”不解释</b>：要说明“分子体积变得重要 / 分子间力变得重要”。",
           "<b>求出 M 后忘了判断是什么气体</b>：例如 M = 28 g·mol⁻¹ 的双原子气体是 N₂。"],
 defs=[("Ideal gas", "理想气体", "A gas whose particles have no volume and no intermolecular forces, and which obeys the gas laws at all temperatures and pressures.")],
 ex=[dict(n="12.1", lv=1, q="Convert to SI units: 200 kPa; 500 cm³; 25 °C.", mk=3, ln=1),
     dict(n="12.2", lv=1, q="Calculate the number of moles of gas in 10 dm³ at 101,3 kPa and 0 °C.", mk=3, ln=2),
     dict(n="12.3", lv=2, q="Calculate the mass of CO₂ in a 5 dm³ container at 150 kPa and 30 °C.", mk=4, ln=3),
     dict(n="12.4", lv=2, q="Under which TWO conditions does a real gas deviate most from ideal behaviour? Explain each.", mk=4, ln=4),
     dict(n="12.5", lv=3, q="2,8 g of a diatomic element gas occupies 2,46 dm³ at 100 kPa and 23 °C. Determine its molar mass and identify the gas.", mk=5, ln=4),
     dict(n="12.6", lv=3, q="Two syringes at the same temperature contain H₂ and O₂. Compare the average speeds of the molecules and explain.", mk=3, ln=2)],
 ans_warm=["2 × 10⁵ Pa；5 × 10⁻⁴ m³", "8 ÷ 32 = 0,25 mol"],
 ans=[("12.1", f"2 × 10⁵ Pa {OK}；5 × 10⁻⁴ m³ {OK}；298 K {OK}"),
      ("12.2", f"n = pV/RT = (101 300)(0,01)/((8,31)(273)) {OK}{OK} = 0,45 mol {OK}"),
      ("12.3", f"n = (150 000)(0,005)/((8,31)(303)) {OK} = 0,30 mol {OK}；m = nM = 0,298 × 44 {OK} = 13,11 g {OK}"),
      ("12.4", f"高压 {OK}：分子之间距离小，分子本身的体积不能忽略 {OK}；低温 {OK}：分子运动慢，分子间吸引力变得明显 {OK}"),
      ("12.5", f"n = pV/RT = (1 × 10⁵)(2,46 × 10⁻³)/((8,31)(296)) {OK}{OK} = 0,10 mol {OK}；M = 2,8/0,10 = 28 g·mol⁻¹ {OK}；N₂ {OK}"),
      ("12.6", f"H₂ 分子更快 {OK}；同温度下平均动能相同 {OK}，E<sub>k</sub> = ½mv²，H₂ 质量更小所以速度更大 {OK}")]),

# ------------------------------------------------------------------ C14
dict(code="c14", zh="能量与化学变化", en="Energy & chemical change",
 bridge="Grade 9：放热与吸热反应",
 warm=[("燃烧木柴是放热还是吸热？", 1), ("冰融化时吸收能量还是放出能量？", 1)],
 learn="""
<p>化学反应 = <b>断开旧键（吸收能量）</b> + <b>形成新键（放出能量）</b>。</p>
<p><b>ΔH = 断键吸收的总能量 − 成键放出的总能量</b>。<b>放热 exothermic</b>：ΔH < 0，生成物能量低于反应物；<b>吸热 endothermic</b>：ΔH > 0。</p>
<p><b>活化能 Ea</b>：反应发生所需的最低能量；曲线顶点是<b>活化络合物 activated complex</b>。逆反应的活化能 = 顶点 − 生成物能量。</p>
<p><b>催化剂</b>：提供活化能更低的路径，加快反应；<b>不改变 ΔH</b>，反应结束后本身不变。</p>""",
 formulas=[M("ΔH = H<sub>products</sub> − H<sub>reactants</sub>"), M("ΔH = Σ(断键) − Σ(成键)")],
 pitfalls=["<b>断键/成键次数没有乘系数</b>：2CH₃OH 要算 2 个分子里所有的键。",
           "<b>ΔH 漏掉负号或单位</b>：写 −184 kJ·mol⁻¹。",
           "<b>能量图标注不全</b>：坐标轴、反应物、生成物、Ea、ΔH、活化络合物都要标出。"],
 defs=[("Exothermic reaction", "放热反应", "A reaction that releases energy to the surroundings (ΔH < 0)."),
       ("Endothermic reaction", "吸热反应", "A reaction that absorbs energy from the surroundings (ΔH > 0)."),
       ("Activation energy", "活化能", "The minimum energy needed for a reaction to take place."),
       ("Activated complex", "活化络合物", "The unstable transition state with the highest potential energy during a reaction."),
       ("Catalyst", "催化剂", "A substance that increases the rate of a reaction but remains unchanged at the end of the reaction.")],
 ex=[dict(n="14.1", lv=1, q="Define activation energy.", mk=2, ln=1),
     dict(n="14.2", lv=1, q="In an energy profile, the reactants are at 100 kJ, the activated complex at 250 kJ and the products at 40 kJ. Determine (a) Ea for the forward reaction; (b) ΔH, and state whether exo- or endothermic; (c) Ea for the reverse reaction.", mk=4, ln=3),
     dict(n="14.3", lv=2, q="H₂ + Cl₂ → 2HCl. Bond energies (kJ·mol⁻¹): H–H 436; Cl–Cl 242; H–Cl 431. Calculate ΔH.", mk=4, ln=3),
     dict(n="14.4", lv=2, q="How does adding a catalyst affect (a) the activation energy and (b) ΔH?", mk=2, ln=1),
     dict(n="14.5", lv=3, q="CH₄ + 2O₂ → CO₂ + 2H₂O(g). Bond energies (kJ·mol⁻¹): C–H 414; O=O 499; C=O 799; O–H 460. (a) Calculate ΔH. (5)　(b) Sketch a labelled energy profile. (3)", mk=8, ln=5, box=24)],
 ans_warm=["放热", "吸收能量"],
 ans=[("14.1", f"反应发生所需的最低能量 {OK}{OK}"),
      ("14.2", f"(a) 250 − 100 = 150 kJ {OK}　(b) 40 − 100 = −60 kJ {OK}，放热 {OK}　(c) 250 − 40 = 210 kJ {OK}"),
      ("14.3", f"断键：436 + 242 = 678 kJ {OK}；成键：2 × 431 = 862 kJ {OK}；ΔH = 678 − 862 {OK} = −184 kJ·mol⁻¹ {OK}"),
      ("14.4", f"(a) 降低 {OK}　(b) 不变 {OK}"),
      ("14.5", f"(a) 断键：4(414) + 2(499) = 2 654 kJ {OK}{OK}；成键：2(799) + 4(460) = 3 438 kJ {OK}{OK}；ΔH = 2 654 − 3 438 = −784 kJ·mol⁻¹ {OK}<br>"
               f"(b) 生成物低于反应物 {OK}；标出 Ea {OK} 和 ΔH（向下的箭头） {OK}")]),

# ------------------------------------------------------------------ C16
dict(code="c16", zh="摩尔、摩尔体积与浓度", en="The mole, molar volume & concentration",
 bridge="Grade 9–10：相对原子质量、化学式",
 warm=[("计算 H₂O 和 NaCl 的摩尔质量（H 1，O 16，Na 23，Cl 35,5）。", 1), ("250 cm³ 等于多少 dm³？", 1)],
 learn="""
<p><b>1 mol</b> 任何物质都含有 6,02 × 10²³ 个粒子（阿伏伽德罗常数 N<sub>A</sub>）。<b>摩尔质量 M</b> = 1 mol 的质量（g·mol⁻¹），由元素周期表相加得到。</p>
<p>所有换算都<b>先变成 n</b>：质量 n = m/M；粒子数 N = n·N<sub>A</sub>；气体 n = V/V<sub>m</sub>（STP 下 V<sub>m</sub> = 22,4 dm³·mol⁻¹）；溶液 n = cV（V 用 dm³）。</p>
<p><b>稀释</b>：溶质的量不变，c₁V₁ = c₂V₂。<b>加多少水</b> = V₂ − V₁。</p>
<p><b>离子浓度</b>：Na₂SO₄ → 2Na⁺ + SO₄²⁻，所以 c(Na⁺) = 2 × c(Na₂SO₄)。</p>""",
 formulas=[M("n = " + FR("m", "M")), M("N = n·N<sub>A</sub>"), M("n = " + FR("V", "V<sub>m</sub>")), M("c = " + FR("n", "V")), M("c₁V₁ = c₂V₂")],
 pitfalls=["<b>体积用 cm³ 代入 c = n/V</b>：必须除以 1 000 换成 dm³。",
           "<b>稀释题直接写 V₂</b>：题目问“加多少水”时要减去原来的体积。",
           "<b>双原子分子的 M</b>：O₂ = 32，不是 16。"],
 defs=[("Mole", "摩尔", "The SI unit for amount of substance; one mole contains as many particles as there are atoms in 12 g of carbon-12."),
       ("Molar mass", "摩尔质量", "The mass of one mole of a substance (g·mol⁻¹)."),
       ("Molar concentration", "物质的量浓度", "The amount of solute per unit volume of solution (mol·dm⁻³)."),
       ("Molar gas volume", "摩尔气体体积", "The volume occupied by one mole of any gas (22,4 dm³ at STP).")],
 ex=[dict(n="16.1", lv=1, q="Calculate (a) the number of moles and (b) the number of molecules in 11 g of CO₂.", mk=4, ln=2),
     dict(n="16.2", lv=1, q="Calculate the volume occupied by 0,15 mol O₂ at STP.", mk=2, ln=1),
     dict(n="16.3", lv=2, q="Calculate the mass of NaOH needed to prepare 250 cm³ of a 0,2 mol·dm⁻³ solution.", mk=4, ln=3),
     dict(n="16.4", lv=2, q="100 cm³ of 2 mol·dm⁻³ HCl is diluted to 0,5 mol·dm⁻³. Calculate the volume of water that must be added.", mk=4, ln=3),
     dict(n="16.5", lv=3, q="7,1 g of Na₂SO₄ is dissolved in water to make 200 cm³ of solution. Calculate (a) c(Na₂SO₄) (3) and (b) the concentration of Na⁺ ions (2).", mk=5, ln=4)],
 ans_warm=["H₂O = 18 g·mol⁻¹；NaCl = 58,5 g·mol⁻¹", "0,25 dm³"],
 ans=[("16.1", f"(a) n = 11/44 {OK} = 0,25 mol {OK}　(b) N = 0,25 × 6,02 × 10²³ {OK} = 1,51 × 10²³ 个分子 {OK}"),
      ("16.2", f"V = nV<sub>m</sub> = 0,15 × 22,4 {OK} = 3,36 dm³ {OK}"),
      ("16.3", f"n = cV = 0,2 × 0,25 {OK} = 0,05 mol {OK}；m = nM = 0,05 × 40 {OK} = 2,00 g {OK}"),
      ("16.4", f"c₁V₁ = c₂V₂：2 × 100 = 0,5 × V₂ {OK}{OK} → V₂ = 400 cm³ {OK}；加水 400 − 100 = 300 cm³ {OK}"),
      ("16.5", f"(a) M = 142 g·mol⁻¹；n = 7,1/142 = 0,05 mol {OK}；c = 0,05/0,2 {OK} = 0,25 mol·dm⁻³ {OK}　(b) Na⁺ : Na₂SO₄ = 2 : 1 {OK} → 0,50 mol·dm⁻³ {OK}")]),

# ------------------------------------------------------------------ C18
dict(code="c18", zh="百分组成、经验式与分子式", en="Percentage composition, empirical & molecular formulae",
 bridge="Day 16 的 n = m/M",
 warm=[("计算 C₆H₁₂O₆ 的摩尔质量（C 12，H 1，O 16）。", 1), ("把 4 : 8 : 2 化成最简整数比。", 1)],
 learn="""
<p><b>百分组成</b>：某元素的质量百分比 = (该元素在 1 mol 中的质量 ÷ M) × 100。</p>
<p><b>经验式 empirical formula</b> = 各原子的<b>最简整数比</b>；<b>分子式 molecular formula</b> = 一个分子中各原子的<b>实际</b>个数。分子式 = 经验式 × (M ÷ 经验式质量)。</p>
<p><b>固定流程</b>（见下图）：百分比 → 假设 100 g → 各元素 n = m/M → 全部除以最小的 n → 整数比 → 经验式。</p>
<p><b>结晶水 water of crystallisation</b>：加热后失去的质量就是水，x = n(H₂O) ÷ n(无水盐)。</p>""",
 formulas=[M("% = " + FR("元素质量", "M") + " × 100"), M("倍数 = " + FR("M", "经验式质量"))],
 pitfalls=["<b>比值有小数时直接四舍五入</b>：1,5 要 ×2，1,33 要 ×3；只有非常接近整数（如 5,98）才可取整。",
           "<b>忘了用 n = m/M</b>：直接用百分比算比例是错的。",
           "<b>分子式题没有写出经验式质量</b>：会少拿过程分。"],
 defs=[("Empirical formula", "经验式", "The simplest whole-number ratio of atoms of each element in a compound."),
       ("Molecular formula", "分子式", "The actual number of atoms of each element in one molecule of a compound.")],
 ex=[dict(n="18.1", lv=1, q="Calculate the percentage of nitrogen by mass in NH₄NO₃.", mk=3, ln=2),
     dict(n="18.2", lv=2, q="A compound contains 40,0% C, 6,7% H and 53,3% O by mass. Its molar mass is 180 g·mol⁻¹. Determine its empirical and molecular formulae.", mk=6, ln=6),
     dict(n="18.3", lv=2, q="A hydrocarbon contains 85,7% C. Its molar mass is 56 g·mol⁻¹. Determine its molecular formula.", mk=5, ln=4),
     dict(n="18.4", lv=3, q="5,00 g of hydrated copper(II) sulfate, CuSO₄·xH₂O, is heated until all the water is removed. 3,20 g of anhydrous CuSO₄ remains. Determine x.", mk=5, ln=5)],
 ans_warm=["180 g·mol⁻¹", "2 : 4 : 1"],
 ans=[("18.1", f"M(NH₄NO₃) = 80 g·mol⁻¹ {OK}；N 的质量 = 28 g {OK}；28/80 × 100 = 35% {OK}"),
      ("18.2", f"n(C) = 40/12 = 3,33 {OK}；n(H) = 6,7/1 = 6,7 {OK}；n(O) = 53,3/16 = 3,33 {OK}；比值 1 : 2 : 1 → CH₂O {OK}；"
               f"经验式质量 30，180/30 = 6 {OK} → C₆H₁₂O₆ {OK}"),
      ("18.3", f"H = 14,3% {OK}；n(C) = 85,7/12 = 7,14，n(H) = 14,3 {OK}；比 1 : 2 → CH₂ {OK}；56/14 = 4 {OK} → C₄H₈ {OK}"),
      ("18.4", f"m(H₂O) = 5,00 − 3,20 = 1,80 g {OK}；n(H₂O) = 1,80/18 = 0,10 mol {OK}；n(CuSO₄) = 3,20/159,5 = 0,020 mol {OK}；x = 0,10/0,020 {OK} = 5 {OK}")]),

# ------------------------------------------------------------------ C20
dict(code="c20", zh="限量试剂、产率与纯度", en="Limiting reagent, percentage yield & purity",
 bridge="Grade 9–10：配平化学方程式",
 warm=[("配平：H₂ + O₂ → H₂O", 1), ("在配平后的方程式中，H₂ 与 H₂O 的物质的量之比是多少？", 1)],
 learn="""
<p><b>限量试剂 limiting reagent</b>：先被完全消耗的反应物，它决定生成物的量；另一种是<b>过量试剂</b>。</p>
<p><b>判断方法</b>：① 把每种反应物换成 n；② 选一种反应物，按方程式系数算出它需要另一种多少 mol；③ 实际的量不够 → 那一种就是限量试剂。之后<b>只用限量试剂</b>计算产物。</p>
<p><b>产率 % yield</b> = 实际产量 ÷ 理论产量 × 100（理论产量由限量试剂算出）。产率低于 100% 的原因：反应不完全、产物在转移中损失、有副反应。</p>
<p><b>纯度 % purity</b> = 纯物质的质量 ÷ 不纯样品的质量 × 100。纯物质的质量由产物（如生成的气体）反推得到。</p>""",
 formulas=[M("% yield = " + FR("实际", "理论") + " × 100"), M("% purity = " + FR("m<sub>纯</sub>", "m<sub>样品</sub>") + " × 100")],
 pitfalls=["<b>直接比较两种反应物的 n</b>：要结合系数（2 : 1 时，3 mol 并不一定比 2 mol 多余）。",
           "<b>用过量试剂计算产物</b>：结果会偏大。",
           "<b>纯度题用了样品的全部质量去算 n</b>：样品中只有一部分会反应。"],
 defs=[("Limiting reagent", "限量试剂", "The reactant that is completely used up in a reaction and therefore limits the amount of product formed."),
       ("Percentage yield", "产率", "The actual yield expressed as a percentage of the theoretical yield."),
       ("Percentage purity", "纯度", "The mass of the pure substance expressed as a percentage of the mass of the impure sample.")],
 ex=[dict(n="20.1", lv=1, q="2H₂ + O₂ → 2H₂O. 4 mol H₂ reacts with 3 mol O₂. (a) Which is the limiting reagent? (b) How many moles of the excess reagent remain? (c) How many moles of water form?", mk=4, ln=3),
     dict(n="20.2", lv=2, q="N₂ + 3H₂ → 2NH₃. 14 g of N₂ reacts with 4 g of H₂. Determine the limiting reagent and calculate the theoretical mass of NH₃.", mk=6, ln=5),
     dict(n="20.3", lv=2, q="In 20.2 only 12,75 g of NH₃ is obtained. Calculate the percentage yield.", mk=2, ln=1),
     dict(n="20.4", lv=3, q="25 g of impure limestone reacts with excess HCl: CaCO₃ + 2HCl → CaCl₂ + H₂O + CO₂. 4,48 dm³ of CO₂ is collected at STP. Calculate the percentage purity of the limestone.", mk=6, ln=5)],
 ans_warm=["2H₂ + O₂ → 2H₂O", "1 : 1"],
 ans=[("20.1", f"(a) 4 mol H₂ 只需要 2 mol O₂，O₂ 有 3 mol → H₂ 是限量试剂 {OK}{OK}　(b) 剩余 O₂：3 − 2 = 1 mol {OK}　(c) 4 mol H₂O {OK}"),
      ("20.2", f"n(N₂) = 14/28 = 0,5 mol {OK}；n(H₂) = 4/2 = 2 mol {OK}；0,5 mol N₂ 需要 1,5 mol H₂，H₂ 过量 → N₂ 是限量试剂 {OK}{OK}；"
               f"n(NH₃) = 2 × 0,5 = 1 mol {OK}；m = 1 × 17 = 17 g {OK}"),
      ("20.3", f"% yield = 12,75/17 × 100 {OK} = 75% {OK}"),
      ("20.4", f"n(CO₂) = 4,48/22,4 = 0,2 mol {OK}{OK}；n(CaCO₃) = 0,2 mol（1 : 1） {OK}；m = 0,2 × 100 = 20 g {OK}；纯度 = 20/25 × 100 {OK} = 80% {OK}")]),

# ------------------------------------------------------------------ C22
dict(code="c22", zh="有机①：烃与 IUPAC 命名", en="Organic I — hydrocarbons & IUPAC naming",
 bridge="Grade 9：碳的价电子数为 4",
 warm=[("碳原子能形成几个共价键？", 1), ("写出甲烷 methane 的分子式。", 1)],
 learn="""
<p><b>同系物 homologous series</b>：通式相同、官能团相同、相邻成员相差一个 CH₂。<b>烷烃 alkane</b> CₙH₂ₙ₊₂（只有单键，<b>饱和</b>）；<b>烯烃 alkene</b> CₙH₂ₙ（含 C=C，不饱和）；<b>炔烃 alkyne</b> CₙH₂ₙ₋₂（含 C≡C）。</p>
<p>碳数前缀：1 meth，2 eth，3 prop，4 but，5 pent，6 hex，7 hept，8 oct。</p>
<p><b>IUPAC 命名步骤</b>：① 找<b>最长碳链</b>（必须含双键/三键）；② 从离双键/三键（若没有，则离支链）最近的一端编号；③ 支链按<b>字母顺序</b>写，相同支链用 di-、tri-，位置号用逗号隔开，数字与字母之间用短横线。</p>
<p><b>结构式</b>画出每个原子和键；<b>缩写结构式</b>如 CH₃CH(CH₃)CH₂CH₃。</p>""",
 formulas=["alkane CₙH₂ₙ₊₂", "alkene CₙH₂ₙ", "alkyne CₙH₂ₙ₋₂"],
 pitfalls=["<b>没找到真正的最长链</b>：弯折的链也算，见下图。",
           "<b>编号方向错</b>：要让双键或支链的位置号最小。",
           "<b>格式错误</b>：2,3-dimethylpentane（逗号、短横线、连写），不能写成 2,3 dimethyl pentane。"],
 defs=[("Homologous series", "同系物", "A series of organic compounds that can be described by the same general formula and in which each member differs from the next by a CH₂ group."),
       ("Saturated compound", "饱和化合物", "A compound in which there are only single bonds between carbon atoms."),
       ("Unsaturated compound", "不饱和化合物", "A compound with one or more multiple bonds (double or triple) between carbon atoms.")],
 ex=[dict(n="22.1", lv=1, q="Classify each as an alkane, alkene or alkyne: C₅H₁₂; C₃H₄; C₆H₁₂.", mk=3, ln=1),
     dict(n="22.2", lv=1, q="Write down the IUPAC names: (a) CH₃CH₂CH₂CH₃ (b) CH₂=CHCH₃ (c) HC≡CCH₂CH₃", mk=3, ln=2),
     dict(n="22.3", lv=2, q="Write down the IUPAC names: (a) CH₃CH(CH₃)CH₂CH₃ (b) CH₃C(CH₃)₂CH₃ (c) CH₃CH=CHCH₂CH₃", mk=6, ln=2),
     dict(n="22.4", lv=2, q="Draw the structural formula of 3-ethyl-2-methylhexane.", mk=3, ln=0, box=24),
     dict(n="22.5", lv=3, q="A learner named a compound “2-ethylbutane”. Explain why this name is incorrect and give the correct IUPAC name.", mk=3, ln=3)],
 ans_warm=["4 个", "CH₄"],
 ans=[("22.1", f"C₅H₁₂ 烷烃 {OK}；C₃H₄ 炔烃 {OK}；C₆H₁₂ 烯烃 {OK}"),
      ("22.2", f"(a) butane {OK}　(b) propene {OK}　(c) but-1-yne {OK}"),
      ("22.3", f"(a) 2-methylbutane {OK}{OK}　(b) 2,2-dimethylpropane {OK}{OK}　(c) pent-2-ene {OK}{OK}"),
      ("22.4", f"主链 6 个 C {OK}；C2 上接 –CH₃ {OK}；C3 上接 –CH₂CH₃，所有 H 补齐 {OK}"),
      ("22.5", f"乙基在 2 号位说明最长链没找对 {OK}；最长链实际有 5 个 C {OK}；正确名称 3-methylpentane {OK}")]),

# ------------------------------------------------------------------ C24
dict(code="c24", zh="有机②：官能团与同分异构", en="Organic II — functional groups & isomers",
 bridge="Day 22 的命名规则",
 warm=[("写出烯烃的通式。", 1), ("命名 C₃H₈。", 1)],
 learn="""
<p><b>官能团 functional group</b>：决定有机物化学性质的原子或原子团。下表是 Grade 11 必须认识的六类（命名时官能团的位置号要尽量小）。</p>
<p><b>结构异构体 structural isomers</b>：分子式相同、结构式不同。</p>
<ul class="tight"><li><b>链异构</b>：碳链不同，例如 butane 与 2-methylpropane；</li>
<li><b>位置异构</b>：官能团位置不同，例如 propan-1-ol 与 propan-2-ol；</li>
<li><b>官能团异构</b>：官能团不同，例如 propanoic acid 与 methyl ethanoate（都是 C₃H₆O₂），propanal 与 propanone。</li></ul>""",
 formulas=["醇 -ol", "醛 -al", "酮 -one", "羧酸 -oic acid", "酯 alkyl alkanoate", "卤代烷 halo-"],
 pitfalls=["<b>酯的名称前后颠倒</b>：醇的部分在前（-yl），酸的部分在后（-oate）。",
           "<b>醛和酮混淆</b>：C=O 在链端是醛，在链中间是酮。",
           "<b>羧酸的碳数</b>：–COOH 中的 C 也要算进主链。"],
 defs=[("Functional group", "官能团", "A bond or an atom or a group of atoms that determines the physical and chemical properties of a group of organic compounds."),
       ("Structural isomers", "结构异构体", "Organic molecules with the same molecular formula but different structural formulae.")],
 ex=[dict(n="24.1", lv=1, q="Name the homologous series of: (a) CH₃CH₂OH (b) CH₃COOH (c) CH₃CHO (d) CH₃COCH₃ (e) CH₃CH₂Br (f) HCOOCH₃", mk=6, ln=2),
     dict(n="24.2", lv=2, q="Write down the IUPAC names: (a) CH₃CH₂CH₂OH (b) CH₃CH(OH)CH₃ (c) CH₃CH₂COOH (d) CH₃CH₂CHBrCH₃", mk=4, ln=2),
     dict(n="24.3", lv=2, q="(a) Name the ester CH₃CH₂COOCH₃. (2)　(b) Draw the structural formula of ethyl methanoate. (2)", mk=4, ln=1, box=18),
     dict(n="24.4", lv=3, q="Give the structural formulae and IUPAC names of TWO functional isomers with molecular formula C₃H₆O₂.", mk=4, ln=0, box=24),
     dict(n="24.5", lv=3, q="Write down the IUPAC names of TWO positional isomers with formula C₄H₉Cl that have an unbranched chain.", mk=2, ln=1)],
 ans_warm=["CₙH₂ₙ", "propane"],
 ans=[("24.1", f"(a) 醇 alcohol {OK}　(b) 羧酸 carboxylic acid {OK}　(c) 醛 aldehyde {OK}　(d) 酮 ketone {OK}　(e) 卤代烷 haloalkane {OK}　(f) 酯 ester {OK}"),
      ("24.2", f"(a) propan-1-ol {OK}　(b) propan-2-ol {OK}　(c) propanoic acid {OK}　(d) 2-bromobutane {OK}"),
      ("24.3", f"(a) methyl propanoate {OK}{OK}　(b) H–C(=O)–O–CH₂–CH₃，所有键画出 {OK}{OK}"),
      ("24.4", f"propanoic acid CH₃CH₂COOH {OK}{OK}；methyl ethanoate CH₃COOCH₃（或 ethyl methanoate HCOOCH₂CH₃） {OK}{OK}"),
      ("24.5", f"1-chlorobutane {OK}；2-chlorobutane {OK}")]),
]
