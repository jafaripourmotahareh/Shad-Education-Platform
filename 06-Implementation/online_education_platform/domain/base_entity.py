import uuid
from datetime import datetime


class BaseEntity:
        def __init__(self, entity_id=None):
           self._id = entity_id or uuid.uuid4()
           self.created_at: datetime = datetime.now()
           self.updated_at: datetime = datetime.now()

        def getUdentifier(self):
               return self._id

