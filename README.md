# cupazo
*hackatonAI2025*

# What am I?
A voice bot, help you out with a call.
- Using model to answer.
- Text to voice using Eleven Labs TTS.

# Run me
### steps

### STEP 01 - Clone the repo and set up environment
```bash
git clone https://github.com/Palmarea/cupazo.git
cd cupazo
```
```bash
uv sync
```

### STEP 02 - Create your .env file with your ElevenLabs API key
```bash
cp .env.example .env
```

Then edit `.env` and add your API key:
```
ELEVENLABS_API_KEY=your_api_key_here
ELEVENLABS_AGENT_ID=agent_6701kb9wfserehrrf5fg4w3jydq7
```

> Get your API key at https://elevenlabs.io/app/settings/api-keys  
> Make sure to enable **ElevenLabs Agents → Write** permission

### STEP 03 - Run the server
```bash
uv run uvicorn api.server:app --reload --host 0.0.0.0 --port 8000
```

Open http://localhost:8000/demo and click "Start Conversation" , api done!

# Files Structure
```
cupazo/
├── api/
│   └── server.py        # FastAPI server with ElevenLabs integration
├── data/
├── .env                  # Your API keys (never commit this)
├── .env.example          # Template for .env
├── .gitignore
├── pyproject.toml
└── README.md
```
