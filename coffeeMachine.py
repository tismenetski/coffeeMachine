MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 0.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 0.75,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 1.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "quarter" : {"value":0.25, "amount":0},
    "dime" : {"value":0.10, "amount":0},
    "nickle" : {"value":0.05, "amount":0},
    "penny" : {"value":0.01, "amount":0},
}
current_input_coins = {
    "quarter" : {"value":0.25, "amount":0},
    "dime" : {"value":0.10, "amount":0},
    "nickle" : {"value":0.05, "amount":0},
    "penny" : {"value":0.01, "amount":0},
}


def report():
    print(resources)

def check_resources(selection):
    """Function responsible for checking if machine has enough resources to process the requested drink"""
    errors = []
    drink = MENU[selection]
    ingredients_of_beverage = drink["ingredients"]

    for ingredient in ingredients_of_beverage:
        if ingredients_of_beverage[ingredient] > resources[ingredient]:
            errors.append(f"Sorry there is not enough {ingredient}")

    if len(errors) > 0:
        print(errors)
        return False
    else:
        return True


def process_coins(selection):
    """Function responsible for taking coins,checking sum of coins equal to drink cost, update money and return change"""
    drink = MENU[selection]
    cost_of_beverage = drink["cost"]
    print(f"Please insert {cost_of_beverage}:")
    coin_insert = True

    while coin_insert:
        coin = (input("Insert quarters - $0.25, dimes - $0.10, nickles - $0.05, pennies - $0.01, s-Stop"))
        if coin != 's':
            for current_coin in current_input_coins.items():
                if current_coin[0] == coin:
                    current_coin[1]["amount"] += 1
        else:
            coin_insert = False

    customer_input = 0
    for current_coin in current_input_coins.items():
        customer_input += current_coin[1]["value"] * current_coin[1]["amount"]
    if customer_input >= cost_of_beverage:
        customer_input -= cost_of_beverage
    else :
        return False  # Not enough money inserted
    if(customer_input==0): #  Case when customer gives exact sum
        for coin in current_input_coins.items():
            coin[1]["amount"] = 0
            if 'money' not in resources.keys():
                resources["money"] = cost_of_beverage
            else:
                resources["money"] += cost_of_beverage
            print(f"Enjoy your {selection}")
            return True


    else:  # Empty current_input_coins, pass money to resources and return change
        for coin in current_input_coins.items():
            while(cost_of_beverage > 0 and coin[1]["amount"]>0 and cost_of_beverage >= coin[1]["value"]):
                cost_of_beverage-= coin[1]["value"]
                coin[1]["amount"]-=1
                if 'money' not in resources.keys():
                    resources["money"] = coin[1]["value"]
                else:
                    resources["money"]+= coin[1]["value"]

        change = 0
        for coin in current_input_coins.items():
                change += coin[1]["value"]*coin[1]["amount"]
                coin[1]["amount"] = 0

        print(f"Enjoy your {selection}")
        print(f"The change is ${change}")
        return True

def brew_drink(selection):
    """Function Responsible for reducing the used ingredients from the machine"""
    drink = MENU[selection]
    ingredients_of_beverage = drink["ingredients"]

    for ingredient in ingredients_of_beverage:
        resources[ingredient] = resources[ingredient] -  ingredients_of_beverage[ingredient]
    #resources[money] += drink[cost]

def main():
    """Function responsible for Coffee Machine functionality and user menu"""
    off = False
    while not off:
        selection = input("What would you like? (espresso/latte/cappuccino report-report off-turn off)")
        if selection == 'off':
            off = True
            break
        if selection == 'report':
            report()
        else:
            if check_resources(selection):
                if process_coins(selection):
                    brew_drink(selection)
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print("Sorry for your inconvenience")

main()