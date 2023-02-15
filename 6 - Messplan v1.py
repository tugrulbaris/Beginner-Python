print("Welcome to Messplan!")

messages = []

while True:
    action = input("Please type save, show, info or exit: ")

    match action:
        case 'save':
            name = input("Please type name of your friend: ")
            messages.append(name)

            text = input("Please type your message: ")
            messages.append(text)

            time = input("When should I send this message?")
            messages.append(time)

            print("Okay, I saved your message. Dont forget to check later!")

        case 'show':
            for item in messages:
                print(item.capitalize())

        case 'info':
            print("Hello, my name is Messplan")
            print("My developer designed me so you don't forget your messages.")
            print("Thanks for using me!")

        case 'exit':
            print("See you later!")
            break








