from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


machine_on = True

while machine_on:
    user_choice = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "off":
        machine_on = False

    elif user_choice == "report":
        u = CoffeeMaker()
        print( u.report() )



    # elif user_choice in Menu():
    #     selected_drink = Menu[user_choice]
    #     print (0)

    #     if check_resources(selected_drink):
    #         payment = process_coins()
    #
    #         if payment >= selected_drink["cost"]:
    #             change = round(payment - selected_drink["cost"], 2)
    #             if change > 0:
    #                 print(f"Here is ${change} in change.")
    #
    #             make_coffee(user_choice, selected_drink)
    #
    #         else:
    #             print("Sorry that's not enough money. Money refunded.")
    #
    # else:
    #     print("Invalid selection.")