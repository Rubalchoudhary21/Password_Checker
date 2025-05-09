import re
import random
import string

def check_password_strength(password):
    strength = 0
    remarks = []

    # Criteria checks
    if len(password) >= 8:
        strength += 1
    else:
        remarks.append("Password should be at least 8 characters.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        remarks.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        remarks.append("Add uppercase letters.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        remarks.append("Include digits.")

    if re.search(r"[^\w\s]", password):
        strength += 1
    else:
        remarks.append("Add special characters (e.g. !@#$%).")

    levels = {
        5: "Very Strong 💪",
        4: "Strong 🙂",
        3: "Moderate 😐",
        2: "Weak 😟",
        1: "Very Weak 😧",
        0: "Extremely Weak 🚫"
    }

    return strength, levels[strength], remarks

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# === Main ===
if __name__ == "__main__":
    choice = input("Do you want to (1) check a password or (2) generate a strong one? [1/2]: ")

    if choice == "1":
        password = input("Enter your password: ")  # <-- Password is visible here
        score, level, feedback = check_password_strength(password)
        print(f"\nPassword Strength: {level}")
        if feedback:
            print("Suggestions:")
            for item in feedback:
                print(f"- {item}")
    elif choice == "2":
        pwd = generate_password()
        print(f"\nGenerated Password: {pwd}")
        score, level, _ = check_password_strength(pwd)
        print(f"Strength: {level}")
    else:
        print("Invalid choice.")
