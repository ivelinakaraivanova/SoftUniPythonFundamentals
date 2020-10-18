input_list = list(map(int, input().split(", ")))

for item in input_list:
    if item == 0:
        input_list.remove(item)
        input_list.append(item)

print(input_list)