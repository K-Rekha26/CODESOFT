import tkinter as tk
from tkinter import messagebox, simpledialog

# Function to add a task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Function to clear all tasks
def clear_tasks():
    tasks_listbox.delete(0, tk.END)

# Function to update a selected task
def update_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        existing_task = tasks_listbox.get(selected_task_index)
        new_task = simpledialog.askstring("Update Task", f"Update task '{existing_task}':")
        if new_task:
            tasks_listbox.delete(selected_task_index)
            tasks_listbox.insert(selected_task_index, new_task)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to update.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create a frame for the task entry box and buttons
frame = tk.Frame(root)
frame.pack(pady=10)

# Create a task entry box
task_entry = tk.Entry(frame, width=50)
task_entry.pack(side=tk.LEFT, padx=10)

# Create an Add Task button
add_task_button = tk.Button(frame, text="Add Task", command=add_task)
add_task_button.pack(side=tk.LEFT)

# Create a listbox to display tasks
tasks_listbox = tk.Listbox(root, width=50, height=10)
tasks_listbox.pack(pady=10)

# Create an Update Task button
update_task_button = tk.Button(root, text="Update Task", command=update_task)
update_task_button.pack(pady=5)

# Create a Delete Task button
delete_task_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_task_button.pack(pady=5)

# Create a Clear Tasks button
clear_tasks_button = tk.Button(root, text="Clear Tasks", command=clear_tasks)
clear_tasks_button.pack(pady=5)

# Run the main loop
root.mainloop()
