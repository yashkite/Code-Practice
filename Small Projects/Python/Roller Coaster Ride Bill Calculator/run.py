print("Wellcome to the Rollercoster Ride")

bill = 0

hight = float(input("Enter your Hight in CM: "))
age = float(input("Enter your Age: "))
if hight > 120:
    if age < 12:
        print("You have to pay $5")
        bill += 5

    elif 12 <= age <=18:
        print("You have to pay $7")
        bill += 7

    else:
        print("You have to pay $12")
        bill += 12

    want_photos = input("Do you want a photo taken? Y or N.: ")
    if want_photos == "Y":
        bill += 3
    

    print(f"Your bill is {bill}")
else:
    print("Sorry you not eligible for ride")
