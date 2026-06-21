import streamlit as st
import re

st.set_page_config(
    page_title="MEREBE — Triple Media 통합 전략 기획서",
    page_icon="🧺",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Streamlit 기본 UI 완전 제거 ──────────────────────────────────────────────
st.markdown("""
<style>
header[data-testid="stHeader"]       { display:none !important; }
#MainMenu                             { display:none !important; }
footer                                { display:none !important; }
.stDeployButton                       { display:none !important; }
div[data-testid="stToolbar"]          { display:none !important; }
div[data-testid="stDecoration"]       { display:none !important; }
div[data-testid="stStatusWidget"]     { display:none !important; }
section[data-testid="stSidebar"]      { display:none !important; }
div[data-testid="collapsedControl"]   { display:none !important; }

.main .block-container {
    padding: 0 !important;
    max-width: 100% !important;
}
.main > div { padding: 0 !important; }
.stMainBlockContainer { padding: 0 !important; }
.stApp { background: #F7F3EE !important; }

/* st.html() 내부 여백 제거 */
div[data-testid="stHtml"] {
    padding: 0 !important;
    margin: 0 !important;
}
div[data-testid="stHtml"] > div {
    padding: 0 !important;
    margin: 0 !important;
}
</style>
""", unsafe_allow_html=True)

# ── HTML 파일 로드 ───────────────────────────────────────────────────────────
with open("merebe.html", "r", encoding="utf-8") as f:
    html_raw = f.read()

# Google Fonts 링크 추출
font_links = "\n".join(re.findall(r'<link[^>]+googleapis[^>]+>', html_raw))

# <style> 블록 추출
style_match = re.search(r'<style>(.*?)</style>', html_raw, re.DOTALL)
style_block = f"<style>{style_match.group(1)}</style>" if style_match else ""

# <body> 내용 추출
body_match = re.search(r'<body>(.*?)</body>', html_raw, re.DOTALL)
body_html = body_match.group(1) if body_match else html_raw

# ── st.html()로 직접 주입 (iframe 없음, 높이 제한 없음) ─────────────────────
# st.html()은 Streamlit 1.31+ 에서 지원, iframe 없이 페이지에 직접 렌더링
st.html(font_links + "\n" + style_block + "\n" + body_html)
