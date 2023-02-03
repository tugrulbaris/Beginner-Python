print("Welcome to my special to do list app!")

name = input("Please enter your username: ")
passw = input("Please enter your password: ")

while name.lower() != 'bitrays':
    print("Your username was wrong. Please try again!")
    name = input("Please enter your username: ")

while passw != 'littleboy':
    print("Your password was wrong. Please try again!")
    passw = input("Please enter your password: ")

print("Welcome! What do you want to do?")

todos = []

while True:
    action = input("Please type add, show or exit. ")
    action = action.strip()

    match action:
        case 'add':
            todo = input("Please enter a to do: ")
            todos.append(todo)

        case 'show':
            for item in todos:
                print(item)

        case 'exit':
            break

print("See you later!")
