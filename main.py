import typer

from task_list import TaskList

app = typer.Typer()
task_list = TaskList()


@app.command()
def add(description: str):
    task_list.add_task(description)
    task_list.write_tasks()
    print(f"Added task: {description}")


@app.command()
def update(id: int, description: str):
    task_list.update_task(id, description)


@app.command()
def list():
    task_list.print_tasks()


@app.command()
def delete(id: int):
    task_list.delete_task(id)
    task_list.write_tasks()
    print(f"Deleted task with id {id}")


if __name__ == "__main__":
    task_list.load_tasks()
    app()
