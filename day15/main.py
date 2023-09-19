import os
from art import logo

print(logo)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')



from data import MENU, resources

Water_amount = resources["water"]
Milk_amount = resources["milk"]
Coffee_amount = resources["coffee"]
Money_amount = resources["money"]


def resources_check(coffee_type):

    global Water_amount, Milk_amount, Coffee_amount, Money_amount

    espresso_ingredients = MENU["espresso"]["ingredients"]
    latte_ingredients = MENU["latte"]["ingredients"]
    cappuccino_ingredients = MENU["cappuccino"]["ingredients"]
    
    espresso_water = espresso_ingredients["water"]
    espresso_coffee = espresso_ingredients["coffee"]
    espresso_money = MENU["espresso"]["cost"]

    latte_water = latte_ingredients["water"]
    latte_milk = latte_ingredients["milk"]
    latte_coffee = latte_ingredients["coffee"]
    latte_money = MENU["latte"]["cost"]

    cappuccino_water = cappuccino_ingredients["water"]
    cappuccino_milk = cappuccino_ingredients["milk"]
    cappuccino_coffee = cappuccino_ingredients["coffee"]
    cappuccino_money = MENU["cappuccino"]["cost"]

    water_check = False
    milk_check = False
    coffee_check = False

    if coffee_type == "espresso":

        if Water_amount >= espresso_water:
            water_check = True
        else:
            print("Not enough Water! ")
        if Coffee_amount >= espresso_coffee:
            coffee_check = True
        else:
            print("Not enough Coffee! ")

    elif coffee_type == "latte":

        if Water_amount >= latte_water:
            water_check = True
        else:
            print("Not enough Water! ")
        if Coffee_amount >= latte_coffee:
            coffee_check = True
        else:
            print("Not enough Coffee! ")
        if Milk_amount >= latte_milk:
            milk_check = True
        else:
            print("Not enough Milk! ")
        
    else:
        if Water_amount >= cappuccino_water:
            water_check = True
        else:
            print("Not enough Water! ")
        if Coffee_amount >= cappuccino_coffee:
            coffee_check = True
        else:
            print("Not enough Coffee! ")
        if Milk_amount >= cappuccino_milk:
            milk_check = True
        else:
            print("Not enough Milk! ")

    full_check = (water_check == True and coffee_check == True and milk_check == True)

    if coffee_type == "espresso" and water_check == True and coffee_check == True:
        Water_amount = Water_amount - espresso_water
        Coffee_amount = Coffee_amount - espresso_coffee
        Money_amount += espresso_money
        full_check = True
    elif coffee_type == "latte" and full_check == True:
        Water_amount = Water_amount - latte_water
        Milk_amount = Milk_amount - latte_milk
        Coffee_amount = Coffee_amount - latte_coffee
        Money_amount += latte_money
    elif coffee_type == "cappuccino" and full_check == True:
        Water_amount = Water_amount - cappuccino_water
        Milk_amount = Milk_amount - cappuccino_milk
        Coffee_amount = Coffee_amount - cappuccino_coffee
        Money_amount += cappuccino_money
    
    return full_check


def process_coins(coffee_type):

    print("Please insert coins: ")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    sum = round((quarters * 0.25 ) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01), 2)

    espresso_cost = MENU["espresso"]["cost"]
    latte_cost = MENU["latte"]["cost"]
    cappuccino_cost = MENU["cappuccino"]["cost"]

    money_flag = False

    if coffee_type == "espresso":
        if sum >= espresso_cost:
            print(f"Here is ${round((sum - espresso_cost),2)} in change")
            money_flag = True
        else:
            print("Sorry that's not enough money. money is refunded")
    elif coffee_type == "latte":
        if sum >= latte_cost:
            print(f"Here is ${round((sum - latte_cost),2)} in change")
            money_flag = True
        else:
            print("Sorry that's not enough money. money is refunded")
    else:
        if sum >= cappuccino_cost:
            print(f"Here is ${round((sum - cappuccino_cost),2)} in change")
            money_flag = True
        else:
            print("Sorry that's not enough money. money is refunded")

    return money_flag


def Coffee_Machine():

    global Water_amount, Milk_amount, Coffee_amount, Money_amount

    coffee_input_check = True
    while coffee_input_check:
        coffee = input("\nWhat would you like? espresso/latte/cappuccino! or 'resources' or 'off': ").lower()
        if coffee == "espresso" or coffee == "latte" or coffee == "cappuccino" or coffee == "off" or coffee == "resources":
            coffee_input_check = False
        else:
            print("Invalid Entry! Enter again.")

    is_enough_money = False
    
    if coffee == "espresso" or coffee == "latte" or coffee == "cappuccino":
        are_resources_available = resources_check(coffee)
        if are_resources_available == True:
            is_enough_money = process_coins(coffee)
    elif coffee == "off":
        clear_console()
        print("Turning off the coffee machine. Goodbye!")
        exit()
    else:
        print(f"Water: {Water_amount}ml")
        print(f"Milk: {Milk_amount}ml")
        print(f"Coffee: {Coffee_amount}g")
        print(f"Money: ${Money_amount}")

    if is_enough_money == True and are_resources_available == True:
        print(f"Here is your {coffee} ☕ Enjoy!")

while True:
    Coffee_Machine()