def get_todos(filepath="files/todos.txt"):
    """ Read a text file and return a list
    of to-do list of items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="files/todos.txt"):
    """ Write to-do list items in text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# if __name__ == "__main__":
#     print("Hello")

# This script is executed prior to code in main
# Output:
# Hello from functions
# Type add, show, edit, complete, or exit: