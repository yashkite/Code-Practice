row1 = ["🥲","🥲","🥲"]
row2 = ["🥲","🥲","🥲"]
row3 = ["🥲","🥲","🥲"]

map = str(f"{row1}\n{row2}\n{row3}")

print(map)

x_location = input("Enter the location in xy number format like \"23\" to put \"x\" there: ")

row = int(x_location[1])
column = int(x_location[0])

if 1<= row <=3  and 1<= column <=3 :
    match row:
        case 1:
            row1[column-1] = "x" 
        case 2:
            row2[column-1] = "x" 
        case 3:
            row3[column-1] = "x"

else:
    print("Invalid Input")

map= str(f"{row1}\n{row2}\n{row3}")
print(map)







