data = list(input())

result_list = [data[0]]

for i in range(len(data)-1):
    if data[i+1] != data[i]:
        result_list.append(data[i+1])

print("".join(result_list))
