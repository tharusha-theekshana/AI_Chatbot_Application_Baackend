import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY")
    GEMINI_VERSION: str = os.getenv("GEMINI_VERSION")


# Export settings
settings = Settings()
