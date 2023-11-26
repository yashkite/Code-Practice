class Drink:
    def __init__(self, name, ingredients, cost):
        self.name = name
        self.ingredients = ingredients
        self.cost = cost


class CoinProcessor:
    @staticmethod
    def process_coins():
        print("Please insert coins.")
        total = int(input("how many quarters?: ")) * 0.25
        total += int(input("how many dimes?: ")) * 0.1
        total += int(input("how many nickles?: ")) * 0.05
        total += int(input("how many pennies?: ")) * 0.01
        return total

    @staticmethod
    def do_transaction(drink_cost, coins):
        change = round(coins - drink_cost, 2)
        print(f"Here is your Coffee and your change is ${change}")
        return change


class CoffeeMachine:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
        self.drinks = {
            "espresso": Drink("espresso", {"water": 50, "coffee": 18}, 1.5),
            "latte": Drink("latte", {"water": 200, "milk": 150, "coffee": 24}, 2.5),
            "cappuccino": Drink("cappuccino", {"water": 250, "milk": 100, "coffee": 24}, 3.0)
        }
        self.profit = 0
        self.coin_processor = CoinProcessor()

    def is_ingredients_available(self, drink):
        for ingredient, amount in drink.ingredients.items():
            if self.resources[ingredient] < amount:
                print(f"{ingredient} is not in enough quantity to make {drink.name}")
                return False
        return True

    def make_coffee(self, drink):
        if self.is_ingredients_available(drink):
            coins = self.coin_processor.process_coins()
            if coins < drink.cost:
                print(f"You have ${coins}, but the drink costs ${drink.cost}.")
                return False
            else:
                for ingredient, amount in drink.ingredients.items():
                    self.resources[ingredient] -= amount
                self.profit += self.coin_processor.do_transaction(drink.cost, coins)
                return True
        else:
            print("Some ingredients are missing.")
            return False

    def report(self):
        for ingredient, amount in self.resources.items():
            print(f"{ingredient}: {amount}ml/g")
        print(f"Profit: ${self.profit}")

    def run(self):
        while True:
            print("1. Espresso - $1.5 ")
            print("2. Latte - $2.5 ")
            print("3. Cappuccino - $3.0 ")
            print("4. Report")
            print("5. Exit")
            choice = int(input("Enter Your Choice in Numbers: "))
            match choice:
                case 1:
                    self.make_coffee(self.drinks["espresso"])
                case 2:
                    self.make_coffee(self.drinks["latte"])
                case 3:
                    self.make_coffee(self.drinks["cappuccino"])
                case 4:
                    self.report()
                case 5:
                    break


# To run the coffee machine
coffee_machine = CoffeeMachine()
coffee_machine.run()
