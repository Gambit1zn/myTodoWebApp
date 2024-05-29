FILEPATH = "todos.txt"


def get_todos(path=FILEPATH):
    """This is a function that returns the todo_ items from a file"""

    with open(path, 'r') as file_local:
        todos_local = file_local.readlines()

    return todos_local


def write_todos(todos_arg, filepath='files/todos.txt'):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)
