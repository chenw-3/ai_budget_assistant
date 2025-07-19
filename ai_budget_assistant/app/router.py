import streamlit as st
from app.components import upload, dashboard, goal_planner

def run_router():
    pages = {
        "Upload Transactions": upload.render,
        "Budget Dashboard": dashboard.render,
        "Wealth Goal Planner": goal_planner.render
    }
    page = st.sidebar.selectbox("Navigate", list(pages.keys()))
    pages[page]()