input_list = list(map(int, input().split(', ')))

boundary = 10
result_list = []

while len(input_list) > 0:
    group = list(filter(lambda x: x <= boundary, input_list))
    result_list.append((boundary, group))
    input_list = list(filter(lambda x: x > boundary, input_list))
    boundary += 10

for item in result_list:
    print(f"Group of {item[0]}'s: {item[1]}")

