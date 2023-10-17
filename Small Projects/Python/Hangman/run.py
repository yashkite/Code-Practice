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

chance = 0

while game_state:

    guess = input("Guess the letter in the word: ")
    
    is_word_present = False

    for letter in fruit:
        if letter is guess:
            is_word_present = True
    
    if is_word_present and chance != 7:
        for letter in range(0,len(fruit)):
            if fruit[letter] == guess:
                out[letter]= guess         
        
        check_letters = len(fruit) 

        for letter in range(0,len(fruit)):
            
            if out[letter] != "_":
                check_letters -= 1
            if check_letters == 0:

                game_state = False
                print("Congratulation You won:- The Word was \"{fruit}\"") 
        print(out)
    else:
        print(pics[chance])
        chance +=1
        if chance == 7:
            game_state = False
            print(f"Game Over: The Word was \"{fruit}\"")
            

            
