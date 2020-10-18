gifts = input().split(" ")
is_no_money = False
while not is_no_money:
    command = input()
    if command == "No Money":
        is_no_money = True
    else:
        split_command = command.split(" ")
        action = split_command[0]
        gift = split_command[1]
        index = None
        if len(split_command) > 2:
            index = int(split_command[2])
        if action == "OutOfStock":
            for i, element in enumerate(gifts):
                if element == gift:
                    gifts[i] = "None"
        elif action == "Required":
            if 0<= index < len(gifts):
                gifts[index] = gift
        elif action == "JustInCase":
            gifts[-1] = gift

print(" ".join([i for i in gifts if i != "None"]))