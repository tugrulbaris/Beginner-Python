# I remove log in system at this version, also I add remove case, I made little changes and I improved 'show' case.

print("Welcome! What do you want to do?")
todos = []

while True:
    action = input("Please type add, remove, show, edit or exit. ")
    action = action.strip()

    match action:
        case 'add':
            todo = input("Please enter a to do: ")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                row = f"{index + 1}- {item}"
                print(row)
        case 'edit':
            for index, item in enumerate(todos):
                row = f"{index + 1}- {item}"
                print(row)
            number = int(input("Number of to do to edit: "))
            number = number - 1
            new_todo = input("Please enter a new to do: ")
            todos[number] = new_todo
            print("I updated your to do list!")
        case 'remove':
            for index, item in enumerate(todos):
                row = f"{index + 1}- {item}"
                print(row)
            rmv = int(input("Enter a to do number that you want to remove from your list: "))
            todos.pop(rmv - 1)
            print("I updated your list.")
        case 'exit':
            break

print("See you later!")
