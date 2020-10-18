split_first_version = list(map(int, input().split(".")))
first_number = split_first_version[0]
second_number = split_first_version[1]
third_number = split_first_version[2]

if 0 <= third_number < 9:
    third_number += 1
elif third_number == 9:
    third_number = 0
    if 0 <= second_number < 9:
        second_number += 1
    elif second_number == 9:
        second_number = 0
        first_number += 1

print(f"{first_number}.{second_number}.{third_number}")
