from uuid import UUID
from dataclasses import replace
from task_manager.models import Task

def add_task(tasks: list[Task], title: str, category: str = "") -> list[Task]:
    """Add a new task to the task list.

    Args:
        tasks: Current list of tasks.
        title: Title of the new task.
        category: Optional category for the task.

    Returns:
        New list of tasks with the added task.
    """
    return [*tasks, Task(title=title, category=category)]

def list_tasks(tasks: list[Task]) -> None:
    """Print tasks to the terminal.

    Prints nothing if the task list is empty.

    Args:
        tasks: Current list of tasks.
    """
    for task in tasks:
        category = f" · {task.category}" if task.category else ""
        status = "X" if task.completed else " "

        print(f"\n[{status}] {task.title}")
        print(f"{task.created_at.date()}{category}")
        print(f"id: {task.id}")

def complete_task(tasks: list[Task], task_id: str) -> list[Task]:
    """Mark a task as completed.

    Args:
        tasks: Current list of tasks.
        task_id: Id of the task to mark completed.

    Returns:
        New list of tasks with the task marked as completed.

    Raises:
    ValueError: If no task with the given task_id is found.
    """
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
    """Deletes a task.

    Args:
        tasks: Current list of tasks.
        task_id: Id of the task to delete.

    Returns:
        New list of tasks without the deleted task.

    Raises:
    ValueError: If no task with the given task_id is found.
    """
    target_id = UUID(task_id)

    if not any(task.id == target_id for task in tasks):
        raise ValueError(f"The tasks id ({task_id}) was not found.")

    return [
        task
        for task in tasks
        if task.id != target_id
    ]
