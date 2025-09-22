from pathlib import Path
from pydantic import BaseModel

from task import Task

path = Path("tasks.json")


class TaskList(BaseModel):
    tasks: list[Task] = []

    def load_tasks(self):
        if path.exists():
            loaded_tasklist = TaskList.model_validate_json(path.read_text())
            self.tasks = loaded_tasklist.tasks

    def add_task(self, description: str):
        task_id = max((t.id for t in self.tasks), default=0) + 1
        self.tasks.append(Task(id=task_id, description=description))

    def update_task(self, id: int, description: str):
        task = next((t for t in self.tasks if t.id == id), None)
        if task:
            task.description = description
        else:
            print(f"Cant find task with id {id}")

    def delete_task(self, id: int):
        self.tasks = [task for task in self.tasks if task.id != id]
        print(f"Deleted task with id {id}")

    def print_tasks(self):
        for task in self.tasks:
            print(task)
