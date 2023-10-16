import random

pics = ["  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========", 

        "  +---+\n  |   |\n  O   |\n /|\  |\n      |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n /    |\n      |\n=========",

        "  +---+\n  |   |\n  O   |\n /|\  |\n / \  |\n      |\n========="] 

fruits = ["apple", "orange", "banana", "mango", "grape"]

fruit = fruits[random.randint(0,len(fruits)-1)]

out = []
for x in range(0,len(fruit)):
    out.append("_")

game_state = True

while game_state:

    guess = input("Guess the letter in the word: ")
    
    # is_word_present = True

    for letter in range(0,len(fruit)):

        if fruit[letter] == guess:
            out[letter]= guess         
    

    



    check_letters = len(fruit) 

    for letter in range(0,len(fruit)):
         
        if out[letter] != "_":
            check_letters -= 1
        if check_letters == 0:

            game_state = False
            print("won") 

    print(out)