text = input()

while True:
    data = input()
    if data == "Done":
        break
    split_data = data.split()
    command = split_data[0]

    if command == "Change":
        char = split_data[1]
        replacement = split_data[2]
        text = text.replace(char, replacement)
        print(text)

    elif command == "Includes":
        string = split_data[1]
        if string in text:
            print("True")
        else:
            print("False")

    elif command == "End":
        string = split_data[1]
        print('True' if text.endswith(string) else 'False')

    elif command == "Uppercase":
        text = text.upper()
        print(text)

    elif command == "FindIndex":
        char = split_data[1]
        print(text.find(char))

    elif command == "Cut":
        start_index = int(split_data[1])
        length = int(split_data[2])
        string = text[start_index:start_index+length]
        print(string)
