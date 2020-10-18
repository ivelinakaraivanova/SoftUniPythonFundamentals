def list_digits(string):
    return [int(s) for s in string if s.isdigit()]


def list_non_digits(string):
    return [s for s in string if not s.isdigit()]


def get_take_list(data_list):
    return [data_list[t] for t in range(len(data_list)) if t % 2 == 0]


def get_skip_list(data_list):
    return [data_list[t] for t in range(len(data_list)) if t % 2 != 0]


input_string = input()
non_numbers = list_non_digits(input_string)
non_numbers_string = "".join(non_numbers)
numbers = list_digits(input_string)
take_list = get_take_list(numbers)
skip_list = get_skip_list(numbers)
result_string = ""

for i in range(len(take_list)):
    take = non_numbers_string[i:take_list[i]]
    result_string += take
    non_numbers_string = non_numbers_string[take_list[i]:]


print(non_numbers_string)
print(result_string)
