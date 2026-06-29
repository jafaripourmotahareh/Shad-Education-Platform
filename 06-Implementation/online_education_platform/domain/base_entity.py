import uuid
from datetime import datetime

class BaseEntity:
    def __init__(self):
        self.id: uuid.UUID = uuid.uuid4()
        self.created_at : datetime = datetime.now()
        self.updated_at : datetime = datetime.now()

    def get_identifier(self) -> uuid.UUID:
        return self.id