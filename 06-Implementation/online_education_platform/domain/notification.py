from datetime import datetime
from .base_entity import BaseEntity


class Notification(BaseEntity):
    def __init__(self, userId, type, title, message, targetLink="", entity_id=None):
        super().__init__(entity_id)
        self.userId = userId
        self.type = type
        self.title = title
        self.message = message
        self.IsRead = False
        self.targetLink = targetLink
        self.sentAt = datetime.now()

    def markAsRead(self):
        self.IsRead = True
