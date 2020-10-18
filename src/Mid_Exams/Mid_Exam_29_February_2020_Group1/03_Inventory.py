collection = input().split(", ")

while True:
    command = input()
    if command == "Craft!":
        print(", ".join(collection))
        break
    else:
        split_command = command.split(" - ")
        action = split_command[0]
        if action == "Collect":
            item = split_command[1]
            if item not in collection:
                collection.append(item)
        elif action == "Drop":
            item = split_command[1]
            if item in collection:
                collection = [c for c in collection if c != item]
        elif action == "Combine Items":
            old_item = split_command[1].split(":")[0]
            new_item = split_command[1].split(":")[1]
            if old_item in collection:
                old_index = collection.index(old_item)
                new_index = old_index + 1
                collection.insert(new_index, new_item)
        elif action == "Renew":
            item = split_command[1]
            if item in collection:
                collection.remove(item)
                collection.append(item)
