import secrets
import string
import time

lowerLetters = string.ascii_lowercase
upperLetters = string.ascii_uppercase
numbers = string.digits
symbols = "!@#$%^&*()_+-=~`"

allCharacters = lowerLetters + upperLetters + numbers + symbols

print("Processing...")
time.sleep(2)
print("Done!")

password = ''.join(secrets.choice(allCharacters) for _ in range(12))
print("Your password is:", password)