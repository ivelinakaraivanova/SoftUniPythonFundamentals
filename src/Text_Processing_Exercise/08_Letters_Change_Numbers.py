def upper_before(letter, number):
    result = number / (ord(letter) - 64)
    return result


def lower_before(letter, number):
    result = number * (ord(letter) - 96)
    return result


def upper_after(letter, number):
    result = number - (ord(letter) - 64)
    return result


def lower_after(letter, number):
    result = number + (ord(letter) - 96)
    return result


input_list = input().split()
result_list = []

for string in input_list:
    temp_str = ''
    letter_before = string[0]
    letter_after = string[-1]
    number = int(string[1:-1])

    if 65 <= ord(letter_before) <= 90:
        temp_str = upper_before(letter_before, number)
    elif 97 <= ord(letter_before) <= 122:
        temp_str = lower_before(letter_before, number)

    if 65 <= ord(letter_after) <= 90:
        temp_str = upper_after(letter_after, temp_str)
    elif 97 <= ord(letter_after) <= 122:
        temp_str = lower_after(letter_after, temp_str)

    result_list.append(temp_str)

print(f"{round(sum(result_list)+0.00000000001,2):.2f}")
