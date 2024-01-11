#ask user to generate password or not
#if yes, ask password length
#if no, exit program
#generate pw
#print password

import string
import random

characters = string.ascii_letters + string.digits + "!@$%^&*()"

def generatePassword():
    passwordLength = int(input("How long would you like your password? "))

    random.shuffle(characters)

    password = []

    for x in range(passwordLength):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("Do you want to generate a password? (Yes/No): ")

if option == "Yes":
    generatePassword
elif option == "No":
    print("Program terminated")
    quit()
else:
    print("Invalid input, input Yes/No")
    quit()