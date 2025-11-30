"""
Async local runner for CareGuide Coach using Google ADK.
Run from project root (with venv active and GOOGLE_API_KEY set):

    python -m scripts.run_local
"""

import asyncio

from google.adk.runners import Runner
from google.genai import types

from agents.orchestrator_agent import orchestrator_agent
from memory.session_service import CareGuideSessionManager
from observability.logging_config import configure_logging
import logging


APP_NAME = "agents"          # must match SessionService app name
USER_ID = "demo-user"
SESSION_ID = "local-cli-session"


async def main() -> None:
    configure_logging()
    logger = logging.getLogger("careguide_cli")
    # Set up session + runner
    session_manager = CareGuideSessionManager()

    session = await session_manager.get_or_create_session(
        user_id=USER_ID,
        session_id=SESSION_ID,
        initial_state={},
    )

    runner = Runner(
        agent=orchestrator_agent,
        app_name=APP_NAME,
        session_service=session_manager.service,
    )

    print("CareGuide Coach – local test")
    print("Type a health education question (or 'exit' to quit).")
    print()

    while True:
        user_message = input("You: ")
        if user_message.strip().lower() in {"exit", "quit"}:
            print("Goodbye!")
            break
        logger.info("User question: %s", user_message)
        # Build Gemini content
        content = types.Content(
            role="user",
            parts=[types.Part(text=user_message)],
        )

        # Stream events from the orchestrator
        events = runner.run_async(
            user_id=USER_ID,
            session_id=session.id,
            new_message=content,
        )

        final_text: str | None = None
        async for event in events:
            if event.is_final_response() and event.content and event.content.parts:
                # Take first text part as the answer
                part = event.content.parts[0]
                if hasattr(part, "text") and part.text is not None:
                    final_text = part.text

        if final_text:
            logger.info(
                "Assistant response (first 120 chars): %s",
                final_text[:120] if len(final_text) > 120 else final_text,
            )
            print("\nAssistant:", final_text, "\n")
        else:
            logger.warning("No final response from runner.")
            print("\nAssistant: (no final response)\n")


if __name__ == "__main__":
    asyncio.run(main())
