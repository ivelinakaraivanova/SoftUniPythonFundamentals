'''
does not work completely - 80/100
'''


def create_even_odd_list(input_list):
    evens_list = [i for i in input_list if i % 2 == 0]
    odds_list = [i for i in input_list if i % 2 == 1]
    return evens_list, odds_list


def exchange(input_list, index):
    new_first_part = input_list[index+1:]
    new_second_part = input_list[:index+1]
    new_first_part.extend(new_second_part)
    return new_first_part


def max_even(input_list):
    index_me = None
    maxi = -999999999999999
    for index in range(len(input_list)):
        if input_list[index] % 2 == 0 and input_list[index] >= maxi:
            maxi = input_list[index]
            index_me = index
    return index_me


def max_odd(input_list):
    index_mo = None
    maxi = -999999999999999
    for index in range(len(input_list)):
        if input_list[index] % 2 == 1 and input_list[index] >= maxi:
            maxi = input_list[index]
            index_mo = index
    return index_mo


def min_even(input_list):
    index_mie = None
    mini = 99999999999999
    for index in range(len(input_list)):
        if (input_list[index] % 2 == 0) and (input_list[index] <= mini):
            mini = input_list[index]
            index_mie = index
    return index_mie


def min_odd(input_list):
    index_mio = None
    mini = 999999999999999
    for index in range(len(input_list)):
        if input_list[index] % 2 == 1 and input_list[index] <= mini:
            mini = input_list[index]
            index_mio = index
    return index_mio


def first_count_elements(input_list, count):
    if len(input_list) > 0:
        if 0 <= count <= len(input_list):
            first_count_list = input_list[:count]
            return first_count_list
        else:
            return input_list
    else:
        return []


def last_count_elements(input_list, count):
    if len(input_list) > 0:
        if 0 <= count <= len(input_list):
            last_count_list = input_list[(len(input_list) - count):]
            return last_count_list
        else:
            return input_list
    else:
        return []


input_data = list(map(int, input().split()))
evens, odds = create_even_odd_list(input_data)
is_end = False

while not is_end:
    command = input()
    if command == 'end':
        is_end = True
        print(input_data)
    else:
        split_command = command.split()
        if split_command[0] == "exchange":
            if 0 <= int(split_command[1]) <= len(input_data):
                input_data = exchange(input_data, int(split_command[1]))
                evens, odds = create_even_odd_list(input_data)
            else:
                print("Invalid index")
        elif split_command[0] == "max":
            if split_command[1] == "even":
                ma_e = max_even(input_data)
                if ma_e is None:
                    print("No matches")
                else:
                    print(ma_e)
            elif split_command[1] == "odd":
                ma_o = max_odd(input_data)
                if ma_o is None:
                    print("No matches")
                else:
                    print(ma_o)
        elif split_command[0] == "min":
            if split_command[1] == "even":
                mi_e = min_even(input_data)
                if mi_e is None:
                    print("No matches")
                else:
                    print(mi_e)
            elif split_command[1] == "odd":
                mi_o = min_odd(input_data)
                if mi_o is None:
                    print("No matches")
                else:
                    print(mi_o)
        elif split_command[0] == "first":
            if split_command[2] == "even":
                f_e = first_count_elements(evens, int(split_command[1]))
                if int(split_command[1]) > len(input_data):
                    print("Invalid count")
                else:
                    print(f_e)
            elif split_command[2] == "odd":
                f_o = first_count_elements(odds, int(split_command[1]))
                if int(split_command[1]) > len(input_data):
                    print("Invalid count")
                else:
                    print(f_o)
        elif split_command[0] == "last":
            if split_command[2] == "even":
                l_e = last_count_elements(evens, int(split_command[1]))
                if int(split_command[1]) > len(input_data):
                    print("Invalid count")
                else:
                    print(l_e)
            elif split_command[2] == "odd":
                l_o = last_count_elements(odds, int(split_command[1]))
                if int(split_command[1]) > len(input_data):
                    print("Invalid count")
                else:
                    print(l_o)
