# AI Chatbot Application Backend (FastAPI)

## Requirements
- Python 3.10+
- Docker (optional)
- Google API Key from Google AI Studio

## Setup the project locally
1. Clone the Repository
    
    command : **git clone https://github.com/tharusha-theekshana/AI_Chatbot_Application_Backend**


2. Add your Google API Key to .env file **GOOGLE_API_KEY** property.


3. Create virtual environment
    
    command : **python -m venv venv**


4. run virtual environment

   command : **.\venv\Scripts\activate**


5. Install requirements

    command : **pip install -r requirements.txt**


6. Run project

    command : **uvicorn app.main:app --reload**


7. Access to api doc generate with Fast API
   
    url : http://localhost:8000/docs


8. Run with Docker if you need.

   command : docker compose up --build

   