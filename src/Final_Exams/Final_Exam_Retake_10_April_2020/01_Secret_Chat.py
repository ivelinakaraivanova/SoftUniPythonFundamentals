def insert_space(string, index):
    string = string[:index] + ' ' + string[index:]
    return string


def reverse(string, substring):
    sub_index = string.find(substring)
    if sub_index == -1:
        result = sub_index
    else:
        result = string[:sub_index] + string[sub_index+len(substring):] + substring[::-1]
    return result


def change_all(string, substring, replacement):
    string = string.replace(substring, replacement)
    return string


message = input()

while True:
    command_line = input()
    if command_line == "Reveal":
        break
    split_command = command_line.split(":|:")
    command = split_command[0]

    if command == "InsertSpace":
        index = int(split_command[1])
        message = insert_space(message, index)
        print(message)

    elif command == "Reverse":
        substr = split_command[1]
        res_reverse = reverse(message, substr)
        if res_reverse == -1:
            print("error")
        else:
            message = res_reverse
            print(message)

    elif command == "ChangeAll":
        substr = split_command[1]
        replstr = split_command[2]
        message = change_all(message, substr, replstr)
        print(message)


print(f"You have a new text message: {message}")
