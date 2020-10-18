import math


def find_distance_to_center(x, y):
    result = abs(math.sqrt((x**2) + (y**2)))
    return result


first_point_x = float(input())
first_point_y = float(input())
second_point_x = float(input())
second_point_y = float(input())

if find_distance_to_center(first_point_x, first_point_y) <= find_distance_to_center(second_point_x, second_point_y):
    print(f"({int(first_point_x)}, {int(first_point_y)})")
else:
    print(f"({int(second_point_x)}, {int(second_point_y)})")