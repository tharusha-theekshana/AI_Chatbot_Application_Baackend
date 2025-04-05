from fastapi import FastAPI
from app.config import settings

app = FastAPI()

# Store google api key & gemini version
apiKey = settings.GOOGLE_API_KEY
gemini_version = settings.GEMINI_VERSION


@app.get("/")
def testRequest():
    return {"message : Test Request"}
