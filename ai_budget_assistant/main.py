import streamlit as st
from app.router import run_router

st.set_page_config(page_title="AI Budget Coach", layout="wide")
st.title("🧠 AI Budget & Wealth Assistant")

run_router()