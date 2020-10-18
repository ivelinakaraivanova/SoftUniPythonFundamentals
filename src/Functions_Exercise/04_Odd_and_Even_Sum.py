def odd_even_sums(num):
    odd_sum = sum([int(d) for d in num if int(d) % 2 == 1])
    even_sum = sum([int(d) for d in num if int(d) % 2 == 0])
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = input()
print(odd_even_sums(number))
