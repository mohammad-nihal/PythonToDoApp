while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            # file = open('Files/todos.txt', 'r')
            # todos = file.readlines()
            # file.close()   # always close open files, after processing

            # file handling can be replaced with a with-context manager
            # this will ensure file is closed on completion of required actions
            with open('Files/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('Files/todos.txt', 'w') as file:
                file.writelines(todos)
        case 'show':
            with open('Files/todos.txt', 'r') as file:
                todos = file.readlines()

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
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number -= 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            number -= 1
            todos.pop(number)
        case 'exit':
            break
        case whatever:
#or use case _ : < this will also work
            print("You typed an unknown command")

print("Bye!")