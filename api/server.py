from fastapi import FastAPI
from pydantic import BaseModel
from modules.assistant import generar_respuesta
from modules.voice_output import hablar

app = FastAPI(title="Asistente de Voz Virtual")

class Mensaje(BaseModel):
    texto: str

@app.post("/asistente/")
def obtener_respuesta(mensaje: Mensaje):
    """
    Recibe un texto del usuario y devuelve la respuesta del asistente.
    """
    respuesta = generar_respuesta(f"Cliente dice: {mensaje.texto}\nAsistente responde:")
    hablar(respuesta)  # Convierte la respuesta a voz
    return {"respuesta": respuesta}
