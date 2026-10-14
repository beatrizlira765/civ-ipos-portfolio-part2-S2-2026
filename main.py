from src.task_manager import add_task, delete_task, list_tasks, check_tasks
from src.file_handler import load_tasks
import schedule
import threading
import time
from plyer import notification


def remind(tasks):
    message = check_tasks(tasks)

    if message:
        notification.notify(
            title="Task List Reminder",
            message=message,
            timeout=10
        )


def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)


def main():
    tasks = load_tasks()

    remind(tasks)

    schedule.every(1).minutes.do(remind, tasks)

    threading.Thread(target=run_schedule, daemon=True).start()

    while True:
        print("\nTask Manager CLI")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. List Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            title = input("Title: ")
            description = input("Description: ")
            due_date = input("Due Date (DD-MM-YYYY): ")
            add_task(tasks, title, description, due_date)
        elif choice == "2":
            title = input("Title of the task to delete: ")
            if delete_task(tasks, title):
                print("Task deleted successfully.")
            else:
                print("Task not found.")
        elif choice == "3":
            list_tasks(tasks)
        elif choice == "4":
            print("Exiting Task Manager.")
            break
        else:
            print("Invalid choice. Try again.")



if __name__ == "__main__":
    main()
