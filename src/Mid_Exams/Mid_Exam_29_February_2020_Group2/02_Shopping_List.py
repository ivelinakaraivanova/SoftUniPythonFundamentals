groceries = input().split("!")

while True:
    input_line = input()
    if input_line == "Go Shopping!":
        break
    else:
        command = input_line.split()[0]
        item = input_line.split()[1]

        if command == "Urgent":
            if item not in groceries:
                groceries.insert(0, item)

        elif command == "Unnecessary":
            if item in groceries:
                groceries.remove(item)

        elif command == "Correct":
            new_item = input_line.split()[2]
            if item in groceries:
                index = groceries.index(item)
                groceries.remove(item)
                groceries.insert(index, new_item)

        elif command == "Rearrange":
            if item in groceries:
                groceries.remove(item)
                groceries.append(item)

print(", ".join(groceries))