def palindromes(num):
    temp = num
    rev = 0
    while num > 0:
        dig = num % 10
        rev = rev * 10 + dig
        num = num // 10
    if temp == rev:
        return True
    else:
        return False


ints_string = input().split(", ")

for i in ints_string:
    print(palindromes(int(i)))