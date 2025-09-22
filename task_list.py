from datetime import datetime
from pathlib import Path
from pydantic import BaseModel

from task import Task


class TaskList(BaseModel):
    tasks: list[Task] = []
    path = Path("tasks.json")

    def load_tasks(self):
        if self.path.exists():
            loaded_tasklist = TaskList.model_validate_json(self.path.read_text())
            self.tasks = loaded_tasklist.tasks

    def add_task(self, description: str):
        task_id = max((t.id for t in self.tasks), default=0) + 1
        self.tasks.append(Task(id=task_id, description=description))
        self.path.write_text(self.model_dump_json())
        print(f"Added task: {description}")

    def update_task(self, id: int, description: str):
        task = next((t for t in self.tasks if t.id == id), None)
        if task:
            task.description = description
            task.updated_at = datetime.now()
            print(f"Updated task {id} description to: {description}")
            self.path.write_text(self.model_dump_json())
        else:
            print(f"Cant find task with id {id}")

    def delete_task(self, id: int):
        self.tasks = [task for task in self.tasks if task.id != id]
        self.path.write_text(self.model_dump_json())
        print(f"Deleted task with id {id}")

    def print_tasks(self):
        for task in self.tasks:
            print(task)
