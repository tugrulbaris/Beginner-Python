# Yo Messplan isnt working, I made this for just training my python skills.
# At this version when u type show, scheduled messages looks better than first version.
# Note to future: I cant study python rn because of earthquake man, hope we'll escape from this fucking situation see you. 

print("Welcome to Messplan!")

messages = []

while True:
    action = input("Please type save, show, info or exit: ")

    match action:
        case 'save':
            name = input("Please type name of your friend: ")
            text = input("Please type your message: ")
            time = input("When should I send your message? ")

            stext = ("I'll send this message: " + text + " to " + name.capitalize() + " at " + time)
            messages.append(stext)

            print("I'll send your message at " + time + " to " + name.capitalize())

        case 'show':
            print("Scheduled messages:")
            for item in messages:
                print(item)

        case 'info':
            print("Hello, my name is Messplan")
            print("My developer designed me so you don't forget your messages.")
            print("Thanks for using me!")

        case 'exit':
            print("See you later!")
            break
