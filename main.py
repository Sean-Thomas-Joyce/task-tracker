import typer
from pathlib import Path

from task_list import TaskList

app = typer.Typer()
task_list = TaskList()

path = Path("tasks.json")


@app.command()
def add(description: str):
    task_list.add_task(description)
    path.write_text(task_list.model_dump_json())
    print(f"Added task: {description}")


@app.command()
def update(id: int, description: str):
    task_list.update_task(id, description)
    path.write_text(task_list.model_dump_json())


@app.command()
def list():
    task_list.print_tasks()


@app.command()
def delete(id: int):
    task_list.delete_task(id)
    path.write_text(task_list.model_dump_json())


if __name__ == "__main__":
    task_list.load_tasks()
    app()
