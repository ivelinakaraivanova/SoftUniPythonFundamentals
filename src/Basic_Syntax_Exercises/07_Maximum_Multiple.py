divisor = int(input())
bound = int(input())
max_num = 1

for i in range(divisor, bound+1):
    if i % divisor == 0:
        if i > max_num:
            max_num = i

print(max_num)