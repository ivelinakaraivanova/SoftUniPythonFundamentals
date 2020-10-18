n = int(input())

count = 0
is_balanced = True

for i in range(n):
    string = input()
    if string == "(":
        count += 1

    elif string == ")":
        count -= 1

    if count < 0 or count > 1:
        is_balanced = False

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")