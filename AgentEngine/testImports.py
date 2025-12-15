from fastapi import FastAPI
import uvicorn
from langchain_google_genai import ChatGoogleGenerativeAI
from google import genai
from dotenv import load_dotenv
from pydantic import BaseModel

print("All imports OK")
