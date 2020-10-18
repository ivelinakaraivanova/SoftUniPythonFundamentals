factor = int(input())
count = int(input())

result_list = []

for i in range(1, count+1):
    result = i * factor
    result_list.append(result)

print(result_list)