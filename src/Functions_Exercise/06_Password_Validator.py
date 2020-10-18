def check_length(input_string):
    if 6 <= len(input_string) <= 10:
        return True
    else:
        return False


def check_chars(input_string):
    count = 0
    for s in input_string:
        if 48 <= ord(s) <= 57 or 65 <= ord(s) <= 90 or 97 <= ord(s) <= 122:
            count += 1
    if count == len(input_string):
        return True
    else:
        return False


def check_digits(input_string):
    count = 0
    for s in input_string:
        if s.isdigit():
            count += 1
    if count >= 2:
        return True
    else:
        return False


def check_password(input_string):
    if check_length(input_string) and check_chars(input_string) and check_digits(input_string):
        print("Password is valid")
    if not check_length(input_string):
        print("Password must be between 6 and 10 characters")
    if not check_chars(input_string):
        print("Password must consist only of letters and digits")
    if not check_digits(input_string):
        print("Password must have at least 2 digits")


input_data = input()

check_password(input_data)