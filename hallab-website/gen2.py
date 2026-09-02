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
# services.html
# ============================================================
services_body = """  <div class="page-hero"><div class="page-hero-inner">
    <span class="sec-label reveal">Services</span>
    <h1 class="page-hero-en reveal d1">私たちの取組</h1>
    <div class="sec-rule reveal d2"></div>
    <p class="page-hero-desc reveal d3">健康づくり・予防から医療支援、研究、教育まで。<br>科学的根拠に基づいた包括的なアプローチで地域の健康を支えます。</p>
  </div></div>

  <section class="section section--dark">
    <div class="container">
      <div class="services-grid">

        <div class="service-card reveal d1" id="health-promotion">
          <div class="service-num">01</div>
          <div class="service-title-en">Health Promotion / Prevention</div>
          <div class="service-title-ja">健康づくり・予防</div>
          <div class="service-rule"></div>
          <div class="service-sub-title">1. 介護予防事業支援</div>
          <ul class="service-list">
            <li class="service-item">高齢者健診・体力測定会事業</li>
            <li class="service-item">データ分析業務・事業成果検証</li>
            <li class="service-item">介護予防事業計画策定支援</li>
            <li class="service-item">講師派遣</li>
            <li class="service-item">その他の関連業務支援</li>
          </ul>
          <div class="service-note">事業例）総合事業（介護予防把握事業・一般介護予防事業 等）</div>
          <div class="service-sub-title" style="margin-top:1.25rem;">2. 保健事業支援</div>
          <ul class="service-list">
            <li class="service-item">事業計画策定支援</li>
            <li class="service-item">データヘルス計画策定</li>
            <li class="service-item">ハイリスクアプローチ</li>
            <li class="service-item">ポピュレーションアプローチ</li>
          </ul>
          <div class="service-note">事業例）高齢者の保健事業と介護予防の一体的実施 / 健康教育・健康相談 / ICTを活用した介護予防事業 / PHR活用事業 等</div>
        </div>

        <div class="service-card reveal d2" id="life-support">
          <div class="service-num">02</div>
          <div class="service-title-en">Life Support</div>
          <div class="service-title-ja">生活支援</div>
          <div class="service-rule"></div>
          <div class="service-sub-title">1. 地域リハビリテーション</div>
          <ul class="service-list">
            <li class="service-item">体力測定事業（身体機能測定・オーラルフレイル判定・認知機能測定等）</li>
            <li class="service-item">事業策定支援</li>
            <li class="service-item">介護予防リーダー育成</li>
            <li class="service-item">講師派遣</li>
          </ul>
          <div class="service-note">※ 自治体と総合事業の経験も豊富なメンバーが在籍しています。お気軽にご相談ください。<br><br>事業例）総合事業（介護予防事業）/ 日常生活支援事業 / 通所型サービス事業支援 / 地域ケア会議</div>
          <div class="service-sub-title" style="margin-top:1.25rem;">2. 医学的リハビリテーション支援</div>
          <ul class="service-list">
            <li class="service-item">高次脳機能障害者支援</li>
            <li class="service-item">医学的リハ終了者支援</li>
            <li class="service-item">遠隔リハ（心臓・呼吸・神経筋疾患・生活習慣病 等）</li>
          </ul>
          <div class="service-note">※ 遠隔診療・リハビリテーションにも取組んでいるメンバーが在籍しています。</div>
        </div>

        <div class="service-card reveal d1" id="research">
          <div class="service-num">03</div>
          <div class="service-title-en">Research</div>
          <div class="service-title-ja">研究</div>
          <div class="service-rule"></div>
          <div class="service-sub-title">1. ヒトの健康増進・予防</div>
          <ul class="service-list">
            <li class="service-item">フレイル / オーラルフレイル・口腔嚥下</li>
            <li class="service-item">サルコペニア</li>
            <li class="service-item">ヘルスリテラシー</li>
            <li class="service-item">軽度認知障害（MCI）・認知症</li>
            <li class="service-item">介護予防・通いの場 / 重症化予防</li>
            <li class="service-item">障碍者スポーツ / RWD分析</li>
          </ul>
          <div class="service-sub-title" style="margin-top:1.25rem;">2. 研究開発</div>
          <ul class="service-list">
            <li class="service-item">生体センシング / モニタリング</li>
            <li class="service-item">PHR / デジタルヘルス</li>
            <li class="service-item">生体工学・バイオメカニクス</li>
            <li class="service-item">リハビリテーション・生活支援ロボティクス・Physical AI</li>
          </ul>
          <div class="service-note">※ 社会課題解決に資する研究・研究開発支援を推進しています。<br>※ AI・Physical AI開発については、研究・開発を専門とする企業のご紹介も可能です。</div>
        </div>

        <div class="service-card reveal d2" id="education">
          <div class="service-num">04</div>
          <div class="service-title-en">Education</div>
          <div class="service-title-ja">教育</div>
          <div class="service-rule"></div>
          <div class="service-sub-title">1. リハビリテーション専門職支援</div>
          <ul class="service-list">
            <li class="service-item">研究サポート</li>
            <li class="service-item">臨床サポート</li>
            <li class="service-item">新人教育サポート</li>
            <li class="service-item">講義</li>
            <li class="service-item">キャリア相談</li>
          </ul>
          <div class="service-sub-title" style="margin-top:1.25rem;">2. 学生支援</div>
          <ul class="service-list">
            <li class="service-item">講義</li>
            <li class="service-item">研究サポート</li>
            <li class="service-item">キャリア相談</li>
            <li class="service-item">在学中の地域リハ体験</li>
          </ul>
        </div>

      </div>

      <div class="mt-4 reveal" style="text-align:center;padding:3rem 2rem;background:var(--bg-card);border:1px solid var(--line-sub);border-radius:var(--radius-md);">
        <span class="sec-label" style="display:block;text-align:center;margin-bottom:0.75rem;">Contact</span>
        <h2 class="sec-title-en" style="margin-bottom:0.5rem;">お気軽にご相談ください</h2>
        <p style="font-size:0.85rem;color:var(--text-2);margin-bottom:2rem;line-height:2;">各事業についてのご相談・お問い合わせはいつでも受け付けております。</p>
        <a href="company.html" class="btn btn-gold">法人情報・お問い合わせ →</a>
      </div>
    </div>
  </section>"""

with open(f"{BASE}/services.html", "w", encoding="utf-8") as f:
    f.write(wrap("私たちの取組 — HAL Lab.", "HAL Lab.の4つの事業領域：健康づくり・予防、生活支援、研究、教育。科学と実践で地域の健康未来を創造します。", "css/style.css", "js/main.js", "services", "", services_body))
print("services.html OK")

# ============================================================
# achievements.html
# ============================================================
achievements_body = """  <div class="page-hero"><div class="page-hero-inner">
    <span class="sec-label reveal">Achievements</span>
    <h1 class="page-hero-en reveal d1">実績</h1>
    <div class="sec-rule reveal d2"></div>
    <p class="page-hero-desc reveal d3">各メンバーが積み重ねてきた研究実績・受賞歴・特許・プロジェクトの一部をご紹介します。</p>
  </div></div>

  <section class="section section--dark" aria-labelledby="patent-title">
    <div class="container">
      <div class="reveal"><span class="sec-label">Patent</span><h2 class="sec-title-en" id="patent-title">特許</h2><div class="sec-rule"></div></div>
      <div class="mt-2 reveal d1">
        <div class="patent-block">
          <div class="patent-icon">📜</div>
          <div>
            <div class="patent-title">健診データ・レセプトデータ等によるフレイル判定・予測AI</div>
            <div class="patent-num">第7673921号（P7673921）</div>
            <div style="font-size:0.78rem;color:var(--text-3);margin-top:0.5rem;letter-spacing:0.04em;">発明者：阿部 祐樹（代表理事）</div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--dark" aria-labelledby="awards-title">
    <div class="container">
      <div class="reveal"><span class="sec-label">Awards</span><h2 class="sec-title-en" id="awards-title">受賞歴</h2><div class="sec-rule"></div></div>

      <div class="mt-3 reveal">
        <p style="font-size:0.72rem;letter-spacing:0.15em;color:var(--gold);margin-bottom:1rem;">板垣 篤典 / Itagaki Atsunori</p>
        <div class="award-list">
          <div class="award-row"><span class="award-year">2023</span><span class="award-desc">第8回日本栄養・嚥下理学療法研究会学術集会 セレクション演題</span></div>
          <div class="award-row"><span class="award-year">2021</span><span class="award-desc">The 7th Asian Conference for Frailty and Sarcopenia (ACFS) Best Poster Award</span></div>
          <div class="award-row"><span class="award-year">2021</span><span class="award-desc">学長賞 研究部門, 青森県立保健大学</span></div>
          <div class="award-row"><span class="award-year">2018</span><span class="award-desc">第82回日本循環器学会 第8回コメディカル賞 最優秀賞</span></div>
          <div class="award-row"><span class="award-year">2017</span><span class="award-desc">Asia Western Pacific Region of World Confederation for Physical Therapy congress 2017 Third Place Award</span></div>
          <div class="award-row"><span class="award-year">2015</span><span class="award-desc">The 19th Annual Scientific Meeting of Japan Heart Failure Society Young Investigator's Award (YIA) 3 nominate</span></div>
          <div class="award-row"><span class="award-year">2013</span><span class="award-desc">第67回国立病院機構総合医学会 ベストポスター賞</span></div>
        </div>
      </div>

      <div style="height:1px;background:var(--line-sub);margin:2.5rem 0;"></div>

      <div class="reveal">
        <p style="font-size:0.72rem;letter-spacing:0.15em;color:var(--gold);margin-bottom:1rem;">木村 鷹介 / Kimura Yosuke</p>
        <div class="award-list">
          <div class="award-row"><span class="award-year">2025</span><span class="award-desc">第23回日本神経理学療法学会学術大会 奨励賞</span></div>
          <div class="award-row"><span class="award-year">2024</span><span class="award-desc">第26回日本運動疫学会 優秀演題賞</span></div>
          <div class="award-row"><span class="award-year">2023</span><span class="award-desc">第21回日本神経理学療法学会学術大会 最優秀賞</span></div>
          <div class="award-row"><span class="award-year">2023</span><span class="award-desc">第2回日本老年療法学会学術集会 大会長賞</span></div>
          <div class="award-row"><span class="award-year">2023</span><span class="award-desc">第9回日本栄養・嚥下理学療法学会学術大会 最優秀賞</span></div>
          <div class="award-row"><span class="award-year">2022</span><span class="award-desc">第1回日本老年療法学会学術集会 大会長賞</span></div>
          <div class="award-row"><span class="award-year">2021</span><span class="award-desc">Best poster award, The 7th Asian Conference for Frailty and Sarcopenia (ACFS 2021)</span></div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--dark" aria-labelledby="projects-title">
    <div class="container">
      <div class="reveal"><span class="sec-label">Projects &amp; Activities</span><h2 class="sec-title-en" id="projects-title">主なプロジェクト</h2><div class="sec-rule"></div></div>
      <div class="mt-2" style="display:grid;gap:1.25rem;">

        <div class="service-card reveal d1">
          <div class="service-num">01</div>
          <div class="service-title-en">高齢者体力測定会の開催</div>
          <div class="service-title-ja">地域リハビリテーション活動</div>
          <div class="service-rule"></div>
          <p style="font-size:0.82rem;color:var(--text-2);line-height:1.9;letter-spacing:0.04em;">創業メンバーによる研究チームを発足し、高齢者を対象とした体力測定会を開催。介護予防促進のための研究活動を継続的に実施しています。</p>
        </div>

        <div class="service-card reveal d2">
          <div class="service-num">02</div>
          <div class="service-title-en">電力データ×AIフレイル検知</div>
          <div class="service-title-ja">デジタルヘルス・DX事業</div>
          <div class="service-rule"></div>
          <p style="font-size:0.82rem;color:var(--text-2);line-height:1.9;letter-spacing:0.04em;">電力データとAIを活用したフレイル検知・MCI検知事業に参画。KDB・レセプトデータ等のRWD利活用によるAIデータ分析でフレイル特性分類にも取組んでいます。</p>
        </div>

        <div class="service-card reveal d1">
          <div class="service-num">03</div>
          <div class="service-title-en">東京2020オリンピック・パラリンピック</div>
          <div class="service-title-ja">車椅子バスケットボール日本代表 メディカルスタッフ</div>
          <div class="service-rule"></div>
          <p style="font-size:0.82rem;color:var(--text-2);line-height:1.9;letter-spacing:0.04em;">車椅子バスケットボール日本代表選手をメディカルスタッフとしてサポート。チームは銀メダルを獲得しました。</p>
        </div>

      </div>
    </div>
  </section>"""

with open(f"{BASE}/achievements.html", "w", encoding="utf-8") as f:
    f.write(wrap("実績 — HAL Lab.", "HAL Lab.の研究実績・受賞歴・特許情報。フレイル判定AI特許取得をはじめ、多数の学術的成果を有する専門家集団です。", "css/style.css", "js/main.js", "achievements", "", achievements_body))
print("achievements.html OK")

# ============================================================
# Member page helper
# ============================================================
def member_wrap(title, desc, initials, role_en, role_ja, name_ja, name_en, certs, affil, av_extra, body_sections):
    cert_items = "".join(f'            <span class="cert">{c}</span>\n' for c in certs)
    return wrap(
        title, desc,
        "../css/style.css", "../js/main.js",
        "about", "../",
        f"""  <div class="profile-header">
    <div class="profile-header-inner">
      <div class="profile-av{av_extra} reveal">{initials}</div>
      <div class="reveal d1">
        <div class="profile-role">{role_en} / {role_ja}</div>
        <h1 class="profile-name-ja">{name_ja}</h1>
        <p class="profile-name-en">{name_en}</p>
        <div class="cert-wrap">
{cert_items}        </div>
        <div class="profile-affil">{affil}</div>
      </div>
    </div>
  </div>

  <div class="profile-body">
    <div class="profile-grid">
{body_sections}    </div>
  </div>

  <div style="padding:0 var(--px) 3rem;max-width:var(--max-w);margin:0 auto;">
    <a href="../about.html" class="btn-back">← メンバー一覧に戻る</a>
  </div>"""
    )

# ============================================================
# abe-yuki.html
# ============================================================
abe_body = """      <div class="reveal">
        <div class="profile-sec-title">Areas of Expertise</div>
        <span class="profile-sec-ja">専門領域・研究テーマ</span>
        <div class="tag-wrap">
          <span class="tag">フレイル・介護予防</span>
          <span class="tag">保健事業支援</span>
          <span class="tag">予防理学療法</span>
          <span class="tag">地域リハビリテーション</span>
          <span class="tag">医学的リハビリテーション</span>
          <span class="tag">DX / AX</span>
          <span class="tag">新規事業開発（ヘルスケア領域）</span>
          <span class="tag">RWDデータ分析</span>
        </div>
      </div>

      <div class="reveal d1">
        <div class="profile-sec-title">Profile</div>
        <span class="profile-sec-ja">経歴</span>
        <div class="profile-text">
          <p>国立大学法人千葉大学医学部附属病院リハビリテーション科にて理学療法士としてキャリアをスタート。高度急性期医療にて、臨床・研究・教育等に従事。がん、ICU、NICU、糖尿病代謝内科など多くの診療科・疾患を対象に身体機能および動作・活動能力の維持向上、生活支援等に関わった。脳神経内科ではパーキンソン病（DBS）研究班として研究や院内プロジェクトにも参画。</p>
          <p>その後、地域の中核医療を担う医療法人の本部にてCommunity Based Rehabilitationに従事。通所リハなどの介護保険事業の立ち上げ、自治体とも連携のもと一般介護予防事業、通所型サービス、地域ケア会議、地域リハ支援事業等に従事。</p>
          <p>東京2020オリンピック・パラリンピックではメディカルスタッフとして車椅子バスケットボール日本代表選手をサポート（銀メダル獲得）。</p>
          <p>キャンサースキャンでは、マーケティングと公衆衛生を組み合わせた高齢者に特化した健康づくり・予防に係る事業を開発。ナッジ理論を活用したTVCM作製プロジェクトもリード。KDB・レセプトデータ等のRWD利活用によるAIデータ分析によるフレイル検知と特性分類に取組む。</p>
          <p>現在は東京大学発のAIスタートアップにて、DX/AXコンサルタントとして予防・医療・介護領域におけるヘルスケア領域を中心としたDX/AXや健康増進・予防医学・介護予防に係る新たな事業創発等にチャレンジしている。電力データAIフレイル検知・MCI検知、PHR、IoTによる健康状態可視化、医療情報連携基盤構築等に従事。国会議員・内閣府および中央省庁との折衝にも対応。</p>
        </div>
      </div>

      <div class="reveal">
        <div class="profile-sec-title">Projects &amp; Activities</div>
        <span class="profile-sec-ja">プロジェクト・活動</span>
        <div class="profile-text">
          <p>一般社団法人HAL Lab.を創業。健康づくり・予防に係る取組推進のためアカデミアとの研究チームを発足し、本法人を設立するに至った。電力データAIフレイル検知に係る事業拡大にも貢献。他、電力データ利活用によるMCI検知、PHR、IoTによる健康状態可視化、POSデータ利活用による新規事業開発、DX人材育成事業、医療情報連携基盤構築に係る取組などに従事している。</p>
        </div>
      </div>

      <div class="reveal d1">
        <div class="profile-sec-title">Patent</div>
        <span class="profile-sec-ja">特許</span>
        <div class="patent-block">
          <div class="patent-icon">📜</div>
          <div>
            <div class="patent-title">健診データ・レセプトデータ等によるフレイル判定・予測AI</div>
            <div class="patent-num">第7673921号（P7673921）</div>
          </div>
        </div>
      </div>

      <div class="reveal">
        <div class="profile-sec-title">Professional Memberships</div>
        <span class="profile-sec-ja">所属学会・団体</span>
        <div class="tag-wrap">
          <span class="tag">フレイル対策コンソーシアム</span>
          <span class="tag">日本がん治療・研究機構 外部研究員</span>
          <span class="tag">日本理学療法士協会</span>
          <span class="tag">日本臨床神経整理学会</span>
        </div>
      </div>
"""

with open(f"{BASE}/members/abe-yuki.html", "w", encoding="utf-8") as f:
    f.write(member_wrap(
        "阿部 祐樹 — HAL Lab.",
        "阿部 祐樹（Abe Yuki）。HAL Lab.代表理事。理学療法士・DX/AXコンサルタント。株式会社JDSC DXストラテジーマネージャー。",
        "AY", "Representative Director", "代表理事",
        "阿部 祐樹", "Abe Yuki &nbsp;PT, MSc",
        ["理学療法士", "修士（保健科学）", "DX/AX コンサルタント"],
        "株式会社JDSC DXストラテジー マネージャー<br>フレイル対策コンソーシアム<br>日本がん治療・研究機構 外部研究員<br>日本理学療法士協会 / 日本臨床神経整理学会",
        " profile-av--rep", abe_body
    ))
print("abe-yuki.html OK")

# ============================================================
# itagaki-atsunori.html
# ============================================================
itagaki_body = """      <div class="reveal">
        <div class="profile-sec-title">Areas of Expertise</div>
        <span class="profile-sec-ja">専門領域・研究テーマ</span>
        <div class="tag-wrap">
          <span class="tag">内部障害</span>
          <span class="tag">老年学</span>
          <span class="tag">健康科学</span>
          <span class="tag">理学療法学</span>
          <span class="tag">介護予防</span>
        </div>
      </div>

      <div class="reveal d1">
        <div class="profile-sec-title">Profile</div>
        <span class="profile-sec-ja">経歴</span>
        <div class="profile-text">
          <p>2011年 理学療法士免許取得。独立行政法人国立病院機構 水戸医療センターにて3次救急・ドクターヘリ基地病院での急性期分野のリハビリテーションに従事。</p>
          <p>2014年 公益財団法人心臓血管研究所にて循環器疾患に特化したリハビリテーションと研究に携わる。</p>
          <p>2020年 東北大学大学院医学系研究科障害科学専攻博士後期課程修了。青森県立保健大学 助教に着任。</p>
          <p>2023年 東京都立大学 助教。</p>
          <p>2025年 一般社団法人HAL Lab.を共同起業。</p>
        </div>
      </div>

      <div class="reveal">
        <div class="profile-sec-title">Awards</div>
        <span class="profile-sec-ja">受賞歴</span>
        <div class="award-list">
          <div class="award-row"><span class="award-year">2023</span><span class="award-desc">第8回日本栄養・嚥下理学療法研究会学術集会 セレクション演題</span></div>
          <div class="award-row"><span class="award-year">2021</span><span class="award-desc">The 7th Asian Conference for Frailty and Sarcopenia (ACFS) Best Poster Award</span></div>
          <div class="award-row"><span class="award-year">2021</span><span class="award-desc">学長賞 研究部門, 青森県立保健大学</span></div>
          <div class="award-row"><span class="award-year">2018</span><span class="award-desc">第82回日本循環器学会 第8回コメディカル賞 最優秀賞</span></div>
          <div class="award-row"><span class="award-year">2017</span><span class="award-desc">Asia Western Pacific Region of World Confederation for Physical Therapy congress 2017 Third Place Award</span></div>
          <div class="award-row"><span class="award-year">2015</span><span class="award-desc">The 19th Annual Scientific Meeting of Japan Heart Failure Society Young Investigator's Award (YIA) 3 nominate</span></div>
          <div class="award-row"><span class="award-year">2013</span><span class="award-desc">第67回国立病院機構総合医学会 ベストポスター賞</span></div>
        </div>
      </div>
"""

with open(f"{BASE}/members/itagaki-atsunori.html", "w", encoding="utf-8") as f:
    f.write(member_wrap(
        "板垣 篤典 — HAL Lab.",
        "板垣 篤典（Itagaki Atsunori）。HAL Lab.理事。東京都立大学健康福祉学部助教。理学療法士・博士（障害科学）。",
        "IA", "Director", "理事",
        "板垣 篤典", "Itagaki Atsunori &nbsp;PT, Ph.D.",
        ["理学療法士", "博士（障害科学）", "認定PT（循環）", "心臓リハビリテーション指導士", "腎臓リハビリテーション指導士", "3学会合同呼吸療法認定士"],
        "東京都立大学 健康福祉学部 助教<br>Assistant Professor, Tokyo Metropolitan University",
        "", itagaki_body
    ))
print("itagaki-atsunori.html OK")

# ============================================================
# kondo-ikue.html
# ============================================================
kondo_body = """      <div class="reveal">
        <div class="profile-sec-title">Areas of Expertise</div>
        <span class="profile-sec-ja">専門領域・研究テーマ</span>
        <div class="tag-wrap">
          <span class="tag">失語症・高次脳機能障害</span>
          <span class="tag">認知症</span>
          <span class="tag">口腔・嚥下機能低下症</span>
          <span class="tag">オーラルフレイル</span>
          <span class="tag">地域包括ケア</span>
          <span class="tag">言語聴覚学</span>
          <span class="tag">介護予防</span>
        </div>
      </div>

      <div class="reveal d1">
        <div class="profile-sec-title">Profile</div>
        <span class="profile-sec-ja">経歴</span>
        <div class="profile-text">
          <p>北里大学を卒業後、江戸川病院リハビリテーション科にて言語聴覚士としてキャリアをスタート。江戸川病院の失語症に対する長期言語訓練を学び、臨床・研究・教育等に従事。失語症のある人とその家族に寄り添ったリハビリテーションを提供するとともに、就労支援も行っている。「実践！失語症のリハビリテーション」の出版にも協力。その他、認知症評価や家族指導も実施している。</p>
          <p>東京都立大学では客員研究員として地域在住高齢者を対象とした介護予防やフレイル予防に関わる研究活動を行っている。専門は認知症、オーラルフレイル。</p>
        </div>
      </div>

      <div class="reveal">
        <div class="profile-sec-title">Projects &amp; Activities</div>
        <span class="profile-sec-ja">プロジェクト・活動</span>
        <div class="profile-text">
          <p>一般社団法人HAL Lab.の創業メンバー。地元に恩返しをしたいという想いから、介護予防促進のための研究活動を開始。大学院時代の同期らと共に研究チームを発足し、高齢者を対象とした体力測定会を開催。普段は江戸川病院にて言語聴覚士として勤務し、東京都立大学客員研究員として、地域在住高齢者を対象としたオーラルフレイル・認知症予防のための研究活動も行っている。</p>
        </div>
      </div>

      <div class="reveal d1">
        <div class="profile-sec-title">Professional Memberships</div>
        <span class="profile-sec-ja">所属学会・団体</span>
        <div class="tag-wrap">
          <span class="tag">日本言語聴覚士協会 地域包括ケアシステム部</span>
          <span class="tag">日本高次脳機能学会</span>
          <span class="tag">日本老年療法学会 教育委員</span>
        </div>
      </div>
"""

with open(f"{BASE}/members/kondo-ikue.html", "w", encoding="utf-8") as f:
    f.write(member_wrap(
        "近藤 郁江 — HAL Lab.",
        "近藤 郁江（Kondo Ikue）。HAL Lab.理事。江戸川病院・東京都立大学研究員。言語聴覚士・認定ST（失語・高次脳機能障害）。",
        "KI", "Director", "理事",
        "近藤 郁江", "Kondo Ikue &nbsp;ST, MSc",
        ["言語聴覚士", "認定ST（失語・高次脳機能障害）", "公認心理士", "臨床神経心理士"],
        "一般社団法人仁生社 江戸川病院<br>東京都立大学 研究員（Researcher, Tokyo Metropolitan University）",
        "", kondo_body
    ))
print("kondo-ikue.html OK")

# ============================================================
# kimura-yosuke.html
# ============================================================
kimura_body = """      <div class="reveal">
        <div class="profile-sec-title">Areas of Expertise</div>
        <span class="profile-sec-ja">専門領域・研究テーマ</span>
        <div class="tag-wrap">
          <span class="tag">内部障害学</span>
          <span class="tag">老年学</span>
          <span class="tag">健康科学</span>
          <span class="tag">理学療法学</span>
          <span class="tag">介護予防</span>
          <span class="tag">デジタルヘルス</span>
          <span class="tag">身体活動量促進</span>
        </div>
      </div>

      <div class="reveal d1">
        <div class="profile-sec-title">Profile</div>
        <span class="profile-sec-ja">経歴</span>
        <div class="profile-text">
          <p>JCHO東京新宿メディカルセンターにて理学療法士としてキャリアをスタートし、脳卒中や大腿骨近位部骨折などの急性期・回復期患者に対するリハビリテーションに従事。臨床に携わる中で、自治体と連携した地域住民向けの介護予防体操の開発や普及活動にも取り組むなど、地域リハビリテーションにも積極的に関わる。</p>
          <p>臨床現場での課題をもとに筑波大学大学院に進学し、脳卒中患者の機能回復に関する研究で博士（リハビリテーション科学）の学位を取得。以降、大学教員として教育・研究に従事し、回復期脳卒中患者や地域在住高齢者を対象とした機能回復や重症化予防、身体活動量の向上に関する研究を推進。近年ではデジタルヘルス技術を活用した身体活動量促進の実践モデルの開発にも取り組んでいる。</p>
          <p>「理学療法ガイドライン第2版 フレイル理学療法ガイドライン」や「サルコペニア・フレイルの予防・改善に関するデジタルヘルスのためのガイドライン」作成にも参画し、科学的知見に基づいた実践指針の整備にも尽力している。</p>
          <p>研究・臨床・地域活動の三位一体による取り組みを通じて、高齢者や障害のある人々が住み慣れた地域で安心して暮らし続けられる社会の実現を目指している。</p>
        </div>
      </div>

      <div class="reveal">
        <div class="profile-sec-title">Awards</div>
        <span class="profile-sec-ja">受賞歴</span>
        <div class="award-list">
          <div class="award-row"><span class="award-year">2025</span><span class="award-desc">第23回日本神経理学療法学会学術大会 奨励賞</span></div>
          <div class="award-row"><span class="award-year">2024</span><span class="award-desc">第26回日本運動疫学会 優秀演題賞</span></div>
          <div class="award-row"><span class="award-year">2023</span><span class="award-desc">第21回日本神経理学療法学会学術大会 最優秀賞</span></div>
          <div class="award-row"><span class="award-year">2023</span><span class="award-desc">第2回日本老年療法学会学術集会 大会長賞</span></div>
          <div class="award-row"><span class="award-year">2023</span><span class="award-desc">第9回日本栄養・嚥下理学療法学会学術大会 最優秀賞</span></div>
          <div class="award-row"><span class="award-year">2022</span><span class="award-desc">第1回日本老年療法学会学術集会 大会長賞</span></div>
          <div class="award-row"><span class="award-year">2021</span><span class="award-desc">Best poster award, The 7th Asian Conference for Frailty and Sarcopenia (ACFS 2021)</span></div>
        </div>
      </div>

      <div class="reveal d1">
        <div class="profile-sec-title">Professional Memberships</div>
        <span class="profile-sec-ja">所属学会・団体</span>
        <div class="tag-wrap">
          <span class="tag">日本老年療法学会 監事</span>
          <span class="tag">日本神経理学療法学会 戦略的課題解決委員会</span>
          <span class="tag">日本栄養・嚥下理学療法学会 評議員</span>
        </div>
      </div>
"""

with open(f"{BASE}/members/kimura-yosuke.html", "w", encoding="utf-8") as f:
    f.write(member_wrap(
        "木村 鷹介 — HAL Lab.",
        "木村 鷹介（Kimura Yosuke）。HAL Lab.理事。東洋大学生命科学部准教授。理学療法士・博士（リハビリテーション科学）。",
        "KY", "Director", "理事",
        "木村 鷹介", "Kimura Yosuke &nbsp;PT, Ph.D.",
        ["理学療法士", "博士（リハビリテーション科学）", "専門PT（神経系）", "認定PT（脳卒中）", "介護予防推進リーダー"],
        "東洋大学 生命科学部 生命医工学科 准教授<br>Associate Professor, Department of Life Sciences, Toyo University",
        "", kimura_body
    ))
print("kimura-yosuke.html OK")

# ============================================================
# imagawa-norie.html
# ============================================================
imagawa_body = """      <div class="reveal">
        <div class="profile-sec-title">Areas of Expertise</div>
        <span class="profile-sec-ja">専門領域・研究テーマ</span>
        <div class="tag-wrap">
          <span class="tag">聴覚障害</span>
          <span class="tag">難聴高齢者</span>
          <span class="tag">人工内耳</span>
          <span class="tag">QOL</span>
          <span class="tag">費用対効果評価</span>
          <span class="tag">介護予防</span>
        </div>
      </div>

      <div class="reveal d1">
        <div class="profile-sec-title">Profile</div>
        <span class="profile-sec-ja">経歴</span>
        <div class="profile-text">
          <p>言語聴覚士免許取得後、大学病院の耳鼻咽喉・頭頚部外科に入職し、主に聴覚障害への評価や支援に従事。現在は教員として言語聴覚士養成校にて勤務し、後世の育成に努めている。また、地域在住者の健康促進のため、大学附属診療センターにて臨床業務も行っている。</p>
          <p>研究活動は、大学病院勤務時代から一貫して高齢人工内耳装用者の装用実態や、費用効用分析を含めた有効性の検討を行っている。また、臨床現場でのリサーチクエッションを基に、補聴器装用、頭頸部癌術後のリハビリテーション、顔面神経麻痺、構音障害、音声障害についても、学会発表や論文報告にて研究活動してきた。</p>
        </div>
      </div>
"""

with open(f"{BASE}/members/imagawa-norie.html", "w", encoding="utf-8") as f:
    f.write(member_wrap(
        "今川 記恵 — HAL Lab.",
        "今川 記恵（Imagawa Norie）。HAL Lab.理事。県立広島大学保健福祉学部助教。言語聴覚士・博士。聴覚障害・人工内耳専門。",
        "IN", "Director", "理事",
        "今川 記恵", "Imagawa Norie &nbsp;ST, Ph.D.",
        ["言語聴覚士", "博士", "聴覚障害専門", "人工内耳専門"],
        "県立広島大学 保健福祉学部 助教<br>Assistant Professor, Faculty of Health and Welfare, Prefectural University of Hiroshima",
        "", imagawa_body
    ))
print("imagawa-norie.html OK")

# ============================================================
# satoh-toshimi.html
# ============================================================
satoh_body = """      <div class="reveal">
        <div class="profile-sec-title">Areas of Expertise</div>
        <span class="profile-sec-ja">専門領域・研究テーマ</span>
        <div class="tag-wrap">
          <span class="tag">内部障害学</span>
          <span class="tag">心血管理学療法</span>
          <span class="tag">障害科学</span>
          <span class="tag">理学療法学</span>
          <span class="tag">介護予防</span>
        </div>
      </div>

      <div class="reveal d1">
        <div class="profile-sec-title">Profile</div>
        <span class="profile-sec-ja">経歴</span>
        <div class="profile-text">
          <p>2007年から2023年、全国に100以上の医療・介護・福祉施設を展開する南東北グループにて、超急性期から回復期、在宅まで幅広いリハビリテーションに携わり、循環器疾患および腎疾患を中心とした多くの研究・発信を行う。</p>
          <p>2018年 東北大学大学院医学系研究科障害科学専攻博士前期課程修了。</p>
          <p>2021年 東北大学大学院医学系研究科障害科学専攻博士後期課程修了。</p>
          <p>2023年 福島県立医科大学保健科学部理学療法学科 助教・同附属病院リハビリテーションセンター兼務。</p>
          <p>2025年 福島県立医科大学保健科学部 講師。一般社団法人HAL Lab. 理事就任。</p>
        </div>
      </div>

      <div class="reveal">
        <div class="profile-sec-title">Professional Memberships</div>
        <span class="profile-sec-ja">所属学会・団体</span>
        <div class="tag-wrap">
          <span class="tag">日本循環器理学療法学会 評議員</span>
          <span class="tag">日本循環器理学療法学会 研究推進委員会</span>
          <span class="tag">日本循環器理学療法学会 学術集会委員会</span>
          <span class="tag">日本臨床運動療法学会 評議員</span>
          <span class="tag">日本心臓リハビリテーション学会</span>
          <span class="tag">日本腎臓リハビリテーション学会</span>
          <span class="tag">日本呼吸ケア・リハビリテーション学会</span>
          <span class="tag">日本理学療法士協会</span>
          <span class="tag">International Confederation of Cardiorespiratory Physical Therapists</span>
          <span class="tag">International Association of Physical Therapists working with Older People</span>
        </div>
      </div>
"""

with open(f"{BASE}/members/satoh-toshimi.html", "w", encoding="utf-8") as f:
    f.write(member_wrap(
        "佐藤 聡見 — HAL Lab.",
        "佐藤 聡見（Satoh Toshimi）。HAL Lab.理事。福島県立医科大学保健科学部講師。理学療法士・博士（障害科学）・専門PT（心血管）。",
        "ST", "Director", "理事",
        "佐藤 聡見", "Satoh Toshimi &nbsp;PT, Ph.D.",
        ["理学療法士", "博士（障害科学）", "専門PT（心血管理学療法）", "認定PT（心血管）", "心臓リハビリテーション指導士", "介護支援専門員"],
        "福島県立医科大学 保健科学部 講師<br>Lecturer, Fukushima Medical University",
        "", satoh_body
    ))
print("satoh-toshimi.html OK")

# ============================================================
# kakehi-tomohiro.html
# ============================================================
kakehi_body = """      <div class="reveal">
        <div class="profile-sec-title">Areas of Expertise</div>
        <span class="profile-sec-ja">専門領域・研究テーマ</span>
        <div class="tag-wrap">
          <span class="tag">作業療法学</span>
          <span class="tag">心臓リハビリテーション</span>
          <span class="tag">生活行為向上支援</span>
          <span class="tag">フレイル・介護予防</span>
          <span class="tag">老年医学</span>
          <span class="tag">転倒予防</span>
        </div>
      </div>

      <div class="reveal d1">
        <div class="profile-sec-title">Profile</div>
        <span class="profile-sec-ja">経歴</span>
        <div class="profile-text">
          <p>2007年作業療法士免許取得後、医療法人社団常仁会牛久愛和総合病院に勤務し、脳血管疾患、運動器疾患、循環器疾患など幅広い疾患の急性期リハビリテーションに従事。</p>
          <p>2020年より国際医療福祉大学成田保健医療学部作業療法学科に着任し、教育の場に携わりながら、転倒に関する研究や循環器疾患の生活支援に関する研究を続けている。</p>
          <p>「イラストでわかる高齢者の生活機能向上支援（文光堂）」など共同執筆著書多数。</p>
          <p>2024年 国際医療福祉大学医学研究科博士後期課程修了。博士（医学）取得。</p>
        </div>
      </div>

      <div class="reveal">
        <div class="profile-sec-title">Message</div>
        <span class="profile-sec-ja">メッセージ</span>
        <div style="background:var(--bg-card);border-left:3px solid var(--gold);padding:1.5rem;border-radius:0 var(--radius-md) var(--radius-md) 0;">
          <p style="font-family:var(--f-serif);font-size:1rem;color:var(--text);letter-spacing:0.08em;line-height:2;">皆さまの健康と寿命の延伸に役立てるよう取組んでまいります</p>
        </div>
      </div>

      <div class="reveal d1">
        <div class="profile-sec-title">Professional Memberships</div>
        <span class="profile-sec-ja">所属学会・団体</span>
        <div class="tag-wrap">
          <span class="tag">日本作業療法士協会 生活行為向上マネジメント推進プロジェクト委員</span>
          <span class="tag">日本作業療法士協会 生活行為向上マネジメント A事例審査員</span>
          <span class="tag">日本作業療法士協会 教育部</span>
          <span class="tag">茨城県作業療法士会 常任理事</span>
        </div>
      </div>
"""

with open(f"{BASE}/members/kakehi-tomohiro.html", "w", encoding="utf-8") as f:
    f.write(member_wrap(
        "筧 智裕 — HAL Lab.",
        "筧 智裕（Kakehi Tomohiro）。HAL Lab.理事。国際医療福祉大学成田保健医療学部講師。作業療法士・認定OT・博士（医学）。",
        "KT", "Director", "理事",
        "筧 智裕", "Kakehi Tomohiro &nbsp;OT, Ph.D.",
        ["作業療法士", "認定作業療法士", "博士（医学）", "心臓リハビリテーション指導士", "生活行為向上マネジメント指導士"],
        "国際医療福祉大学 成田保健医療学部 講師<br>Lecturer, School of Health Sciences at Narita, International University of Health and Welfare",
        "", kakehi_body
    ))
print("kakehi-tomohiro.html OK")

print("\nAll files updated successfully.")
