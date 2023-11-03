import random

question = "Would you like to toss a coin again? (y/n): "

while True:
    coin = random.randint(0,1)
    if coin == 0:
        print("head")
    else:
        print("tails")
    while (ans:=input(question)) not in ["y", "n"]:
        continue
    if ans == "n":
        break