
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

def is_ingradiants_available(type_coffee):
    ingrediants = type_coffee["ingredients"]
    is_available = True
    for ingrediant in ingrediants:
        if resources[ingrediant] < ingrediants[ingrediant]:
            print(f"{ingrediant} is not in enough quantity to make drink")
            is_available = False
    return is_available

     
    
def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def do_transaction(type_coffee, coins):
    
    ingrediants = type_coffee["ingredients"]
    for ingrediant in ingrediants:
        resources[ingrediant] -= ingrediants[ingrediant]
    change = round(coins - type_coffee['cost'],2)
    print(f"here is your Coffee and your change is ${change}")


def make_coffee(type_coffee):
    
    if is_ingradiants_available(type_coffee):
        coins = process_coins()
        if coins < drink["cost"]:
            print(f"You have ${coins} and Coffee costs ${type_coffee['cost']}")
        else:
            do_transaction(type_coffee, coins)
            return True
    else:
        print("Some ingrediants are missing")

def report(resources):
    for ingrediant in resources:
        print(f"{ingrediant} = {resources[ingrediant]}")
    print(f"Profit = ${profit}")


drink = ""
profit = 0
choice = 0
while choice != 5:
    print("1. Espresso - $1.5 ")
    print("2. Latte - $2.5 ")
    print("3. Cappuccino - $3.0 ")
    print("4. Report")
    print("5. Exit")
    choice = int(input("Enter Your Choice in Numbers: "))
    match choice:
        case 1:
            drink = MENU["espresso"]
        case 2:
            drink = MENU["latte"]
        case 3:
            drink = MENU["cappuccino"]
        case 4:
            report(resources)
            continue
        case 5:
            break
    
    if make_coffee(drink):
        profit += drink['cost']

