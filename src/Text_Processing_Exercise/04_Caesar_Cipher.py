input_string = input()
result_string = ''

for s in input_string:
    new_ord = ord(s) + 3
    new_sym = chr(new_ord)
    result_string += new_sym

print(result_string)
