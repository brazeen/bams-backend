from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import logging
from supabase import create_client, Client
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)
logger = logging.getLogger(__name__)

app = FastAPI()


# Not safe! Add your own allowed domains
origins = [
    "*",
] 

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define what you will receiving in request
class TypePayload(BaseModel):
    content: str

# Example GET route for app
@app.get("/")
async def read_root():
    return {"Hello": "World"}
