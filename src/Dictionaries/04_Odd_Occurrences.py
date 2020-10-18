words = input().split()

times = {}

for word in words:
    lower_word = word.lower()
    if lower_word in times:
        times[lower_word] += 1
    else:
        times[lower_word] = 1

odd_occurrences = []

for word in times:
    if times[word] % 2 == 1:
        odd_occurrences.append(word)

print(" ".join(odd_occurrences))