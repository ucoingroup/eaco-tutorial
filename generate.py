#!/usr/bin/env python3
"""Generate EACO tutorial web app."""
import pathlib, json

OUT = pathlib.Path(r"C:\Users\Administrator\.qclaw\workspace-ua58rsb93veqtxl7\eaco-tutorial-app")
OUT.mkdir(parents=True, exist_ok=True)

# Read i18n from JSON
i18n_path = OUT / "i18n.json"
with open(i18n_path, "r", encoding="utf-8") as f:
    i18n = json.load(f)

js_i18n = json.dumps(i18n, ensure_ascii=False, indent=0)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>EACO Beginner's Guide</title>
<style>
:root{{--primary:#6C5CE7;--primary-dark:#5A4BD1;--accent:#00B894;--warn:#FDCB6E;--bg:#0F0F1A;--card:#1A1A2E;--card2:#16213E;--text:#EAEAEA;--text2:#B0B0C0;--border:#2D2D44;--radius:16px;--shadow:0 8px 32px rgba(0,0,0,0.3)}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:'Segoe UI',system-ui,-apple-system,sans-serif;background:var(--bg);color:var(--text);line-height:1.7;overflow-x:hidden}}
a{{color:var(--accent);text-decoration:none;transition:.2s}}
a:hover{{color:#55EFC4}}
.container{{max-width:900px;margin:0 auto;padding:0 20px}}
nav{{position:sticky;top:0;z-index:100;background:rgba(15,15,26,0.92);backdrop-filter:blur(16px);border-bottom:1px solid var(--border);padding:12px 0}}
.nav-inner{{display:flex;align-items:center;justify-content:space-between;max-width:900px;margin:0 auto;padding:0 20px}}
.logo{{font-size:1.5rem;font-weight:800;background:linear-gradient(135deg,var(--primary),var(--accent));-webkit-background-clip:text;-webkit-text-fill-color:transparent}}
.lang-switcher{{position:relative}}
.lang-btn{{background:var(--card);border:1px solid var(--border);color:var(--text);padding:8px 16px;border-radius:10px;cursor:pointer;font-size:.9rem;transition:.2s}}
.lang-btn:hover{{border-color:var(--primary)}}
.lang-dropdown{{display:none;position:absolute;right:0;top:110%;background:var(--card);border:1px solid var(--border);border-radius:12px;overflow:hidden;min-width:180px;box-shadow:var(--shadow)}}
.lang-dropdown.show{{display:block}}
.lang-option{{padding:10px 16px;cursor:pointer;transition:.15s;font-size:.9rem}}
.lang-option:hover{{background:var(--primary);color:#fff}}
.hero{{text-align:center;padding:80px 20px 60px;position:relative}}
.hero::before{{content:'';position:absolute;top:-100px;left:50%;transform:translateX(-50%);width:600px;height:600px;background:radial-gradient(circle,rgba(108,92,231,0.15),transparent 70%);pointer-events:none}}
.hero h1{{font-size:3rem;font-weight:800;margin-bottom:12px;background:linear-gradient(135deg,#fff,var(--primary));-webkit-background-clip:text;-webkit-text-fill-color:transparent}}
.hero .subtitle{{font-size:1.2rem;color:var(--text2);margin-bottom:24px}}
.badge{{display:inline-block;background:linear-gradient(135deg,var(--accent),#00CEC9);color:#000;font-weight:700;padding:6px 18px;border-radius:20px;font-size:.85rem;margin-bottom:20px}}
.section{{padding:50px 0}}
.section-title{{font-size:1.8rem;font-weight:700;margin-bottom:8px}}
.section-desc{{color:var(--text2);margin-bottom:30px;font-size:1rem}}
.step{{background:var(--card);border:1px solid var(--border);border-radius:var(--radius);padding:28px 28px 24px;margin-bottom:20px;position:relative;transition:.2s}}
.step:hover{{border-color:var(--primary);transform:translateY(-2px);box-shadow:var(--shadow)}}
.step-num{{position:absolute;top:-14px;left:24px;background:linear-gradient(135deg,var(--primary),var(--accent));color:#fff;width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:.9rem}}
.step h3{{font-size:1.2rem;margin-bottom:10px;color:#fff}}
.step p{{color:var(--text2);font-size:.95rem}}
.step code{{background:rgba(108,92,231,0.2);padding:2px 8px;border-radius:6px;font-family:'Consolas',monospace;font-size:.88rem;color:#A29BFE;word-break:break-all}}
.warning{{background:rgba(253,203,110,0.08);border:1px solid rgba(253,203,110,0.3);border-radius:var(--radius);padding:20px 24px;margin:24px 0}}
.warning-title{{color:var(--warn);font-weight:700;margin-bottom:6px;display:flex;align-items:center;gap:8px}}
.warning p{{color:var(--text2);font-size:.92rem}}
.info-card{{background:var(--card2);border:1px solid var(--border);border-radius:var(--radius);padding:20px 24px;margin-bottom:16px}}
.info-card h4{{color:var(--accent);margin-bottom:6px}}
.info-card p,.info-card code{{color:var(--text2);font-size:.93rem}}
.info-card code{{background:rgba(0,184,148,0.12);padding:2px 8px;border-radius:6px;font-family:'Consolas',monospace;color:#55EFC4;word-break:break-all;font-size:.85rem}}
.btn{{display:inline-flex;align-items:center;gap:8px;padding:12px 28px;border-radius:12px;font-weight:600;font-size:1rem;border:none;cursor:pointer;transition:.2s;text-decoration:none}}
.btn-accent{{background:linear-gradient(135deg,var(--accent),#00CEC9);color:#000}}
.btn-accent:hover{{transform:translateY(-2px);box-shadow:0 4px 20px rgba(0,184,148,0.4)}}
footer{{text-align:center;padding:40px 20px;border-top:1px solid var(--border);color:var(--text2);font-size:.85rem}}
.copy-btn{{background:rgba(108,92,231,0.2);border:1px solid var(--primary);color:#A29BFE;padding:4px 12px;border-radius:8px;font-size:.8rem;cursor:pointer;margin-left:8px;transition:.2s}}
.copy-btn:hover{{background:var(--primary);color:#fff}}
.copied{{background:var(--accent)!important;color:#000!important;border-color:var(--accent)!important}}
@media(max-width:600px){{.hero h1{{font-size:2rem}}.step{{padding:22px 18px 18px}}.lang-dropdown{{right:-40px}}}}
</style>
</head>
<body>
<nav><div class="nav-inner"><div class="logo">\U0001fa99 EACO</div><div class="lang-switcher"><button class="lang-btn" onclick="toggleLang()" id="langBtn">\U0001f310 English</button><div class="lang-dropdown" id="langDropdown"><div class="lang-option" onclick="setLang('en')">\U0001f1fa\U0001f1f8 English</div><div class="lang-option" onclick="setLang('zh')">\U0001f1e8\U0001f1f3 \u4e2d\u6587</div><div class="lang-option" onclick="setLang('es')">\U0001f1ea\U0001f1f8 Espa\u00f1ol</div><div class="lang-option" onclick="setLang('fr')">\U0001f1eb\U0001f1f7 Fran\u00e7ais</div><div class="lang-option" onclick="setLang('ar')">\U0001f1f8\U0001f1e6 \u0627\u0644\u0639\u0631\u0628\u064a\u0629</div><div class="lang-option" onclick="setLang('ru')">\U0001f1f7\U0001f1fa \u0420\u0443\u0441\u0441\u043a\u0438\u0439</div></div></div></div></nav>
<div class="hero"><div class="badge" data-i18n="badge">Solana Token</div><h1 data-i18n="hero_title">EACO Beginner's Guide</h1><p class="subtitle" data-i18n="hero_sub">Your first EACO token \u2014 step by step, safe and simple</p></div>
<div class="container">
<div class="section"><div class="warning"><div class="warning-title">\u26a0\ufe0f <span data-i18n="warn_title">Safety Reminders (Stay Positive &amp; Protected)</span></div><p data-i18n="warn_1">Your seed phrase = your wallet. Never share it with anyone, never enter it into any website.</p><p data-i18n="warn_2">Only use official Solflare and verified links.</p><p data-i18n="warn_3">Start small \u2013 test with tiny amounts before moving bigger ones.</p><p data-i18n="warn_4">Check the contract address twice before every swap.</p></div></div>
<div class="section"><h2 class="section-title" data-i18n="ca_title">\U0001f4cc EACO Contract Address (CA)</h2><p class="section-desc" data-i18n="ca_desc">Always verify this address before any transaction</p><div class="info-card"><h4 data-i18n="ca_label">Contract Address</h4><p><code id="caAddr">DqfoyZH96RnvZusSp3Cdncjpyp3C74ZmJzGhjmHnDHRH</code><button class="copy-btn" onclick="copyCA()" id="copyBtn" data-i18n="copy">Copy</button></p></div></div>
<div class="section"><h2 class="section-title" data-i18n="exp_title">\U0001f50d Official Explorers</h2><div class="info-card"><h4>OrbMarkets</h4><p><a href="https://orbmarkets.io/token/DqfoyZH96RnvZusSp3Cdncjpyp3C74ZmJzGhjmHnDHRH" target="_blank">orbmarkets.io/token/EACO \u2192</a></p></div><div class="info-card"><h4>Solscan</h4><p><a href="https://solscan.io/token/DqfoyZH96RnvZusSp3Cdncjpyp3C74ZmJzGhjmHnDHRH" target="_blank">solscan.io/token/EACO \u2192</a></p></div></div>
<div class="section"><h2 class="section-title" data-i18n="steps_title">\U0001f680 Get Your First EACO</h2><p class="section-desc" data-i18n="steps_desc">Follow these steps to buy EACO safely</p>
<div class="step"><div class="step-num">1</div><h3 data-i18n="s1_title">Install Solflare Wallet</h3><p data-i18n="s1_desc">Download Solflare from the official website. Available as browser extension and mobile app. Never download from unofficial sources.</p><p style="margin-top:10px"><a href="https://solflare.com/" target="_blank" class="btn btn-accent">\U0001f517 <span data-i18n="s1_btn">Get Solflare</span></a></p></div>
<div class="step"><div class="step-num">2</div><h3 data-i18n="s2_title">Create or Import Wallet</h3><p data-i18n="s2_desc">Create a new wallet or import an existing one. Write down your seed phrase on paper and store it somewhere safe. Never store it digitally or share it with anyone.</p></div>
<div class="step"><div class="step-num">3</div><h3 data-i18n="s3_title">Deposit SOL</h3><p data-i18n="s3_desc">Transfer SOL to your Solflare wallet address. You will need SOL to swap for EACO and to pay for gas fees. Always keep at least <code>0.05 SOL</code> for transaction fees.</p></div>
<div class="step"><div class="step-num">4</div><h3 data-i18n="s4_title">Swap SOL \u2192 EACO</h3><p data-i18n="s4_desc">Open Solflare built-in Swap feature. Paste the EACO contract address exactly:</p><p style="margin-top:8px"><code>DqfoyZH96RnvZusSp3Cdncjpyp3C74ZmJzGhjmHnDHRH</code></p><p style="margin-top:8px" data-i18n="s4_desc2">Double-check the contract address, then enter the amount of SOL to swap and confirm.</p></div>
<div class="step"><div class="step-num">5</div><h3 data-i18n="s5_title">Verify Your EACO</h3><p data-i18n="s5_desc">After the transaction completes, check your EACO balance in Solflare. You can also verify on Solscan using your wallet address.</p></div>
</div>
<div class="section"><h2 class="section-title" data-i18n="tips_title">\U0001f4a1 Key Trading Tips</h2><div class="info-card"><h4 data-i18n="t1_title">Gas Fees</h4><p data-i18n="t1_desc">Always reserve at least 0.05 SOL for gas fees. Without it, you cannot send or swap tokens.</p></div><div class="info-card"><h4 data-i18n="t2_title">Built-in Swap</h4><p data-i18n="t2_desc">Use Solflare built-in Swap for the safest experience. Avoid unknown DEXs.</p></div><div class="info-card"><h4 data-i18n="t3_title">Double-Check CA</h4><p data-i18n="t3_desc">Always verify the contract address before swapping. Scammers create fake tokens with similar names.</p></div><div class="info-card"><h4 data-i18n="t4_title">Start Small</h4><p data-i18n="t4_desc">Test with a small amount first. Once you are confident, you can increase your position.</p></div></div>
</div>
<footer><p data-i18n="footer">EACO Community \u00b7 Not financial advice \u00b7 Always DYOR</p></footer>
<script>
const i18n={js_i18n};
let currentLang='en';
const langNames={{en:'English',zh:'\u4e2d\u6587',es:'Espa\u00f1ol',fr:'Fran\u00e7ais',ar:'\u0627\u0644\u0639\u0631\u0628\u064a\u0629',ru:'\u0420\u0443\u0441\u0441\u043a\u0438\u0439'}};
function toggleLang(){{document.getElementById('langDropdown').classList.toggle('show')}}
document.addEventListener('click',e=>{{if(!e.target.closest('.lang-switcher'))document.getElementById('langDropdown').classList.remove('show')}});
function setLang(lang){{
  currentLang=lang;
  document.getElementById('langBtn').textContent='\U0001f310 '+langNames[lang];
  document.getElementById('langDropdown').classList.remove('show');
  document.documentElement.lang=lang;
  document.documentElement.dir=lang==='ar'?'rtl':'ltr';
  document.querySelectorAll('[data-i18n]').forEach(el=>{{
    const key=el.getAttribute('data-i18n');
    if(i18n[lang]&&i18n[lang][key])el.textContent=i18n[lang][key];
  }});
  document.title=i18n[lang]?.hero_title||'EACO';
}}
function copyCA(){{
  navigator.clipboard.writeText('DqfoyZH96RnvZusSp3Cdncjpyp3C74ZmJzGhjmHnDHRH');
  const btn=document.getElementById('copyBtn');
  btn.textContent=i18n[currentLang]?.copied||'Copied!';
  btn.classList.add('copied');
  setTimeout(()=>{{btn.textContent=i18n[currentLang]?.copy||'Copy';btn.classList.remove('copied')}},2000);
}}
const userLang=navigator.language.slice(0,2);
if(i18n[userLang])setLang(userLang);
</script>
</body>
</html>"""

out_path = OUT / "index.html"
with open(out_path, "w", encoding="utf-8", newline="\n") as f:
    f.write(html)

print(f"Generated: {out_path}")
print(f"Size: {out_path.stat().st_size} bytes")
