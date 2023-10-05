total_bill = input("What is the Total Bill?: ")
tip_percentage = input("Enter the Tip Percentage: ")
split_number = input("In how many peoples have to split the bill: ")

per_person = str(((float(tip_percentage)/100 * float(total_bill)) + float(total_bill) )/float(split_number))


print("Per person will have to pay: $" + per_person )