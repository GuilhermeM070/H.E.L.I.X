from fastapi import FastAPI

app = FastAPI()

@app.get("/") #endpoint que recebe dados (como link do YouTube, por exemplo);
def home():
    return{"mensagem": "API online e funcional"} #mensagem que irá aparecer no navegador


