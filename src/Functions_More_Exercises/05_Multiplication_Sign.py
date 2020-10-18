def sign(n, m):
    if (n > 0 and m > 0) or (n < 0 and m < 0):
        return 1
    elif (n > 0 and m < 0) or (n < 0 and m > 0):
        return -1
    elif n == 0 or m == 0:
        return 0


number_1 = int(input())
number_2 = int(input())
number_3 = int(input())

result = sign(sign(number_1, number_2), number_3)

if result == 1:
    print("positive")
elif result == -1:
    print("negative")
else:
    print("zero")