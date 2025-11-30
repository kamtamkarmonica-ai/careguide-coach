# a2a/careguide_a2a_server.py
"""
Expose CareGuide Coach orchestrator as an A2A server.

Run locally:
    python -m a2a.careguide_a2a_server
"""

from google.adk.a2a.utils.agent_to_a2a import to_a2a
from agents.orchestrator_agent import orchestrator_agent


# Turn the orchestrator into an A2A-compatible ASGI app
a2a_app = to_a2a(orchestrator_agent)


if __name__ == "__main__":
    import uvicorn

    # Start local A2A server
    uvicorn.run(
        a2a_app,
        host="0.0.0.0",
        port=8081,
    )
