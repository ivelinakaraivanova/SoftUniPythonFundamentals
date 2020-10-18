n = int(input())

for i in range(1, n+1):
    digits_sum = 0
    digits = i
    while digits > 0:
        digits_sum += digits % 10
        digits = int(digits / 10)
    if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")

"""
for i in range(1, n+1):
    sum_of_digits = 0
    for c in str(i):
        sum_of_digits += int(c)
    is_special = sum_of_digits in (5, 7, 11)
    print(f"{i} -> {is_special}")
"""