"""
agents/retrieval_agent.py

Retrieval Agent for CareGuide Coach.

This agent:
- Figures out which chronic condition/topic the user is asking about.
- Calls the custom `get_condition_info` tool.
- Returns structured information in simple language.
"""

from google.adk.agents import LlmAgent
from google.genai import types

from tools.health_info_tool import get_condition_info

MODEL_ID = "gemini-2.0-flash"

RETRIEVAL_INSTRUCTIONS = """
You are the CareGuide Retrieval Agent.

Your job:
- Identify the main chronic condition or topic the user cares about
  (e.g., "high blood pressure", "diabetes").
- Always call the `get_condition_info` tool to retrieve structured info.
- Present the result in a clear, short explanation with:
  1) A simple summary
  2) 3–5 bullet key points
  3) 3–5 lifestyle / self-care tips
- Use simple, friendly language, suitable for a non-medical person.
- DO NOT give diagnosis, treatment decisions, or medication changes.
- At the end, remind the user that this is for education only,
  not a substitute for a doctor.
"""

retrieval_agent = LlmAgent(
    name="retrieval_agent",
    model=MODEL_ID,
    description="Retrieves structured health information via custom tools.",
    instruction=RETRIEVAL_INSTRUCTIONS,
    tools=[get_condition_info],  # ADK wraps this as a FunctionTool automatically
)
