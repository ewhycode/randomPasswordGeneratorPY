import random
import string

def generate_password(length=12):
    # Define character sets for password generation
    letters = string.ascii_letters
    digits = string.digits
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?`~" #add special characters for more complexity

    #concatenate
    allCharacters = letters + digits + special_chars

    #Password contains at least one of each character set
    password = [random.choice(letters),
                random.choice(digits),
                random.choice(special_chars)]

    #Generate remaining characters in random
    password += random.choices(allCharacters, k=length-3)

    #Shuffle password characters
    random.shuffle(password)

    # Convert password list to string
    return ''.join(password)

if __name__ == "__main__":
    password_length = int(input("Enter password length: "))
    generated_password = generate_password(password_length)
    print("Generated Password:", generated_password)

#generate
