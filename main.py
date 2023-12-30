def get_todos(filepath='Files/todos.txt'):    #function definition
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local

def write_todos(todos_arg,filepath='Files/todos.txt'):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"

        # file = open('Files/todos.txt', 'r')
        # todos = file.readlines()
        # file.close()   # always close open files, after processing

        # file handling can be replaced with a with-context manager
        # this will ensure file is closed on completion of required actions
        todos = get_todos()

        todos.append(todo)

        write_todos(todos, 'Files/todos.txt') # order matters, else specify which arg is being passed.
    elif 'show' in user_action:
        todos = get_todos()

        # new_todos = []

        # for item in todos:
        #     new_item = item.strip('\n')
        #     new_todos.append(new_item)

        # list comprehension achieves the same as the for loop above in a single line
        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')   # alternately, you can add strip here insead of for loop or list comprehension
            row=f"{index + 1 }-{item}"  # f string
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number -= 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith('complete'):
        try:
            todos = get_todos()

            number = int(user_action[9:])
            number -= 1
            todo_to_remove = todos[number].strip('\n')
            todos.pop(number)

            write_todos(todos)

            print(f"To do {todo_to_remove} was removed from list.")
        except IndexError:
            print("There is no items with that number.")
            continue
    elif 'exit' in user_action:
        break
    else:
        print("Command is not valid")

print("Bye!")