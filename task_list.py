from __future__ import annotations
from dataclasses import dataclass, asdict, field
from pathlib import Path
import json

from task import Task
from util.custom_encoder import custom_encoder

path = Path("tasks.json")


@dataclass
class TaskList:
    tasks: list[Task] = field(default_factory=list)

    def load_tasks(self):
        if path.exists():
            contents = path.read_text()
            data = json.loads(contents)
            self.tasks.clear()
            for item in data:
                self.tasks.append(Task.from_dict(item))

    def add_task(self, description: str):
        task_id = max((t.id for t in self.tasks), default=0) + 1
        self.tasks.append(Task(task_id, description))

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
            print(task)

    def write_tasks(self):
        contents = json.dumps(
            [asdict(task) for task in self.tasks], default=custom_encoder
        )
        path.write_text(contents)
