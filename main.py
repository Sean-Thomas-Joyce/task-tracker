# Todo: Update task
# Todo: Delete Task
# Todo: Change status of task
from dataclasses import asdict
from datetime import datetime
import typer
import json
from pathlib import Path

from task import Status, Task
from util.custom_encoder import custom_encoder

app = typer.Typer()

tasks: list[Task] = []
path = Path("tasks.json")


@app.command()
def add(title: str):
    id = max((t.id for t in tasks), default=0) + 1
    tasks.append(Task(id, title))
    contents = json.dumps([asdict(task) for task in tasks], default=custom_encoder)
    path.write_text(contents)
    print(f"Added task: {title}")


@app.command()
def list():
    for task in tasks:
        print(task.__str__())


def load_tasks():
    global tasks
    if path.exists():
        contents = path.read_text()
        data = json.loads(contents)
        tasks.clear()
        for item in data:
            tasks.append(
                Task(
                    id=item["id"],
                    description=item["description"],
                    status=Status(item["status"]),
                    created_at=datetime.fromisoformat(item["created_at"]),
                    updated_at=datetime.fromisoformat(item["updated_at"]),
                )
            )


def main():
    load_tasks()
    app()


if __name__ == "__main__":
    main()
