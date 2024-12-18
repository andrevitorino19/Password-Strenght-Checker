import string

# Welcome message
print("Welcome to Andre's Password Strength Checker!\n")

# Ask the user to proceed
input("Do you really trust a Python script made by a newbie? Press Enter to proceed...\n")

# Prompt the user to enter a password
password = input("Enter the password: ")


# Check for character types
upper_case = any(c in string.ascii_uppercase for c in password)
lower_case = any(c in string.ascii_lowercase for c in password)
special = any(c in string.punctuation for c in password)
digits = any(c in string.digits for c in password)

# Count types of characters
types_of_characters = sum([upper_case, lower_case, special, digits])

# Password length
length = len(password)

# Initialize score
score = 0 

# Check if password is common
try:
    with open('common.txt', 'r') as f:
        common = f.read().splitlines()

    if password in common:
        print("\nPassword was found in a common list. Score: 0 / 7")
        exit()
except FileNotFoundError:
    print("\nError: 'common.txt' file not found. Please ensure the file is in the same directory.")
    exit()
# Add points based on password length
if length > 8:
    score += 1
if length > 12:
    score += 1
if length > 17:
    score += 1
if length > 25:
    score += 1


# Add points for character types
score += types_of_characters

# Print final score
# Print final score with messages
if score < 4:
    print(f"The password is quite weak! Score: {score} / 10")
elif score == 4:
    print(f"The password is ok! Score: {score} / 10")
elif 4 < score < 6:
    print(f"The password is pretty good! Score: {score} / 10")
elif score >= 6:
    print(f"The password is strong! Score: {score} / 10")
