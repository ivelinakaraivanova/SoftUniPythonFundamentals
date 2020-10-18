import math


def find_distance_to_center(x, y):
    result = abs(math.sqrt((x**2) + (y**2)))
    return result


def find_line(x1, y1, x2, y2):
    a = x2 - x1
    b = y2 - y1
    result = abs(math.sqrt((a**2) + (b**2)))
    return result


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x_3 = float(input())
y_3 = float(input())
x_4 = float(input())
y_4 = float(input())

if find_line(x_1, y_1, x_2, y_2) >= find_line(x_3, y_3, x_4, y_4):
    if find_distance_to_center(x_1, y_1) <= find_distance_to_center(x_2, y_2):
        print(f"({int(x_1)}, {int(y_1)})({int(x_2)}, {int(y_2)})")
    else:
        print(f"({int(x_2)}, {int(y_2)})({int(x_1)}, {int(y_1)})")
else:
    if find_distance_to_center(x_3, y_3) <= find_distance_to_center(x_4, y_4):
        print(f"({int(x_3)}, {int(y_3)})({int(x_4)}, {int(y_4)})")
    else:
        print(f"({int(x_4)}, {int(y_4)})({int(x_3)}, {int(y_3)})")