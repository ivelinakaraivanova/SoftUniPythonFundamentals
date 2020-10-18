numbers_strings = input().split()

result_string = ''

result_list = sorted(numbers_strings, reverse=True)
for num in result_list:
    result_string += num

print(result_string)
