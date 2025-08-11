import os
import json

FILE_NAME = "tasks.json"
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []
def save_tasks(tasks):
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f)
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            status = "✓" if task['done'] else "✗"
            print(f"{i}. [{status}] {task['text']}")
def add_task(tasks):
    text = input("Enter task: ").strip()
    if text:
        tasks.append({'text': text, 'done': False})
        print("Task added.")
def mark_done(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]['done'] = True
            print("Task marked as done.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Invalid input.")
def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Deleted: {removed['text']}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Invalid input.")
def main():
    tasks = load_tasks()

    while True:
        print("\n==== To-Do List ====")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
