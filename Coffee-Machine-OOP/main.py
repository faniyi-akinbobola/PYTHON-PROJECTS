from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

brewing = True
while brewing:
    order = input(f"What would you like ({menu.get_items()}): ")
    if order == "report":
        coffeemaker.report()
        moneymachine.report()
    elif order == "off":
        brewing = False
    else:
        drink = menu.find_drink(order)
        menuitem = MenuItem(drink.name, drink.ingredients["water"], drink.ingredients["milk"], drink.ingredients["coffee"],
                            drink.cost)
        if coffeemaker.is_resource_sufficient(menuitem):
            payment = moneymachine.make_payment(drink.cost)
            if payment:
                coffeemaker.make_coffee(drink)