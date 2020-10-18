first_list = input().split(", ")
second_list = input().split(", ")

result_list =[]

for item in first_list:
    for item2 in second_list:
        if item in item2:
            if item not in result_list:
                result_list.append(item)

print(result_list)