Password Strength Checker
A simple Python-based password strength checker that evaluates the strength of a password based on various criteria, including length, character types, and more. It also includes a password generator for creating strong passwords and provides suggestions to improve weak passwords.

Features
Password Strength Evaluation: Checks the password for:

Minimum length of 8 characters.

Presence of lowercase letters.

Presence of uppercase letters.

Presence of digits.

Presence of special characters (!@#$%^&*() etc.)

Password Feedback & Suggestions: If the password does not meet the strength criteria, helpful suggestions are provided to improve it.

Password Generator: Automatically generates a random, strong password containing letters, digits, and special characters.

Visible Password Input: The script shows the password as you type, making it easier to test and adjust your password. (Not recommended for sensitive passwords in production environments.)

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/Rubalchoudhary21/password-strength-checker.git
cd password-strength-checker
Install the required dependencies (if any). This script only requires Python 3.x and built-in libraries:

bash
Copy
Edit
pip install -r requirements.txt  # Optional, if you add external libraries in future
Usage
Checking Password Strength
Run the script in your terminal, and choose option 1 to check the strength of an entered password.

bash
Copy
Edit
python password_checker.py
It will prompt you to enter a password, and then it will display the strength along with suggestions to improve it.

Generating a Strong Password
Run the script and choose option 2 to generate a strong password. The generated password will meet the following criteria:

Minimum 12 characters.

Includes uppercase, lowercase, digits, and special characters.

bash
Copy
Edit
python password_checker.py
Example Run:
css
Copy
Edit
Do you want to (1) check a password or (2) generate a strong one? [1/2]: 1
Enter your password: abc123

Password Strength: Weak 😟
Suggestions:
- Add uppercase letters.
- Add special characters (e.g. !@#$%).
- Password should be at least 8 characters.
Example Password Generation:
css
Copy
Edit
Do you want to (1) check a password or (2) generate a strong one? [1/2]: 2

Generated Password: A}cW9!d*B6q(
Strength: Very Strong 💪
