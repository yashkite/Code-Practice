import random
import os

exit = False

while not exit:
    rand_num = random.randint(1,100)

    level = int(input('''
1. Easy
2. Hard
Choose level: '''))
    
    lives = 0

    if level == 1:
        lives = 10
    else:
        lives = 5

    game_over = False
    while lives != 0 and game_over != True:
    
        guess_num = int(input("Guess the number between (0-100): "))

        if guess_num == rand_num:
            print(f"Your Right, The number is {guess_num}")
            game_over = True
        elif guess_num < rand_num:
            print(f"The number is bigger than {guess_num}")
            lives -= 1
            print(f"you have {lives} lives left")

        elif guess_num > rand_num:
            print(f"The number is smaller than {guess_num}")
            lives -= 1
            print(f"you have {lives} lives left")

        if lives == 0:
            print("Game Over")
            game_over = True

    play_again = int(input("""
1. Play Again
2. Exit
Enter the Choice: """))
    if play_again == 1:
        os.system('clear')    
        continue
    else:
        print("Exiting....")
        exit = True
    