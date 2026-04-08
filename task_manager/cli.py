import argparse
from task_manager.manager import add_task, list_tasks, complete_task, delete_task
from task_manager.storage import load_tasks, save_tasks

FILE_PATH = "tasks.json"

def handle_add(title: str, category:str = "") -> None:
    """Add a task and save it to JSON file.

    Args:
        title: Title of the new task.
        category: Optional category for the task.
    """
    loaded_tasks = load_tasks(FILE_PATH)
    new_tasks = add_task(tasks=loaded_tasks, title=title, category=category)
    save_tasks(FILE_PATH, tasks=new_tasks)

def handle_list() -> None:
    """Print all tasks to the terminal."""
    loaded_tasks = load_tasks(FILE_PATH)
    list_tasks(tasks=loaded_tasks)

def handle_complete(task_id: str) -> None:
    """Mark given task as completed and save it in a JSON file.

    Args:
        task_id: Id of the task to mark completed.

    Raises:
        ValueError: If no task with the given task_id is found.
    """
    loaded_tasks = load_tasks(FILE_PATH)
    new_tasks = complete_task(loaded_tasks, task_id)
    save_tasks(FILE_PATH, tasks=new_tasks)

def handle_delete(task_id: str) -> None:
    """Delete a given task and save state to JSON file.

    Args:
        task_id: Id of the task to delete.

    Raises:
        ValueError: If no task with the given task_id is found.
    """
    loaded_tasks = load_tasks(FILE_PATH)
    new_tasks = delete_task(loaded_tasks, task_id)
    save_tasks(FILE_PATH, tasks=new_tasks)


def main():
    parser =  argparse.ArgumentParser(prog="task-manager")
    subparsers = parser.add_subparsers(dest="command", required=True, help="sub-command help")

    add_parser = subparsers.add_parser("add", help="Add new task.")
    add_parser.add_argument("title")
    add_parser.add_argument("--category", default="")
    add_parser.set_defaults(func=handle_add)

    subparsers.add_parser("list", help="List all tasks.").set_defaults(func=handle_list)

    complete_parser = subparsers.add_parser("complete", help="Mark task as completed.")
    complete_parser.add_argument("task_id")
    complete_parser.set_defaults(func=handle_complete)

    delete_parser = subparsers.add_parser("delete", help="Delete a task.")
    delete_parser.add_argument("task_id")
    delete_parser.set_defaults(func=handle_delete)

    args = parser.parse_args()
    func = args.func
    kwargs = vars(args)
    kwargs.pop("command")
    kwargs.pop("func")

    try:
        func(**kwargs)
    except ValueError as e:
        print(f"Error: {e}")
