from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any


class EventType(Enum):
    USER_REGISTERED = "USER_REGISTERED"
    COURSE_CREATED = "COURSE_CREATED"
    STUDENT_ENROLLED = "STUDENT_ENROLLED"
    EXAM_CREATED = "EXAM_CREATED"
    EXAM_SUBMITTED = "EXAM_SUBMITTED"
    GRADE_CALCULATED = "GRADE_CALCULATED"
    NOTIFICATION_CREATED = "NOTIFICATION_CREATED"


@dataclass(slots=True)
class Event:
    event_type: EventType
    payload: dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.utcnow)