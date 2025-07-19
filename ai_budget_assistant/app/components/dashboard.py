import streamlit as st
import pandas as pd

def render():
    st.header("Budget Dashboard")
    df = st.session_state.get("transactions")
    if df is None:
        st.warning("Please upload and categorize your transactions first.")
        return

    st.write("Summary:", df.describe())