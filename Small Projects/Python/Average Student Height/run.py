student_heights = input("Enter Students heights with \",\": ").strip().split(", ")
student_heights =  [float(i) for i in student_heights]

heights_Average = round(sum(student_heights)/len(student_heights), 2)

print(f"Total Student heights Average is: {heights_Average} cm")
