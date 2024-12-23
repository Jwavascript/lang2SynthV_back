from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from services.openai_service import text_to_ipa
from services.ipa_to_synthv_service import ipa_to_synthv
import os
import time
from dotenv import load_dotenv

# load .env 
load_dotenv()

# OpenAI API key check
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise RuntimeError("OPENAI_API_KEY is not set in .env file!")

app = FastAPI()

# CORS setting

CORS_ORIGIN = os.getenv("CORS_ORIGIN")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://lang2synthv.vercel.app", "https://lang2synthv-3ek7nicjd-jwavascripts-projects.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# request limit setting
REQUEST_LIMIT = 30
TIME_WINDOW = 3600
request_counts = {}

# request limit check
def check_request_limit(client_ip):
    current_time = time.time()
    if client_ip not in request_counts:
        request_counts[client_ip] = {"count": 0, "start_time": current_time}

    client_data = request_counts[client_ip] 

    if current_time - client_data["start_time"] > TIME_WINDOW:
        request_counts[client_ip] = {"count": 0, "start_time": current_time}
        client_data = request_counts[client_ip]

    if client_data["count"] >= REQUEST_LIMIT:
        raise HTTPException(
            status_code=429,
            detail=f"Request limit exceeded. Try again in {TIME_WINDOW // 60} minutes.",
        )

    client_data["count"] += 1

class TextRequest(BaseModel):
    text: str

@app.post("/convert")
async def convert_text(request: TextRequest, req: Request):
    # request limit check
    client_ip = req.client.host
    check_request_limit(client_ip)

    # language 2 ipa
    ipa_result = text_to_ipa(request.text)

    # ipa 2 synthv
    synthv_result = ipa_to_synthv(ipa_result)

    return {"ipa": ipa_result, "synthv": synthv_result}
