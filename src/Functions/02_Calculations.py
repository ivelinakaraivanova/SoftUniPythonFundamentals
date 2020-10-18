operator = input()
first = int(input())
second = int(input())


def calculator(num_a, num_b, operation):
    result = 0
    if operation == "multiply":
        result = num_a * num_b
    elif operation == 'divide':
        if num_b != 0:
            result = num_a // num_b
    elif operation == 'add':
        result = num_a + num_b
    elif operation == 'subtract':
        result = num_a - num_b
    return result


print(calculator(first, second, operator))
