import streamlit as st
import re

st.set_page_config(
    page_title="MEREBE — Triple Media 통합 전략 기획서",
    page_icon="🧺",
    layout="wide",
    initial_sidebar_state="collapsed",
)

with open("merebe.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Extract Google Fonts links
font_links = re.findall(r'<link[^>]+googleapis[^>]+>', html_content)

# Extract <style> block
style_match = re.search(r'<style>(.*?)</style>', html_content, re.DOTALL)
style_block = f"<style>{style_match.group(1)}</style>" if style_match else ""

# Extract <body> content
body_match = re.search(r'<body>(.*?)</body>', html_content, re.DOTALL)
body_content = body_match.group(1) if body_match else ""

# Streamlit UI 완전 제거 스타일
hide_streamlit = """
<style>
    /* Streamlit 기본 UI 제거 */
    header[data-testid="stHeader"] { display: none !important; }
    #MainMenu { display: none !important; }
    footer { display: none !important; }
    .stDeployButton { display: none !important; }
    div[data-testid="stToolbar"] { display: none !important; }
    div[data-testid="stDecoration"] { display: none !important; }
    div[data-testid="stStatusWidget"] { display: none !important; }

    /* 패딩 완전 제거 */
    .main .block-container {
        padding: 0 !important;
        max-width: 100% !important;
    }
    .main > div {
        padding: 0 !important;
    }
    section[data-testid="stSidebar"] { display: none !important; }
    div[data-testid="collapsedControl"] { display: none !important; }
</style>
"""

# 1) Streamlit UI 숨기기
st.markdown(hide_streamlit, unsafe_allow_html=True)

# 2) Google Fonts 로드
if font_links:
    st.markdown("\n".join(font_links), unsafe_allow_html=True)

# 3) 원본 CSS 주입
st.markdown(style_block, unsafe_allow_html=True)

# 4) 원본 HTML 본문 주입
st.markdown(body_content, unsafe_allow_html=True)
