while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            file = open('Files/todos.txt', 'r')
            todos = file.readlines()
            file.close()   # always close open files, after processing

            todos.append(todo)

            file = open('Files/todos.txt', 'w') #Path is relative to project directory
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('Files/todos.txt', 'r')
            todos = file.readlines()
            file.close()   # always close open files, after processing

            new_todos = []

            for item in todos:
                new_item = item.strip('\n')
                new_todos.append(new_item)

            for index, item in enumerate(new_todos):
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