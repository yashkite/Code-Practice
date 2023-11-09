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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0


def is_ingredients_available(type_coffee):
    ingredients = type_coffee["ingredients"]
    is_available = True
    for ingredient in ingredients:
        if resources[ingredient] < ingredients[ingredient]:
            print(
                f"Sorry, {ingredient} is not in sufficient quantity to make the drink."
            )
            is_available = False
    return is_available


def process_coins():
    print("\nPlease insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def do_transaction(type_coffee, coins):
    ingredients = type_coffee["ingredients"]
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    change = round(coins - type_coffee["cost"], 2)
    print(
        f"Here is your {type_coffee} and your change is ${change}.\nEnjoy your coffee!"
    )


def make_coffee(type_coffee):
    print(f"\nMaking {type_coffee}...\n")
    if is_ingredients_available(type_coffee):
        coins = process_coins()
        if coins < type_coffee["cost"]:
            print(
                f"Sorry, you have ${coins} but {type_coffee} costs ${type_coffee['cost']}. Money refunded."
            )
        else:
            do_transaction(type_coffee, coins)
            return True
    else:
        print("Some ingredients are missing.")


def display_report(resources):
    print("\nCurrent Resources:")
    for ingredient, quantity in resources.items():
        print(f"{ingredient.capitalize()}: {quantity}")
    print(f"Total Profit: ${profit}")


choice = 0
while choice != 5:
    print("\n===== Coffee Machine Menu =====")
    print("1. Espresso - $1.5")
    print("2. Latte - $2.5")
    print("3. Cappuccino - $3.0")
    print("4. Report")
    print("5. Exit")
    choice = int(input("Enter your choice (1-5): "))

    if choice == 4:
        display_report(resources)
        continue

    if 1 <= choice <= 3:
        drink_type = list(MENU.keys())[choice - 1]
        drink = MENU[drink_type]
        if make_coffee(drink):
            profit += drink["cost"]

print("\nThank you for using the Coffee Machine. Have a great day!")
