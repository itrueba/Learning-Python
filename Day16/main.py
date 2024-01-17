
from menu import MenuItem, Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine(): 
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    
    turned_on = True
    
    while turned_on:
        options = menu.get_items()
        selection = input(f"What would you like? ({options}): ")
        if selection == "off":
            print("The machine has turned OFF")
            turned_on = False
            return
        elif selection == "report":
            coffee_maker.report()
            money_machine.report()
        elif selection in options:
            drink = menu.find_drink(selection)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
        else:
            print("Wrong")


coffee_machine()   
