from datetime import datetime
from enum import Enum
from pydantic import BaseModel


class Status(str, Enum):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"


class Task(BaseModel):
    id: int
    description: str
    status: Status = Status.TODO
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

    def update_description(self, new_description: str):
        self.description = new_description
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.id}] {self.description} - {self.status.name} (Created: {self.created_at}, Updated: {self.updated_at})"
