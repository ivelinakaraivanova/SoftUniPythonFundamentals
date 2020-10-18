def find_name(string):
    start_index = string.index('@')
    stop_index = string.index('|')
    return string[start_index+1:stop_index]


def find_age(string):
    start_index = string.index('#')
    stop_index = string.index('*')
    return string[start_index+1:stop_index]


n = int(input())

for _ in range(n):
    data = input()
    name = find_name(data)
    age = find_age(data)
    print(f"{name} is {age} years old.")
