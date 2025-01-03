import tkinter as tk
from tkinter import messagebox
from functions import get_todos, write_todos


def add_todo():
    todo = todo_entry.get()
    if todo:
        todos = get_todos()
        todos.append(todo + '\n')
        write_todos(todos)
        listbox.insert(tk.END, todo)
        todo_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Todo added successfully!")
    else:
        messagebox.showwarning("Warning", "You must enter a todo")


def show_todos():
    todos = get_todos()
    listbox.delete(0, tk.END)
    for todo in todos:
        listbox.insert(tk.END, todo.strip())


def edit_todo():
    try:
        index = listbox.curselection()[0]
        new_todo = todo_entry.get()
        if new_todo:
            todos = get_todos()
            todos[index] = new_todo + '\n'
            write_todos(todos)
            listbox.delete(index)
            listbox.insert(index, new_todo)
            messagebox.showinfo("Success", "Todo edited successfully!")
        else:
            messagebox.showwarning("Warning", "You must enter a new todo")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a todo to edit")


def complete_todo():
    try:
        index = listbox.curselection()[0]
        todos = get_todos()
        todo_to_remove = todos.pop(index).strip()
        write_todos(todos)
        listbox.delete(index)
        messagebox.showinfo("Info", f'Todo {todo_to_remove} was removed from the list.')
    except IndexError:
        messagebox.showwarning("Warning", "You must select a todo to complete")


# Main app window
app = tk.Tk()
app.title("Beautiful Todo App")
app.geometry("500x450")
app.configure(bg="#f0f0f0")

# Frame for entry and add button
frame = tk.Frame(app, bg="#f0f0f0")
frame.pack(pady=20)

# Entry box for new todos
todo_entry = tk.Entry(frame, width=40, font=("Arial", 12))
todo_entry.pack(side=tk.LEFT, padx=10)

# Add button
add_button = tk.Button(frame, text="Add Todo", command=add_todo, bg="#4CAF50", fg="white", font=("Arial", 12), padx=10)
add_button.pack(side=tk.LEFT)

# Listbox to display todos
listbox = tk.Listbox(app, width=50, height=10, font=("Arial", 12), selectbackground="#4CAF50")
listbox.pack(pady=20)

# Frame for action buttons
button_frame = tk.Frame(app, bg="#f0f0f0")
button_frame.pack(pady=10)

# Show button
show_button = tk.Button(button_frame, text="Show Todos", command=show_todos, bg="#2196F3", fg="white", font=("Arial", 12), padx=10)
show_button.grid(row=0, column=0, padx=5)

# Edit button
edit_button = tk.Button(button_frame, text="Edit Todo", command=edit_todo, bg="#FFC107", fg="white", font=("Arial", 12), padx=10)
edit_button.grid(row=0, column=1, padx=5)

# Complete button
complete_button = tk.Button(button_frame, text="Complete Todo", command=complete_todo, bg="#F44336", fg="white", font=("Arial", 12), padx=10)
complete_button.grid(row=0, column=2, padx=5)

app.mainloop()




