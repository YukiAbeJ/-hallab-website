import os, sys
sys.stdout.reconfigure(encoding='utf-8')

BASE = "C:/Users/Abe_Yuki/Desktop/hallab-website"

FONT = '<link rel="preconnect" href="https://fonts.googleapis.com">\n  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&family=Noto+Serif+JP:wght@400;500;700&family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400;1,600&family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&display=swap" rel="stylesheet">'

SVG = """<svg class="logo-mark" viewBox="0 0 56 40" fill="none" aria-hidden="true">
      <path d="M4 36 Q28 4 52 36" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"/>
      <circle cx="4"  cy="36" r="3.5" fill="currentColor"/>
      <circle cx="52" cy="36" r="3.5" fill="currentColor"/>
      <circle cx="28" cy="6"  r="2.5" fill="currentColor"/>
    </svg>"""

PAGES = [
    ("index.html#greeting", "index", "ご挨拶"),
    ("about.html", "about", "私たちについて"),
    ("services.html", "services", "私たちの取組"),
    ("achievements.html", "achievements", "実績"),
    ("news.html", "news", "お知らせ"),
    ("company.html", "company", "法人情報"),
]

def nav(prefix, active):
    links = ""
    for href, key, label in PAGES:
        ac = ' class="active"' if active == key else ""
        links += f'      <a href="{prefix}{href}"{ac}>{label}</a>\n'
    overlay = ""
    for href, key, label in PAGES:
        overlay += f'  <a href="{prefix}{href}">{label}</a>\n'
    return f"""<nav class="nav" id="nav" role="navigation">
  <a href="{prefix}index.html" class="logo">
    {SVG}
    <div class="logo-text">
      <span class="logo-name">HAL Lab.</span>
      <span class="logo-sub">Healthy Ageing &amp; Longevity Laboratory</span>
    </div>
  </a>
  <div class="nav-links">
{links}    <a href="#" class="nav-login">Login</a>
  </div>
  <button class="hamburger" aria-label="メニューを開く" aria-expanded="false" aria-controls="nav-overlay">
    <span></span><span></span><span></span>
  </button>
</nav>
<div class="nav-overlay" id="nav-overlay" role="dialog" aria-hidden="true">
{overlay}  <div class="nav-overlay-line" aria-hidden="true"></div>
  <a href="#" class="nav-login">Login</a>
</div>"""

def footer(prefix):
    return f"""<footer class="footer" role="contentinfo">
  <div class="footer-inner">
    <div>
      <a href="{prefix}index.html" class="logo logo-footer">
        {SVG}
        <div class="logo-text">
          <span class="logo-name">HAL Lab.</span>
          <span class="logo-sub">Healthy Ageing &amp; Longevity Laboratory</span>
        </div>
      </a>
      <p class="footer-tagline">今日も「生きる」を支えていきます</p>
    </div>
    <div>
      <div class="footer-nav-title">NAVIGATION</div>
      <nav class="footer-links">
        <a href="{prefix}index.html#greeting">ご挨拶</a>
        <a href="{prefix}about.html">私たちについて</a>
        <a href="{prefix}services.html">私たちの取組</a>
        <a href="{prefix}achievements.html">実績</a>
        <a href="{prefix}news.html">お知らせ</a>
        <a href="{prefix}company.html">法人情報</a>
      </nav>
    </div>
    <div>
      <div class="footer-nav-title">MEMBERS</div>
      <nav class="footer-links">
        <a href="{prefix}members/abe-yuki.html">阿部 祐樹</a>
        <a href="{prefix}members/itagaki-atsunori.html">板垣 篤典</a>
        <a href="{prefix}members/kondo-ikue.html">近藤 郁江</a>
        <a href="{prefix}members/kimura-yosuke.html">木村 鷹介</a>
        <a href="{prefix}members/imagawa-norie.html">今川 記恵</a>
        <a href="{prefix}members/satoh-toshimi.html">佐藤 聡見</a>
        <a href="{prefix}members/kakehi-tomohiro.html">筧 智裕</a>
      </nav>
    </div>
    <div class="footer-address">
      <strong>ADDRESS</strong>
      〒107-0061<br>東京都港区北青山<br>一丁目3番1号<br>アールキューブ青山3階<br><br>設立：2025年4月1日
    </div>
  </div>
  <div class="footer-bottom">
    <p class="footer-copy">&copy; 2025 一般社団法人 HAL Lab. All rights reserved.</p>
  </div>
</footer>"""

def wrap(title, desc, css, js, active, prefix, body):
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  {FONT}
  <link rel="stylesheet" href="{css}">
</head>
<body>
<a class="skip-link" href="#main">本文へスキップ</a>
{nav(prefix, active)}
<main id="main">
{body}
</main>
{footer(prefix)}
<script src="{js}"></script>
</body>
</html>"""

# ============================================================
# about.html
# ============================================================
about_body = """  <div class="page-hero">
    <div class="page-hero-inner">
      <span class="sec-label reveal">About Us</span>
      <h1 class="page-hero-en reveal d1">私たちについて</h1>
      <div class="sec-rule reveal d2"></div>
      <p class="page-hero-desc reveal d3">私たちは、予防・医療・介護のエキスパート集団であり、東京都立大学発のスタートアップです。</p>
    </div>
  </div>

  <section class="section section--dark">
    <div class="container">
      <div class="reveal"><span class="sec-label">Who we are</span><h2 class="sec-title">私たちの想い</h2><div class="sec-rule"></div></div>
      <div class="reveal d1" style="max-width:720px;display:flex;flex-direction:column;gap:1.2rem;font-size:clamp(0.82rem,1.8vw,0.95rem);color:var(--text-2);line-height:2.2;letter-spacing:0.06em;margin-top:2rem;">
        <p>私たちは、大学・研究機関、医療機関に所属し、臨床・教育・研究・社会実装の経験が豊富な研究者、臨床家らから構成される専門家集団です。</p>
        <p>一次予防から医療、介護まで人々の生活を支援してきたリハビリテーションの専門家集団による人々の「健康づくり、予防、生活支援」に係る新たな取組みです。</p>
        <p>科学的根拠に基づく実践と地域との連携により、すべての人が健やかに、そして長く「生きる」を享受できる社会の実現を目指します。</p>
      </div>
    </div>
  </section>

  <div class="sec-divider"></div>

  <section class="section section--dark">
    <div class="container">
      <div class="reveal"><span class="sec-label">Representative Director</span><h2 class="sec-title-en">代表理事</h2><div class="sec-rule"></div></div>
      <div class="mt-2">
        <a href="members/abe-yuki.html" class="rep-card reveal d1">
          <div class="rep-avatar">AY</div>
          <div><div class="rep-tag">代表理事 / Representative Director</div><div class="rep-name-ja">阿部 祐樹</div><div class="rep-name-en">Abe Yuki &ensp;PT, MSc</div><div class="rep-affil">株式会社JDSC DXストラテジー Mgr. &nbsp;/&nbsp; DX・AXコンサルタント &nbsp;/&nbsp; 理学療法士<br>フレイル対策コンソーシアム &nbsp;/&nbsp; 日本がん治療・研究機構 外部研究員</div></div>
          <div class="rep-arrow" aria-hidden="true">→</div>
        </a>
      </div>
    </div>
  </section>

  <div class="sec-divider"></div>

  <section class="section section--dark">
    <div class="container">
      <div class="reveal"><span class="sec-label">Directors</span><h2 class="sec-title-en">理事</h2><div class="sec-rule"></div></div>
      <div class="team-grid mt-2">
        <a href="members/itagaki-atsunori.html" class="team-card reveal d1"><div class="avatar">IA</div><div><div class="card-role">Director</div><div class="card-name-ja">板垣 篤典</div><div class="card-name-en">Itagaki Atsunori, Ph.D.</div><div class="card-affil">東京都立大学 健康福祉学部 助教</div><div class="card-cert">PT / 博士（障害科学）/ 認定PT（循環）</div></div></a>
        <a href="members/kondo-ikue.html" class="team-card reveal d2"><div class="avatar">KI</div><div><div class="card-role">Director</div><div class="card-name-ja">近藤 郁江</div><div class="card-name-en">Kondo Ikue, MSc</div><div class="card-affil">一般社団法人仁生社 江戸川病院<br>東京都立大学 研究員</div><div class="card-cert">ST / 認定ST（失語・高次脳機能障害）/ 公認心理士</div></div></a>
        <a href="members/kimura-yosuke.html" class="team-card reveal d3"><div class="avatar">KY</div><div><div class="card-role">Director</div><div class="card-name-ja">木村 鷹介</div><div class="card-name-en">Kimura Yosuke, Ph.D.</div><div class="card-affil">東洋大学 生命科学部 生命医工学科 准教授</div><div class="card-cert">PT / 博士（リハビリテーション科学）/ 専門PT（神経系）</div></div></a>
        <a href="members/imagawa-norie.html" class="team-card reveal d1"><div class="avatar">IN</div><div><div class="card-role">Director</div><div class="card-name-ja">今川 記恵</div><div class="card-name-en">Imagawa Norie, Ph.D.</div><div class="card-affil">県立広島大学 保健福祉学部 助教</div><div class="card-cert">ST / 博士 / 聴覚障害・人工内耳専門</div></div></a>
        <a href="members/satoh-toshimi.html" class="team-card reveal d2"><div class="avatar">ST</div><div><div class="card-role">Director</div><div class="card-name-ja">佐藤 聡見</div><div class="card-name-en">Satoh Toshimi, Ph.D.</div><div class="card-affil">福島県立医科大学 保健科学部 講師</div><div class="card-cert">PT / 博士（障害科学）/ 専門PT（心血管）</div></div></a>
        <a href="members/kakehi-tomohiro.html" class="team-card reveal d3"><div class="avatar">KT</div><div><div class="card-role">Director</div><div class="card-name-ja">筧 智裕</div><div class="card-name-en">Kakehi Tomohiro, Ph.D.</div><div class="card-affil">国際医療福祉大学 成田保健医療学部 講師</div><div class="card-cert">OT / 博士（医学）/ 認定OT / 心臓リハ指導士</div></div></a>
      </div>
    </div>
  </section>

  <div class="sec-divider"></div>

  <section class="section section--dark">
    <div class="container">
      <div class="reveal"><span class="sec-label">Advisors</span><h2 class="sec-title-en">アドバイザー</h2><div class="sec-rule"></div></div>
      <div class="advisor-row">
        <div class="advisor-card reveal d1"><div class="advisor-avatar">SM</div><div><div class="advisor-name-ja">鈴木 瑞恵</div><div class="advisor-name-en">Suzuki Mizue, Ph.D.</div><div class="advisor-cert">ST, Ph.D.</div></div></div>
        <div class="advisor-card reveal d2"><div class="advisor-avatar">SS</div><div><div class="advisor-name-ja">澤野 晋之介</div><div class="advisor-name-en">Sawano Sinnosuke, Ph.D.</div><div class="advisor-cert">MD, Ph.D.</div></div></div>
      </div>
    </div>
  </section>"""

with open(f"{BASE}/about.html", "w", encoding="utf-8") as f:
    f.write(wrap("私たちについて — HAL Lab.", "HAL Lab.メンバー紹介。予防・医療・介護のエキスパート集団。", "css/style.css", "js/main.js", "about", "", about_body))
print("about.html OK")

# ============================================================
# news.html
# ============================================================
news_body = """  <div class="page-hero"><div class="page-hero-inner">
    <span class="sec-label reveal">News</span><h1 class="page-hero-en reveal d1">お知らせ</h1><div class="sec-rule reveal d2"></div>
  </div></div>
  <section class="section section--dark">
    <div class="container container--text" style="margin:0 auto;">
      <div class="news-list reveal">
        <div class="news-row">
          <span class="news-date">2025.04.01</span>
          <div><span class="news-badge">法人設立</span><p class="news-title">一般社団法人HAL Lab.（Healthy Aging &amp; Longevity Laboratory / ヘルシーエイジング・長寿研究所）を設立しました。<br><span style="font-size:0.8rem;color:var(--text-3);display:block;margin-top:0.4rem;">所在地：東京都港区北青山一丁目3番1号 アールキューブ青山3階</span></p></div>
        </div>
      </div>
      <div class="mt-4 reveal" style="text-align:center;padding:3rem 2rem;background:var(--bg-card);border:1px solid var(--line-sub);border-radius:var(--radius-md);">
        <p style="font-size:0.88rem;color:var(--text-2);letter-spacing:0.06em;line-height:2;">今後の活動・お知らせは随時こちらに掲載いたします。</p>
      </div>
    </div>
  </section>"""

with open(f"{BASE}/news.html", "w", encoding="utf-8") as f:
    f.write(wrap("お知らせ — HAL Lab.", "一般社団法人HAL Lab.からのお知らせ。", "css/style.css", "js/main.js", "news", "", news_body))
print("news.html OK")

# ============================================================
# company.html
# ============================================================
company_body = """  <div class="page-hero"><div class="page-hero-inner">
    <span class="sec-label reveal">Organization</span><h1 class="page-hero-en reveal d1">法人情報</h1><div class="sec-rule reveal d2"></div>
  </div></div>
  <section class="section section--dark">
    <div class="container container--text" style="margin:0 auto;">
      <div class="reveal"><span class="sec-label">Organization Info</span><h2 class="sec-title-en">法人概要</h2><div class="sec-rule"></div></div>
      <div class="mt-2 reveal d1">
        <table class="org-table">
          <tr><th>法人名</th><td>一般社団法人 HAL Lab.<br><span style="font-size:0.78rem;color:var(--text-3);">Health Aging &amp; Longevity Laboratory（ヘルシーエイジング・長寿研究所）</span></td></tr>
          <tr><th>設立</th><td>2025年4月1日</td></tr>
          <tr><th>所在地</th><td>〒107-0061<br>東京都港区北青山一丁目3番1号<br>アールキューブ青山3階</td></tr>
          <tr><th>代表理事</th><td>阿部 祐樹（PT, MSc）</td></tr>
          <tr><th>理事</th><td>板垣 篤典（PT, Ph.D.）<br>近藤 郁江（ST, MSc）<br>木村 鷹介（PT, Ph.D.）<br>今川 記恵（ST, Ph.D.）<br>佐藤 聡見（PT, Ph.D.）<br>筧 智裕（OT, Ph.D.）</td></tr>
          <tr><th>アドバイザー</th><td>鈴木 瑞恵（ST, Ph.D.）<br>澤野 晋之介（MD, Ph.D.）</td></tr>
          <tr><th>事業内容</th><td>健康づくり・予防事業支援 / 地域リハビリテーション・生活支援<br>医療・介護リハビリテーション支援 / 研究・研究開発支援<br>教育・人材育成支援</td></tr>
        </table>
      </div>
      <div class="mt-4 reveal">
        <span class="sec-label">Contact</span><h2 class="sec-title-en">お問い合わせ</h2><div class="sec-rule"></div>
        <div style="background:var(--bg-card);border:1px solid var(--line-sub);border-radius:var(--radius-md);padding:2rem 2.5rem;margin-top:1.5rem;">
          <p style="font-size:0.88rem;color:var(--text-2);line-height:2.2;letter-spacing:0.05em;margin-bottom:1.5rem;">各事業へのご相談・お問い合わせは下記よりお気軽にご連絡ください。自治体・医療機関・研究機関・企業からのご相談も歓迎いたします。</p>
          <table class="org-table">
            <tr><th>受付時間</th><td>平日 9:00〜18:00</td></tr>
            <tr><th>備考</th><td style="font-size:0.82rem;color:var(--text-2);">※ 内容によっては回答にお時間をいただく場合があります。</td></tr>
          </table>
        </div>
      </div>
    </div>
  </section>"""

with open(f"{BASE}/company.html", "w", encoding="utf-8") as f:
    f.write(wrap("法人情報 — HAL Lab.", "一般社団法人HAL Lab.の法人情報・お問い合わせ。", "css/style.css", "js/main.js", "company", "", company_body))
print("company.html OK")

print("All done.")
