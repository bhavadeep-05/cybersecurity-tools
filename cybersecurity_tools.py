import random
import string

# Password Strength Checker
def check_password_strength(password):
    length = len(password)
    lower = any(c.islower() for c in password)
    upper = any(c.isupper() for c in password)
    digit = any(c.isdigit() for c in password)
    special = any(c in string.punctuation for c in password)

    score = 0
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if lower:
        score += 1
    if upper:
        score += 1
    if digit:
        score += 1
    if special:
        score += 1

    messages = []
    if length < 8:
        messages.append("Password is too short; try at least 8 characters.")
    if not lower:
        messages.append("Add lowercase letters.")
    if not upper:
        messages.append("Add uppercase letters.")
    if not digit:
        messages.append("Add digits.")
    if not special:
        messages.append("Add special characters (e.g., !, @, #).")

    if score <= 2:
        strength = "Very Weak"
    elif score == 3:
        strength = "Weak"
    elif score == 4:
        strength = "Moderate"
    elif score == 5:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return strength, messages

# Password Generator
def generate_password(length=12):
    if length < 6:
        print("Password length too short, setting to 6")
        length = 6

    all_chars = string.ascii_letters + string.digits + string.punctuation

    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]

    password += random.choices(all_chars, k=length - 4)

    random.shuffle(password)
    return ''.join(password)

# Simple Caesar Cipher Encryption
def encrypt(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            # Shift within A-Z or a-z
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

# Simple Caesar Cipher Decryption
def decrypt(text, shift=3):
    return encrypt(text, -shift)

# Main menu for all features
def main():
    while True:
        print("\n=== Cybersecurity Tool ===")
        print("1. Check password strength")
        print("2. Generate a strong password")
        print("3. Encrypt text")
        print("4. Decrypt text")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            pwd = input("Enter the password to check: ")
            strength, feedback = check_password_strength(pwd)
            print(f"\nPassword Strength: {strength}")
            if feedback:
                print("Suggestions to improve your password:")
                for msg in feedback:
                    print(f"- {msg}")

        elif choice == '2':
            try:
                length = int(input("Enter desired password length (minimum 6): "))
            except ValueError:
                print("Invalid input, using default length 12.")
                length = 12
            new_password = generate_password(length)
            print(f"\nGenerated password: {new_password}")

        elif choice == '3':
            text = input("Enter text to encrypt: ")
            shift = input("Enter shift number (default 3): ")
            shift = int(shift) if shift.isdigit() else 3
            encrypted = encrypt(text, shift)
            print(f"Encrypted text: {encrypted}")

        elif choice == '4':
            text = input("Enter text to decrypt: ")
            shift = input("Enter shift number (default 3): ")
            shift = int(shift) if shift.isdigit() else 3
            decrypted = decrypt(text, shift)
            print(f"Decrypted text: {decrypted}")

        elif choice == '5':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 5.")

if __name__ == "__main__":
    main()
