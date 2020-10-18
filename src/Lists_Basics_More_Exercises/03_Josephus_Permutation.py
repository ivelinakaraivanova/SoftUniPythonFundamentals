input_list = input().split(' ')
k = int(input())

new_list = []
curc = 1
index = 0

while input_list:
    if index >= len(input_list):
        index = 0
    if curc % k == 0:
        new_list.append(input_list.pop(index))
        index -= 1
    curc += 1
    index += 1

print(f"[{','.join(new_list)}]")