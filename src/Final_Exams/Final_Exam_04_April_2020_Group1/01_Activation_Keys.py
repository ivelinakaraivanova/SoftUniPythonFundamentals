def contains(string, substring):
    if substring in string:
        return 1
    else:
        return -1


def flip(string, case, start, end):
    substr = string[start:end]
    if case == "Upper":
        substr = substr.upper()
    elif case == "Lower":
        substr = substr.lower()
    string = string[:start] + substr + string[end:]
    return string


def slice(string, start, end):
    string = string[:start] + string[end:]
    return string


activation_key = input()

while True:
    data = input()
    split_data = data.split(">>>")
    command = split_data[0]
    if command == "Generate":
        break

    if command == "Contains":
        substring = split_data[1]
        result = contains(activation_key, substring)
        if result == 1:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif command == "Flip":
        case = split_data[1]
        start_index = int(split_data[2])
        end_index = int(split_data[3])
        activation_key = flip(activation_key, case, start_index, end_index)
        print(activation_key)

    elif command == "Slice":
        start_index = int(split_data[1])
        end_index = int(split_data[2])
        activation_key = slice(activation_key, start_index, end_index)
        print(activation_key)

print(f"Your activation key is: {activation_key}")