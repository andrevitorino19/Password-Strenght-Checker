# Password-Strenght-Checker Project
A Python script that analyzes password strength and checks against a common password list.

## Objective

The objective of this project is to build a simple Python script that evaluates password strength by analyzing its complexity and verifying it against a list of commonly used passwords.

## Skills Learned

- Reading and writing files in Python
- Using string manipulation to check character types
- Implementing control flow (conditions, loops)
- Handling user input and error exceptions
- Practicing with GitHub for version control and project management


## Features

- Checks for password length and complexity (uppercase, lowercase, digits, and special characters).
- Verifies if the password exists in a common password list (`common.txt`).
- Provides a password strength score out of 10.

## How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/password-strength-checker.git
   cd password-strength-checker
   
## Run the script:
```bash
python password_checker.py
```   

## Example Output
```bash
Welcome to Andre's Password Strength Checker!

Do you really trust a Python script made by a newbie? Press Enter to proceed...

Enter the password: My_Strong@Pass99

The password is strong! Score: 7 / 10
```

## Requirements
 - Python 3.x
 - common.txt file with a list of common passwords.

## File Structure
```bash
password-strength-checker/
│
├── password_checker.py   # The main Python script
├── common.txt            # List of common passwords
└── README.md             # Project documentation
```

## License

