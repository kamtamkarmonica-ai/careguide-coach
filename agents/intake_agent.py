# agents/intake_agent.py

"""
Intake Agent for CareGuide Coach.

This agent:
- Cleans and normalizes the user question
- Detects topic/condition (non-diagnostic)
- Detects language (e.g., English, Hindi, Marathi)
- Flags if the user is asking for diagnosis, prescriptions, or emergencies
"""

from google.adk.agents import LlmAgent  # type: ignore

MODEL_ID = "gemini-2.0-flash"

INTAKE_INSTRUCTIONS = """
You are the Intake Agent for CareGuide Coach.

Your output is for another AI agent (the orchestrator), NOT for the end user.

Given a user message:
- Rewrite it as a simple "Cleaned question".
- Identify the main topic/condition.
- Identify the language.
- Detect risk flags (e.g., emergency vs general education).

Return text in exactly this format:

Cleaned question: <one line>
Topic: <one line>
Language: <one line>
Risk flags: <one line>

Do NOT give explanations, education, or advice.
Do NOT write disclaimers.
Do NOT address the user directly (no “you”).
"""


intake_agent = LlmAgent(
    name="careguide_intake_agent",
    model=MODEL_ID,
    description="Analyzes and cleans the user question before routing.",
    instruction=INTAKE_INSTRUCTIONS,
)
