from uuid import UUID
from dataclasses import replace
from task_manager.models import Task

def add_task(tasks: list[Task], title: str, category: str = "") -> list[Task]:
    return [*tasks, Task(title=title, category=category)]

def list_tasks(tasks: list[Task]) -> None:
    for task in tasks:
        category = f" | {task.category}" if task.category else ""
        status = "X" if task.completed else " "

        print(f"[{status}] - {task.title} (id: {task.id})")
        print(f"{task.created_at.date()}{category}")

def complete_task(tasks: list[Task], task_id: str) -> list[Task]:
    target_id = UUID(task_id)

    if not any(task.id == target_id for task in tasks):
        raise ValueError(f"The tasks id ({task_id}) was not found.")

    return [
        replace(task, completed=True)
        if task.id == target_id
        else task
        for task in tasks
    ]

def delete_task(tasks: list[Task], task_id: str) -> list[Task]:
    target_id = UUID(task_id)

    if not any(task.id == target_id for task in tasks):
        raise ValueError(f"The tasks id ({task_id}) was not found.")

    return [
        task
        for task in tasks
        if task.id != target_id
    ]
