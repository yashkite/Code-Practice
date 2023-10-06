year = float(input("Enter the year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Its a Leap year")
        else:
            print("Its Not a Leap year")
    else:
        print("Its a Leap year")
else:
    print("Its Not a Leap year")