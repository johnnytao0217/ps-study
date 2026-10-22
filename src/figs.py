"""每日图解（SVG）。静态时显示完整终态；.fig.play 时按 --d 顺序动画。"""
import math

COL = {"k": "#1f2937", "r": "#dc2626", "b": "#2563eb", "g": "#059669", "a": "#d97706", "s": "#6b7280", "p": "#7c3aed"}


def defs(p):
    ms = "".join(
        f'<marker id="{p}{n}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        f'<path d="M0 0L10 5L0 10z" fill="{c}"/></marker>' for n, c in COL.items())
    return f"<defs>{ms}</defs>"


def st(d=None, extra=""):
    s = (f"--d:{d}s;" if d is not None else "") + extra
    return f' style="{s}"' if s else ""


def arrow(p, x1, y1, x2, y2, c="k", w=2.4, d=None, dash=False):
    da = ' stroke-dasharray="6 4"' if dash else ""
    cls = ' class="fd"' if d is not None else ""
    return (f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{COL[c]}" stroke-width="{w}"'
            f' marker-end="url(#{p}{c})"{da}{cls}{st(d)}/>')


def path(dstr, c="k", w=2.2, d=None, length=None, fill="none", dash=False, cls=None):
    if cls is None:
        cls = "dr" if (d is not None and length) else ("fd" if d is not None else "")
    extra = f"--len:{length:.0f};" if length else ""
    da = ' stroke-dasharray="6 4"' if dash else ""
    c_ = f' class="{cls}"' if cls else ""
    return f'<path d="{dstr}" stroke="{COL.get(c, c)}" stroke-width="{w}" fill="{fill}"{da}{c_}{st(d, extra)}/>'


def sb(t):
    """SVG 下标（字母下标没有对应的 Unicode 字符时用，如 m_A）"""
    return f'<tspan class="sub" style="font-size:72%;baseline-shift:-22%">{t}</tspan>'


def text(x, y, s, d=None, size=None, c="k", anchor="start", weight=None, cls=""):
    a = []
    if size:
        a.append(f'font-size="{size}"')
    if weight:
        a.append(f'font-weight="{weight}"')
    k = " ".join(filter(None, ["fd" if d is not None else "", cls]))
    kk = f' class="{k}"' if k else ""
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" fill="{COL.get(c, c)}" {" ".join(a)}{kk}{st(d)}>{s}</text>')


def g(inner, d=None, cls="fd", extra=""):
    c = f' class="{cls}"' if (d is not None or cls not in ("fd",)) else ""
    return f"<g{c}{st(d, extra)}>{inner}</g>"


def svg(p, w, h, inner, attrs=""):
    return f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" role="img" {attrs}>{defs(p)}{inner}</svg>'


def fig(svg_html, caption, anim=True, style="", cls=""):
    a = " data-anim" if anim else ""
    s = f"<style>{style}</style>" if style else ""
    return f'<figure class="fig{cls}"{a}>{s}{svg_html}<figcaption>{caption}</figcaption></figure>'


def L(x1, y1, x2, y2):
    return math.hypot(x2 - x1, y2 - y1)


# ---------------------------------------------------------------- 物理 ----

def p01_vectors():
    p = "v1"
    O = (50, 175)
    E = (250, 175)
    N = (250, 25)
    s = [
        '<g stroke="#e5e7eb">' + "".join(f'<line x1="{x}" y1="15" x2="{x}" y2="185"/>' for x in range(50, 300, 50))
        + "".join(f'<line x1="40" y1="{y}" x2="290" y2="{y}"/>' for y in range(25, 186, 50)) + "</g>",
        text(14, 30, "N↑", c="s"),
        arrow(p, *O, *E, "b", 3, d=0.2),
        text(150, 196, "4 m 向东 (east)", d=0.2, c="b", anchor="middle"),
        arrow(p, *E, *N, "b", 3, d=1.0),
        text(258, 105, "3 m 向北", d=1.0, c="b"),
        text(258, 120, "(north)", d=1.0, c="b"),
        arrow(p, *O, *N, "r", 3.4, d=1.9),
        text(140, 72, "合位移 R = 5 m", d=1.9, c="r", weight=700, anchor="end"),
        path("M90 175 A40 40 0 0 0 82 151", "r", 1.6, d=2.4),
        text(96, 162, "θ", d=2.4, c="r", cls="m"),
        text(52, 214, "R² = 4² + 3²  →  R = 5 m；tan θ = 3/4 → θ = 36,87° N of E", d=2.6, size=11.5),
    ]
    # 分解：40 N @30°
    ox, oy, F = 340, 175, 150
    fx, fy = ox + F * math.cos(math.radians(30)), oy - F * math.sin(math.radians(30))
    s += [
        text(318, 26, "分解 Resolve：F = 40 N，30°", size=11.5, weight=700),
        arrow(p, ox, oy, fx, fy, "k", 3, d=3.0),
        text(392, 118, "F", d=3.0, cls="m", size=15),
        arrow(p, ox, oy, fx, oy, "g", 2.4, d=3.6, dash=True),
        text(400, 194, "Fx = F cos30° = 34,64 N", d=3.6, c="g", anchor="middle", size=11.5),
        arrow(p, fx, oy, fx, fy, "a", 2.4, d=4.2, dash=True),
        text(fx + 6, 132, "Fy = F sin30°", d=4.2, c="a", size=11.5),
        text(fx + 6, 146, "= 20,00 N", d=4.2, c="a", size=11.5),
        path(f"M{ox + 36} {oy} A36 36 0 0 0 {ox + 36 * math.cos(math.radians(30)):.1f} {oy - 18:.1f}", "k", 1.4),
        text(ox + 42, oy - 6, "30°", size=11),
    ]
    return fig(svg(p, 560, 222, "".join(s)),
               "左：首尾相接 (tip-to-tail) 求合矢量；右：把一个斜向的力分解成水平和竖直分量")


def p03_distance():
    p = "v3"
    pathd = "M40 175 L240 175 L240 25"
    s = [
        path(pathd, "s", 2, dash=True),
        text(40, 194, "A 起点", anchor="middle"), text(240, 194, "B", anchor="middle"), text(250, 22, "C 终点"),
        text(140, 168, "40 m 东", c="s", anchor="middle"), text(248, 105, "30 m 北", c="s"),
        f'<circle r="7" fill="#2563eb" class="mover" style="offset-path:path(\'{pathd}\')" cx="0" cy="0"/>',
        arrow(p, 40, 175, 240, 25, "r", 3, d=3.2),
        text(165, 122, "位移 = 50 m", d=3.2, c="r", weight=700, anchor="middle"),
        text(165, 138, "方位角 053,13°", d=3.2, c="r", anchor="middle"),
    ]
    s += [
        text(300, 40, "路程 distance（标量）", weight=700, c="b"),
        text(300, 58, "= 实际走过的路径长度 = 40 + 30 = 70 m"),
        text(300, 90, "位移 displacement（矢量）", weight=700, c="r"),
        text(300, 108, "= 从起点指向终点的直线 + 方向"),
        text(300, 126, "= √(40² + 30²) = 50 m"),
        text(300, 158, "用时 25 s：", weight=700),
        text(300, 176, "平均速率 = 70 ÷ 25 = 2,8 m·s⁻¹"),
        text(300, 194, "平均速度 = 50 ÷ 25 = 2,0 m·s⁻¹，53,13°"),
    ]
    css = (".fig .mover{offset-distance:100%}"
           ".fig.play .mover{animation:v3mv 3s linear both}"
           "@keyframes v3mv{from{offset-distance:0%}to{offset-distance:100%}}")
    return fig(svg(p, 540, 206, "".join(s)), "蓝点走过的总长度是路程；红色箭头（起点→终点）是位移", style=css)


def p05_chase():
    p = "v5"
    x0, sc = 40, 1.05  # 1 m = 1.05 px
    ts = [0, 4, 8, 12, 16, 20]
    goods = [20 * t for t in ts]
    expr = [t * t for t in ts]
    kf1 = "".join(f"{i * 20}%{{transform:translateX({x * sc:.1f}px)}}" for i, x in enumerate(goods))
    kf2 = "".join(f"{i * 20}%{{transform:translateX({x * sc:.1f}px)}}" for i, x in enumerate(expr))
    css = (f".fig.play .tg{{animation:v5g 5s linear both}}.fig.play .te{{animation:v5e 5s linear both}}"
           f"@keyframes v5g{{{kf1}}}@keyframes v5e{{{kf2}}}"
           f".fig .tg,.fig .te{{transform:translateX({400 * sc:.1f}px)}}")
    s = [
        f'<line x1="{x0}" y1="62" x2="{x0 + 430}" y2="62" stroke="#9ca3af" stroke-width="3"/>',
        f'<line x1="{x0}" y1="122" x2="{x0 + 430}" y2="122" stroke="#9ca3af" stroke-width="3"/>',
        "".join(text(x0 + m * sc, 145, f"{m} m", c="s", size=10, anchor="middle") for m in range(0, 401, 100)),
        f'<g class="tg"><rect x="{x0 - 30}" y="40" width="30" height="18" rx="3" fill="#2563eb"/></g>',
        f'<g class="te"><rect x="{x0 - 30}" y="100" width="30" height="18" rx="3" fill="#dc2626"/></g>',
        text(x0, 34, "货车 goods：匀速 20 m·s⁻¹，Δx = 20t", c="b", size=11.5),
        text(x0, 94, "快车 express：从静止出发 a = 2 m·s⁻²，Δx = ½(2)t² = t²", c="r", size=11.5),
        f'<line x1="{x0 + 400 * sc}" y1="30" x2="{x0 + 400 * sc}" y2="130" stroke="#7c3aed" stroke-dasharray="4 3"/>',
        text(x0 + 400 * sc - 4, 170, "相遇：位移相等 20t = t² → t = 20 s，Δx = 400 m", c="p", anchor="end", weight=700),
        text(x0, 192, "追及题套路：两车同起点 → 分别写出 Δx 的表达式 → 令两者相等 → 解 t", size=11.5),
    ]
    return fig(svg(p, 520, 200, "".join(s)), "动画把 20 s 压缩成 5 s：开始时货车领先，快车越跑越快，最终追上", style=css)


def p07_graphs():
    p = "v7"
    # motion: 0-4 a=2, 4-8 v=8, 8-10 a=-4
    def x_of(t):
        if t <= 4:
            return t * t
        if t <= 8:
            return 16 + 8 * (t - 4)
        u = t - 8
        return 48 + 8 * u - 2 * u * u

    def v_of(t):
        return 2 * t if t <= 4 else (8 if t <= 8 else 8 - 4 * (t - 8))

    panels = []
    W, H = 140, 120
    bases = [(30, 20), (205, 20), (380, 20)]
    names = [("x-t 位置-时间", "斜率 = 速度"), ("v-t 速度-时间", "斜率 = 加速度，面积 = 位移"), ("a-t 加速度-时间", "面积 = 速度变化")]
    for (bx, by), (n1, n2) in zip(bases, names):
        panels.append(f'<line x1="{bx}" y1="{by}" x2="{bx}" y2="{by + H}" stroke="#1f2937" stroke-width="1.4"/>')
        panels.append(text(bx + 4, by + 8, n1, size=11, weight=700))
        panels.append(text(bx + W / 2, by + H + 42, n2, size=10.5, c="r", anchor="middle"))
        panels.append(text(bx + W, by + H + 26, "t (s)", size=10, c="s", anchor="end"))
    # x-t
    bx, by = bases[0]
    y0 = by + H
    pts = " ".join(f"{bx + t * W / 10:.1f},{y0 - x_of(t) * (H - 14) / 56:.1f}" for t in [i / 4 for i in range(41)])
    panels.append(f'<line x1="{bx}" y1="{y0}" x2="{bx + W}" y2="{y0}" stroke="#1f2937" stroke-width="1.4"/>')
    panels.append(f'<polyline points="{pts}" fill="none" stroke="#2563eb" stroke-width="2.4"/>')
    # v-t
    bx, by = bases[1]
    y0 = by + H
    vs = lambda v: y0 - v * (H - 20) / 8
    panels.append(f'<line x1="{bx}" y1="{y0}" x2="{bx + W}" y2="{y0}" stroke="#1f2937" stroke-width="1.4"/>')
    poly = f"{bx},{y0} {bx + 4 * W / 10},{vs(8)} {bx + 8 * W / 10},{vs(8)} {bx + W},{y0}"
    panels.append(f'<polygon points="{poly}" fill="#bfdbfe" opacity=".7"/>')
    panels.append(f'<polyline points="{poly}" fill="none" stroke="#2563eb" stroke-width="2.4"/>')
    panels.append(text(bx + W / 2, vs(3), "面积 = 56 m", c="b", size=11, anchor="middle"))
    # a-t
    bx, by = bases[2]
    mid = by + H / 2 + 6
    as_ = lambda a: mid - a * 11
    panels.append(f'<line x1="{bx}" y1="{mid}" x2="{bx + W}" y2="{mid}" stroke="#1f2937" stroke-width="1.4"/>')
    panels.append(f'<polyline points="{bx},{as_(2)} {bx + 4 * W / 10},{as_(2)} {bx + 4 * W / 10},{mid} {bx + 8 * W / 10},{mid} '
                  f'{bx + 8 * W / 10},{as_(-4)} {bx + W},{as_(-4)}" fill="none" stroke="#2563eb" stroke-width="2.4"/>')
    panels.append(text(bx + 4, as_(2) - 4, "+2", size=10, c="b"))
    panels.append(text(bx + W - 4, as_(-4) + 14, "−4", size=10, c="b", anchor="end"))
    # cursor
    cur = "".join(f'<line x1="{bx}" y1="{by}" x2="{bx}" y2="{by + H}" stroke="#dc2626" stroke-width="1.6"/>' for bx, by in bases)
    panels.append(f'<g class="cur">{cur}</g>')
    panels.append(text(30, 196, "0–4 s 加速 → 4–8 s 匀速 → 8–10 s 减速到停", size=11.5, weight=700))
    css = (f".fig .cur{{opacity:0}}.fig.play .cur{{animation:v7c 6s linear both}}"
           f"@keyframes v7c{{0%{{opacity:1;transform:translateX(0)}}95%{{opacity:1}}100%{{opacity:0;transform:translateX({W}px)}}}}")
    return fig(svg(p, 540, 205, "".join(panels)), "同一个运动的三张图：红线是“时间光标”，三张图同一时刻一一对应", style=css)


def ex07_vt():
    p = "e7"
    ox, oy, sx, sy = 50, 110, 16, 7
    s = ['<g stroke="#e5e7eb">' + "".join(f'<line x1="{ox + t * sx}" y1="{oy - 12 * sy}" x2="{ox + t * sx}" y2="{oy + 7 * sy}"/>' for t in range(0, 26, 5))
         + "".join(f'<line x1="{ox}" y1="{oy - v * sy}" x2="{ox + 25 * sx}" y2="{oy - v * sy}"/>' for v in range(-5, 11, 5)) + "</g>",
         f'<line x1="{ox}" y1="{oy}" x2="{ox + 26 * sx}" y2="{oy}" stroke="#1f2937" stroke-width="1.5"/>',
         f'<line x1="{ox}" y1="{oy - 13 * sy}" x2="{ox}" y2="{oy + 8 * sy}" stroke="#1f2937" stroke-width="1.5"/>']
    pts = [(0, 0), (5, 10), (15, 10), (20, 0), (25, -5)]
    s.append(f'<polyline points="{" ".join(f"{ox + t * sx},{oy - v * sy}" for t, v in pts)}" fill="none" stroke="#2563eb" stroke-width="2.6"/>')
    s += [text(ox + t * sx, oy + 14 if t else oy + 14, str(t), size=10, anchor="middle") for t in range(5, 26, 5)]
    s += [text(ox - 5, oy - v * sy + 4, str(v), size=10, anchor="end") for v in (-5, 5, 10)]
    s += [text(ox + 26 * sx, oy - 4, "t (s)", size=10, anchor="end"), text(ox + 4, oy - 12 * sy - 2, "v (m·s⁻¹)，取向北为正", size=10)]
    return fig(svg(p, 480, 170, "".join(s)), "练习用图：一辆车的 v-t 图（向北为正）", anim=False, cls=" ex")


def p09_fbd():
    p = "v9"
    bx, by, bw, bh = 170, 100, 90, 56
    cx, cy = bx + bw / 2, by + bh / 2
    ang = math.radians(30)
    fx, fy = cx + 120 * math.cos(ang), cy - 120 * math.sin(ang)
    s = [
        f'<line x1="30" y1="{by + bh}" x2="430" y2="{by + bh}" stroke="#1f2937" stroke-width="2"/>',
        "".join(f'<line x1="{x}" y1="{by + bh}" x2="{x - 10}" y2="{by + bh + 10}" stroke="#9ca3af"/>' for x in range(40, 431, 16)),
        f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" fill="#f3f4f6" stroke="#1f2937" stroke-width="2"/>',
        text(cx, cy + 5, "m", anchor="middle", cls="m", size=16),
        arrow(p, cx, cy, cx, cy + 95, "k", 2.6, d=0.2), text(cx + 6, cy + 92, "w = mg 重力", d=0.2),
        arrow(p, cx, cy, cx, cy - 85, "b", 2.6, d=0.9), text(cx + 6, cy - 72, "N 法向力", d=0.9, c="b"),
        arrow(p, cx, cy, fx, fy, "g", 2.6, d=1.6), text(fx + 4, fy + 4, "F 拉力", d=1.6, c="g"),
        arrow(p, cx, cy, cx - 95, cy, "r", 2.6, d=2.3), text(cx - 98, cy - 6, "f 摩擦力", d=2.3, c="r", anchor="end"),
        arrow(p, cx, cy, fx, cy, "g", 1.6, d=3.0, dash=True), text(fx + 4, cy + 14, "F cosθ", d=3.0, c="g", cls="m"),
        arrow(p, fx, cy, fx, fy, "g", 1.6, d=3.0, dash=True), text(fx + 6, (cy + fy) / 2, "F sinθ", d=3.0, c="g", cls="m"),
        text(cx + 36, cy - 4, "θ", cls="m", c="g"),
        text(30, 20, "竖直方向（不动）：N + F sinθ = mg → N = mg − F sinθ", d=3.6, size=11.5, weight=700),
        text(30, 38, f"水平方向：F{sb('net')} = F cosθ − f = ma，其中 f = μ{sb('k')}N", d=3.6, size=11.5, weight=700),
    ]
    return fig(svg(p, 520, 260, "".join(s)), "受力图 free-body diagram：所有箭头从物体中心画出；斜拉时 N 不等于 mg")


def p11_incline():
    p = "v11"
    th = math.radians(30)
    A, Bx, H = (40, 200), 340, 300 * math.tan(th)
    top = (Bx, 200 - H)
    P = (40 + 0.55 * 300, 200 - 0.55 * H)
    n = (-math.sin(th), -math.cos(th))
    C = (P[0] + 20 * n[0], P[1] + 20 * n[1])
    W = 100
    down = (-math.cos(th), math.sin(th))
    into = (math.sin(th), math.cos(th))
    wpar = (C[0] + W * math.sin(th) * down[0], C[1] + W * math.sin(th) * down[1])
    wper = (C[0] + W * math.cos(th) * into[0], C[1] + W * math.cos(th) * into[1])
    Nend = (C[0] - W * math.cos(th) * into[0], C[1] - W * math.cos(th) * into[1])
    fend = (C[0] - W * math.sin(th) * down[0], C[1] - W * math.sin(th) * down[1])
    s = [
        f'<polygon points="{A[0]},{A[1]} {Bx},{A[1]} {top[0]},{top[1]:.1f}" fill="#f3f4f6" stroke="#1f2937" stroke-width="2"/>',
        f'<rect x="{C[0] - 26:.1f}" y="{C[1] - 18:.1f}" width="52" height="36" fill="#fde68a" stroke="#1f2937" stroke-width="1.8" transform="rotate(-30 {C[0]:.1f} {C[1]:.1f})"/>',
        path(f"M{A[0] + 50} {A[1]} A50 50 0 0 0 {A[0] + 50 * math.cos(th):.1f} {A[1] - 50 * math.sin(th):.1f}", "k", 1.4),
        text(A[0] + 56, A[1] - 8, "θ", cls="m"),
        arrow(p, *C, C[0], C[1] + W, "k", 2.8, d=0.2), text(C[0] + 5, C[1] + W + 4, "w = mg", d=0.2, cls="m"),
        arrow(p, *C, *wpar, "a", 2.4, d=1.0, dash=True), text(wpar[0] - 4, wpar[1] + 16, "w∥ = mg sinθ", d=1.0, c="a", anchor="end", size=11.5),
        arrow(p, *C, *wper, "g", 2.4, d=1.6, dash=True), text(wper[0] + 8, wper[1] + 4, "w⊥ = mg cosθ", d=1.6, c="g", size=11.5),
        arrow(p, *C, *Nend, "b", 2.6, d=2.3), text(Nend[0] - 4, Nend[1] - 4, "N = mg cosθ", d=2.3, c="b", anchor="end", size=11.5),
        arrow(p, *C, *fend, "r", 2.6, d=2.9), text(fend[0] + 4, fend[1] - 6, "f（静止时 = mg sinθ）", d=2.9, c="r", size=11.5),
    ]
    s += [text(370, 40, "解斜面题三步：", weight=700), text(370, 60, "① 沿斜面、垂直斜面建坐标"),
          text(370, 80, "② 把重力分解成 w∥ 和 w⊥"), text(370, 100, "③ 两个方向分别列方程"),
          text(370, 130, "θ 变大：w∥ 变大，N 变小", c="r", weight=700),
          text(370, 150, "检查：θ = 0 时 w∥ = 0，N = mg ✓", c="s", size=11.5)]
    return fig(svg(p, 560, 225, "".join(s)), "斜面 inclined plane：重力不变，只是被“拆”成两个方向的分量")


def p13_connected():
    p = "v13"
    css = (".fig.play .ma{animation:v13a 2.4s ease-in .4s both}.fig.play .mb{animation:v13b 2.4s ease-in .4s both}"
           "@keyframes v13a{from{transform:translateX(0)}to{transform:translateX(44px)}}"
           "@keyframes v13b{from{transform:translateY(0)}to{transform:translateY(44px)}}")
    tx, ty = 330, 90  # pulley
    s = [
        f'<rect x="20" y="{ty + 12}" width="{tx - 8}" height="14" fill="#d1d5db" stroke="#1f2937"/>',
        f'<line x1="{tx - 120}" y1="{ty - 1}" x2="{tx}" y2="{ty - 1}" stroke="#6b7280" stroke-width="2"/>',
        f'<line x1="{tx + 13}" y1="{ty + 8}" x2="{tx + 13}" y2="{ty + 112}" stroke="#6b7280" stroke-width="2"/>',
        f'<circle cx="{tx}" cy="{ty + 8}" r="13" fill="#fff" stroke="#1f2937" stroke-width="2"/>',
        f'<g class="ma"><rect x="110" y="{ty - 28}" width="90" height="40" fill="#bfdbfe" stroke="#1f2937" stroke-width="2"/>'
        f'{text(155, ty - 3, "A 4 kg", anchor="middle", weight=700)}'
        f'{arrow(p, 200, ty - 8, 250, ty - 8, "g", 2.4)}{text(222, ty - 14, "T", c="g", cls="m")}'
        f'{arrow(p, 110, ty - 8, 66, ty - 8, "r", 2.4)}{text(70, ty - 14, "f", c="r", cls="m")}</g>',
        f'<g class="mb"><rect x="{tx - 10}" y="{ty + 70}" width="46" height="50" fill="#fecaca" stroke="#1f2937" stroke-width="2"/>'
        f'{text(tx + 13, ty + 100, "B 2 kg", anchor="middle", size=11, weight=700)}'
        f'{arrow(p, tx + 13, ty + 70, tx + 13, ty + 34, "g", 2.4)}{text(tx + 20, ty + 52, "T", c="g", cls="m")}'
        f'{arrow(p, tx + 13, ty + 120, tx + 13, ty + 160, "k", 2.4)}{text(tx + 20, ty + 158, "w = m" + sb("B") + "g", size=11)}</g>',
    ]
    s += [text(400, 30, "连接体 connected bodies", weight=700),
          text(400, 50, "同一根轻绳：两边张力 T 相同"), text(400, 68, "两块一起动：加速度 a 相同"),
          text(400, 96, f"A：T − f = m{sb('A')}a", c="b"), text(400, 114, f"B：m{sb('B')}g − T = m{sb('B')}a", c="r"),
          text(400, 132, "两式相加消去 T："), text(400, 150, f"m{sb('B')}g − f = (m{sb('A')} + m{sb('B')})a", weight=700)]
    return fig(svg(p, 580, 270, "".join(s)), "B 向下拉，A 向右滑；分别给每个物体画受力图、各列一个方程", style=css)


def p15_gravity():
    p = "v15"
    s = [f'<circle cx="60" cy="100" r="42" fill="#93c5fd" stroke="#1e40af" stroke-width="2"/>',
         text(60, 105, "地球 M", anchor="middle", weight=700)]
    for i, (r, lab, ln) in enumerate([(1, "F", 80), (2, "F/4", 24), (3, "F/9", 14)]):
        x = 60 + 130 * r
        d = 0.4 + i * 1.0
        s += [g(f'<circle cx="{x}" cy="100" r="11" fill="#fde68a" stroke="#1f2937" stroke-width="1.6"/>'
                + arrow(p, x - 12, 100, x - 12 - ln, 100, "r", 3)
                + text(x - 12 - ln / 2, 88, lab, c="r", anchor="middle", weight=700)
                + text(x, 135, f"距离 {r}r" if r > 1 else "距离 r", anchor="middle"), d=d)]
    s += [path("M60 160 L190 160", "s", 1.2), text(125, 175, "r 从球心量起", c="s", size=10.5, anchor="middle"),
          text(20, 196, "F = Gm₁m₂/r²：距离 ×2 → 力 ×1/4；距离 ×3 → 力 ×1/9", size=11.5, weight=700, d=3.4), text(20, 212, "这叫平方反比关系 inverse square law", size=11, c="s", d=3.4)]
    return fig(svg(p, 560, 220, "".join(s)), "同一颗卫星离地球越远，受到的引力按距离的平方减小")


def p17_contact():
    p = "v17"
    css = (".fig .el{opacity:0}.fig.play .el{animation:v17e 1.6s ease-in-out both;animation-delay:var(--d)}"
           "@keyframes v17e{0%{opacity:1;transform:translateX(0)}100%{opacity:1;transform:translateX(-46px)}}")

    def sph(x, q, col):
        return (f'<line x1="{x}" y1="112" x2="{x}" y2="160" stroke="#6b7280" stroke-width="5"/>'
                f'<circle cx="{x}" cy="90" r="24" fill="{col}" stroke="#1f2937" stroke-width="1.8"/>' + text(x, 95, q, anchor="middle", weight=700, size=12))
    s = [text(70, 24, "① 接触前", anchor="middle", weight=700), sph(40, "+6 nC", "#fecaca"), sph(110, "−2 nC", "#bfdbfe"),
         text(255, 24, "② 接触：电子从 B 流向 A", anchor="middle", weight=700), sph(232, "A", "#e9d5ff"), sph(280, "B", "#e9d5ff")]
    s += [f'<circle class="el" cx="{272 + (i % 2) * 6}" cy="{80 + i * 5}" r="3" fill="#2563eb" style="--d:{0.4 + i * 0.25}s"/>' for i in range(5)]
    s += [text(440, 24, "③ 分开后：平均分配", anchor="middle", weight=700), sph(410, "+2 nC", "#fecaca"), sph(480, "+2 nC", "#fecaca"),
          text(20, 190, "Q = (Q₁ + Q₂)/2 = (+6 − 2)/2 = +2 nC；A 的电荷从 +6 变成 +2，得到了 4 nC 的电子", size=11.5, d=2.2),
          text(20, 208, "电子数 n = ΔQ / e = 4×10⁻⁹ ÷ 1,6×10⁻¹⁹ = 2,5×10¹⁰ 个（只有电子会移动，质子不动）", size=11.5, d=2.6)]
    return fig(svg(p, 540, 218, "".join(s)), "两个相同的导体球接触后电荷平分；电荷守恒：总电荷前后都是 +4 nC", style=css)


def p19_field():
    p = "v19"
    s = []

    def radial(cx, cy, out, col, d):
        o = ""
        for k in range(8):
            a = k * math.pi / 4
            x1, y1 = cx + 18 * math.cos(a), cy + 18 * math.sin(a)
            x2, y2 = cx + 62 * math.cos(a), cy + 62 * math.sin(a)
            o += arrow(p, x1, y1, x2, y2, col, 1.8) if out else arrow(p, x2, y2, x1, y1, col, 1.8)
        return g(o, d=d)
    s += [radial(80, 95, True, "r", 0.2), f'<circle cx="80" cy="95" r="14" fill="#fecaca" stroke="#1f2937"/>', text(80, 100, "+", anchor="middle", size=16, weight=700),
          text(80, 185, "正电荷：向外", anchor="middle", c="r"),
          radial(220, 95, False, "b", 0.9), f'<circle cx="220" cy="95" r="14" fill="#bfdbfe" stroke="#1f2937"/>', text(220, 100, "−", anchor="middle", size=16, weight=700),
          text(220, 185, "负电荷：向内", anchor="middle", c="b")]
    # dipole
    A, B = (340, 95), (480, 95)
    lines = ""
    for hgt in (-70, -40, -18, 18, 40, 70):
        lines += f'<path d="M{A[0] + 14} {A[1]} C{A[0] + 40} {A[1] + hgt * 1.4} {B[0] - 40} {B[1] + hgt * 1.4} {B[0] - 14} {B[1]}" fill="none" stroke="#7c3aed" stroke-width="1.6"/>'
    lines += arrow(p, A[0] + 14, A[1], B[0] - 16, B[1], "p", 1.6)
    for hgt in (-70, -40, 40, 70):
        mx = (A[0] + B[0]) / 2
        lines += arrow(p, mx - 6, A[1] + hgt * 1.05, mx + 6, A[1] + hgt * 1.05, "p", 1.6)
    s += [g(lines, d=1.6), f'<circle cx="{A[0]}" cy="{A[1]}" r="14" fill="#fecaca" stroke="#1f2937"/>', text(A[0], A[1] + 5, "+", anchor="middle", size=16, weight=700),
          f'<circle cx="{B[0]}" cy="{B[1]}" r="14" fill="#bfdbfe" stroke="#1f2937"/>', text(B[0], B[1] + 5, "−", anchor="middle", size=16, weight=700),
          text(410, 185, "一正一负：从 + 出发，到 − 结束", anchor="middle", c="p")]
    s += [text(20, 206, "规则：方向 = 正试探电荷的受力方向；线不相交；线越密，电场越强", size=11.3, weight=700), text(20, 222, "E = kQ/r²：距离加倍 → E 变为 1/4", size=11.3, c="s")]
    return fig(svg(p, 540, 228, "".join(s)), "电场线 electric field lines")


def p21_series_parallel():
    p = "v21"

    def battery(x, y):
        return (f'<line x1="{x - 6}" y1="{y - 14}" x2="{x - 6}" y2="{y + 14}" stroke="#1f2937" stroke-width="2.4"/>'
                f'<line x1="{x + 6}" y1="{y - 8}" x2="{x + 6}" y2="{y + 8}" stroke="#1f2937" stroke-width="4"/>')

    def res(x, y, lab, vert=False):
        if vert:
            return f'<rect x="{x - 9}" y="{y - 22}" width="18" height="44" fill="#fff" stroke="#1f2937" stroke-width="2"/>' + text(x + 14, y + 4, lab, size=11)
        return f'<rect x="{x - 22}" y="{y - 9}" width="44" height="18" fill="#fff" stroke="#1f2937" stroke-width="2"/>' + text(x, y - 13, lab, size=11, anchor="middle")
    w = 'stroke="#2563eb" stroke-width="2.6" fill="none" class="flow"'
    base = 'stroke="#1f2937" stroke-width="2" fill="none"'
    s = [f'<path d="M40 40 H220 V150 H40 Z" {base}/>', f'<path d="M40 40 H220 V150 H40 Z" {w}/>',
         battery(130, 150), res(95, 40, "R₁"), res(175, 40, "R₂"),
         text(130, 182, "串联 series", anchor="middle", weight=700),
         text(130, 200, "I 处处相同；V = V₁ + V₂", anchor="middle", size=11.3),
         text(130, 216, "R = R₁ + R₂（越串越大）", anchor="middle", size=11.3)]
    s += [f'<path d="M300 40 H500 V150 H300 Z" {base}/>', f'<path d="M420 40 V150" {base}/>',
          f'<path d="M300 150 V40 H500 V150 H300" {w}/>', f'<path d="M420 40 V150" {w}/>',
          battery(360, 150), res(420, 95, "R₁", True), res(500, 95, "R₂", True),
          text(400, 182, "并联 parallel", anchor="middle", weight=700),
          text(400, 200, "V 各支路相同；I = I₁ + I₂", anchor="middle", size=11.3),
          text(400, 216, "1/R = 1/R₁ + 1/R₂（越并越小）", anchor="middle", size=11.3)]
    return fig(svg(p, 540, 224, "".join(s)), "屏幕上蓝色虚线的流动表示电流（打印版为静态）", anim=False)


def ex21_circuit():
    p = "e21"
    base = 'stroke="#1f2937" stroke-width="2.4" fill="none"'
    s = [f'<path d="M114 140 H30 V30 H330 V140 H126" {base}/>', f'<path d="M220 30 V140" {base}/>',
         '<line x1="114" y1="124" x2="114" y2="156" stroke="#1f2937" stroke-width="2.6"/>',
         '<line x1="126" y1="131" x2="126" y2="149" stroke="#1f2937" stroke-width="5"/>',
         text(120, 178, "12 V（内阻不计）", anchor="middle", size=15),
         '<rect x="94" y="20" width="52" height="20" fill="#fff" stroke="#1f2937" stroke-width="2.4"/>', text(120, 14, "4 Ω", anchor="middle", size=16),
         '<rect x="210" y="60" width="20" height="50" fill="#fff" stroke="#1f2937" stroke-width="2.4"/>', text(238, 91, "6 Ω", size=16),
         '<rect x="320" y="60" width="20" height="50" fill="#fff" stroke="#1f2937" stroke-width="2.4"/>', text(348, 91, "12 Ω", size=16)]
    return fig(svg(p, 400, 186, "".join(s)), "第 21.3 题电路图", anim=False, cls=" ex sm")


def p23_emf():
    p = "v23"
    s = [f'<rect x="30" y="40" width="190" height="90" rx="8" fill="#f9fafb" stroke="#6b7280" stroke-dasharray="5 4"/>',
         text(125, 32, "电池内部 = 理想电源 + 内阻 r", anchor="middle", size=11.5, weight=700),
         '<line x1="70" y1="70" x2="70" y2="100" stroke="#1f2937" stroke-width="2.4"/><line x1="82" y1="77" x2="82" y2="93" stroke="#1f2937" stroke-width="4"/>',
         text(76, 120, "emf ε", anchor="middle", cls="m"),
         '<path d="M30 85 H70 M82 85 H140" stroke="#1f2937" stroke-width="2"/>',
         '<rect x="140" y="76" width="44" height="18" fill="#fff" stroke="#1f2937" stroke-width="2"/>', text(162, 120, "内阻 r", anchor="middle"),
         '<path d="M184 85 H220" stroke="#1f2937" stroke-width="2"/>',
         text(125, 158, "端电压 V = ε − Ir", anchor="middle", weight=700, c="b"),
         text(125, 176, "Ir 叫 lost volts（内阻上“损失”的电压）", anchor="middle", size=11.3),
         text(125, 194, "ε = I(R + r)", anchor="middle", weight=700)]
    ox, oy, W, H = 290, 175, 220, 140
    emf, r = 6.0, 1.5
    vs = lambda v: oy - v / emf * (H - 10)
    is_ = lambda i: ox + i / 4 * W
    s += [f'<line x1="{ox}" y1="{oy}" x2="{ox + W + 10}" y2="{oy}" stroke="#1f2937" stroke-width="1.5"/>',
          f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy - H - 8}" stroke="#1f2937" stroke-width="1.5"/>',
          text(ox + W + 8, oy + 16, "I (A)", size=10.5, anchor="end"), text(ox + 4, oy - H - 10, "V (V)", size=10.5),
          f'<line x1="{ox}" y1="{vs(emf)}" x2="{is_(4)}" y2="{vs(emf - 4 * r)}" stroke="#2563eb" stroke-width="2.6"/>',
          text(ox - 4, vs(emf) + 4, "ε", anchor="end", cls="m", c="r", size=15),
          text(ox + 30, vs(emf) - 8, "y 截距 = emf（I = 0 时）", c="r", size=11),
          text(is_(2.2), vs(emf - 2.2 * r) - 14, "斜率 = −r", c="r", size=11.5, weight=700),
          f'<circle class="dot" cx="{is_(0.5)}" cy="{vs(emf - 0.5 * r)}" r="6" fill="#dc2626"/>']
    css = (f".fig.play .dot{{animation:v23d 4s ease-in-out both}}"
           f"@keyframes v23d{{from{{transform:translate(0,0)}}to{{transform:translate({is_(3.5) - is_(0.5):.1f}px,{vs(emf - 3.5 * r) - vs(emf - 0.5 * r):.1f}px)}}}}")
    s += [text(ox - 20, oy + 32, "R 变小 → I 变大 → Ir 变大 → V 下降", size=11, c="s")]
    return fig(svg(p, 540, 215, "".join(s)), "左：电池模型；右：V-I 图（红点随电流增大沿直线下滑）", style=css)


# ---------------------------------------------------------------- 化学 ----

def dots(x, y, n, col="#1f2937", r=2.6, gap=7, vert=False):
    out = ""
    for i in range(n):
        dx, dy = (0, (i - (n - 1) / 2) * gap) if vert else ((i - (n - 1) / 2) * gap, 0)
        out += f'<circle cx="{x + dx}" cy="{y + dy}" r="{r}" fill="{col}"/>'
    return out


def cross(x, y, col="#dc2626", s=3):
    return f'<path d="M{x - s} {y - s}L{x + s} {y + s}M{x + s} {y - s}L{x - s} {y + s}" stroke="{col}" stroke-width="1.6"/>'


def c02_dative():
    p = "c2"

    def nh3(cx, cy):
        # N 在中心；左右下三个 H，各共用一对电子（● 来自 N，× 来自 H）；上方一对孤对电子
        o = text(cx, cy + 8, "N", anchor="middle", size=22, weight=700)
        o += text(cx - 50, cy + 7, "H", anchor="middle", size=18) + dots(cx - 24, cy - 4, 1) + cross(cx - 24, cy + 6)
        o += text(cx + 50, cy + 7, "H", anchor="middle", size=18) + dots(cx + 24, cy - 4, 1) + cross(cx + 24, cy + 6)
        o += text(cx, cy + 56, "H", anchor="middle", size=18) + dots(cx - 5, cy + 26, 1) + cross(cx + 5, cy + 26)
        o += dots(cx, cy - 20, 2, col="#2563eb", r=3.2)
        return o
    s = [text(20, 22, "● N 的电子   × H 的电子   蓝色 ●● = N 的孤对电子", size=11, c="s"),
         nh3(90, 100), text(170, 105, "+", anchor="middle", size=22),
         text(210, 108, "H⁺", anchor="middle", size=22, weight=700, c="r"),
         text(210, 130, "（没有电子）", anchor="middle", size=10.5, c="s"),
         arrow(p, 250, 100, 300, 100, "k", 2.4), nh3(390, 110),
         f'<g class="hin">{text(390, 66, "H", anchor="middle", size=18, c="r", weight=700)}</g>',
         f'<ellipse cx="390" cy="88" rx="18" ry="10" fill="none" stroke="#2563eb" stroke-width="1.6" stroke-dasharray="3 3" class="fd" style="--d:1.6s"/>',
         '<path d="M338 48 H330 V178 H338 M442 48 H450 V178 H442" fill="none" stroke="#6b7280" stroke-width="2"/>', text(456, 56, "+", size=20, c="s", weight=700),
         text(270, 196, "N 上的孤对电子 (lone pair) 两个电子都给了 H⁺ → 配位键 dative covalent bond → NH₄⁺", size=11.5, weight=700, anchor="middle", d=2.0)]
    css = ".fig.play .hin{animation:c2h 1.4s ease-out .2s both}@keyframes c2h{from{transform:translate(-180px,40px);opacity:.3}to{transform:translate(0,0);opacity:1}}"
    return fig(svg(p, 540, 206, "".join(s)), "铵根离子 NH₄⁺ 的形成：H⁺ 被 NH₃ 的孤对电子“抓住”", style=css)


def c04_vsepr():
    p = "c4"
    s = []
    items = [
        ("直线形 linear", "2 键 0 孤对", "180°", "CO₂ BeCl₂"),
        ("平面三角形 trigonal planar", "3 键 0 孤对", "120°", "BF₃"),
        ("正四面体 tetrahedral", "4 键 0 孤对", "109,5°", "CH₄"),
        ("三角锥 trigonal pyramidal", "3 键 1 孤对", "≈107°", "NH₃"),
        ("V 形 bent/angular", "2 键 2 孤对", "≈104,5°", "H₂O"),
        ("八面体 octahedral", "6 键 0 孤对", "90°", "SF₆"),
    ]
    for i, (n, bp, ang, eg) in enumerate(items):
        cx, cy = 80 + (i % 3) * 185, 52 + (i // 3) * 128
        o = f'<circle cx="{cx}" cy="{cy}" r="9" fill="#1f2937"/>'

        def b(dx, dy, kind="n"):
            if kind == "w":
                return f'<polygon points="{cx},{cy} {cx + dx - dy * .12:.1f},{cy + dy + dx * .12:.1f} {cx + dx + dy * .12:.1f},{cy + dy - dx * .12:.1f}" fill="#1f2937"/>' + f'<circle cx="{cx + dx}" cy="{cy + dy}" r="7" fill="#fca5a5" stroke="#1f2937"/>'
            if kind == "h":
                return f'<line x1="{cx}" y1="{cy}" x2="{cx + dx}" y2="{cy + dy}" stroke="#1f2937" stroke-width="2" stroke-dasharray="3 3"/>' + f'<circle cx="{cx + dx}" cy="{cy + dy}" r="7" fill="#fca5a5" stroke="#1f2937"/>'
            return f'<line x1="{cx}" y1="{cy}" x2="{cx + dx}" y2="{cy + dy}" stroke="#1f2937" stroke-width="2.4"/>' + f'<circle cx="{cx + dx}" cy="{cy + dy}" r="7" fill="#fca5a5" stroke="#1f2937"/>'

        def lp(dx, dy):
            return f'<ellipse cx="{cx + dx}" cy="{cy + dy}" rx="7" ry="11" fill="#bfdbfe" stroke="#2563eb" transform="rotate({math.degrees(math.atan2(dy, dx)) + 90:.0f} {cx + dx} {cy + dy})"/>' + dots(cx + dx, cy + dy, 2, "#2563eb", 2, 6, vert=False)
        if i == 0:
            o = b(-40, 0) + b(40, 0) + o
        elif i == 1:
            o = b(0, -36) + b(-34, 20) + b(34, 20) + o
        elif i == 2:
            o = b(0, -38) + b(-36, 14) + b(30, 24, "w") + b(34, 8, "h") + o
        elif i == 3:
            o = lp(0, -24) + b(-34, 18) + b(30, 26, "w") + b(34, 10, "h") + o
        elif i == 4:
            o = lp(-14, -22) + lp(14, -22) + b(-32, 22) + b(32, 22) + o
        else:
            o = b(0, -38) + b(0, 38) + b(-40, 0) + b(40, 0) + b(24, -18, "h") + b(-24, 18, "w") + o
        o += text(cx, cy + 50, n, anchor="middle", size=11, weight=700)
        o += text(cx, cy + 64, f"{bp} · {ang} · {eg}", anchor="middle", size=10.3, c="s")
        s.append(g(o, d=0.2 + i * 0.5))
    return fig(svg(p, 560, 256, "".join(s)), "VSEPR：中心原子周围的电子对互相排斥、尽量远离；孤对电子（蓝）排斥更强，把键角“压小”")


def c06_imf():
    p = "c6"
    css = (".fig.play .fl{animation:c6f 1.2s ease-in-out 0s 4 alternate both}"
           "@keyframes c6f{from{transform:translateX(-10px)}to{transform:translateX(10px)}}")
    s = []
    # London
    s.append(text(70, 20, "① London 力", anchor="middle", size=11.5, weight=700))
    for cx in (42, 100):
        s.append(f'<ellipse cx="{cx}" cy="75" rx="24" ry="16" fill="#e5e7eb" stroke="#1f2937"/>')
        s.append(f'<g class="fl"><ellipse cx="{cx - 6}" cy="75" rx="12" ry="10" fill="#93c5fd" opacity=".8"/></g>')
        s.append(text(cx - 18, 60, "δ−", size=10, c="b") + text(cx + 12, 60, "δ+", size=10, c="r"))
    s.append(text(70, 112, "所有分子都有", anchor="middle", size=10.5, c="s") + text(70, 126, "瞬时偶极", anchor="middle", size=10.5, c="s"))
    # dipole-dipole
    s.append(text(205, 20, "② 偶极-偶极", anchor="middle", size=11.5, weight=700))
    for i, y in enumerate((55, 95)):
        s.append(text(170, y, "δ+H", size=13, c="r") + text(205, y, "—", size=13) + text(222, y, "Clδ−", size=13, c="b"))
    s.append(f'<line x1="232" y1="60" x2="182" y2="82" stroke="#7c3aed" stroke-width="1.8" stroke-dasharray="3 3" class="fd" style="--d:.6s"/>')
    s.append(text(205, 122, "极性分子之间", anchor="middle", size=10.5, c="s") + text(205, 136, "δ+ 吸引 δ−", anchor="middle", size=10.5, c="s"))
    # H-bond
    s.append(text(355, 20, "③ 氢键", anchor="middle", size=11.5, weight=700))
    s.append(text(320, 60, "H—O", size=14) + text(334, 78, "|", size=12) + text(330, 94, "H", size=14))
    s.append(text(380, 92, "O—H", size=14) + text(384, 110, "|", size=12) + text(380, 126, "H", size=14))
    s.append(f'<line x1="342" y1="92" x2="380" y2="88" stroke="#dc2626" stroke-width="2.4" stroke-dasharray="4 3" class="fd" style="--d:1.0s"/>')
    s.append(text(355, 146, "H 连在 N/O/F 上", anchor="middle", size=10.5, c="s") + text(355, 160, "吸引另一分子的孤对电子", anchor="middle", size=10.5, c="s"))
    # ion-dipole
    s.append(text(495, 20, "④ 离子-偶极", anchor="middle", size=11.5, weight=700))
    s.append(f'<circle cx="495" cy="80" r="14" fill="#fde68a" stroke="#1f2937"/>' + text(495, 85, "Na⁺", anchor="middle", size=11, weight=700))
    for k in range(4):
        a = k * math.pi / 2 + math.pi / 4
        x, y = 495 + 40 * math.cos(a), 80 + 40 * math.sin(a)
        s.append(text(x, y + 4, "O", anchor="middle", size=13, c="b", weight=700))
        s.append(f'<line x1="{495 + 18 * math.cos(a):.1f}" y1="{80 + 18 * math.sin(a):.1f}" x2="{495 + 32 * math.cos(a):.1f}" y2="{80 + 32 * math.sin(a):.1f}" stroke="#7c3aed" stroke-dasharray="2 2" stroke-width="1.6"/>')
    s.append(text(495, 146, "离子溶于水", anchor="middle", size=10.5, c="s") + text(495, 160, "O(δ−) 朝向 Na⁺", anchor="middle", size=10.5, c="s"))
    s.append(text(20, 184, "强度：London（同等大小时最弱）&lt; 偶极-偶极 &lt; 氢键 &lt; 离子-偶极；分子间力 ≪ 分子内的化学键", size=11.5, weight=700))
    s.append(text(20, 202, "注意：London 力随电子数（分子大小）增加而变强，大分子的 London 力可以超过小分子的偶极力", size=11, c="s"))
    return fig(svg(p, 560, 210, "".join(s)), "四种分子间作用力 intermolecular forces", style=css)


def c08_bp():
    p = "c8"
    data = [("H₂O", 100), ("H₂S", -60), ("H₂Se", -41), ("H₂Te", -2)]
    zero = 120
    sc = 0.75
    s = [f'<line x1="40" y1="{zero}" x2="330" y2="{zero}" stroke="#1f2937" stroke-width="1.5"/>',
         text(36, zero + 4, "0 °C", anchor="end", size=10.5)]
    for i, (n, v) in enumerate(data):
        x = 60 + i * 68
        h = abs(v) * sc
        y = zero - h if v > 0 else zero
        col = "#dc2626" if i == 0 else "#2563eb"
        s.append(f'<rect x="{x}" y="{y:.1f}" width="40" height="{h:.1f}" fill="{col}" class="gy" style="--d:{0.2 + i * 0.4}s;--o:{"bottom" if v > 0 else "top"}"/>')
        s.append(text(x + 20, (y - 5) if v > 0 else (y + h + 14), f"{v} °C", anchor="middle", size=11, weight=700))
        s.append(text(x + 20, zero - 6 if v < 0 else zero + 16, n, anchor="middle", size=12))
    s += [arrow(p, 158, 196, 318, 150, "b", 2, d=2.0), text(250, 200, "London 力随电子数 ↑", c="b", size=11, d=2.0),
          text(350, 30, "H₂O 反常地高：", c="r", weight=700, d=2.4),
          text(350, 48, "分子间有氢键 hydrogen bonds", c="r", d=2.4),
          text(350, 80, "答题四步（4 分题）：", weight=700),
          text(350, 98, "① 写出两者的 IMF 类型"), text(350, 116, "② 比较强弱并说原因"),
          text(350, 134, "③ 克服 IMF 需要更多能量"), text(350, 152, "④ 所以沸点更高")]
    return fig(svg(p, 560, 210, "".join(s)), "第 16 族氢化物的沸点（文献近似值）：IMF 越强，沸点越高")


def c10_kmt():
    p = "c10"
    import random
    rnd = random.Random(7)
    L_, T_, B_, R_ = 30, 30, 170, 300
    s = [f'<rect x="{L_}" y="{T_}" width="{R_ - L_ + 40}" height="{B_ - T_}" fill="#f9fafb" stroke="#1f2937" stroke-width="2.4"/>']
    s += [f'<circle class="p" cx="{rnd.uniform(L_ + 8, 220):.1f}" cy="{rnd.uniform(T_ + 8, B_ - 8):.1f}" r="4.5" fill="#2563eb"/>' for _ in range(26)]
    s += [f'<rect class="piston" x="{R_}" y="{T_ + 2}" width="14" height="{B_ - T_ - 4}" fill="#9ca3af" stroke="#1f2937"/>',
          text(L_, 192, "", cls="hits", size=11.5, c="r", weight=700),
          text(L_ + 210, 192, "", cls="vol", size=11.5, c="s")]
    s += [text(370, 34, "分子运动论 KMT：", weight=700), text(370, 52, "· 气体分子不停地随机运动", size=11.5),
          text(370, 70, "· 撞击器壁 → 产生压强", size=11.5), text(370, 88, "· 温度 ∝ 分子平均动能", size=11.5),
          text(370, 116, "体积变小（T 不变）：", weight=700, c="b"), text(370, 134, "分子速度不变，但单位时间", size=11.5),
          text(370, 152, "撞墙次数增多 → 压强增大", size=11.5), text(370, 176, "这就是 Boyle 定律 p ∝ 1/V", weight=700, c="r")]
    attrs = f'data-kmt data-left="{L_}" data-top="{T_}" data-bottom="{B_}" data-right="{R_}" data-min="{150}"'
    return fig(svg(p, 560, 200, "".join(s), attrs), "屏幕上：活塞来回推拉，注意碰撞次数随体积变化（打印版为静态）", anim=False)


def c12_real():
    p = "c12"
    import random
    rnd = random.Random(3)
    css = ".fig .jg{animation:c12j 1.4s ease-in-out infinite alternate}@keyframes c12j{to{transform:translate(2px,-2px)}}@media print{.fig .jg{animation:none}}"
    s = [f'<rect x="20" y="30" width="200" height="130" fill="#f9fafb" stroke="#1f2937" stroke-width="2"/>',
         text(120, 22, "低压、高温：接近理想气体", anchor="middle", weight=700, c="g")]
    s += [f'<circle class="jg" cx="{rnd.uniform(30, 210):.1f}" cy="{rnd.uniform(40, 150):.1f}" r="3" fill="#2563eb"/>' for _ in range(10)]
    s += [f'<rect x="300" y="30" width="110" height="130" fill="#f9fafb" stroke="#1f2937" stroke-width="2"/>',
          text(355, 22, "高压、低温：偏离", anchor="middle", weight=700, c="r")]
    pts = [(312 + (i % 5) * 21, 44 + (i // 5) * 24) for i in range(25)]
    s += [f'<circle cx="{x}" cy="{y}" r="8" fill="#93c5fd" stroke="#1e40af"/>' for x, y in pts]
    s += [f'<line x1="{x + 8}" y1="{y}" x2="{x + 13}" y2="{y}" stroke="#dc2626" stroke-width="2" stroke-dasharray="2 1"/>' for x, y in pts[:4]]
    s += [text(440, 50, "① 分子本身的体积", size=11.5, weight=700), text(440, 66, "不能再忽略", size=11.5),
          text(440, 96, "② 分子间吸引力", size=11.5, weight=700), text(440, 112, "（红色）变得明显", size=11.5),
          text(440, 140, "温度接近沸点时", size=11.5), text(440, 156, "气体会液化", size=11.5),
          text(20, 186, "理想气体假设：分子无体积、无分子间力。真实气体只在“分子相距很远”时才接近理想。", size=11.5, weight=700)]
    return fig(svg(p, 580, 196, "".join(s)), "理想气体 vs 真实气体", anim=False, style=css)


def c14_profile():
    p = "c14"
    ox, oy = 50, 180
    s = [f'<line x1="{ox}" y1="{oy}" x2="{ox + 330}" y2="{oy}" stroke="#1f2937" stroke-width="1.5"/>',
         f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="20" stroke="#1f2937" stroke-width="1.5"/>',
         text(ox + 6, 22, "势能 Ep", size=11), text(ox + 330, oy + 16, "反应进程", size=11, anchor="end")]
    R, peak, Pd = 120, 40, 155
    main = f"M{ox + 10} {R} H{ox + 90} C{ox + 130} {R} {ox + 140} {peak} {ox + 170} {peak} C{ox + 200} {peak} {ox + 210} {Pd} {ox + 250} {Pd} H{ox + 320}"
    cat = f"M{ox + 90} {R} C{ox + 130} {R} {ox + 140} 85 {ox + 170} 85 C{ox + 200} 85 {ox + 210} {Pd} {ox + 250} {Pd}"
    s += [path(main, "k", 2.6, d=0.1, length=460),
          text(ox + 40, R - 8, "反应物", size=11), text(ox + 262, Pd + 16, "生成物", size=11),
          text(ox + 170, peak - 8, "活化络合物 activated complex", size=10.5, anchor="middle"),
          arrow(p, ox + 70, R, ox + 70, peak + 2, "r", 2, d=1.3), f'<line x1="{ox + 60}" y1="{peak}" x2="{ox + 175}" y2="{peak}" stroke="#9ca3af" stroke-dasharray="3 3"/>',
          text(ox + 64, 80, "Ea", c="r", anchor="end", weight=700, d=1.3),
          arrow(p, ox + 300, R, ox + 300, Pd - 2, "b", 2, d=1.8), f'<line x1="{ox + 90}" y1="{R}" x2="{ox + 310}" y2="{R}" stroke="#9ca3af" stroke-dasharray="3 3"/>',
          text(ox + 306, 142, "ΔH &lt; 0", c="b", weight=700, d=1.8),
          path(cat, "g", 2.2, d=2.4, length=300, dash=False),
          text(ox + 222, 70, "绿线：加催化剂", c="g", size=11, d=2.6), text(ox + 222, 86, "Ea 变小", c="g", size=11, d=2.6)]
    s += [text(400, 40, "放热反应 exothermic", weight=700, c="b"), text(400, 58, "生成物能量更低，ΔH 为负", size=11.5),
          text(400, 86, "吸热反应 endothermic", weight=700, c="r"), text(400, 104, "生成物能量更高，ΔH 为正", size=11.5),
          text(400, 132, "ΔH = 断键吸收 − 成键放出", weight=700), text(400, 160, "催化剂：降低 Ea，", c="g", size=11.5),
          text(400, 176, "ΔH 不变", c="g", size=11.5, weight=700)]
    return fig(svg(p, 580, 200, "".join(s)), "能量曲线 energy profile（放热反应）；绿线 = 加入催化剂后的新路径")


def c16_molemap():
    p = "c16"
    cx, cy = 270, 105
    s = [f'<circle cx="{cx}" cy="{cy}" r="36" fill="#fde68a" stroke="#b45309" stroke-width="2.4"/>',
         text(cx, cy - 2, "n", anchor="middle", size=24, cls="m", weight=700), text(cx, cy + 18, "mol", anchor="middle", size=11)]
    nodes = [(80, 105, "质量 m (g)", "n = m/M", "÷M", "×M"), (460, 105, "粒子数 N", "N = n·N_A", "×N_A", "÷N_A"),
             (270, 18, "气体体积 V (dm³)", f"n = V/V{sb('m')}（STP: 22,4）", "", ""), (270, 192, "溶液 c, V (dm³)", "n = cV", "", "")]
    for i, (x, y, lab, f, a1, a2) in enumerate(nodes):
        s.append(g(f'<rect x="{x - 70}" y="{y - 16}" width="140" height="32" rx="16" fill="#fff" stroke="#b45309" stroke-width="2"/>'
                   + text(x, y + 5, lab, anchor="middle", weight=700, size=12), d=0.3 + i * 0.4))
        if i == 0:
            s.append(arrow(p, 150, 98, 232, 98, "a", 2, d=0.3) + arrow(p, 232, 112, 150, 112, "a", 2, d=0.3))
            s.append(text(191, 92, f, anchor="middle", size=11, d=0.3))
        elif i == 1:
            s.append(arrow(p, 308, 98, 390, 98, "a", 2, d=0.7) + arrow(p, 390, 112, 308, 112, "a", 2, d=0.7))
            s.append(text(349, 92, "×6,02×10²³", anchor="middle", size=11, d=0.7))
        elif i == 2:
            s.append(arrow(p, 262, 36, 262, 67, "a", 2, d=1.1) + arrow(p, 278, 67, 278, 36, "a", 2, d=1.1))
            s.append(text(290, 56, f, size=11, d=1.1))
        else:
            s.append(arrow(p, 262, 175, 262, 143, "a", 2, d=1.5) + arrow(p, 278, 143, 278, 175, "a", 2, d=1.5))
            s.append(text(290, 162, f + "（cm³ ÷ 1000 → dm³）", size=11, d=1.5))
    return fig(svg(p, 540, 214, "".join(s)), "摩尔桥 mole bridge：任何换算都先“走到”中间的 n，再走出去")


def c18_flow():
    p = "c18"
    steps = [("① 百分比", "C 52,2%  H 13,0%  O 34,8%"), ("② 假设 100 g", "52,2 g  13,0 g  34,8 g"),
             ("③ n = m/M", "4,35  13,0  2,175 mol"), ("④ ÷ 最小值", "2 : 5,98 : 1"), ("⑤ 经验式", "C₂H₆O")]
    s = []
    for i, (a, b) in enumerate(steps):
        x = 12 + i * 108
        s.append(g(f'<rect x="{x}" y="36" width="96" height="80" rx="8" fill="#fffbeb" stroke="#b45309" stroke-width="1.8"/>'
                   + text(x + 48, 58, a, anchor="middle", weight=700, size=12)
                   + "".join(text(x + 48, 80 + k * 13, t, anchor="middle", size=10.5) for k, t in enumerate(b.split("  "))), d=0.2 + i * 0.5))
        if i < 4:
            s.append(arrow(p, x + 97, 75, x + 107, 75, "a", 2, d=0.2 + i * 0.5))
    s += [text(12, 142, "⑥ 分子式：若 M = 46 g·mol⁻¹，经验式质量 C₂H₆O = 46 → 倍数 46 ÷ 46 = 1 → 分子式 C₂H₆O", size=11.5, weight=700, d=2.8),
          text(12, 162, "小数处理：比值是 1,5 → 全部 ×2；1,33 或 1,67 → 全部 ×3；接近整数（如 5,98）才可以直接取整", size=11.3, c="r", d=3.1),
          text(12, 184, "水合物 CuSO₄·xH₂O：失去的质量 = 水；x = n(H₂O) ÷ n(CuSO₄)", size=11.3, c="s", d=3.3)]
    return fig(svg(p, 560, 194, "".join(s)), "由百分比求经验式 empirical formula 的固定流程")


def c20_sandwich():
    p = "c20"

    def bread(x, y):
        return f'<rect x="{x}" y="{y}" width="26" height="9" rx="3" fill="#f59e0b" stroke="#92400e"/>'

    def cheese(x, y):
        return f'<rect x="{x + 2}" y="{y}" width="22" height="7" fill="#fde047" stroke="#a16207"/>'
    s = [text(20, 22, "配方：2 片面包 + 1 片芝士 → 1 个三明治", weight=700)]
    s += [bread(20 + (i % 5) * 32, 40 + (i // 5) * 16) for i in range(10)]
    s.append(text(100, 92, "10 片面包", anchor="middle", size=11))
    s += [cheese(210 + i * 30, 48) for i in range(3)]
    s.append(text(252, 92, "3 片芝士", anchor="middle", size=11))
    s.append(arrow(p, 300, 56, 340, 56, "k", 2.4))
    for i in range(3):
        x = 355 + i * 40
        s.append(g(bread(x, 40) + cheese(x, 50) + bread(x, 58), d=0.4 + i * 0.5))
    s.append(text(410, 92, "只能做 3 个", anchor="middle", size=11, d=1.8))
    s += [g(bread(480 + (i % 2) * 30, 40 + (i // 2) * 14), d=2.0) for i in range(4)]
    s.append(text(510, 92, "剩 4 片面包", anchor="middle", size=11, d=2.0))
    s += [text(20, 124, "芝士 = 限量试剂 limiting reagent（先用完，决定产量）", c="r", weight=700, d=2.4),
          text(20, 142, "面包 = 过量试剂 excess reagent（有剩余）", c="b", weight=700, d=2.4),
          text(20, 168, "化学里同理：先把质量换成 mol，再按方程式系数比较，“不够用”的那个就是限量试剂。", size=11.5, d=2.8),
          text(20, 186, "不能直接比较质量（g），也不能只比较 mol 数，一定要结合系数！", size=11.5, c="r", d=3.0)]
    return fig(svg(p, 560, 196, "".join(s)), "三明治类比：理解限量试剂")


def c22_naming():
    p = "c22"
    # skeleton: a-b-c-d horizontal; methyl on b (up), ethyl on c (down two)
    pos = {"a": (80, 70), "b": (160, 70), "c": (240, 70), "d": (320, 70), "m": (160, 20), "e1": (240, 120), "e2": (320, 120)}
    bonds = [("a", "b"), ("b", "c"), ("c", "d"), ("b", "m"), ("c", "e1"), ("e1", "e2")]
    s = ["".join(f'<line x1="{pos[u][0]}" y1="{pos[u][1]}" x2="{pos[v][0]}" y2="{pos[v][1]}" stroke="#1f2937" stroke-width="2"/>' for u, v in bonds)]
    chain = ["a", "b", "c", "e1", "e2"]
    dpath = "M" + " L".join(f"{pos[k][0]} {pos[k][1]}" for k in chain)
    s.append(path(dpath, "#f59e0b", 14, d=0.3, length=360).replace('fill="none"', 'fill="none" stroke-linecap="round" stroke-linejoin="round" opacity=".55"'))
    labels = {"a": "CH₃", "b": "CH", "c": "CH", "d": "CH₃", "m": "CH₃", "e1": "CH₂", "e2": "CH₃"}
    for k, (x, y) in pos.items():
        s.append(f'<rect x="{x - 22}" y="{y - 13}" width="44" height="26" rx="6" fill="#fff" stroke="#1f2937"/>' + text(x, y + 5, labels[k], anchor="middle", size=13))
    for i, k in enumerate(chain):
        x, y = pos[k]
        s.append(text(x - 26, y - 14, str(i + 1), c="r", weight=700, size=14, d=1.6 + i * 0.25))
    s.append(text(160, 4, "", size=1))
    s += [text(380, 30, "命名步骤：", weight=700), text(380, 50, "① 找最长碳链（不一定是横的！）", size=11.5),
          text(380, 68, "   橙色 = 5 个 C → pentane", size=11.5, c="a"),
          text(380, 90, "② 从离支链最近的一端编号", size=11.5), text(380, 108, "   支链在 2 号和 3 号碳上", size=11.5, c="r"),
          text(380, 130, "③ 支链按字母序，相同的用 di/tri", size=11.5),
          text(380, 160, "2,3-dimethylpentane", weight=700, size=15, c="g", d=3.0),
          text(380, 180, "✗ 不是 2-ethyl-3-methylbutane", size=11.5, c="r", d=3.2)]
    return fig(svg(p, 580, 190, "".join(s)), "IUPAC 命名：最常见的陷阱是没找到真正的最长链")


def c24_groups():
    rows = [("卤代烷 haloalkane", "−X（F, Cl, Br, I）", "前缀 chloro-/bromo-", "CH₃CH₂Cl chloroethane"),
            ("醇 alcohol", "−OH 羟基", "后缀 -ol", "CH₃CH₂OH ethanol"),
            ("醛 aldehyde", "−CHO（C=O 在链端）", "后缀 -al", "CH₃CHO ethanal"),
            ("酮 ketone", "C=O 在链中间", "后缀 -one", "CH₃COCH₃ propanone"),
            ("羧酸 carboxylic acid", "−COOH 羧基", "后缀 -oic acid", "CH₃COOH ethanoic acid"),
            ("酯 ester", "−COO−", "烷基 + -oate", "CH₃COOCH₂CH₃ ethyl ethanoate")]
    html = '<div style="overflow-x:auto"><table class="grid" style="font-size:12.3px;min-width:480px"><tr><th>类别 homologous series</th><th>官能团 functional group</th><th>命名</th><th>例子</th></tr>'
    for i, r in enumerate(rows):
        html += f'<tr class="fd" style="--d:{0.2 + i * 0.35}s">' + "".join(f"<td>{c}</td>" for c in r) + "</tr>"
    html += "</table></div>"
    html += ('<p style="font-size:12.3px;margin:4px 2px"><b>酯的命名口诀：</b>来自<b style="color:#b45309">醇</b>的部分写在前面（-yl），'
             '来自<b style="color:#2563eb">酸</b>的部分写在后面（-oate）。CH₃COO|CH₂CH₃：左边 2 个 C 来自 ethanoic acid，右边来自 ethanol → ethyl ethanoate。</p>')
    return f'<figure class="fig" data-anim>{html}<figcaption>六类官能团速查表</figcaption></figure>'


def c24_ester():
    p = "c24"
    s = [text(20, 30, "CH₃—C", size=18), text(76, 14, "O", size=16), text(78, 26, "‖", size=14),
         text(92, 30, "—O—CH₂—CH₃", size=18),
         f'<rect x="14" y="8" width="80" height="34" rx="6" fill="none" stroke="#2563eb" stroke-width="2" class="fd" style="--d:.3s"/>',
         f'<rect x="114" y="8" width="112" height="34" rx="6" fill="none" stroke="#b45309" stroke-width="2" class="fd" style="--d:.9s"/>',
         text(54, 62, "来自酸 → ethanoate", c="b", anchor="middle", size=11.5, d=.3),
         text(170, 62, "来自醇 → ethyl", c="a", anchor="middle", size=11.5, d=.9)]
    return svg(p, 250, 70, "".join(s))


def p25_faraday():
    p = "v25"
    css = (".fig.play .mag{animation:v25m 2.4s ease-in-out .3s 2 alternate both}"
           "@keyframes v25m{from{transform:translateX(-70px)}to{transform:translateX(0)}}"
           ".fig.play .ndl{transform-box:view-box;transform-origin:250px 170px;animation:v25n 2.4s ease-in-out .3s 2 alternate both}"
           "@keyframes v25n{0%{transform:rotate(0)}50%{transform:rotate(28deg)}100%{transform:rotate(0)}}")
    coil = "".join(f'<ellipse cx="{150 + k * 12}" cy="80" rx="6" ry="26" fill="none" stroke="#b45309" stroke-width="2.4"/>' for k in range(8))
    s = [coil,
         '<path d="M150 106 V170 H230 M270 170 H330 V106 H234" fill="none" stroke="#1f2937" stroke-width="2"/>',
         '<circle cx="250" cy="170" r="20" fill="#fff" stroke="#1f2937" stroke-width="2"/>', text(250, 202, "电流计 G", anchor="middle", size=11),
         '<line class="ndl" x1="250" y1="170" x2="250" y2="154" stroke="#dc2626" stroke-width="2.4"/>',
         '<g class="mag"><rect x="40" y="66" width="44" height="28" fill="#dc2626"/><rect x="84" y="66" width="44" height="28" fill="#2563eb"/>'
         + text(62, 85, "S", anchor="middle", c="#ffffff", weight=700) + text(106, 85, "N", anchor="middle", c="#ffffff", weight=700) + "</g>",
         text(30, 20, "磁铁进/出 → 磁通变化 → 感应电流", size=11.5, weight=700),
         text(30, 38, "磁铁不动 → 磁通不变 → 指针不动", size=11, c="s")]
    ox, oy = 450, 110
    s += [text(390, 20, "Φ = BA cosθ 中的 θ", size=11.5, weight=700),
          '<line x1="420" y1="60" x2="480" y2="160" stroke="#1f2937" stroke-width="5"/>',
          text(486, 170, "线圈平面", size=10.5),
          arrow(p, 450, 110, 450 + 70 * 0.866, 110 - 70 * 0.5, "g", 2.2),
          text(512, 70, "法线 normal", size=10.5, c="g"),
          arrow(p, 380, 110, 540, 110, "b", 2.2), text(380, 102, "磁场 B", size=10.5, c="b"),
          path("M480 110 A30 30 0 0 0 476 95", "r", 1.6), text(486, 104, "θ", c="r", cls="m"),
          text(370, 196, "平面⊥B：θ = 0°，Φ 最大", size=11), text(370, 212, "平面∥B：θ = 90°，Φ = 0", size=11)]
    return fig(svg(p, 580, 220, "".join(s)), "左：法拉第电磁感应（动画中磁铁进出，指针来回偏）；右：θ 是 B 与线圈平面法线的夹角", style=css)


def p26_lenz():
    p = "v26"
    css = (".fig.play .mg{animation:v26m 2s ease-out .2s both}@keyframes v26m{from{transform:translateX(-60px)}to{transform:translateX(0)}}")
    coil = "".join(f'<ellipse cx="{170 + k * 11}" cy="70" rx="6" ry="28" fill="none" stroke="#b45309" stroke-width="2.4"/>' for k in range(7))
    s = [text(20, 20, "① 来拒：N 靠近 → 左端感应出 N 极，排斥", size=11.5, weight=700),
         '<g class="mg"><rect x="40" y="56" width="44" height="28" fill="#dc2626"/><rect x="84" y="56" width="44" height="28" fill="#2563eb"/>'
         + text(62, 75, "S", anchor="middle", c="#ffffff", weight=700) + text(106, 75, "N", anchor="middle", c="#ffffff", weight=700) + "</g>",
         arrow(p, 100, 104, 140, 104, "k", 2), text(100, 120, "靠近", size=10.5),
         coil, text(158, 75, "N", anchor="end", weight=700, c="b", size=14),
         arrow(p, 156, 44, 136, 44, "r", 2.4), text(146, 38, "排斥", size=10.5, c="r", anchor="middle"),
         text(20, 150, "② 去留：N 离开 → 左端变成 S 极，吸引", size=11.5, weight=700),
         text(20, 168, "感应电流总是“反对”磁通的变化（楞次定律）", size=11, c="s")]
    # transformer
    s += ['<rect x="330" y="40" width="200" height="120" rx="6" fill="none" stroke="#6b7280" stroke-width="14"/>',
          "".join(f'<line x1="318" y1="{60 + k * 12}" x2="342" y2="{66 + k * 12}" stroke="#b45309" stroke-width="2.4"/>' for k in range(7)),
          "".join(f'<line x1="518" y1="{54 + k * 9}" x2="542" y2="{60 + k * 9}" stroke="#2563eb" stroke-width="2.4"/>' for k in range(10)),
          text(330, 30, "原线圈 Nₚ（接 AC）", size=11, c="#b45309", anchor="middle"),
          text(530, 30, "副线圈 Nₛ", size=11, c="b", anchor="middle"),
          text(430, 104, "铁芯中磁通", size=11, anchor="middle"), text(430, 120, "不断变化", size=11, anchor="middle"),
          text(330, 190, "Vₛ/Vₚ = Nₛ/Nₚ；只能用交流 AC", size=11.5, weight=700),
          text(330, 208, "Nₛ &gt; Nₚ 升压；Nₛ &lt; Nₚ 降压", size=11)]
    return fig(svg(p, 580, 216, "".join(s).replace(" > ", " &gt; ").replace(" < ", " &lt; ")),
               "左：楞次定律“来拒去留”；右：变压器（磁通变化才能在副线圈感应出电压）", style=css)


def p27_zero():
    p = "v27"
    A, B = 60, 300  # +Q at 60, +9Q at 300 (12 cm → 240 px)
    P = A + 60      # 3 cm
    s = [f'<line x1="30" y1="70" x2="330" y2="70" stroke="#9ca3af" stroke-dasharray="4 3"/>',
         f'<circle cx="{A}" cy="70" r="12" fill="#fecaca" stroke="#1f2937"/>', text(A, 75, "+Q", anchor="middle", size=10.5, weight=700),
         f'<circle cx="{B}" cy="70" r="20" fill="#fecaca" stroke="#1f2937"/>', text(B, 75, "+9Q", anchor="middle", size=11, weight=700),
         f'<circle cx="{P}" cy="70" r="4" fill="#7c3aed"/>', text(P, 58, "P：E = 0", anchor="middle", c="p", weight=700, size=11),
         arrow(p, P, 92, P + 50, 92, "r", 2.4, d=0.4), text(P + 54, 96, "E 来自 +Q（向右）", size=10.5, c="r", d=0.4),
         arrow(p, P, 108, P - 50, 108, "b", 2.4, d=0.9), text(P - 54, 126, "E 来自 +9Q（向左）", size=10.5, c="b", d=0.9),
         text(A, 150, "x = 3 cm", size=11, d=1.4), text(A + 120, 150, "12 − x = 9 cm", size=11, d=1.4),
         text(20, 178, "kQ/3² = k(9Q)/9² ✓ 两个场大小相等、方向相反", size=11.3, weight=700, d=1.8),
         text(20, 198, "零场点在两个同号电荷之间，靠近小电荷", size=11.3, c="s", d=1.8)]
    ox, oy, W, H = 380, 170, 170, 140
    s += [f'<line x1="{ox}" y1="{oy}" x2="{ox + W}" y2="{oy}" stroke="#1f2937" stroke-width="1.5"/>',
          f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy - H}" stroke="#1f2937" stroke-width="1.5"/>',
          text(ox + W, oy + 16, "r", size=11, anchor="end", cls="m"), text(ox + 4, oy - H - 4, "E", size=11, cls="m")]
    for q, col, lab in ((2, "#2563eb", "+2 nC"), (4, "#dc2626", "+4 nC")):
        pts = " ".join(f"{ox + x:.1f},{oy - min(H - 6, q * 18720 / (x + 10) ** 2):.1f}" for x in range(14, W, 3))
        s.append(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="2.4"/>')
        lx = 24 if q == 4 else 44
        s.append(text(ox + lx + 6, oy - q * 18720 / (lx + 10) ** 2 - 4, lab, size=11, c=col, weight=700))
    s.append(text(ox, oy + 34, "电荷越大，同一距离 E 越大", size=11, c="s"))
    return fig(svg(p, 580, 210, "".join(s)), "左：两个同号电荷之间的零场点；右：E 随距离的变化（反平方）")


def p28_vertical():
    p = "v28"
    css = (".fig.play .bl{animation:v28b 3s ease-in-out both}"
           "@keyframes v28b{0%{transform:translateY(0)}50%{transform:translateY(-120px);animation-timing-function:ease-in}100%{transform:translateY(0)}}")
    gx, gy = 70, 170
    s = [f'<line x1="20" y1="{gy + 10}" x2="160" y2="{gy + 10}" stroke="#1f2937" stroke-width="2"/>']
    # strobe positions (equal time intervals): heights from 14.7 m/s throw, scaled
    ts = [0, 0.5, 1.0, 1.5]
    for i, t in enumerate(ts):
        h = 14.7 * t - 4.9 * t * t
        y = gy - h * 10.9
        v = 14.7 - 9.8 * t
        s.append(f'<circle cx="{gx}" cy="{y:.1f}" r="7" fill="#bfdbfe" stroke="#1e40af" opacity=".55"/>')
        if v > 0.1:
            s.append(arrow(p, gx + 14, y, gx + 14, y - v * 4, "b", 2))
        s.append(text(gx - 14, y + 4, f"{t:.1f} s", size=9.5, anchor="end", c="s"))
    s += [f'<circle class="bl" cx="{gx}" cy="{gy}" r="8" fill="#2563eb"/>',
          text(gx + 34, gy - 140, "最高点：v = 0", size=11, c="r", weight=700),
          text(gx + 34, gy - 124, "a 仍 = 9,8 m·s⁻² ↓", size=11, c="r"),
          text(gx + 34, gy - 40, "蓝箭头 = 速度", size=10.5, c="b"),
          text(gx + 34, gy - 24, "越往上越短", size=10.5, c="b"),
          text(20, 204, "上抛 14,7 m·s⁻¹：每 0,5 s 的位置", size=10.5, c="s")]
    ox, oy, W = 260, 100, 290
    s += [f'<line x1="{ox}" y1="{oy}" x2="{ox + W}" y2="{oy}" stroke="#1f2937" stroke-width="1.5"/>',
          f'<line x1="{ox}" y1="20" x2="{ox}" y2="180" stroke="#1f2937" stroke-width="1.5"/>',
          text(ox + 4, 18, "v（向上为正）", size=10.5), text(ox + W, oy + 16, "t", size=11, anchor="end", cls="m"),
          text(ox + W / 2, 22, "弹跳球的 v–t 图", size=11.5, weight=700, anchor="middle")]
    # 斜率处处为 −g：每单位时间速度减少 70（像素单位），三段互相平行
    k, sx = 70.0, 70.0
    t, v0, lines = 0.0, 0.0, []
    for vstart, vend in ((0, -70), (60, -60), (50, -50)):
        dt = (vstart - vend) / k
        lines.append(f'<line x1="{ox + t * sx:.1f}" y1="{oy - vstart}" x2="{ox + (t + dt) * sx:.1f}" y2="{oy - vend}" stroke="#2563eb" stroke-width="2.6"/>')
        t += dt
    s += lines
    s += [f'<polygon points="{ox},{oy} {ox + sx},{oy + 70} {ox + sx},{oy}" fill="#bbf7d0" opacity=".7"/>',
          f'<line x1="{ox + sx}" y1="175" x2="{ox + sx}" y2="30" stroke="#9ca3af" stroke-dasharray="3 3"/>',
          text(ox + sx + 6, 42, "触地：v 由负变正", size=10.5, c="s"),
          text(ox + 150, 70, "各段平行：斜率 = −g", size=11, c="r", weight=700),
          text(ox + 4, oy + 90, "绿色面积 = 下落高度", size=10.5, c="g")]
    return fig(svg(p, 580, 210, "".join(s)), "左：上抛运动（动画中小球上升又落回）；右：弹跳球 v–t 图，各段平行", style=css)


def c29_rates():
    p = "c29"
    ox, oy, W, H = 40, 180, 300, 150
    import math as _m

    def mb(T):
        pts = []
        for i in range(0, 101):
            E = i / 100 * 4.0
            f = E ** 0.5 * _m.exp(-E / T) / T ** 1.5
            pts.append((ox + E / 4.0 * W, oy - f * 160))
        return pts
    c1, c2 = mb(0.5), mb(0.9)
    Ea = 2.2
    xe = ox + Ea / 4 * W
    shade = [(x, y) for x, y in c2 if x >= xe]
    poly = f"{xe},{oy} " + " ".join(f"{x:.1f},{y:.1f}" for x, y in shade) + f" {ox + W},{oy}"
    s = [f'<polygon points="{poly}" fill="#fecaca" class="fd" style="--d:1.6s"/>',
         f'<line x1="{ox}" y1="{oy}" x2="{ox + W + 10}" y2="{oy}" stroke="#1f2937" stroke-width="1.5"/>',
         f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="20" stroke="#1f2937" stroke-width="1.5"/>',
         text(ox + 4, 18, "粒子数", size=10.5), text(ox + W + 6, oy + 16, "动能 Ek", size=10.5, anchor="end"),
         f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in c1)}" fill="none" stroke="#2563eb" stroke-width="2.4"/>',
         f'<polyline class="dr" style="--d:.4s;--len:420" points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in c2)}" fill="none" stroke="#dc2626" stroke-width="2.4"/>',
         text(ox + 26, 36, "T₁", c="b", weight=700), text(ox + 64, 96, "T₂ &gt; T₁", c="r", weight=700),
         f'<line x1="{xe}" y1="{oy}" x2="{xe}" y2="40" stroke="#1f2937" stroke-dasharray="4 3"/>', text(xe + 4, 50, "Ea", cls="m", weight=700),
         f'<line x1="{xe - 50}" y1="{oy}" x2="{xe - 50}" y2="120" stroke="#059669" stroke-dasharray="4 3" class="fd" style="--d:2.4s"/>',
         text(xe - 50, oy + 30, "绿线：加催化剂后 Ea 左移", size=10.5, c="g", anchor="middle", d=2.4),
         text(xe + 10, 150, "阴影：能量 ≥ Ea", size=10.5, c="r", d=1.6), text(xe + 10, 164, "的粒子（可反应）", size=10.5, c="r", d=1.6)]
    gx, gy, gw, gh = 400, 170, 150, 120
    curve = " ".join(f"{gx + t:.1f},{gy - gh * 0.85 * (1 - _m.exp(-t / 30)):.1f}" for t in range(0, gw + 1, 3))
    curve2 = " ".join(f"{gx + t:.1f},{gy - gh * 0.85 * (1 - _m.exp(-t / 70)):.1f}" for t in range(0, gw + 1, 3))
    s += [f'<line x1="{gx}" y1="{gy}" x2="{gx + gw}" y2="{gy}" stroke="#1f2937" stroke-width="1.5"/>',
          f'<line x1="{gx}" y1="{gy}" x2="{gx}" y2="{gy - gh - 10}" stroke="#1f2937" stroke-width="1.5"/>',
          text(gx + 4, gy - gh - 12, "生成气体体积", size=10.5), text(gx + gw, gy + 16, "时间", size=10.5, anchor="end"),
          f'<polyline points="{curve}" fill="none" stroke="#dc2626" stroke-width="2.4"/>',
          f'<polyline points="{curve2}" fill="none" stroke="#2563eb" stroke-width="2.4"/>',
          text(gx + 30, gy - 112, "粉末 / 更热：更快", size=10, c="r"), text(gx + 60, gy - 50, "块状：较慢", size=10, c="b"),
          text(gx, gy + 34, "斜率 = 速率；最终体积相同", size=10.5, c="s")]
    return fig(svg(p, 580, 216, "".join(s)), "左：Maxwell–Boltzmann 能量分布（温度升高，阴影面积变大）；右：速率曲线")


def c30_redox():
    p = "c30"
    css = (".fig .cu{opacity:1}.fig.play .cu{animation:fig-fade 1s ease-out 1.6s both}"
           ".fig.play .ed{animation:c30e 1.4s ease-in .2s 2 both}@keyframes c30e{from{transform:translate(0,0);opacity:1}to{transform:translate(34px,30px);opacity:.2}}")
    s = ['<path d="M40 60 V180 H180 V60" fill="none" stroke="#1f2937" stroke-width="2"/>',
         '<rect x="42" y="95" width="136" height="83" fill="#bfdbfe" opacity=".75"/>',
         '<rect x="98" y="40" width="22" height="130" fill="#9ca3af" stroke="#1f2937"/>', text(109, 34, "Zn", anchor="middle", weight=700),
         '<g class="cu">' + "".join(f'<circle cx="{120 + (i % 2) * 5}" cy="{110 + i * 9}" r="3.5" fill="#b45309"/>' for i in range(7)) + '</g>',
         text(150, 112, "Cu²⁺", size=11, c="b"), text(60, 150, "Cu²⁺", size=11, c="b"),
         '<g class="ed">' + "".join(f'<circle cx="{108 + i * 3}" cy="{100 + i * 14}" r="2.6" fill="#dc2626"/>' for i in range(3)) + '</g>',
         text(110, 200, "Zn 失去电子，Cu 析出在锌片上", anchor="middle", size=10.5, c="s")]
    s += [text(210, 40, "Zn → Zn²⁺ + 2e⁻", weight=700, c="r"), text(380, 40, "氧化（失电子）", c="r", size=11),
          text(210, 64, "Cu²⁺ + 2e⁻ → Cu", weight=700, c="b"), text(380, 64, "还原（得电子）", c="b", size=11),
          text(210, 92, "Zn：被氧化 → 是还原剂", size=11.5), text(210, 110, "Cu²⁺：被还原 → 是氧化剂", size=11.5),
          text(210, 140, "OIL RIG：Oxidation Is Loss，Reduction Is Gain", size=11.5, weight=700, c="p")]
    ox, y = 210, 178
    s.append(f'<line x1="{ox}" y1="{y}" x2="{ox + 340}" y2="{y}" stroke="#1f2937" stroke-width="1.5"/>')
    for k, n in enumerate(range(-2, 8)):
        x = ox + 10 + k * 36
        s.append(f'<line x1="{x}" y1="{y - 4}" x2="{x}" y2="{y + 4}" stroke="#1f2937"/>' + text(x, y + 18, f"{n:+d}" if n else "0", size=10, anchor="middle"))
    s += [arrow(p, ox + 120, y - 10, ox + 200, y - 10, "r", 2), text(ox + 160, y - 16, "氧化：氧化数升高", size=10, c="r", anchor="middle"),
          arrow(p, ox + 300, y - 10, ox + 230, y - 10, "b", 2), text(ox + 300, y - 16, "还原：降低", size=10, c="b", anchor="end")]
    return fig(svg(p, 580, 212, "".join(s)), "锌片放进 CuSO₄ 溶液：Zn 被氧化、Cu²⁺ 被还原（动画中电子从 Zn 转移给 Cu²⁺）", style=css)


def c31_cell():
    p = "c31"
    s = ['<path d="M30 80 V190 H170 V80" fill="none" stroke="#1f2937" stroke-width="2"/>', '<rect x="32" y="110" width="136" height="78" fill="#e5e7eb" opacity=".8"/>',
         '<path d="M330 80 V190 H470 V80" fill="none" stroke="#1f2937" stroke-width="2"/>', '<rect x="332" y="110" width="136" height="78" fill="#bfdbfe" opacity=".8"/>',
         '<rect x="88" y="60" width="20" height="110" fill="#9ca3af" stroke="#1f2937"/>', '<rect x="392" y="60" width="20" height="110" fill="#b45309" stroke="#1f2937"/>',
         '<path d="M140 150 V95 H360 V150" fill="none" stroke="#d97706" stroke-width="16" stroke-linejoin="round" opacity=".55"/>',
         text(250, 90, "盐桥 salt bridge（离子移动）", size=10.5, anchor="middle"),
         '<path d="M98 60 V30 H230 M270 30 H402 V60" fill="none" stroke="#1f2937" stroke-width="2"/>',
         '<circle cx="250" cy="30" r="18" fill="#fff" stroke="#1f2937" stroke-width="2"/>', text(250, 35, "V", anchor="middle", weight=700),
         '<path d="M110 22 H228" stroke="#dc2626" stroke-width="2.4" fill="none" class="flow"/>', '<path d="M272 22 H392" stroke="#dc2626" stroke-width="2.4" fill="none" class="flow"/>',
         arrow(p, 160, 14, 200, 14, "r", 2), text(150, 10, "e⁻", c="r", size=11),
         text(98, 206, "Zn 阳极（−）：氧化", anchor="middle", size=11, weight=700),
         text(98, 222, "Zn → Zn²⁺ + 2e⁻", anchor="middle", size=10.5),
         text(402, 206, "Cu 阴极（+）：还原", anchor="middle", size=11, weight=700),
         text(402, 222, "Cu²⁺ + 2e⁻ → Cu", anchor="middle", size=10.5),
         text(140, 140, "Zn²⁺", size=10, c="s"), text(430, 140, "Cu²⁺", size=10, c="b")]
    s += [text(490, 60, "原电池：", size=11, weight=700), text(490, 76, "化学能→电能", size=10.5),
          text(490, 104, "E°cell", size=11, weight=700), text(490, 120, "= 0,34 − (−0,76)", size=10.5), text(490, 136, "= 1,10 V", size=10.5, weight=700),
          text(490, 168, "An Ox,", size=11, c="p", weight=700), text(490, 184, "Red Cat", size=11, c="p", weight=700)]
    return fig(svg(p, 590, 230, "".join(s)), "Zn–Cu 原电池：电子经导线从阳极流向阴极（屏幕上红线流动），盐桥中移动的是离子", anim=False)


FIGS = {
    "p01": p01_vectors, "p03": p03_distance, "p05": p05_chase, "p07": p07_graphs, "p09": p09_fbd, "p11": p11_incline,
    "p13": p13_connected, "p15": p15_gravity, "p17": p17_contact, "p19": p19_field, "p21": p21_series_parallel, "p23": p23_emf,
    "c02": c02_dative, "c04": c04_vsepr, "c06": c06_imf, "c08": c08_bp, "c10": c10_kmt, "c12": c12_real, "c14": c14_profile,
    "c16": c16_molemap, "c18": c18_flow, "c20": c20_sandwich, "c22": c22_naming, "c24": c24_groups,
    "p25": p25_faraday, "p26": p26_lenz, "p27": p27_zero, "p28": p28_vertical,
    "c29": c29_rates, "c30": c30_redox, "c31": c31_cell,
}
EXFIGS = {"ex07": ex07_vt, "ex21": ex21_circuit}
