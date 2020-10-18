contacts = input().split()

while True:
    input_command = input()
    command = input_command.split()[0]

    if command == "Print":
        way = input_command.split()[1]
        if way == "Normal":
            print(f"Contacts: {' '.join(contacts)}")
        elif way == "Reversed":
            reversed_contacts = list(reversed(contacts))
            print(f"Contacts: {' '.join(reversed_contacts)}")
        break

    elif command == "Add":
        name = input_command.split()[1]
        index = int(input_command.split()[2])
        if name in contacts:
            if index in range(len(contacts)):
                contacts.insert(index, name)
        else:
            contacts.append(name)

    elif command == "Remove":
        index = int(input_command.split()[1])
        if index in range(len(contacts)):
            contacts.pop(index)

    elif command == "Export":
        start_index = int(input_command.split()[1])
        count = int(input_command.split()[2])
        if count in range(len(contacts)):
            print_list = contacts[start_index:start_index+count]
        else:
            print_list = contacts[start_index:]
        print(" ".join(print_list))
