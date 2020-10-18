import re

pairs_pattern = r'(?P<sign>@|#)(?P<first>[A-Za-z]{3,})\1\1(?P<second>[A-Za-z]{3,})\1'

text = input()

matches = re.findall(pairs_pattern, text)
if len(matches) > 0:
    print(f"{len(matches)} word pairs found!")
else:
    print("No word pairs found!")

mirror_words = []

for match in matches:
    first = match[1]
    second = match[2]
    if first == second[::-1]:
        mirror_words.append(first + " <=> " + second)

if len(mirror_words) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(mirror_words))
