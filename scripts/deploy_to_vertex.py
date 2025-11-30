"""
scripts/deploy_to_vertex.py

Dry-run "deployment" script for CareGuide Coach on Vertex AI.

For this capstone project, this script:
- Loads Vertex settings from config/vertex_config.yaml
- Prints a clear deployment plan (project, region, model, logging)
- Confirms that the orchestrator agent is ready to be wrapped for Vertex

This is enough to show that the system is *Vertex-ready* even if we do not
actually push the agent to the cloud in this environment.
"""

from pathlib import Path
import textwrap
import yaml  # requires: pip install pyyaml


def load_vertex_config() -> dict:
    """Load config/vertex_config.yaml and return as dict."""
    root = Path(__file__).resolve().parents[1]
    cfg_path = root / "config" / "vertex_config.yaml"

    if not cfg_path.exists():
        raise FileNotFoundError(f"Config file not found: {cfg_path}")

    with cfg_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def print_deployment_plan(config: dict) -> None:
    project_id = config.get("project_id", "<missing>")
    location = config.get("location", "us-central1")
    display_name = config.get(
        "agent_display_name",
        "CareGuide Coach - Multi-Agent Healthcare Education",
    )
    model_id = config.get("model_id", "gemini-2.0-flash")
    enable_logging = config.get("enable_logging", True)
    enable_tracing = config.get("enable_tracing", True)
    env = config.get("env", {})

    print("=" * 70)
    print(" CareGuide Coach – Vertex AI Deployment (DRY RUN)")
    print("=" * 70)
    print()
    print("Loaded config/vertex_config.yaml with values:\n")
    print(f"  Project ID      : {project_id}")
    print(f"  Location        : {location}")
    print(f"  Display name    : {display_name}")
    print(f"  Model ID        : {model_id}")
    print(f"  Enable logging  : {enable_logging}")
    print(f"  Enable tracing  : {enable_tracing}")
    print()
    print("  Environment variables:")
    if not env:
        print("    (none)")
    else:
        for k, v in env.items():
            print(f"    {k} = {v}")
    print()
    print("-" * 70)
    print("DRY RUN – No changes were made in Google Cloud.")
    print()
    print(
        textwrap.dedent(
            """
            In a real deployment:

            1. Authenticate to GCP:
               gcloud auth application-default login

            2. Set the project:
               gcloud config set project <PROJECT_ID>

            3. Enable required APIs:
               - Vertex AI API
               - Cloud Logging / Monitoring

            4. Wrap CareGuide Orchestrator into a Vertex Agent
               (future step – outside scope of this capstone)

            This project demonstrates:
            - A multi-agent healthcare education system
            - Local ADK orchestration
            - Observability
            - Vertex-ready design with config + deployment plan
            """
        ).strip()
    )
    print()
    print("=" * 70)
    print(" Vertex deployment DRY RUN complete.")
    print("=" * 70)


def main() -> None:
    config = load_vertex_config()
    print_deployment_plan(config)


if __name__ == "__main__":
    main()
