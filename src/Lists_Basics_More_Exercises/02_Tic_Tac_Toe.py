first_row = list(map(int, input().split(" ")))
second_row = list(map(int, input().split(" ")))
third_row = list(map(int, input().split(" ")))

first_column = [first_row[0], second_row[0], third_row[0]]
second_column = [first_row[1], second_row[1], third_row[1]]
third_column = [first_row[2], second_row[2], third_row[2]]

left_diagonal = [first_row[0], second_row[1], third_row[2]]
right_diagonal = [first_row[2], second_row[1], third_row[0]]

combinations = [first_row, second_row, third_row,
                first_column, second_column, third_column,
                left_diagonal, right_diagonal]

printout = "Draw!"
for c in combinations:
    if 0 in c or (sum(c) != 3 and sum(c) != 6):
        continue
    if sum(c) == 3:
        printout = "First player won"
        break
    elif sum(c) == 6:
        printout = "Second player won"
        break

print(printout)