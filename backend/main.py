from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

#step-2; receieve and validate the request from frontend 
class Query(BaseModel):
    message: str

app.post("/ask")
async def ask(query: Query):
    #AI Agent
    response = "This is from backend"

    #Step3: Response to the frontend
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000,reload=True)