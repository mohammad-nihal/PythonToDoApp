from Functions import functions
import PySimpleGUI as sg
import time

sg.theme("DarkPurple4")
label_clock = sg.Text('', key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button(size=10,image_source="add.png",tooltip="Add todo", key="Add")
list_box = sg.Listbox(values=functions.get_todos('../Files/todos.txt'), key='todos',
                      enable_events=True, size=(45,10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[label_clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]
                           ],
                   font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=200)  #<- will excute every 200 ms
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # print(event)
    # print(values)
    match event:
        case "Add":
            todos = functions.get_todos('../Files/todos.txt')
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos,'../Files/todos.txt')
            window['todos'].update(values=todos)  #<- point to key of list_box
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos('../Files/todos.txt')
                index = todos.index(todo_to_edit)
                todos[index]=new_todo + '\n'
                functions.write_todos(todos,'../Files/todos.txt')
                window['todos'].update(values=todos)  #<- point to key of list_box
            except IndexError:
                sg.popup("Please select an item first",
                         font=('Helvetica', 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]

                todos = functions.get_todos('../Files/todos.txt')
                todos.remove(todo_to_complete)
                functions.write_todos(todos,'../Files/todos.txt')
                window['todos'].update(values=todos)  #<- point to key of list_box
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first",
                         font=('Helvetica', 20))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0]) #<- point to key of input_box
        case sg.WIN_CLOSED:
            break

window.close()