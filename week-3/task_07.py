
def check_length(password, min_length=8):
    if len(password) >= min_length:
        return True
    else:
        return False


def check_uppercase(password):
    for character in password:
        if character >= "A" and character <= "Z":
            return True

    return False


def check_lowercase(password):
    for character in password:
        if character >= "a" and character <= "z":
            return True

    return False


def check_digit(password):
    for character in password:
        if character >= "0" and character <= "9":
            return True

    return False


def check_special_character(password):
    special_characters = "!@#$%^&*()-_+=?"

    for character in password:
        if character in special_characters:
            return True

    return False


def analyze_password(password, min_length=8):
    report = {
        "minimum_length": check_length(password, min_length),
        "uppercase": check_uppercase(password),
        "lowercase": check_lowercase(password),
        "digit": check_digit(password),
        "special_character": check_special_character(password)
    }

    return report


# Test fictional passwords

passwords = [
    "hello",
    "HELLO123",
    "Hello123",
    "hello@123",
    "Strong@2026"
]

for password in passwords:
    print("\nPassword:", password)

    report = analyze_password(password)

    passed = 0
    failed = 0

    for requirement in report:
        if report[requirement] == True:
            print(requirement, ": PASS")
            passed = passed + 1
        else:
            print(requirement, ": FAIL")
            failed = failed + 1

    print("Passed:", passed)
    print("Failed:", failed)

    if failed == 0:
        print("Password meets all requirements.")
    else:
        print("Password does not meet all requirements.")
