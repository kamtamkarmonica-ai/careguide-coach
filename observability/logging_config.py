"""
observability/logging_config.py

Basic Python logging setup for CareGuide Coach.

- Logs to console (VS Code terminal)
- Logs to a file: observability/careguide_local.log
"""

import logging
from pathlib import Path


def configure_logging() -> None:
    logs_dir = Path(__file__).resolve().parent
    logs_dir.mkdir(exist_ok=True)

    log_file = logs_dir / "careguide_local.log"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler(log_file, encoding="utf-8"),
        ],
    )

    logging.getLogger(__name__).info("Logging configured. Log file: %s", log_file)
