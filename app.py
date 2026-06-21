import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="MEREBE — Triple Media 통합 전략 기획서",
    page_icon="🧺",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
    .main > div { padding: 0 !important; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    header { display: none !important; }
    #MainMenu { display: none !important; }
    footer { display: none !important; }
    .stApp { background: #F7F3EE; }
</style>
""", unsafe_allow_html=True)

with open("merebe.html", "r", encoding="utf-8") as f:
    html_content = f.read()

components.html(html_content, height=10000, scrolling=True)
