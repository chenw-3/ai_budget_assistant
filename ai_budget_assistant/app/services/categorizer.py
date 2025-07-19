import openai
import os
from app.utils.constants import EXPENSE_CATEGORIES

openai.api_key = os.getenv("OPENAI_API_KEY")

def categorize_transactions(df):
    def ask_gpt(description):
        prompt = f"Categorize this transaction: '{description}'\nCategories: {', '.join(EXPENSE_CATEGORIES)}"
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        return response.choices[0].message.content.strip()

    df["category"] = df["description"].apply(ask_gpt)
    return df