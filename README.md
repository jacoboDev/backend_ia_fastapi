
1. Activate environment

venv\Scripts\activate



2. Install anything

pip install fastapi uvicorn



3. Programe, execute

python main.py


4. Exit environment

deactivate



---- Our first dependencies:
pip install fastapi uvicorn openai python-dotenv








_______________________HELP

- Create / update into requirements.txt for saving venv config into git

pip freeze > requirements.txt


- Other dev fetch project

venv\Scripts\activate
pip install -r requirements.txt


- Update requirements every time something new is installed:

pip install sqlalchemy
pip freeze > requirements.txt

___________

Error MUY típico
pip install -r requirements.txt

sin antes:
venv\Scripts\activate


Resultado: librerías en global, proyecto raro, bugs fantasma


------------

Clone repo:
 ```
git clone repo
cd repo
python -m venv venv      ← crear entorno
venv\Scripts\activate   ← activarlo
pip install -r requirements.txt
```



--------

HOW TO EXECUTE SERVER:

From project root:
cd C:\WORKSPACE\backend-ia-fastapi
venv\Scripts\activate  
uvicorn app.main:app --reload  


Open navigator:
http://127.0.0.1:8000/docs

This is an automatic swagger.

You can try:

GET /health
POST /ask

or

{
  "question": "Explícame qué es REST en una frase"
}



------

execute test_main:
cd C:\WORKSPACE\backend-ia-fastapi
venv\Scripts\activate  
uvicorn test_main:app --reload




----------- TorGPT
install library:
cd C:\WORKSPACE\backend-ia-fastapi
venv\Scripts\activate
pip install requests




--------------- OPEN FRONTEND

uvicorn app.main:app --reload
http://127.0.0.1:8000/static/index.html


try gemini engine
http://127.0.0.1:8000/askGemini?question=hola



--------------- TEST ENGINE FROM CONSOLE
// Prueba esto en la consola (ajusta /ask si en el docs ves otra cosa)
fetch("https://backend-ia-fastapi.onrender.com/ask_Gemini_Post", { // <--- Sin barra al final si así está en Python
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ 
    question: "Hola, ¿quién eres?"
  })
})
.then(res => res.json())
.then(console.log);
