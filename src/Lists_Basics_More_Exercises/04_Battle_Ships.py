n = int(input())

field = []

for i in range(n):
    split_row = list(map(int, input().split(" ")))
    field.append(split_row)

attacked = input().split(" ")
ships = 0
for item in attacked:
    row = int(item.split("-")[0])
    col = int(item.split("-")[1])
    if field[row][col] > 0:
        field[row][col] -= 1
        if field[row][col] == 0:
            ships += 1
print(ships)