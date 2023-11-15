import random
import os

money = 1000


def pick_card():
    random_index = random.randrange(len(list_card))
    random_number = list_card.pop(random_index)
    return random_number


def print_stats(computer, user):
    if computer:
        print(f"Computer: [{computer[0]}, *] ")
    else:
        print("Computer: []")

    print(f"User: {user} = Sum {card_sum(user)} ")
    print(f"Your Wallet Fund: ${money}")


def card_sum(cards):
    return sum(cards)


def skip_computer():
    while card_sum(computer) <= 17:
        computer.append(pick_card())


def display_winner():
    global money
    if card_sum(computer) == card_sum(user):
        print(f"Match Draw: Computer-{computer} and User-{user}")
        money += pot / 2
    elif card_sum(computer) > 21 or (21 >= card_sum(user) > card_sum(computer)):
        print(f"User Wins: ${pot}")
        money += pot
    else:
        print("Computer Wins!")


def play_again():
    return input("Play Again? (y/n):").lower() == "y"


exit_game = False

while money > 0 and not exit_game:
    list1 = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    list2 = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    list3 = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    list4 = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    list_card = list1 + list2 + list3 + list4

    user = []
    computer = [pick_card()]  # Initialize computer with one card

    print(f"Your Wallet Fund: ${money}")
    pot = int(input("Enter the Starting Bet: "))

    if pot > money:
        print("You don't have enough money in your wallet")
        continue

    money -= pot
    pot *= 2

    print_stats(computer, user)

    computer.append(pick_card())
    user.append(pick_card())
    computer.append(pick_card())
    user.append(pick_card())

    if card_sum(computer) == 22:
        computer.remove(11)
        computer.append(1)

    if card_sum(user) == 22:
        user.remove(11)
        user.append(1)

    print_stats(computer, user)

    if card_sum(computer) == 21 or card_sum(user) == 21:
        display_winner()
        if play_again():
            continue
        else:
            exit_game = True
            break

    while True:
        choice = int(
            input(
                """
1. Hit
2. Double
3. Stand
Enter Choice Number: """
            )
        )

        if choice == 1:
            user.append(pick_card())
            if card_sum(user) < 21:
                print_stats(computer, user)
                continue
            else:
                print("Game Over!")
                display_winner()
                exit_game = True
                break
        elif choice == 2:
            amount = pot / 2
            if amount > money:
                print("You don't have enough money in your wallet.")
                continue
            else:
                money -= amount
                pot *= 2
                user.append(pick_card())
                if card_sum(user) > 21:
                    print("Game Over!")
                    display_winner()
                    exit_game = True
                    break
                elif card_sum(user) == 21:
                    skip_computer()
                    display_winner()
                    if play_again():
                        break
                    else:
                        exit_game = True
                        break
        elif choice == 3:
            skip_computer()
            display_winner()
            if play_again():
                break
            else:
                exit_game = True
                break
        else:
            print(f"Wrong Input: {choice}")
            continue

        skip_computer()

        if card_sum(computer) == card_sum(user):
            print(f"Match Draw: Computer-{computer} and User-{user}")
            money += pot / 2
            display_winner()
            if play_again():
                break
            else:
                exit_game = True
                break
        elif card_sum(computer) > 21:
            print(f"User Wins: ${pot}")
            money += pot
            display_winner()
            if play_again():
                break
            else:
                exit_game = True
                break
        elif 21 >= card_sum(user) > card_sum(computer):
            print(f"User Wins: ${pot}")
            money += pot
            display_winner()
            if play_again():
                break
            else:
                exit_game = True
                break
        else:
            print("Game Over!")
            display_winner()
            if play_again():
                break
            else:
                exit_game = True
                break

    os.system("cls")
