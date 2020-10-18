first = input()
second = input()
string = input()

total_sum = 0

for s in string:
    if ord(first) < ord(second):
        if ord(first) < ord(s) < ord(second):
            total_sum += ord(s)
    else:
        if ord(second) < ord(s) < ord(first):
            total_sum += ord(s)

print(total_sum)
