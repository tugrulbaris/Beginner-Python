print("Welcome to MediStore!")

name = input("Please enter your name: ")
password = input("Please enter your password: ")

while name.lower() != 'bitrays':
    print("Your username was wrong. Please try again: ")
    name = input("Please enter your name: ")

while password != 'dolphin09':
    print("Your password was wrong. Please try again: ")
    password = input("Please enter your password: ")

print("You logged in succesfully.")
medicines = ['Antibiotics $20', 'Xanax $60', 'Ritalin $55', 'Parasetamol $10']
q = input("If you want to see medicines and prices, please type something and enter: ")

for index, item in enumerate(medicines):
    index = int(index)
    index = index + 1
    row = f"{index}- {item}"
    print(row)

prc1qu = 0
prc2qu = 0
prc3qu = 0
prc4qu = 0

while True:
    qmed = input("Please enter number of medicine, when you finish please type finish.")
    match qmed:
        case '1':
            prc1qu += int(input("How much Antibiotic do you want to buy?"))
            print("It costs " + (str(prc1qu*20)) + " $" + "\nI'll sent this to your credit card bills.")
        case '2':
            prc2qu += int(input("How much Xanax do you want to buy?"))
            print("It costs " + (str(prc2qu*60)) + " $" + "\nI'll sent this to your credit card bills.")
        case '3':
            prc3qu += int(input("How much Ritalin do you want to buy?"))
            print("It costs " + (str(prc3qu*55)) + " $" + "\nI'll sent this to your credit card bills.")
        case '4':
            prc4qu += int(input("How much Parasetamol do you want to buy?"))
            print("It costs " + (str(prc4qu*10)) + " $" + "\nI'll sent this to your credit card bills.")
        case 'finish':
            break

print("You finished your shopping.")
print("You bought:")
total = (prc1qu*20) + (prc2qu*60) + (prc3qu*55) + (prc4qu*10)
print("All items costs $ " + str(total) + "\nI've sent your bills to your mobile app.")
print("Thanks for using MediStore, see you later!")

antibiotics = ("Antibiotics $" + str(prc1qu*20) + " | " + str(prc1qu) + " items") + '\n'
xanax = ("Xanax $" + str(prc2qu*60) + " " + str(prc2qu) + " items") + '\n'
ritalin = ("Ritalin $" + str(prc3qu*55) + " " + str(prc3qu) + " items") + '\n'
parasetamol = ("Parasetamol $" + str(prc4qu*55) + " " + str(prc4qu) + " items") + '\n'
prices = ("All items costs $ " + str(total))


file = open('purchases.txt', 'w')
file.writelines("You bought:" + '\n')
file.writelines(antibiotics)
file.writelines(xanax)
file.writelines(ritalin)
file.writelines(parasetamol)
file.writelines(prices)
