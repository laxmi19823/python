import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols, exclude_similar):
    similar_chars = 'il1Lo0O'
    characters = ''
    
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if exclude_similar:
        characters = ''.join(c for c in characters if c not in similar_chars)

    if not characters:
        return "Please select at least one character type!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_strength(length):
    if length < 6:
        return "Weak 🔴"
    elif length < 10:
        return "Moderate 🟡"
    else:
        return "Strong 🟢"

# User Input
print("🔐 Welcome to Laxmi's Personalized Password Generator 🔐")
name = input("Enter your name: ").capitalize()
print(f"\nHi {name}, let's customize your secure password!")

length = int(input("Enter desired password length: "))

# Feature toggles
use_upper = input("Include UPPERCASE letters? (y/n): ").lower() == 'y'
use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include numbers? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
exclude_similar = input("Exclude similar characters (like 'O' and '0')? (y/n): ").lower() == 'y'

# Generate Password
password = generate_password(length, use_upper, use_lower, use_digits, use_symbols, exclude_similar)
print(f"\n🧾 Password Strength: {password_strength(length)}")
print(f"🔑 Your personalized password: {password}")

