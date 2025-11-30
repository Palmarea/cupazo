# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Cupazo is a Spanish-language voice assistant bot that uses:
- **Qwen2-7B-Instruct** model for generating conversational responses
- **Eleven Labs TTS** for text-to-speech output
- **Google Speech Recognition** for speech-to-text input

## Commands

### Run the voice assistant (CLI mode)
```bash
python main.py
```

### Run the FastAPI server
```bash
uvicorn api.server:app --reload
```

### Install dependencies
```bash
# Using uv (recommended, see uv.lock)
uv sync

# Or using pip
pip install -r requirements.txt
```

## Architecture

The application has two entry points:
1. **main.py** - Interactive CLI loop that records voice → transcribes → generates response → speaks
2. **api/server.py** - FastAPI REST endpoint at `/asistente/` that accepts text and returns spoken responses

### Module Structure

- **modules/voice_input.py** - Records audio via sounddevice, saves as WAV
- **modules/voice_output.py** - Uses Eleven Labs API to convert text to speech and play it
- **modules/assistant.py** - Loads Qwen2 model and generates responses (uses MPS on Apple Silicon, falls back to CPU)
- **config/config.py** - Stores Eleven Labs API key and voice configuration

### Data Flow (CLI)
```
grabar_voz() → input.wav → speech_recognition → generar_respuesta() → hablar()
```

## Configuration

The Eleven Labs API key must be set in `config/config.py`. The voice model is configured via `ELEVEN_VOICE`.

## Language

- The codebase uses Spanish for function names, comments, and user-facing text
- Speech recognition is configured for Spanish (`es-ES`)
