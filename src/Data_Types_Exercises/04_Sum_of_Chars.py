n = int(input())

letter_sum = 0

for _ in range(n):
    letter = ord(input())
    letter_sum += letter

print(f"The sum equals: {letter_sum}")
