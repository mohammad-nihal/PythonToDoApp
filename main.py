todos = []

while True:
    user_action = input("Type add, show, edit or exit:")
    user_action = user_action.strip()
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                row=f"{index}-{item}"  # f string
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'exit':
            break
        case whatever:
#or use case _ : < this will also work
            print("You typed an unknown command")

print("Bye!")