from database import data
import random

exit = False

while not exit:
    
    points = 0 
    game_over = False
    option_b = random.choice(data)
    while not game_over:
        option_a = option_b
        option_b = random.choice(data)
        if option_a == option_b:
            continue
        
        name_a = option_a["name"]
        name_b = option_b["name"]
        follow_count_a = option_a["follower_count"]
        follow_count_b = option_b["follower_count"]
        print(f"1. {name_a}")
        print(f"2. {name_b}")
        
        choice = int(input("Who has More followers 1 or 2: "))

        if choice == 1 and follow_count_a > follow_count_b:
            print("Your Right")
            points += 1
            continue
        elif choice == 2 and follow_count_a < follow_count_b:
            print("Your Right")
            points += 1
            continue
        else:
            print("Game Over")
            print(f"You Won {points} points !!!")
            game_over = True

    play_again = int(input("""
1. Play Again
2. Exit
Enter the Choice: """))
    
    if play_again == 1:
        continue
    else:
        exit = True
        print("Exiting...")



