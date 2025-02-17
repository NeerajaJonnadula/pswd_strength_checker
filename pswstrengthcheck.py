import re

def evaluate_password(password):
    score = 0
    feedback = ""

    # Validate length
    if len(password) >= 8:
        score += 1
    else:
        feedback += "Password must be at least 8 characters long.\n"

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback += "Password should include at least one uppercase letter.\n"

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback += "Password should include at least one lowercase letter.\n"

    # Check for digits
    if re.search(r"\d", password):
        score += 1
    else:
        feedback += "Password should include at least one numeric digit.\n"

    # Check for special characters
    if re.search(r"[@$!%*?&]", password):
        score += 1
    else:
        feedback += "Password should include at least one special character (e.g., @, $, !, %, *, ?, &).\n"

    # Assess strength
    if score == 5:
        return "Password Strength: Strong ✅"
    elif score >= 3:
        return "Password Strength: Moderate ⚠\n" + feedback
    else:
        return "Password Strength: Weak ❌\n" + feedback

# User input
password_input = input("Please enter your password: ")
output = evaluate_password(password_input)
print("\n" + output)