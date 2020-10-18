def add_target(input_targets, index_number, value_number):
    if index_number in range(len(input_targets)):
        input_targets.insert(index_number, value_number)
        return input_targets
    return False


def shoot(input_list, index_value, power_value):
    if index_value in range(len(input_list)):
        input_list[index_value] -= power_value
        if input_list[index_value] <= 0:
            input_list.remove(input_list[index_value])


def strike(input_list, index_value, radius_value):
    start_index = index_value - radius_value
    stop_index = index_value + radius_value
    if (start_index in range(len(input_list))) and (stop_index in range(len(input_list))):
        input_list = input_list[:start_index] + input_list[stop_index+1:]
        return input_list
    return False


targets = list(map(int, input().split()))

while True:
    command = input()
    if command == "End":
        print(f"{'|'.join(list(map(str, targets)))}")
        break
    else:
        tokens = command.split()
        action = tokens[0]
        index = int(tokens[1])
        if action == "Shoot":
            power = int(tokens[2])
            shoot(targets, index, power)
        elif action == "Add":
            value = int(tokens[2])
            if add_target(targets, index, value):
                continue
            else:
                print("Invalid placement!")
        elif action == "Strike":
            radius = int(tokens[2])
            if strike(targets, index, radius):
                targets = strike(targets, index, radius)
            else:
                print("Strike missed!")
