first_number = int(input())
second_number = int(input())
third_number = int(input())


def sum_numbers(a, b):
    return a + b


def subtract(a, b, c):
    return sum_numbers(a, b) - c


def add_and_subtract(a, b, c):
    return subtract(a,b,c)


print(add_and_subtract(first_number, second_number, third_number))