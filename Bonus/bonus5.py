waiting_list = ["sen", "ben", "john"]

waiting_list.sort() #sort list

for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)


#you can also use three variables
buttons = [('John', 'Sen', 'Morro'), ('Lin', 'Ajay', 'Filip'), ('Chen', 'Vijay', 'Malte')]
for first, second, third in buttons:
    print(first, second, third)