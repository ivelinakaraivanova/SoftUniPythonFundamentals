string = input()

for index in range(0, len(string)*2, 2):
    string = string[:index] + string[index] + string[index:]
print(string)

"""
doubled_string = ""
for symbol in string:
    doubled_string += symbol*2
"""
