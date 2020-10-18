is_end = False
to_do_notes =[]

while not is_end:
    command = input()
    if command == "End":
        is_end = True
    else:
        importance = int(command.split("-")[0])
        value = command.split("-")[1]
        to_do_notes.append((importance, value))

result_list = []
for item in sorted(to_do_notes):
    if item != 0:
        result_list.insert(item[0], item[1])

print(result_list)