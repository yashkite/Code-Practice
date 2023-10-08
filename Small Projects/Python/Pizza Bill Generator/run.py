piza_size = input("Enter the size of the Pizza:- S, M and L: ")
pepperoni = input("Do you like to have Pepperoni on the Pizza:- Y or N: ")
extra_cheese = input("Do you like to have Extra Cheese on the Pizza:- Y or N: ")

bill = 0

match piza_size:
    case "S":
        bill += 5
    case "M":
        bill += 7
    case "L":
        bill += 9


if pepperoni == "Y":
    bill += 2
if extra_cheese == "Y":
    bill += 3

print(f"Your bill for the Pizza is: ${bill}")


