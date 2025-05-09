
Password Strength Checker
A simple Python-based password strength checker that helps evaluate the strength of passwords based on multiple security criteria. It provides helpful suggestions to improve weak passwords and includes a password generator to create secure passwords automatically.

Features
Password Strength Evaluation:

Checks for:

Minimum password length of 8 characters.

Presence of lowercase letters.

Presence of uppercase letters.

Presence of digits.

Presence of special characters (!@#$%^&*() etc.)

Feedback & Suggestions:

Provides detailed suggestions for improving passwords that don't meet the required criteria.

Password Generator:

Automatically generates a strong password that meets the specified criteria.

Generates passwords with a mix of lowercase, uppercase, digits, and special characters.

Visible Password Input:

The script allows you to see the password as you type for ease of testing. (This is not recommended for real-world, production environments with sensitive data.)

Installation
Clone the repository:

git clone https://github.com/Rubalchoudhary21/password-strength-checker.git
cd password-strength-checker

Run the script:
The script works with Python 3.x and doesn't require any external libraries.

Simply run the script using Python:
python password_checker.py
(Optional) Install dependencies:

If you decide to extend the functionality and need additional packages in the future, you can install them using:
pip install -r requirements.txt
