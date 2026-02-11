from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import QuestionRequest, AnswerResponse
import requests
from app.ai import ask_ai, ask_gemini


app = FastAPI(title="Mini Backend IA")


# Serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Allow CORS between frontend navigator and backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
#    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
#    allow_methods=["GET", "POST"],
    allow_headers=["*"]
#    allow_headers=["Content-Type", "Authorization"]
)



# root
@app.get("/")
def read_root():
    return {"message": "Hola, tu backend de IA funciona!"}


@app.get("/health")
def health():
    return {"status": "ok"}


# OpenAI
@app.post("/ask_OpenAI", response_model=AnswerResponse)
def ask_OpenAI(request: QuestionRequest):
    answer = ask_ai(request.question)
    return {"answer": answer}

#TorGPT
@app.get("/ask_Tor_GPT")
def ask_Tor_GPT(question: str):
    try:
        response = requests.post(
            "https://www.torgpt.space/api/v1/chat",
            json={"messages": [{"role": "user", "content": question}]},
            timeout=10
        )
        return {
            "status_code": response.status_code,
            "text": response.text
        }
    except Exception as e:
        return {"error": str(e)}


#Gemini
@app.get("/askGemini")
def askGemini(question: str):
    answer = ask_gemini(question)
    return {"question": question, "answer": answer}


@app.post("ask_Gemini_Post", response_model=AnswerResponse)
def ask_gemini_post(request: QuestionRequest):
    answer = ask_gemini(request.question)
    return {"answer": answer}