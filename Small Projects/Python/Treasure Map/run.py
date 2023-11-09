#default map style
row1 = ["🥲","🥲","🥲"]
row2 = ["🥲","🥲","🥲"]
row3 = ["🥲","🥲","🥲"]

#arrange the map vertically
map = str(f"{row1}\n{row2}\n{row3}")

#print default map
print(map)

#input to put the x there
x_location = input("Enter the location in xy number format like \"23\" to put \"x\" there: ")

#format text to row and column
row = int(x_location[1])
column = int(x_location[0])

#check the input is valid and write the x on the position
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

#show the final map
map= str(f"{row1}\n{row2}\n{row3}")
print(map)







