import random

while True:
    answer = input(" 'f' to flip the coin, 'q' to exit: \n ")
    if answer == "f":
        coin = random.randint(0, 1)
        if coin == 1:
            print("heads")
        else:
            print("tails")
    elif answer == "q":
        break

