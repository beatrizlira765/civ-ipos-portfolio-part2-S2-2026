from src.task import Task
from src.file_handler import save_tasks
from datetime import datetime
from rich.console import Console
from rich.table import Table


def add_task(tasks, title, description, due_date):
    """
    Add a new task to the task list.

    Args:
        tasks (list): The list of existing Task objects.
        title (str): The title of the new task.
        description (str): A brief description of the task.
        due_date (str): The due date of the task in 'DD-MM-YYYY' format.

    Returns:
        bool: True if the task is added successfully, False otherwise.

    Raises:
        ValueError: If the due date is not in the correct format.

    Side Effects:
        - Saves the updated task list to a file using `save_tasks`.
    """
    # Prevent duplicate tasks
    if any(task.title == title for task in tasks):
        print("Error: A task with this title already exists.")
        return False

    # Validate due date format
    try:
        datetime.strptime(due_date, "%d-%m-%Y")
    except ValueError:
        print("Error: Invalid date format. Use DD-MM-YYYY.")
        return False

    tasks.append(Task(title, description, due_date))
    save_tasks(tasks)
    return True


def delete_task(tasks, title):
    """
    Delete a task from the task list based on its title.

    Args:
        tasks (list): The list of existing Task objects.
        title (str): The title of the task to be deleted.

    Returns:
        bool: True if the task was found and deleted, False otherwise.

    Side Effects:
        - Saves the updated task list to a file using `save_tasks`.
    """
    for task in tasks:
        if task.title == title:
            tasks.remove(task)
            save_tasks(tasks)
            return True
    return False


def get_status_color(status):
    if status == "pending":
        return "red"
    elif status == "completed":
        return "green"


def list_tasks(tasks, status=None):
    """
    Display tasks in the task list, optionally filtered by status.

    Args:
        tasks (list): The list of existing Task objects.
        status (str, optional): The status to filter tasks
        by (e.g., "pending" or "completed").

    Returns:
        None

    Side Effects:
        - Prints the list of tasks to the console.
    """
    if not status:
        # If status is not set
        filtered = tasks
    else:
        # Filter tasks based on their status
        filtered = []
        for task in tasks:
            if task.status == status:
                filtered.append(task)

    if not filtered:
        print("No tasks found.")
        return

    table = Table()
    console = Console(force_terminal=True, color_system="standard")

    table.add_column("Title")
    table.add_column("Description")
    table.add_column("Due Date")
    table.add_column("Status")

    for task in filtered:
        color = get_status_color(task.status)

        color_string = f"[{color}]{task.status}[/{color}]"
        table.add_row(task.title, task.description, task.due_date, color_string)

    console.print(table)


def filter_tasks_by_status(tasks, status):
    """
    Filter tasks by their status.

    Args:
        tasks (list): The list of existing Task objects.
        status (str): The status to filter tasks by (e.g., "pending" or "completed").

    Returns:
        list: A list of Task objects that match the specified status.
    """
    return [task for task in tasks if task.status == status]
