import random
list_card = [11,2,3,4,5,6,7,8,9,10,10,10,10,
             11,2,3,4,5,6,7,8,9,10,10,10,10,
             11,2,3,4,5,6,7,8,9,10,10,10,10,
             11,2,3,4,5,6,7,8,9,10,10,10,10]

money = 1000

def pick_card():
    return list_card[random.randint(0,len(list_card))]

def print_stats(computer, user):
    print(f"computer: [{computer[0]}, *] ")
    print(f"user : {user} ")

def card_sum(list):
    return sum(list)

def skip_computer():
    while card_sum(computer) <= 17:
        computer.append(pick_card())
    

exit = True
while money> 0 or not exit:
    user = []
    computer = []
    
    print(f"Your wallet fund is {money}")
    pot = int(input("Enter the Starting bet: "))

    if pot > money:
        print("You dont have enough Money in Wallet")
        continue
    money - pot
    pot = pot * 2
    print(f"Your wallet fund is ${money}")
    print(f"Table: ${pot}")



    computer.append(pick_card())
    user.append(pick_card())
    computer.append(pick_card())
    user.append(pick_card())

    print_stats(computer,user)

    if (card_sum(computer) == 21 or card_sum(user) == 21) and card_sum(computer) != card_sum(user):
        if card_sum(computer) == 21:
            print(f"Computer Wins Blackjack: ${pot}")
            if input("Play Again? : y or n:-") == "y":
                continue
            else:
                break
        else:
            money += pot
            print(f"User Wins Blackjack: ${pot}")
            if input("Play Again? : y or n:-") == "y":
                continue
            else:
                break
    elif card_sum(computer) == card_sum(user):
        print(f"Match Draw: computer-{computer} and user-{user}")
        money += pot/2
    
    else:
        game_continue = True
        while game_continue:
            choice = int(input('''
1. Hit
2. Duble
3. Stand
Enter Choice Number: '''))
            match choice:
                case 1:
                    user.append(pick_card())
                case 2:
                    amount = pot/2
                    if amount > money:
                        print("You dont have enough Money in Wallet")
                        continue
                    else:
                        money -= amount
                        pot = pot * 2
                        user.append(pick_card())
                case 3:
                    skip_computer()
                case _:
                    print(f"Wrong Input: {choice}")
                    continue
            if card_sum(user)==21:
                skip_computer()

            elif card_sum(user)>21:
            

    

