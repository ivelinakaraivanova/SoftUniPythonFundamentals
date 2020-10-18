n = int(input())

int_list = []

for i in range(n):
    number = int(input())
    int_list.append(number)

command = input()

new_list = []
if command == "even":
    for number in int_list:
        if number % 2 == 0:
            new_list.append(number)
elif command == "odd":
    for number in int_list:
        if number % 2 == 1:
            new_list.append(number)
elif command == "negative":
    for number in int_list:
        if number < 0:
            new_list.append(number)
elif command == "positive":
    for number in int_list:
        if number >= 0:
            new_list.append(number)

print(new_list)