import random
from extra import MENU 
from extra import resources 
from extra import profit 
from extra import coins

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

def is_enough_resources(order_ingredients):
    
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    total = 0
    for coin in coins:
        total += int(input(f"how many {coin}?: ")) * coins[coin]
    return total

def make_coffee(selection, order_ingredients):
    
    for item in order_ingredients:
        resources[item] -=order_ingredients[item]

    print(f"Here is your {selection} ☕️. Enjoy!")

def coffee_machine():
    turned_on = True
    global profit
    while turned_on:
        selection = input("What would you like? (espresso/latte/cappuccino): ")
        if selection == "off":
            print("The machine has turned OFF")
            turned_on = False
            return
        elif selection == "report":
            print_report()
        elif selection in MENU :
            coffee_ingredients = MENU[selection]["ingredients"]
            if is_enough_resources(coffee_ingredients):
                user_coins = process_coins() 
                coffee_cost = MENU[selection]["cost"]
                if coffee_cost < user_coins:
                    make_coffee(selection, MENU[selection]["ingredients"])
                    profit += coffee_cost
                    change = round(user_coins - coffee_cost, 2)
                    print(f"Here is ${change} dollars in change.")
                else:
                    print("Sorry that's not enough money. Money refunded.")    
        else:
            print("Wrong")


coffee_machine()