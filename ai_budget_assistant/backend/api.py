from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Budget AI API is running"}