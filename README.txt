PassChecker.io — Advanced Password Strength Validator

PassChecker.io is a Python-based password strength evaluator that helps users test, improve, and understand the quality of their passwords through multi-step validation, password generation, brute-force time estimation, and visual complexity analysis.

- Features

- Password Validation
Enforces length (14–24 characters)
Checks for uppercase, lowercase, digits, special characters
Detects whitespace and common/weak passwords

- Password Generator
Produces random secure passwords with mixed characters

- Brute-force Time Estimator
Simulates how long various attack tools (Hashcat, Hydra, Patator) might take to crack a password

- Complexity Analyzer + Score
Evaluates password structure and assigns a score out of 10
Visualizes key metrics using Pygal charts

- User Guidance
Educates users on what makes a strong password and why weak ones fail

- Password Evaluation Criteria -
Length: 14–24 characters
At least one uppercase and lowercase letter
At least one number
At least one special character
No whitespace
Not found in the common_passwords.txt list

The complexity analysis generates an interactive .svg chart showing:

Password length
Character set size
Breakdown of character types
Overall strength score (0–10)

Prerequisites
Python 3.8+
Pygal (pip install pygal)
(Optional) common_passwords.txt — Add your own dictionary file with weak passwords to enhance security
Running the Program
python3 your_file_name.py
Example Workflow
Run the program
Choose from the menu:
Option 1: Validate an existing password
Option 2: Generate a secure password
Option 3: Estimate brute-force cracking time
Option 4: Visualize password complexity
Option 5: Exit
Interact with prompts using secure getpass input
Review results and, if applicable, view generated visual_Chart.svg

- File Structure
├── your_script.py
├── common_passwords.txt
└── visual_Chart.svg       # Generated after complexity analysis

- Planned Improvements
GUI interface with PyQt or Tkinter
Entropy-based scoring
Heatmap-style visual feedback
Password policy customization

⚠️ Disclaimer:
This tool is educational and for offline use only. Do not enter actual passwords from your accounts.

License:
MIT License