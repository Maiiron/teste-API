from fastapi import APIRouter
from models.soma_model import SomaRequest

router = APIRouter()

@router.post("/somar")
def somar_valores(request: SomaRequest):
    resultado = request.a + request.b
    return {
        "a": request.a,
        "b": request.b,
        "resultado": resultado
    }
