scores = input("Enter the Scores with \",\": ").split(", ")

highest = 0
for score in scores:
    if float(score) > highest:
        highest = float(score)

print(f"Highest score is: {highest}")