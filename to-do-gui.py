import tkinter as tk
from tkinter import messagebox

tasks = []

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        tasks.pop(selected[0])
        update_listbox()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def mark_complete():
    selected = listbox.curselection()
    if selected:
        task = tasks[selected[0]]
        tasks[selected[0]] = f"✔ {task}"
        update_listbox()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to mark complete.")

# Create main window
root = tk.Tk()
root.title("To-Do List App")

# Entry widget
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Buttons
tk.Button(root, text="Add Task", command=add_task).pack()
tk.Button(root, text="Delete Task", command=delete_task).pack()
tk.Button(root, text="Mark as Complete", command=mark_complete).pack()

# Listbox to display tasks
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# Run the application
root.mainloop()