name = input("Please enter your username: ")
password = input("Please enter your password: ")

while name.lower() != ("bitrays"):
    print("Your username was wrong, please try again.")
    name = input("Please enter your username:")

while password != "mylovelyfriend":
    print("Your password was wrong, please try again.")
    password = input("Please enter your password: ")

print("Welcome back again " + name + ", have a nice day!")
