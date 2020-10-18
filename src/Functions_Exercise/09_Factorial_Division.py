def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


first_input = int(input())
second_input = int(input())
division = factorial(first_input) / factorial(second_input)
print(f"{division:.2f}")
