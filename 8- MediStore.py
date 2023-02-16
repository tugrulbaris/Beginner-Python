# This is longest code I've ever made. I'm very happy because I did this!!
# I want to learn more and write more complicated codes. I'm very excited for that!

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
q = input("If you want to see medicines and prices, please type show.")

match q:
    case 'show':
        print("1- Antibiotics $20")
        print("2- Xanax $60")
        print("3- Ritalin $55")
        print("4- Parasetamol $10")

tprice = []

while True:
    qmed = input("Please enter number of medicine, when you finish please type finish.")

    match qmed:
        case '1':
            prc1 = input("How much Antibiotic do you want to buy?")
            prc1 = int(prc1)
            total1 = (prc1 * 20)
            total1 = str(total1)
            print("It costs " + total1 + " $" + "\nI'll sent this to your credit card bills.")
            total1 = int(total1)
            tprice.append(total1)
        case '2':
            prc2 = input("How much Xanax do you want to buy?")
            prc2 = int(prc2)
            total2 = (prc2 * 60)
            total2 = str(total2)
            print("It costs " + total2 + " $" + "\nI'll sent this to your credit card bills.")
            total2 = int(total2)
            tprice.append(total2)
        case '3':
            prc3 = input("How much Ritalin do you want to buy?")
            prc3 = int(prc3)
            total3 = (prc3 * 55)
            total3 = str(total3)
            print("It costs " + total3 + " $" + "\nI'll sent this to your credit card bills.")
            total3 = int(total3)
            tprice.append(total3)
        case '4':
            prc4 = input("How much Parasetamol do you want to buy?")
            prc4 = int(prc4)
            total4 = (prc4 * 10)
            total4 = str(total4)
            print("It costs " + total4 + " $" + "\nI'll sent this to your credit card bills.")
            total4 = int(total4)
            tprice.append(total4)

        case 'finish':
            break

print("You finished your shopping.")
stprice = sum(tprice)
stprice = str(stprice)
print("All items costs $ " + stprice + "\nI've sent your bills to your mobile app.")
print("Thanks for using MediStore, see you later!")
