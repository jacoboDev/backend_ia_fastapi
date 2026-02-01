
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

- Create requirements.txt for saving venv config into git

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


💥 Resultado: librerías en global, proyecto raro, bugs fantasma


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
cd backend-ia-fastapi
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
