from __future__ import annotations

import logging
from collections import defaultdict
from typing import TYPE_CHECKING

from event.event_models import Event, EventType

if TYPE_CHECKING:
    from event.event_listeners import BaseEventListener

logger = logging.getLogger(__name__)


class EventPublisher:
    """
    Central Event Publisher responsible for managing event subscriptions
    and dispatching events to registered listeners.

    Implements the Publisher role of the Observer Pattern.
    """

    def __init__(self) -> None:
        """
        Initialize the publisher with an empty listener registry.
        """
        self._listeners: dict[EventType, list["BaseEventListener"]] = defaultdict(list)

    def subscribe(
        self,
        event_type: EventType,
        listener: "BaseEventListener",
    ) -> None:
        """
        Register a listener for a specific event type.

        Args:
            event_type: Event to subscribe to.
            listener: Listener instance.
        """
        if listener not in self._listeners[event_type]:
            self._listeners[event_type].append(listener)
            logger.info(
                "Listener '%s' subscribed to '%s'.",
                listener.__class__.__name__,
                event_type.value,
            )

    def unsubscribe(
        self,
        event_type: EventType,
        listener: "BaseEventListener",
    ) -> None:
        """
        Remove a listener from a specific event type.

        Args:
            event_type: Event to unsubscribe from.
            listener: Listener instance.
        """
        if listener in self._listeners[event_type]:
            self._listeners[event_type].remove(listener)
            logger.info(
                "Listener '%s' unsubscribed from '%s'.",
                listener.__class__.__name__,
                event_type.value,
            )

    def publish(self, event: Event) -> None:
        """
        Publish an event to all registered listeners.

        Args:
            event: Event object to publish.
        """
        listeners = self._listeners.get(event.event_type, [])

        logger.info(
            "Publishing event '%s' to %d listener(s).",
            event.event_type.value,
            len(listeners),
        )

        for listener in listeners:
            try:
                listener.handle(event)
            except Exception as exc:
                logger.exception(
                    "Listener '%s' failed while processing '%s'. Error: %s",
                    listener.__class__.__name__,
                    event.event_type.value,
                    exc,
                )

    def get_listeners(
        self,
        event_type: EventType,
    ) -> list["BaseEventListener"]:
        """
        Retrieve all listeners subscribed to a specific event.

        Args:
            event_type: Event type.

        Returns:
            List of registered listeners.
        """
        return list(self._listeners.get(event_type, []))

    def clear(self) -> None:
        """
        Remove all registered listeners.
        """
        self._listeners.clear()
        logger.info("All event listeners have been cleared.")