first_number = int(input())
second_number = int(input())
third_number = int(input())


def find_the_smallest(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    else:
        return c


print(find_the_smallest(first_number, second_number, third_number))