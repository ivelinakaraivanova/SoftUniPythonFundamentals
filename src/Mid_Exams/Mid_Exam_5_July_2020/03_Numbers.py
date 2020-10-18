numbers = list(map(int, input().split()))

average = sum(numbers) / len(numbers)

greater = [x for x in numbers if x > average]
sorted_greater = sorted(greater, reverse=True)

if len(sorted_greater) > 0:
    first = sorted_greater[:5]
    print(" ".join(list(map(str, first))))
else:
    print("No")
