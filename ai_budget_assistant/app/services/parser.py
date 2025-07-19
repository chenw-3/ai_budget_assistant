import pandas as pd

def parse_csv(file):
    df = pd.read_csv(file)
    df.columns = [c.strip().lower() for c in df.columns]
    df.rename(columns={"amount": "amount", "date": "date", "description": "description"}, inplace=True)
    df = df[["date", "description", "amount"]]
    df["date"] = pd.to_datetime(df["date"])
    return df