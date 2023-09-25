def get_todos(filepath="/Users/tlede/Desktop/Python/CompletedApps/ToDo/files/todo.txt"):
    # """ Read a text file and return a list
    # of to-do list of items.
    # """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="/Users/tlede/Desktop/Python/CompletedApps/ToDo/files/todo.txt"):
    # """ Write to-do list items in text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


