import random
import string

def generate_password(length):
    #Define the character sets to be used for the password
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Create a combined character set
    characters = lowercase_letters + uppercase_letters + digits + special_chars

    # Generate the random password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Prompt the user to enter the desire password length
while True:
    password_length_str = input("Enter the desired password length")
    try:
        password_length = int(password_length_str)
        break
    except ValueError:
        print("Invalid input. Please enter a calid integer.")

# Generate and display the password
generated_password = generate_password(password_length)
print(f"Your generated password is: {generated_password}")