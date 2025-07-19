import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_plan(goal_amount, months):
    prompt = f"Help a user save ${goal_amount} in {months} months. Create a monthly plan to reach this goal."
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()