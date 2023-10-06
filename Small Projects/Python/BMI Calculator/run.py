height = float(input("Enter Your Hight in Meters: "))
weight = float(input("Enter Your Weight in Kg: "))

bmi = weight/height ** 2
bmi_text = "{:.2f}".format(bmi) 

if bmi < 18.5 :
    print(f"Your Underweight and your BMI is {bmi_text}")
elif  18.5 <= bmi <= 24.9:
    print(f"Your Normal and your BMI is {bmi_text}")
elif  25 <= bmi <= 29.9:
    print(f"Your Overweight and your BMI is {bmi_text}")
elif  30 <= bmi <= 34.9:
    print(f"Your Obese and your BMI is {bmi_text}")
else:
    print(f"Your Extreamely Obese and your BMI is {bmi_text}")