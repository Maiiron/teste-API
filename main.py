from fastapi import FastAPI
from routers.soma_route import router as calc_router

app = FastAPI()

app.include_router(calc_router)

contador = 0

@app.get("/")
def root():
    return {"message": "fiz minha primeira API com deploy (Mayron)"}

@app.get("/valor")
def get_valor():
    return {"contador": contador}

@app.get("/incrementar")
def incrementar():
    global contador
    contador += 1
    return {"contador": contador}
