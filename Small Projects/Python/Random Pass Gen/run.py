import random
import string

ascii_letters = list(string.ascii_letters)
digits = list(string.digits)
punctuations = list(string.punctuation)

mix = [ascii_letters, digits, punctuations]

length = int(input("Enter the Password Length in numbers: "))

password = ""
i = []
for x in range(0,length):
    i = mix[random.randint(0,len(mix)-1)]
    password += i[random.randint(0,len(i)-1)]

print(f"your password is: {password}")