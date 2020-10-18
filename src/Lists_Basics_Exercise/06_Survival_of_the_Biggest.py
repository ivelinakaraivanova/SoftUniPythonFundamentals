input_numbers = list(map(int, input().split(" ")))
n = int(input())

min_list = sorted(input_numbers)[:n]
result_list =[]

for item in input_numbers:
    if item not in min_list:
        result_list.append(item)

print(result_list)