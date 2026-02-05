import requests
from fastapi import FastAPI
from app.schemas import QuestionRequest, AnswerResponse
from app.ai import ask_ai, ask_gemini



app = FastAPI(title="Mini Backend IA")


@app.get("/")
def read_root():
    return {"message": "Hola, tu backend de IA funciona!"}


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask_OpenAI", response_model=AnswerResponse)
def ask_OpenAI(request: QuestionRequest):
    answer = ask_ai(request.question)
    return {"answer": answer}

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


@app.get("/ask_Gemini")
def ask_Gemini(question: str):
    answer = ask_gemini(question)
    return {"question": question, "answer": answer}