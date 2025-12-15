from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os

load_dotenv()

app = FastAPI()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
)

class EchoRequest(BaseModel):
    message: str

class EchoResponse(BaseModel):
    reply: str

@app.post("/test", response_model=EchoResponse)
async def test(req: EchoRequest):
    resp = llm.invoke(f"Reply in one sentence: {req.message}")
    return EchoResponse(reply=resp.content)
