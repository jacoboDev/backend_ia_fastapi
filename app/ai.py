from openai import OpenAI
import os

from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()  # carga .env



genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-3-flash-preview")



API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise Exception("No se encontró OPENAI_API_KEY")

client = OpenAI(api_key=API_KEY)


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_ai(question: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Responde de forma clara y concisa."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

def ask_gemini(question: str) -> str:
    try:
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"Gemini error: {e}"