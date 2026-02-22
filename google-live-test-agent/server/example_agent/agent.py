from google.adk.agents import Agent
from google.genai.types import GenerateContentConfig

from .prompts import AGENT_INSTRUCTION

genai_config = GenerateContentConfig(temperature=0.5)

root_agent = Agent(
    name="live_test_agent",
    model="gemini-live-2.5-flash-preview-native-audio",
    description="Real-time interview and hackathon coaching agent.",
    instruction=AGENT_INSTRUCTION,
)
