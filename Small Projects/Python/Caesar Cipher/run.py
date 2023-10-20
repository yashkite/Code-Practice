import string


list = list(string.ascii_lowercase) + list(string.ascii_lowercase)
exit = True



def encrypt(text_e, shift):
    encrypt_m = ""
    for x in text_e:
        index = list.index(x) + shift
        encrypt_m +=  list[index]
    print(f"Encrypted Messege is : {encrypt_m}")
def decrypt(text_d, shift):
    decrypt_m = ""
    for x in text_d:
        index = list.index(x) - shift
        decrypt_m +=  list[index]
    print(f"Encrypted Messege is : {decrypt_m}")


while exit :
    choice = int(input(
'''
1. Encrypt
2. Decrypt
3. Exit
Enter the choice: '''))

    match choice:
        case 1:
            text_e = input("Enter the messege to encrypt: ") 
            shift = int(input("Enter the Shift Number(0-25): "))
            encrypt(text_e, shift)
        case 2:
            text_d = input("Enter the messege to decrypt: ") 
            shift = int(input("Enter the Shift Number(0-25): "))
            decrypt(text_d, shift)
        case _:
            exit = False

