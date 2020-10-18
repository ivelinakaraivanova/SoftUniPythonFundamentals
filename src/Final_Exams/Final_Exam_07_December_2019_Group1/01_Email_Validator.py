def make(string, case):
    if case == "Upper":
        string = string.upper()
    elif case == "Lower":
        string = string.lower()
    return string


def get_username(string):
    if "@" in string:
        ind = string.index("@")
        return string[:ind]
    else:
        return -1


def encrypt(string):
    result = [str(ord(s)) for s in string]
    return result


email = input()

while True:
    data = input()
    if data == "Complete":
        break
    split_data = data.split()
    command = split_data[0]

    if command == "Make":
        case = split_data[1]
        email = make(email, case)
        print(email)

    elif command == "GetDomain":
        count = int(split_data[1])
        print(email[-count:])

    elif command == "GetUsername":
        result = get_username(email)
        if result == -1:
            print(f"The email {email} doesn't contain the @ symbol.")
        else:
            print(result)

    elif command == "Replace":
        char = split_data[1]
        email = email.replace(char, '-')
        print(email)

    elif command == "Encrypt":
        print(' '.join(encrypt(email)))
