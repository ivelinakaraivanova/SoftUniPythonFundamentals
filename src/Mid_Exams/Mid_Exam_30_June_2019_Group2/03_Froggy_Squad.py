frogs = input().split()


while True:
    input_command = input()
    command = input_command.split()[0]

    if command == "Print":
        way = input_command.split()[1]
        if way == "Normal":
            print(f"Frogs: {' '.join(frogs)}")
        elif way == "Reversed":
            reversed_frogs = list(reversed(frogs))
            print(f"Frogs: {' '.join(reversed_frogs)}")
        break

    elif command == "Join":
        name = input_command.split()[1]
        frogs.append(name)

    elif command == "Jump":
        name = input_command.split()[1]
        index = int(input_command.split()[2])
        if index in range(len(frogs)):
            frogs.insert(index, name)

    elif command == "Dive":
        index = int(input_command.split()[1])
        if index in range(len(frogs)):
            frogs.pop(index)

    elif command == "First":
        count = int(input_command.split()[1])
        if count in range(len(frogs)):
            first = frogs[:count]
            print(" ".join(first))
        else:
            print(" ".join(frogs))

    elif command == "Last":
        count = int(input_command.split()[1])
        if count in range(len(frogs)):
            last = frogs[-count:]
            print(" ".join(last))
        else:
            print(" ".join(frogs))
