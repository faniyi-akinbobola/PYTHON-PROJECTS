MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def account(quarters_entered, dimes_entered, nickels_entered, pennies_entered):
    total_quarters = quarters_entered * 0.25
    total_dimes = dimes_entered * 0.10
    total_nickels = nickels_entered * 0.05
    total_pennies = pennies_entered * 0.01
    total_amount = total_pennies + total_quarters + total_nickels + total_dimes
    return total_amount


cooking = True
while cooking:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        cooking = False
    elif order == "report":
        print(f"water : {resources["water"]}")
        print(f"milk : {resources["milk"]}")
        print(f"coffee : {resources["coffee"]}")
        print(f"money : ${resources["money"]}")
    elif order == "espresso":
        if resources["water"] >= MENU[order]["ingredients"]["water"] and resources["coffee"] >= \
                MENU[order]["ingredients"]["coffee"]:
            print("Please enter coins.")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickels = float(input("How many nickels?: "))
            pennies = float(input("How many pennies?: "))
            amount_account = account(quarters_entered=quarters, dimes_entered=dimes, nickels_entered=nickels,
                                     pennies_entered=pennies)
            change = round(amount_account - MENU[order]["cost"], 2)

            if change > 0:
                print(f"Here is ${change} in change.")
            print(f"Here is your {order}☕.Enjoy!")
            resources["money"] += MENU[order]["cost"]
            resources["water"] -= MENU[order]["ingredients"]["water"]
            resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
        elif resources["water"] < MENU[order]["ingredients"]["water"]:
            print("Not enough water.")
        elif resources["coffee"] < MENU[order]["ingredients"]["coffee"]:
            print("Not enough coffee.")
    else:
        if (resources["water"] >= MENU[order]["ingredients"]["water"] and resources["milk"] >=
                MENU[order]["ingredients"]["milk"] and resources["coffee"] >= MENU[order]["ingredients"]["coffee"]):
            print("Please enter coins.")
            quarters = float(input("How many quarters?: "))
            dimes = float(input("How many dimes?: "))
            nickels = float(input("How many nickels?: "))
            pennies = float(input("How many pennies?: "))
            amount_account = account(quarters_entered=quarters, dimes_entered=dimes, nickels_entered=nickels,
                                     pennies_entered=pennies)
            change = round(amount_account - MENU[order]["cost"], 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            print(f"Here is your {order}☕.Enjoy!")
            resources["money"] += MENU[order]["cost"]
            resources["water"] -= MENU[order]["ingredients"]["water"]
            resources["milk"] -= MENU[order]["ingredients"]["milk"]
            resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
        elif resources["water"] < MENU[order]["ingredients"]["water"]:
            print("Not enough water.")
        elif resources["coffee"] < MENU[order]["ingredients"]["coffee"]:
            print("Not enough coffee.")
        elif resources["milk"] < MENU[order]["ingredients"]["milk"]:
            print("Not enough milk.")
