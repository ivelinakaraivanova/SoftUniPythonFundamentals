text = input()

while True:
    data = input()
    if data == "Travel":
        break
    split_data = data.split(":")
    command = split_data[0]

    if command == "Add Stop":
        index = int(split_data[1])
        string = split_data[2]
        if 0 <= index < len(text):
            text = text[:index] + string + text[index:]

    elif command == "Remove Stop":
        start_index = int(split_data[1])
        end_index = int(split_data[2])
        if 0 <= start_index < len(text) and 0 <= end_index < len(text):
            text = text[:start_index] + text[end_index+1:]

    elif command == "Switch":
        old_string = split_data[1]
        new_string = split_data[2]
        if old_string in text:
            text = text.replace(old_string, new_string)

    print(text)

print(f"Ready for world tour! Planned stops: {text}")