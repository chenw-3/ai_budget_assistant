import streamlit as st
from app.services.parser import parse_csv
from app.services.categorizer import categorize_transactions

def render():
    st.header("Upload Bank Transactions")
    uploaded = st.file_uploader("Upload CSV", type=["csv"])

    if uploaded:
        df = parse_csv(uploaded)
        st.write("Raw Transactions", df.head())

        with st.spinner("Categorizing with AI..."):
            categorized_df = categorize_transactions(df)

        st.success("Categorized!")
        st.write("Categorized Transactions", categorized_df.head())
        st.session_state["transactions"] = categorized_df