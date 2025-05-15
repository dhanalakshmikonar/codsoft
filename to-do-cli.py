import json

tasks = []

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(task):
    tasks.append({"task": task, "completed": False})
    save_tasks()

def view_tasks():
    for idx, task in enumerate(tasks, 1):
        status = "✔" if task["completed"] else "❌"
        print(f"{idx}. {task['task']} [{status}]")

def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks()

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks()

# Main loop
tasks = load_tasks()

while True:
    print("\n1. View Tasks\n2. Add Task\n3. Mark Complete\n4. Delete Task\n5. Exit")
    choice = input("Choose: ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "3":
        view_tasks()
        index = int(input("Task number to complete: ")) - 1
        complete_task(index)
    elif choice == "4":
        view_tasks()
        index = int(input("Task number to delete: ")) - 1
        delete_task(index)
    elif choice == "5":
        break