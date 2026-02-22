# google-adk-live-test-agent

Google Devpost **Agent Live Hackathon** project.

## Current direction
Build a real-time **LiveTest Agent** (voice + text) that helps users practice technical interviews and hackathon pitching with instant feedback.

## Repository layout
- `google-live-test-agent/` → base ADK live app (client + server)
- `google-live-test-agent/server/example_agent/` → active prompt + agent logic

## What is done
- ✅ Repository cloned and set up locally
- ✅ Agent prompt switched from generic math tutor to **interview/hackathon coach**
- ✅ Agent identity updated to `live_test_agent`

## Next build steps
1. Add session memory (track weak areas across questions)
2. Add scoring JSON output for each answer
3. Add question packs by role (SDE, AI Engineer, PM)
4. Add export to markdown report after session
5. Add demo video + Devpost writeup

## Run locally
```bash
cd google-live-test-agent
# server
cd server
uv venv
uv pip install .
uvicorn main:app --reload

# client (new terminal)
cd ../client
npm install
npm run dev
```
