# 🧠 AI Mental Health Therapist

SafeSpace is an **AI-powered mental health companion** that combines a chat-style frontend, an LLM-based backend agent, and integrations with **Twilio WhatsApp** and **Google Maps**.  
It is designed as an **educational / demo project** to showcase how to build a **tool-using AI agent** for mental health–style conversations.

> ⚠️ **Disclaimer**  
> This project is for educational and demonstration purposes only.  
> It is **NOT** a substitute for professional mental health care or emergency services.

---

## ✨ Features

- 💬 Conversational mental health guidance using a therapeutic LLM (MedGemma via Groq)
- 🧠 **Conversation memory** using LangGraph (per-user session memory)
- 🚨 Crisis detection with an emergency call tool (Twilio Voice)
- 📍 Location-aware therapist finder using Google Maps
- 🌐 Streamlit-based web chat UI
- 📱 WhatsApp chat support via Twilio webhook

---

## 🏗️ Project Structure

```
safespace-ai-therapist/
├── backend/
│   ├── ai_agent.py         # LangGraph agent + tools
│   ├── config.py           # API keys & credentials (not committed)
│   ├── main.py             # FastAPI backend (/ask + /whatsapp_ask)
│   ├── tools.py            # Low-level integrations (LLM, Twilio, Maps)
│   └── test_location_tool.py
├── frontend.py             # Streamlit chat UI
├── pyproject.toml          # Dependencies (managed with uv)
└── README.md
```

---

## 🧠 Memory Architecture (Important)

SafeSpace uses **LangGraph’s built-in checkpointer** to provide **conversation memory**.

### What memory enables:
- Remembers previous user messages
- Improves intent detection after greetings like “hi”
- Persists location (e.g., “I live in Gurgaon”)
- Prevents repetitive responses
- Improves tool usage accuracy

### How memory works:
- Uses `MemorySaver` from LangGraph
- Each conversation is identified by a **thread_id**
- For WhatsApp: `thread_id = From` (phone number)
- For Web UI: `thread_id = web_user` (or session-based ID)

> ⚠️ Memory is **in-memory only** (RAM). Restarting the server clears it.
> For production, use Redis or a database-backed checkpointer.

---

## ⚙️ Tech Stack

**Language**
- Python 3.11+

**Backend**
- FastAPI
- Uvicorn

**Frontend**
- Streamlit

**LLM / Agent**
- LangChain
- LangGraph
- ChatGroq (Groq API)
- ReAct-style tool-using agent

**Integrations**
- Twilio (WhatsApp + Voice)
- Google Maps API (Geocoding + Places)

**Environment & Packaging**
- uv

---

## 📦 Dependencies

Main dependencies (from `pyproject.toml`):

```
fastapi
geopy
googlemaps
langchain
langchain-groq
langchain-openai
langgraph
ollama
pydantic
python-multipart
requests
streamlit
twilio
uvicorn
```

---

## ✅ Prerequisites

- Python 3.11+
- `uv` installed
- API keys:
  - Groq (`GROQ_API_KEY`)
  - Google Maps (`GOOGLE_MAPS_API_KEY`)
  - Twilio (Account SID, Auth Token, WhatsApp/Voice numbers)

---

## 🚀 Setup (Using uv)

### 1️⃣ Clone & install
```bash
git clone https://github.com/AIwithhassan/safespace-ai-therapist.git
cd safespace-ai-therapist
uv sync
```

### 2️⃣ Activate virtual environment
```bash
source .venv/bin/activate
```

### 3️⃣ Configure backend/config.py

Create `backend/config.py`:

```python
GROQ_API_KEY = "your_groq_api_key"
GOOGLE_MAPS_API_KEY = "your_google_maps_api_key"

TWILIO_ACCOUNT_SID = "your_twilio_sid"
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_FROM_NUMBER = "+1234567890"
TWILIO_EMERGENCY_TO_NUMBER = "+1987654321"
```

⚠️ Do NOT commit this file.

---

## ▶️ Running the Backend

```bash
cd backend
uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### Available endpoints:
- `POST /ask` – Web frontend API
- `POST /whatsapp_ask` – Twilio WhatsApp webhook

---

## 🧪 API Examples

### `/ask` (JSON)

```http
POST http://localhost:8000/ask
Content-Type: application/json

{
  "message": "I feel anxious lately"
}
```

Response:
```json
{
  "response": "...",
  "tool_called": "ask_mental_health_specialist"
}
```

---

### `/whatsapp_ask` (Twilio webhook)

```bash
curl -X POST http://localhost:8000/whatsapp_ask   -H "Content-Type: application/x-www-form-urlencoded"   -d "Body=I feel overwhelmed&From=whatsapp:+919999999999"
```

---

## 🌐 Running the Frontend

```bash
uv run streamlit run frontend.py
```

Open: http://localhost:8501

---

## 📱 Twilio WhatsApp Setup

1. Run backend on port 8000
2. Expose using ngrok:
```bash
ngrok http 8000
```
3. Set Twilio webhook:
```
https://<ngrok-url>/whatsapp_ask
```

---

## 🚨 Emergency Call Tool

- Automatically triggered if suicidal ideation or crisis is detected
- Uses Twilio Voice to call a predefined helpline
- **Use extreme caution** if adapting for real-world use

---

## 🧪 Testing

```bash
uv run pytest
```

(Optional – add more tests under `tests/`)

---

## 🔮 Suggested Next Improvements

- Redis-backed persistent memory
- Twilio signature validation
- Rate limiting
- GDPR-safe “forget me” command
- Emotion summarization memory
- Better UI safety disclaimers

---

## 📜 Disclaimer

This project is a **technical demonstration only**.  
It must **not** be used as a replacement for licensed mental health professionals or emergency services.

If you or someone you know is in immediate danger, contact local emergency services or a crisis hotline.

---

🧠 Built for learning, safety-aware experimentation, and agentic AI exploration.
