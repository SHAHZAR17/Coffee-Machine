from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money = MoneyMachine()
c_maker = CoffeeMaker()
c_menu = Menu()

while True:
    order_name = input(f"What would you like? ({c_menu.get_items()}):").lower()
    if order_name == "report":
        c_maker.report()
        money.report()
    elif order_name == "espresso" or order_name == "latte" or order_name == "cappuccino":
        drink = c_menu.find_drink(order_name)
        if c_maker.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                c_maker.make_coffee(drink)
    elif order_name == "off":
        break