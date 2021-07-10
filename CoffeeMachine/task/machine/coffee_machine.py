water = 400
milk = 540
coffee = 120
cups = 9
money = 550


def inventory():
    print(f"""The coffee machine has:
    {water} of water
    {milk} of milk
    {coffee} of coffee beans
    {cups} of disposable cups
    ${money} of money""")
    user_choice()


def buy():
    global water, milk, coffee, cups, money
    order = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    if order == "1":
        if water < 250:
            print("Sorry, not enough water!")
            return user_choice()
        elif coffee < 16:
            print("Sorry, not enough coffee!")
            return user_choice()
        elif cups < 1:
            print("Sorry, not enough cups!")
            return user_choice()
        else:
            print("I have enough resources, making you a coffee!")
            water -= 250
            coffee -= 16
            cups -= 1
            money += 4
            return water, coffee, cups, money, user_choice()
    if order == "2":
        if water < 350:
            print("Sorry, not enough water!")
            return user_choice()
        elif milk < 75:
            print("Sorry, not enough milk!")
            return user_choice()
        elif coffee < 20:
            print("Sorry, not enough coffee!")
            return user_choice()
        elif cups < 1:
            print("Sorry, not enough cups!")
            return user_choice()
        else:
            print("I have enough resources, making you a coffee!")
            water -= 350
            milk = milk - 75
            coffee -= 20
            cups -= 1
            money += 7
            return water, milk, coffee, cups, money, user_choice()
    if order == "3":
        if water < 200:
            print("Sorry, not enough water!")
            return user_choice()
        elif milk < 100:
            print("Sorry, not enough milk!")
            return user_choice()
        elif coffee < 12:
            print("Sorry, not enough coffee!")
            return user_choice()
        elif cups < 1:
            print("Sorry, not enough cups!")
            return user_choice()
        else:
            print("I have enough resources, making you a coffee!")
            water -= 200
            milk -= 100
            coffee -= 12
            cups -= 1
            money += 6
            return water, milk, coffee, cups, money, user_choice()
    if order == "back":
        return user_choice()


def fill():
    global water, milk, coffee, cups
    add_water = int(input("Write how many ml of water you want to add:"))
    add_milk = int(input("Write how many ml of milk you want to add:"))
    add_coffee = int(input("Write how many grams of coffee beans you want to add:"))
    add_cups = int(input("Write how many disposable coffee cups you want to add"))
    water += add_water
    milk += add_milk
    coffee += add_coffee
    cups += add_cups
    return water, milk, coffee, cups, user_choice()


def take():
    global money
    print(f'I gave you ${money}')
    money = 0
    return money, user_choice()


def user_choice():
    choice = input("Write action (buy, fill, take, remaining, exit):")
    if choice == "exit":
        exit()
    elif choice == "buy":
        return buy()
    elif choice == "take":
        return take()
    elif choice == "fill":
        return fill()
    elif choice == "remaining":
        return inventory()


user_choice()
