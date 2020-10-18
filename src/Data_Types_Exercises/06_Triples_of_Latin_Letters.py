n = int(input())

for letter1 in range(n):
    for letter2 in range(n):
        for letter3 in range(n):
            print(f"{chr(97+letter1)}{chr(97+letter2)}{chr(97+letter3)}")
