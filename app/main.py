from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.model import ChatRequest, ChatResponse

import google.generativeai as generativeAi

app = FastAPI()

# Store google api key & gemini version
apiKey = settings.GOOGLE_API_KEY

# Config google ai client
generativeAi.configure(api_key=apiKey)
model = generativeAi.GenerativeModel("gemini-2.0-flash")

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # or ["*"] to allow all
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Post endpoint
@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        response = model.generate_content(request.message)
        response_text = response.text
        return ChatResponse(reply=response_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error with response generate : {str(e)}")
