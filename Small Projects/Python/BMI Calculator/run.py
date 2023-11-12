from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Height", "Weight", "BMI", "Category"]

row = []
height = float(input("Enter Your Hight in Meters: "))
row.append(f"{height} M")
weight = float(input("Enter Your Weight in Kg: "))
row.append(f"{weight} Kg")

bmi = weight/height ** 2
bmi_text = "{:.2f}".format(bmi) 
row.append(bmi_text)
if bmi < 18.5 :
    print(f"Your Underweight and your BMI is {bmi_text}")
    row.append("Underweight")
elif  18.5 <= bmi <= 24.9:
    print(f"Your Normal and your BMI is {bmi_text}")
    row.append("Normal")
elif  25 <= bmi <= 29.9:
    print(f"Your Overweight and your BMI is {bmi_text}")
    row.append("Overweight")
elif  30 <= bmi <= 34.9:
    print(f"Your Obese and your BMI is {bmi_text}")
    row.append("Obese")
else:
    print(f"Your Extreamely Obese and your BMI is {bmi_text}")
    row.append("Extremely Obese")

table.add_row(row)

print(table)
