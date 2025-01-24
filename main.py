from fastapi import FastAPI
from agent import run_agent

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Pydantic AI Agent!"}

@app.get("/query")
def query_agent(user_query: str):
    response = run_agent(user_query)
    return {"query": user_query, "response": response}
