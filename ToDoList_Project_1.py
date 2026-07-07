from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

TASKS_FILE = Path("tasks.json")


def load_tasks() -> List[Dict[str, Any]]:
    if not TASKS_FILE.exists():
        return []
    try:
        with TASKS_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            tasks = []
            for item in data:
                if isinstance(item, dict) and "title" in item and "done" in item:
                    tasks.append({"title": str(item["title"]).strip(), "done": bool(item["done"])})
            return tasks
    except (json.JSONDecodeError, OSError):
        pass
    return []


def save_tasks(tasks: List[Dict[str, Any]]) -> None:
    with TASKS_FILE.open("w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def show_tasks(tasks: List[Dict[str, Any]]) -> None:
    if not tasks:
        print("\nNo tasks yet.")
        return

    print("\nYour Tasks:")
    print("-" * 40)
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{index}. [{status}] {task['title']}")
    print("-" * 40)


def add_task(tasks: List[Dict[str, Any]]) -> None:
    title = input("Enter task: ").strip()
    if not title:
        print("Task cannot be empty.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added.")


def delete_task(tasks: List[Dict[str, Any]]) -> None:
    if not tasks:
        print("No tasks to delete.")
        return

    show_tasks(tasks)
    try:
        choice = int(input("Enter task number to delete: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def mark_task_done(tasks: List[Dict[str, Any]]) -> None:
    if not tasks:
        print("No tasks to update.")
        return

    show_tasks(tasks)
    try:
        choice = int(input("Enter task number to mark as done: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["done"] = True
            save_tasks(tasks)
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")


def main() -> None:
    tasks = load_tasks()

    while True:
        print("\n=== TO-DO LIST ===")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
