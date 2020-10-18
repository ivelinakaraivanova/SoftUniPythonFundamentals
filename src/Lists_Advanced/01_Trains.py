def add_people(input_list, number):
    input_list[-1] = input_list[-1] + number
    return input_list


def insert_people(input_list, index, number):
    input_list[index] = input_list[index]+number
    return input_list


def leave_people(input_list, index, number):
    input_list[index] = input_list[index] - number
    return input_list


wagons = int(input())
zero_list = [0] * wagons
is_end = False
result_list = zero_list

while not is_end:
    command = input()
    if command == "End":
        is_end = True
    else:
        action = command.split()[0]
        if action == "add":
            people = int(command.split()[1])
            result_list = add_people(result_list, people)
        elif action == "insert":
            index = int(command.split()[1])
            people = int(command.split()[2])
            result_list = insert_people(result_list, index, people)
        elif action == "leave":
            index = int(command.split()[1])
            people = int(command.split()[2])
            result_list = leave_people(result_list, index, people)

print(result_list)

