def get_todos(filepath='Files/todos.txt'):    #function definition
    """
    This is a function to get todos from a file.
    And you are looking at an example of doc stream
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg,filepath='Files/todos.txt'):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
