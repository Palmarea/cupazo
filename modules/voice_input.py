import sounddevice as sd
import numpy as np
import wavio

def grabar_voz(nombre_archivo="input.wav", duracion=5, fs=44100):
    print("Hablá ahora...")
    grabacion = sd.rec(int(duracion * fs), samplerate=fs, channels=1)
    sd.wait()
    wavio.write(nombre_archivo, grabacion, fs, sampwidth=2)
    print(f"Grabación guardada en {nombre_archivo}")
    return nombre_archivo
