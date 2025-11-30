# main.py
from modules.voice_input import grabar_voz
from modules.voice_output import hablar
from modules.assistant import generar_respuesta
import speech_recognition as sr

def main():
    while True:
        grabar_voz("input.wav", duracion=5)

        # Convertir voz a texto
        r = sr.Recognizer()
        with sr.AudioFile("input.wav") as source:
            audio = r.record(source)
            try:
                texto_usuario = r.recognize_google(audio, language="es-ES")
                print("Usuario:", texto_usuario)
            except:
                print("No entendí lo que dijiste.")
                continue

        # Generar respuesta
        respuesta = generar_respuesta(f"Cliente dice: {texto_usuario}\nAsistente responde:")
        print("Asistente:", respuesta)

        # Hablar la respuesta
        hablar(respuesta)

if __name__ == "__main__":
    main()
