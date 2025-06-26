import random
import string

def generate_password(length):
    if length < 4:
        return "Password too short!"
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("🔐 Welcome to Random Password Generator!")
try:
    length = int(input("Enter the desired password length: "))
    result = generate_password(length)
    print("Your Random Password is:", result)
except ValueError:
    print("Please enter a valid number.")
