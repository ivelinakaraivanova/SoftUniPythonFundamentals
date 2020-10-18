def data_type(data_type, data_input):
    result = None
    if data_type == "int":
        result = int(data_input) * 2
    elif data_type == "real":
        result = f"{float(data_input) * 1.5:.2f}"
    elif data_type == "string":
        result = '$' + data_input + '$'
    return result


first_input = input()
second_input = input()

print(data_type(first_input, second_input))

"""
def is_float(s):
    result = False
    if s.count(".") == 1:
        if s.replace(".", "").isdigit():
            result = True
    return result


data = input()

if data.isnumeric():
    print(int(data) * 2)
elif is_float(data):
    print(f"{float(data)*1.5:.2f}")
elif isinstance(data, str):
    print('$'+data+'$')
"""