# Rock
import random


print_rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
print_paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
print_scissor ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


def print_choice(num):
    match num:
        case 0:
            print(print_rock)
        case 1:
            print(print_paper)
        case 2:
            print(print_scissor)
        case _:
            print("Invalid Responce")

user_choice = int(input("Enter number for 0 for Rock, 1 for Paper, 2 for Scissor: "))

computer_choice = random.randint(0,2)

print("Computer Choice: ")
print_choice(computer_choice)
print("User Choice: ")
print_choice(user_choice)

if user_choice == 0 and computer_choice == 0:
    print("match draw")
elif user_choice == 0 and computer_choice == 1:
    print("you lose")
elif user_choice == 0 and computer_choice == 2:
    print("you Win")
elif user_choice == 1 and computer_choice == 0:
    print("you Win")
elif user_choice == 1 and computer_choice == 1:
    print("match draw")
elif user_choice == 1 and computer_choice == 2:
    print("you lose")
elif user_choice == 2 and computer_choice == 0:
    print("you lose")
elif user_choice == 2 and computer_choice == 1:
    print("you Win")
elif user_choice == 2 and computer_choice == 2:
    print("match draw")












