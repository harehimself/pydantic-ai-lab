from pydantic import BaseModel

# User input model
class UserQuery(BaseModel):
    query: str

# AI response model
class AIResponse(BaseModel):
    response: str
