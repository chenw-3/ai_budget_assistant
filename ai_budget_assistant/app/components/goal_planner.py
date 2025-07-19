import streamlit as st
from app.services.planner import generate_plan

def render():
    st.header("Wealth Goal Planner")

    goal_amount = st.number_input("Target Amount ($)", min_value=100.0)
    months = st.number_input("Target Timeline (Months)", min_value=1)

    if st.button("Generate Plan"):
        plan = generate_plan(goal_amount, months)
        st.markdown("### AI-Generated Plan")
        st.write(plan)