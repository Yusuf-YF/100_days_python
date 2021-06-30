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
}

profits = 0


# TODO: 4. check resources sufficient.
def is_sufficient(order_ingredients):
    """Returns true if payment successful, false if not."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


# TODO: 5. Process coins.
def coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.1
    return total


# TODO: 6. Check transaction successful.
def is_success(money_received, drink_cost):
    """Returns true when payment accepted, false if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here's ${change} in change")
        global profits
        profits += drink_cost
        return True
    else:
        print("Sorry that's not enough money, money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the ingredients"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's {drink_name}, enjoy!")


# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino): continuously"
is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino),'report','r' to show resources, 'off' to turn "
                   "off the machine: ").lower()
    # TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if choice == 'off':
        is_on = False
        print("Powering off...")
    # TODO: 3. Print report.
    elif choice == 'report' or choice == 'r':
        print(f"Water:  {resources['water']}ml")
        print(f"Milk:   {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money:  ${profits}")
    else:
        drink = MENU[choice]
        if is_sufficient(drink["ingredients"]):
            payment = coins()
            if is_success(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
