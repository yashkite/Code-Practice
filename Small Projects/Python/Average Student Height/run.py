student_hights = input("Enter Students hights with \",\": ").split(", ")

total_hight = 0
total_students = 0
for student in student_hights:
    total_hight += float(student)
    total_students += 1
Hight_Average = round(total_hight/total_students)
print(f"Total Student Hights Average is: {Hight_Average}" )

