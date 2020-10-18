username = input()

while True:
    data = input()
    if data == "Sign up":
        break
    split_data = data.split()
    command = split_data[0]

    if command == "Case":
        case = split_data[1]
        if case == "upper":
            username = username.upper()
        elif case == "lower":
            username = username.lower()
        print(username)

    elif command == "Reverse":
        start_index = int(split_data[1])
        end_index = int(split_data[2])
        if 0 <= start_index <= len(username) and 0 <= end_index <= len(username):
            substring = username[start_index:end_index+1]
            print(substring[::-1])

    elif command == "Cut":
        substring = split_data[1]
        if substring in username:
            username = username.replace(substring, '')
            print(username)
        else:
            print(f"The word {username} doesn't contain {substring}.")

    elif command == "Replace":
        char = split_data[1]
        username = username.replace(char, '*')
        print(username)

    elif command == "Check":
        char = split_data[1]
        if char in username:
            print("Valid")
        else:
            print(f"Your username must contain {char}.")
