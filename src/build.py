#!/usr/bin/env python3
"""生成静态网站：python3 src/build.py（输出到仓库根目录）"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from content_phys import PHYS, PHYS_EXTRA, M, FR  # noqa: E402
from content_chem import CHEM  # noqa: E402
from figs import FIGS, EXFIGS  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "IEB Physical Sciences · Grade 11"

# 物理、化学交替排列
DAYS = [d for pair in zip(PHYS, CHEM) for d in pair] + PHYS_EXTRA
N = len(DAYS)


def subj(d):
    return "phy" if d["code"].startswith("p") else "chem"


def subj_zh(d):
    return "物理 P1" if subj(d) == "phy" else "化学 P2"


def page(title, body, rel="", cls="", bar=""):
    return f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="{rel}assets/style.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='7' fill='%230f766e'/%3E%3Ctext x='16' y='22' font-size='16' text-anchor='middle' fill='white' font-family='Arial'%3EPS%3C/text%3E%3C/svg%3E">
</head>
<body class="{cls}">
{bar}
{body}
<script src="{rel}assets/fig.js"></script>
</body>
</html>
"""


def bar(rel, links):
    a = "".join(f'<a href="{h}">{t}</a>' for t, h in links)
    return (f'<nav class="bar"><a href="{rel}index.html">🏠 首页</a>{a}<span class="sp"></span>'
            f'<button class="print" onclick="window.print()">🖨 打印 / 存 PDF</button></nav>')


def stars(lv):
    return "★" * lv


def ex_html(e):
    lines = "".join('<div class="ln"></div>' for _ in range(e.get("ln", 0)))
    box = f'<div class="box" style="height:{e["box"]}mm"></div>' if e.get("box") else ""
    return (f'<div class="q"><span class="no">{e["n"]}</span><span class="lv">{stars(e["lv"])}</span>'
            f'<span class="tx">{e["q"]}</span><span class="mk">({e["mk"]})</span></div>{lines}{box}')


def day_page(i, d):
    no = i + 1
    rel = "../"
    prev_ = f"d{no - 1:02d}.html" if no > 1 else None
    next_ = f"d{no + 1:02d}.html" if no < N else None
    links = []
    if prev_:
        links.append(("← 上一天", prev_))
    if next_:
        links.append(("下一天 →", next_))
    links.append(("✅ 答案", f"../answers/a{no:02d}.html"))
    total = sum(e["mk"] for e in d["ex"])
    head = (f'<div class="hd"><span class="day">Day {no:02d}</span><span class="tag">{subj_zh(d)}</span>'
            f'<span class="t">{d["zh"]}</span><span class="sub">日期 ______ 用时 ______ 分钟</span></div>'
            f'<div class="hd" style="border:0;margin:-6px 0 4px;padding:0"><span class="en">{d["en"]}</span></div>')
    warm = "".join(f'<div class="q"><span class="no">W{k + 1}</span><span class="tx">{q}</span></div>'
                   + "".join('<div class="ln"></div>' for _ in range(n)) for k, (q, n) in enumerate(d["warm"]))
    formulas = '<div class="fbox">' + "".join(f"<span>{f}</span>" for f in d["formulas"]) + "</div>"
    pit = "".join(f'<div class="warn">⚠ {p}</div>' for p in d["pitfalls"])
    defs = '<dl class="defs">' + "".join(f"<dt>{en} · {zh}</dt><dd>{df}</dd>" for en, zh, df in d["defs"]) + "</dl>"
    foot = lambda side: f'<div class="foot"><span>{SITE} · Day {no:02d} / {N}</span><span>{side}</span></div>'
    front = (f'<section class="sheet">{head}'
             f'<h3 class="sec">⏱ 热身 5 分钟<small>连接旧知识：{d["bridge"]}</small></h3><div class="warm">{warm}</div>'
             f'<h3 class="sec">📘 今日新知</h3>{d["learn"]}'
             f'{FIGS[d["code"]]()}'
             f'<h3 class="sec">🧮 公式</h3>{formulas}'
             f'<h3 class="sec">📖 必背定义<small>今天就背；反面练习时合上正面默写</small></h3>{defs}{foot("正面 · 讲解")}</section>')
    exfig = EXFIGS[d["exfig"]]() if d.get("exfig") else ""
    back = (f'<section class="sheet"><div class="hd"><span class="day">Day {no:02d}</span><span class="t">练习 Practice</span>'
            f'<span class="sub">共 {total} 分 · 写出公式、代入、答案和单位</span></div>'
            f'<p class="note">做题时不要翻看正面。空间不够时写在草稿纸上，并标好题号。</p>'
            f'<h3 class="sec">⚠ 做题前先读：常见失分点</h3>{pit}'
            f'<h3 class="sec">✏️ 今日练习<small>★ 基础　★★ 考试常见　★★★ 拔高</small></h3>{exfig}'
            + "".join(ex_html(e) for e in d["ex"])
            + f'<div class="self"><div>得分：<span></span> / {total}</div><div>错题题号：<span style="min-width:120px"></span></div>'
              f'<div>最不懂的一点：<span style="min-width:150px"></span></div><div>明天要重做：□ 是　□ 否</div></div>'
            f'{foot("反面 · 练习")}</section>')
    cls = "chem" if subj(d) == "chem" else ""
    return page(f"Day {no:02d} · {d['zh']}", front + back, rel, cls, bar(rel, links))


def answer_page(i, d):
    no = i + 1
    rel = "../"
    total = sum(e["mk"] for e in d["ex"])
    mk = {e["n"]: e["mk"] for e in d["ex"]}
    warm = "".join(f"<li><b>W{k + 1}</b>　{a}</li>" for k, a in enumerate(d["ans_warm"]))
    ans = "".join(f'<li><b>{n}</b>　<span class="note">({mk[n]} 分)</span><br>{a}</li>' for n, a in d["ans"])
    body = (f'<section class="sheet"><div class="hd"><span class="day">Day {no:02d}</span><span class="tag">{subj_zh(d)}</span>'
            f'<span class="t">答案与评分点</span><span class="sub">共 {total} 分</span></div>'
            f'<p class="note">每个 ✓ 代表考试中的 1 分。核对时不只看最终答案：公式、代入、单位、方向都要有。</p>'
            f'<h3 class="sec">⏱ 热身</h3><ol class="ans" style="list-style:none;padding-left:4px">{warm}</ol>'
            f'<h3 class="sec">✏️ 练习</h3><ol class="ans" style="list-style:none;padding-left:4px">{ans}</ol>'
            f'<h3 class="sec">🔁 订正方法</h3><p>错题用红笔在原题旁订正，并写一句“错在哪里”。第二天热身前，先把错题<b>不看答案</b>重做一遍。</p>'
            f'<div class="foot"><span>{SITE} · Day {no:02d} 答案</span><span>答案页</span></div></section>')
    links = [("← 回到题目", f"../days/d{no:02d}.html")]
    cls = "chem" if subj(d) == "chem" else ""
    return page(f"Day {no:02d} 答案 · {d['zh']}", body, rel, cls, bar(rel, links))


def index_page():
    rows = ""
    for i, d in enumerate(DAYS):
        no = i + 1
        if no == len(PHYS) + len(CHEM) + 1:
            rows += '<tr><td colspan="6" style="background:#ecfdf5"><b>补充：根据近期测验的薄弱点（电磁学、静电推理）</b></td></tr>'
        color = "#0f766e" if subj(d) == "phy" else "#b45309"
        rows += (f'<tr><td><b>Day {no:02d}</b></td><td style="color:{color};font-weight:700">{subj_zh(d)}</td>'
                 f'<td><a href="days/d{no:02d}.html">{d["zh"]}</a><br><span class="note">{d["en"]}</span></td>'
                 f'<td><a href="answers/a{no:02d}.html">答案</a></td><td></td><td></td></tr>')
    body = f"""<section class="sheet flow">
<div class="hd"><span class="day">Grade 11</span><span class="t">Physical Sciences 每日一练</span><span class="sub">IEB · 物理 P1 + 化学 P2</span></div>
<p>每天一张 A4（正面讲解、反面练习），双面打印。Day 01–24 物理和化学交替，覆盖 Grade 11 两张试卷的核心考点；Day 25–27 是针对近期测验薄弱点的物理补充，共 {N} 天。屏幕上的图解可以播放动画。</p>
<div class="card-links">
<a href="formulas.html"><b>🧮 公式总表</b><br><span class="note">对照 IEB data sheet，并列出表上没有、必须自己记的公式</span></a>
<a href="definitions.html"><b>📖 必背定义</b><br><span class="note">定义题每题 2 分，全部汇总，可遮住自测</span></a>
<a href="days/d01.html"><b>▶ 从 Day 01 开始</b><br><span class="note">矢量：合成与分解</span></a>
</div>
<h3 class="sec">每天 40 分钟怎么用</h3>
<ol class="tight">
<li><b>5 分钟热身</b>：做正面最上面的两道低年级题，把旧知识“接上”。</li>
<li><b>15 分钟学习</b>：读“今日新知”，看图解（屏幕上可以播放动画），把公式抄一遍，读失分点。</li>
<li><b>20 分钟练习</b>：翻到反面，先背定义，再按 ★ → ★★ → ★★★ 做题。<b>不要先看答案。</b></li>
<li><b>对答案</b>：用答案页按 ✓ 给自己打分，在下表记录；错题第二天重做。</li>
</ol>
<h3 class="sec">进度表</h3>
<table class="grid"><tr><th style="width:62px">天</th><th style="width:66px">科目</th><th>主题</th><th style="width:44px">答案</th><th style="width:70px">完成日期</th><th style="width:58px">得分</th></tr>{rows}</table>
<p class="note" style="margin-top:6px">符号与常数按 IEB Grade 11 data sheet：g = 9,8 m·s⁻²；运动方程按 2026 年测验所附公式表用 u（初速度）、v（末速度），旧写法 u、v 意思相同。小数点按考卷习惯写作逗号（9,8 = 9.8）。题目均为原创练习题。</p>
<p class="note">后续计划：Grade 11 下半年新主题，以及 Grade 8–10 基础和 Grade 12 内容，将陆续补充。</p>
</section>"""
    return page("Grade 11 Physical Sciences 每日一练", body, "", "", bar("", [("🧮 公式总表", "formulas.html"), ("📖 必背定义", "definitions.html")]))


def formulas_page():
    phys_const = [("重力加速度 Acceleration due to gravity", "g", "9,8 m·s⁻²"), ("光速 Speed of light", "c", "3,0 × 10⁸ m·s⁻¹"),
                  ("万有引力常量 Gravitational constant", "G", "6,67 × 10⁻¹¹ N·m²·kg⁻²"), ("库仑常量 Coulomb’s constant", "k", "9,0 × 10⁹ N·m²·C⁻²"),
                  ("电子电荷 Charge on electron", "e", "−1,6 × 10⁻¹⁹ C"), ("电子质量 Electron mass", "mₑ", "9,11 × 10⁻³¹ kg")]
    chem_const = [("阿伏伽德罗常数 Avogadro’s constant", "N<sub>A</sub>", "6,02 × 10²³ mol⁻¹"), ("摩尔气体常数 Molar gas constant", "R", "8,31 J·K⁻¹·mol⁻¹"),
                  ("STP 摩尔气体体积 Molar gas volume at STP", "V<sub>m</sub>", "22,4 dm³·mol⁻¹"), ("标准压强 Standard pressure", "p<sup>θ</sup>", "1,013 × 10⁵ Pa"),
                  ("标准温度 Standard temperature", "T<sup>θ</sup>", "273 K")]
    tbl = lambda rows: ('<table class="grid"><tr><th>名称</th><th style="width:60px">符号</th><th style="width:190px">数值</th></tr>'
                        + "".join(f"<tr><td>{a}</td><td>{M(b)}</td><td>{c}</td></tr>" for a, b, c in rows) + "</table>")
    sheet = lambda rows: ('<table class="grid"><tr><th style="width:110px">主题</th><th>公式</th></tr>'
                          + "".join(f"<tr><td>{a}</td><td>{'　　'.join(M(x) for x in b)}</td></tr>" for a, b in rows) + "</table>")
    phys_on = [("运动 Motion", ["v = u + aΔt", "Δx = uΔt + ½aΔt²", "v² = u² + 2aΔx", "Δx = ((v + u)/2)Δt"]),
               ("力 Force", ["F<sub>net</sub> = ma", "F<sub>g</sub> = mg", "μ<sub>s</sub> = f<sub>s(max)</sub>/N", "μ<sub>k</sub> = f<sub>k</sub>/N"]),
               ("引力与电场", ["F = Gm₁m₂/r²", "g = GM/r²", "F = kQ₁Q₂/r²", "E = F/q", "E = kQ/r²"]),
               ("电路 Circuits", ["I = Q/Δt", "V = W/q", "R = V/I", "emf = I(R + r)", "R<sub>s</sub> = R₁ + R₂", "1/R<sub>p</sub> = 1/R₁ + 1/R₂"]),
               ("功率与能量", ["P = W/Δt", "W = PΔt", "P = VI = I²R = V²/R", "W = VIΔt = I²RΔt = V²Δt/R", "E<sub>k</sub> = ½mv²", "E<sub>p</sub> = mgh"]),
               ("电磁 Electrodynamics", ["Φ = BA cosθ", "emf = −NΔΦ/Δt", "V<sub>s</sub>/V<sub>p</sub> = N<sub>s</sub>/N<sub>p</sub>", "V<sub>p</sub>I<sub>p</sub> = V<sub>s</sub>I<sub>s</sub>"])]
    phys_off = [("矢量分解", ["F<sub>x</sub> = F cosθ", "F<sub>y</sub> = F sinθ", "R² = x² + y²"]),
                ("斜面", ["w<sub>∥</sub> = mg sinθ", "w<sub>⊥</sub> = mg cosθ = N"]),
                ("电梯", ["N − mg = ma（向上为正）"]),
                ("电荷", ["Q = ne", "Q<sub>new</sub> = (Q₁ + Q₂)/2"]),
                ("内阻", ["V<sub>端</sub> = emf − Ir", "lost volts = Ir"]),
                ("电磁", ["磁通链 = NΦ", "1 cm² = 10⁻⁴ m²"]),
                ("比例法", ["F₂ = F₁(r₁/r₂)²", "零场点 kQ₁/x² = kQ₂/(d − x)²"]),
                ("单位换算", ["km·h⁻¹ ÷ 3,6 = m·s⁻¹", "1 kWh = 3,6 × 10⁶ J"])]
    chem_f = [("摩尔", ["n = m/M", "N = nN<sub>A</sub>", "n = V/V<sub>m</sub>"]), ("溶液", ["c = n/V", "c₁V₁ = c₂V₂"]),
              ("气体", ["p₁V₁/T₁ = p₂V₂/T₂", "pV = nRT", "T(K) = θ(°C) + 273"]), ("能量", ["ΔH = Σ断键 − Σ成键", "ΔH = H<sub>P</sub> − H<sub>R</sub>"]),
              ("产率与纯度", ["% yield = 实际/理论 × 100", "% purity = m<sub>纯</sub>/m<sub>样品</sub> × 100"])]
    body = f"""<section class="sheet">
<div class="hd"><span class="day">公式总表</span><span class="t">Physics P1</span><span class="sub">对照学校 Grade 11 data sheet</span></div>
<h3 class="sec">物理常数 Physical constants</h3>{tbl(phys_const)}
<h3 class="sec">考试公式表上有的公式</h3>{sheet(phys_on)}<p class="note">运动方程按 2026 年 8 月测验所附公式表写作 u（初速度）、v（末速度）；2022 年卷所附旧表写作 v<sub>i</sub>、v<sub>f</sub>，意思相同。</p>
<h3 class="sec" style="border-color:#dc2626">⚠ 公式表上没有、必须自己记住的</h3>{sheet(phys_off)}
<div class="foot"><span>{SITE} · 公式总表</span><span>物理</span></div></section>
<section class="sheet chem">
<div class="hd"><span class="day">公式总表</span><span class="t">Chemistry P2</span><span class="sub">IEB 常用数值</span></div>
<h3 class="sec">化学常数</h3>{tbl(chem_const)}
<h3 class="sec">化学计算公式</h3>{sheet(chem_f)}
<p class="note" style="margin-top:6px">说明：物理部分逐项核对了学校 Grade 11 考卷所附的 data sheet。化学 data sheet 不在已扫描的资料里，上表按 IEB 常用数值整理，以考试实际发的表为准。</p>
<h3 class="sec">单位速查</h3>
<table class="grid"><tr><th>换算</th><th>方法</th></tr>
<tr><td>cm³ → dm³</td><td>÷ 1 000</td></tr><tr><td>dm³ → m³</td><td>÷ 1 000</td></tr><tr><td>kPa → Pa</td><td>× 1 000</td></tr>
<tr><td>°C → K</td><td>+ 273</td></tr><tr><td>μ（micro）/ n（nano）</td><td>× 10⁻⁶ / × 10⁻⁹</td></tr><tr><td>g → kg</td><td>÷ 1 000</td></tr></table>
<div class="foot"><span>{SITE} · 公式总表</span><span>化学</span></div></section>"""
    return page("公式总表 · Grade 11 Physical Sciences", body, "", "", bar("", [("📖 必背定义", "definitions.html")]))


def definitions_page():
    out = ""
    for title, group, cls in (("物理 P1", PHYS + PHYS_EXTRA, ""), ("化学 P2", CHEM, "chem")):
        rows = ""
        seen = set()
        for d in group:
            for en, zh, df in d["defs"]:
                if en in seen:
                    continue
                seen.add(en)
                rows += f'<tr><td><b>{en}</b><br>{zh}</td><td style="font-family:Georgia,serif">{df}</td><td style="width:22px"></td></tr>'
        out += (f'<section class="sheet flow {cls}"><div class="hd"><span class="day">必背定义</span><span class="t">{title}</span>'
                f'<span class="sub">遮住右栏 → 说出定义 → 对照 → 在最后一栏打 ✓</span></div>'
                f'<table class="grid" style="font-size:12.2px"><tr><th style="width:150px">术语</th><th>定义（考试英文原句风格）</th><th>✓</th></tr>{rows}</table>'
                f'<div class="foot"><span>{SITE} · 必背定义</span><span>{title}</span></div></section>')
    return page("必背定义 · Grade 11 Physical Sciences", out, "", "", bar("", [("🧮 公式总表", "formulas.html")]))


def w(rel_path, html):
    p = os.path.join(ROOT, rel_path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(html)


def main():
    w("index.html", index_page())
    w("formulas.html", formulas_page())
    w("definitions.html", definitions_page())
    for i, d in enumerate(DAYS):
        w(f"days/d{i + 1:02d}.html", day_page(i, d))
        w(f"answers/a{i + 1:02d}.html", answer_page(i, d))
    print(f"built {N} days")


if __name__ == "__main__":
    main()
