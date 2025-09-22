from dataclasses import dataclass
from datetime import date, datetime
from enum import Enum, auto


class Status(int, Enum):
    TODO = auto()
    IN_PROGRESS = auto()
    DONE = auto()


@dataclass
class Task:
    id: int
    description: str
    status: Status = Status.TODO
    created_at: date = datetime.now()
    updated_at: date = datetime.now()

    def update_description(self, new_description: str):
        self.description = new_description
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{self.id}] {self.description} - {self.status.name} (Created: {self.created_at}, Updated: {self.updated_at})"
