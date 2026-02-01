import requests
from fastapi import FastAPI
from app.schemas import QuestionRequest, AnswerResponse
from app.ai import ask_ai


app = FastAPI(title="Mini Backend IA")


@app.get("/")
def read_root():
    return {"message": "Hola, tu backend de IA funciona!"}


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask", response_model=AnswerResponse)
def ask(request: QuestionRequest):
    answer = ask_ai(request.question)
    return {"answer": answer}

@app.get("/ask_free")
def ask_free(question: str):
    response = requests.post(
        "https://www.torgpt.space/api/v1/chat",
        json={"messages":[{"role":"user","content": question}]}
    )
    return response.json()

