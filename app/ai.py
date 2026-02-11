import os
from dotenv import load_dotenv
from openai import OpenAI
import google.generativeai as genai

load_dotenv()  # carga .env


#Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model_gemini = genai.GenerativeModel("models/gemini-3-flash-preview")

#Configure OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


#OpenAI
def ask_ai(question: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Responde de forma clara y concisa."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

#Gemini
def ask_gemini(question: str) -> str:
    try:
        response = model_gemini.generate_content(question)
        return response.text
    except Exception as e:
        return f"Gemini error: {e}"