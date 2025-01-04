import FreeSimpleGUI as sg

# Define file path
FILEPATH = "todos.txt"


# Function to get todos from the file
def get_todos(filepath=FILEPATH):
    """Read a text file and return the list of to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


# Function to write todos to the file
def write_todos(todos_arg, filepath=FILEPATH):
    """Write the to-do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# Get todos from the file
todos = get_todos()

# Define GUI components
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key='todo', enable_events=True, size=(45, 1))
add_button = sg.Button("Add")
list_box = sg.Listbox(values=todos, key="todos", size=(45, 10), select_mode=sg.LISTBOX_SELECT_MODE_SINGLE)
edit_button = sg.Button("Edit")

# Create the window
layout = [[label], [input_box, add_button], [list_box, edit_button]]
window = sg.Window("My To-Do App", layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    match event:
        case "Add":
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            write_todos(todos)
            window['todos'].update(values=todos)
            print("New to-do added:", new_todo)
        case "Edit":
            try:
                selected_todo = values['todos'][0]
                new_todo = values['todo'] + "\n"
                index = todos.index(selected_todo)
                todos[index] = new_todo
                write_todos(todos)
                window['todos'].update(values=todos)
                print("To-do edited:", new_todo)
            except IndexError:
                print("Please select a to-do to edit.")

window.close()




