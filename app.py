import streamlit as st
import re

st.set_page_config(
    page_title="MEREBE — Triple Media 통합 전략 기획서",
    page_icon="🧺",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Streamlit 기본 UI 완전 제거 ──────────────────────────────────────────────
st.markdown(
    """
    <style>
    header[data-testid="stHeader"]          { display: none !important; }
    #MainMenu                               { display: none !important; }
    footer                                  { display: none !important; }
    .stDeployButton                         { display: none !important; }
    div[data-testid="stToolbar"]            { display: none !important; }
    div[data-testid="stDecoration"]         { display: none !important; }
    div[data-testid="stStatusWidget"]       { display: none !important; }
    section[data-testid="stSidebar"]        { display: none !important; }
    div[data-testid="collapsedControl"]     { display: none !important; }

    /* 모든 패딩·마진 제거 */
    .main .block-container,
    .main > div,
    .stMainBlockContainer,
    [data-testid="stAppViewBlockContainer"],
    [data-testid="stVerticalBlockBorderWrapper"] {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }

    /* st.html 래퍼 여백 제거 */
    div[data-testid="stHtml"],
    div[data-testid="stHtml"] > div {
        padding: 0 !important;
        margin: 0 !important;
    }

    /* 앱 배경 */
    .stApp,
    [data-testid="stAppViewContainer"] {
        background: #F7F3EE !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── HTML 로드 ─────────────────────────────────────────────────────────────────
with open("merebe.html", "r", encoding="utf-8") as f:
    raw = f.read()

# <link> 태그 전부 추출 (Google Fonts preconnect + stylesheet 포함)
link_tags = "\n".join(re.findall(r"<link[^>]+>", raw))

# <style> 블록 추출
style_match = re.search(r"<style>(.*?)</style>", raw, re.DOTALL)
style_block = f"<style>{style_match.group(1)}</style>" if style_match else ""

# <body> 내용 추출
body_match = re.search(r"<body>(.*?)</body>", raw, re.DOTALL)
body_html  = body_match.group(1) if body_match else raw

# ── st.html() 로 직접 주입 ────────────────────────────────────────────────────
# link 태그(폰트) + style(CSS) + body 순서로 합쳐서 주입
# st.html() : iframe 없이 페이지에 직접 렌더링 (Streamlit 1.31+)
st.html(link_tags + "\n" + style_block + "\n" + body_html, width="stretch")
