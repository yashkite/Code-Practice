import random
import string


def generate_password(length, char_types):
    characters = []

    if "alphanumeric" in char_types:
        characters.extend(list(string.ascii_letters + string.digits))

    if "digit" in char_types:
        characters.extend(list(string.digits))

    if "punctuation" in char_types:
        characters.extend(list(string.punctuation))

    if not characters:
        print("Please select at least one character type.")
        return None

    password = "".join(random.choice(characters) for _ in range(length))
    return password


length = int(input("Enter the Password Length in numbers: "))

selected_char_types = []
while not selected_char_types:
    selected_char_types = input(
        "Select character types (alphanumeric, digit, punctuation) separated by commas: "
    ).split(",")
    selected_char_types = [s.strip().lower() for s in selected_char_types]

password = generate_password(length, selected_char_types)

if password:
    print(f"Your password is: {password}")
