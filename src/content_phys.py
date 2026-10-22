"""Grade 11 物理（P1）每日内容。题目与答案为原创；常数按 IEB Grade 11 data sheet：g = 9,8 m·s⁻²。"""

M = lambda s: f'<span class="m">{s}</span>'
FR = lambda a, b: f'<span class="fr"><i>{a}</i><i>{b}</i></span>'
OK = '<span class="ok">✓</span>'

PHYS = [
# ------------------------------------------------------------------ P01
dict(code="p01", zh="矢量：合成与分解", en="Vectors — resultant & components",
 bridge="Grade 9 数学：勾股定理、三角函数",
 warm=[("直角三角形两条直角边分别是 6 和 8，求斜边。", 1), ("若 tan θ = 0,75，求 θ（计算器设为 DEG）。", 1)],
 learn="""
<p><b>标量 scalar</b> 只有大小（质量、时间、路程、速率、能量）；<b>矢量 vector</b> 既有大小又有方向（位移、速度、加速度、力、重力 weight）。</p>
<p><b>合矢量 resultant</b>：能代替所有矢量共同作用效果的那<b>一个</b>矢量。求法：把矢量<b>首尾相接 tip-to-tail</b>，从第一个的尾指向最后一个的头。</p>
<p>两个矢量<b>互相垂直</b>时：大小用勾股定理，方向用 tan。两个力同向时相加、反向时相减，所以 15 N 和 7 N 的合力一定在 8 N 到 22 N 之间。</p>
<p><b>分解 resolve</b>：一个斜向的力 F（与水平成 θ）可以拆成水平分量 F cosθ 和竖直分量 F sinθ。斜面、斜拉题全靠它。</p>""",
 formulas=[M("R² = x² + y²"), M("tan θ = " + FR("对边 opp", "邻边 adj")), M("F<sub>x</sub> = F cos θ"), M("F<sub>y</sub> = F sin θ")],
 pitfalls=["<b>只写大小不写方向</b>：矢量答案必须带方向，如 “22,62° N of E” 或方位角 “067,38°”。",
           "<b>垂直的两个矢量直接相加</b>：3 m + 4 m ≠ 7 m，要用勾股定理得 5 m。",
           "<b>计算器在 RAD 模式</b>：考前检查屏幕上是否显示 D/DEG。"],
 defs=[("Scalar", "标量", "A physical quantity that has magnitude only."),
       ("Vector", "矢量", "A physical quantity that has both magnitude and direction."),
       ("Resultant vector", "合矢量", "The single vector that has the same effect as all the original vectors acting together.")],
 ex=[dict(n="1.1", lv=1, q="Classify each as a scalar or a vector: mass, weight, speed, displacement, time, force.", mk=3, ln=2),
     dict(n="1.2", lv=1, q="Two forces of 15 N and 7 N act on an object. Write down the maximum and the minimum possible magnitude of their resultant.", mk=2, ln=1),
     dict(n="1.3", lv=2, q="A hiker walks 120 m east and then 50 m north. Calculate the magnitude and direction of her resultant displacement.", mk=4, ln=4),
     dict(n="1.4", lv=2, q="A rope pulls a box with a force of 40 N at 30° above the horizontal. Calculate the horizontal and vertical components of the force.", mk=4, ln=3),
     dict(n="1.5", lv=3, q="A swimmer heads straight across (north) a river 60 m wide at 1,5 m·s⁻¹ relative to the water. The river flows east at 0,8 m·s⁻¹.<br>(a) Calculate the magnitude and direction of the swimmer’s resultant velocity. (4)　(b) Calculate the time taken to cross. (2)　(c) How far downstream does the swimmer land? (2)", mk=8, ln=6)],
 ans_warm=["√(6² + 8²) = 10", "θ = tan⁻¹(0,75) = 36,87°"],
 ans=[("1.1", f"Scalar: mass, speed, time {OK}；Vector: weight, displacement, force {OK}{OK}"),
      ("1.2", f"最大 15 + 7 = 22 N {OK}（同向）；最小 15 − 7 = 8 N {OK}（反向）"),
      ("1.3", f"R² = 120² + 50² {OK} → R = 130 m {OK}；tan θ = 50/120 {OK} → θ = 22,62° N of E（方位角 067,38°） {OK}"),
      ("1.4", f"F<sub>x</sub> = 40 cos30° {OK} = 34,64 N {OK}；F<sub>y</sub> = 40 sin30° {OK} = 20,00 N {OK}"),
      ("1.5", f"(a) v² = 1,5² + 0,8² {OK} → v = 1,70 m·s⁻¹ {OK}；tan θ = 0,8/1,5 {OK} → θ = 28,07° E of N {OK}<br>"
              f"(b) 过河只看垂直河岸的速度：Δt = 60 ÷ 1,5 {OK} = 40 s {OK}<br>(c) 0,8 × 40 {OK} = 32 m 下游 {OK}")]),

# ------------------------------------------------------------------ P03
dict(code="p03", zh="运动学①：位移、速度、加速度", en="Kinematics I — displacement, velocity, acceleration",
 bridge="Grade 8–9：速度 = 路程 ÷ 时间、单位换算",
 warm=[("把 72 km·h⁻¹ 换算成 m·s⁻¹。", 1), ("2,5 分钟等于多少秒？", 1)],
 learn="""
<p><b>路程 distance</b> = 实际路径总长度（标量）；<b>位移 displacement Δx</b> = 位置的变化，从起点指向终点（矢量，可正可负）。</p>
<p><b>平均速率</b> = 总路程 ÷ 总时间；<b>平均速度</b> = 位移 ÷ 时间（带方向）。绕操场跑一圈回到起点：速率不为 0，速度 = 0。</p>
<p><b>加速度 acceleration</b> = 速度的变化率。先规定一个<b>正方向</b>：a 与 v 同号 → 加速；a 与 v 异号 → 减速。负号表示方向，不表示“更小”。</p>
<p><b>km·h⁻¹ ÷ 3,6 = m·s⁻¹</b>。计算前统一成 SI 单位：m、s、m·s⁻¹。</p>""",
 formulas=[M("v<sub>ave</sub> = " + FR("Δx", "Δt")), M("平均速率 = " + FR("总路程", "总时间")), M("a = " + FR("Δv", "Δt") + " = " + FR("v − u", "Δt"))],
 pitfalls=["<b>平均速率 ≠ 速率的平均值</b>：前后两段速度不同、时间不同，必须用 总路程 ÷ 总时间。",
           "<b>忘记换单位</b>：km·h⁻¹ 与 m·s⁻¹ 混用，答案差 3,6 倍。",
           "<b>减速时 a 的方向写错</b>：向北减速 → 加速度向南。"],
 defs=[("Displacement", "位移", "The change in position of an object (a vector from initial to final position)."),
       ("Speed", "速率", "The rate of change of distance."),
       ("Velocity", "速度", "The rate of change of position (displacement)."),
       ("Acceleration", "加速度", "The rate of change of velocity.")],
 ex=[dict(n="3.1", lv=1, q="An athlete runs one full lap of a 400 m track in 80 s and finishes at the start. Calculate the average speed and the average velocity.", mk=3, ln=2),
     dict(n="3.2", lv=1, q="A car speeds up uniformly from 10 m·s⁻¹ to 25 m·s⁻¹ east in 5 s. Calculate its acceleration.", mk=3, ln=2),
     dict(n="3.3", lv=2, q="A car travelling north at 90 km·h⁻¹ slows down uniformly to 54 km·h⁻¹ in 4 s. Calculate the magnitude and direction of the acceleration.", mk=4, ln=3),
     dict(n="3.4", lv=2, q="A driver travels 12 km at 60 km·h⁻¹ and then another 12 km at 120 km·h⁻¹. Calculate the average speed for the whole trip.", mk=4, ln=3),
     dict(n="3.5", lv=3, q="A cyclist rides 3 km north in 10 min, then 4 km east in 15 min.<br>(a) Calculate the average speed in m·s⁻¹. (3)　(b) Determine the resultant displacement. (3)　(c) Calculate the average velocity. (2)", mk=8, ln=6)],
 ans_warm=["72 ÷ 3,6 = 20 m·s⁻¹", "2,5 × 60 = 150 s"],
 ans=[("3.1", f"平均速率 = 400/80 {OK} = 5 m·s⁻¹ {OK}；位移 = 0，所以平均速度 = 0 {OK}"),
      ("3.2", f"a = (25 − 10)/5 {OK}{OK} = 3 m·s⁻² east {OK}"),
      ("3.3", f"u = 25 m·s⁻¹，v = 15 m·s⁻¹ {OK}；a = (15 − 25)/4 {OK} = −2,5 m·s⁻² {OK} → 2,5 m·s⁻² south {OK}"),
      ("3.4", f"Δt₁ = 12/60 = 0,2 h {OK}；Δt₂ = 12/120 = 0,1 h {OK}；平均速率 = 24/0,3 {OK} = 80 km·h⁻¹ {OK}（不是 90！）"),
      ("3.5", f"(a) 总路程 7 000 m {OK}，总时间 1 500 s {OK}，速率 = 4,67 m·s⁻¹ {OK}<br>"
              f"(b) Δx = √(3² + 4²) = 5 km {OK}；tan θ = 4/3 → θ = 53,13° E of N（方位角 053,13°） {OK}{OK}<br>"
              f"(c) v = 5 000/1 500 = 3,33 m·s⁻¹ {OK}，方向 053,13° {OK}")]),

# ------------------------------------------------------------------ P05
dict(code="p05", zh="运动学②：四个运动方程", en="Kinematics II — equations of motion",
 bridge="Grade 9 数学：解一元二次方程",
 warm=[("解方程：2x + 5 = 17。", 1), ("把 a = Δv/Δt 变形，写出 Δt 的表达式。", 1)],
 learn="""
<p>四个运动方程<b>只适用于匀加速直线运动</b>（a 不变）。每个方程缺一个量，按“缺什么”选方程。</p>
<p><b>符号</b>：u = 初速度，v = 末速度（旧教材写作 u、v，意思相同）。<b>解题四步：</b>① 规定正方向；② 列出已知量 u、v、a、Δx、Δt（“从静止出发”= u = 0，“停下”= v = 0）；③ 选不含无关量的方程；④ 写出公式 → 代入 → 带单位的答案。</p>
<p><b>追及问题</b>：两车从同一点出发，追上时<b>位移相等</b>。若一辆晚出发 3 s，它的时间是 t，另一辆是 (t + 3)。</p>
<p><b>反应时间</b>内车仍以原速匀速前进，刹车距离要加上这一段。</p>""",
 formulas=[M("v = u + aΔt"), M("Δx = uΔt + ½aΔt²"), M("v² = u² + 2aΔx"), M("Δx = (" + FR("v + u", "2") + ")Δt")],
 pitfalls=["<b>正负号不一致</b>：取向前为正，减速时 a 代入负值。",
           "<b>u 和 v 搞反</b>：u 是初速度（开始时），v 是末速度（结束时）。考试发的公式表用 u、v，旧教材的 u、v 是同一个意思。",
           "<b>追及题忘了时间差</b>：晚出发的物体用时更短。"],
 defs=[("Uniform acceleration", "匀加速", "Acceleration that remains constant in magnitude and direction.")],
 ex=[dict(n="5.1", lv=1, q="A car starts from rest and accelerates uniformly at 3 m·s⁻² for 6 s. Calculate its final velocity and its displacement.", mk=4, ln=3),
     dict(n="5.2", lv=1, q="A car moving at 30 m·s⁻¹ brakes uniformly and stops in 75 m. Calculate the magnitude of its acceleration.", mk=3, ln=2),
     dict(n="5.3", lv=2, q="A cyclist speeds up uniformly from 4 m·s⁻¹ to 10 m·s⁻¹ while covering 42 m. How long does this take?", mk=3, ln=2),
     dict(n="5.4", lv=2, q="A driver travelling at 20 m·s⁻¹ sees a hazard. Her reaction time is 0,5 s, after which she brakes with a deceleration of 5 m·s⁻². Calculate the total stopping distance.", mk=5, ln=3),
     dict(n="5.5", lv=3, q="A speeding car passes a stationary police car at a constant 20 m·s⁻¹. The police car starts 3 s later, accelerating uniformly at 4 m·s⁻². How long after the police car starts does it catch the speeding car, and how far from the starting point?", mk=6, ln=5)],
 ans_warm=["x = 6", "Δt = Δv / a"],
 ans=[("5.1", f"v = 0 + 3(6) {OK} = 18 m·s⁻¹ {OK}；Δx = 0 + ½(3)(6)² {OK} = 54 m {OK}"),
      ("5.2", f"v² = u² + 2aΔx：0 = 30² + 2a(75) {OK}{OK} → a = −6 m·s⁻²，大小 6 m·s⁻² {OK}"),
      ("5.3", f"Δx = ((v + u)/2)Δt：42 = (14/2)Δt {OK}{OK} → Δt = 6 s {OK}"),
      ("5.4", f"反应距离 = 20 × 0,5 = 10 m {OK}{OK}；刹车：0 = 20² + 2(−5)Δx {OK} → Δx = 40 m {OK}；总距离 50 m {OK}"),
      ("5.5", f"设警车用时 t：警车 Δx = ½(4)t² = 2t² {OK}；超速车 Δx = 20(t + 3) {OK}；令相等：2t² = 20t + 60 {OK} → t² − 10t − 30 = 0 {OK}<br>"
              f"t = (10 + √220)/2 = 12,42 s {OK}；距离 = 2(12,42)² ≈ 308,32 m {OK}")]),

# ------------------------------------------------------------------ P07
dict(code="p07", zh="运动学③：运动图像", en="Kinematics III — motion graphs",
 bridge="Grade 9 数学：直线斜率、三角形和梯形面积",
 warm=[("求过点 (0, 2) 和 (4, 10) 的直线的斜率。", 1), ("底 6、高 12 的三角形面积是多少？", 1)],
 learn="""
<p><b>x-t 图</b>：斜率 = 速度。水平线 = 静止；直线 = 匀速；曲线 = 速度在变。</p>
<p><b>v-t 图</b>：斜率 = 加速度；<b>面积 = 位移</b>（时间轴上方为正，下方为负）。水平线 = 匀速（a = 0，合力为 0）。</p>
<p><b>a-t 图</b>：面积 = 速度的变化量 Δv。</p>
<p>画图题的要点：坐标轴名称和单位、关键点数值、形状正确（匀加速时 x-t 是抛物线，匀速时是直线）。</p>""",
 formulas=["x-t：斜率 = " + M("v"), "v-t：斜率 = " + M("a") + "，面积 = " + M("Δx"), "a-t：面积 = " + M("Δv")],
 pitfalls=["<b>v-t 图面积在时间轴以下要算负</b>：求位移时相减，求路程时相加。",
           "<b>x-t 图的“下降”不是减速</b>：它表示往负方向运动。"],
 defs=[("Acceleration", "加速度", "The rate of change of velocity."),
       ("Instantaneous velocity", "瞬时速度", "The velocity of an object at a particular moment in time (the gradient of the x-t graph at that instant).")],
 exfig="ex07",
 ex=[dict(n="7.1", lv=1, q="Use the graph above. Calculate the acceleration of the car from 0 s to 5 s.", mk=3, ln=2),
     dict(n="7.2", lv=1, q="During which time interval is the resultant force on the car zero? Give a reason.", mk=2, ln=1),
     dict(n="7.3", lv=2, q="Calculate the displacement of the car from 0 s to 20 s.", mk=4, ln=3),
     dict(n="7.4", lv=2, q="Calculate the displacement AND the total distance travelled from 0 s to 25 s.", mk=4, ln=2),
     dict(n="7.5", lv=3, q="Sketch the acceleration-time graph for 0–25 s. Show all values on the axes.", mk=4, ln=0, box=26),
     dict(n="7.6", lv=3, q="Describe the motion of the car between 20 s and 25 s (speed and direction).", mk=2, ln=1)],
 ans_warm=["斜率 = (10 − 2)/(4 − 0) = 2", "½ × 6 × 12 = 36"],
 ans=[("7.1", f"a = Δv/Δt = (10 − 0)/5 {OK}{OK} = 2 m·s⁻² north {OK}"),
      ("7.2", f"5 s – 15 s {OK}：速度不变，a = 0，所以合力为零 {OK}"),
      ("7.3", f"面积 = ½(5)(10) + (10)(10) + ½(5)(10) {OK}{OK} = 25 + 100 + 25 {OK} = 150 m north {OK}"),
      ("7.4", f"20–25 s 面积 = ½(5)(−5) = −12,5 m {OK}；位移 = 150 − 12,5 = 137,5 m north {OK}{OK}；路程 = 150 + 12,5 = 162,5 m {OK}"),
      ("7.5", f"0–5 s：+2 m·s⁻² {OK}；5–15 s：0 {OK}；15–20 s：−2 m·s⁻² {OK}；20–25 s：−1 m·s⁻² {OK}（水平线段，阶梯状）"),
      ("7.6", f"从静止开始加速 {OK}，向南运动（速度为负） {OK}")]),

# ------------------------------------------------------------------ P09
dict(code="p09", zh="牛顿定律①：受力分析与 F = ma", en="Newton's laws I — forces & F = ma",
 bridge="Grade 8–9：重力 w = mg、力的单位 N",
 warm=[("质量 50 kg 的学生，重力 w 是多少？（g = 9,8 m·s⁻²）", 1), ("用基本单位表示 1 N。", 1)],
 learn="""
<p>常见的力：<b>重力 w = mg</b>（竖直向下）、<b>法向力 N</b>（垂直于接触面）、<b>摩擦力 f</b>（平行于接触面，阻碍相对运动）、拉力/张力 T、外加力 F。</p>
<p><b>牛顿第一定律（惯性）</b>：合力为零时，物体保持静止或匀速直线运动。<b>牛顿第二定律</b>：F<sub>net</sub> = ma，加速度方向与合力方向相同。</p>
<p><b>摩擦</b>：静摩擦 f<sub>s</sub> 会“跟着”外力变化，最大值 f<sub>s(max)</sub> = μ<sub>s</sub>N；滑动后是动摩擦 f<sub>k</sub> = μ<sub>k</sub>N，大小固定。</p>
<p><b>受力图 FBD</b>：物体画成一个点或方框，所有力从中心画出，标名称。<b>不要画“合力”或“ma”</b>。</p>""",
 formulas=[M("F<sub>net</sub> = ma"), M("F<sub>g</sub> = w = mg"), M("μ<sub>s</sub> = " + FR("f<sub>s(max)</sub>", "N")), M("μ<sub>k</sub> = " + FR("f<sub>k</sub>", "N"))],
 pitfalls=["<b>默认 N = mg</b>：只有水平面、且没有其他竖直方向的力时才成立。斜拉时 N = mg − F sinθ。",
           "<b>受力图漏掉力或多画了“运动方向的力”</b>：匀速运动不需要“向前的力”。",
           "<b>静摩擦都用 μ<sub>s</sub>N 计算</b>：μ<sub>s</sub>N 只是最大值。"],
 defs=[("Newton’s First Law", "牛顿第一定律", "An object continues in a state of rest or uniform motion (constant velocity) unless it is acted upon by a net (resultant) force."),
       ("Newton’s Second Law", "牛顿第二定律", "When a net force acts on an object, the object accelerates in the direction of the net force. The acceleration is directly proportional to the net force and inversely proportional to the mass of the object."),
       ("Inertia", "惯性", "The property of an object that causes it to resist a change in its state of rest or uniform motion."),
       ("Normal force", "法向力", "The force exerted by a surface on an object in contact with it, acting perpendicular to the surface.")],
 ex=[dict(n="9.1", lv=1, q="A resultant force of 12 N acts on a 4 kg box. Calculate its acceleration.", mk=2, ln=1),
     dict(n="9.2", lv=1, q="Draw a labelled free-body diagram for a book lying at rest on a table.", mk=2, ln=0, box=22),
     dict(n="9.3", lv=2, q="A 10 kg box is pulled along a rough horizontal floor by a horizontal force of 50 N. μ<sub>k</sub> = 0,3. Calculate:<br>(a) the normal force (2)　(b) the kinetic frictional force (2)　(c) the acceleration of the box (3)", mk=7, ln=4),
     dict(n="9.4", lv=3, q="The same 10 kg box is now pulled with 50 N at 30° above the horizontal. μ<sub>k</sub> = 0,3.<br>(a) Draw a labelled free-body diagram. (4)　(b) Calculate the normal force. (3)　(c) Calculate the acceleration. (4)", mk=11, ln=6, box=22)],
 ans_warm=["w = 50 × 9,8 = 490 N", "1 N = 1 kg·m·s⁻²"],
 ans=[("9.1", f"a = F<sub>net</sub>/m = 12/4 {OK} = 3 m·s⁻² {OK}（方向与合力相同）"),
      ("9.2", f"向下的重力 w / F<sub>g</sub> {OK}；向上的法向力 N {OK}（两箭头等长）"),
      ("9.3", f"(a) N = mg = 10 × 9,8 {OK} = 98 N {OK}<br>(b) f<sub>k</sub> = μ<sub>k</sub>N = 0,3 × 98 {OK} = 29,4 N {OK}<br>"
              f"(c) F<sub>net</sub> = ma：50 − 29,4 = 10a {OK}{OK} → a = 2,06 m·s⁻² {OK}"),
      ("9.4", f"(a) w 向下、N 向上、F 斜向上 30°、f 与运动方向相反 {OK}{OK}{OK}{OK}<br>"
              f"(b) N + F sin30° = mg {OK} → N = 98 − 25 {OK} = 73 N {OK}<br>"
              f"(c) f<sub>k</sub> = 0,3 × 73 = 21,9 N {OK}；F cos30° = 43,30 N {OK}；43,30 − 21,9 = 10a {OK} → a = 2,14 m·s⁻² {OK}")]),

# ------------------------------------------------------------------ P11
dict(code="p11", zh="牛顿定律②：斜面", en="Newton's laws II — inclined planes",
 bridge="Day 1 的力的分解 + Grade 10 三角函数",
 warm=[("写出 sin 30° 和 cos 30° 的值（保留两位小数）。", 1), ("5 kg 物体的重力是多少？", 1)],
 learn="""
<p>在斜面上，<b>重力不变</b>（仍然竖直向下），但要分解成两个分量：</p>
<ul class="tight"><li>平行斜面向下：<b>w<sub>∥</sub> = mg sinθ</b>（使物体往下滑）</li><li>垂直斜面向内：<b>w<sub>⊥</sub> = mg cosθ</b>（被法向力抵消，N = mg cosθ）</li></ul>
<p>物体<b>静止</b>：静摩擦 f<sub>s</sub> = mg sinθ（沿斜面向上）。物体<b>下滑</b>：F<sub>net</sub> = mg sinθ − f<sub>k</sub>。物体被<b>推上坡</b>：摩擦沿斜面向下，F − mg sinθ − f<sub>k</sub> = ma。</p>
<p>θ 增大 → sinθ 增大、cosθ 减小 → w<sub>∥</sub> 和所需静摩擦增大，N 减小。</p>""",
 formulas=[M("w<sub>∥</sub> = mg sin θ"), M("w<sub>⊥</sub> = mg cos θ = N"), M("f<sub>k</sub> = μ<sub>k</sub> mg cos θ")],
 pitfalls=["<b>sin 和 cos 用反</b>：检查 θ = 0（平地）时，w<sub>∥</sub> 应该等于 0。",
           "<b>摩擦方向画错</b>：摩擦总是和运动（或运动趋势）方向相反，上坡时向下。",
           "<b>斜面上仍写 N = mg</b>：应为 N = mg cosθ。"],
 defs=[("Kinetic friction", "动摩擦力", "The force that opposes the motion of a moving object relative to a surface."),
       ("Static friction", "静摩擦力", "The force that opposes the tendency of motion of a stationary object relative to a surface.")],
 ex=[dict(n="11.1", lv=1, q="A 3 kg block rests on a slope inclined at 30°. Calculate the parallel and perpendicular components of its weight.", mk=4, ln=3),
     dict(n="11.2", lv=1, q="For the block in 11.1, write down the magnitude of (a) the static frictional force and (b) the normal force.", mk=2, ln=1),
     dict(n="11.3", lv=2, q="A 6 kg block slides down a 25° slope. μ<sub>k</sub> = 0,2. Calculate the acceleration of the block.", mk=5, ln=4),
     dict(n="11.4", lv=2, q="The angle of a slope is slowly increased while a block stays at rest. How do the normal force and the static frictional force change? Explain.", mk=3, ln=2),
     dict(n="11.5", lv=3, q="A 2 kg block is pushed up a 20° slope at CONSTANT velocity by a force parallel to the slope. μ<sub>k</sub> = 0,25. Draw a free-body diagram and calculate the pushing force.", mk=6, ln=4, box=18)],
 ans_warm=["sin30° = 0,50；cos30° = 0,87", "w = 5 × 9,8 = 49 N"],
 ans=[("11.1", f"w<sub>∥</sub> = 3(9,8)sin30° {OK} = 14,70 N {OK}；w<sub>⊥</sub> = 3(9,8)cos30° {OK} = 25,46 N {OK}"),
      ("11.2", f"(a) f<sub>s</sub> = 14,70 N（沿斜面向上） {OK}　(b) N = 25,46 N {OK}"),
      ("11.3", f"w<sub>∥</sub> = 6(9,8)sin25° = 24,85 N {OK}；N = 6(9,8)cos25° = 53,29 N {OK}；f<sub>k</sub> = 0,2 × 53,29 = 10,66 N {OK}；"
               f"24,85 − 10,66 = 6a {OK} → a = 2,37 m·s⁻² 沿斜面向下 {OK}"),
      ("11.4", f"N = mg cosθ 减小 {OK}；f<sub>s</sub> = mg sinθ 增大 {OK}；因为 θ 增大时 cosθ 减小、sinθ 增大 {OK}"),
      ("11.5", f"受力图：F 沿斜面向上，w 向下，N 垂直斜面，f 沿斜面向下 {OK}；匀速 → F<sub>net</sub> = 0 {OK}；"
               f"w<sub>∥</sub> = 2(9,8)sin20° = 6,70 N {OK}；f<sub>k</sub> = 0,25 × 2(9,8)cos20° = 4,60 N {OK}；"
               f"F = 6,70 + 4,60 {OK} = 11,31 N {OK}")]),

# ------------------------------------------------------------------ P13
dict(code="p13", zh="牛顿定律③：连接体、第三定律、电梯", en="Newton's laws III — connected bodies, Newton III, lifts",
 bridge="Grade 9：作用力与反作用力",
 warm=[("两个物体 4 kg 和 2 kg，总质量是多少？一起受 30 N 合力，加速度是多少？", 1), ("举一个“作用力与反作用力”的生活例子。", 1)],
 learn="""
<p><b>连接体</b>：轻绳连接的物体有<b>相同的加速度大小</b>；同一根绳两端的张力 T 相等。方法：给每个物体<b>分别</b>画受力图、各列 F<sub>net</sub> = ma，再联立。</p>
<p><b>牛顿第三定律</b>：A 对 B 施力，B 同时对 A 施加大小相等、方向相反的力。这对力<b>作用在两个不同物体上</b>，所以不能互相抵消。“书的重力”的反作用力是“书对地球的引力”，<b>不是</b>桌子的支持力。</p>
<p><b>电梯</b>：体重秤读数 = 法向力 N。向上加速：N − mg = ma，读数变大；向下加速：读数变小；匀速：读数 = mg。</p>""",
 formulas=[M("F<sub>net</sub> = ma") + "（每个物体各列一次）", M("N − mg = ma") + "（电梯，取向上为正）"],
 pitfalls=["<b>把重力和法向力当成第三定律的一对</b>：它们作用在同一个物体上。",
           "<b>连接体只列一个方程</b>：求张力 T 时必须单独分析其中一个物体。",
           "<b>电梯“向下运动”就认为读数变小</b>：要看加速度方向，不是运动方向。"],
 defs=[("Newton’s Third Law", "牛顿第三定律", "When object A exerts a force on object B, object B simultaneously exerts an oppositely directed force of equal magnitude on object A.")],
 ex=[dict(n="13.1", lv=1, q="State Newton’s Third Law of Motion in words.", mk=2, ln=2),
     dict(n="13.2", lv=1, q="Name the reaction force to the weight of a book resting on a table.", mk=1, ln=1),
     dict(n="13.3", lv=2, q="Blocks of 6 kg and 4 kg on a frictionless horizontal surface are joined by a light string. A 30 N force pulls the 6 kg block horizontally. Calculate the acceleration and the tension in the string.", mk=5, ln=4),
     dict(n="13.4", lv=2, q="A 60 kg learner stands on a bathroom scale in a lift that accelerates upward at 1,5 m·s⁻². Calculate the reading on the scale.", mk=4, ln=3),
     dict(n="13.5", lv=3, q="Block A (4 kg) on a rough horizontal table (μ<sub>k</sub> = 0,2) is connected over a frictionless pulley to a hanging block B (2 kg), as in the diagram on the front. Calculate the acceleration of the system and the tension in the string.", mk=6, ln=6)],
 ans_warm=["6 kg；a = 30 ÷ 6 = 5 m·s⁻²", "如：划船时桨推水向后，水推桨向前"],
 ans=[("13.1", f"当 A 对 B 施力时，B 同时对 A 施加一个大小相等 {OK}、方向相反的力 {OK}"),
      ("13.2", f"书对地球的引力（向上） {OK}"),
      ("13.3", f"整体：30 = (6 + 4)a {OK} → a = 3 m·s⁻² {OK}；4 kg 块：T = 4 × 3 {OK}{OK} = 12 N {OK}"),
      ("13.4", f"N − mg = ma {OK}；N = 60(9,8) + 60(1,5) {OK}{OK} = 678 N {OK}"),
      ("13.5", f"f = 0,2 × 4 × 9,8 = 7,84 N {OK}；A：T − 7,84 = 4a {OK}；B：2(9,8) − T = 2a {OK}；相加：19,6 − 7,84 = 6a {OK} → a = 1,96 m·s⁻² {OK}；"
               f"T = 7,84 + 4(1,96) = 15,68 N {OK}")]),

# ------------------------------------------------------------------ P15
dict(code="p15", zh="万有引力", en="Newton's law of universal gravitation",
 bridge="Grade 9 数学：科学记数法、指数运算",
 warm=[("计算 (6 × 10²⁴) × (2 × 10³)。", 1), ("6 400 km 等于多少 m？用科学记数法表示。", 1)],
 learn="""
<p>任何两个有质量的物体都互相吸引：F = Gm₁m₂/r²。力与质量乘积成正比，与距离的<b>平方</b>成反比。</p>
<p><b>r 是两个球心之间的距离</b>：卫星在地面上空 h 处时，r = R<sub>地球</sub> + h。</p>
<p><b>比例题</b>（选择题常考）：先写出 F ∝ m₁m₂/r²，再代入倍数。例如两个质量都加倍、距离变成 3 倍：F' = (2 × 2)/3² F = 4F/9。</p>
<p>星球表面的重力加速度：g = GM/R²。质量 m 是物体本身的属性，到哪里都不变；重力 w = mg 随 g 改变。</p>""",
 formulas=[M("F = " + FR("Gm₁m₂", "r²")), M("g = " + FR("GM", "r²")), M("G = 6,67 × 10⁻¹¹ N·m²·kg⁻²")],
 pitfalls=["<b>r 用了离地高度</b>：必须从球心量起，加上半径。",
           "<b>km 没换成 m</b>：答案会差 10⁶ 倍。",
           "<b>忘了平方</b>：距离变 2 倍，力变成 1/4，而不是 1/2。"],
 defs=[("Newton’s Law of Universal Gravitation", "万有引力定律", "Every particle with mass in the universe attracts every other particle with a force which is directly proportional to the product of their masses and inversely proportional to the square of the distance between their centres."),
       ("Weight", "重力", "The gravitational force the Earth exerts on any object on or near its surface.")],
 ex=[dict(n="15.1", lv=1, q="State Newton’s Law of Universal Gravitation in words.", mk=2, ln=2),
     dict(n="15.2", lv=1, q="Two objects attract with force F. Write down the new force if (a) the distance between them is doubled; (b) both masses are doubled AND the distance is tripled.", mk=4, ln=2),
     dict(n="15.3", lv=2, q="The mass of the Earth is 5,97 × 10²⁴ kg and its radius is 6,38 × 10⁶ m. Calculate g at the Earth’s surface.", mk=3, ln=2),
     dict(n="15.4", lv=2, q="A 500 kg satellite orbits at a height of 3,6 × 10⁷ m ABOVE the Earth’s surface. Calculate the gravitational force of the Earth on the satellite.", mk=4, ln=3),
     dict(n="15.5", lv=3, q="Planet X has twice the mass of the Earth and half its radius. (a) Express g on planet X in terms of g on Earth. (3)　(b) What is the weight of a 60 kg astronaut on planet X? (2)", mk=5, ln=4)],
 ans_warm=["1,2 × 10²⁸", "6,4 × 10⁶ m"],
 ans=[("15.1", f"任何两个物体之间的引力与它们质量的乘积成正比 {OK}，与它们球心之间距离的平方成反比 {OK}"),
      ("15.2", f"(a) F/4 {OK}{OK}　(b) (2 × 2)/3² = 4F/9 {OK}{OK}"),
      ("15.3", f"g = GM/r² = (6,67 × 10⁻¹¹)(5,97 × 10²⁴)/(6,38 × 10⁶)² {OK}{OK} = 9,78 m·s⁻² {OK}"),
      ("15.4", f"r = 6,38 × 10⁶ + 3,6 × 10⁷ = 4,238 × 10⁷ m {OK}；F = (6,67 × 10⁻¹¹)(5,97 × 10²⁴)(500)/(4,238 × 10⁷)² {OK}{OK} = 110,85 N {OK}"),
      ("15.5", f"(a) g<sub>X</sub> = G(2M)/(½R)² {OK} = 8GM/R² {OK} = 8g {OK}　(b) w = 60 × 8 × 9,8 {OK} = 4 704 N {OK}")]),

# ------------------------------------------------------------------ P17
dict(code="p17", zh="静电学①：电荷与库仑定律", en="Electrostatics I — charge & Coulomb's law",
 bridge="Grade 8–9：原子结构、电子带负电",
 warm=[("原子中哪种粒子可以从一个物体转移到另一个物体？", 1), ("把 3 μC 和 5 nC 用 C 表示。", 1)],
 learn="""
<p>物体带电是因为<b>电子转移</b>：得到电子带负电，失去电子带正电（质子不移动）。电荷量是电子电荷的整数倍：Q = n·e，e = 1,6 × 10⁻¹⁹ C。</p>
<p><b>电荷守恒</b>：孤立系统总电荷不变。<b>两个相同的导体球接触后分开</b>：各自得到 (Q₁ + Q₂)/2。</p>
<p><b>库仑定律</b>：F = kQ₁Q₂/r²。代入时<b>只代大小（不带正负号）</b>，然后用文字说明是吸引（异号）还是排斥（同号）。</p>
<p>三个电荷在一条直线上：分别求另外两个电荷对它的力，<b>按方向</b>相加减。</p>""",
 formulas=[M("Q = n·e"), M("Q<sub>new</sub> = " + FR("Q₁ + Q₂", "2")), M("F = " + FR("kQ₁Q₂", "r²")), M("k = 9,0 × 10⁹ N·m²·C⁻²")],
 pitfalls=["<b>说质子在移动</b>：只有电子会转移。",
           "<b>μC、nC、cm 没有换算</b>：μ = 10⁻⁶，n = 10⁻⁹，cm ÷ 100。",
           "<b>多个力直接相加</b>：先判断每个力的方向，同向相加，反向相减。"],
 defs=[("Principle of conservation of charge", "电荷守恒", "The net charge of an isolated system remains constant during any physical process."),
       ("Principle of charge quantization", "电荷量子化", "Every charge is an integer multiple of the charge of an electron (e = 1,6 × 10⁻¹⁹ C)."),
       ("Coulomb’s Law", "库仑定律", "The magnitude of the electrostatic force exerted by one point charge on another is directly proportional to the product of the magnitudes of the charges and inversely proportional to the square of the distance between them.")],
 ex=[dict(n="17.1", lv=1, q="State the principle of conservation of charge.", mk=2, ln=1),
     dict(n="17.2", lv=1, q="Identical spheres A (+8 nC) and B (−2 nC) touch and are separated. (a) Calculate the final charge on each sphere. (2)　(b) Calculate the number of electrons transferred and state the direction of transfer. (4)", mk=6, ln=4),
     dict(n="17.3", lv=1, q="State Coulomb’s law in words.", mk=2, ln=2),
     dict(n="17.4", lv=2, q="Calculate the electrostatic force between a +3 μC and a −4 μC point charge 20 cm apart. Is the force attractive or repulsive?", mk=4, ln=3),
     dict(n="17.5", lv=3, q="Three point charges lie on a straight line: A (+2 μC) at 0 m, B (−3 μC) at 0,3 m and C (+1 μC) at 0,5 m. Calculate the net electrostatic force on B.", mk=6, ln=6)],
 ans_warm=["电子 electron", "3 × 10⁻⁶ C；5 × 10⁻⁹ C"],
 ans=[("17.1", f"孤立系统的总电荷在任何过程中保持不变 {OK}{OK}"),
      ("17.2", f"(a) (+8 − 2)/2 {OK} = +3 nC 各 {OK}<br>(b) A 的电荷变化 = +3 − (+8) = −5 nC {OK}；n = 5 × 10⁻⁹/1,6 × 10⁻¹⁹ {OK} = 3,13 × 10¹⁰ 个电子 {OK}，从 B 转移到 A {OK}"),
      ("17.3", f"两个点电荷之间的静电力与电荷量的乘积成正比 {OK}，与距离的平方成反比 {OK}"),
      ("17.4", f"F = (9 × 10⁹)(3 × 10⁻⁶)(4 × 10⁻⁶)/(0,2)² {OK}{OK} = 2,70 N {OK}，吸引 attractive {OK}"),
      ("17.5", f"F<sub>AB</sub> = (9 × 10⁹)(2 × 10⁻⁶)(3 × 10⁻⁶)/0,3² {OK} = 0,60 N，指向 A（向左） {OK}；"
               f"F<sub>CB</sub> = (9 × 10⁹)(1 × 10⁻⁶)(3 × 10⁻⁶)/0,2² {OK} = 0,675 N，指向 C（向右） {OK}；"
               f"F<sub>net</sub> = 0,675 − 0,60 {OK} = 0,075 N，指向 C（向右） {OK}")]),

# ------------------------------------------------------------------ P19
dict(code="p19", zh="静电学②：电场", en="Electrostatics II — electric fields",
 bridge="Day 1 矢量在一条直线上的加减",
 warm=[("5 N 向右 + 3 N 向左 = ？", 1), ("距离从 10 cm 变成 20 cm，1/r² 变为原来的几倍？", 1)],
 learn="""
<p><b>电场 electric field</b>：电荷周围的一个区域，放在其中的电荷会受到力。电场方向 = <b>正</b>试探电荷在该点受力的方向。</p>
<p><b>电场线</b>：从正电荷出发、到负电荷结束；线不相交；越密的地方电场越强；画图时要有箭头，且与电荷表面垂直。</p>
<p>点电荷的电场强度：E = kQ/r²（只代大小）。正电荷的场<b>背离</b>它，负电荷的场<b>指向</b>它。</p>
<p>某点的<b>合电场</b>：分别求每个电荷在该点产生的 E，判断方向，再按矢量相加。电荷 q 在该点受力：F = qE。</p>""",
 formulas=[M("E = " + FR("F", "q")), M("E = " + FR("kQ", "r²")), "单位 " + M("N·C⁻¹")],
 pitfalls=["<b>把电场方向和“电荷移动方向”混淆</b>：负电荷受力方向与 E 相反。",
           "<b>电场线画成相交或没有箭头</b>：会被扣分。",
           "<b>合电场方向判断错误</b>：在两个异号电荷之间，两个场方向相同（都指向负电荷），要相加。"],
 defs=[("Electric field", "电场", "A region of space in which an electric charge experiences a force."),
       ("Electric field at a point", "某点的电场强度", "The electrostatic force experienced per unit positive charge placed at that point.")],
 ex=[dict(n="19.1", lv=1, q="Define electric field.", mk=2, ln=1),
     dict(n="19.2", lv=1, q="Sketch the electric field pattern around two equal POSITIVE point charges placed close together.", mk=3, ln=0, box=24),
     dict(n="19.3", lv=2, q="Calculate the magnitude and direction of the electric field 15 cm from a +5 nC point charge.", mk=3, ln=2),
     dict(n="19.4", lv=2, q="A −2 nC charge is placed at the point in 19.3. Calculate the force on it and state its direction.", mk=3, ln=2),
     dict(n="19.5", lv=3, q="A (+4 nC) and B (−6 nC) are 30 cm apart. Point P lies on the line between them, 10 cm from A. Calculate the net electric field at P.", mk=6, ln=6)],
 ans_warm=["2 N 向右", "1/4"],
 ans=[("19.1", f"电荷在其中会受到力的空间区域 {OK}{OK}"),
      ("19.2", f"箭头从两个电荷向外 {OK}；线不相交、中间有“无场点” {OK}；对称 {OK}"),
      ("19.3", f"E = (9 × 10⁹)(5 × 10⁻⁹)/0,15² {OK} = 2 000 N·C⁻¹ {OK}，背离电荷 {OK}"),
      ("19.4", f"F = qE = (2 × 10⁻⁹)(2 000) {OK} = 4 × 10⁻⁶ N {OK}，指向 +5 nC 电荷 {OK}"),
      ("19.5", f"E<sub>A</sub> = (9 × 10⁹)(4 × 10⁻⁹)/0,1² {OK} = 3 600 N·C⁻¹，指向 B（背离 A） {OK}；"
               f"E<sub>B</sub> = (9 × 10⁹)(6 × 10⁻⁹)/0,2² {OK} = 1 350 N·C⁻¹，指向 B {OK}；"
               f"同向相加：E<sub>net</sub> = 4 950 N·C⁻¹ {OK}，指向 B {OK}")]),

# ------------------------------------------------------------------ P21
dict(code="p21", zh="电路①：欧姆定律与串并联", en="Electric circuits I — Ohm's law, series & parallel",
 bridge="Grade 9：电流、电压、电阻的基本概念",
 warm=[("计算：1/R = 1/6 + 1/3，求 R。", 1), ("电流表和电压表分别怎么接入电路？", 1)],
 learn="""
<p><b>电流 I = Q/Δt</b>（电荷的流动速率，A）；<b>电势差 V = W/q</b>（每库仑电荷获得或消耗的能量，V）；<b>电阻 R = V/I</b>（Ω）。</p>
<p><b>欧姆定律</b>：温度不变时，导体中的电流与两端电压成正比。灯泡变热后电阻变大，I-V 图弯曲，不是欧姆导体。</p>
<p><b>串联</b>：电流处处相等；电压分配，V = V₁ + V₂；R = R₁ + R₂。<b>并联</b>：各支路电压相同；电流分配，I = I₁ + I₂；1/R = 1/R₁ + 1/R₂，<b>并联总电阻比最小的那个还小</b>。</p>
<p>复杂电路的步骤：先算并联部分 → 再算总电阻 → 总电流 → 每一部分的电压 → 支路电流。</p>""",
 formulas=[M("I = " + FR("Q", "Δt")), M("V = " + FR("W", "q")), M("R = " + FR("V", "I")), M("R<sub>s</sub> = R₁ + R₂"), M(FR("1", "R<sub>p</sub>") + " = " + FR("1", "R₁") + " + " + FR("1", "R₂"))],
 pitfalls=["<b>1/R 算完忘了取倒数</b>：1/R = 0,25 → R = 4 Ω。",
           "<b>并联支路用总电压</b>：如果电路中还有串联电阻，并联部分只分到一部分电压。"],
 defs=[("Current", "电流", "The rate of flow of charge."),
       ("Potential difference", "电势差", "The work done per unit positive charge to move it between two points."),
       ("Resistance", "电阻", "The opposition to the flow of electric current (ratio of potential difference to current)."),
       ("Ohm’s Law", "欧姆定律", "The potential difference across a conductor is directly proportional to the current in the conductor at constant temperature.")],
 exfig="ex21",
 ex=[dict(n="21.1", lv=1, q="A charge of 30 C passes a point in a circuit in 2 minutes. Calculate the current.", mk=3, ln=1),
     dict(n="21.2", lv=1, q="State Ohm’s law in words.", mk=2, ln=2),
     dict(n="21.3", lv=2, q="For the circuit above, calculate: (a) the total resistance (3); (b) the current through the battery (2); (c) the potential difference across the parallel section (2); (d) the current in the 6 Ω resistor (2).", mk=9, ln=5),
     dict(n="21.4", lv=2, q="The I-V graph of a filament lamp is curved. Explain why the lamp does not obey Ohm’s law.", mk=2, ln=2),
     dict(n="21.5", lv=3, q="A potential difference of 8 V is applied across a 20 Ω resistor. Calculate the number of electrons that pass through the resistor in 10 s.", mk=5, ln=3)],
 ans_warm=["1/R = 1/6 + 2/6 = 1/2 → R = 2 Ω", "电流表串联；电压表并联"],
 ans=[("21.1", f"I = Q/Δt = 30/120 {OK}{OK} = 0,25 A {OK}"),
      ("21.2", f"温度不变时 {OK}，导体两端的电势差与通过它的电流成正比 {OK}"),
      ("21.3", f"(a) 1/R<sub>p</sub> = 1/6 + 1/12 {OK} → R<sub>p</sub> = 4 Ω {OK}；R<sub>总</sub> = 4 + 4 = 8 Ω {OK}<br>"
               f"(b) I = 12/8 {OK} = 1,5 A {OK}　(c) V<sub>p</sub> = IR<sub>p</sub> = 1,5 × 4 {OK} = 6 V {OK}　(d) I = 6/6 {OK} = 1 A {OK}"),
      ("21.4", f"电流使灯丝温度升高 {OK}，电阻随温度增大，V/I 不再是常数 {OK}"),
      ("21.5", f"I = V/R = 8/20 = 0,4 A {OK}；Q = IΔt = 0,4 × 10 = 4 C {OK}{OK}；n = Q/e = 4/1,6 × 10⁻¹⁹ {OK} = 2,5 × 10¹⁹ 个 {OK}")]),

# ------------------------------------------------------------------ P23
dict(code="p23", zh="电路②：电动势、内阻、功率与电费", en="Electric circuits II — emf, internal resistance, power",
 bridge="Grade 9：P = VI、千瓦时 kWh",
 warm=[("230 V、2 A 的电器功率是多少？", 1), ("3 kW 的电器用 2 小时，消耗多少 kWh？", 1)],
 learn="""
<p><b>电动势 emf (ε)</b>：电池<b>没有电流</b>时两端的电压。电池内部有<b>内阻 r</b>，有电流时一部分电压“损失”在内阻上：<b>lost volts = Ir</b>。</p>
<p><b>端电压</b> V = ε − Ir。外电阻越小 → 电流越大 → lost volts 越大 → 端电压越低。完整公式：<b>ε = I(R + r)</b>，R 是外电路总电阻。</p>
<p>V-I 图：直线的 <b>y 截距 = ε</b>，<b>斜率 = −r</b>。</p>
<p><b>功率</b> P = W/Δt = VI = I²R = V²/R；<b>能量</b> W = PΔt。电费：kW × h = kWh，再乘以单价。</p>""",
 formulas=[M("ε = I(R + r)"), M("V = ε − Ir"), M("P = VI = I²R = " + FR("V²", "R")), M("W = PΔt"), M("1 kWh = 3,6 × 10⁶ J")],
 pitfalls=["<b>功率用 W 而不是 kW 算电费</b>：2 000 W = 2 kW。",
           "<b>把 ε 当作端电压</b>：只有 I = 0 时 V = ε。",
           "<b>ε = I(R + r) 中的 R 只用了一个电阻</b>：要用外电路的总电阻。"],
 defs=[("Emf", "电动势", "The maximum energy provided by a battery per coulomb of charge passing through it (the potential difference across the battery when no current flows)."),
       ("Power", "功率", "The rate at which work is done (or energy is transferred)."),
       ("Internal resistance", "内阻", "The resistance within a battery that causes a drop in potential difference (lost volts) when current flows.")],
 ex=[dict(n="23.1", lv=1, q="Define emf.", mk=2, ln=1),
     dict(n="23.2", lv=1, q="A battery has an emf of 9 V. When it delivers 0,5 A, the potential difference across its terminals is 7,5 V. Calculate its internal resistance.", mk=3, ln=2),
     dict(n="23.3", lv=2, q="A battery (emf 12 V, internal resistance 0,5 Ω) is connected to an external resistor of 5,5 Ω. Calculate (a) the current; (b) the terminal potential difference; (c) the power dissipated in the external resistor.", mk=6, ln=5),
     dict(n="23.4", lv=2, q="A 2 000 W kettle is used for 15 minutes every day for 30 days. Electricity costs R3,20 per kWh. Calculate the cost.", mk=4, ln=3),
     dict(n="23.5", lv=3, q="For a battery, the terminal potential difference is 5,4 V when the current is 0,4 A, and 4,2 V when the current is 1,2 A. Determine the emf and the internal resistance of the battery.", mk=5, ln=5)],
 ans_warm=["P = 230 × 2 = 460 W", "3 × 2 = 6 kWh"],
 ans=[("23.1", f"电池在没有电流时两端的电势差（每库仑电荷获得的最大能量） {OK}{OK}"),
      ("23.2", f"lost volts = 9 − 7,5 = 1,5 V {OK}；r = 1,5/0,5 {OK} = 3 Ω {OK}"),
      ("23.3", f"(a) 12 = I(5,5 + 0,5) {OK} → I = 2 A {OK}　(b) V = 2 × 5,5 {OK} = 11 V {OK}　(c) P = I²R = 2² × 5,5 {OK} = 22 W {OK}"),
      ("23.4", f"W = 2 kW × 0,25 h × 30 {OK}{OK} = 15 kWh {OK}；费用 = 15 × 3,20 = R48,00 {OK}"),
      ("23.5", f"V = ε − Ir：5,4 = ε − 0,4r，4,2 = ε − 1,2r {OK}{OK}；相减：1,2 = 0,8r → r = 1,5 Ω {OK}；ε = 5,4 + 0,4(1,5) {OK} = 6,0 V {OK}")]),
]

# 根据近期测验（2026 年 8 月 Cycle Test、随堂测验）暴露的弱项补充的物理日
PHYS_EXTRA = [
# ------------------------------------------------------------------ P25
dict(code="p25", zh="电磁感应①：磁通量与法拉第定律", en="Electromagnetism I — magnetic flux & Faraday's law",
 bridge="Grade 9：磁铁与磁场；Day 15 科学记数法",
 warm=[("800 cm² 等于多少 m²？", 1), ("cos 0°、cos 90° 分别等于多少？", 1)],
 learn="""
<p><b>电流产生磁场</b>：通电直导线周围的磁场是一圈圈同心圆。<b>右手定则</b>：大拇指指电流方向，四指弯曲的方向就是磁场方向。⊙ 表示电流流出纸面（磁场逆时针），⊗ 表示流入纸面（磁场顺时针）。螺线管：四指顺着电流绕，大拇指指向 N 极。</p>
<p><b>磁通量 Φ = BA cosθ</b>（单位 Wb），θ 是磁场 B 与线圈平面<b>法线 normal</b> 之间的夹角：线圈平面与磁场垂直时 θ = 0°，Φ 最大；平面与磁场平行时 Φ = 0。<b>磁通链 flux linkage = NΦ</b>（N 为匝数）。</p>
<p><b>法拉第定律</b>：穿过线圈的磁通发生<b>变化</b>时产生感应电动势，emf = −NΔΦ/Δt，其中 ΔΦ = Φ<sub>末</sub> − Φ<sub>初</sub>。<b>增大 emf 的方法</b>：增加匝数 N；更快地改变（Δt 更小）；用更强的磁场；增大线圈面积。</p>""",
 formulas=[M("Φ = BA cos θ"), "磁通链 " + M("NΦ"), M("emf = −N" + FR("ΔΦ", "Δt")), M("1 cm² = 10⁻⁴ m²")],
 pitfalls=["<b>cm² 换算成 m² 写成 ×10⁻²</b>：面积要 ×10⁻⁴，例如 800 cm² = 0,08 m²。",
           "<b>问“磁通链”却只算了 Φ</b>：磁通链 = NΦ，要乘匝数。",
           "<b>数量级算错</b>：算完 emf 检查 10 的幂次；θ 是磁场与线圈<b>法线</b>的夹角，不是与平面的夹角。"],
 defs=[("Magnetic field", "磁场", "A region in space where a magnet or a ferromagnetic material experiences a (non-contact) force."),
       ("Magnetic flux", "磁通量", "The product of the component of the magnetic field perpendicular to a surface and the area of that surface (Φ = BA cos θ)."),
       ("Faraday’s Law of electromagnetic induction", "法拉第电磁感应定律", "The magnitude of the induced emf across the ends of a conductor is directly proportional to the rate of change in the magnetic flux linkage with the conductor.")],
 ex=[dict(n="25.1", lv=1, q="Draw the magnetic field pattern around a straight conductor carrying current INTO the page (⊗). Show the direction.", mk=2, ln=0, box=18),
     dict(n="25.2", lv=2, q="A rectangular coil of 200 turns measures 0,2 m × 0,3 m. Its plane is perpendicular to a uniform magnetic field. The field increases uniformly from 0,4 T to 1,2 T in 0,5 s. Calculate (a) the area of the coil (1); (b) the change in magnetic flux (3); (c) the magnitude of the induced emf (3).", mk=7, ln=5),
     dict(n="25.3", lv=2, q="A coil of 150 turns and area 40 cm² is held with its axis parallel to a magnetic field of 0,5 T. Calculate the magnetic flux linkage.", mk=3, ln=2),
     dict(n="25.4", lv=2, q="State THREE ways to increase the magnitude of the emf induced in a coil.", mk=3, ln=2),
     dict(n="25.5", lv=3, q="A coil of 100 turns and area 0,02 m² is in a field of 0,8 T with its plane perpendicular to the field. It is rotated through 90° in 0,1 s so that its plane becomes parallel to the field. Calculate the average induced emf.", mk=5, ln=4)],
 ans_warm=["800 × 10⁻⁴ = 0,08 m²", "cos 0° = 1；cos 90° = 0"],
 ans=[("25.1", f"以导线为圆心的同心圆 {OK}；方向顺时针 {OK}"),
      ("25.2", f"(a) A = 0,2 × 0,3 = 0,06 m² {OK}<br>(b) ΔΦ = ΔB·A cos0° {OK} = (1,2 − 0,4)(0,06)(1) {OK} = 0,048 Wb {OK}<br>"
               f"(c) emf = NΔΦ/Δt = 200 × 0,048 / 0,5 {OK}{OK} = 19,2 V {OK}"),
      ("25.3", f"A = 40 × 10⁻⁴ = 4 × 10⁻³ m² {OK}；Φ = 0,5 × 4 × 10⁻³ × cos0° = 2 × 10⁻³ Wb {OK}；NΦ = 150 × 2 × 10⁻³ = 0,30 Wb {OK}"),
      ("25.4", f"增加匝数 {OK}；更快地移动磁铁或线圈（缩短 Δt） {OK}；使用更强的磁场或更大的线圈面积 {OK}"),
      ("25.5", f"Φ<sub>初</sub> = 0,8 × 0,02 × cos0° = 0,016 Wb {OK}；Φ<sub>末</sub> = 0（cos90° = 0） {OK}；ΔΦ = −0,016 Wb {OK}；"
               f"emf = −100 × (−0,016)/0,1 {OK} = 16 V {OK}")]),

# ------------------------------------------------------------------ P26
dict(code="p26", zh="电磁感应②：楞次定律、变压器、高压输电", en="Electromagnetism II — Lenz's law, transformers, power transmission",
 bridge="Day 23 的 P = VI 和 P = I²R",
 warm=[("1 000 W 的电器接 250 V，电流是多少？", 1), ("电流 4 A 通过 2 Ω 的导线，发热功率 I²R 是多少？", 1)],
 learn="""
<p><b>楞次定律 Lenz's law</b>：感应电流的方向，总是使它产生的磁场<b>反对引起它的磁通变化</b>。口诀“来拒去留”：磁铁 N 极靠近线圈 → 线圈这一端变成 N 极（排斥）；N 极离开 → 这一端变成 S 极（吸引）。</p>
<p><b>变压器只能用交流 AC</b>：原线圈中的交流电使铁芯里的磁通<b>不断变化</b> → 副线圈产生感应 emf。稳定的直流 DC 只在接通瞬间有变化，之后磁通不变 → 没有感应电流。理想变压器：V<sub>s</sub>/V<sub>p</sub> = N<sub>s</sub>/N<sub>p</sub>；N<sub>s</sub> &gt; N<sub>p</sub> 为升压，反之为降压。</p>
<p><b>为什么 Eskom 用高压输电</b>：输送功率 P = VI 一定时，电压升高 → <b>电流减小</b> → 输电线上的热损耗 P<sub>损</sub> = I²R 大大减小。到用户附近再用降压变压器降压。</p>
<p class="warm"><b>解释题四步模板</b>：① 什么在变化（磁通？）→ ② 法拉第：产生感应 emf / 电流 → ③ 楞次：感应磁场方向反对这个变化 → ④ 结果（排斥、吸引、环跳起……）。每一步一句话，写完再停。</p>""",
 formulas=[M(FR("V<sub>s</sub>", "V<sub>p</sub>") + " = " + FR("N<sub>s</sub>", "N<sub>p</sub>")), M("V<sub>p</sub>I<sub>p</sub> = V<sub>s</sub>I<sub>s</sub>"), M("P<sub>损</sub> = I²R")],
 pitfalls=["<b>高压输电写成“为了减少电压损失”</b>：得 0 分。要写：电压升高 → 电流减小 → I²R 热损耗减小。",
           "<b>楞次定律只写“方向相反”</b>：要写“反对<b>磁通的变化</b>”，不是反对磁场本身。",
           "<b>解释题写成一大段</b>：按四步模板，每步一句，关键词必须出现（磁通变化、感应电流、反对、排斥）。"],
 defs=[("Lenz’s Law", "楞次定律", "The induced current flows in a direction so as to set up a magnetic field that opposes the change in magnetic flux that produced it."),
       ("Step-up transformer", "升压变压器", "A transformer with more turns on the secondary coil than on the primary coil, so that the secondary voltage is greater than the primary voltage.")],
 ex=[dict(n="26.1", lv=1, q="State Lenz’s law in words.", mk=2, ln=2),
     dict(n="26.2", lv=1, q="An ideal transformer has 200 turns on the primary and 50 turns on the secondary coil. The primary is connected to 240 V AC. Calculate the secondary voltage and state whether it is a step-up or step-down transformer.", mk=3, ln=2),
     dict(n="26.3", lv=2, q="The north pole of a bar magnet is pulled AWAY from end X of a solenoid. Which magnetic pole forms at X? Explain using Lenz’s law.", mk=3, ln=3),
     dict(n="26.4", lv=2, q="A power station sends 50 kW through cables with a total resistance of 4 Ω. Calculate the power lost in the cables when the power is transmitted at (a) 1 000 V and (b) 10 000 V. (c) What does this show?", mk=5, ln=3),
     dict(n="26.5", lv=2, q="For an ideal transformer, V<sub>p</sub> = 240 V, I<sub>p</sub> = 0,5 A and V<sub>s</sub> = 12 V. Calculate I<sub>s</sub>.", mk=3, ln=2),
     dict(n="26.6", lv=3, q="Explain why a transformer does not work with a steady DC supply. Use the four-step template.", mk=3, ln=3)],
 ans_warm=["I = P/V = 1 000/250 = 4 A", "P = 4² × 2 = 32 W"],
 ans=[("26.1", f"感应电流的方向使它产生的磁场 {OK} 反对引起它的磁通变化 {OK}"),
      ("26.2", f"V<sub>s</sub>/240 = 50/200 {OK} → V<sub>s</sub> = 60 V {OK}；降压变压器 step-down {OK}"),
      ("26.3", f"S 极 {OK}；N 极离开使穿过线圈的磁通减小 {OK}；感应电流的磁场反对这种减小，在 X 端形成 S 极吸引磁铁（反对它离开） {OK}"),
      ("26.4", f"(a) I = 50 000/1 000 = 50 A {OK}；P<sub>损</sub> = 50² × 4 = 10 000 W {OK}　(b) I = 5 A {OK}；P<sub>损</sub> = 5² × 4 = 100 W {OK}<br>"
               f"(c) 电压提高 10 倍，电流减小 10 倍，损耗减小 100 倍，所以要用高压输电 {OK}"),
      ("26.5", f"V<sub>p</sub>I<sub>p</sub> = V<sub>s</sub>I<sub>s</sub> {OK}；240 × 0,5 = 12 I<sub>s</sub> {OK} → I<sub>s</sub> = 10 A {OK}"),
      ("26.6", f"稳定的直流在铁芯中产生不变的磁场，磁通不变 {OK}；没有磁通变化就没有感应 emf（法拉第定律） {OK}；所以副线圈中没有感应电流和输出电压 {OK}")]),

# ------------------------------------------------------------------ P27
dict(code="p27", zh="静电专练：比例推理、零场点、电子转移", en="Electrostatics practice — ratios, zero-field points, electron transfer",
 bridge="Day 17、Day 19 的库仑定律与电场",
 warm=[("距离变为原来的 1/2，F ∝ 1/r² 中的力变为原来的几倍？", 1), ("计算 (30/20)²。", 1)],
 learn="""
<p><b>比例法（不用 k 计算）</b>：F ∝ 1/r²，所以 F₂ = F₁ × (r₁/r₂)²。例：r 从 30 mm 变成 20 mm，F × (30/20)² = F × 2,25。表格题里“不用计算求缺失值”就用这个方法。</p>
<p><b>图像</b>：F 对 1/r² 作图是<b>过原点的直线</b>；F 对 r 或 r² 作图是下降的曲线。同一个电荷 q 放在不同电场中，F = qE，所以 F 对 E 是<b>过原点的直线</b>。E 对距离作图：电荷越大，同一距离处 E 越大，曲线越高。</p>
<p><b>零场点 E = 0</b>：两个<b>同号</b>电荷之间有一点合电场为零，位置<b>靠近较小的电荷</b>；令 kQ₁/x² = kQ₂/(d − x)² 求 x。两个异号电荷之间不可能为零。</p>
<p><b>电子转移数</b>：先求<b>其中一个球</b>的电荷变化量 ΔQ = Q<sub>末</sub> − Q<sub>初</sub>，再 n = |ΔQ|/e。ΔQ 为正说明这个球失去了电子。</p>""",
 formulas=[M("F₂ = F₁ (" + FR("r₁", "r₂") + ")²"), M("F = qE"), "零场点：" + M(FR("kQ₁", "x²") + " = " + FR("kQ₂", "(d − x)²")), M("n = " + FR("|ΔQ|", "e"))],
 pitfalls=["<b>表格缺失值题直接套 kQ₁Q₂/r²</b>：不知道电荷时，用比例 F₂ = F₁(r₁/r₂)²。",
           "<b>零场点找在大电荷附近</b>：应在<b>小电荷</b>一侧。",
           "<b>电子转移数用两个球的电荷差</b>：要用<b>一个球</b>前后电荷的变化。"],
 defs=[("Coulomb’s Law", "库仑定律", "The magnitude of the electrostatic force exerted by one point charge on another is directly proportional to the product of the magnitudes of the charges and inversely proportional to the square of the distance between them."),
       ("Electric field at a point", "某点的电场强度", "The electrostatic force experienced per unit positive charge placed at that point.")],
 ex=[dict(n="27.1", lv=1, q="Two charges exert a force of 40 N on each other when 30 mm apart. Without using k, determine the force when they are (a) 20 mm apart and (b) 60 mm apart.", mk=4, ln=3),
     dict(n="27.2", lv=1, q="Which graph gives a straight line through the origin: F vs r, F vs r², or F vs 1/r²?", mk=1, ln=1),
     dict(n="27.3", lv=2, q="Point charges +Q and +9Q are 12 cm apart. Calculate how far from +Q the net electric field is zero.", mk=4, ln=3),
     dict(n="27.4", lv=2, q="Identical spheres A (−6 pC) and B (−2 pC) touch and are separated. Calculate the number of electrons transferred and state the direction of transfer.", mk=4, ln=3),
     dict(n="27.5", lv=3, q="On the same set of axes, sketch graphs of electric field strength E against distance for a +2 nC and a +4 nC point charge. Label the graphs.", mk=3, ln=0, box=24),
     dict(n="27.6", lv=3, q="The same charge q is placed in electric fields of different strength. Sketch the graph of force F against field strength E, and state what the gradient represents.", mk=2, ln=0, box=18)],
 ans_warm=["4 倍", "2,25"],
 ans=[("27.1", f"(a) F = 40 × (30/20)² {OK} = 90 N {OK}　(b) F = 40 × (30/60)² {OK} = 10 N {OK}"),
      ("27.2", f"F vs 1/r² {OK}"),
      ("27.3", f"kQ/x² = k(9Q)/(12 − x)² {OK}{OK}；(12 − x)/x = 3 {OK} → x = 3 cm（距 +Q） {OK}"),
      ("27.4", f"Q<sub>末</sub> = (−6 − 2)/2 = −4 pC {OK}；A：ΔQ = −4 − (−6) = +2 pC，A 失去电子 {OK}；n = 2 × 10⁻¹²/1,6 × 10⁻¹⁹ = 1,25 × 10⁷ 个 {OK}；从 A 转移到 B {OK}"),
      ("27.5", f"两条都是随距离迅速下降的曲线（反平方） {OK}；+4 nC 的曲线在每个距离处都更高 {OK}；曲线不与坐标轴相交，标出两条曲线 {OK}"),
      ("27.6", f"过原点的直线 {OK}；斜率 = q（电荷量） {OK}")]),
]
