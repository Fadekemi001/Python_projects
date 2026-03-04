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
    "money": 0
}


def print_report():
    """Print current resource values"""
    for key, value in resources.items():
        if key == "money":
            print(f"{key}: ${value}")
        else:
            print(f"{key}: {value}ml")


def check_resources(drink):
    """Return True if resources are enough, otherwise False"""
    for ingredient in drink["ingredients"]:
        if resources[ingredient] < drink["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def process_coins():
    """Return total money inserted"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    return quarters + dimes + nickels + pennies


def make_coffee(drink_name, drink):
    """Deduct ingredients and add money"""
    for ingredient in drink["ingredients"]:
        resources[ingredient] -= drink["ingredients"][ingredient]

    resources["money"] += drink["cost"]
    print(f"Here is your {drink_name} ☕. Enjoy!")


# ---------------- MAIN LOOP ---------------- #

machine_on = True

while machine_on:
    user_choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        machine_on = False

    elif user_choice == "report":
        print_report()

    elif user_choice in MENU:
        selected_drink = MENU[user_choice]

        if check_resources(selected_drink):
            payment = process_coins()

            if payment >= selected_drink["cost"]:
                change = round(payment - selected_drink["cost"], 2)
                if change > 0:
                    print(f"Here is ${change} in change.")

                make_coffee(user_choice, selected_drink)

            else:
                print("Sorry that's not enough money. Money refunded.")

    else:
        print("Invalid selection.")






