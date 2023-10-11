import random
name = input("Enter the name with \",\": ")
name_list = name.split(", ")

position = random.randint(0,len(name_list) -1)

print(name_list[position]+" will pay the bill")