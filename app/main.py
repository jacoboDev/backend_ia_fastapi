from fastapi import FastAPI
from app.schemas import QuestionRequest, AnswerResponse
from app.ai import ask_ai
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Mini Backend IA")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask", response_model=AnswerResponse)
def ask(request: QuestionRequest):
    answer = ask_ai(request.question)
    return {"answer": answer}
