import re

# Password Strength Checker
def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        "Minimum length 8 characters": length_error,
        "At least one digit": digit_error,
        "At least one uppercase letter": uppercase_error,
        "At least one lowercase letter": lowercase_error,
        "At least one special symbol (!@#$%^&*(),.?\":{}|<>)": symbol_error,
    }

    if all(not v for v in errors.values()):
        return "Strong password"
    else:
        messages = [msg for msg, err in errors.items() if err]
        return "Weak password. Issues:\n- " + "\n- ".join(messages)

# Simple Caesar Cipher Encryption and Decryption
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Shift within alphabet, wrap around using modulo
            offset = 65 if char.isupper() else 97
            result += chr((ord(char) - offset + shift) % 26 + offset)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("----- Password Strength Checker -----")
    pwd = input("Enter password to check strength: ")
    print(check_password_strength(pwd))
    print()

    print("----- Simple Caesar Cipher -----")
    text = input("Enter text to encrypt: ")
    shift = int(input("Enter shift number (e.g., 3): "))
    encrypted = caesar_encrypt(text, shift)
    print(f"Encrypted text: {encrypted}")

    decrypted = caesar_decrypt(encrypted, shift)
    print(f"Decrypted text: {decrypted}")

if __name__ == "__main__":
    main()
