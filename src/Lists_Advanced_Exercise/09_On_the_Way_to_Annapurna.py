def find_store_index(store):
    for element in store_items_list:
        if element[0] == store:
            return store_items_list.index(element)

    return -1


def add_store(store, items_list):
    index = find_store_index(store)
    if index >= 0:
        store_items_list[index][1] += items_list
    else:
        store_items_list.append([store, items_list])


def remove_store(store):
    index = find_store_index(store)
    if index >= 0:
        store_items_list.pop(index)


store_items_list = []
is_end = False

while not is_end:
    command = input()
    if command == "END":
        is_end = True
    else:
        token = command.split("->")
        action = token[0]
        store_name = token[1]

        if action == "Add":
            items = token[2].split(",")
            add_store(store_name, items)

        elif action == "Remove":
            remove_store(store_name)


store_items_sorted = sorted(store_items_list, key=lambda x: (len(x[1]), x[0]), reverse=True)

print("Stores list:")
for item in store_items_sorted:
    print(item[0])
    for element in item[1]:
        print(f"<<{element}>>")
