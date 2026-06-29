def check_password_strength(password):
    if len(password) < 8:
        return "password too short"

    has_upper = False
    has_digit = False
    has_special = False
    special_chars = "!@#$%^&*()-_=+"

    for char in password:
        if char.isupper():
            has_upper = True
        if char.isdigit():
            has_digit = True
        if char in special_chars:
            has_special = True

    if not has_upper:
        return "Password is supposed to have at least 1 uppercase letter"
    if not has_digit:
        return "Password is supposed to have at least 1 digit"
    if not has_special:
        return "Password is supposed to have at least 1 special character"

    return f"Password '{password}' is solid"

user_password = input("Enter a password to check: ")
result = check_password_strength(user_password)
print(result)       