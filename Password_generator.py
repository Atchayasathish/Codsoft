import random
import string

# Function to generate a random password
def generate_password(length):
    # Define character sets for different complexities
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Combine character sets based on complexity
    if length < 4:
        charset = lower_chars
    elif length < 8:
        charset = lower_chars + digits
    elif length < 12:
        charset = lower_chars + digits + upper_chars
    else:
        charset = lower_chars + digits + upper_chars + special_chars

    # Generate a random password using the selected character set
    password = ''.join(random.choice(charset) for _ in range(length))
    return password

# Main program
if __name__ == "__main__":
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 1:
            print("Invalid length. Please enter a positive number.")
        else:
            password = generate_password(length)
            print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")
