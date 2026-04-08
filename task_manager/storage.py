from uuid import UUID
from datetime import datetime
from dataclasses import asdict
import json
from task_manager.models import Task

# test_tasks = [
#     Task(
#         title=f"Tarea {i}"
#     )
#     for i in range(1, 6)
# ]

def load_tasks(filepath: str) -> list[Task]:
    """Load tasks from a JSON file.

    Returns an empty list if the file does not exist,
    allowing first-run usage without setup.
    """
    try:
        with open(filepath, "r") as file:
            tasks = json.load(file)

            return [
                Task(
                    title=task.get("title"),
                    category=task.get("category", ""),
                    id=UUID(task.get("id")),
                    created_at=datetime.fromisoformat(task.get("created_at")),
                    completed=task.get("completed", False)
                )
                for task in tasks
            ]
    except FileNotFoundError:
        return []

def save_tasks(filepath: str, tasks: list[Task]) -> None:
    """Save tasks to a JSON file, creating it if it does not exist.

    Args:
        filepath: Path to the JSON file.
        tasks: List of tasks to serialize and save.
    """
    with open(filepath, "w") as file:
        tasks_list = [
            asdict(task)
            for task in tasks
        ]
        json_string = json.dumps(
                tasks_list,
                indent=4,
                sort_keys=True,
                default=str
                )
        file.write(json_string)
