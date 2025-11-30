"""
Session & state management for CareGuide Coach.

This module wraps google.adk.sessions.InMemorySessionService and adds
helper methods for:
- creating / retrieving sessions
- reading / writing simple key/value state
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Optional

from google.adk.sessions import InMemorySessionService, Session  # type: ignore


DEFAULT_APP_NAME = "agents"



@dataclass
class CareGuideSessionConfig:
    app_name: str = DEFAULT_APP_NAME


class CareGuideSessionManager:
    """
    Thin wrapper around InMemorySessionService that:
    - manages sessions per user
    - exposes convenience methods to get/set state keys
    """

    def __init__(self, config: Optional[CareGuideSessionConfig] = None) -> None:
        self.config = config or CareGuideSessionConfig()
        self._service = InMemorySessionService()

    @property
    def service(self) -> InMemorySessionService:
        """Access the underlying ADK session service (for Runner / AdkApp)."""
        return self._service

    async def get_or_create_session(
        self,
        user_id: str,
        session_id: Optional[str] = None,
        initial_state: Optional[Dict[str, Any]] = None,
    ) -> Session:
        """
        Get an existing session or create a new one.
        """
        session = await self._service.create_session(
            app_name=self.config.app_name,
            user_id=user_id,
            session_id=session_id,
            state=initial_state or {},
        )
        return session

    async def set_state_value(
        self,
        session: Session,
        key: str,
        value: Any,
    ) -> Session:
        """
        Set a single key in the session.state and save it.
        """
        session.state[key] = value
        session = await self._service.update_session(session)
        return session

    def get_state_value(
        self,
        session: Session,
        key: str,
        default: Any = None,
    ) -> Any:
        return session.state.get(key, default)
