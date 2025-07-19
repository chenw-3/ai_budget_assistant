from pydantic import BaseModel

class User(BaseModel):
    id: str
    email: str

class Budget(BaseModel):
    user_id: str
    transactions: list

class Goal(BaseModel):
    user_id: str
    goal_amount: float
    timeline_months: int