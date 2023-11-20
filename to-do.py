import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        task_list.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def remove_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove!")

# Create the main application window
app = tk.Tk()
app.title("To-Do List")

# Create and configure the task entry field
entry = tk.Entry(app, width=40)
entry.pack(pady=10)

# Create the "Add Task" button
add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack()

# Create the task list
task_list = tk.Listbox(app, width=40)
task_list.pack(pady=10)

# Create the "Remove Task" button
remove_button = tk.Button(app, text="Remove Task", command=remove_task)
remove_button.pack()

# Start the GUI application
app.mainloop()
