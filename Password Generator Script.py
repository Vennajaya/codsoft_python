import random
import string

def generate_password(length):
    """Generates a random password of the specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    """Prompts the user for password length and generates a password."""
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    password = generate_password(length)
    print("Your generated password is:", password)

if __name__ == "__main__":
    main()
