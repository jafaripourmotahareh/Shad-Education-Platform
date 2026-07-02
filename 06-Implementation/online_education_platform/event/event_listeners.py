from __future__ import annotations

import logging
from abc import ABC, abstractmethod

from event.event_models import Event

logger = logging.getLogger(__name__)


class BaseEventListener(ABC):
    """
    Abstract base class for all event listeners.
    """

    @abstractmethod
    def handle(self, event: Event) -> None:
        """
        Process an incoming event.
        """
        pass


class LoggingListener(BaseEventListener):
    """
    Logs all published events.
    """

    def handle(self, event: Event) -> None:
        logger.info(
            "[EVENT] %s | Payload=%s | Time=%s",
            event.event_type.value,
            event.payload,
            event.timestamp,
        )


class AuditListener(BaseEventListener):
    """
    Stores audit information.
    """

    def handle(self, event: Event) -> None:
        logger.info(
            "[AUDIT] %s processed successfully.",
            event.event_type.value,
        )


class NotificationListener(BaseEventListener):
    """
    Handles notification-related events.

    NotificationService will be integrated later.
    """

    def handle(self, event: Event) -> None:
        logger.info(
            "[NOTIFICATION] Event=%s Payload=%s",
            event.event_type.value,
            event.payload,
        )


class GradeListener(BaseEventListener):
    """
    Handles grading-related events.

    GradeService will be integrated later.
    """

    def handle(self, event: Event) -> None:
        logger.info(
            "[GRADE] Event=%s Payload=%s",
            event.event_type.value,
            event.payload,
        )