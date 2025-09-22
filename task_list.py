from dataclasses import dataclass, asdict
from datetime import datetime
from pathlib import Path
import json

from task import Status, Task
from util.custom_encoder import custom_encoder


path = Path("tasks.json")


@dataclass
class TaskList:
    tasks: list[Task] = []

    def load_tasks(self):
        if path.exists():
            contents = path.read_text()
            data = json.loads(contents)
            self.tasks.clear()
            for item in data:
                self.tasks.append(
                    Task(
                        id=item["id"],
                        description=item["description"],
                        status=Status(item["status"]),
                        created_at=datetime.fromisoformat(item["created_at"]),
                        updated_at=datetime.fromisoformat(item["updated_at"]),
                    )
                )

    def add_task(self, description: str):
        id = max((t.id for t in self.tasks), default=0) + 1
        self.tasks.append(Task(id, description))

    def update_task(self, id: int, description: str):
        task = next((t for t in self.tasks if t.id == id), None)
        if task:
            task.update_description(description)
            self.write_tasks()
        else:
            print(f"Cant find task with id {id}")

    def delete_task(self, id: int):
        self.tasks = [task for task in self.tasks if task.id != id]

    def print_tasks(self):
        for task in self.tasks:
            print(task.__str__())

    def write_tasks(self):
        contents = json.dumps(
            [asdict(task) for task in self.tasks], default=custom_encoder
        )
        path.write_text(contents)
