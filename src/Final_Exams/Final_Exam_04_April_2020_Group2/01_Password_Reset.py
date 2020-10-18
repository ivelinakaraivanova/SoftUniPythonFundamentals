def take_odd(string):
    result_string = ''
    for ind in range(len(string)):
        if ind % 2 == 1:
            result_string += string[ind]
    return result_string


def cut(string, ind, leng):
    string = string[:ind] + string[ind+leng:]
    return string


def substitute(string, substring, subst):
    if substring in string:
        string = string.replace(substring, subst)
        return string
    else:
        return -1


password = input()

while True:
    split_command = input().split()
    command = split_command[0]
    if command == "Done":
        break

    if command == "TakeOdd":
        password = take_odd(password)
        print(password)

    elif command == "Cut":
        index = int(split_command[1])
        length = int(split_command[2])
        password = cut(password, index, length)
        print(password)

    elif command == "Substitute":
        substr = split_command[1]
        substi = split_command[2]
        if substitute(password, substr, substi) == -1:
            print("Nothing to replace!")
        else:
            password = substitute(password, substr, substi)
            print(password)

print(f"Your password is: {password}")