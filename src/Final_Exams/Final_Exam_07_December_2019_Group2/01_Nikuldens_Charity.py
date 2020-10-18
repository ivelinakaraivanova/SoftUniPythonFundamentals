def replace_char(string, curr_char, n_char):
    if curr_char in string:
        string = string.replace(curr_char, n_char)
    return string


def cut_char(string, start_ind, end_ind):
    if 0 <= start_ind < len(string) and 0 <= end_ind < len(string):
        string = string[:start_ind] + string[end_ind+1:]
        return string
    else:
        return -1


def make(string, case):
    if case == "Upper":
        return string.upper()
    elif case == "Lower":
        return string.lower()


def check(string, substr):
    if substr in string:
        return 1
    else:
        return -1


def sum_str(string, start_ind, end_ind):
    suma = 0
    if 0 <= start_ind < len(string) and 0 <= end_ind < len(string):
        substring = string[start_ind:end_ind+1]
        for s in substring:
            suma += ord(s)
        return suma
    else:
        return -1


text = input()

while True:
    data = input()
    if data == "Finish":
        break
    split_data = data.split()
    command = split_data[0]
    if command == "Replace":
        current_char = split_data[1]
        new_char = split_data[2]
        text = replace_char(text, current_char, new_char)
        print(text)

    elif command == "Cut":
        start_index = int(split_data[1])
        end_index = int(split_data[2])
        result = cut_char(text, start_index, end_index)
        if result == -1:
            print("Invalid indexes!")
        else:
            text = result
            print(text)

    elif command == "Make":
        case = split_data[1]
        text = make(text, case)
        print(text)

    elif command == "Check":
        substring = split_data[1]
        if check(text, substring) == 1:
            print(f"Message contains {substring}")
        else:
            print(f"Message doesn't contain {substring}")

    elif command == "Sum":
        start_index = int(split_data[1])
        end_index = int(split_data[2])
        result = sum_str(text, start_index, end_index)
        if result == -1:
            print("Invalid indexes!")
        else:
            print(result)
