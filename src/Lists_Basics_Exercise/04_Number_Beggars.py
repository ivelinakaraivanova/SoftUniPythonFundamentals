input_string = list(map(int, input().split(", ")))
beggars = int(input())

sum_list = []

for b in range(beggars):
    sum_b = 0
    for index in range(b, len(input_string), beggars):
        sum_b += input_string[index]
    sum_list.append(sum_b)

print(sum_list)