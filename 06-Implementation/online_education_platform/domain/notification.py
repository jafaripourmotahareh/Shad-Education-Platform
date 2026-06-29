import uuid
from domain.base_entity import BaseEntity

class Notification(BaseEntity):
    def __init__(self, user_id: uuid.UUID, title: str, message: str):
        super().__init__()
        self.user_id = user_id
        self.title = title
        self.message = message
        self.is_read = False
        self.sent_at = self.created_at

        def mark_as_read(self) -> None :
            self.is_read = True
