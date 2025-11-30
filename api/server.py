import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
import httpx

load_dotenv()

app = FastAPI(title="Sabobot - ElevenLabs Conversational AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
AGENT_ID = os.getenv("ELEVENLABS_AGENT_ID")

@app.get("/")
def home():
    return {"status": "ok", "agent": "sabobot", "agent_id": AGENT_ID}

@app.get("/get-signed-url")
async def get_signed_url():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://api.elevenlabs.io/v1/convai/conversation/get_signed_url?agent_id={AGENT_ID}",
            headers={"xi-api-key": ELEVENLABS_API_KEY}
        )
        
        if response.status_code != 200:
            return {"error": response.text, "status": response.status_code}
        
        return response.json()

@app.get("/demo", response_class=HTMLResponse)
def demo_page():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sabobot Demo</title>
        <style>
            body { font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; }
            button { padding: 15px 30px; font-size: 18px; cursor: pointer; margin: 10px; }
            #status { margin: 20px 0; padding: 10px; border-radius: 5px; }
            .connected { background: #d4edda; color: #155724; }
            .disconnected { background: #f8d7da; color: #721c24; }
            .connecting { background: #fff3cd; color: #856404; }
        </style>
    </head>
    <body>
        <h1>🤖 Sabobot</h1>
        <p>ElevenLabs Conversational AI Agent</p>
        
        <div id="status" class="disconnected">Disconnected</div>
        
        <button id="startBtn" onclick="startConversation()">🎤 Start Conversation</button>
        <button id="stopBtn" onclick="stopConversation()" disabled>⏹️ Stop</button>
        
        <script>
            let conversation = null;
            
            async function startConversation() {
                document.getElementById('status').textContent = 'Connecting...';
                document.getElementById('status').className = 'connecting';
                
                try {
                    const response = await fetch('/get-signed-url');
                    const data = await response.json();
                    
                    if (data.error) {
                        throw new Error(data.error);
                    }
                    
                    const { Conversation } = await import('https://cdn.jsdelivr.net/npm/@11labs/client@latest/+esm');
                    
                    conversation = await Conversation.startSession({
                        signedUrl: data.signed_url,
                        onConnect: () => {
                            document.getElementById('status').textContent = 'Connected - Speak now!';
                            document.getElementById('status').className = 'connected';
                            document.getElementById('startBtn').disabled = true;
                            document.getElementById('stopBtn').disabled = false;
                        },
                        onDisconnect: () => {
                            document.getElementById('status').textContent = 'Disconnected';
                            document.getElementById('status').className = 'disconnected';
                            document.getElementById('startBtn').disabled = false;
                            document.getElementById('stopBtn').disabled = true;
                        },
                        onError: (error) => {
                            console.error('Error:', error);
                            document.getElementById('status').textContent = 'Error: ' + error.message;
                            document.getElementById('status').className = 'disconnected';
                        }
                    });
                    
                } catch (error) {
                    console.error('Failed to start:', error);
                    document.getElementById('status').textContent = 'Error: ' + error.message;
                    document.getElementById('status').className = 'disconnected';
                }
            }
            
            async function stopConversation() {
                if (conversation) {
                    await conversation.endSession();
                    conversation = null;
                }
            }
        </script>
    </body>
    </html>
    """
