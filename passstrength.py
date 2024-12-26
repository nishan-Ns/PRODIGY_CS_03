def check_password_strength(password):
  
    length = len(password) >= 8
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*(),.?\":{}|<>" for char in password)

    
    score = sum([length, has_upper, has_lower, has_digit, has_special])

    if score == 5:
        return "Strong"
    elif score >= 3:
        return "Moderate"
    else:
        return "Weak"


while True:
    password = input("\nEnter a password to check (or type 'exit' to quit): ")
    if password.lower() == 'exit':
        print("Exiting the program. Stay safe!")
        break

    strength = check_password_strength(password)
    print(f"Password Strength: {strength}")
