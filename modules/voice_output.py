from elevenlabs import set_api_key, generate, play
from config.config import ELEVEN_LABS_API_KEY, ELEVEN_VOICE

set_api_key(ELEVEN_LABS_API_KEY)

def hablar(texto):
    voz = generate(text=texto, voice=ELEVEN_VOICE, model="eleven_monolingual_v1")
    play(voz)
